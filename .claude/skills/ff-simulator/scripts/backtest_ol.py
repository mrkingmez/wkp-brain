"""Backtest the offensive-line layer: same simulations with the OL layer off / half / full, same seeds.

python backtest_ol.py [first_order last_order] [--sims 400]

Needs ol_coefs.json fitted on games BEFORE the window (python ol_model.py fit --train-before <first_order>) and
ol_panel.csv (written by the fit). OL absence per team-game is the ex-ante version: a usual starter with zero snaps.
Scores two things against what actually happened:
  team level   : sacks, passing yards and rushing yards per offense team-game (sim env mean vs actual)
  player level : IRFL points for QB, RB, WR, TE (sim mean vs actual), all players and teams with miss >= 0.15
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import backtest_sim as bs
import run_week as rw
import simulate as sm

SCALES = {"off": (0.0, ()), "half": (0.5, ()), "full": (1.0, ()), "yds": (1.0, ("sack_rate",))}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sims = 400
    if "--sims" in sys.argv:
        sims = int(sys.argv[sys.argv.index("--sims") + 1])
        args = [a for a in args if a != str(sims)]
    lo, hi = (int(args[0]), int(args[1])) if len(args) >= 2 else (202506, 202605)
    panel = pd.read_csv(r"D:\WKP\data\ff-simulator\ol_panel.csv")
    p, tg = rw.cm.build_tables()
    pw_all = sm.load_player_weeks((2024, 2025, 2026))
    sched = pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet")
    pw_all["pts"] = bs.actual_points(pw_all)
    weeks = sorted(set(int(o) for o in pw_all.order.unique() if lo <= o <= hi))
    prow, trow = [], []
    for order in weeks:
        season, week = divmod(order, 100)
        pn = panel[panel.order == order]
        miss = dict(zip(pn.team, pn.miss))
        lg = rw.cm.league_means(tg[tg.order < order])
        defs, lg_def = sm.defense_table(order)
        pw_hist = pw_all[pw_all.order < order]
        act = pw_all[pw_all.order == order].set_index("player_id").pts
        res = {}
        for name, (sc, zero) in SCALES.items():
            sm.set_ol(sc, zero)
            ids, results, M, envs, _ = rw.simulate_week(season, week, {}, tg, lg, pw_hist, defs, lg_def, sched, sims=sims,
                                                        seed=order, verbose=False, apply_quest_zero=False, ol_missing=miss)
            res[name] = (ids, results, M, envs)
        ids, results = res["off"][0], res["off"][1]
        for n, i in enumerate(ids):
            if i not in act.index:
                continue
            team = results[i][1]
            r = dict(order=order, id=i, name=results[i][0], team=team, group=results[i][2], actual=float(act[i]),
                     miss=miss.get(team, np.nan))
            for name in SCALES:
                r[name] = float(res[name][2][n].mean())
            prow.append(r)
        pn2 = pn.set_index("team")
        for g, env in res["off"][3].items():
            for team in [k for k in env if not k.startswith("_") and k not in ("spread_home", "total")]:
                if team not in pn2.index:
                    continue
                a = pn2.loc[team]
                r = dict(order=order, team=team, miss=a.miss, act_sacks=a.sacks, act_pass_yds=a.ypa * a.att,
                         act_rush_yds=a.ypc * a.carries)
                for name in SCALES:
                    e = res[name][3][g][team]
                    r[f"{name}_sacks"], r[f"{name}_pass_yds"], r[f"{name}_rush_yds"] = e["sacks"], e["pass_yds"], e["rush_yds"]
                trow.append(r)
        print("done", order, flush=True)
    sm.set_ol(0.0)
    P, T = pd.DataFrame(prow), pd.DataFrame(trow)
    P.to_csv(r"D:\WKP\data\ff-simulator\backtest_ol_players.csv", index=False)
    T.to_csv(r"D:\WKP\data\ff-simulator\backtest_ol_teams.csv", index=False)

    print(f"\n=== TEAM LEVEL: {len(T)} offense team-games, {T.order.nunique()} weeks, {sims} sims ===")
    for label, sub in (("all games", T), ("OL miss >= 0.15", T[T.miss >= 0.15]), ("OL miss >= 0.30", T[T.miss >= 0.30]),
                       ("OL miss == 0", T[T.miss == 0])):
        print(f"\n{label}: n={len(sub)}, mean miss {sub.miss.mean():.2f}")
        for stat in ("sacks", "pass_yds", "rush_yds"):
            line = f"  {stat:9s} actual mean {sub['act_' + stat].mean():7.2f} |"
            for name in SCALES:
                e = sub[f"{name}_{stat}"] - sub["act_" + stat]
                line += f" {name}: bias {e.mean():+6.2f} MAE {e.abs().mean():6.2f} RMSE {np.sqrt((e ** 2).mean()):6.2f} |"
            print(line)
    print(f"\n=== PLAYER LEVEL (QB, RB, WR, TE with a stat line) ===")
    Q = P[P.group.isin(["QB", "RB", "WR", "TE"]) & (P.off > 0.5)]
    for label, sub in (("all", Q), ("team OL miss >= 0.15", Q[Q.miss >= 0.15])):
        print(f"\n{label}: n={len(sub)}")
        for grp in ("QB", "RB", "WR", "TE"):
            g = sub[sub.group == grp]
            if len(g) < 20:
                continue
            line = f"  {grp}: n={len(g):4d} |"
            for name in SCALES:
                e = g[name] - g.actual
                line += f" {name}: bias {e.mean():+5.2f} MAE {e.abs().mean():5.2f} RMSE {np.sqrt((e ** 2).mean()):5.2f} |"
            print(line)
        line = "  ALL four |"
        for name in SCALES:
            e = sub[name] - sub.actual
            line += f" {name}: MAE {e.abs().mean():5.3f} RMSE {np.sqrt((e ** 2).mean()):5.3f} |"
        print(line)


if __name__ == "__main__":
    main()
