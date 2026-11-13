"""cfb_snapshot.py -- save a dated snapshot of ESPN college-football (FBS)
lines, rankings, schedule and box-score leaders, then print a short diff
against the previous snapshot.

Why: ESPN deletes the odds block once a game goes final (see espn_games.py
docstring), so line history only exists if we save it ourselves.
Decision SW-2026-11-11-01.

Run (interpreter path is in LOCAL-PATHS.md, section Tools, "python"):
    <python> Fantasy-Football\\tracker\\cfb_snapshot.py
Options:
    --back N      days before today to include (default 5, picks up last
                  Saturday's finals for box-score leaders)
    --ahead N     days after today to include (default 5)
    --out DIR     output folder (default <repo>\\data\\cfb, or env CFB_DATA_DIR)
    --no-save     fetch and diff but do not write a file

Output file: <repo>\\data\\cfb\\YYYY-MM-DD-HHMM-cfb.json

NO INJURY DATA. This feed carries no injuries, starting QBs or depth
charts. Those must come from the conference availability reports (Big Ten,
SEC) read by hand and labeled SECONDARY.

Politeness: generic descriptive User-Agent (no personal details), 0.5 s
between calls, hard cap of 40 calls per run, in-run cache, no retries.
Same ESPN scoreboard call tracker\\espn_games.py makes (groups=80, one call
per calendar day because a date range returns HTTP 400).
"""
import argparse
import glob
import json
import os
import sys
import time
from datetime import datetime, timedelta

import requests

BASE = "https://site.api.espn.com/apis/site/v2/sports/football/college-football"
SCOREBOARD = BASE + "/scoreboard"
RANKINGS = BASE + "/rankings"
USER_AGENT = "cfb-snapshot-local/1.0 (personal research script, low volume)"
CALL_CAP = 40
DELAY_SECONDS = 0.5
MOVE_THRESHOLD = 1.0

NO_INJURY_HEADER = (
    "NO INJURY DATA: this snapshot carries no injuries, starting QBs or depth charts.\n"
    "Injury and QB status must come from the conference availability reports\n"
    "(Big Ten, SEC) read by hand and labeled SECONDARY."
)


def repo_root() -> str:
    # tracker\ -> Fantasy-Football\ -> repo root. No hardcoded drive path.
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def default_out_dir() -> str:
    return os.environ.get("CFB_DATA_DIR") or os.path.join(repo_root(), "data", "cfb")


class Fetcher:
    """HTTP GET JSON with in-run cache, call cap and delay. Never raises on
    network trouble: failures are recorded in self.failures."""

    def __init__(self, cap=CALL_CAP, delay=DELAY_SECONDS, session=None, sleep=time.sleep):
        self.cap, self.delay, self.sleep = cap, delay, sleep
        self.session = session or requests.Session()
        self.session.headers["User-Agent"] = USER_AGENT
        self.calls = 0
        self.cache = {}
        self.failures = []

    def get(self, url, params=None, what=""):
        key = (url, tuple(sorted((params or {}).items())))
        if key in self.cache:
            return self.cache[key]
        if self.calls >= self.cap:
            self.failures.append(f"{what or url}: not retrieved, call cap of {self.cap} reached")
            return None
        if self.calls:
            self.sleep(self.delay)
        self.calls += 1
        try:
            resp = self.session.get(url, params=params, timeout=20)
            resp.raise_for_status()
            data = resp.json()
        except Exception as exc:  # noqa: BLE001 - report, do not crash
            self.failures.append(f"{what or url}: not retrieved ({type(exc).__name__}: {exc})")
            data = None
        self.cache[key] = data
        return data


def _num(text):
    """'-13.5' -> -13.5, 'o54.5' -> 54.5, 'PK'/'EVEN' -> 0.0, junk -> None."""
    if text is None:
        return None
    s = str(text).strip().lower().lstrip("ou")
    if s in ("pk", "even", "ev"):
        return 0.0
    try:
        return float(s)
    except ValueError:
        return None


def _rank(comp):
    r = (comp.get("curatedRank") or {}).get("current")
    return r if isinstance(r, int) and 0 < r < 99 else None


def _leaders(comp):
    out = {}
    for cat in comp.get("leaders") or []:
        ls = cat.get("leaders") or []
        if ls:
            ath = ls[0].get("athlete") or {}
            out[cat.get("name", "?")] = {
                "player": ath.get("displayName") or ath.get("fullName"),
                "pos": (ath.get("position") or {}).get("abbreviation"),
                "line": ls[0].get("displayValue"),
            }
    return out


