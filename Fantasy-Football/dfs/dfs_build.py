"""dfs_build.py - build exactly THREE DraftKings classic lineups for the 2026-11-15 early slate
(decision support, Zac enters by hand).

python dfs_build.py [--tries 250] [--seed 11]

Structure comes from the friend's process (chalk pool >= 5, QB gate, stack, bring-back <= 2, no forced players, broad caps).
Our simulator (data\\ff-simulator\\dfs_draws_2026_wk10.npz, 20,000 draws) supplies ceilings and the correlation between players.
Sources per number: My Proj, My Own, implied total = friend's file. sim average/p90, QB ceiling rank = our Week 10 simulation.
Defense rank vs QBs = our nflverse 2026 weeks 1-9 (see dfs_common.defense_vs_qb). DST has no sim draws (friend-normal draws used).
Lineups: A floor (pool >= 6, ranked by sim 25th percentile), B balanced (pool >= 5, ranked by sim mean),
C leverage (gate-passing QB under 15 percent owned, 2+ skill/DST under 10 percent owned, ranked by sim 90th percentile).
"""
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import Bounds, LinearConstraint, milp
from dfs_common import prepare, qb_gates, lineup_stats, CAP, LOW_OWN

HERE = Path(__file__).parent
OUT = Path(r"D:\WKP\data\dfs-friend")
QB_LOW_OWN = 15.0   # ASSUMPTION: the biggest QB owner on this slate is 21 percent, so "low-owned" for a QB is under 15 percent (skill players: under 10)
MAX_OVERLAP = 5     # our three lineups share at most 5 of 9 players (portfolio, not copies)


def solve(m, score, qb_ok, min_pool, extra=None):
    n = len(m); pos = m.pos.values; team = m.Team.values; opp = m.Opp.values
    A, lo, hi = [], [], []

    def add(row, l, h):
        A.append(row); lo.append(l); hi.append(h)

    add(m.Salary.values.astype(float), 48500, CAP)
    for p, l, h in (("QB", 1, 1), ("RB", 2, 3), ("WR", 3, 4), ("TE", 1, 2), ("DST", 1, 1)):
        add((pos == p).astype(float), l, h)
    add(np.isin(pos, ["RB", "WR", "TE"]).astype(float), 7, 7)
    add((m.pool.values & np.isin(pos, ["RB", "WR", "TE"])).astype(float), min_pool, 9)
    for t in np.unique(team):
        add(((team == t) & (pos != "DST")).astype(float), 0, 5)   # broad team cap, not a lock
    for q in np.where(pos == "QB")[0]:
        mates = ((team == team[q]) & np.isin(pos, ["WR", "TE"])).astype(float); mates[q] = -1
        add(mates, 0, np.inf)                                         # QB chosen => at least one WR/TE of his team
        back = ((team == opp[q]) & np.isin(pos, ["RB", "WR", "TE"])).astype(float); back[q] = 5
        add(back, 0, 7)                                               # QB chosen => at most 2 bring-backs
        for d in np.where((pos == "DST") & (opp == team[q]))[0]:      # no DST facing our own QB
            r = np.zeros(n); r[q] = 1; r[d] = 1; add(r, 0, 1)
    for row, l, h in (extra or []):
        add(row, l, h)
    ub = np.ones(n)
    ub[(pos == "QB") & ~qb_ok] = 0
    res = milp(-score, constraints=LinearConstraint(np.array(A), lo, hi), integrality=np.ones(n), bounds=Bounds(np.zeros(n), ub))
    return tuple(np.where(res.x > 0.5)[0]) if res.success else None


def candidates(m, X, qb_ok, min_pool, tries, rng, lam_own=0.0, extra=None):
    S = X.shape[1]; mean = X.mean(1); proj = m.proj.values; own = m.own.values
    out = {}
    for _ in range(tries):
        s = rng.integers(0, S, 3)
        w = rng.uniform(0.2, 0.8)
        score = w * proj + (1 - w) * (0.5 * mean + 0.5 * X[:, s].mean(1)) - lam_own * own
        lu = solve(m, score, qb_ok, min_pool, extra)
        if lu:
            out[lu] = None
    return list(out)


