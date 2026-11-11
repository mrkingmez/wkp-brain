"""Fix 5 in-house study on free nflverse data (2024-2026 regular season, closing lines from nflverse schedules).
Part A: measured correlations (QB with own pass catchers, QB with opposing QB) and how much the closing game total explains DK points.
Part B: PROXY backtest of stacking, not a real DFS backtest: no free archive of historical DK/FD salaries or ownership was found,
so salary = a made-up function of trailing average points plus noise. It only tests whether stacked lineups differ in mean and
upper tail from unstacked lineups built the same way. Run: python -I dfs_study.py"""
import pandas as pd, numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
S=pd.concat([pd.read_parquet(rf"D:\WKP\data\nfl\stats_player\stats_player_week_{y}.parquet") for y in (2024,2025,2026)])
S=S[(S.season_type=="REG")&S.position.isin(["QB","RB","WR","TE"])].copy()
f=lambda c:S[c].fillna(0) if c in S else 0
S["dk"]=(0.04*f("passing_yards")+4*f("passing_tds")-1*f("passing_interceptions")+0.1*f("rushing_yards")+6*f("rushing_tds")
 +f("receptions")+0.1*f("receiving_yards")+6*f("receiving_tds")-1*(f("rushing_fumbles_lost")+f("sack_fumbles_lost")+f("receiving_fumbles_lost"))
 +2*(f("passing_2pt_conversions")+f("rushing_2pt_conversions")+f("receiving_2pt_conversions"))
 +3*(f("passing_yards")>=300)+3*(f("rushing_yards")>=100)+3*(f("receiving_yards")>=100))
g=pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet"); g=g[g.game_type=="REG"&(g.season>=2024) if False else (g.game_type=="REG")&(g.season>=2024)]
gm=pd.concat([g.assign(team=g.home_team,opp=g.away_team,fav=g.spread_line),g.assign(team=g.away_team,opp=g.home_team,fav=-g.spread_line)])
gm["team_total"]=gm.total_line/2+gm.fav/2   # implied team total: fav = points the team is favored by
S=S.merge(gm[["season","week","team","opp","total_line","team_total","fav"]],on=["season","week","team"],how="inner")
print("player-game rows",len(S),"slates",S.groupby(["season","week"]).ngroups)
# A1 totals
print("\nA1. DK points regressed on implied team total (players with >=1 target/carry/attempt)")
S["usage"]=f("attempts")+f("carries")+f("targets")
U=S[S.usage>=5]
for pos,gp in U.groupby("position"):
    b,a=np.polyfit(gp.team_total,gp.dk,1); r=np.corrcoef(gp.team_total,gp.dk)[0,1]
    print(f"  {pos}: n={len(gp)} corr {r:.3f}  R2 {r*r:.3f}  slope {b:.2f} DK pts per +1 implied team point")
# top-tertile vs bottom tertile team total, top-2 WR/RB/QB per team
print("  mean DK of the top 3 QB/RB/WR/TE (by usage) per team-game, by implied team total tercile:")
t=U.sort_values("usage",ascending=False).groupby(["season","week","team"]).head(3); t=t.assign(q=pd.qcut(t.team_total,3,labels=["low","mid","high"]))
print(t.groupby("q").dk.agg(["mean","std","size"]).round(2).to_string())
# A2 correlations
q=S[S.position=="QB"].sort_values("attempts",ascending=False).drop_duplicates(["season","week","team"])[["season","week","team","opp","dk"]].rename(columns={"dk":"qb"})
pc=S[S.position.isin(["WR","TE"])].sort_values("targets",ascending=False)
pc["rk"]=pc.groupby(["season","week","team","position"]).cumcount()+1
w1=pc[(pc.position=="WR")&(pc.rk==1)][["season","week","team","dk"]].rename(columns={"dk":"wr1"})
w2=pc[(pc.position=="WR")&(pc.rk==2)][["season","week","team","dk"]].rename(columns={"dk":"wr2"})
t1=pc[(pc.position=="TE")&(pc.rk==1)][["season","week","team","dk"]].rename(columns={"dk":"te1"})
r1=S[S.position=="RB"].sort_values("carries",ascending=False).drop_duplicates(["season","week","team"])[["season","week","team","dk"]].rename(columns={"dk":"rb1"})
M=q.merge(w1,on=["season","week","team"]).merge(w2,on=["season","week","team"]).merge(t1,on=["season","week","team"],how="left").merge(r1,on=["season","week","team"],how="left")
O=q[["season","week","team","qb"]].rename(columns={"team":"opp","qb":"opp_qb"}); M=M.merge(O,on=["season","week","opp"],how="left")
print("\nA2. Pearson correlations of DK points (QB = pass-attempt leader, WR1/WR2/TE1 = target leaders, RB1 = carry leader), n team-games =",len(M))
for a,b in (("qb","wr1"),("qb","wr2"),("qb","te1"),("qb","rb1"),("qb","opp_qb"),("wr1","wr2"),("rb1","wr1")):
    d=M[[a,b]].dropna(); print(f"  {a:7s} vs {b:7s}: {np.corrcoef(d[a],d[b])[0,1]:+.3f} (n={len(d)})")