def parse_event(event):
    """One compact game dict. Spread sign follows the repo convention
    (espn_games.normalize_games): spread_home positive = home favored."""
    comp = event["competitions"][0]
    away = next(c for c in comp["competitors"] if c["homeAway"] == "away")
    home = next(c for c in comp["competitors"] if c["homeAway"] == "home")
    g = {
        "game_id": str(event["id"]),
        "kickoff": event.get("date"),
        "state": comp["status"]["type"]["state"],
        "away": away["team"].get("abbreviation"),
        "home": home["team"].get("abbreviation"),
        "away_name": away["team"].get("displayName"),
        "home_name": home["team"].get("displayName"),
        "away_rank": _rank(away),
        "home_rank": _rank(home),
        "away_score": away.get("score"),
        "home_score": home.get("score"),
        "odds": None,
        "leaders": {"away": _leaders(away), "home": _leaders(home)},
    }
    odds = comp.get("odds")
    if odds:
        o = odds[0]
        ps = o.get("pointSpread") or {}
        tot = o.get("total") or {}
        cur = _num(((ps.get("home") or {}).get("close") or {}).get("line"))
        opn = _num(((ps.get("home") or {}).get("open") or {}).get("line"))
        if cur is None and o.get("spread") is not None:
            cur = o["spread"]
        g["odds"] = {
            "provider": (o.get("provider") or {}).get("name"),
            "details": o.get("details"),
            "spread_home": None if cur is None else -cur,
            "open_spread_home": None if opn is None else -opn,
            "total": _num((tot.get("over", {}).get("close") or {}).get("line")) or o.get("overUnder"),
            "open_total": _num((tot.get("over", {}).get("open") or {}).get("line")),
        }
    return g


def parse_rankings(data):
    polls = []
    for r in (data or {}).get("rankings", []):
        if r.get("type") not in ("cfp", "ap", "usa"):
            continue
        polls.append({
            "poll": r.get("name"),
            "headline": r.get("shortHeadline") or r.get("headline"),
            "date": r.get("date"),
            "ranks": [
                {"rank": x.get("current"), "team": (x.get("team") or {}).get("abbreviation"),
                 "record": x.get("recordSummary")}
                for x in r.get("ranks", [])
            ],
        })
    return polls


def build_snapshot(fetcher, today, back, ahead, now=None):
    now = now or datetime.now()
    games, seen = [], set()
    for off in range(-back, ahead + 1):
        day = (today + timedelta(days=off)).strftime("%Y%m%d")
        data = fetcher.get(SCOREBOARD, {"groups": "80", "limit": 300, "dates": day}, f"scoreboard {day}")
        for e in (data or {}).get("events", []):
            if e["id"] in seen:
                continue
            seen.add(e["id"])
            try:
                games.append(parse_event(e))
            except (KeyError, StopIteration, IndexError) as exc:
                fetcher.failures.append(f"event {e.get('id')}: not parsed ({type(exc).__name__})")
    rk = fetcher.get(RANKINGS, None, "rankings")
    games.sort(key=lambda g: g["kickoff"] or "")
    return {
        "taken_at": now.strftime("%Y-%m-%d %H:%M"),
        "source": "ESPN site.api.espn.com college-football (unofficial, keyless)",
        "contains_injury_data": False,
        "injury_notice": NO_INJURY_HEADER.replace("\n", " "),
        "calls_made": fetcher.calls,
        "not_retrieved": list(fetcher.failures),
        "games": games,
        "rankings": parse_rankings(rk),
    }


# --------------------------------------------------------------------------- CFBD (added 2026-11-12)
# collegefootballdata.com, free tier 1,000 calls a month. This block uses 5 calls a run (calendar, lines, SP+, Elo,
# FPI). Two runs a week is about 45 calls a month. Terms read 2026-11-11: private caching allowed, no republishing.
# The key comes from the CFBD_API_KEY user environment variable (registry fallback for sessions opened before it
# was set). It is never printed and never written to a file. No injuries or depth charts exist on CFBD either.
CFBD = "https://api.collegefootballdata.com"
ELO_PER_POINT, ELO_HOME = 0.0404, 3.98      # fitted on 2024 (n=752): margin = 0.0404 x Elo diff + 3.98 home field
SP_HOME = 2.5


def cfbd_key():
    k = os.environ.get("CFBD_API_KEY")
    if not k and os.name == "nt":
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as h:
                k = winreg.QueryValueEx(h, "CFBD_API_KEY")[0]
        except OSError:
            k = None
    return k or None


