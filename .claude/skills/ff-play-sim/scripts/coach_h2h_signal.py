"""Coach head-to-head test (market-relative).

For every game, take the same two head coaches' earlier meetings (any teams, any year), express each as how much the first coach beat the
closing spread, and ask whether that history predicts how this game lands against the closing spread. Also a simpler 'coach vs the
spread overall' persistence check. If the closing line already holds everything, both coefficients are ~0.
"""
import numpy as np
import pandas as pd

g = pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet")
g = g[(g.game_type == "REG") & g.result.notna() & g.spread_line.notna() & g.home_coach.notna() & g.away_coach.notna()].copy()
g = g.sort_values(["season", "week", "gameday"]).reset_index(drop=True)
g["resid"] = g.result - g.spread_line          # home margin vs closing spread (positive = home beat the line)
hist = {}                                       # (coach_a, coach_b) sorted -> list of resid from the view of the alphabetically first coach
rows = []
for r in g.itertuples():
    a, b = r.home_coach, r.away_coach
    key = tuple(sorted((a, b)))
    h = hist.get(key, [])
    # prior meetings, from the home coach's point of view
    sign = 1 if a == key[0] else -1
    prior = [sign * x for x in h]
    if prior:
        rows.append(dict(season=r.season, n_prior=len(prior), prior_mean=float(np.mean(prior)), prior_sum=float(np.sum(prior)), resid=r.resid))
    hist.setdefault(key, []).append((1 if a == key[0] else -1) * r.resid)
d = pd.DataFrame(rows)
print(f"games with at least one prior meeting of the same two coaches: {len(d)} of {len(g)}")
for lo in (1, 2, 3):
    x = d[d.n_prior >= lo]
    b = np.polyfit(x.prior_mean, x.resid, 1)
    X = np.column_stack([np.ones(len(x)), x.prior_mean])
    beta = np.linalg.lstsq(X, x.resid.values, rcond=None)[0]
    e = x.resid.values - X @ beta
    V = np.linalg.inv(X.T @ X) @ (X.T * e ** 2) @ X @ np.linalg.inv(X.T @ X)
    se = np.sqrt(np.diag(V))
    print(f"  >= {lo} prior meetings: n={len(x):5d}  coefficient on prior mean vs-spread {beta[1]:+.3f} (se {se[1]:.3f}, t {beta[1] / se[1]:+.1f})")
x = d[d.season >= 2015]
X = np.column_stack([np.ones(len(x)), x.prior_mean])
beta = np.linalg.lstsq(X, x.resid.values, rcond=None)[0]
e = x.resid.values - X @ beta
V = np.linalg.inv(X.T @ X) @ (X.T * e ** 2) @ X @ np.linalg.inv(X.T @ X)
print(f"  2015+ only: n={len(x)} coefficient {beta[1]:+.3f} (se {np.sqrt(V[1, 1]):.3f})")

# a coach's own record vs the spread: does last season's persist into this season?
cs = []
for r in g.itertuples():
    cs.append(dict(season=r.season, coach=r.home_coach, v=r.resid))
    cs.append(dict(season=r.season, coach=r.away_coach, v=-r.resid))
c = pd.DataFrame(cs).groupby(["coach", "season"]).v.agg(["mean", "count"]).reset_index()
c = c[c["count"] >= 12]
n = c.merge(c.assign(season=c.season - 1), on=["coach", "season"], suffixes=("", "_prev"))
b = np.polyfit(n.mean_prev, n["mean"], 1)
print(f"\ncoach vs-the-spread persistence season to season: n={len(n)}, slope {b[0]:+.3f} (corr {np.corrcoef(n.mean_prev, n['mean'])[0, 1]:+.3f})")
