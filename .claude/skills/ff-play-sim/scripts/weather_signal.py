"""Do weather, roof and surface move scoring and play outcomes, and does the market already price it?

1. Game level (schedules, every season on file): actual total minus closing total on wind, cold, roof, surface. If the market already
   prices weather, these coefficients are ~0.
2. Play level (pbp 2023-25): pass completion, pass yards, run yards with and without weather/roof/surface features, train 2023-24, test 2025.
"""
import numpy as np
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier as HGC
from sklearn.ensemble import HistGradientBoostingRegressor as HGR
from sklearn.metrics import log_loss, mean_squared_error

g = pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet")
g = g[(g.game_type == "REG") & g.total.notna() & g.total_line.notna()].copy()
g["resid"] = g.total - g.total_line
g["dome"] = g.roof.isin(["dome", "closed"]).astype(float)
g["wind15"] = ((g.wind >= 15) & (g.dome == 0)).astype(float)
g["wind10"] = ((g.wind >= 10) & (g.dome == 0)).astype(float)
g["cold"] = ((g.temp <= 32) & (g.dome == 0)).astype(float)
g["hot"] = ((g.temp >= 85) & (g.dome == 0)).astype(float)
g["turf"] = (~g.surface.fillna("grass").str.contains("grass")).astype(float)
print(f"GAME LEVEL: {len(g)} games, seasons {g.season.min()}-{g.season.max()}; mean(total - closing total) = {g.resid.mean():+.2f}")
def ols(y, X, names):
    X = np.column_stack([np.ones(len(X)), X])
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    e = y - X @ beta
    XtXi = np.linalg.inv(X.T @ X)
    V = XtXi @ (X.T * (e ** 2)) @ X @ XtXi                 # HC0 robust covariance
    se = np.sqrt(np.diag(V))
    for n, b, s_ in zip(["const"] + names, beta, se):
        print(f"   {n:10s} {b:+7.2f}  (se {s_:.2f}, t {b / s_:+.1f})")


W = ["dome", "wind15", "cold", "hot", "turf"]
print("actual total minus closing total:")
ols(g.resid.values, g[W].values, W)
print("\nactual total on weather + closing total line (weather effect AFTER the market):")
ols(g.total.values, np.column_stack([g[W].values, g.total_line.values]), W + ["total_line"])
print("games by condition:", {k: int(g[k].sum()) for k in ("dome", "wind15", "cold", "hot", "turf")})

# ---- play level
PBP = r"D:\WKP\data\nfl\pbp\play_by_play_%d.parquet"
cols = ["game_id", "season", "play_type", "complete_pass", "sack", "yards_gained", "down", "ydstogo", "yardline_100", "score_differential",
        "half_seconds_remaining", "qtr", "shotgun", "no_huddle", "qb_kneel", "qb_spike", "posteam", "home_team"]
d = pd.concat([pd.read_parquet(PBP % y, columns=cols) for y in (2023, 2024, 2025)], ignore_index=True)
s = g[["game_id", "wind", "temp", "dome", "turf"]].copy()
d = d.merge(s, on="game_id", how="left")
d = d[d.down.notna() & d.score_differential.notna() & (d.qb_kneel != 1) & (d.qb_spike != 1)]
d["wind"] = d.wind.fillna(0)
d["temp"] = d.temp.fillna(70)
for c in ("shotgun", "no_huddle"):
    d[c] = d[c].fillna(0)
d["home"] = (d.posteam == d.home_team).astype(float)
BASE = ["down", "ydstogo", "yardline_100", "score_differential", "half_seconds_remaining", "qtr", "shotgun", "no_huddle", "home"]
WX = ["wind", "temp", "dome", "turf"]
tr, te = d[d.season < 2025], d[d.season == 2025]
for name, mask, target, kind in (
        ("PASS completion log-loss", lambda x: (x.play_type == "pass") & (x.sack != 1), "complete_pass", "clf"),
        ("PASS yards RMSE", lambda x: (x.play_type == "pass") & (x.sack != 1), "yards_gained", "reg"),
        ("RUN yards RMSE", lambda x: x.play_type == "run", "yards_gained", "reg")):
    a, b = tr[mask(tr)], te[mask(te)]
    out = []
    for feats in (BASE, BASE + WX):
        if kind == "clf":
            mo = HGC(max_iter=200, learning_rate=0.06, random_state=0).fit(a[feats], a[target])
            out.append(log_loss(b[target], mo.predict_proba(b[feats])[:, 1]))
        else:
            mo = HGR(max_iter=200, learning_rate=0.06, random_state=0).fit(a[feats], a[target])
            out.append(float(np.sqrt(mean_squared_error(b[target], mo.predict(b[feats])))))
    print(f"\n{name}: situation {out[0]:.4f} | + weather/roof/surface {out[1]:.4f}  ({(out[1] / out[0] - 1) * 100:+.2f}%)")