# opposing pass catcher: QB vs the opponent's WR1
ow=w1.rename(columns={"team":"opp","wr1":"opp_wr1"}); X=M[["season","week","team","opp","qb"]].merge(ow,on=["season","week","opp"]); print(f"  qb vs opposing WR1: {np.corrcoef(X.qb,X.opp_wr1)[0,1]:+.3f} (n={len(X)})")
# B proxy backtest
print("\nB. PROXY stacking backtest (salary is synthetic: 3000+260*trailing-4 avg DK pts, plus noise sd 500, clipped 3000-9500; cap 50000; QB/2RB/3WR/TE/FLEX; no DST)")
S=S.sort_values(["gsis_id" if "gsis_id" in S else "player_id","season","week"])
pid="player_id"; S["proj"]=S.groupby([pid,"season"]).dk.transform(lambda x:x.shift(1).rolling(4,min_periods=2).mean())
rng=np.random.default_rng(5); out=[]
for (se,wk),d in S.groupby(["season","week"]):
    d=d[d.proj>=4].reset_index(drop=True)
    if len(d)<60 or wk<4: continue
    sal=np.clip(3000+260*d.proj+rng.normal(0,500,len(d)),3000,9500).values
    pos=d.position.values; tm=d.team.values; n=len(d)
    def solve(score,stack,env=0.0):
        sc=score+env*(d.team_total.values-d.team_total.mean())
        A=[sal];lo=[0];hi=[50000]
        for p,a,b in (("QB",1,1),("RB",2,3),("WR",3,4),("TE",1,2)): A.append((pos==p).astype(float));lo.append(a);hi.append(b)
        A.append(np.ones(n));lo.append(8);hi.append(8)
        if stack:
            for qi in np.where(pos=="QB")[0]:
                row=((tm==tm[qi])&np.isin(pos,["WR","TE"])).astype(float); row[qi]=-1; A.append(row);lo.append(0);hi.append(np.inf)
        r=milp(-sc,constraints=LinearConstraint(np.array(A),lo,hi),integrality=np.ones(n),bounds=Bounds(0,1))
        return None if not r.success else np.where(r.x>0.5)[0]
    row=dict(season=se,week=wk)
    for name,stack,env in (("plain",False,0.0),("stack",True,0.0),("stack+env",True,0.6)):
        ix=solve(d.proj.values,stack,env); row[name]=d.dk.values[ix].sum() if ix is not None else np.nan
    out.append(row)
R=pd.DataFrame(out).dropna(); print("slates",len(R))
print("share of slates stack+env beats plain: %.2f; stack beats plain: %.2f"%((R["stack+env"]>R["plain"]).mean(),(R["stack"]>R["plain"]).mean()))
print("90th pct plain %.1f stack %.1f stack+env %.1f"%tuple(np.percentile(R[c],90) for c in ("plain","stack","stack+env")))
print(R[["plain","stack","stack+env"]].describe().round(1).to_string())
print("paired mean diff stack-plain %.2f (se %.2f); stack+env-plain %.2f (se %.2f)"%((R["stack"]-R["plain"]).mean(),(R["stack"]-R["plain"]).std()/np.sqrt(len(R)),(R["stack+env"]-R["plain"]).mean(),(R["stack+env"]-R["plain"]).std()/np.sqrt(len(R))))
R.to_csv("dfs_proxy_backtest.csv",index=False)
