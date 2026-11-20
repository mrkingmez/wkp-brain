"""dk_actual.py - real DraftKings classic points for one week from local nflverse data (after the games).

python dk_actual.py --season 2026 --week 10 --out ACTUAL.csv
Skill players from stats_player_week: pass yd 0.04, 300+ bonus 3, pass TD 4, INT -1, rush and rec yd 0.1, 100+ bonus 3 each,
rush/rec TD 6, reception 1, fumble lost -1, 2-pt conversion 2, return TD 6.
DST: summed from that team's defenders and returners in the same file: sack 1, INT 2, opponent fumble recovered 2, defensive or
return TD 6, safety 2, blocked kick 2, plus points-allowed tiers on the opponent's final score from the schedule.
APPROXIMATION: DK takes defensive and return TDs scored by the opponent out of points allowed; this uses the plain final score.
Method only. The output csv holds player data, so write it under D:\\Draft Kings\\, not the repo.
"""
import argparse
import numpy as np
import pandas as pd

STATS = r"D:\WKP\data\nfl\stats_player\stats_player_week_{s}.parquet"
SCHED = r"D:\WKP\data\nfl\schedules\games.parquet"
FIX = {"LA": "LAR", "JAC": "JAX", "WSH": "WAS"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, required=True); ap.add_argument("--week", type=int, required=True); ap.add_argument("--out", required=True)
    a = ap.parse_args()
    d = pd.read_parquet(STATS.format(s=a.season))
    d = d[(d.week == a.week) & (d.season_type == "REG")].copy()
    f = lambda c: d[c].fillna(0)
    d["dk"] = (f("passing_yards") * 0.04 + (f("passing_yards") >= 300) * 3 + f("passing_tds") * 4 - f("passing_interceptions")
               + f("rushing_yards") * 0.1 + (f("rushing_yards") >= 100) * 3 + f("rushing_tds") * 6
               + f("receptions") + f("receiving_yards") * 0.1 + (f("receiving_yards") >= 100) * 3 + f("receiving_tds") * 6
               - (f("rushing_fumbles_lost") + f("receiving_fumbles_lost") + f("sack_fumbles_lost"))
               + 2 * (f("passing_2pt_conversions") + f("rushing_2pt_conversions") + f("receiving_2pt_conversions"))
               + 6 * f("special_teams_tds"))
    d["team"] = d.team.map(lambda t: FIX.get(t, t))
    skill = d[d.position_group.isin(["QB", "RB", "WR", "TE"])][["player_id", "player_display_name", "team", "position", "dk"]]
    skill.columns = ["gsis_id", "name", "team", "pos", "dk_actual"]
    t = d.groupby("team").agg(sk=("def_sacks", "sum"), it=("def_interceptions", "sum"), fr=("fumble_recovery_opp", "sum"),
                              dtd=("def_tds", "sum"), sttd=("special_teams_tds", "sum"), saf=("def_safeties", "sum"),
                              blk=("def_punt_blocks", "sum"), blk2=("def_fg_blocks", "sum"), blk3=("def_pat_blocks", "sum"))
    s = pd.read_parquet(SCHED)
    s = s[(s.season == a.season) & (s.week == a.week)]
    pa = {}
    for _, g in s.iterrows():
        h, w = FIX.get(g.home_team, g.home_team), FIX.get(g.away_team, g.away_team)
        if pd.notna(g.home_score):
            pa[h], pa[w] = g.away_score, g.home_score
    rows = []
    for tm, r in t.iterrows():
        if tm not in pa:
            continue
        x = pa[tm]
        tier = 10 if x <= 0 else 7 if x <= 6 else 4 if x <= 13 else 1 if x <= 20 else 0 if x <= 27 else -1 if x <= 34 else -4
        pts = r.sk + 2 * r.it + 2 * r.fr + 6 * (r.dtd + r.sttd) + 2 * r.saf + 2 * (r.blk + r.blk2 + r.blk3) + tier
        rows.append(dict(gsis_id=f"DST_{tm}", name=f"{tm} DST", team=tm, pos="DST", dk_actual=float(pts)))
    out = pd.concat([skill, pd.DataFrame(rows)], ignore_index=True)
    out.to_csv(a.out, index=False)
    print(f"week {a.week}: {len(skill)} skill rows, {len(rows)} DST rows, games with a final score: {len(pa) // 2} -> {a.out}")


if __name__ == "__main__":
    main()
