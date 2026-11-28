r"""wk11_after_action.py - Week 11 DFS after-action helpers (2026-11-22). DFS only. Read only, never enters or spends.
Scores lineups from ESPN final box scores (ACTUAL_week11_espn.csv, made by scratch/wk11/actuals.py via dashboard/dfs_live.py).
Slate data stays under D:\Draft Kings\Week 11\ (outside repo)."""
import re
import pandas as pd

W = r"D:\Draft Kings\Week 11"
SLOTS = ["QB", "RB", "RB", "WR", "WR", "WR", "TE", "FLEX", "DST"]


def norm(n):
    n = re.sub(r"\b(jr|sr|ii|iii|iv|v)\b\.?", "", (n or "").lower())
    return re.sub(r"[^a-z0-9]", "", n)


def fix(t):
    return {"WAS": "WSH", "JAC": "JAX", "LA": "LAR", "ARZ": "ARI"}.get(t, t)


def load_actual():
    a = pd.read_csv(rf"{W}\ACTUAL_week11_espn.csv")
    return {(fix(r.team), r.norm): r.pts for r in a.itertuples()}


def load_salaries():
    s = pd.read_csv(rf"{W}\DKSalaries_week11.csv", encoding="utf-8-sig")
    s["team"] = s.TeamAbbrev.map(fix)
    return s.set_index("ID")


def actual_of(act, name, team, pos):
    return act.get((fix(team), "dst" if pos == "DST" else norm(name)))


def entries():
    rows = [l.strip().split(",") for l in open(rf"{W}\DKEntries_week11_LINEUPS_UPLOAD.csv", encoding="utf-8-sig")]
    return [(r[0], [int(x) for x in r[4:13]]) for r in rows[1:] if r[0].isdigit() and r[4]]
