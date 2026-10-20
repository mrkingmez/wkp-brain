"""Zac's roster: simulator vs MFL projection, plus the top of each position pool.
python roster_compare.py 2026 6
"""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

season, week = int(sys.argv[1]), int(sys.argv[2])
base = Path(r"D:\WKP\data\ff-simulator") / f"sim_{season}_wk{week}"
summ = pd.read_csv(str(base) + "_summary.csv")
npl = pd.read_parquet(r"D:\WKP\data\nfl\players\players.parquet")[["gsis_id", "espn_id"]].dropna()
npl["espn_id"] = npl.espn_id.astype(str).str.replace(r"\.0$", "", regex=True)
e2g = dict(zip(npl.espn_id, npl.gsis_id))
rows = json.load(open(r"D:\WKP\scratch\wk6_roster.json"))   # pos,name,team,status,salary,contractYear,proj,inj,mfl,espn
r = pd.DataFrame(rows, columns=["pos", "name", "nfl", "status", "salary", "cy", "proj", "inj", "mfl", "espn"])
r["gsis_id"] = r.espn.astype(str).str.replace(r"\.0$", "", regex=True).map(e2g)
m = r.merge(summ[["gsis_id", "mean", "sd", "p10", "p50", "p90", "group"]], on="gsis_id", how="left")
m["proj"] = pd.to_numeric(m.proj, errors="coerce")
pd.set_option("display.width", 200)
print(m.sort_values(["pos", "mean"], ascending=[True, False])[
    ["pos", "name", "nfl", "status", "inj", "proj", "mean", "sd", "p10", "p90"]].round(1).to_string(index=False))
ok = m.dropna(subset=["proj", "mean"])
ok = ok[(ok.proj > 0) & (ok["mean"] > 0)]
print(f"\nCorrelation sim mean vs MFL projection: {ok['proj'].corr(ok['mean']):.2f} (n={len(ok)}); "
      f"average sim {ok['mean'].mean():.1f} vs MFL {ok['proj'].mean():.1f}")
print("\nTop 8 per group in the whole league:")
for g in ("QB", "RB", "WR", "TE", "K", "DL", "LB", "DB"):
    print(g, ", ".join(f"{a} {b:.1f}" for a, b in summ[summ.group == g].nlargest(8, "mean")[["name", "mean"]].values))
