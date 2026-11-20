"""dk_own.py - OUR projected field ownership for a DraftKings slate (option A, Zac 2026-11-19). Every number is an ESTIMATE.

Fit and backtest (on a week where we have a reference ownership column, e.g. the friend's Week 10 'My Own'):
  python dk_own.py fit --table OWN_PROJ.csv --ref FRIEND.csv --params PARAMS.json --report REPORT.txt [--oof OOF.csv] [--nosal]
Predict (any week, uses only our own numbers):
  python dk_own.py predict --table OWN_PROJ.csv --params PARAMS.json --out OUT.csv [--nosal]

Model (plain words)
  Ownership is a fixed budget per position: every DK lineup has 1 QB, 1 DST and 7 RB/WR/TE (2 RB + 3 WR + 1 TE + 1 FLEX).
  So the field's ownership adds to 100 percent at QB and DST, and to about 230 RB, 339 WR, 131 TE percent (the FLEX split,
  taken from the Week 10 reference file as a calibration constant; it is a slate-level number, not a player number).
  Inside each position the budget is shared out by a softmax of a popularity score:
     score = a_pos * value + b_pos * projection + c * ceiling + d * team implied total + e * game total + f * salary + g * Q-tag
  value = our DK mean per $1,000, projection = our DK mean, ceiling = our dk_95 percentile, all as percentile ranks inside
  the position on this slate (ranks beat z-scores on the Week 10 backtest: z-scores let one star soak up the budget). For DST the implied total is the OPPONENT's, sign flipped (people chase defenses facing weak offenses).
  Recent usage and news enter through our projection (snap and target shares, injuries, starting QB). Slate size enters through
  the softmax: the same budget spread over fewer games concentrates on the top plays. Coefficients are fit by least squares with
  a small ridge penalty. --nosal drops value and salary (for a week where DK salaries are not out yet; rougher).
Method only, no player data in this file.
"""
import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import spearmanr

POS = ["QB", "RB", "WR", "TE", "DST"]
BUDGET = {"QB": 100.0, "RB": 230.25, "WR": 339.0, "TE": 130.75, "DST": 100.0}   # Week 10 reference FLEX split
RIDGE = 0.02
import os
FORM = os.environ.get("DK_OWN_FORM", "rank")   # 2026-11-19: rank beat z-score on the Week 10 backtest (LOGO MAE 1.95 vs 2.68)


def features(T, nosal=False):
    T = T.copy()
    T["pos"] = T.pos.astype(str)
    imp = T.implied.astype(float)
    if "opp" in T:
        opp_imp = T.opp.map(T.drop_duplicates("team").set_index("team").implied)
        imp = np.where(T.pos == "DST", -opp_imp, imp)
    T["f_imp"] = imp
    T["f_tot"] = T.game_total.astype(float)
    T["f_proj"] = T.dk_mean.astype(float)
    T["f_ceil"] = T.dk_95_percentile.astype(float)
    T["f_q"] = (T.status.fillna("") == "Q").astype(float)
    cols = ["f_proj", "f_ceil", "f_imp", "f_tot"]
    if not nosal:
        T["f_val"] = T.dk_mean / (T.Salary / 1000.0)
        T["f_sal"] = T.Salary.astype(float)
        cols += ["f_val", "f_sal"]
    for c in cols:   # inside position on this slate: percentile rank scaled to -2..2 (default) or z-score (DK_OWN_FORM=z)
        g = T.groupby("pos")[c]
        if FORM == "rank":
            T[c] = (g.rank(pct=True) * 4 - 2).fillna(0)
        else:
            T[c] = ((T[c] - g.transform("mean")) / g.transform("std").replace(0, 1)).fillna(0)
    return T


def unpack(w, nosal):
    k = 0
    a = {}
    for p in POS:
        a[p] = (w[k], 0.0 if nosal else w[k + 1]); k += 1 if nosal else 2
    shared = w[k:]
    return a, shared


def n_params(nosal):
    return len(POS) * (1 if nosal else 2) + (4 if nosal else 5)


def predict(T, w, nosal):
    a, s = unpack(w, nosal)
    out = np.zeros(len(T))
    for p in POS:
        m = (T.pos == p).values
        if not m.any():
            continue
        x = T[m]
        if nosal:
            sc = a[p][0] * x.f_proj + s[0] * x.f_ceil + s[1] * x.f_imp + s[2] * x.f_tot + s[3] * x.f_q
        else:
            sc = a[p][0] * x.f_val + a[p][1] * x.f_proj + s[0] * x.f_ceil + s[1] * x.f_imp + s[2] * x.f_tot + s[3] * x.f_sal + s[4] * x.f_q
        e = np.exp(np.clip(sc.values, -30, 30))
        out[m] = BUDGET[p] * e / e.sum()
    return out


def fit(T, y, train, nosal):
    def loss(w):
        r = predict(T, w, nosal)[train] - y[train]
        return float(np.mean(r ** 2)) + RIDGE * float(np.sum(w ** 2))
    w0 = np.zeros(n_params(nosal)); w0[0] = 1.0
    return minimize(loss, w0, method="L-BFGS-B").x


def metrics(y, pred, T, mask=None):
    m = np.ones(len(y), bool) if mask is None else mask
    rho = spearmanr(y[m], pred[m]).correlation
    mae = float(np.mean(np.abs(y[m] - pred[m])))
    big = m & (y >= 5)
    mae_big = float(np.mean(np.abs(y[big] - pred[big]))) if big.any() else float("nan")
    return rho, mae, mae_big, int(m.sum()), int(big.sum())


