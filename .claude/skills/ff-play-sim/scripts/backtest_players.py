"""Player-level backtest of the play-by-play sim against the plain recent average and the old ff-simulator.

Same rules as ff-simulator's backtest_sim.py: only players who recorded a stat that week are scored, IRFL points, nothing from that
week or later is used, no injury information (so absences hit every method the same way). Uses the player-weeks already in
D:\\WKP\\data\\ff-simulator\\backtest_sim.csv (which holds the old sim's mean, the baseline and the actual) and adds the new sim's mean.
Offense and kicker only (QB RB WR TE K): the play sim has no defenders yet.

python backtest_players.py [--n 300]
"""
import argparse
import os
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import backtest_engine as be
import play_engine as pe
import player_layer as pl

OLD = Path(r"D:\WKP\data\ff-simulator\backtest_sim.csv")
OUT = Path(r"D:\WKP\data\ff-play-sim\backtest_players.csv")


def main(n, oracle=False):
    old = pd.read_csv(OLD)
    old = old[old.group.isin(["QB", "RB", "WR", "TE", "K", "DL", "LB", "DB"])]
    pbp = pe.load_pbp()
    part = None
    if oracle:      # "known active": only players who actually recorded a stat that week can get the ball (what an injury report tells Zac)
        sp = pd.concat([pd.read_parquet(rf"D:\WKP\data\nfl\stats_player\stats_player_week_{s}.parquet") for s in (2025, 2026)])
        sp = sp[sp.season_type == "REG"]
        part = {(int(r.season) * 100 + int(r.week), r.team): set() for r in sp[["season", "week", "team"]].drop_duplicates().itertuples()}
        for r in sp[["season", "week", "team", "player_id"]].itertuples():
            part[(int(r.season) * 100 + int(r.week), r.team)].add(r.player_id)
    rows = []
    for order in sorted(old.order.unique()):
        season, week = divmod(int(order), 100)
        T = pe.Tables(pbp, order)
        models, dmodels = {}, {}
        for _, g in be.games_of(pbp, season, week).iterrows():
            for tm in (g.home, g.away):
                if tm not in models:
                    act = part.get((int(order), tm), set()) if oracle else None
                    models[tm] = pl.PlayerModel(pbp, order, tm, active=act)
                    dmodels[tm] = pl.DefenseModel(pbp, order, tm, active=act)
            use_qb = os.environ.get("PS_QBADJ", "1") == "1"
            mh = pe.Matchup(T, g.home, g.away, off_coach=g.hc, qb=models[g.home].qb if use_qb else None)
            ma = pe.Matchup(T, g.away, g.home, off_coach=g.ac, qb=models[g.away].qb if use_qb else None)
            H, A, HN, AN, pl_ = pe.sim_game(T, mh, ma, n=n, seed=int(order) * 100 + hash(g.game_id) % 97,
                                           pm=(models[g.home], models[g.away]), return_players=True,
                                           dm=(dmodels[g.home], dmodels[g.away]))
            for pid, d in pl_.items():
                rows.append(dict(order=order, id=pid, new=float(d["pts"].mean()), new_p10=float(np.percentile(d["pts"], 10)),
                                 new_p90=float(np.percentile(d["pts"], 90))))
        print("done", order, flush=True)
    new = pd.DataFrame(rows).drop_duplicates(["order", "id"])
    d = old.merge(new, on=["order", "id"], how="left")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    d.to_csv(OUT, index=False)
    summarize(d)


def summarize(d):
    d = d.dropna(subset=["base"])
    d = d[(d.sim > 0.5)]
    cover = d.new.notna().mean()
    print(f"\n{len(d)} player-weeks (old sim > 0.5 pts, has baseline); new sim has a value for {cover:.0%}")
    d = d.dropna(subset=["new"])
    d = d.assign(blend=(d.new + d.sim) / 2)
    print("group |  n  | MAE new | MAE old sim | MAE avg | RMSE new | RMSE old | RMSE avg | rank corr new | old | avg | p10-p90 cover new")
    for grp in ("QB", "RB", "WR", "TE", "K", "DL", "LB", "DB"):
        g = d[d.group == grp]
        if len(g) < 30:
            continue
        m = lambda c: (g[c] - g.actual).abs().mean()
        r = lambda c: np.sqrt(((g[c] - g.actual) ** 2).mean())
        rc = lambda c: np.nanmean([x[c].corr(x.actual, method="spearman") for _, x in g.groupby("order") if len(x) > 8])
        cov = ((g.actual >= g.new_p10) & (g.actual <= g.new_p90)).mean()
        print(f"{grp:4s}  | {len(g):4d} | {m('new'):7.2f} | {m('sim'):11.2f} | {m('base'):7.2f} | {r('new'):8.2f} | {r('sim'):8.2f} | "
              f"{r('base'):8.2f} | {rc('new'):13.3f} | {rc('sim'):.3f} | {rc('base'):.3f} | {cov:.0%}")
    print("\nbias (new minus actual):", d.groupby("group").apply(lambda x: (x.new - x.actual).mean(), include_groups=False).round(2).to_dict())
    print("blend (new + old)/2 MAE:", d.groupby("group").apply(lambda x: (x.blend - x.actual).abs().mean(), include_groups=False).round(2).to_dict())


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=300)
    ap.add_argument("--oracle", action="store_true", help="known-active test: players who did not play get no share")
    a = ap.parse_args()
    import os
    tag = os.environ.get("PS_TAG", "")
    if a.oracle:
        OUT = Path(r"D:\WKP\data\ff-play-sim\backtest_players_oracle%s.csv" % tag)
    main(a.n, a.oracle)
