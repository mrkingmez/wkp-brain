"""Fix 1 rule tests on nflverse closing lines (proxy for the frozen Monday line: nflverse keeps no opening lines).
League rule: NO push, underdog wins ties. Tests which side to take in coin-flip games.
Run: python -I pickem_rules_test.py"""
import pandas as pd, numpy as np
g=pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet")
g=g[(g.game_type=="REG")&g.result.notna()&g.spread_line.notna()&(g.season>=2016)&(g.season<=2025)].copy()
g["fav_home"]=g.spread_line>0; s=g.spread_line.abs(); g["s"]=s
m=g.result*np.sign(g.spread_line)  # favorite margin (spread_line=0: sign 0)
g=g[g.spread_line!=0].copy(); g["fav_margin"]=g.result*np.sign(g.spread_line)
g["dog_wins"]=g.fav_margin<=g.s    # tie goes to dog
g["fav_wins"]=~g.dog_wins
g["tie"]=g.fav_margin==g.s
g["integer"]=(g.s%1==0)
print("games",len(g),"seasons",g.season.min(),"-",g.season.max())
print("tie rate overall",g.tie.mean().round(4))
for nm,sub in (("integer lines",g[g.integer]),("half-point lines",g[~g.integer]),("all",g)):
    n=len(sub); k=sub.dog_wins.sum(); print(f"{nm}: n={n}  underdog side wins {k/n:.4f}  (ties {sub.tie.mean():.4f})  fav side {1-k/n:.4f}")
print("\nunderdog win rate by key number (integer lines):")
t=g[g.integer].groupby("s").agg(n=("dog_wins","size"),dog=("dog_wins","mean"),tie=("tie","mean")).round(3); print(t[t.n>=40].to_string())
print("\nby season, integer lines, underdog side:"); print(g[g.integer].groupby("season").dog_wins.agg(["size","mean"]).round(3).T.to_string())
# home/away/fav-home on half-point lines
h=g[~g.integer]; hc=(h.result>h.spread_line)
print("\nhalf-point lines: home covers",hc.mean().round(4),"fav covers",(1-h.dog_wins).mean().round(4),"home dog covers",(hc[~h.fav_home]).mean().round(4),"n",(~h.fav_home).sum())
# bootstrap CI integer underdog
rng=np.random.default_rng(3); x=g[g.integer].dog_wins.values.astype(float)
bs=[x[rng.integers(0,len(x),len(x))].mean() for _ in range(2000)]; print("integer-line underdog 90% CI",np.percentile(bs,[5,95]).round(4))
# break-even implied: how many games per week are integer lines on the card?
p=pd.read_csv(r"D:\WKP\Fantasy-Football\tracker\predictions.csv"); m=p[(p.source=="model")&p.week.isin([6,7,8,9])&p.closing_line.notna()]
print("\ncard (frozen) lines W6-9 NFL: integer share",(m.line_used.abs()%1==0).mean().round(2),"n",len(m)); print(m.line_used.abs().value_counts().sort_index().to_dict())
# Apply rule to the W6-9 card: for every NFL game with integer frozen line, take the frozen-line underdog
m=m.copy(); m["frozen_home_fav"]=m.line_used>0; m["dog_home"]=~m.frozen_home_fav
res=m.home_score-m.away_score; fm=res*np.where(m.frozen_home_fav,1,-1); sl=m.line_used.abs()
m["dog_covers"]=fm<=sl
print("W6-9 NFL games n",len(m),"underdog side (tie rule) won",m.dog_covers.sum(),"=",m.dog_covers.mean().round(3))
mi=m[sl%1==0]; print("integer-line games only n",len(mi),"dog won",mi.dog_covers.sum())
# model pick record
mm=m.copy(); print("model picks W6-9 NFL:",(mm.result_ats=="correct").sum(),"of",len(mm))
mm["pick_is_dog"]=np.where(mm.pick_ats==mm.home_team,mm.dog_home,~mm.dog_home)
print("model pick = frozen underdog share",mm.pick_is_dog.mean().round(2),"; fav picks",(~mm.pick_is_dog).sum(),"won",((mm.result_ats=="correct")&~mm.pick_is_dog).sum(),"; dog picks",mm.pick_is_dog.sum(),"won",((mm.result_ats=="correct")&mm.pick_is_dog).sum())
