"""Lineup-level calibration: projected (old / blend / MFL) vs actual for every franchise's STARTERS, weeks 6-9.
Also Zac's lineup. Writes lineup_calib.csv. Run: python -I lineup_calib.py"""
import json, sys
import pandas as pd, numpy as np
LAST=int(sys.argv[1]) if len(sys.argv)>1 else 9
from pathlib import Path
H=Path(r"D:\WKP\Fantasy-Football\fixes-2026-11-10"); C=H/"mfl_cache"
D=pd.read_csv(H/"dataset.csv")
rows=[];det=[]
for w in range(6,LAST+1):
    wr=json.load(open(C/f"weeklyResults_w{w}.json",encoding="utf-8-sig"))["weeklyResults"]["matchup"]
    d=D[D.week==w].dropna(subset=["mfl"]).copy(); d["mfl"]=d.mfl.astype(int).astype(str); d=d.drop_duplicates("mfl").set_index("mfl")
    for m in wr:
        for f in m["franchise"]:
            st=[p for p in f["player"] if p["status"]=="starter"]
            pr=dict(old=0.,blend=0.,mfl=0.,n=0,act=0.,miss=0)
            for p in st:
                a=float(p.get("score") or 0); pr["act"]+=a
                if p["id"] in d.index:
                    r=d.loc[p["id"]]; pr["old"]+=r.old; pr["blend"]+=r.blend; pr["n"]+=1
                else: pr["miss"]+=1
                det.append(dict(week=w,fr=f["id"],id=p["id"],actual=a,proj_old=d.old.get(p["id"]),proj_blend=d.blend.get(p["id"]),proj_mfl=d.mfl_proj.get(p["id"]),grp=d.group.get(p["id"])))
            rows.append(dict(week=w,fr=f["id"],score_reported=float(f["score"]),**pr))
L=pd.DataFrame(rows); L.to_csv(H/"lineup_calib.csv",index=False)
print(L[L.fr=="0012"].round(1).to_string())
ok=L[L.miss<=2]  # lineups with nearly all starters projected
for c in ["old","blend"]:
    e=ok.act-ok[c]; print(c,"lineups",len(ok),"bias",round(e.mean(),1),"sd",round(e.std(),1),"mae",round(e.abs().mean(),1),"corr",round(np.corrcoef(ok[c],ok.act)[0,1],2),"slope",round(np.polyfit(ok[c],ok.act,1)[0],2))
print(ok.groupby("fr").apply(lambda x:(x.act-x.blend).mean()).round(1).to_dict())
z=ok[ok.fr=="0012"]; e=z.act-z.blend; print("Zac blend bias",e.mean().round(1),"per week",e.round(1).tolist())
pd.DataFrame(det).to_csv(H/"starters_detail.csv",index=False)
