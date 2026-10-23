r"""Does the injury report move a game's true margin away from the closing line? Walk-forward backtest.

python injury_margin.py            backtest 2018-2026, print verdict
Writes D:\WKP\data\ff-simulator\injury_margin_backtest.csv (one row per game) and injury_margin_coef.json.

Per team-week: qb_loss = (starting-level QB rolling fantasy points - 8) if the QB is Out (x0.75 if Doubtful).
skill_loss = sum of rolling fantasy points of Out/Doubtful RB/WR/TE who average 6+ (Doubtful x0.75).
Rolling = mean of the player's previous 6 games, using only games before that week.
Target: result - spread_line (how far the game landed from the CLOSING line, home perspective).
Offense only; defensive injuries are not measured. Report status is the final one (Friday), so this tests the
closing line, not the Monday line (nflverse keeps no opening lines).
"""
import json
from pathlib import Path

import nflreadpy as nr
import numpy as np
import pandas as pd

OUT = Path(r"D:\WKP\data\ff-simulator")
FIX = {"LAR": "LA", "WSH": "WAS", "JAC": "JAX", "ARZ": "ARI", "BLT": "BAL", "CLV": "CLE", "HST": "HOU", "SD": "LAC", "STL": "LA", "OAK": "LV"}
YEARS = list(range(2018, 2027))


def tm(s):
    return s.map(lambda t: FIX.get(t, t))


def rolling_table():
    s = nr.load_player_stats(YEARS).to_pandas()
    s = s[(s.season_type == "REG") & s.position.isin(["QB", "RB", "WR", "TE"])].copy()
    s["t"] = s.season * 100 + s.week
    s = s.sort_values(["player_id", "t"])
    s["roll"] = s.groupby("player_id").fantasy_points_ppr.transform(lambda x: x.rolling(6, min_periods=2).mean())
    return s[["player_id", "t", "roll", "position"]].dropna()


def team_week_features():
    inj = nr.load_injuries(YEARS).to_pandas()
    inj = inj[(inj.game_type == "REG") & inj.report_status.isin(["Out", "Doubtful"]) & inj.position.isin(["QB", "RB", "WR", "TE"])].copy()
    inj["t"] = inj.season * 100 + inj.week
    inj["team"] = tm(inj.team)
    inj["w"] = np.where(inj.report_status == "Out", 1.0, 0.75)
    inj["t"] = inj.t.astype(int)
    inj["k"] = inj.gsis_id
    rt = rolling_table()
    rt["t"] = rt.t.astype(int)
    rt["k"] = rt.player_id
    m = pd.merge_asof(inj.sort_values("t"), rt[["t", "k", "roll"]].sort_values("t"), on="t", by="k",
                      direction="backward", allow_exact_matches=False).dropna(subset=["roll"])
    qb = m[(m.position == "QB") & (m.roll >= 12)].assign(v=lambda d: (d.roll - 8) * d.w)
    sk = m[m.position.isin(["RB", "WR", "TE"]) & (m.roll >= 6)].assign(v=lambda d: d.roll * d.w)
    f_qb = qb.groupby(["season", "week", "team"]).v.max().rename("qb_loss")
    f_sk = sk.groupby(["season", "week", "team"]).v.sum().rename("skill_loss")
    return pd.concat([f_qb, f_sk], axis=1).fillna(0).reset_index()


def ols(X, y):
    X1 = np.column_stack([np.ones(len(X)), X])
    b, *_ = np.linalg.lstsq(X1, y, rcond=None)
    res = y - X1 @ b
    cov = np.linalg.inv(X1.T @ X1) * res.var(ddof=X1.shape[1])
    return b, np.sqrt(np.diag(cov))


if __name__ == "__main__":
    f = team_week_features()
    g = nr.load_schedules(YEARS).to_pandas()
    g = g[(g.game_type == "REG") & g.result.notna() & g.spread_line.notna()].copy()
    g["home_team"], g["away_team"] = tm(g.home_team), tm(g.away_team)
    for side in ("home", "away"):
        g = g.merge(f.rename(columns={"team": f"{side}_team", "qb_loss": f"{side}_qb", "skill_loss": f"{side}_sk"}),
                    on=["season", "week", f"{side}_team"], how="left")
    g[["home_qb", "home_sk", "away_qb", "away_sk"]] = g[["home_qb", "home_sk", "away_qb", "away_sk"]].fillna(0)
    g["x_qb"] = g.away_qb - g.home_qb
    g["x_sk"] = g.away_sk - g.home_sk
    g["resid"] = g.result - g.spread_line
    print(f"{len(g)} games, {g.season.min()}-{g.season.max()}; games with a QB out: {(g.x_qb != 0).sum()}; "
          f"games with skill players out: {(g.x_sk != 0).sum()}")
    X = g[["x_qb", "x_sk"]].to_numpy()
    b, se = ols(X, g.resid.to_numpy())
    print(f"\nAll seasons: points the game lands away from the closing line per unit of injury loss")
    for n, bb, ss in zip(["intercept", "QB out", "skill out"], b, se):
        print(f"  {n:10s} {bb:7.3f}  (se {ss:.3f}, t {bb/ss:5.1f})")
    rows = []
    for S in range(2022, 2027):
        tr, te = g[g.season < S], g[g.season == S]
        if te.empty:
            continue
        bb, _ = ols(tr[["x_qb", "x_sk"]].to_numpy(), tr.resid.to_numpy())
        adj = bb[1] * te.x_qb + bb[2] * te.x_sk
        te = te.assign(adj=adj)
        rows.append(te)
        mse0, mse1 = (te.resid ** 2).mean(), ((te.resid - adj) ** 2).mean()
        print(f"\n{S}: {len(te)} games  error vs closing {mse0**.5:.2f} -> {mse1**.5:.2f} after adjusting")
        for thr in (1.0, 2.0):
            bet = te[te.adj.abs() >= thr]
            bet = bet[bet.resid != 0]
            wins = ((np.sign(bet.adj) == np.sign(bet.resid))).sum()
            if len(bet):
                print(f"   adjustment >= {thr:.0f} pt: bet {len(bet)}, covers {wins} ({wins/len(bet):.1%}; 52.4% breaks even)")
    allt = pd.concat(rows)
    allt.to_csv(OUT / "injury_margin_backtest.csv", index=False)
    json.dump(dict(qb=float(b[1]), skill=float(b[2]), intercept=float(b[0])), open(OUT / "injury_margin_coef.json", "w"))
    print("\nPooled 2022 onward:")
    for thr in (0.5, 1.0, 2.0):
        bet = allt[(allt.adj.abs() >= thr) & (allt.resid != 0)]
        w = (np.sign(bet.adj) == np.sign(bet.resid)).sum()
        print(f"   adjustment >= {thr} pt: bet {len(bet)}, covers {w} ({w/len(bet):.1%})")
