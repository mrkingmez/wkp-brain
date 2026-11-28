"""Keeps the day's NFL scores (and DFS entry results) on the dashboard (Zac 2026-11-22).
Persisted to scoreboard_day.json, keyed by game-day date (US Eastern). Written by the poller.
The day is replaced only when a game from a LATER day has started."""
import json
from datetime import datetime, timedelta, timezone

import config

PATH = config.DASHBOARD_DIR / "scoreboard_day.json"


def _et(dt):
    try:
        from zoneinfo import ZoneInfo
        return dt.astimezone(ZoneInfo("America/New_York"))
    except Exception:
        return dt.astimezone(timezone(timedelta(hours=-5)))


def _load():
    try:
        return json.loads(PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save(d):
    tmp = PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(d, indent=2), encoding="utf-8")
    tmp.replace(PATH)


def _row(e, on_card_abbrs):
    comp = e["competitions"][0]
    st = comp["status"]
    away = next(c for c in comp["competitors"] if c["homeAway"] == "away")
    home = next(c for c in comp["competitors"] if c["homeAway"] == "home")
    kick = datetime.fromisoformat(e["date"].replace("Z", "+00:00"))
    a, h = away["team"]["abbreviation"], home["team"]["abbreviation"]
    return {
        "id": e["id"], "kickoff": e["date"], "date": _et(kick).strftime("%Y-%m-%d"),
        "away_team": a, "away_score": away.get("score"), "home_team": h, "home_score": home.get("score"),
        "state": st["type"]["state"], "status": st["type"].get("description"),
        "detail": st["type"].get("shortDetail") or "",
        "on_card": a in on_card_abbrs or h in on_card_abbrs,
    }


def update_games(nfl_scoreboard, on_card_abbrs):
    d = _load()
    rows = []
    for e in (nfl_scoreboard or {}).get("events", []):
        try:
            rows.append(_row(e, on_card_abbrs))
        except Exception:
            continue
    started = [r["date"] for r in rows if r["state"] in ("in", "post")]
    if started:
        latest = max(started)
        if not d.get("date") or latest > d["date"]:
            d = {"date": latest, "games": {}}
        if latest == d["date"]:
            for r in rows:
                if r["date"] != d["date"]:
                    continue
                old = d["games"].get(r["id"])
                if old and old["state"] == "post" and r["state"] != "post":
                    continue  # a final stays final
                r["updated"] = datetime.now(timezone.utc).isoformat()
                d["games"][r["id"]] = r
            _save(d)
    return d


def update_dfs(live):
    """Persist each entry's total and the day's best from dfs_live. A final total is never replaced by a non-final one."""
    d = _load()
    if not d.get("date") or not live or not live.get("entries"):
        return d
    cur = (d.get("dfs") or {}).get("entries", {})
    for e in live["entries"]:
        old = cur.get(e["entry_id"])
        if old and old.get("all_final") and not e.get("all_final"):
            continue
        cur[e["entry_id"]] = {k: e.get(k) for k in ("entry_id", "contest_name", "entry_fee", "total", "all_final",
                                                    "dk_points", "dk_rank", "dk_total")}
    best = max(cur.values(), key=lambda x: x.get("total") or 0)
    d["dfs"] = {"week": live.get("week"), "entries": cur, "best_entry": best["entry_id"],
                "best_total": best.get("total"), "updated": datetime.now(timezone.utc).isoformat()}
    _save(d)
    return d


def panel():
    d = _load()
    games = sorted(d.get("games", {}).values(), key=lambda g: g["kickoff"])
    return {"date": d.get("date"), "games": games, "dfs": d.get("dfs")}