def reason(r, q):
    if r.pos == "QB":
        return f"QB, implied {r.imp_team:.1f}, opp defense rank {int(r.opp_def_rank)} of 32 (1 = toughest)"
    if r.pos == "DST":
        return f"DST, proj {r.proj:.1f}, {r.own:.1f}% owned, no sim draws for DST"
    bits = []
    if r.Team == q.Team:
        bits.append("stack partner")
    elif r.Team == q.Opp:
        bits.append("bring-back")
    bits.append("chalk pool" if r.pool else ("dart under 10%" if r.own < LOW_OWN else "mid-owned, off pool"))
    bits.append(f"proj {r.proj:.1f} for ${int(r.Salary):,} ({r.proj / (r.Salary / 1000):.1f} per $1k)")
    return ", ".join(bits)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--tries", type=int, default=250); ap.add_argument("--seed", type=int, default=11)
    ap.add_argument("--qb-c", default="", help="runbook rule R1: use this QB in lineup C (must still pass the gate unless --allow-gate-fail)")
    ap.add_argument("--allow-gate-fail", action="store_true")
    a = ap.parse_args()
    st = json.loads((HERE / "dfs_status_2026-11-15.json").read_text(encoding="utf-8"))
    m, X, defs, notes, nqb = prepare()
    dnp = {k for k, v in st["practice"].items() if v == "DNP"}
    keep = ((m.pos == "DST") | ((m.pos == "QB") & (m.Salary >= 5000)) | ((m.pos.isin(["RB", "WR", "TE"])) & (m.proj >= 3))) & ~m.Name.isin(dnp)
    dropped_dnp = m[m.Name.isin(dnp)].Name.tolist()
    mask = keep.values
    m2 = m[mask].reset_index(drop=True); X2 = X[mask]
    qg = qb_gates(m2, {k: v[0] for k, v in st["qb_start"].items()})
    m2["qb_gate"] = False
    m2.loc[qg.index, "qb_gate"] = qg.gate_pass
    rng = np.random.default_rng(a.seed)
    is_qb = (m2.pos == "QB").values
    qb_pass = is_qb & m2.qb_gate.values
    qb_low = qb_pass & (m2.own.values < QB_LOW_OWN)
    if a.qb_c:
        pick = is_qb & (m2.Name.values == a.qb_c)
        if not pick.any():
            raise SystemExit(f"--qb-c {a.qb_c}: not a usable QB on the slate")
        if not (pick & m2.qb_gate.values).any():
            print(f"WARNING: {a.qb_c} FAILS the QB gate")
            if not a.allow_gate_fail:
                raise SystemExit("rerun with --allow-gate-fail only if you accept a gate failure")
        qb_low = pick
    print("QB gate passers:", m2[qb_pass].Name.tolist(), "| low-owned (<15%) gate passers:", m2[qb_low].Name.tolist())
    low_skill = ((m2.own.values < LOW_OWN) & ~is_qb).astype(float)
    cands = {
        "C": candidates(m2, X2, qb_low, 5, a.tries, rng, lam_own=0.06, extra=[(low_skill, 2, 9)]),
        "A": candidates(m2, X2, qb_pass, 6, a.tries, rng),
        "B": candidates(m2, X2, qb_pass, 5, a.tries, rng, lam_own=0.015),
    }
    tot = lambda lu: X2[list(lu)].sum(0)
    qbof = lambda lu: [i for i in lu if m2.pos[i] == "QB"][0]
    metric = {"A": lambda t: np.percentile(t, 25), "B": lambda t: t.mean(), "C": lambda t: np.percentile(t, 90)}
    chosen = {}
    for k in ["C", "A", "B"]:
        best = None
        for lu in cands[k]:
            if any(qbof(lu) == qbof(c) for c in chosen.values()):
                continue
            if any(len(set(lu) & set(c)) > MAX_OVERLAP for c in chosen.values()):
                continue
            v = metric[k](tot(lu))
            if best is None or v > best[0]:
                best = (v, lu)
        if best is None:
            raise SystemExit(f"no legal lineup for {k}")
        chosen[k] = best[1]
        print(f"candidates {k}: {len(cands[k])} legal; chosen metric {best[0]:.1f}")
    names = {"A": "A  FLOOR (lean on chalk)", "B": "B  BALANCED", "C": "C  LEVERAGE (low-owned gate QB)"}
    rows = []
    for k in ["A", "B", "C"]:
        ids = m2.loc[list(chosen[k]), "DFS ID"].tolist()
        s = lineup_stats(m2, X2, ids); L = s["L"].copy(); q = s["qb"]
        L["o"] = L.pos.map({"QB": 0, "RB": 1, "WR": 2, "TE": 3, "DST": 5})
        L = L.sort_values(["o", "Salary"], ascending=[True, False])
        print(f"\n=== LINEUP {names[k]} ===")
        for _, r in L.iterrows():
            qs = st["practice"].get(r.Name, "")
            tag = f" [Q, {qs} in practice]" if r.q_flag else ""
            src = "" if r.sim_src == "sim" else " (friend-normal)"
            print(f"  {r.pos:3s} {r.Name:<22s} {r.Team:3s} v {r.Opp:3s} ${int(r.Salary):>5,} proj {r.proj:5.1f} own {r.own:5.1f}% sim avg {r.sim_avg:5.1f} p90 {r.sim_p90:5.1f}{src} {'POOL' if r.pool else ''}{tag}")
            print(f"        why: {reason(r, q)}")
            rows.append(dict(lineup=k, pos=r.pos, name=r.Name, team=r.Team, opp=r.Opp, salary=int(r.Salary), proj=r.proj, own=round(r.own, 2),
                             sim_avg=round(r.sim_avg, 2), sim_p90=round(r.sim_p90, 2), pool=bool(r.pool), q=bool(r.q_flag), dfs_id=int(r["DFS ID"])))
        qq = qg[qg.Name == q.Name].iloc[0]
        print(f"  QB gate: salary>=5000 {qq.g_salary} | starter {qq.g_start} | implied>=21 {qq.g_imp} ({q.imp_team:.1f}) | top-12 sim ceiling {qq.g_ceil} (rank {int(q.qb_ceil_rank)} of {nqb}) | opp def outside top 8 {qq.g_def} (rank {int(q.opp_def_rank)}) => {'PASS' if qq.gate_pass else 'FAIL'}")
        print(f"  salary ${s['salary']:,} (left ${CAP - s['salary']:,}) | sum proj {s['proj']:.1f} | own sum {s['own_sum']:.0f}% avg {s['own_avg']:.1f}% | pool {s['pool']} | stack partners {s['stack']} | bring-backs {s['bring']} | sim avg {s['sim_avg']:.1f} p10 {s['sim_p10']:.1f} p25 {s['sim_p25']:.1f} p90 {s['sim_p90']:.1f}")
    pd.DataFrame(rows).to_csv(OUT / "our_three_lineups_2026-11-15.csv", index=False)
    qb = qb_gates(m[(m.pos == "QB") & (m.proj >= 10)], {k: v[0] for k, v in st["qb_start"].items()})   # board: every projected starter, incl. under $5,000
    qb["start_note"] = qb.Name.map(lambda n: st["qb_start"].get(n, [False, "no entry"])[1])
    qb.sort_values("proj", ascending=False).to_csv(OUT / "qb_board_2026-11-15.csv", index=False)
    m2.assign(in_lineup=m2["DFS ID"].isin(pd.DataFrame(rows)["dfs_id"])).to_csv(OUT / "pool_table_2026-11-15.csv", index=False)
    print("\ndropped for DNP practice:", dropped_dnp)
    print("wrote our_three_lineups, qb_board, pool_table to", OUT)


if __name__ == "__main__":
    main()
