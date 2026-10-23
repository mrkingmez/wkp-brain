"""Simulate one game with named players (ff-play-sim Phase 2).

python run_game.py <season> <week> <HOME> <AWAY> [--n 2000] [--top 14]
Uses games before that week, the week's injury file (data\\ff-simulator\\injuries_<season>_wk<week>.csv, play_prob and roster team),
and each head coach's latest tendencies. Prints per-player IRFL offense + kicker points (mean, p10, p90), volume, and the score.
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import play_engine as pe
import player_layer as pl

INJ = r"D:\WKP\data\ff-simulator\injuries_{s}_wk{w}.csv"


def avail_for(team, inj):
    if inj is None:
        return {}
    a = {}
    for r in inj.itertuples():
        if pd.isna(r.gsis_id):
            continue
        p = 0.0 if (isinstance(r.roster_team, str) and r.roster_team != team) else float(r.play_prob)
        a[r.gsis_id] = min(a.get(r.gsis_id, 1.0), p)
    return a


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("season", type=int)
    ap.add_argument("week", type=int)
    ap.add_argument("home")
    ap.add_argument("away")
    ap.add_argument("--n", type=int, default=2000)
    ap.add_argument("--top", type=int, default=14)
    a = ap.parse_args()
    as_of = a.season * 100 + a.week
    pbp = pe.load_pbp()
    T = pe.Tables(pbp, as_of)
    f = Path(INJ.format(s=a.season, w=a.week))
    inj = pd.read_csv(f) if f.exists() else None
    print("injury file:", f if inj is not None else "NONE (everyone available)")
    pmh = pl.PlayerModel(pbp, as_of, a.home, avail_for(a.home, inj))
    pma = pl.PlayerModel(pbp, as_of, a.away, avail_for(a.away, inj))
    mh = pe.Matchup(T, a.home, a.away, qb=pmh.qb)
    ma = pe.Matchup(T, a.away, a.home, qb=pma.qb)
    print("QB adjustment vs team's recent mix:", a.home, mh.qb_note, "|", a.away, ma.qb_note)
    dmh = pl.DefenseModel(pbp, as_of, a.home, avail_for(a.home, inj))
    dma = pl.DefenseModel(pbp, as_of, a.away, avail_for(a.away, inj))
    H, A, HN, AN, players = pe.sim_game(T, mh, ma, n=a.n, seed=as_of, pm=(pmh, pma), return_players=True, dm=(dmh, dma))
    pinfo = pd.read_parquet(r"D:\WKP\data\nfl\players\players.parquet")
    gname = dict(zip(pinfo.gsis_id, pinfo.display_name))
    gpos = dict(zip(pinfo.gsis_id, pinfo.position))
    print(f"{a.away} @ {a.home}: sim score {a.away} {A.mean():.1f}  {a.home} {H.mean():.1f}  (totals run light, see SKILL.md)  "
          f"home win {((H > A).mean() + 0.5 * (H == A).mean()):.1%}")
    print(f"QBs: {a.home} {pmh.names.get(pmh.qb, pmh.qb)} | {a.away} {pma.names.get(pma.qb, pma.qb)}\n")
    names = {**gname, **pmh.names, **pma.names}
    team_of = {i: a.home for i in list(pmh.tgt_ids) + list(pmh.car_ids) + [pmh.qb, pmh.kicker]}
    team_of.update({i: a.away for i in list(pma.tgt_ids) + list(pma.car_ids) + [pma.qb, pma.kicker]})
    for dmx, tm in ((dmh, a.home), (dma, a.away)):
        for nm_, (ids_, _c) in dmx.lists.items():
            for i_ in ids_:
                team_of.setdefault(i_, tm)
    rows = []
    for pid, d in players.items():
        rows.append(dict(player=names.get(pid, pid), pos=gpos.get(pid, "?"), team=team_of.get(pid, "?"), mean=d["pts"].mean(),
                         p10=np.percentile(d["pts"], 10), p90=np.percentile(d["pts"], 90),
                         tgt=d["tgt"], rec=d["rec"], rec_yds=d["rec_yds"], car=d["car"], car_yds=d["car_yds"]))
    df = pd.DataFrame(rows).sort_values("mean", ascending=False)
    pd.set_option("display.width", 200)
    off = df[df.pos.isin(["QB", "RB", "WR", "TE", "K", "FB"])]
    dfn = df[~df.pos.isin(["QB", "RB", "WR", "TE", "K", "FB", "P", "LS"])]
    print(off.head(a.top).round(1).to_string(index=False))
    print("\nDEFENDERS (IRFL: solo 1, assist 0.5, sack 3, INT 3, PD 1, FF 2, FR 2, TD 6)")
    print(dfn.head(a.top + 6)[["player", "pos", "team", "mean", "p10", "p90"]].round(1).to_string(index=False))


if __name__ == "__main__":
    main()
