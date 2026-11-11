"""Scores the Fix 1 labels on weeks 6-9 NFL games: does the stated probability hold up?  Side wins use the league's tie rule (underdog wins ties)."""
import pandas as pd, numpy as np
FIX={"WSH":"WAS","LAR":"LA"}
p=pd.read_csv(r"D:\WKP\Fantasy-Football\tracker\predictions.csv"); p=p[(p.source=="model")&p.week.isin([6,7,8,9])&p.closing_line.notna()]
L=pd.concat([pd.read_csv(f"pickem_labels_wk{w}.csv") for w in (6,7,8,9)])
L["k"]=L.game; p["k"]=p.away_team+" @ "+p.home_team
j=L.merge(p[["week","k","home_team","away_team","home_score","away_score","line_used"]],left_on=["week","k"],right_on=["week","k"])
j=j[j.market_home.notna()].copy()
res=j.home_score-j.away_score; card=j.line_used
home_cov=np.where(card>0,res>card,res>=-card.abs()*-1)   # placeholder replaced below
# home covers: card>0 home favored: home covers if res>card (tie->dog=away). card<0 home dog: home covers if res>=card (tie->home dog wins)
home_cov=np.where(card>0,res>card,res>=card)
j["home_cov"]=home_cov
def side_wins(side_home): return np.where(side_home,home_cov,~home_cov)
mk_home=(j.market_home-j.line_used)>0
j["mkt_wins"]=side_wins(mk_home.values)
dog_home=(card<0).values; j["dog_wins"]=side_wins(dog_home)
j["fav_wins"]=~j.dog_wins
for t,g in j.groupby("tier"):
    print(f"{t:8s} n={len(g):3d}  market-side wins {int(g.mkt_wins.sum()):3d} ({g.mkt_wins.mean():.3f})  stated p {g.p.mean():.3f}  | frozen dog {int(g.dog_wins.sum())}  frozen fav {int(g.fav_wins.sum())}")
ne=j[j.tier!="NO EDGE"]; print(f"\nLEAN+SLIGHT n={len(ne)} wins {int(ne.mkt_wins.sum())} ({ne.mkt_wins.mean():.3f}) vs stated {ne.p.mean():.3f}; SE of a rate at this n = {np.sqrt(.25/len(ne)):.3f}")
print("Games needed to tell a true 53% from 50% at 80% power: about", int(((0.84+1.28)**2*0.25/0.03**2)))
print("note: JAX@BAL wk9 uses the Odds API market (-10), not nflverse closing (+3.0, looks wrong)")
j.to_csv("pickem_backtest_rows.csv",index=False)
