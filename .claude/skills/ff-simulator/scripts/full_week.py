"""Full-week simulation report: every game's box score, winners, five IRFL lineups, DraftKings/FanDuel points.

python full_week.py 2026 6 [--sims 4000] [--odds <json>] [--md <out.md>]

One pass of the game simulator keeps every simulated stat line, so the same 4,000 simulated weeks give
  - team and player box scores per game (means and 10th-90th ranges)
  - win and cover probabilities (the sim is anchored on the market line, so these ARE the market's odds;
    power_rating.py tested an independent football-only rating and it did not beat the market)
  - five IRFL lineups scored on the same draws
  - DraftKings and FanDuel fantasy points per player (for dfs_optimize.py once a salary file exists)
Roster and statuses: D:\\WKP\\scratch\\wk6_roster.json (MFL pull). Golden is treated as active (signed 2026-10-15).
"""
import argparse
import itertools
import json
import sys
from math import erf, sqrt
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import run_week as rw

OUT = Path(r"D:\WKP\data\ff-simulator")
ACTIVE_OVERRIDE = {"Golden, Matthew"}          # taxi players now on the active roster
POSMAP = {"QB": "QB", "RB": "RB", "WR": "WR", "TE": "TE", "PK": "PK", "DT": "DL", "DE": "DL", "LB": "LB", "CB": "DB", "S": "DB"}
Phi = lambda x: 0.5 * (1 + erf(x / sqrt(2)))


# ------------------------------------------------------------------ fantasy scoring on raw stat lines
def dk_pts(b):
    py, ry, cy = b["pass_yd"], b["rush_yd"], b["rec_yd"]
    return (py * 0.04 + (py >= 300) * 3 + b["ptd"] * 4 - b["ints"] + ry * 0.1 + (ry >= 100) * 3 + b["rtd"] * 6
            + b["rec"] + cy * 0.1 + (cy >= 100) * 3 + b["rcd"] * 6 - b["fum"])


def fd_pts(b):
    return (b["pass_yd"] * 0.04 + b["ptd"] * 4 - b["ints"] + b["rush_yd"] * 0.1 + b["rtd"] * 6 + b["rec"] * 0.5
            + b["rec_yd"] * 0.1 + b["rcd"] * 6 - 2 * b["fum"])


def ms(a):
    a = np.asarray(a, float)
    return a.mean(), np.percentile(a, 10), np.percentile(a, 90)


