"""Realized DraftKings points per player for a week from nflverse (no DST). Used to validate Zac's two Week 9 lineups (107, 149) and score new ones."""
import pandas as pd, numpy as np, re
def dk_points(season,week):
    S=pd.read_parquet(r"D:\WKP\data\nfl\stats_player\stats_player_week_%d.parquet"%season); S=S[(S.week==week)&(S.season_type=="REG")].copy()
    f=lambda c:S[c].fillna(0) if c in S else 0
    S["dk"]=(0.04*f("passing_yards")+4*f("passing_tds")-1*f("passing_interceptions")+0.1*f("rushing_yards")+6*f("rushing_tds")+f("receptions")+0.1*f("receiving_yards")+6*f("receiving_tds")-1*(f("rushing_fumbles_lost")+f("sack_fumbles_lost")+f("receiving_fumbles_lost"))+2*(f("passing_2pt_conversions")+f("rushing_2pt_conversions")+f("receiving_2pt_conversions"))+3*(f("passing_yards")>=300)+3*(f("rushing_yards")>=100)+3*(f("receiving_yards")>=100))
    S["key"]=S.player_display_name.map(norm); S["team"]=S.team.replace({"LAR":"LA","JAC":"JAX","WSH":"WAS"}); return S[["key","team","dk","position"]]
def norm(s):
    s=re.sub(r"[.,'’]","",str(s).lower()); s=re.sub(r"\b(jr|sr|ii|iii|iv|v)\b","",s); return re.sub(r"\s+"," ",s).strip()
if __name__=="__main__":
    D=dk_points(2026,9); l=pd.read_csv(r"D:\WKP\data\ff-simulator\dfs_lineups_dk_2026_wk9.csv"); l["key"]=l.name.map(norm); l["team"]=l.team.replace({"LAR":"LA","JAC":"JAX","WSH":"WAS"})
    for n,g in l.groupby("lineup"):
        m=g[g.pos!="DST"].merge(D,on=["key","team"],how="left"); print(m[["name","team","salary","avg","dk"]].round(1).to_string(index=False)); print("lineup",n,"non-DST realized",round(m.dk.sum(),1),"unmatched",m.dk.isna().sum(),"| projected avg sum",round(g.avg.sum(),1))
