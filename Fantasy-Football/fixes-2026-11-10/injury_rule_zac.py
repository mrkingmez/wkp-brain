"""Fix 3 backtest on Zac's own roster, weeks 6-9, league scoring (MFL playerScores), all positions incl IDP.
Compares: saved starters (what Zac actually ran), model lineup (blend, as the reports built it), rule lineup (blend with
Questionable x practice haircut + backup-QB haircut), and the hindsight optimum.
Injury status = nflverse injuries_2026 (LAST report of the week, usually Friday: more informative than the Thursday lock,
so this flatters the rule; flagged in the report)."""
import json, pandas as pd, numpy as np
from pathlib import Path
from scipy.optimize import milp, LinearConstraint, Bounds
H=Path(r"D:\WKP\Fantasy-Football\fixes-2026-11-10"); C=H/"mfl_cache"
D=pd.read_csv(H/"dataset.csv"); D=D[D.mfl.notna()].copy(); D["mfl"]=D.mfl.astype(int).astype(str)
INJ=pd.read_csv(H/"nfl_cache/injuries_2026.csv",low_memory=False)
bridge=D.drop_duplicates("gsis_id").set_index("gsis_id").mfl
INJ["mfl"]=INJ.gsis_id.map(bridge)
def pc(p): return "none" if not isinstance(p,str) else ("DNP" if p.startswith("Did Not") else "LP" if p.startswith("Limited") else "FP")
INJ["pc"]=INJ.practice_status.map(pc); INJ["rs"]=INJ.report_status.fillna("none")
# multipliers RELATIVE to the sim's own value (sim plays a Questionable 75%): empirical ratio vs healthy / 0.75
REL={"DNP":0.55,"LP":1.0,"FP":1.0,"NA":0.8}   # adopted multipliers on the sim value (see report: exact Wed-DNP check 0.48, 3-season final-status 0.61; LP left neutral because evidence conflicts)
QBOUT=0.80/0.93   # pass catchers and backs when QB1 is out/doubtful, relative to healthy
SLOTS={"QB":(1,1),"K":(1,1),"RB":(2,3),"WR":(2,4),"TE":(1,2),"DL":(2,3),"LB":(2,3),"DB":(2,3)}
def lineup(df,col):
    n=len(df); g=df.group.values
    A=[np.ones(n)];lo=[17];hi=[17]
    for p,(a,b) in SLOTS.items(): A.append((g==p).astype(float));lo.append(a);hi.append(b)
    A.append(np.isin(g,["DL","LB","DB"]).astype(float));lo.append(8);hi.append(8)
    r=milp(-df[col].values,constraints=LinearConstraint(np.array(A),lo,hi),integrality=np.ones(n),bounds=Bounds(0,1))
    return df.index[r.x>0.5]
rows=[]
for w in range(6,10):
    wr=json.load(open(C/f"weeklyResults_w{w}.json",encoding="utf-8-sig"))["weeklyResults"]["matchup"]
    f=[x for m in wr for x in m["franchise"] if x["id"]=="0012"][0]
    pl=pd.DataFrame(f["player"]); pl["actual"]=pd.to_numeric(pl.score,errors="coerce").fillna(0.0) if "score" in pl else 0.0
    d=pl.merge(D[D.week==w][["mfl","name","group","blend","team"]],left_on="id",right_on="mfl",how="left")
    d["blend"]=d.blend.fillna(0.0); d["group"]=d.group.fillna("NA")
    d=d[d.group!="NA"].copy()
    iw=INJ[INJ.week==w].drop_duplicates("mfl").set_index("mfl")
    d["rs"]=d.id.map(iw.rs).fillna("none"); d["pc"]=d.id.map(iw.pc).fillna("none")
    # QB1 out: our QB (the one starting on the team) flagged Out/Doubtful in the injuries file for that team
    outq=set(INJ[(INJ.week==w)&(INJ.position=="QB")&(INJ.rs.isin(["Out","Doubtful"]))].team)
    d["qbout"]=d.team.isin(outq)&d.group.isin(["RB","WR","TE"])
    d["rule"]=d.blend
    q=d.rs=="Questionable"
    d.loc[q,"rule"]=d.loc[q].apply(lambda r:r.blend*REL.get(r.pc,REL["LP"]),axis=1)
    # no hindsight: a player who ended the week Out/Doubtful is treated as a Wednesday-DNP/limited Questionable, not as a zero
    o=d.rs.isin(["Out","Doubtful"])
    d.loc[o,"rule"]=d.loc[o].apply(lambda r:r.blend*REL.get(r.pc if r.pc in ("DNP","LP","FP") else "DNP",REL["DNP"]),axis=1)
    d.loc[d.qbout,"rule"]*=QBOUT
    d["blend_nofix"]=d.blend; d=d.reset_index(drop=True)
    saved=d[d.status=="starter"]
    L={"saved(actually ran)":saved.index,"model(blend)":lineup(d,"blend"),"rule":lineup(d,"rule"),"hindsight":lineup(d,"actual")}
    row=dict(week=w)
    for k,ix in L.items():
        row[k]=d.loc[ix,"actual"].sum(); row[k+"_proj"]=d.loc[ix,"blend"].sum()
    rows.append(row)
    chg=set(d.loc[L["rule"],"name"])-set(d.loc[L["model(blend)"],"name"]); chg2=set(d.loc[L["model(blend)"],"name"])-set(d.loc[L["rule"],"name"])
    print(f"W{w}: rule swaps IN {sorted(chg)}  OUT {sorted(chg2)}")
    fl=d[(d.rs!="none")|d.qbout].loc[:, ["name","group","blend","rs","pc","qbout","actual"]]
    fl=fl[fl.blend>=3]; print(fl.round(1).to_string(index=False))
R=pd.DataFrame(rows).round(1); print(R.to_string(index=False)); R.to_csv(H/"injury_rule_zac.csv",index=False)
print(R[[c for c in R if not c.endswith("_proj") and c!="week"]].mean().round(1))
