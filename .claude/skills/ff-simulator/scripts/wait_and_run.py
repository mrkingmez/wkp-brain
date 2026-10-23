"""Wait until every team playing this week has an injury report, then refresh injuries and run the sim.

python wait_and_run.py 2026 7 [--every 20] [--until "2026-10-23 12:00"] [--no-run]

Gate: nflverse injuries release has at least one row for week W from every team that plays (bye teams excluded,
taken from the nflverse schedule). Polls every N minutes. When all teams are in: build_injuries.py, fetch_odds.py,
run_week.py, optimize.py, in that order. If --until passes first, nothing is simulated and the missing teams are printed.
Teams are checked against the nflverse release, which can trail the official NFL report by some time.
"""
import argparse
import datetime as dt
import io
import subprocess
import sys
import time
from pathlib import Path

import pandas as pd
import requests

HERE = Path(__file__).parent
PY = sys.executable
URL = "https://github.com/nflverse/nflverse-data/releases/download/injuries/injuries_{s}.csv"


def playing(season, week):
    g = pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet")
    g = g[(g.season == season) & (g.week == week) & (g.game_type == "REG")]
    return set(g.home_team) | set(g.away_team)


def reported(season, week):
    d = pd.read_csv(io.StringIO(requests.get(URL.format(s=season), timeout=60).text), low_memory=False)
    return set(d[d.week == week].team)


def step(*args):
    print(">>", " ".join(args), flush=True)
    subprocess.run([PY, "-I", *args], cwd=HERE, check=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("season", type=int)
    ap.add_argument("week", type=int)
    ap.add_argument("--every", type=int, default=20, help="minutes between checks")
    ap.add_argument("--until", help="give up at this local time, YYYY-MM-DD HH:MM")
    ap.add_argument("--no-run", action="store_true", help="only report when the gate opens")
    a = ap.parse_args()
    need = playing(a.season, a.week)
    stop = dt.datetime.fromisoformat(a.until) if a.until else None
    while True:
        try:
            have = reported(a.season, a.week)
        except Exception as e:
            have = set()
            print("check failed:", e, flush=True)
        miss = sorted(need - have)
        print(f"{dt.datetime.now():%a %H:%M} week {a.week}: {len(need) - len(miss)}/{len(need)} teams reported; missing {miss}", flush=True)
        if not miss:
            break
        if stop and dt.datetime.now() >= stop:
            raise SystemExit(f"Gave up at {stop}: reports still missing for {miss}. Sim NOT run.")
        time.sleep(a.every * 60)
    print("All teams reported.", flush=True)
    if a.no_run:
        raise SystemExit(0)
    odds = rf"D:\WKP\scratch\wk{a.week}_odds.json"
    step("build_injuries.py", str(a.season), str(a.week))
    step("fetch_odds.py", odds)
    step("run_week.py", str(a.season), str(a.week), "--odds", odds)
    step("optimize.py", str(a.season), str(a.week))
