"""Fix 3 test. Large sample: nflverse 2024-2026, QB/RB/WR/TE, regular season. Proxy projection = mean PPR points over the
player's previous 4 games that season (min 2). Compares actual/proxy for healthy vs Questionable by practice status,
and for pass catchers/backs on teams whose QB1 is Out/Doubtful.
CAVEAT: nflverse keeps the LAST practice status of the week (usually Friday), not Wednesday's.
Run: python -I injury_rule_test.py"""
import pandas as pd, numpy as np
from pathlib import Path
H=Path(r"D:\WKP\Fantasy-Football\fixes-2026-11-10")
S=[];I=[]
for y in (2024,2025,2026):
    s=pd.read_parquet(rf"D:\WKP\data\nfl\stats_player\stats_player_week_{y}.parquet"); S.append(s[s.season_type=="REG"])
    i=pd.read_csv(H/f"nfl_cache/injuries_{y}.csv",low_memory=False); I.append(i[i.game_type=="REG"] if "game_type" in i else i)
S=pd.concat(S); I=pd.concat(I)
S=S[S.position.isin(["QB","RB","WR","TE"])][["player_id","season","week","team","position","fantasy_points_ppr","attempts"]].rename(columns={"player_id":"gsis_id"})
S=S.sort_values(["gsis_id","season","week"])
S["proxy"]=S.groupby(["gsis_id","season"]).fantasy_points_ppr.transform(lambda x:x.shift(1).rolling(4,min_periods=2).mean())
# team-week universe: every player with a trailing proxy, expected to appear. Players who did not play have no stats row -> build rows from injuries
I=I[I.position.isin(["QB","RB","WR","TE"])]
I["rs"]=I.report_status.fillna("none")
def pcat(p):
    if isinstance(p,str):
        return "DNP" if p.startswith("Did Not") else ("LP" if p.startswith("Limited") else "FP")
    return "NA"
I["pc"]=I.practice_status.map(pcat)
M=S.merge(I[["gsis_id","season","week","rs","pc"]].drop_duplicates(["gsis_id","season","week"]),on=["gsis_id","season","week"],how="left")
M["rs"]=M.rs.fillna("none"); M["pc"]=M.pc.fillna("none")
# add Questionable/Doubtful/Out player-weeks with no stats row (did not play): need proxy from earlier
last=S.groupby(["gsis_id","season"]).apply(lambda g:g.set_index("week").fantasy_points_ppr)
def proxy_for(r):
    try:
        g=last.loc[(r.gsis_id,r.season)]; g=g[g.index<r.week].tail(4)
        return g.mean() if len(g)>=2 else np.nan
    except KeyError: return np.nan
miss=I.merge(S[["gsis_id","season","week"]],on=["gsis_id","season","week"],how="left",indicator=True)
miss=miss[(miss._merge=="left_only")&(miss.rs.isin(["Questionable","Doubtful","Out"]))].copy()
miss["proxy"]=miss.apply(proxy_for,axis=1); miss["fantasy_points_ppr"]=0.0; miss["position"]=miss.position; miss["team"]=miss.team
M=pd.concat([M,miss[["gsis_id","season","week","team","position","fantasy_points_ppr","proxy","rs","pc"]]],ignore_index=True)
M=M[M.proxy>=6].copy()   # relevant starters only
M["ratio"]=M.fantasy_points_ppr/M.proxy
def summ(g): return pd.Series(dict(n=len(g),proxy=g.proxy.mean(),actual=g.fantasy_points_ppr.mean(),ratio=g.fantasy_points_ppr.sum()/g.proxy.sum(),zero=(g.fantasy_points_ppr<=0.5).mean()))
M["grp"]=np.where(M.rs=="none","healthy (no report)",M.rs+" / "+M.pc)
T=M.groupby("grp").apply(summ).round(2); print(T.to_string()); T.to_csv(H/"injury_rule_table.csv")
# bootstrap CI on ratio for Q/DNP vs healthy
rng=np.random.default_rng(1)
def ci(g):
    x=g.fantasy_points_ppr.values; p=g.proxy.values; r=[]
    for _ in range(2000):
        k=rng.integers(0,len(x),len(x)); r.append(x[k].sum()/p[k].sum())
    return np.percentile(r,[5,95]).round(2)
for k in ["Questionable / DNP","Questionable / LP","Questionable / FP","healthy (no report)","Doubtful / DNP"]:
    g=M[M.grp==k]
    if len(g)>20: print(k,"n",len(g),"ratio 90% CI",ci(g))
# 2026 only
print("\n2026 only"); print(M[M.season==2026].groupby("grp").apply(summ).round(2).to_string())
# backup QB effect: teams whose QB1 (most attempts in prior 4 wks avg) is Out/Doubtful that week
q=S[S.position=="QB"].copy(); q["att4"]=q.groupby(["gsis_id","season"]).attempts.transform(lambda x:x.shift(1).rolling(4,min_periods=1).mean())
q1=q.sort_values("att4",ascending=False).groupby(["team","season","week"]).head(1)[["team","season","week","gsis_id"]].rename(columns={"gsis_id":"qb1"})
# QB1 status uses prior-weeks identity; a QB1 who is out has NO stats row that week, so derive QB1 from previous week
prev=S[S.position=="QB"].sort_values(["team","season","week"]); 
prev=prev.groupby(["team","season","week"]).attempts.idxmax()
q1p=S.loc[prev.values][["team","season","week","gsis_id"]].rename(columns={"gsis_id":"qb1"}); q1p["week"]+=1
out=I[(I.position=="QB")&(I.rs.isin(["Out","Doubtful"]))][["gsis_id","season","week"]].assign(qbout=1).rename(columns={"gsis_id":"qb1"})
q1p=q1p.merge(out,on=["qb1","season","week"],how="left"); q1p["qbout"]=q1p.qbout.fillna(0)
P=M[M.position.isin(["RB","WR","TE"])&(M.rs=="none")].merge(q1p[["team","season","week","qbout"]],on=["team","season","week"],how="left")
P=P[P.qbout.notna()]
print("\nPass catchers/backs, healthy, by QB1 out (QB1 = last week's attempts leader on that team)")
print(P.groupby(["position","qbout"]).apply(summ).round(2).to_string())
print(P.groupby("qbout").apply(summ).round(2).to_string())
M.to_csv(H/"injury_rule_rows.csv",index=False)
