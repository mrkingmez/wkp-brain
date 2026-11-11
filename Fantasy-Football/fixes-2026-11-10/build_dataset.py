"""Joins sim projections (old sim, play sim, MFL projection) to actual MFL player scores, weeks 6-9.
Run: python -I build_dataset.py   (writes dataset.csv)
Actuals = MFL TYPE=playerScores (league scoring, not raw stats: allowed). Missing row = 0.
"""
import json, sys
import re
LAST=int(sys.argv[1]) if len(sys.argv)>1 else 9
import pandas as pd
from pathlib import Path
H=Path(r"D:\WKP\Fantasy-Football\fixes-2026-11-10"); C=H/"mfl_cache"
SK=Path(r"D:\WKP\.claude\skills\fantasy-football-data"); DS=Path(r"D:\WKP\data\ff-simulator"); PS=Path(r"D:\WKP\data\ff-play-sim")
det=pd.DataFrame(json.load(open(SK/"players-cache-details.json",encoding="utf-8"))["players"]["player"])
sl=json.load(open(SK/"sleeper-players-cache.json",encoding="utf-8"))
sl=pd.DataFrame([{"espn_id":str(v.get("espn_id") or ""),"gsis_id":v.get("gsis_id")} for v in sl.values() if v.get("gsis_id") and v.get("espn_id")])
br=det[["id","name","position","team","espn_id"]].copy(); br["espn_id"]=br.espn_id.astype(str)
br=br.merge(sl.drop_duplicates("espn_id"),on="espn_id",how="left").rename(columns={"id":"mfl"})
def norm(n):
    n=str(n)
    if "," in n: a,b=n.split(",",1); n=b+" "+a
    n=re.sub(r"[.,'’]","",n.lower()); n=re.sub(r"(jr|sr|ii|iii|iv|v)","",n); return re.sub(r"\s+"," ",n).strip()
TF={"WSH":"WAS","LAR":"LA","JAC":"JAX","LVR":"LV","GBP":"GB","KCC":"KC","NEP":"NE","NOS":"NO","SFO":"SF","TBB":"TB"}
det["k"]=det.name.map(norm)+"|"+det.team.replace(TF)
namebr=det.drop_duplicates("k").set_index("k").id
print("bridge matched", br.gsis_id.notna().sum(),"of",len(br))
rows=[]
for w in range(6,LAST+1):
    act={x["id"]:float(x["score"]) for x in json.load(open(C/f"playerScores_w{w}.json",encoding="utf-8-sig"))["playerScores"]["playerScore"]}
    mp={x["id"]:float(x["score"]) for x in json.load(open(C/f"projectedScores_w{w}.json",encoding="utf-8-sig"))["projectedScores"]["playerScore"] if x.get("score") not in ("",None)}
    old=pd.read_csv(DS/f"sim_2026_wk{w}_summary.csv")
    pl=pd.read_csv(PS/f"play_sim_2026_wk{w}.csv") if (PS/f"play_sim_2026_wk{w}.csv").exists() else None
    d=old.rename(columns={"mean":"old","sd":"old_sd"})[["gsis_id","name","team","group","old","old_sd","p10","p90","questionable"]]
    if pl is not None: d=d.merge(pl[["gsis_id","new","opp"]],on="gsis_id",how="left")
    else: d["new"]=float("nan"); d["opp"]=""
    d=d.merge(br[["mfl","gsis_id"]].drop_duplicates("gsis_id"),on="gsis_id",how="left")
    d["k"]=d.name.map(norm)+"|"+d.team.replace(TF)
    d["mfl"]=d.mfl.fillna(d.k.map(namebr))
    d["week"]=w; d["actual"]=d.mfl.map(act); d["mfl_proj"]=d.mfl.map(mp)
    d["on_mfl_scores"]=d.actual.notna(); d["actual"]=d.actual.fillna(0.0)
    rows.append(d)
D=pd.concat(rows); 
W={"QB":.9,"PK":.5,"K":.5,"RB":.15,"WR":.2,"TE":.2}
D["w_new"]=D.group.map(W).fillna(0.0)
D["blend"]=[o if pd.isna(n) else (1-w)*o+w*n for o,n,w in zip(D.old,D.new,D.w_new)]
D.to_csv(H/"dataset.csv",index=False)
print(D.groupby("week").agg(n=("old","size"),mfl_matched=("mfl",lambda s:s.notna().sum()),with_play=("new",lambda s:s.notna().sum())))
print(D.group.value_counts())