def _cfbd_week(calendar, today):
    """CFBD week number whose window holds `today` (college weeks run one ahead of the NFL card week)."""
    best = None
    for w in calendar or []:
        if (w.get("seasonType") or "regular") != "regular":
            continue
        a = str(w.get("startDate") or w.get("firstGameStart") or "")[:10]
        b = str(w.get("endDate") or w.get("lastGameStart") or "")[:10]
        if a and a <= today.isoformat() and (not b or today.isoformat() <= b):
            return w.get("week")
        if a and a > today.isoformat() and best is None:
            best = w.get("week")
    return best


def parse_cfbd_lines(lines):
    """CFBD spreads are home-negative. Flip to the repo convention: spread_home positive = home favored."""
    out = []
    for g in lines or []:
        books = []
        for b in g.get("lines") or []:
            sp, op = b.get("spread"), b.get("spreadOpen")
            books.append({"provider": b.get("provider"), "spread_home": None if sp is None else -float(sp),
                          "open_spread_home": None if op is None else -float(op), "total": b.get("overUnder"),
                          "open_total": b.get("overUnderOpen")})
        if books:
            out.append({"game_id": str(g.get("id")), "home": g.get("homeTeam"), "away": g.get("awayTeam"), "books": books})
    return out


def cfbd_block(today, session=None, key=None, sleep=time.sleep):
    """Lines for the current CFBD week plus SP+, Elo and FPI for every team. Never raises: failures are listed."""
    key = key or cfbd_key()
    blk = {"source": "collegefootballdata.com (attribution: Data provided by CollegeFootballData.com)", "calls_made": 0,
           "not_retrieved": [], "week": None, "lines": [], "ratings": {}}
    if not key:
        blk["not_retrieved"].append("CFBD: not available, CFBD_API_KEY is not set")
        return blk
    session = session or requests.Session()

    def get(path, **params):
        if blk["calls_made"]:
            sleep(DELAY_SECONDS)
        blk["calls_made"] += 1
        try:
            r = session.get(CFBD + path, params=params, headers={"Authorization": "Bearer " + key}, timeout=30)
            r.raise_for_status()
            blk["calls_left_this_month"] = getattr(r, "headers", {}).get("x-calllimit-remaining")
            return r.json()
        except Exception as exc:  # noqa: BLE001
            blk["not_retrieved"].append(f"CFBD {path}: not retrieved ({type(exc).__name__})")
            return None

    year = today.year if today.month >= 7 else today.year - 1
    blk["week"] = _cfbd_week(get("/calendar", year=year), today)
    if blk["week"] is not None:
        blk["lines"] = parse_cfbd_lines(get("/lines", year=year, week=blk["week"], seasonType="regular"))
    for name, path, field in (("sp", "/ratings/sp", "rating"), ("elo", "/ratings/elo", "elo"), ("fpi", "/ratings/fpi", "fpi")):
        for x in get(path, year=year) or []:
            if x.get("team") and x.get(field) is not None:
                blk["ratings"].setdefault(x["team"], {})[name] = x[field]
                if name == "sp" and x.get("ranking") is not None:
                    blk["ratings"][x["team"]]["sp_rank"] = x["ranking"]
    return blk


def rating_margins(blk, home, away, neutral=False):
    """Home margin implied by each rating system (sanity check only: 2025 test, n=762, Elo added nothing to the
    market line, slope 0.05 with error 0.09). None where a rating is missing."""
    h, a = blk["ratings"].get(home, {}), blk["ratings"].get(away, {})
    hf = 0.0 if neutral else 1.0
    out = {}
    if "sp" in h and "sp" in a:
        out["sp"] = round(h["sp"] - a["sp"] + SP_HOME * hf, 1)
    if "fpi" in h and "fpi" in a:
        out["fpi"] = round(h["fpi"] - a["fpi"] + SP_HOME * hf, 1)
    if "elo" in h and "elo" in a:
        out["elo"] = round(ELO_PER_POINT * (h["elo"] - a["elo"]) + ELO_HOME * hf, 1)
    return out


def snapshot_path(out_dir, now):
    return os.path.join(out_dir, now.strftime("%Y-%m-%d-%H%M") + "-cfb.json")


def latest_previous(out_dir, exclude=None):
    files = sorted(glob.glob(os.path.join(out_dir, "????-??-??-????-cfb.json")))
    files = [f for f in files if os.path.abspath(f) != os.path.abspath(exclude or "")]
    return files[-1] if files else None


