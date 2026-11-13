"""Lineup optimizer on top of the simulator's draws.

IRFL starting rules (MFL TYPE=league, pulled 2026-10-15): 17 starters, 8 of them IDP.
  QB 1 | RB 2-3 | WR 2-4 | TE 1-2 | PK 1 | DT+DE 2-3 | LB 2-3 | CB+S 2-3
So: offense = QB + PK + 7 from RB/WR/TE; defense = 8 from DL/LB/DB.
Every legal slot split is tried and the best players are taken in each group.

python optimize.py 2026 6 [--taxi] [--roster path.json] [--sheet names.json]
  --taxi   treat taxi-squad players as startable (use only if the league lets you activate before lock)

Three lineups are reported:
  EXPECTED   highest average points
  SAFE       highest average after penalising spread (mean - 0.5 sd): protects a favourite
  UPSIDE     highest 90th-percentile outcome per player: for when you are the underdog
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

season, week = int(sys.argv[1]), int(sys.argv[2])
allow_taxi = "--taxi" in sys.argv
SHEET = None                                      # optional: JSON list of player names currently set on MFL
if "--roster" not in sys.argv:                    # 2026-11-12: the default used to be the Week 6 roster file
    raise SystemExit("optimize.py needs --roster <this week's MFL roster json>")
ROSTER = sys.argv[sys.argv.index("--roster") + 1]
if "--sheet" in sys.argv:
    SHEET = sys.argv[sys.argv.index("--sheet") + 1]
SUF = sys.argv[sys.argv.index("--suffix") + 1] if "--suffix" in sys.argv else ""
# 2026-11-12: --blend <roster_compare csv from run_week_play.py> scales each player's draws to the BLEND average, so the
# lineup is picked on the same numbers the report shows (before this the optimizer used the old sim alone).
# --opp <json list of the opponent's starters as gsis ids> scores them on the same simulated games and prints the
# chance each lineup wins. Both sides use the same dice, so shared games are handled properly.
BLEND = sys.argv[sys.argv.index("--blend") + 1] if "--blend" in sys.argv else None
OPP = sys.argv[sys.argv.index("--opp") + 1] if "--opp" in sys.argv else None
base = Path(r"D:\WKP\data\ff-simulator") / f"sim_{season}_wk{week}{SUF}"
z = np.load(str(base) + ".npz")
ids, names, teams, groups, D = z["ids"], z["names"], z["teams"], z["groups"], z["draws"]
idx = {i: n for n, i in enumerate(ids)}

npl = pd.read_parquet(r"D:\WKP\data\nfl\players\players.parquet")[["gsis_id", "espn_id"]].dropna()
npl["espn_id"] = npl.espn_id.astype(str).str.replace(r"\.0$", "", regex=True)
e2g = dict(zip(npl.espn_id, npl.gsis_id))
rows = json.load(open(ROSTER))   # pos,name,team,status,salary,contractYear,proj,inj,mfl,espn
POSMAP = {"QB": "QB", "RB": "RB", "WR": "WR", "TE": "TE", "PK": "PK", "DT": "DL", "DE": "DL", "LB": "LB", "CB": "DB", "S": "DB"}
pool, missing = [], []
for pos, name, nfl, status, sal, cy, proj, inj, mfl, espn in rows:
    g = POSMAP.get(pos)
    if g is None:
        continue
    if status in ("INJURED_RESERVE",) or (status == "TAXI_SQUAD" and not allow_taxi):
        continue
    gid = e2g.get(str(espn).replace(".0", "")) if espn else None
    if gid in idx:
        pool.append(dict(name=name, grp=g, row=idx[gid], nfl=nfl, status=status, inj=inj))
    else:
        missing.append(f"{name} ({nfl}, {g}, {status})")

S = D.shape[1]
if BLEND:
    D = D.astype(np.float32).copy()
    bl = pd.read_csv(BLEND)
    bmean = dict(zip(bl.name, bl.blend))
    for p in pool:
        b, mu = bmean.get(p["name"]), float(D[p["row"]].mean())
        if b == b and b is not None and mu > 0:
            D[p["row"]] *= float(b) / mu
    print("draws scaled to the blend averages from", BLEND)
for p in pool:
    d = D[p["row"]]
    p.update(mean=float(d.mean()), sd=float(d.std()), p10=float(np.percentile(d, 10)), p90=float(np.percentile(d, 90)))

SLOTS = {"QB": (1, 1), "PK": (1, 1)}
combos = []
for rb in (2, 3):
    for wr in (2, 3, 4):
        for te in (1, 2):
            if rb + wr + te == 7:
                for dl, lb, db in itertools.product((2, 3), repeat=3):
                    if dl + lb + db == 8:
                        combos.append(dict(QB=1, PK=1, RB=rb, WR=wr, TE=te, DL=dl, LB=lb, DB=db))


def best_lineup(score):
    by = {g: sorted([p for p in pool if p["grp"] == g], key=lambda p: -score(p)) for g in
          ("QB", "RB", "WR", "TE", "PK", "DL", "LB", "DB")}
    best, best_val = None, -1e9
    for c in combos:
        if any(len(by[g]) < n for g, n in c.items()):
            continue
        pick = [p for g, n in c.items() for p in by[g][:n]]
        v = sum(score(p) for p in pick)
        if v > best_val:
            best, best_val = pick, v
    return best


def dist(pick):
    tot = sum(D[p["row"]].astype(np.float64) for p in pick)
    return tot


def show(title, pick):
    tot = dist(pick)
    print(f"\n{title}: mean {tot.mean():.1f} | sd {tot.std():.1f} | 10th {np.percentile(tot, 10):.1f} | "
          f"90th {np.percentile(tot, 90):.1f}")
    order = ["QB", "RB", "WR", "TE", "PK", "DL", "LB", "DB"]
    for g in order:
        for p in [q for q in pick if q["grp"] == g]:
            print(f"   {g:2s} {p['name']:<22s} {p['nfl']:<4s} mean {p['mean']:5.1f}  sd {p['sd']:4.1f}  "
                  f"range {p['p10']:4.1f} to {p['p90']:4.1f}  {p['inj'] or ''}")
    return tot


print(f"{len(pool)} startable roster players have a simulation; {len(missing)} have none (bye, no team, or no usage):")
print("   " + "; ".join(missing))
L = {
    "EXPECTED": best_lineup(lambda p: p["mean"]),
    "SAFE": best_lineup(lambda p: p["mean"] - 0.5 * p["sd"]),
    "UPSIDE": best_lineup(lambda p: p["p90"]),
}
tots = {k: show(k, v) for k, v in L.items()}
if OPP:
    oids = json.load(open(OPP))
    have = [i for i in oids if i in idx]
    ot = sum(z["draws"][idx[i]].astype(np.float64) for i in have)
    print(f"\nOPPONENT: {len(have)} of {len(oids)} starters have a simulation (the rest count zero). "
          f"mean {ot.mean():.1f} | 10th {np.percentile(ot, 10):.1f} | 90th {np.percentile(ot, 90):.1f} (old sim, no blend for them)")
    for k, t in tots.items():
        print(f"   {k}: wins {np.mean(t > ot):.1%} of simulated weeks (average margin {t.mean() - ot.mean():+.1f})")

# the lineup from the Week 6 pick sheet, scored by the same simulation
doc = json.load(open(SHEET)) if SHEET else []
cur = [p for p in pool if p["name"] in doc]
if doc and len(cur) == len(doc):
    t = show("SAVED LINEUP (the --sheet file)", cur)
    ex = tots["EXPECTED"]
    print(f"\nExpected lineup beats the sheet lineup in {np.mean(ex > t):.0%} of simulated weeks; "
          f"average gain {ex.mean() - t.mean():+.1f} points.")
elif doc:
    print("\n(saved lineup not fully found in pool, these score zero:", [d for d in doc if d not in [p['name'] for p in pool]], ")")

json.dump({k: [p["name"] for p in v] for k, v in L.items()}, open(str(base) + "_lineups.json", "w"), indent=1)