def cmd_fit(a):
    T = features(pd.read_csv(a.table), a.nosal)
    ref = pd.read_csv(a.ref)
    T = T.merge(ref[["DFS ID", "My Own"]].rename(columns={"DFS ID": "ID", "My Own": "ref_own"}), on="ID", how="left")
    T["ref_own"] = T.ref_own.fillna(0.0)
    y = T.ref_own.values
    games = T.apply(lambda r: "@".join(sorted([r.team, str(r.opp)])), axis=1).values
    w_all = fit(T, y, np.ones(len(T), bool), a.nosal)
    ins = predict(T, w_all, a.nosal)
    oof = np.zeros(len(T))
    for g in sorted(set(games)):            # leave one game out: fit on the other games, predict this one
        tr = games != g
        oof[~tr] = predict(T, fit(T, y, tr, a.nosal), a.nosal)[~tr]
    L = [f"OWNERSHIP MODEL BACKTEST ({'no-salary variant' if a.nosal else 'full model'}). Every number is an ESTIMATE.",
         f"table {Path(a.table).name}, reference column 'My Own' from {Path(a.ref).name} (the friend's PROJECTED ownership, not actual ownership)",
         f"players: {len(T)} ({T.pos.value_counts().to_dict()}), games {len(set(games))}, params {n_params(a.nosal)}, ridge {RIDGE}",
         ""]
    for tag, pr in (("IN-SAMPLE (fit on all games, optimistic)", ins), ("LEAVE-ONE-GAME-OUT (honest)", oof)):
        rho, mae, mb, n, nb = metrics(y, pr, T)
        L.append(f"{tag}: Spearman {rho:.3f} | MAE {mae:.2f} pts of ownership over {n} players | MAE {mb:.2f} on the {nb} players the reference has at 5%+")
        for p in POS:
            rho, mae, mb, n, nb = metrics(y, pr, T, (T.pos == p).values)
            L.append(f"   {p:3} n={n:3} Spearman {rho:.3f} MAE {mae:5.2f} | 5%+ n={nb:2} MAE {mb:5.2f}")
    T["pred_oof"] = oof; T["pred_in"] = ins; T["err"] = T.pred_oof - T.ref_own
    L.append("")
    L.append("WORST 15 (leave-one-game-out), reference vs our estimate, percent of lineups:")
    for _, r in T.reindex(T.err.abs().sort_values(ascending=False).index).head(15).iterrows():
        L.append(f"   {r['name']:<24} {r.pos:3} {r.team:3} ${int(r.Salary) if 'Salary' in r and not pd.isna(r.Salary) else 0:>5} proj {r.dk_mean:5.1f}  ref {r.ref_own:5.1f}  ours {r.pred_oof:5.1f}  ({r.err:+.1f})")
    top_ref = set(T.nlargest(15, "ref_own").index); top_us = set(T.nlargest(15, "pred_oof").index)
    L.append(f"top-15 overlap (reference top 15 vs our top 15, any position): {len(top_ref & top_us)} of 15")
    for p in ("RB", "WR", "TE"):
        x = T[T.pos == p]
        L.append(f"chalk-pool overlap {p} (top 6 by ownership): {len(set(x.nlargest(6, 'ref_own').index) & set(x.nlargest(6, 'pred_oof').index))} of 6")
    xq = T[T.pos == "QB"]
    L.append(f"QB under 15% owned: reference {sorted(xq[xq.ref_own < 15].name)} | ours {sorted(xq[xq.pred_oof < 15].name)}")
    a_, s_ = unpack(w_all, a.nosal)
    L.append("coefficients (fit on all games): " + json.dumps({p: [round(v, 3) for v in a_[p]] for p in POS}) + " shared " + str([round(v, 3) for v in s_]))
    Path(a.params).write_text(json.dumps({"nosal": a.nosal, "w": list(map(float, w_all)), "budget": BUDGET, "ridge": RIDGE,
                                          "fit_on": Path(a.ref).name}, indent=1), encoding="utf-8")
    Path(a.report).write_text("\n".join(L), encoding="utf-8")
    if a.oof:
        T[["ID", "name", "team", "pos", "Salary", "dk_mean", "ref_own", "pred_in", "pred_oof"]].to_csv(a.oof, index=False)
    print("\n".join(L))


def cmd_predict(a):
    P = json.loads(Path(a.params).read_text(encoding="utf-8"))
    raw = pd.read_csv(a.table)
    T = features(raw, P["nosal"])
    raw["own_est"] = np.round(predict(T, np.array(P["w"]), P["nosal"]), 2)
    raw["own_note"] = "ESTIMATE" + (" (no-salary model, rough)" if P["nosal"] else "")
    raw.to_csv(a.out, index=False)
    print(f"wrote {a.out}: {len(raw)} rows, ownership ESTIMATE, model fit on {P['fit_on']}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    f = sp.add_parser("fit"); f.add_argument("--table", required=True); f.add_argument("--ref", required=True)
    f.add_argument("--params", required=True); f.add_argument("--report", required=True); f.add_argument("--oof"); f.add_argument("--nosal", action="store_true")
    p = sp.add_parser("predict"); p.add_argument("--table", required=True); p.add_argument("--params", required=True); p.add_argument("--out", required=True)
    p.add_argument("--nosal", action="store_true")
    a = ap.parse_args()
    cmd_fit(a) if a.cmd == "fit" else cmd_predict(a)