def stat_line(b):
    g = b["group"]
    f = lambda k: float(np.mean(b[k]))
    if g == "QB":
        return f"{f('pass_yd'):.0f} pass yd, {f('ptd'):.1f} TD, {f('ints'):.1f} INT" + (f"; {f('rush'):.1f} rush, {f('rush_yd'):.0f} yd" if f("rush") > 1 else "")
    if g in ("RB", "WR", "TE"):
        run = f"{f('rush'):.1f} car, {f('rush_yd'):.0f} yd, {f('rtd'):.2f} TD; " if f("rush") >= 0.5 or g == "RB" else ""
        return f"{run}{f('rec'):.1f} rec, {f('rec_yd'):.0f} yd, {f('rcd'):.2f} TD"
    if g == "K":
        return f"{f('fg'):.1f} FG, {f('xp'):.1f} XP"
    return f"{f('solo'):.1f} solo, {f('ast'):.1f} ast, {f('sck'):.2f} sack, {f('pdf'):.2f} PD, {f('dint'):.2f} INT"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("season", type=int)
    ap.add_argument("week", type=int)
    ap.add_argument("--sims", type=int, default=4000)
    ap.add_argument("--odds", default=r"D:\WKP\scratch\wk6_odds.json")
    ap.add_argument("--md", default=r"D:\WKP\Fantasy-Football\reports\Week6-Full-Simulation-2026-10-15.md")
    ap.add_argument("--seed", type=int, default=2026)
    a = ap.parse_args()
    season, week = a.season, a.week

    tg, lg, pw, defs, lg_def, sched = rw.load_all(season, week)
    lines = rw.market_lines(a.odds)
    drops, quest = rw.injury_sets()
    boxes = {}
    ids, results, M, envs, dropped = rw.simulate_week(season, week, lines, tg, lg, pw, defs, lg_def, sched, drops, quest,
                                                      a.sims, a.seed, boxes=boxes)
    S = M.shape[1]
    idx = {i: n for n, i in enumerate(ids)}
    rng = np.random.default_rng(7)

    # ------------------------------------------------ DFS draws (same availability and widening as the IRFL draws)
    dfs = {}
    for gk, bx in boxes.items():
        for pid, b in bx.items():
            if pid == "_game":
                continue
            if b["group"] in ("QB", "RB", "WR", "TE"):
                dk, fd = dk_pts(b), fd_pts(b)
                for arr_name, arr in (("dk", dk), ("fd", fd)):
                    mu = arr.mean()
                    arr = np.maximum(mu + rw.OFFENSE_WIDEN * (arr - mu), -4.0)
                    if pid in quest and b["group"] != "QB":
                        arr = arr * (rng.random(S) < rw.QUESTIONABLE_PLAY_RATE)
                    dfs.setdefault(pid, {})[arr_name] = arr.astype(np.float32)
                dfs[pid].update(name=b["name"], team=b["team"], group=b["group"])
            elif b["group"] == "K":
                fd = b["fg"] * 3.4 + b["xp"]
                dfs.setdefault(pid, {})["fd"] = fd.astype(np.float32)
                dfs[pid].update(name=b["name"], team=b["team"], group="K")
    dpids = list(dfs)
    np.savez_compressed(OUT / f"dfs_draws_{season}_wk{week}.npz", ids=np.array(dpids),
                        names=np.array([dfs[p]["name"] for p in dpids]), teams=np.array([dfs[p]["team"] for p in dpids]),
                        groups=np.array([dfs[p]["group"] for p in dpids]),
                        dk=np.stack([dfs[p].get("dk", np.zeros(S, np.float32)) for p in dpids]),
                        fd=np.stack([dfs[p].get("fd", np.zeros(S, np.float32)) for p in dpids]))
    dfs_rows = []
    for p in dpids:
        d = dfs[p]
        dkm, fdm = (ms(d["dk"]) if "dk" in d else (np.nan,) * 3), ms(d["fd"])
        dfs_rows.append(dict(gsis_id=p, name=d["name"], team=d["team"], pos=d["group"], p_play=0.75 if p in quest else 1.0,
                             dk_mean=dkm[0], dk_p10=dkm[1], dk_p90=dkm[2], fd_mean=fdm[0], fd_p10=fdm[1], fd_p90=fdm[2],
                             irfl_mean=float(M[idx[p]].mean()) if p in idx else np.nan))
    dfs_df = pd.DataFrame(dfs_rows).sort_values("fd_mean", ascending=False)
    dfs_df.to_csv(OUT / f"dfs_projections_{season}_wk{week}.csv", index=False)

    # ------------------------------------------------ IRFL roster pool and five lineups
    npl = pd.read_parquet(r"D:\WKP\data\nfl\players\players.parquet")[["gsis_id", "espn_id"]].dropna()
    npl["espn_id"] = npl.espn_id.astype(str).str.replace(r"\.0$", "", regex=True)
    e2g = dict(zip(npl.espn_id, npl.gsis_id))
    rows = json.load(open(r"D:\WKP\scratch\wk6_roster.json"))
    pool, missing = [], []
    for pos, name, nfl, status, sal, cy, proj, inj, mfl, espn in rows:
        g = POSMAP.get(pos)
        if g is None:
            continue
        if status == "INJURED_RESERVE" or (status == "TAXI_SQUAD" and name not in ACTIVE_OVERRIDE):
            continue
        gid = e2g.get(str(espn).replace(".0", "")) if espn else None
        if gid in idx:
            d = M[idx[gid]]
            pool.append(dict(name=name, grp=g, row=idx[gid], nfl=nfl, gid=gid, quest=gid in quest, mean=float(d.mean()),
                             sd=float(d.std()), p10=float(np.percentile(d, 10)), p75=float(np.percentile(d, 75)),
                             p90=float(np.percentile(d, 90))))
        else:
            missing.append(f"{name} ({nfl})")
    combos = []
    for rb in (2, 3):
        for wr in (2, 3, 4):
            for te in (1, 2):
                if rb + wr + te == 7:
                    for dl, lb, db in itertools.product((2, 3), repeat=3):
                        if dl + lb + db == 8:
                            combos.append(dict(QB=1, PK=1, RB=rb, WR=wr, TE=te, DL=dl, LB=lb, DB=db))

    def best(score, exclude_quest=False):
        by = {g: sorted([p for p in pool if p["grp"] == g and not (exclude_quest and p["quest"])], key=lambda p: -score(p))
              for g in ("QB", "RB", "WR", "TE", "PK", "DL", "LB", "DB")}
        bp, bv = None, -1e9
        for c in combos:
            if any(len(by[g]) < n for g, n in c.items()):
                continue
            pick = [p for g, n in c.items() for p in by[g][:n]]
            v = sum(score(p) for p in pick)
            if v > bv:
                bp, bv = pick, v
        return bp

    LU = {
        "1 EXPECTED (highest average)": best(lambda p: p["mean"]),
        "2 SAFE (protects a lead)": best(lambda p: p["mean"] - 0.5 * p["sd"]),
        "3 BALANCED UPSIDE (75th percentile)": best(lambda p: p["p75"]),
        "4 SWING (90th percentile, for an underdog)": best(lambda p: p["p90"]),
        "5 CONTINGENCY (every Questionable out)": best(lambda p: p["mean"], exclude_quest=True),
    }
    order = ["QB", "RB", "WR", "TE", "PK", "DL", "LB", "DB"]
    lu_tot = {k: sum(M[p["row"]].astype(np.float64) for p in v) for k, v in LU.items()}
    doc = ["Brissett, Jacoby", "Croskey-Merritt, Jacory", "White, Rachaad", "Flowers, Zay", "Allen, Keenan", "Flournoy, Ryan",
           "Goedert, Dallas", "Schultz, Dalton", "Folk, Nick", "Davis, Jordan", "Kancey, Calijah", "Okereke, Bobby",
           "Strnad, Justin", "Dodson, Tyrel", "Kinchens, Kamren", "Jenkins, Rayshawn", "Mukuba, Andrew"]
    sheet = [p for p in pool if p["name"] in doc]
    sheet_tot = sum(M[p["row"]].astype(np.float64) for p in sheet) if len(sheet) == len(doc) else None

    # ------------------------------------------------ pick'em tables
    pk = pd.read_csv(OUT / f"pickem_probs_{season}_wk{week}.csv")
    gm_rows = []
    for gk, bx in boxes.items():
        G = bx["_game"]
        h, aw = G["home"], G["away"]
        sp, tot = lines[(aw, h)]
        ph = float((G["margin"] > 0).mean())
        gm_rows.append(dict(key=gk, away=aw, home=h, spread=sp, total=tot, p_home=ph, pts_h=float(np.mean(G["pts"][h])),
                            pts_a=float(np.mean(G["pts"][aw])), med_margin=float(np.median(G["margin"]))))
    gdf = pd.DataFrame(gm_rows)

    # ------------------------------------------------ write markdown
    L = []
    w = L.append
    w(f"# Week {week} Full Simulation Report - 15 OCT 2026")
    w("")
    w("Decision support only. Nothing was submitted anywhere. Every number comes from 4,000 simulated versions of each game, "
      "built from the live betting line, each coach's own tendencies, injuries as of this pull, and each player's recent usage.")
    w("")
    w("## 1. Winners and pick'em")
    w("")
    w("The simulator draws each game's score from the market line, so its win odds are the market's odds. I also built a "
      "football-only rating (opponent-adjusted EPA per play) and tested it against 388 real games from 2024 and 2025: blended "
      "with the market it made the picks slightly worse (average miss 9.80 vs 9.64 points), so the market stays the winner "
      "predictor. Your edge on the card is the gap between the frozen card line and today's market, not a better read on who wins.")
    w("")
    w("| Game | Favorite (sim win %) | Sim score | Your ATS pick | Cover % | Your SU pick | SU win % |")
    w("|---|---|---|---|---|---|---|")
    for _, r in gdf.iterrows():
        fav, pf = (r.home, r.p_home) if r.p_home >= 0.5 else (r.away, 1 - r.p_home)
        pr = pk[pk.game.apply(lambda s: s.split(" @ ")[0].replace("LAR", "LA").replace("WSH", "WAS") == r.away and s.split(" @ ")[1].replace("LAR", "LA").replace("WSH", "WAS") == r.home)]
        if len(pr):
            x = pr.iloc[0]
            ats, cov, su, pw_ = x.ats_pick, f"{x.p_cover:.1%}", x.su_pick, f"{x.p_win:.1%}"
        else:
            ats = cov = su = pw_ = "-"
        w(f"| {r.away} @ {r.home} | {fav} {pf:.1%} | {r.away} {r.pts_a:.1f} - {r.home} {r.pts_h:.1f} | {ats} | {cov} | {su} | {pw_} |")
    w("")
    flip = pk[pk.p_win < 0.5]
    if len(flip):
        for _, x in flip.iterrows():
            w(f"**Flag:** the straight-up pick {x.su_pick} in {x.game} is the market underdog ({x.p_win:.1%}). "
              f"It is a coin flip; the other side is the market favorite. Your call.")
            w("")
    w("**Eliminator (fresh start this week, every team open):** best win chances are LA Rams 83.7%, KC 73.5%, SF 72.2%, "
      "IND and NE 70.9%. Surviving all season means saving the biggest favorites for the weeks with weaker options, "
      "so the Rams are the safe pick now but not automatically the smart one. I can plan the full 18 weeks once the schedule "
      "odds are loaded.")
    w("")

    w("## 2. Five IRFL lineups (Golden active)")
    w("")
    w("| Lineup | Average | 10th | 90th |")
    w("|---|---|---|---|")
    for k, t in lu_tot.items():
        w(f"| {k} | {t.mean():.1f} | {np.percentile(t, 10):.1f} | {np.percentile(t, 90):.1f} |")
    if sheet_tot is not None:
        w(f"| Week 6 sheet lineup (for comparison) | {sheet_tot.mean():.1f} | {np.percentile(sheet_tot, 10):.1f} | {np.percentile(sheet_tot, 90):.1f} |")
    w("")
    base = LU["1 EXPECTED (highest average)"]
    base_names = {p["name"] for p in base}
    for k, v in LU.items():
        w(f"**{k}**")
        w("")
        w("| Slot | Player | Team | Avg | Range (10th to 90th) | Note |")
        w("|---|---|---|---|---|---|")
        for g in order:
            for p in [q for q in v if q["grp"] == g]:
                note = ("Questionable, plays about 75% of sims. " if p["quest"] else "") + ("differs from lineup 1" if p["name"] not in base_names and k[0] != "1" else "")
                w(f"| {g} | {p['name']} | {p['nfl']} | {p['mean']:.1f} | {p['p10']:.1f} to {p['p90']:.1f} | {note.strip()} |")
        w("")
    keys = list(LU)
    same = [(keys[i][0], keys[j][0]) for i in range(len(keys)) for j in range(i + 1, len(keys))
            if {p["name"] for p in LU[keys[i]]} == {p["name"] for p in LU[keys[j]]}]
    if same:
        w("Lineups " + "; ".join(f"{x} and {y} are identical" for x, y in same) + ". Your roster has few real choices this week "
          "(the only live decisions are QB, the last DB slot and the last WR slot), so the five lineups collapse. "
          "Averages shift by about half a point between runs because the dice differ.")
        w("")
    w(f"Not simulated this week (bye, no team, or no recent usage): {'; '.join(missing)}.")
    w("")
    w("When the two free agents land (a safety and a defensive end), I will add them for Week 7. Defensive line is the thinnest group: "
      "Davis and Kancey are the only two playable linemen this week.")
    w("")

    w("## 3. Game by game: simulated box scores")
    w("")
    w("Player lines are averages across the simulated games where he plays; Questionable players are marked. "
      "Fantasy points are IRFL scoring. Treat any single stat as a range: the 10th-to-90th spread on a receiver's yards is wide.")
    w("")
    for _, r in gdf.sort_values("key").iterrows():
        bx = boxes[r.key]
        G = bx["_game"]
        w(f"### {r.away} @ {r.home}")
        w("")
        w(f"Market: {r.home} {-r.spread:+.1f}, total {r.total:.1f}. Sim: {r.away} {r.pts_a:.1f}, {r.home} {r.pts_h:.1f}. "
          f"{r.home} wins {r.p_home:.1%}, {r.away} wins {1 - r.p_home:.1%}. Median margin {r.med_margin:+.1f} for {r.home}.")
        w("")
        w("| Team stat | " + r.away + " | " + r.home + " |")
        w("|---|---|---|")
        sa, sh = G["sim"][r.away], G["sim"][r.home]
        tm = lambda s, k: float(np.mean(s[k]))
        w(f"| Plays | {tm(sa, 'plays'):.0f} | {tm(sh, 'plays'):.0f} |")
        w(f"| Pass attempts / completions | {tm(sa, 'att'):.0f} / {tm(sa, 'comp'):.0f} | {tm(sh, 'att'):.0f} / {tm(sh, 'comp'):.0f} |")
        w(f"| Passing yards | {tm(sa, 'pass_yds'):.0f} | {tm(sh, 'pass_yds'):.0f} |")
        w(f"| Rush attempts / yards | {tm(sa, 'carries'):.0f} / {tm(sa, 'rush_yds'):.0f} | {tm(sh, 'carries'):.0f} / {tm(sh, 'rush_yds'):.0f} |")
        w(f"| Sacks taken | {tm(sa, 'sacks'):.1f} | {tm(sh, 'sacks'):.1f} |")
        w(f"| Interceptions thrown | {tm(sa, 'ints'):.1f} | {tm(sh, 'ints'):.1f} |")
        w(f"| Passing / rushing TDs | {tm(sa, 'ptd'):.1f} / {tm(sa, 'rtd'):.1f} | {tm(sh, 'ptd'):.1f} / {tm(sh, 'rtd'):.1f} |")
        w(f"| Field goals | {tm(sa, 'fgm'):.1f} | {tm(sh, 'fgm'):.1f} |")
        w("")
        for team in (r.away, r.home):
            mem = [(pid, b) for pid, b in bx.items() if pid != "_game" and b["team"] == team and pid in idx]
            def mean_of(pid): return float(M[idx[pid]].mean())
            sel = []
            for grp, n in (("QB", 1), ("RB", 3), ("WR", 4), ("TE", 2), ("K", 1), ("DL", 2), ("LB", 3), ("DB", 3)):
                c = sorted([m for m in mem if m[1]["group"] == grp], key=lambda m: -mean_of(m[0]))[:n]
                sel += c
            w(f"**{team}**")
            w("")
            w("| Pos | Player | IRFL pts | Stat line | Note |")
            w("|---|---|---|---|---|")
            for pid, b in sel:
                if mean_of(pid) < 0.6 and b["group"] not in ("QB", "K"):
                    continue
                note = "Questionable" if pid in quest else ""
                w(f"| {b['group']} | {b['name']} | {mean_of(pid):.1f} | {stat_line(b)} | {note} |")
            w("")
    dn = [f"{t}: {n}" for t, n in dropped]
    if dn:
        w(f"Players removed as Out/Doubtful/IR before simulating, with their usage handed to teammates: {', '.join(dn)}.")
        w("")

    w("## 4. DraftKings and FanDuel")
    w("")
    w("Points use each site's classic scoring as I know it (DraftKings: full PPR, 3-point bonuses at 100 rush/rec and 300 pass yards, "
      "-1 INT and fumble; FanDuel: half PPR, -2 fumble, kicker FG about 3.4). Verify the rules on the slate page before building lineups. "
      "Lineups with a salary cap need the slate's salary file, which has to be downloaded from each site by you. "
      "The tool that builds them is `dfs_optimize.py` and it is ready for that file.")
    w("")
    for site, col, lo, hi in (("DraftKings", "dk_mean", "dk_p10", "dk_p90"), ("FanDuel", "fd_mean", "fd_p10", "fd_p90")):
        w(f"**Top projected, {site}**")
        w("")
        w("| Pos | Player | Team | Avg | 10th to 90th |")
        w("|---|---|---|---|---|")
        sub = dfs_df.dropna(subset=[col]).sort_values(col, ascending=False)
        for pos, n in (("QB", 6), ("RB", 10), ("WR", 12), ("TE", 6)) + ((("K", 4),) if site == "FanDuel" else ()):
            for _, x in sub[sub.pos == pos].head(n).iterrows():
                w(f"| {pos} | {x['name']} | {x.team} | {x[col]:.1f} | {x[lo]:.1f} to {x[hi]:.1f} |")
        w("")

    w("## 5. Limits")
    w("")
    w("- The coaching table covers head coaches. nflverse has no play-caller field, so a coordinator who calls plays is "
      "not separated out, and first-year head coaches (BAL, CLE, LV, MIA) lean on team history.")
    w("- Backtest (18 weeks, 14,848 player-weeks): 3 to 6 percent less error than a recent average for QB, RB, WR, TE and K; a tie on defenders.")
    w("- Injury statuses came from MFL at the time of the pull. Re-run Thursday morning and Sunday morning for fresh news.")
    w("- Weather, referee tendencies and in-game injuries are not modeled.")
    Path(a.md).write_text("\n".join(L), encoding="utf-8")
    json.dump({k: [p["name"] for p in v] for k, v in LU.items()}, open(OUT / f"lineups5_{season}_wk{week}.json", "w"), indent=1)
    print("wrote", a.md)
    for k, t in lu_tot.items():
        print(f"{k}: {t.mean():.1f}")


if __name__ == "__main__":
    main()
