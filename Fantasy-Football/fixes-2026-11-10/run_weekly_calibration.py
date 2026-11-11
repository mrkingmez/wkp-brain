"""Fix 2: weekly calibration of the lineup sims against MFL results. Run every Tuesday after Monday Night Football.
    python -I run_weekly_calibration.py <last_completed_week>
Steps: (1) read-only MFL pulls for weeks 6..N (playerScores, weeklyResults, projectedScores) into mfl_cache,
(2) join to sim summaries (old sim, play sim, blend) -> dataset.csv, (3) lineup-level table for all 12 franchises -> lineup_calib.csv,
(4) print the numbers that matter: bias, spread, 80% range to quote next to a projection, and the per-position slope check.
Needs MFL_API_KEY in the environment. Never writes to MFL. Sim files must exist for each week (sim_2026_wkN_summary.csv)."""
import os, sys, subprocess, urllib.request
from pathlib import Path
import numpy as np, pandas as pd
H=Path(__file__).parent; N=int(sys.argv[1]); key=os.environ.get("MFL_API_KEY")
if not key: sys.exit("MFL_API_KEY not set: NOT AVAILABLE, nothing pulled")
for w in range(1,N+1):
    for t in ("playerScores","weeklyResults","projectedScores"):
        f=H/"mfl_cache"/f"{t}_w{w}.json"
        if not f.exists() or w>=N-1:
            u=f"https://www44.myfantasyleague.com/2026/export?TYPE={t}&L=43094&APIKEY={key}&JSON=1&W={w}"
            f.write_bytes(urllib.request.urlopen(u,timeout=60).read())
for s in ("build_dataset.py","lineup_calib.py"):
    r=subprocess.run([sys.executable,"-I",str(H/s),str(N)],capture_output=True,text=True,cwd=H); 
    if r.returncode: sys.exit(r.stderr[-800:])
L=pd.read_csv(H/"lineup_calib.csv",dtype={"fr":str}); ok=L[L.miss<=2]; e=ok.act-ok.blend; sd=e.std()
print(f"Weeks 6-{N}: {len(ok)} lineups (12 franchises x weeks, <=2 starters unmatched)")
print(f"Lineup total, actual minus blend projection: bias {e.mean():+.1f}, SD {sd:.1f}, MAE {e.abs().mean():.1f}; slope of actual on projection {np.polyfit(ok.blend,ok.act,1)[0]:.2f}")
z=ok[ok.fr=="0012"]; ez=z.act-z.blend; print(f"Zac's lineups: bias {ez.mean():+.1f} (n={len(z)}), by week {ez.round(1).tolist()}")
print(f"RANGE TO QUOTE: projection +/- {1.28*sd:.0f} is an 80% range (one-sigma {sd:.0f}). Head to head: win prob = Phi((mine-theirs)/{sd*2**.5:.0f}).")
D=pd.read_csv(H/"dataset.csv"); R=D[D.mfl.notna()&(D.blend>=3)]
for g,x in R.groupby("group"):
    b,a=np.polyfit(x.blend,x.actual,1); print(f"  {g:3s} n={len(x):4d} bias {(x.actual-x.blend).mean():+.2f} slope {b:.2f}")
print("Rule: act on a shrink only if the slope is below 0.85 for a position over 3+ new weeks AND the leave-one-week-out RMSE (recal.py) improves.")
log=H/"calibration_log.csv"; row=pd.DataFrame([dict(through_week=N,n=len(ok),bias=round(e.mean(),2),sd=round(sd,2),zac_bias=round(ez.mean(),2))])
row.to_csv(log,mode="a",header=not log.exists(),index=False)
