"""DFS optimizer v2 (proposal, NEW file, v1 untouched). Same inputs as v1 (simulated draws + salary csv). Changes:
 1. Stack on by default: QB + at least 1 same-team WR/TE (--no-stack to turn off); --bringback adds 1 opposing WR/TE/RB.
 2. Punt-QB guard: QBs under --min-qb-salary (default 5000) are dropped unless --allow-punt.
 3. Objective is the chance of reaching a target, not the 90th percentile: GPP target = the 95th percentile of the best-average lineup's simulated score
    (a 'big slate' number); cash target = --cash-line (default 130, a SECONDARY-sourced figure: 2025 DK double-ups were 115 to 150).
 4. Portfolio: lineups share at most --max-overlap (default 5) of 9 players, so the N lineups are not near-copies (Hunter, Vielma, Zaman idea; they tested hockey/baseball only).
 5. Prints the real simulated range (10/50/90) and hit probability, and says plainly that nothing here is a tested edge.
python dfs_optimize_v2.py dk <DKSalaries.csv> --season 2026 --week 9 [--n 10] [--mode gpp|cash] [--bringback]
"""
import argparse, importlib.util, sys
from pathlib import Path
import numpy as np, pandas as pd
from scipy.optimize import Bounds, LinearConstraint, milp
spec=importlib.util.spec_from_file_location("v1",r"D:\WKP\.claude\skills\ff-simulator\scripts\dfs_optimize.py"); v1=importlib.util.module_from_spec(spec); spec.loader.exec_module(v1)
OUT=Path(r"D:\WKP\Fantasy-Football\fixes-2026-11-10")
def build(a):
    z=np.load(v1.OUT/f"dfs_draws_{a.season}_wk{a.week}.npz"); D=z[a.site].astype(np.float64)
    sim=pd.DataFrame({"name":z["names"],"team":z["teams"],"pos":z["groups"]}); sim["key"]=sim.name.map(v1.norm); sim["row"]=range(len(sim))
    sal=v1.load_salaries(a.site,a.csv); sal=sal[~sal.status.isin(["OUT","IR","O"])]
    top=sal[sal.pos=="QB"].groupby("team").salary.transform("max"); sal=sal[(sal.pos!="QB")|(sal.salary==top.reindex(sal.index))]
    if not a.allow_punt: sal=sal[(sal.pos!="QB")|(sal.salary>=a.min_qb_salary)]
    m=sal.merge(sim[["key","team","row"]],on=["key","team"],how="left"); m=m[m.row.notna()|(m.pos=="DST")].reset_index(drop=True)
    X=np.zeros((len(m),D.shape[1]))
    for i,r in m.iterrows(): X[i]=D[int(r.row)] if pd.notna(r.row) else float(r.avg if pd.notna(r.avg) else 6.0)
    return m,X
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("site",choices=["dk"]); ap.add_argument("csv"); ap.add_argument("--season",type=int,default=2026); ap.add_argument("--week",type=int,default=9)
    ap.add_argument("--n",type=int,default=10); ap.add_argument("--mode",choices=["gpp","cash"],default="gpp"); ap.add_argument("--no-stack",action="store_true"); ap.add_argument("--bringback",action="store_true")
    ap.add_argument("--min-qb-salary",type=int,default=5000); ap.add_argument("--allow-punt",action="store_true"); ap.add_argument("--max-overlap",type=int,default=5)
    ap.add_argument("--cash-line",type=float,default=130.0); ap.add_argument("--tries",type=int,default=400); ap.add_argument("--seed",type=int,default=11)
    a=ap.parse_args(); m,X=build(a); n,S=X.shape; pos=m.pos.values; tm=m.team.values; sa=m.salary.values.astype(float)
    mean=X.mean(1)
    # opponent map from the draws file is not stored: derive bring-back from salary file Game Info when present
    opp={}
    try:
        gi=pd.read_csv(a.csv).rename(columns={"TeamAbbrev":"team"}); 
        for g,t in zip(gi["Game Info"],gi.team):
            ab=str(g).split(" ")[0].split("@"); 
            if len(ab)==2: opp[t.replace("JAC","JAX")]=ab[1] if t==ab[0] else ab[0]
        opp={v1.TEAM_FIX.get(k,k):v1.TEAM_FIX.get(w,w) for k,w in opp.items()}
    except Exception: pass
    def solve(score,ban):
        A=[sa];lo=[0];hi=[v1.CAP[a.site]]
        for p,l,h in (("QB",1,1),("RB",2,3),("WR",3,4),("TE",1,2),("DST",1,1)): A.append((pos==p).astype(float));lo.append(l);hi.append(h)
        A.append(np.isin(pos,["QB","RB","WR","TE"]).astype(float));lo.append(8);hi.append(8)
        for q in np.where(pos=="QB")[0]:
            if not a.no_stack:
                r=((tm==tm[q])&np.isin(pos,["WR","TE"])).astype(float); r[q]=-1; A.append(r);lo.append(0);hi.append(np.inf)
            if a.bringback and tm[q] in opp:
                r=((tm==opp[tm[q]])&np.isin(pos,["WR","TE","RB"])).astype(float); r[q]=-1; A.append(r);lo.append(0);hi.append(np.inf)
        for prev in ban:
            r=np.zeros(n); r[list(prev)]=1; A.append(r);lo.append(0);hi.append(a.max_overlap)
        res=milp(-score,constraints=LinearConstraint(np.array(A),lo,hi),integrality=np.ones(n),bounds=Bounds(0,1))
        return tuple(np.where(res.x>0.5)[0]) if res.success else None
    rng=np.random.default_rng(a.seed); base=solve(mean,[]); cands={base:None} if base else {}
    for _ in range(a.tries):
        s=rng.integers(0,S,3); lu=solve(0.5*mean+0.5*X[:,s].mean(1),[])
        if lu: cands[lu]=None
    if not cands: raise SystemExit("no legal lineup")
    tot={lu:X[list(lu)].sum(0) for lu in cands}
    T=a.cash_line if a.mode=="cash" else float(np.percentile(tot[base],95))
    sc={lu:(t>=T).mean() for lu,t in tot.items()}
    order=sorted(sc,key=lambda k:-sc[k]); pick=[]
    for lu in order:
        if all(len(set(lu)&set(p))<=a.max_overlap for p in pick): pick.append(lu)
        if len(pick)==a.n: break
    print(f"{len(cands)} candidate lineups; target score T={T:.1f} ({'cash line, SECONDARY source' if a.mode=='cash' else '95th pct of the best-average lineup'}). Nothing here is a tested edge.")
    rows=[]
    for k,lu in enumerate(pick,1):
        t=tot[lu]; ps=sorted(lu,key=lambda i:["QB","RB","WR","TE","DST"].index(pos[i]))
        print(f"\nLineup {k}: P(>=T) {sc[lu]:.3f} | avg {t.mean():.1f} | 10th {np.percentile(t,10):.1f} 50th {np.percentile(t,50):.1f} 90th {np.percentile(t,90):.1f} | salary ${int(sa[list(lu)].sum()):,}")
        for i in ps:
            print(f"   {pos[i]:3s} {m.name[i]:<24s} {tm[i]:4s} ${int(sa[i]):>6,} avg {mean[i]:5.1f}"+("  (DST: file average)" if pos[i]=="DST" else ""))
            rows.append(dict(lineup=k,pos=pos[i],name=m.name[i],team=tm[i],salary=int(sa[i]),avg=round(mean[i],1)))
    pd.DataFrame(rows).to_csv(OUT/f"dfs_v2_lineups_{a.mode}_wk{a.week}.csv",index=False)
if __name__=="__main__": main()
