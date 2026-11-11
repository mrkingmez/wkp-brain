"""Per-position recalibration test with leave-one-week-out CV, selection (winner's curse) check, questionable check."""
import pandas as pd, numpy as np
D=pd.read_csv("dataset.csv"); D=D[D.mfl.notna()].copy()
D["pos"]=D.group.replace({"K":"PK"})
R=D[D.blend>=3].copy()
# 1) leave-one-week-out linear recal per position
out=[]
for pos,g in R.groupby("pos"):
    for w in sorted(g.week.unique()):
        tr,te=g[g.week!=w],g[g.week==w]
        b,a=np.polyfit(tr.blend,tr.actual,1)
        te=te.assign(rec=a+b*te.blend)
        out.append(te)
O=pd.concat(out)
res=O.groupby("pos").apply(lambda x:pd.Series(dict(n=len(x),mae_raw=(x.actual-x.blend).abs().mean(),mae_recal=(x.actual-x.rec).abs().mean(),rmse_raw=np.sqrt(((x.actual-x.blend)**2).mean()),rmse_recal=np.sqrt(((x.actual-x.rec)**2).mean())))).round(2)
print(res)
print("ALL rmse raw",np.sqrt(((O.actual-O.blend)**2).mean()).round(3),"recal",np.sqrt(((O.actual-O.rec)**2).mean()).round(3))
# 2) simple global shrink factor s toward position mean: pred = m + s*(blend-m)
for s in (1.0,.95,.9,.85,.8):
    p=O.groupby(["pos","week"]).blend.transform("mean")
    e=O.actual-(p+s*(O.blend-p)); print("shrink",s,"rmse",np.sqrt((e**2).mean()).round(3))
# 3) selection: top-N per position per week
N={"QB":12,"RB":30,"WR":40,"TE":14,"PK":12,"DL":24,"LB":24,"DB":24}
D["rk"]=D.groupby(["week","pos"]).blend.rank(ascending=False)
D["top"]=D.apply(lambda r:r.rk<=N.get(r.pos,12),axis=1)
for t,g in D.groupby("top"):
    e=g.actual-g.blend; print("top" if t else "rest","n",len(g),"bias",e.mean().round(2),"proj",g.blend.mean().round(2))
print(D[D.top].groupby("pos").apply(lambda g:pd.Series(dict(n=len(g),proj=g.blend.mean(),act=g.actual.mean(),bias=(g.actual-g.blend).mean()))).round(2))
# 4) questionable
for q,g in R.groupby("questionable"):
    e=g.actual-g.blend; print("questionable",q,"n",len(g),"bias",e.mean().round(2),"zero-rate",(g.actual==0).mean().round(2),"mae",e.abs().mean().round(2))
# zero rate by projection bucket
R["bucket"]=pd.cut(R.blend,[3,5,8,12,18,40]); print(R.groupby("bucket").apply(lambda g:pd.Series(dict(n=len(g),zero=(g.actual==0).mean(),bias=(g.actual-g.blend).mean()))).round(2))
