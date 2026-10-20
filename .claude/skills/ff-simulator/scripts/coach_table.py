"""Write the current coaching-tendency table (as of the next unplayed week).
Output: D:\\WKP\\data\\ff-simulator\\coach_tendencies_<season>_wk<week>.csv and a printed summary.
Usage: python coach_table.py 2026 6
"""
import sys
from pathlib import Path
import pandas as pd
sys.path.insert(0, str(Path(__file__).parent))
import coach_model as cm

season, week = int(sys.argv[1]), int(sys.argv[2])
as_of = season * 100 + week
p, tg = cm.build_tables()
lg = cm.league_means(tg[tg.order < as_of])
cur = tg[(tg.season == season) & (tg.order < as_of)]
team_coach = cur.sort_values("order").groupby("posteam").coach.last()
rows = []
for team, coach in team_coach.items():
    t = cm.tendencies(tg, coach, team, as_of, lg)
    rows.append({"team": team, "coach": coach, **{k: round(v, 4) for k, v in t.items()}})
df = pd.DataFrame(rows).sort_values("pass_oe", ascending=False)
out = Path(r"D:\WKP\data\ff-simulator")
out.mkdir(parents=True, exist_ok=True)
f = out / f"coach_tendencies_{season}_wk{week}.csv"
df.to_csv(f, index=False)
print("league:", {k: round(v, 3) for k, v in lg.items()})
show = df[["team", "coach", "pass_neutral", "pass_oe", "rz_pass", "go4", "plays_pg", "no_huddle", "_own_plays", "_plays_behind"]]
print(show.to_string(index=False))
print("saved", f)
