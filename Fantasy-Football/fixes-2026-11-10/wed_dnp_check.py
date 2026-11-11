"""Exact-timing check of the Wednesday-DNP rule on Thursday injury captures (weeks 7 and 9 only; the week 8 file was refreshed on Sunday, unusable).
Questionable players with blend>=3 in the dataset, split by the practice status in the Thursday capture note."""
import pandas as pd, numpy as np, re
D=pd.read_csv("dataset.csv"); D=D[D.mfl.notna()]
rows=[]
for w in (7,9):
    i=pd.read_csv(rf"D:\WKP\data\ff-simulator\injuries_2026_wk{w}.csv"); i=i[i.status.eq("Questionable")]
    def pr(n):
        m=re.search(r"practice '([^']+)'",str(n)); 
        if not m: return "unknown"
        t=m.group(1); return "DNP" if t.startswith("Did Not") else "LP" if t.startswith("Limited") else "FP"
    i["pc"]=i.note.map(pr); i=i.drop_duplicates("gsis_id")
    d=D[(D.week==w)&(D.blend>=3)].merge(i[["gsis_id","pc","as_of"]],on="gsis_id",how="inner"); rows.append(d)
R=pd.concat(rows)
g=R.groupby("pc").apply(lambda x:pd.Series(dict(n=len(x),proj=x.blend.mean(),actual=x.actual.mean(),ratio=x.actual.sum()/x.blend.sum(),zero=(x.actual==0).mean()))).round(2); print(g.to_string())
print(R[R.pc=="DNP"][["week","name","team","group","blend","actual"]].round(1).sort_values("blend",ascending=False).to_string(index=False))
