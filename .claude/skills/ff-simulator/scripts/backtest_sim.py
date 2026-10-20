"""Backtest the full simulator against what players actually scored (IRFL rules).

For each week in the window it simulates using only data from BEFORE that week
and the game's closing line from nflverse schedules, then compares each player's
simulated mean to his actual IRFL points. Baseline = his own recency-weighted
average over games he played. Only players who recorded a stat that week are
scored (we cannot know who sits ahead of time in a backtest, and it hits both
methods the same way).

python backtest_sim.py [first_order last_order] [--sims 400]
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import run_week as rw
import simulate as sm


def actual_points(d: pd.DataFrame) -> pd.Series:
    f = lambda c: d[c].fillna(0) if c in d else 0
    fg = (f("fg_made_0_19") + f("fg_made_20_29")) * 3.0 + f("fg_made_30_39") * 3.5 + f("fg_made_40_49") * 4.5 \
        + f("fg_made_50_59") * 5.5 + f("fg_made_60_") * 6.5
    return (f("passing_yards") * 0.04 + f("passing_tds") * 6 - f("passing_interceptions") * 2
            + f("rushing_yards") * 0.1 + f("rushing_tds") * 6 + f("receptions") + f("receiving_yards") * 0.1
            + f("receiving_tds") * 6 - (f("rushing_fumbles_lost") + f("receiving_fumbles_lost") + f("sack_fumbles_lost")) * 2
            + f("def_tackles_solo") + f("def_tackle_assists") * 0.5 + f("def_sacks") * 3 + f("def_interceptions") * 3
            + f("def_pass_defended") + f("def_fumbles_forced") * 2 + f("fumble_recovery_opp") * 2 + f("def_tds") * 6
            + f("def_safeties") * 4 + f("pat_made") + fg)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    sims = 400
    if "--sims" in sys.argv:
        sims = int(sys.argv[sys.argv.index("--sims") + 1])
        args = [a for a in args if a != str(sims)]
    lo, hi = (int(args[0]), int(args[1])) if len(args) >= 2 else (202506, 202605)
    p, tg = rw.cm.build_tables()
    pw_all = sm.load_player_weeks((2024, 2025, 2026))
    sched = pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet")
    pw_all["pts"] = actual_points(pw_all)
    weeks = sorted(set(int(o) for o in pw_all.order.unique() if lo <= o <= hi))
    rows = []
    for order in weeks:
        season, week = divmod(order, 100)
        lg = rw.cm.league_means(tg[tg.order < order])
        defs, lg_def = sm.defense_table(order)
        pw_hist = pw_all[pw_all.order < order]
        ids, results, M, envs, _ = rw.simulate_week(season, week, {}, tg, lg, pw_hist, defs, lg_def, sched,
                                                    sims=sims, seed=order, verbose=False, apply_quest_zero=False)
        act = pw_all[pw_all.order == order].set_index("player_id").pts
        # baseline: recency-weighted average of his own games played
        hist = pw_hist.sort_values("order")
        for n, i in enumerate(ids):
            if i not in act.index:
                continue
            g = hist[hist.player_id == i].tail(14)
            if len(g):
                w = 0.88 ** np.arange(len(g))[::-1]
                base = float((g.pts.values * w).sum() / w.sum())
            else:
                base = np.nan
            rows.append(dict(order=order, id=i, name=results[i][0], group=results[i][2],
                             sim=float(M[n].mean()), p10=float(np.percentile(M[n], 10)), p90=float(np.percentile(M[n], 90)),
                             base=base, actual=float(act[i])))
        print("done", order, flush=True)
    d = pd.DataFrame(rows)
    d.to_csv(r"D:\WKP\data\ff-simulator\backtest_sim.csv", index=False)
    d = d[d.sim > 0.5].dropna(subset=["base"])
    print(f"\n{len(d)} player-weeks, {d.order.nunique()} weeks, {sims} sims per game")
    print("group |  n  | MAE sim | MAE avg | RMSE sim | RMSE avg | rank corr sim | rank corr avg | p10-p90 coverage")
    for grp in ("QB", "RB", "WR", "TE", "K", "DL", "LB", "DB"):
        g = d[d.group == grp]
        if len(g) < 30:
            continue
        mae_s, mae_b = (g.sim - g.actual).abs().mean(), (g.base - g.actual).abs().mean()
        rm_s, rm_b = np.sqrt(((g.sim - g.actual) ** 2).mean()), np.sqrt(((g.base - g.actual) ** 2).mean())
        rc_s = np.nanmean([x.sim.corr(x.actual, method="spearman") for _, x in g.groupby("order") if len(x) > 8])
        rc_b = np.nanmean([x.base.corr(x.actual, method="spearman") for _, x in g.groupby("order") if len(x) > 8])
        cov = ((g.actual >= g.p10) & (g.actual <= g.p90)).mean()
        print(f"{grp:5s} | {len(g):4d} | {mae_s:7.2f} | {mae_b:7.2f} | {rm_s:8.2f} | {rm_b:8.2f} | {rc_s:13.3f} | {rc_b:13.3f} | {cov:.0%}")
    print("\nbias (sim minus actual, mean):", d.groupby("group").apply(lambda x: (x.sim - x.actual).mean(), include_groups=False).round(2).to_dict())


if __name__ == "__main__":
    main()
