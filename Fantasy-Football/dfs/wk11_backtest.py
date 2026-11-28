"""wk11_backtest.py - Week 11 hindsight backtest of the DK portfolio selection (DFS only, 2026-11-22). Read only.
Imports dk_gpp functions UNCHANGED (no defaults edited); every variant changes ONE thing vs the control and is scored on ESPN final points.
One slate is noise: this is a diagnostic, not proof."""
import sys, json, csv
from pathlib import Path
import numpy as np, pandas as pd
sys.path.insert(0, r"D:\WKP\Fantasy-Football\dfs")
import dk_gpp as G
from wk11_after_action import load_actual, load_salaries, actual_of, entries, SLOTS, W

SEED, SIMS, TRIES, FIELD = 11, 20000, 120, 17800
OWN = rf"{W}\sun\own_est_week11.csv"
OUTS = ["Trey McBride"]


def pool_and_sim():
    log = []
    slate = json.loads(Path(rf"{W}\slate_week11.json").read_text(encoding="utf-8"))
    p = G.load_own(OWN, slate, False, OUTS, log)
    p = G.check_dk_salaries(rf"{W}\DKSalaries_week11.csv", p, slate, log)
    X = G.simulate(p, SIMS, SEED)
    return p, X, slate


def actual_vec(p, act):
    return np.array([actual_of(act, r.Name, r.Team, r.pos) or 0.0 for r in p.itertuples()])


def gen_cands(p, X, tiers, rotowire=False, seed=SEED):
    """candidate generation exactly as dk_gpp.main (same rng order)."""
    log = []
    drank = G.defense_rank(log)
    gate = np.zeros(len(p), bool); gt = G.qb_gate(p, drank); gate[gt.index] = gt["pass"].values
    pool = G.chalk_pool(p)
    bb = float(np.median(p.drop_duplicates("Team").total))
    rng = np.random.default_rng(seed)
    mean = X.mean(1); proj = p.proj.values; own = p.own.values
    p85 = p.dk_85_percentile.fillna(p.proj * 1.4).values; p95 = p.dk_95_percentile.fillna(p.proj * 1.8).values
    cands = {}
    for name, tier in tiers.items():
        for _ in range(TRIES):
            w = rng.uniform(*tier["ceil_w"]); draw = X[:, rng.integers(0, X.shape[1], 4)].mean(1)
            score = (1 - w) * (0.5 * proj + 0.5 * mean) + w * (0.5 * p85 + 0.5 * p95) * 0.75 + 0.25 * draw - tier["lam"] * own * 3
            lu = G.solve(p, score, tier, pool, gate, bb)
            if lu and lu not in cands:
                cands[lu] = name
    if rotowire:
        idx = {int(r): i for i, r in enumerate(p["DFS ID"])}
        for row in list(csv.reader(open(rf"{W}\DK_upload_10363_20000.csv", encoding="utf-8-sig")))[1:]:
            ids = [int(v) for v in row if v]
            if all(i in idx for i in ids) and len(set(ids)) == 9:
                lu = tuple(sorted(idx[i] for i in ids))
                if lu not in cands and int(p.Salary[list(lu)].sum()) <= 50000:
                    cands[lu] = "rotowire"
    return cands, gate, pool, bb, rng


def select(p, X, cands, gate, pool, bb, rng, tiers, pcap=4, qcap=2, overlap=5, n=7, fallback=True):
    """selection as dk_gpp.main; pcap = a player is usable while his count < pcap (code default 4), qcap likewise (2),
    overlap = max players two lineups may share (5)."""
    own = p.own.values
    keys = list(cands)
    S = np.stack([X[list(k)].sum(0) for k in keys]); cut = np.percentile(S, 99, axis=0)
    dupes = np.array([FIELD * G.DUPE_FACTOR * float(np.prod(np.clip(own[list(k)], 0.05, 100) / 100)) for k in keys])
    V = (S >= cut) / (1 + dupes)[:, None]
    chosen, best, expo, qbc = [], np.zeros(S.shape[1]), {}, {}
    cands = dict(cands)

    def fits(k):
        qb = [i for i in k if p.pos[i] == "QB"][0]
        return qbc.get(qb, 0) < qcap and all(expo.get(i, 0) < pcap for i in k) and all(len(set(k) & set(keys[c])) <= overlap for c in chosen)

    def best_of(ts):
        pick, gain = None, -1
        for j, k in enumerate(keys):
            if j in chosen or (cands[k] not in ts and cands[k] != "rotowire") or not fits(k):
                continue
            g = np.maximum(best, V[j]).sum() - best.sum() + 1e-6 * S[j].mean()
            if g > gain:
                pick, gain = j, g
        return pick

    for st in G.PLAN7[:n]:
        pick = best_of({st})
        order = [st] + [t for t in ("balanced", "core", "leverage") if t != st]
        for tn in order:
            if pick is not None or not fallback:
                break
            if tn != st:
                pick = best_of({tn})
                if pick is not None:
                    break
            ban = np.zeros(len(p), bool)
            ban[[i for i, c in expo.items() if c >= pcap]] = True
            ban[[q for q, c in qbc.items() if c >= qcap]] = True
            tier = tiers[tn]
            for _ in range(20):
                w = rng.uniform(*tier["ceil_w"]); draw = X[:, rng.integers(0, X.shape[1], 4)].mean(1)
                score = ((1 - w) * (0.5 * p.proj.values + 0.5 * X.mean(1))
                         + w * (0.5 * p.dk_85_percentile.fillna(p.proj * 1.4).values + 0.5 * p.dk_95_percentile.fillna(p.proj * 1.8).values) * 0.75
                         + 0.25 * draw - tier["lam"] * own * 3)
                lu = G.solve(p, score, tier, pool, gate, bb, ban=ban, overlap=[keys[c] for c in chosen])
                if lu and lu not in cands:
                    cands[lu] = tn; keys.append(lu)
                    s_new = X[list(lu)].sum(0)
                    d_new = FIELD * G.DUPE_FACTOR * float(np.prod(np.clip(own[list(lu)], 0.05, 100) / 100))
                    S = np.vstack([S, s_new]); dupes = np.append(dupes, d_new); V = np.vstack([V, (s_new >= cut) / (1 + d_new)])
            pick = best_of({tn})
        if pick is None:
            return [keys[j] for j in chosen], cands, "STOPPED at lineup %d" % (len(chosen) + 1)
        chosen.append(pick); best = np.maximum(best, V[pick])
        for i in keys[pick]:
            expo[i] = expo.get(i, 0) + 1
        qb = [i for i in keys[pick] if p.pos[i] == "QB"][0]; qbc[qb] = qbc.get(qb, 0) + 1
    return [keys[j] for j in chosen], cands, "ok"


def report(name, lus, A, note=""):
    sc = sorted([float(A[list(k)].sum()) for k in lus], reverse=True)
    return dict(variant=name, n=len(lus), best=round(sc[0], 1) if sc else None, mean=round(float(np.mean(sc)), 1) if sc else None,
                n_ge150=sum(s >= 150 for s in sc), n_ge140=sum(s >= 140 for s in sc), scores=[round(s, 1) for s in sc], note=note)
