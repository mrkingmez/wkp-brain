"""Independent team-strength rating from play-by-play EPA, tested against the betting market.

Why: the game simulator takes its score line from the market, so its win odds are the market's
odds. This builds a second opinion that uses only football data (opponent-adjusted offense and
defense EPA per play, recent games weighted more), then tests honestly whether blending it with
the market ever beats the market alone on games it has not seen.

python power_rating.py 2026 6          backtest 2024 wk6 .. 2026 wk5, then print week 6 ratings
Outputs: D:\\WKP\\data\\ff-simulator\\power_backtest.csv and power_<season>_wk<week>.csv
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

PBP = Path(r"D:\WKP\data\nfl\pbp")
OUT = Path(r"D:\WKP\data\ff-simulator")
DECAY = 0.93          # per game back (team's own game index)
LAMBDA = 6.0          # ridge strength, in play-weight units scaled below
YEARS = (2023, 2024, 2025, 2026)


def team_games():
    fr = []
    for y in YEARS:
        f = PBP / f"play_by_play_{y}.parquet"
        if f.exists():
            fr.append(pd.read_parquet(f, columns=["season", "week", "season_type", "posteam", "defteam", "play_type", "epa"]))
    p = pd.concat(fr, ignore_index=True)
    p = p[(p.season_type == "REG") & p.play_type.isin(["pass", "run"]) & p.epa.notna() & p.posteam.notna() & p.defteam.notna()]
    g = p.groupby(["season", "week", "posteam", "defteam"]).epa.agg(["mean", "count"]).reset_index()
    g["order"] = g.season * 100 + g.week
    return g


def fit(tg, as_of):
    """Ridge: epa_per_play = mu + off[team] + def[opp] with recency weights. Returns (net rating dict, mu)."""
    d = tg[tg.order < as_of].copy()
    teams = sorted(set(d.posteam) | set(d.defteam))
    ix = {t: i for i, t in enumerate(teams)}
    n = len(teams)
    # recency by each offense's own game index counted from its latest game
    d = d.sort_values("order")
    d["back"] = d.groupby("posteam").cumcount(ascending=False)
    d["w"] = DECAY ** d.back * d["count"] / 60.0
    X = np.zeros((len(d), 2 * n + 1))
    X[:, 0] = 1
    for r, (o, df) in enumerate(zip(d.posteam, d.defteam)):
        X[r, 1 + ix[o]] = 1
        X[r, 1 + n + ix[df]] = 1
    y = d["mean"].values
    W = d.w.values
    A = X.T @ (X * W[:, None])
    reg = np.eye(2 * n + 1) * LAMBDA
    reg[0, 0] = 0
    beta = np.linalg.solve(A + reg, X.T @ (W * y))
    off = {t: beta[1 + ix[t]] for t in teams}
    dfn = {t: beta[1 + n + ix[t]] for t in teams}
    net = {t: off[t] - dfn[t] for t in teams}      # defense coefficient > 0 means it allows EPA
    return net, off, dfn


def main():
    season, week = int(sys.argv[1]), int(sys.argv[2])
    tg = team_games()
    sch = pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet")
    sch = sch[(sch.game_type == "REG")].copy()
    sch["order"] = sch.season * 100 + sch.week
    rows = []
    for s in (2024, 2025, 2026):
        for w in range(6, 19):
            o = s * 100 + w
            if o >= season * 100 + week:
                continue
            gm = sch[(sch.season == s) & (sch.week == w) & sch.result.notna()]
            if gm.empty:
                continue
            net, _, _ = fit(tg, o)
            for _, r in gm.iterrows():
                if r.home_team in net and r.away_team in net:
                    rows.append(dict(order=o, season=s, week=w, home=r.home_team, away=r.away_team,
                                     rating=net[r.home_team] - net[r.away_team], market=r.spread_line, actual=r.result))
    bt = pd.DataFrame(rows)
    bt.to_csv(OUT / "power_backtest.csv", index=False)
    print(f"{len(bt)} games backtested, {bt.market.notna().sum()} with a market line")
    m = bt.dropna(subset=["market"])
    # margin is home minus away; market is home-favoured positive. Fit scale of rating on history before each season.
    res = []
    for s in sorted(m.season.unique()):
        tr = m[m.season < s] if s > m.season.min() else m[m.season == s]
        te = m[m.season == s]
        # y - market regressed on rating (does the rating explain what the market missed?)
        X = np.c_[np.ones(len(tr)), tr.rating.values]
        yv = (tr.actual - tr.market).values
        b = np.linalg.lstsq(X, yv, rcond=None)[0]
        res.append((s, len(te), b[1], np.abs(te.actual - te.market).mean(),
                    np.abs(te.actual - (te.market + b[0] + b[1] * te.rating)).mean()))
    print("season  n   weight on rating (points per EPA unit)   MAE market   MAE market+rating")
    for r in res:
        print(f"{r[0]}  {r[1]:4d}   {r[2]:8.2f}   {r[3]:.3f}   {r[4]:.3f}")
    # one overall out-of-sample check: leave-one-season-out
    allp = []
    for s in sorted(m.season.unique()):
        tr, te = m[m.season != s], m[m.season == s]
        X = np.c_[np.ones(len(tr)), tr.rating.values]
        b = np.linalg.lstsq(X, (tr.actual - tr.market).values, rcond=None)[0]
        allp.append(np.c_[te.actual - te.market, te.actual - (te.market + b[0] + b[1] * te.rating)])
    allp = np.vstack(allp)
    print(f"leave-one-season-out: market MAE {np.abs(allp[:, 0]).mean():.3f}, market+rating MAE {np.abs(allp[:, 1]).mean():.3f}, "
          f"market RMSE {np.sqrt((allp[:, 0] ** 2).mean()):.3f}, blend RMSE {np.sqrt((allp[:, 1] ** 2).mean()):.3f}")
    X = np.c_[np.ones(len(m)), m.rating.values]
    b = np.linalg.lstsq(X, (m.actual - m.market).values, rcond=None)[0]
    resid = (m.actual - m.market).values - X @ b
    se = np.sqrt(resid.var() / (m.rating.var() * len(m)))
    print(f"all-data weight on rating: {b[1]:.2f} +/- {se:.2f} points per EPA unit, intercept {b[0]:+.2f}")
    # current ratings
    net, off, dfn = fit(tg, season * 100 + week)
    cur = pd.DataFrame({"team": list(net), "net": [net[t] for t in net], "off": [off[t] for t in net], "def": [dfn[t] for t in net]})
    cur = cur.sort_values("net", ascending=False)
    cur.to_csv(OUT / f"power_{season}_wk{week}.csv", index=False)
    pd.set_option("display.width", 200)
    print(cur.round(3).to_string(index=False))
    np.save(OUT / "power_blend_coef.npy", b)


if __name__ == "__main__":
    main()
