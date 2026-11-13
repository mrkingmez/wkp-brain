#!/usr/bin/env python3
"""Winter Wolf's Den weekly shorts scheduler (local replacement for the Apps Script app).

Same rules as the app: 31 heatmap slots, weekly quota, best score in the hottest slot,
stagger YouTube +0 / Instagram +45 / Facebook +90 minutes, YouTube one a day.
Times are America/New_York. Posts go straight to the Opus API, no approval click.

Key: environment variable OPUS_API_KEY (user scope). Never put it in a file or in chat.

PLAN MODE (added 2026-11-12, Zac's locked cadence): --plan-csv FILE posts exactly the rows in the CSV
(date,time_et,platform,clip_id,title), no SLOTS table, no quota, no +45/+90 stagger. The 31-slot table below is the
OLD logic, kept only for the legacy mode. Backup of the original: schedule_week.py.orig-2026-11-11.
  python schedule_week.py PROJECT_ID --copy EP120-approved-copy.json --plan-csv plan-input.csv --plan-out plan-v2.csv

Usage (dry run is the default, nothing is posted):
  python schedule_week.py PROJECT_ID --copy EP119-approved-copy.json --start 2026-11-12
  python schedule_week.py PROJECT_ID --copy ... --start ... --go        # really schedule
  python schedule_week.py PROJECT_ID --cancel-all --go                  # cancel what this script scheduled
  python schedule_week.py PROJECT_ID --show-log
"""
import argparse, csv, json, os, sys, time, urllib.request, urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

BASE = "https://api.opus.pro"
HERE = Path(__file__).resolve().parent
LOGDIR = HERE / "schedule-log"
ET = ZoneInfo("America/New_York")

ACCOUNTS = {
    "youtube":   {"postAccountId": "6a10fa722ae42657e2924bbf", "subAccountId": "UC2BmJmKYi9JozKblfJ_jHsQ"},
    "instagram": {"postAccountId": "69a0f3f44df77d215ab34169", "subAccountId": "17841480730167044"},
    "facebook":  {"postAccountId": "67cd99083a9f32906cd49897", "subAccountId": "104052046075172"},
}
DELAY = {"youtube": 0, "instagram": 45, "facebook": 90}

# Same 31 slots and quota as the app (day: 0=Sunday ... 6=Saturday). Do not change without Zac.
SLOTS = [
    (0,18,1),(5,18,1),(6,18,1),(1,19,1),(0,20,1),(5,20,1),(6,20,1),(1,12,1),
    (0,15,2),(0,12,2),(5,15,2),(5,12,2),(6,15,2),(6,12,2),(2,18,2),(2,20,2),(1,17,2),(3,18,2),
    (2,15,3),(2,12,3),(0,9,3),(5,9,3),(6,9,3),(1,9,3),(3,12,3),(4,18,3),
    (2,9,4),(0,7,4),(5,7,4),(6,7,4),(3,15,4),
]
QUOTA = {0: 6, 1: 4, 2: 5, 3: 3, 4: 1, 5: 6, 6: 6}


def get_key():
    k = os.environ.get("OPUS_API_KEY")
    if not k and sys.platform == "win32":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as h:
                k = winreg.QueryValueEx(h, "OPUS_API_KEY")[0]
        except OSError:
            k = None
    if not k:
        sys.exit("OPUS_API_KEY is not set. Add it as a user environment variable and restart the session.")
    return k


