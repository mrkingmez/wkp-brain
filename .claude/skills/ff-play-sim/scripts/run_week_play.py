"""Simulate a whole NFL week with the play-by-play sim and compare it with the old ff-simulator for Zac's roster.

python run_week_play.py <season> <week> [--n 1500] [--roster D:\\WKP\\scratch\\wk7_roster.json]

Inputs: injuries_<season>_wk<week>.csv (availability, roster team), old sim summary sim_<season>_wk<week>_summary.csv, Zac's MFL roster json.
Outputs: D:\\WKP\\data\\ff-play-sim\\play_sim_<season>_wk<week>.csv (every offensive player and kicker: mean, p10, p90, volume) and a printed
roster table with the BLEND. Blend weights on the new sim come from the player backtest (known-active, 5,550 player-weeks):
QB 0.9, K 0.5, RB 0.15, WR 0.2, TE 0.2; the rest is the old sim. Defenders come from the old sim only (the play sim has no IDP yet).
"""
import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import play_engine as pe
import player_layer as pl
import run_game as rg

W_NEW = {"QB": 0.9, "K": 0.5, "PK": 0.5, "RB": 0.15, "WR": 0.2, "TE": 0.2}
OUTDIR = Path(r"D:\WKP\data\ff-play-sim")
OLD = r"D:\WKP\data\ff-simulator\sim_{s}_wk{w}_summary.csv"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("season", type=int)
    ap.add_argument("week", type=int)
    ap.add_argument("--n", type=int, default=1500)
    ap.add_argument("--roster", default=r"D:\WKP\scratch\wk7_roster.json")
    a = ap.parse_args()
    as_of = a.season * 100 + a.week
    pbp = pe.load_pbp()
    T = pe.Tables(pbp, as_of)
    f = Path(rg.INJ.format(s=a.season, w=a.week))
    inj = pd.read_csv(f) if f.exists() else None
    print("injury file:", f if inj is not None else "NONE (everyone available)")
    sched = pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet")
    sched = sched[(sched.season == a.season) & (sched.week == a.week) & (sched.game_type == "REG")]
    pinfo = pd.read_parquet(r"D:\WKP\data\nfl\players\players.parquet")
    nm = dict(zip(pinfo.gsis_id, pinfo.display_name))
    rows = []
    for g in sched.itertuples():
        pmh = pl.PlayerModel(pbp, as_of, g.home_team, rg.avail_for(g.home_team, inj))
        pma = pl.PlayerModel(pbp, as_of, g.away_team, rg.avail_for(g.away_team, inj))
        mh = pe.Matchup(T, g.home_team, g.away_team, qb=pmh.qb)
        ma = pe.Matchup(T, g.away_team, g.home_team, qb=pma.qb)
        dmh = pl.DefenseModel(pbp, as_of, g.home_team, rg.avail_for(g.home_team, inj))
        dma = pl.DefenseModel(pbp, as_of, g.away_team, rg.avail_for(g.away_team, inj))
        H, A, HN, AN, players = pe.sim_game(T, mh, ma, n=a.n, seed=as_of * 10 + len(rows) % 10, pm=(pmh, pma), return_players=True,
                                           dm=(dmh, dma))
        team_of = {i: g.home_team for i in list(pmh.tgt_ids) + list(pmh.car_ids) + [pmh.qb, pmh.kicker]}
        team_of.update({i: g.away_team for i in list(pma.tgt_ids) + list(pma.car_ids) + [pma.qb, pma.kicker]})
        for dmx, tm in ((dmh, g.home_team), (dma, g.away_team)):
            for _nm, (ids_, _c) in dmx.lists.items():
                for i_ in ids_:
                    team_of.setdefault(i_, tm)
        for pid, d in players.items():
            rows.append(dict(gsis_id=pid, name=nm.get(pid, pmh.names.get(pid) or pma.names.get(pid) or pid), team=team_of.get(pid, "?"),
                             opp=g.away_team if team_of.get(pid) == g.home_team else g.home_team,
                             new=d["pts"].mean(), new_p10=np.percentile(d["pts"], 10), new_p90=np.percentile(d["pts"], 90),
                             tgt=d["tgt"], rec=d["rec"], rec_yds=d["rec_yds"], car=d["car"], car_yds=d["car_yds"],
                             game=f"{g.away_team}@{g.home_team}", game_score=f"{A.mean():.1f}-{H.mean():.1f}"))
        print(f"{g.away_team}@{g.home_team} done", flush=True)
    new = pd.DataFrame(rows)
    OUTDIR.mkdir(parents=True, exist_ok=True)
    new.to_csv(OUTDIR / f"play_sim_{a.season}_wk{a.week}.csv", index=False)
    print("saved", OUTDIR / f"play_sim_{a.season}_wk{a.week}.csv")

    old = pd.read_csv(OLD.format(s=a.season, w=a.week))[["gsis_id", "group", "mean", "sd", "questionable"]].rename(
        columns={"mean": "old", "sd": "old_sd", "group": "pos"})
    pos_map = dict(zip(old.gsis_id, old.pos))
    rost = json.load(open(a.roster))
    r = pd.DataFrame(rost, columns=["pos", "name", "nfl", "status", "salary", "cy", "proj", "inj", "mfl", "espn"])
    npl = pinfo[["gsis_id", "espn_id"]].dropna()
    npl["espn_id"] = npl.espn_id.astype(str).str.replace(r"\.0$", "", regex=True)
    r["gsis_id"] = r.espn.astype(str).str.replace(r"\.0$", "", regex=True).map(dict(zip(npl.espn_id, npl.gsis_id)))
    m = r.merge(old, on="gsis_id", how="left").merge(new[["gsis_id", "new", "new_p10", "new_p90", "tgt", "car", "game"]], on="gsis_id", how="left")
    m["w"] = m.pos_x.map(W_NEW).fillna(0.0)
    m["blend"] = np.where(m.new.notna(), m.w * m.new + (1 - m.w) * m.old, m.old)
    m["proj"] = pd.to_numeric(m.proj, errors="coerce")
    m["gap"] = m.new - m.old
    pd.set_option("display.width", 220)
    cols = ["pos_x", "name", "nfl", "status", "inj", "proj", "old", "new", "blend", "gap", "new_p10", "new_p90", "tgt", "car"]
    print("\nZac's roster: MFL projection, old sim, play sim, blend (|gap| >= 3 is where the two sims disagree)\n")
    print(m.sort_values(["pos_x", "blend"], ascending=[True, False])[cols].round(1).to_string(index=False))
    m.to_csv(OUTDIR / f"roster_compare_{a.season}_wk{a.week}.csv", index=False)


if __name__ == "__main__":
    main()
