"""Scores v2 lineup sets on the ONE real slate we have (Week 9, DK, realized from nflverse, DST excluded for every lineup alike). n=1: illustration, not evidence."""
import subprocess, sys, pandas as pd, numpy as np
from dk_realized import dk_points, norm
D=dk_points(2026,9)
runs={"v2 gpp stack":[],"v2 gpp stack+bringback":["--bringback"],"v2 cash (line 130)":["--mode","cash"],"v2 gpp NO stack, punt allowed":["--no-stack","--allow-punt","--min-qb-salary","0"]}
res=[]
for k,extra in runs.items():
    subprocess.run([sys.executable,"-I","dfs_optimize_v2.py","dk",r"D:\WKP\scratch\DKSalaries-2026-11-07.csv","--week","9","--n","10"]+extra,capture_output=True)
    l=pd.read_csv("dfs_v2_lineups_%s_wk9.csv"%("cash" if "cash" in k else "gpp")); l["key"]=l.name.map(norm); l["team"]=l.team.replace({"LAR":"LA","JAC":"JAX","WSH":"WAS"})
    m=l[l.pos!="DST"].merge(D,on=["key","team"],how="left"); s=m.groupby("lineup").dk.sum(); s_un=m.groupby("lineup").dk.apply(lambda x:x.isna().sum())
    res.append((k,s.values)); print(f"{k:34s} lineups {len(s)}  realized (no DST): mean {s.mean():.1f}  best {s.max():.1f}  worst {s.min():.1f}  unmatched players {int(s_un.sum())}")
print("Zac's two as run (CSV): 121.4 and 143.2 (no DST)")
print("Hindsight: slate best QB/RB/WR/TE points ignoring salary are not computed here.")
