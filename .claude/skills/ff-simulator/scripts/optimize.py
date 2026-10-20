"""Lineup optimizer on top of the simulator's draws.

IRFL starting rules (MFL TYPE=league, pulled 2026-10-15): 17 starters, 8 of them IDP.
  QB 1 | RB 2-3 | WR 2-4 | TE 1-2 | PK 1 | DT+DE 2-3 | LB 2-3 | CB+S 2-3
So: offense = QB + PK + 7 from RB/WR/TE; defense = 8 from DL/LB/DB.
Every legal slot split is tried and the best players are taken in each group.

python optimize.py 2026 6 [--taxi]
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
base = Path(r"D:\WKP\data\ff-simulator") / f"sim_{season}_wk{week}"
z = np.load(str(base) + ".npz")
ids, names, teams, groups, D = z["ids"], z["names"], z["teams"], z["groups"], z["draws"]
idx = {i: n for n, i in enumerate(ids)}

npl = pd.read_parquet(r"D:\WKP\data\nfl\players\players.parquet")[["gsis_id", "espn_id"]].dropna()
npl["espn_id"] = npl.espn_id.astype(str).str.replace(r"\.0$", "", regex=True)
e2g = dict(zip(npl.espn_id, npl.gsis_id))
rows = json.load(open(r"D:\WKP\scratch\wk6_roster.json"))   # pos,name,team,status,salary,contractYear,proj,inj,mfl,espn
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

# the lineup from the Week 6 pick sheet, scored by the same simulation
doc = ["Brissett, Jacoby", "Croskey-Merritt, Jacory", "White, Rachaad", "Flowers, Zay", "Allen, Keenan",
       "Flournoy, Ryan", "Goedert, Dallas", "Schultz, Dalton", "Folk, Nick", "Davis, Jordan", "Kancey, Calijah",
       "Okereke, Bobby", "Strnad, Justin", "Dodson, Tyrel", "Kinchens, Kamren", "Jenkins, Rayshawn", "Mukuba, Andrew"]
cur = [p for p in pool if p["name"] in doc]
if len(cur) == len(doc):
    t = show("SHEET LINEUP (what the Week 6 sheet recommended)", cur)
    ex = tots["EXPECTED"]
    print(f"\nExpected lineup beats the sheet lineup in {np.mean(ex > t):.0%} of simulated weeks; "
          f"average gain {ex.mean() - t.mean():+.1f} points.")
else:
    print("\n(sheet lineup not fully found in pool:", [d for d in doc if d not in [p['name'] for p in pool]], ")")

json.dump({k: [p["name"] for p in v] for k, v in L.items()}, open(str(base) + "_lineups.json", "w"), indent=1)
