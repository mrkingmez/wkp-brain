"""Fix 1: label every pick'em game with the gap to the current market and an honest probability.
Usage: python -I pickem_labels.py <week> [--market pickem_probs csv]  (default: D:\WKP\data\ff-simulator\pickem_probs_2026_wk<week>.csv, else nflverse closing line)
Rules (see report):
  gap  = how far the current market sits from the frozen card line, in points, toward the side named.
  p    = Phi(gap / 13.2): 13.2 = real sd of NFL margin around the closing line (nflverse 2016-2025).  Never above ~0.60 at these gaps.
  tier: LEAN  gap >= 2.0 (p >= 0.56) | SLIGHT 1.0 <= gap < 2.0 (p 0.53 to 0.56) | NO EDGE gap < 1.0 (coin flip)
  NO EDGE games show 'Zac read' blank and a long-run tiebreak (frozen underdog) only if Zac has no read.
  College games: no market data in the tracker -> NO EDGE unless a market gap is supplied.
Writes pickem_labels_wk<week>.csv and prints a markdown table."""
import sys, pandas as pd, numpy as np
from math import erf, sqrt
Phi=lambda x:0.5*(1+erf(x/sqrt(2))); SIG=13.2
H=r"D:\WKP\Fantasy-Football\fixes-2026-11-10"
w=int(sys.argv[1]); p=pd.read_csv(r"D:\WKP\Fantasy-Football\tracker\predictions.csv")
m=p[(p.week==w)&(p.source=="model")].copy()
FIX={"WSH":"WAS","LAR":"LA"}
try:
    q=pd.read_csv(rf"D:\WKP\data\ff-simulator\pickem_probs_2026_wk{w}.csv"); q["a"]=q.game.str.split(" @ ").str[0].replace(FIX); q["h"]=q.game.str.split(" @ ").str[1].replace(FIX)
    mk={(a,h):v for a,h,v in zip(q.a,q.h,q.market_home)}; src="Odds API median (Thursday)"
except FileNotFoundError: mk={}; src="nflverse closing line (no Thursday pull on file)"
rows=[]
for _,r in m.iterrows():
    a,h=FIX.get(r.away_team,r.away_team),FIX.get(r.home_team,r.home_team); card=r.line_used
    cur=mk.get((a,h)); how="odds" if cur is not None else None
    if cur is None and pd.notna(r.closing_line): cur=r.closing_line; how="closing"
    if cur is None: rows.append(dict(week=w,game=f"{r.away_team} @ {r.home_team}",card_line_home=card,market_home=np.nan,gap=np.nan,side="NO EDGE (no market data)",p=0.5,tier="NO EDGE",tiebreak="",logged_pick=r.pick_ats,result=r.result_ats));continue
    d=cur-card                      # home-positive: >0 market moved toward home
    side=h if d>0 else a; gap=abs(d)
    dog=h if card<0 else a          # frozen-card underdog (card>0 = home favored)
    tier="LEAN" if gap>=2 else "SLIGHT" if gap>=1 else "NO EDGE"
    rows.append(dict(week=w,game=f"{r.away_team} @ {r.home_team}",card_line_home=card,market_home=cur,mkt_source=how,gap=round(gap,1),side=side if tier!="NO EDGE" else "NO EDGE",
        p=round(Phi(gap/SIG),3) if tier!="NO EDGE" else 0.5,tier=tier,tiebreak=("" if tier!="NO EDGE" else f"if no read: {dog} (frozen underdog)"),logged_pick=r.pick_ats,result=r.result_ats))
o=pd.DataFrame(rows); o.to_csv(rf"{H}\pickem_labels_wk{w}.csv",index=False)
print(f"Week {w}  market source: {src}\n"); print(o.drop(columns=["week"]).to_string(index=False))
e=o[o.tier!="NO EDGE"]; print(f"\nLEAN {sum(o.tier=='LEAN')} | SLIGHT {sum(o.tier=='SLIGHT')} | NO EDGE {sum(o.tier=='NO EDGE')} of {len(o)} NFL games")
print(f"Expected ATS wins if every game is picked: {(o.p.sum()):.1f} of {len(o)} (coin flips counted at 0.50); SD about {sqrt((o.p*(1-o.p)).sum()):.1f}")