def api(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(BASE + path, data=data, method=method,
                                 headers={"Authorization": "Bearer " + get_key(), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            txt = r.read().decode() or "{}"
            return r.status, json.loads(txt)
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.read().decode()[:300]}


def get_clips(project):
    code, data = api("GET", f"/api/exportable-clips?q=findByProjectId&projectId={project}&pageSize=50")
    if code != 200:
        sys.exit(f"Could not load clips (API {code}): {data}")
    raw = data if isinstance(data, list) else data.get("data", [])
    clips = [{"id": c.get("id"), "projectId": c.get("projectId") or project, "curationId": c.get("curationId"),
              "title": c.get("title") or "Untitled", "description": c.get("description") or "",
              "score": c.get("viralityScore") or c.get("score") or 0,
              "duration": round(c["durationMs"] / 1000) if c.get("durationMs") else 0} for c in raw]
    clips.sort(key=lambda c: -c["score"])
    return clips


def load_copy(path):
    if not path:
        return {}
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    out = {}
    for x in (d if isinstance(d, list) else d.get("clips", [])):
        for k in (x.get("id"), x.get("curationId")):
            if k:
                out[k] = x
    return out


def build_slots(start):
    """start = a Thursday (date). Returns slot dicts with an ET date."""
    q = dict(QUOTA)
    slots = []
    for day, hour, tier in SLOTS:
        if q[day] > 0:
            q[day] -= 1
            slots.append({"day": day, "hour": hour, "tier": tier})
    sdow = (start.weekday() + 1) % 7  # python Mon=0 -> JS Sun=0
    for s in slots:
        s["date"] = start + timedelta(days=(s["day"] - sdow + 7) % 7)
    return slots


def plan(clips, copy, start, spoilers_late, yt_one_a_day, platforms, require_copy):
    slots = build_slots(start)
    chosen = [c for c in clips if (c["id"] in copy or c["curationId"] in copy)] if require_copy else list(clips)
    for c in chosen:
        c["copy"] = copy.get(c["id"]) or copy.get(c["curationId"])
    slots_by_time = sorted(slots, key=lambda s: (s["date"], s["hour"]))
    assign = {}
    pool = list(slots)  # hottest first (list order)
    spoilers = [c for c in chosen if c["copy"] and c["copy"].get("spoiler")] if spoilers_late else []
    if spoilers:
        late = slots_by_time[-len(spoilers):]
        for c, s in zip(sorted(spoilers, key=lambda c: -c["score"]), sorted(late, key=lambda s: (s["tier"], s["date"], s["hour"]))):
            assign[c["id"]] = s
            pool.remove(s)
    rest = [c for c in chosen if c["id"] not in assign]
    for c, s in zip(rest, pool):
        assign[c["id"]] = s
    # YouTube one a day: best score per day
    best = {}
    for c in chosen:
        s = assign.get(c["id"])
        if s and (s["date"] not in best or c["score"] > best[s["date"]]["score"]):
            best[s["date"]] = c
    posts = []
    for c in chosen:
        s = assign.get(c["id"])
        if not s:
            continue
        for plat in platforms:
            if plat == "youtube" and yt_one_a_day and best[s["date"]]["id"] != c["id"]:
                continue
            when = datetime(s["date"].year, s["date"].month, s["date"].day, s["hour"], 0, tzinfo=ET) + timedelta(minutes=DELAY[plat])
            title, desc = text_for(c, plat)
            posts.append({"clip": c, "platform": plat, "when": when, "title": title, "desc": desc})
    posts.sort(key=lambda p: (p["when"], p["platform"]))
    return posts, len(chosen), len(assign)


def plan_from_csv(path, clips, copy, require_copy):
    """Explicit plan mode (added 2026-11-12). Reads exact posts from a CSV instead of the SLOTS table.
    Columns: date (YYYY-MM-DD), time_et (HH:MM, 24h, America/New_York), platform, clip_id (Opus curationId), title (ignored,
    for humans; the posted title comes from the approved copy). No stagger, no quota: each row is one post at that minute."""
    by_id = {}
    for c in clips:
        by_id[c["id"]] = c
        if c["curationId"]:
            by_id[c["curationId"]] = c
    posts, problems = [], []
    with open(path, newline="", encoding="utf-8") as f:
        for n, r in enumerate(csv.DictReader(f), start=2):
            plat = (r.get("platform") or "").strip().lower()
            cid = (r.get("clip_id") or "").strip()
            if plat not in ACCOUNTS:
                problems.append(f"row {n}: unknown platform {plat!r}"); continue
            c = by_id.get(cid)
            if not c:
                problems.append(f"row {n}: clip id {cid!r} not in this Opus project"); continue
            c = dict(c)
            c["copy"] = copy.get(c["id"]) or copy.get(c["curationId"])
            if require_copy and not c["copy"]:
                problems.append(f"row {n}: clip {cid} has no approved copy"); continue
            try:
                when = datetime.strptime(f"{r['date'].strip()} {r['time_et'].strip()}", "%Y-%m-%d %H:%M").replace(tzinfo=ET)
            except (ValueError, KeyError):
                problems.append(f"row {n}: bad date or time_et"); continue
            title, desc = text_for(c, plat)
            posts.append({"clip": c, "platform": plat, "when": when, "title": title, "desc": desc})
    seen, yt_days = set(), {}
    for p in posts:
        k = (p["clip"]["curationId"], p["platform"])
        if k in seen:
            problems.append(f"duplicate post {k}")
        seen.add(k)
        if p["platform"] == "youtube":
            d = p["when"].date()
            yt_days[d] = yt_days.get(d, 0) + 1
    for d, n in yt_days.items():
        if n > 1:
            problems.append(f"{n} YouTube posts on {d} (rule is one a day)")
    posts.sort(key=lambda p: (p["when"], p["platform"]))
    return posts, problems


def text_for(c, plat):
    cp = c.get("copy")
    if cp:
        pc = cp.get(plat) or {}
        title = pc.get("title") or cp.get("title") or c["title"]
        desc = pc.get("description") or cp.get("description") or title
    else:
        title = c["title"]
        desc = (c["description"] or title) + "\n\n#WinterWolfsDen"
    if plat == "youtube" and len(title) > 100:
        title = title[:97] + "..."
    return title, desc


def logpath(project):
    LOGDIR.mkdir(exist_ok=True)
    return LOGDIR / f"{project}.json"


def read_log(project):
    p = logpath(project)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else []


def write_log(project, items):
    logpath(project).write_text(json.dumps(items, indent=1), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--copy", help="approved copy JSON")
    ap.add_argument("--start", help="Thursday that starts the week, YYYY-MM-DD (ET)")
    ap.add_argument("--platforms", default="youtube,instagram,facebook")
    ap.add_argument("--go", action="store_true", help="actually post/cancel. Without it nothing happens.")
    ap.add_argument("--allow-opus-copy", action="store_true", help="also schedule clips with no approved copy")
    ap.add_argument("--no-spoilers-late", action="store_true")
    ap.add_argument("--no-yt-one-a-day", action="store_true")
    ap.add_argument("--plan-csv", help="EXPLICIT PLAN MODE: CSV of exact posts (date,time_et,platform,clip_id,title). "
                                       "Bypasses the SLOTS table, quota and the +45/+90 stagger. --start is not needed.")
    ap.add_argument("--plan-out", help="where plan mode saves the checked plan CSV (default plan-PROJECT-planmode.csv)")
    ap.add_argument("--cancel-all", action="store_true")
    ap.add_argument("--show-log", action="store_true")
    a = ap.parse_args()

    if a.show_log:
        for i in read_log(a.project):
            print(i)
        return
    if a.cancel_all:
        items = read_log(a.project)
        print(f"{len(items)} posts in the local log for {a.project}.")
        if not a.go:
            print("Dry run. Add --go to cancel them.")
            return
        keep = []
        for i in items:
            code, r = api("DELETE", f"/api/publish-schedules/{i['s']}")
            ok = code in (200, 204, 404)
            print(("OK   " if ok else "FAIL ") + i["s"], code)
            if not ok:
                keep.append(i)
            time.sleep(0.2)
        write_log(a.project, keep)
        return

    platforms = [p.strip() for p in a.platforms.split(",") if p.strip()]
    clips = get_clips(a.project)
    copy = load_copy(a.copy)
    if a.plan_csv:
        posts, problems = plan_from_csv(a.plan_csv, clips, copy, not a.allow_opus_copy)
        for pr in problems:
            print("PROBLEM:", pr)
        if problems and a.go:
            sys.exit("Plan has problems. Fix the CSV before --go.")
        nclips = len({p["clip"]["curationId"] for p in posts})
        nplaced = nclips
    else:
        if not a.start:
            sys.exit("Give --start with the Thursday that starts the week (or use --plan-csv).")
        start = datetime.strptime(a.start, "%Y-%m-%d").date()
        if start.weekday() != 3:
            sys.exit(f"{a.start} is not a Thursday.")
        posts, nclips, nplaced = plan(clips, copy, start, not a.no_spoilers_late, not a.no_yt_one_a_day,
                                      platforms, not a.allow_opus_copy)
    now = datetime.now(ET)
    logged = {(i["c"], i["p"]) for i in read_log(a.project)}
    print(f"Project {a.project}: {len(clips)} clips from Opus, {nclips} with approved copy, {nplaced} placed in slots.")
    unmatched = [k for k in {x for x in copy if len(x) <= 12} if k not in {c["id"] for c in clips} | {c["curationId"] for c in clips}]
    if unmatched:
        print("Approved-copy ids not found in this project:", unmatched)
    rows, todo = [], []
    for p in posts:
        past = p["when"] <= now
        dup = (p["clip"]["curationId"], p["platform"]) in logged
        state = "SKIP past" if past else ("SKIP already scheduled" if dup else "plan")
        rows.append([p["when"].strftime("%a %Y-%m-%d %H:%M ET"), p["platform"], p["clip"]["score"],
                     "spoiler" if (p["clip"].get("copy") or {}).get("spoiler") else "", p["title"], state])
        if state == "plan":
            todo.append(p)
    for r in rows:
        print(" | ".join(str(x) for x in r))
    if a.plan_csv:
        out = Path(a.plan_out) if a.plan_out else HERE / f"plan-{a.project}-planmode.csv"
        prow = [[p["when"].strftime("%Y-%m-%d"), p["when"].strftime("%H:%M"), p["platform"], p["clip"]["curationId"],
                 p["title"], p["clip"]["score"], "spoiler" if (p["clip"].get("copy") or {}).get("spoiler") else "", r[-1]]
                for p, r in zip(posts, rows)]
        with open(out, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([["date", "time_et", "platform", "clip_id", "title", "score", "flag", "state"]] + prow)
    else:
        out = HERE / f"plan-{a.project}.csv"
        with open(out, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerows([["when", "platform", "score", "flag", "title", "state"]] + rows)
    print(f"\n{len(todo)} posts would be scheduled. Plan saved to {out}")
    if not a.go:
        print("DRY RUN. Nothing posted. Add --go to schedule.")
        return
    items = read_log(a.project)
    ok = 0
    for p in todo:
        acct = ACCOUNTS[p["platform"]]
        body = {"projectId": p["clip"]["projectId"], "clipId": p["clip"]["curationId"],
                "postAccountId": acct["postAccountId"], "subAccountId": acct["subAccountId"],
                "publishAt": p["when"].astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                "postDetail": {"title": p["title"], "mediaType": "video",
                               "custom": {"description": p["desc"], "privacy": "public"}}}
        for wait in (0, 20, 45, 90, 180):  # back off when Opus says too many requests (429)
            if wait:
                print(f"     rate limited, waiting {wait}s ...")
                time.sleep(wait)
            code, r = api("POST", "/api/publish-schedules", body)
            if code != 429:
                break
        sid = (r.get("data") or {}).get("scheduleId") if isinstance(r, dict) else None
        if code in (200, 201) and sid:
            ok += 1
            items.append({"s": sid, "c": p["clip"]["curationId"], "p": p["platform"],
                          "t": body["publishAt"], "title": p["title"]})
            write_log(a.project, items)
            print("OK   ", p["platform"], p["when"].strftime("%a %m-%d %H:%M"), p["title"][:50])
        else:
            print("FAIL ", p["platform"], p["when"].strftime("%a %m-%d %H:%M"), code, str(r)[:150])
        time.sleep(2.5)
    print(f"\nDone: {ok} of {len(todo)} scheduled. Log: {logpath(a.project)}")


if __name__ == "__main__":
    main()