def diff_snapshots(old, new, threshold=MOVE_THRESHOLD):
    """Line moves of `threshold` points or more (spread or total) for games
    in both snapshots, plus new and dropped games with odds."""
    om = {g["game_id"]: g for g in old["games"]}
    moves, added = [], []
    for g in new["games"]:
        o = om.get(g["game_id"])
        if o is None:
            if g.get("odds"):
                added.append(g)
            continue
        if not (g.get("odds") and o.get("odds")):
            continue
        for key, label in (("spread_home", "spread (home fav +)"), ("total", "total")):
            a, b = o["odds"].get(key), g["odds"].get(key)
            if a is None or b is None:
                continue
            if abs(b - a) >= threshold:
                moves.append({"game": f'{g["away"]} at {g["home"]}', "kind": label,
                              "from": a, "to": b, "move": round(b - a, 1)})
    dropped = [o for gid, o in om.items()
               if gid not in {g["game_id"] for g in new["games"]} and o.get("odds")
               and o.get("state") == "pre"]
    return {"moves": moves, "added": added, "dropped": dropped}


def render_report(snap, path, prev_path, diff):
    up = [g for g in snap["games"] if g["state"] == "pre"]
    with_odds = [g for g in snap["games"] if g.get("odds")]
    lines = ["CFB SNAPSHOT " + snap["taken_at"], NO_INJURY_HEADER, ""]
    lines.append(f'Games: {len(snap["games"])} total, {len(up)} upcoming, {len(with_odds)} with a line. '
                 f'Calls made: {snap["calls_made"]} (cap {CALL_CAP}).')
    lines.append("Saved: " + (path or "not saved (--no-save)"))
    for p in snap["rankings"][:3]:
        top = ", ".join(f'{r["rank"]} {r["team"]}' for r in p["ranks"][:5])
        lines.append(f'{p["poll"]} top 5: {top}')
    c = snap.get("cfbd")
    if c:
        lines.append(f'CFBD: week {c["week"]}, {len(c["lines"])} games with lines, ratings for {len(c["ratings"])} teams, '
                     f'{c["calls_made"]} calls, {c.get("calls_left_this_month", "unknown")} left this month.')
        lines += ["  - " + m for m in c["not_retrieved"]]
    if snap["not_retrieved"]:
        lines.append("")
        lines.append("NOT RETRIEVED:")
        lines += ["  - " + m for m in snap["not_retrieved"]]
    lines.append("")
    if diff is None:
        lines.append("Diff: no earlier snapshot on disk, so no comparison. This is the baseline.")
    else:
        lines.append(f"Diff vs {os.path.basename(prev_path)} (moves of {MOVE_THRESHOLD:g} point or more):")
        if not diff["moves"]:
            lines.append("  no line moves of that size.")
        for m in diff["moves"]:
            lines.append(f'  {m["game"]}: {m["kind"]} {m["from"]:+g} -> {m["to"]:+g} ({m["move"]:+g})')
        for g in diff["added"]:
            lines.append(f'  new line: {g["away"]} at {g["home"]}')
        for g in diff["dropped"]:
            lines.append(f'  line gone: {g["away"]} at {g["home"]} (not in this pull)')
    return "\n".join(lines)


def main(argv=None, fetcher=None, today=None, now=None):
    ap = argparse.ArgumentParser(description="Save a dated ESPN college-football snapshot and diff it.")
    ap.add_argument("--back", type=int, default=5)
    ap.add_argument("--ahead", type=int, default=5)
    ap.add_argument("--out", default=None)
    ap.add_argument("--no-save", action="store_true")
    ap.add_argument("--no-cfbd", action="store_true", help="skip the CFBD block (lines, SP+, Elo, FPI; 5 calls)")
    args = ap.parse_args(argv)
    now = now or datetime.now()
    today = today or now.date()
    out_dir = args.out or default_out_dir()
    live = fetcher is None                   # tests pass their own fetcher: no CFBD call is made for them
    fetcher = fetcher or Fetcher()
    snap = build_snapshot(fetcher, today, args.back, args.ahead, now=now)
    if live and not args.no_cfbd and snap["games"]:
        snap["cfbd"] = cfbd_block(today)
    if not snap["games"]:
        print(NO_INJURY_HEADER)
        print("\nNothing retrieved, nothing saved.")
        for m in snap["not_retrieved"]:
            print("NOT RETRIEVED: " + m)
        return 1
    path = None
    prev = latest_previous(out_dir, snapshot_path(out_dir, now))
    if not args.no_save:
        os.makedirs(out_dir, exist_ok=True)
        path = snapshot_path(out_dir, now)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(snap, f, indent=1)
    diff = None
    if prev:
        try:
            with open(prev, encoding="utf-8") as f:
                diff = diff_snapshots(json.load(f), snap)
        except (OSError, ValueError) as exc:
            snap["not_retrieved"].append(f"previous snapshot {prev}: not read ({exc})")
    print(render_report(snap, path, prev, diff))
    return 0


if __name__ == "__main__":
    sys.exit(main())
