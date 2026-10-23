"""Walk-forward team-level backtest of play_engine.py.

For every game in the chosen weeks the tables are rebuilt from games played BEFORE that week (nothing from the game or later),
the game is simulated N times, and the result is compared with the real score and with the closing market line.
Four configs isolate the layers: full, no_def (league-average defense), no_coach (league-average coach), neither.

Usage:  python backtest_engine.py [--n 300] [--weeks 2025:5-18 2026:3-6]
Output: D:\\WKP\\data\\ff-play-sim\\backtest_games.csv + a printed summary.
"""
import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import play_engine as pe

OUT = Path(r"D:\WKP\data\ff-play-sim")
HFA = 1.5     # home-field points added to the simulated margin (the engine has no home edge of its own)
CFG = {"full": (True, True, 1.0), "stretch15": (True, True, 1.5), "stretch20": (True, True, 2.0),
       "no_def": (False, True, 1.0), "no_coach": (True, False, 1.0)}


def games_of(pbp, season, week):
    g = pbp[(pbp.season == season) & (pbp.week == week)].groupby("game_id").agg(
        home=("home_team", "first"), away=("away_team", "first"), hc=("home_coach", "first"), ac=("away_coach", "first"),
        spread=("spread_line", "first"), total_line=("total_line", "first"), result=("result", "first"), total=("total", "first"))
    return g.reset_index()


def run(weeks, n):
    pbp = pe.load_pbp()
    rows = []
    for season, wk in weeks:
        as_of = season * 100 + wk
        T = pe.Tables(pbp, as_of)
        for _, g in games_of(pbp, season, wk).iterrows():
            if pd.isna(g.result) or pd.isna(g.spread):
                continue
            rec = dict(game_id=g.game_id, season=season, week=wk, home=g.home, away=g.away, spread=g.spread,
                       total_line=g.total_line, result=g.result, total=g.total)
            for name, (ud, uc, sx) in CFG.items():
                mh = pe.Matchup(T, g.home, g.away, off_coach=g.hc, use_def=ud, use_coach=uc, stretch=sx)
                ma = pe.Matchup(T, g.away, g.home, off_coach=g.ac, use_def=ud, use_coach=uc, stretch=sx)
                H, A, HN, AN = pe.sim_game(T, mh, ma, n=n, seed=hash(g.game_id) % 100000)
                rec[f"{name}_margin"] = float((H - A).mean()) + HFA
                rec[f"{name}_total"] = float((H + A).mean())
                rec[f"{name}_plays"] = float((HN + AN).mean())
            rows.append(rec)
        print(f"{season} wk{wk}: {len(rows)} games so far", flush=True)
    d = pd.DataFrame(rows)
    OUT.mkdir(parents=True, exist_ok=True)
    d.to_csv(OUT / "backtest_games.csv", index=False)
    return d


def summarize(d):
    print(f"\n{len(d)} games, {d.season.min()} to {d.season.max()}")
    mk_mae = (d.result - d.spread).abs().mean()
    print(f"Market spread: MAE {mk_mae:.2f}   total line MAE {(d.total - d.total_line).abs().mean():.2f}")
    for name in CFG:
        sm = d[f"{name}_margin"]
        st = d[f"{name}_total"]
        mae = (d.result - sm).abs().mean()
        bias_t = (st - d.total).mean()
        corr_m = np.corrcoef(sm, d.result)[0, 1]
        corr_t = np.corrcoef(st, d.total)[0, 1]
        corr_mk = np.corrcoef(d.spread, d.result)[0, 1]
        # does the sim residual vs the market predict the result?  result = a + b*spread + c*(sim - spread)
        X = np.column_stack([np.ones(len(d)), d.spread.values, (sm - d.spread).values])
        beta, *_ = np.linalg.lstsq(X, d.result.values, rcond=None)
        res = d.result.values - X @ beta
        se = np.sqrt(np.diag(np.linalg.inv(X.T @ X)) * res.var(ddof=3))
        print(f"\n[{name}] margin MAE {mae:.2f} (market {mk_mae:.2f}) | corr margin {corr_m:.3f} (market {corr_mk:.3f}) | "
              f"total bias {bias_t:+.2f} corr {corr_t:.3f} | sd of sim margin {sm.std():.2f} vs spread {d.spread.std():.2f}")
        print(f"   residual-vs-market coef {beta[2]:+.3f} (se {se[2]:.3f}, t {beta[2] / se[2]:+.1f})")
        for thr in (1, 2, 3):
            edge = sm - d.spread
            pick = edge.abs() >= thr
            if pick.sum() == 0:
                continue
            side = np.sign(edge[pick])
            cover = np.sign(d.result[pick] - d.spread[pick])
            push = cover == 0
            w = ((side == cover) & ~push).sum()
            l = ((side != cover) & ~push).sum()
            print(f"   bet sim side when |edge| >= {thr}: {w}-{l} ({w / max(1, w + l):.1%}), {pick.sum()} games")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=300)
    ap.add_argument("--weeks", nargs="*", default=["2025:5-18", "2026:3-6"])
    a = ap.parse_args()
    wk = []
    for tok in a.weeks:
        s, r = tok.split(":")
        lo, hi = r.split("-")
        wk += [(int(s), w) for w in range(int(lo), int(hi) + 1)]
    summarize(run(wk, a.n))
