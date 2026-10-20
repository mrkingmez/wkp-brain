"""Starters-only read of backtest_sim.csv, plus the best blend of simulation and plain average."""
import numpy as np
import pandas as pd

d = pd.read_csv(r"D:\WKP\data\ff-simulator\backtest_sim.csv").dropna(subset=["base"])
th = {"QB": 12, "RB": 6, "WR": 6, "TE": 5, "K": 3, "DL": 2, "LB": 3, "DB": 2.5}
print("Starters only (simulated mean above a position threshold)")
print("pos    n   MAE sim  MAE avg  MAE blend (w_sim)   rank corr sim/avg    bias sim/avg     p10-p90")
tot = {"sim": [], "avg": [], "blend": []}
for g, t in th.items():
    x = d[(d.group == g) & (d.sim >= t)]
    if len(x) < 40:
        continue
    best = min(((np.abs(w * x.sim + (1 - w) * x.base - x.actual).mean(), w) for w in np.linspace(0, 1, 11)))

    def rc(col):
        return np.nanmean([y[col].corr(y.actual, method="spearman") for _, y in x.groupby("order") if len(y) > 6])

    cov = ((x.actual >= x.p10) & (x.actual <= x.p90)).mean()
    print(f"{g:3s} {len(x):5d}  {np.abs(x.sim - x.actual).mean():7.2f}  {np.abs(x.base - x.actual).mean():7.2f}  "
          f"{best[0]:7.2f} ({best[1]:.1f})      {rc('sim'):.3f} / {rc('base'):.3f}   "
          f"{(x.sim - x.actual).mean():+.2f} / {(x.base - x.actual).mean():+.2f}   {cov:.0%}")
