"""Scout's state machine. Pure logic, no screen, no hardware.

Input: one JSON document shaped like the future D:\\WKP\\dashboard\\data\\ feed (see mock_data\\).
Output: a view dict the renderer draws: mood, overlays, one short line, and the reasons behind the mood.

Rules come from SCOUT-CHARACTER-BIBLE.md and CAPABILITIES.md:
  - Two steady moods: THRIVING and BURIED. Scout reflects what is true.
  - Concern, never blame. No guilt lines, no "come back or I'll be sad".
  - Special event (birthday, anniversary) layers ON TOP of the mood, never replaces it.
  - Event reactions (episode live, decision resolved) are "newest since last check", not live push.
  - End-of-day recap surfaces ONE real completed thing, the highest-effort one.

The bible does not define a middle mood. Between the two triggers Scout HOLDS its last mood
(hysteresis), so it does not flicker on one overdue task. Thresholds below are tunable, not canon.
"""
from __future__ import annotations

import datetime as dt

THRIVING, BURIED = "THRIVING", "BURIED"
SPECIAL_TAGS = {"birthday", "anniversary"}
BURIED_AT = 5.0            # load score at or above this: BURIED
CAL_REASONABLE = 5         # calendar items today before it counts as packed
OPEN_DECISIONS_OK = 3      # open decisions before they add load
REACTION_SECONDS = 8       # how long an event reaction stays up
RECAP_HOUR = 19            # evening recap starts at 7 PM local

LINES = {
    THRIVING: ["Board's clear. Good day to build.", "Nothing overdue. I'm glad we're here.",
               "All current. What are we making today?"],
    BURIED: ["Lot on the board today. I'm right here.", "{overdue} past due. Want to start with the first one?",
             "{blocked} blocked. One thing at a time.", "Heavy day. Pick one, I'll watch the rest."],
    # holding THRIVING while something is slipping: still up, but never claims the board is clear
    "THRIVING_HOLD": ["Mostly good. {overdue} slipped, easy catch.", "Good day overall. One thing's waiting on us."],
}
BANNED = ("let me down", "disappointed", "you forgot", "i'm sad", "come back", "lonely", "you failed", "neglect")


def _date(v, today: dt.date) -> dt.date | None:
    if v is None:
        return None
    if isinstance(v, int):
        return today + dt.timedelta(days=v)
    if v == "today":
        return today
    return dt.date.fromisoformat(str(v)[:10])


def assess(data: dict, today: dt.date) -> dict:
    """Count the four composite signals from the bible."""
    tasks = data.get("tasks", [])
    open_tasks = [t for t in tasks if t.get("status", "open") != "done"]
    overdue = [t for t in open_tasks
               if (d := _date(t.get("due", t.get("due_in_days")), today)) is not None and d < today]
    cal_today = [c for c in data.get("calendar", [])
                 if _date(c.get("date", c.get("days_from_today")), today) == today]
    blocked = list(data.get("ventures_blocked", []))
    decisions = int(data.get("open_decisions", 0))
    load = 2.0 * len(overdue) + 3.0 * len(blocked) + 0.5 * max(0, len(cal_today) - CAL_REASONABLE) \
        + 0.5 * max(0, decisions - OPEN_DECISIONS_OK)
    return dict(overdue=overdue, blocked=blocked, cal_today=cal_today, decisions=decisions, load=load,
                open_tasks=open_tasks)


def mood_for(a: dict, previous: str | None) -> str:
    clear = not a["overdue"] and not a["blocked"] and len(a["cal_today"]) <= CAL_REASONABLE
    if clear:
        return THRIVING
    if a["load"] >= BURIED_AT:
        return BURIED
    if previous in (THRIVING, BURIED):
        return previous                       # in the band between: hold, do not flicker
    return BURIED if a["load"] >= BURIED_AT / 2 else THRIVING


def reasons(a: dict) -> list[str]:
    r = []
    if a["overdue"]:
        r.append(f"{len(a['overdue'])} overdue: " + ", ".join(t["title"] for t in a["overdue"][:3]))
    if a["blocked"]:
        r.append(f"{len(a['blocked'])} venture(s) blocked: " + ", ".join(a["blocked"]))
    if len(a["cal_today"]) > CAL_REASONABLE:
        r.append(f"calendar packed: {len(a['cal_today'])} items today")
    if a["decisions"] > OPEN_DECISIONS_OK:
        r.append(f"{a['decisions']} decisions open")
    return r or ["nothing overdue, nothing blocked, calendar reasonable"]


def step(data: dict, memory: dict, now: dt.datetime, tick: int = 0) -> tuple[dict, dict]:
    """One check-in. Returns (view, new_memory). memory is plain JSON so it can live on flash later."""
    today = now.date()
    mem = dict(memory)
    a = assess(data, today)
    mood = mood_for(a, mem.get("mood"))
    if mood != mem.get("mood"):
        mem["mood_since"] = now.isoformat(timespec="seconds")
    mem["mood"] = mood
    overlays, line = [], None

    # special event layer: shown together with the mood, never instead of it
    specials = [c for c in a["cal_today"] if SPECIAL_TAGS & set(c.get("tags", []))]
    if specials:
        overlays.append("SPECIAL")

    # event reactions: only events Scout has not seen before
    seen = set(mem.get("seen_events", []))
    new = [e for e in data.get("events", []) if e.get("id") not in seen]
    if new:
        e = new[-1]
        mem["reaction"] = dict(id=e["id"], type=e.get("type"), title=e.get("title", ""),
                               until=(now + dt.timedelta(seconds=REACTION_SECONDS)).isoformat())
        mem["seen_events"] = sorted(seen | {x.get("id") for x in new})
    r = mem.get("reaction")
    if r and dt.datetime.fromisoformat(r["until"]) > now:
        overlays.append("REACTION")
        line = {"episode_live": "{t} is live!", "decision_resolved": "Decision closed: {t}."}.get(
            r["type"], "{t}").format(t=r["title"])
    elif r:
        mem.pop("reaction", None)

    # evening recap: one real thing, the biggest one finished today
    done_today = [t for t in data.get("tasks", []) if t.get("status") == "done"
                  and _date(t.get("done_on", t.get("done_in_days")), today) == today]
    if now.hour >= RECAP_HOUR and done_today and "REACTION" not in overlays:
        best = max(done_today, key=lambda t: (t.get("effort", 1), len(t.get("title", ""))))
        overlays.append("RECAP")
        line = f"Today you finished: {best['title']}."

    if line is None and specials:
        line = f"It's {specials[0]['title']}! Big day."
    if line is None:
        clear = not a["overdue"] and not a["blocked"]
        pool = LINES["THRIVING_HOLD"] if mood == THRIVING and not clear else LINES[mood]
        line = pool[(tick // 10) % len(pool)].format(overdue=len(a["overdue"]), blocked=len(a["blocked"]))
    assert not any(b in line.lower() for b in BANNED), f"guilt line slipped through: {line}"
    view = dict(mood=mood, overlays=overlays, line=line, reasons=reasons(a), load=round(a["load"], 1),
                counts=dict(overdue=len(a["overdue"]), blocked=len(a["blocked"]), calendar_today=len(a["cal_today"]),
                            decisions=a["decisions"], open_tasks=len(a["open_tasks"])))
    return view, mem
