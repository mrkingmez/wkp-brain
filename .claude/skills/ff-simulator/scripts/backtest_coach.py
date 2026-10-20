"""Backtest the coaching-tendency model.

For every team-game in the target window, predict three things using only
games played BEFORE that week, then compare to what happened:
  neutral pass rate, offensive plays, red-zone pass rate
against two baselines: the league average, and a plain team-to-date average
(no coach weighting, no shrinkage, no recency decay).
Prints MAE per method and the % improvement of the coach model over each.
"""
import sys
import numpy as np
import pandas as pd
sys.path.insert(0, __file__.rsplit("\\", 1)[0])
import coach_model as cm

p, tg = cm.build_tables()
tg = tg.sort_values("order").reset_index(drop=True)
tg["neutral_rate"] = tg.pass_neutral_s / tg.n_neutral.replace(0, np.nan)
tg["rz_rate"] = tg.rz_pass_s / tg.n_rz.replace(0, np.nan)

targets = tg[((tg.season == 2025) & (tg.week >= 5)) | ((tg.season == 2026) & (tg.week >= 2))]
targets = targets[(targets.n_neutral >= 12)]
rows = []
cache = {}
for _, r in targets.iterrows():
    key = r.order
    if key not in cache:
        cache[key] = cm.league_means(tg[tg.order < key])
    lg = cache[key]
    t = cm.tendencies(tg, r.coach, r.posteam, key, lg)
    prev_team = tg[(tg.posteam == r.posteam) & (tg.order < key)]
    prev_team = prev_team.tail(17)
    team_neutral = prev_team.pass_neutral_s.sum() / max(prev_team.n_neutral.sum(), 1) if len(prev_team) else lg["pass_neutral"]
    team_plays = prev_team.plays.mean() if len(prev_team) else lg["plays_pg"]
    team_rz = prev_team.rz_pass_s.sum() / max(prev_team.n_rz.sum(), 1) if len(prev_team) else lg["rz_pass"]
    rows.append(dict(
        order=key, team=r.posteam, coach=r.coach, own_plays=t["_own_plays"],
        a_neutral=r.neutral_rate, a_plays=r.plays, a_rz=r.rz_rate,
        c_neutral=t["pass_neutral"], c_plays=t["plays_pg"], c_rz=t["rz_pass"],
        t_neutral=team_neutral, t_plays=team_plays, t_rz=team_rz,
        l_neutral=lg["pass_neutral"], l_plays=lg["plays_pg"], l_rz=lg["rz_pass"],
    ))
d = pd.DataFrame(rows)


def report(df, label):
    print(f"\n{label}  (n={len(df)} team-games)")
    for m, name in (("neutral", "neutral pass rate"), ("plays", "offensive plays"), ("rz", "red-zone pass rate")):
        a = df["a_" + m]
        ok = a.notna()
        mae = {k: (df.loc[ok, f"{k}_{m}"] - a[ok]).abs().mean() for k in "clt"}
        gain_l = 100 * (mae["l"] - mae["c"]) / mae["l"]
        gain_t = 100 * (mae["t"] - mae["c"]) / mae["t"]
        print(f"  {name:20s} MAE coach {mae['c']:.4f} | team-to-date {mae['t']:.4f} | league {mae['l']:.4f}"
              f"  -> coach model {gain_l:+.1f}% vs league, {gain_t:+.1f}% vs team-to-date")


report(d, "ALL")
report(d[d.own_plays >= 2500], "Coaches with 2,500+ prior plays under own name")
report(d[d.own_plays < 1000], "Thin or new (under 1,000 own plays)")
report(d[d.order >= 202602], "2026 only")
d.to_csv(r"D:\WKP\scratch\coach_backtest.csv", index=False)
