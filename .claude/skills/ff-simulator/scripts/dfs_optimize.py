"""DraftKings / FanDuel lineup builder on the simulator's draws.

python dfs_optimize.py dk <DKSalaries.csv> [--n 20] [--stack] [--mode gpp|cash] [--season 2026 --week 6]
python dfs_optimize.py fd <FanDuel-players-list.csv> [...]

Download the salary file yourself from the slate's page (DraftKings: Draft Team screen, "Export to CSV";
FanDuel: the lineup page's player-list download). The file is read as data only.

Method: each candidate lineup is the salary-cap-legal lineup that scores best in one randomly chosen
simulated slate (blended with the average so it is not pure noise). Hundreds of candidates are built, then every
one is scored on ALL 4,000 simulated slates, and the best N are kept: by average for cash games, by 90th
percentile for tournaments. --stack forces a pass catcher from the QB's team.
The defense/DST slot is not simulated (IDP scoring is not DraftKings scoring): it is filled from the file's
average points, flagged in the output.
Classic NFL rosters: QB, 2 RB, 3 WR, TE, FLEX (RB/WR/TE), DST. Caps: DraftKings 50,000, FanDuel 60,000.
"""
import argparse
import re
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import Bounds, LinearConstraint, milp

OUT = Path(r"D:\WKP\data\ff-simulator")
TEAM_FIX = {"LAR": "LA", "JAC": "JAX", "WSH": "WAS", "LVR": "LV", "ARZ": "ARI", "BLT": "BAL", "CLV": "CLE", "HST": "HOU",
            "SD": "LAC", "OAK": "LV", "STL": "LA", "GBP": "GB", "KCC": "KC", "NEP": "NE", "NOS": "NO", "SFO": "SF",
            "TBB": "TB", "SEA": "SEA"}
CAP = {"dk": 50000, "fd": 60000}


def norm(s):
    s = re.sub(r"[.,'’]", "", str(s).lower())
    s = re.sub(r"\b(jr|sr|ii|iii|iv|v)\b", "", s)
    return re.sub(r"\s+", " ", s).strip()


def load_salaries(site, path):
    d = pd.read_csv(path)
    if site == "dk":
        d = d.rename(columns={"Name": "name", "Position": "pos", "Salary": "salary", "TeamAbbrev": "team",
                              "AvgPointsPerGame": "avg"})
        d = d[["name", "pos", "salary", "team", "avg"]]
    else:
        d["name"] = (d["First Name"].fillna("") + " " + d["Last Name"].fillna("")).str.strip()
        d = d.rename(columns={"Position": "pos", "Salary": "salary", "Team": "team", "FPPG": "avg"})
        d = d[["name", "pos", "salary", "team", "avg"]]
    d["team"] = d.team.replace(TEAM_FIX)
    d["pos"] = d.pos.replace({"D": "DST", "DEF": "DST"})
    d["key"] = d.name.map(norm)
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("site", choices=["dk", "fd"])
    ap.add_argument("csv")
    ap.add_argument("--n", type=int, default=20)
    ap.add_argument("--stack", action="store_true")
    ap.add_argument("--mode", choices=["gpp", "cash"], default="gpp")
    ap.add_argument("--season", type=int, default=2026)
    ap.add_argument("--week", type=int, default=6)
    ap.add_argument("--tries", type=int, default=300)
    a = ap.parse_args()

    z = np.load(OUT / f"dfs_draws_{a.season}_wk{a.week}.npz")
    D = z[a.site].astype(np.float64)
    sim = pd.DataFrame({"name": z["names"], "team": z["teams"], "pos": z["groups"]})
    sim["key"] = sim.name.map(norm)
    sim["row"] = range(len(sim))
    sal = load_salaries(a.site, a.csv)
    m = sal.merge(sim[["key", "team", "row"]], on=["key", "team"], how="left")
    miss = m[m.row.isna() & m.pos.isin(["QB", "RB", "WR", "TE"]) & (m.salary >= 4000)]
    m = m[m.row.notna() | (m.pos == "DST")].reset_index(drop=True)
    n = len(m)
    S = D.shape[1]
    X = np.zeros((n, S))
    for i, r in m.iterrows():
        X[i] = D[int(r.row)] if pd.notna(r.row) else float(r.avg if pd.notna(r.avg) else 6.0)
    mean, p90 = X.mean(1), np.percentile(X, 90, axis=1)
    pos = m.pos.values
    sa = m.salary.values.astype(float)
    print(f"{n} players matched to the simulation; {len(miss)} skill players over $4,000 had no match (no simulated game or bye): "
          + ", ".join(miss.name.head(12)))

    def solve(score, ban=None):
        A, lo, hi = [], [], []
        A.append(sa); lo.append(0); hi.append(CAP[a.site])
        for p, lo_, hi_ in (("QB", 1, 1), ("RB", 2, 3), ("WR", 3, 4), ("TE", 1, 2), ("DST", 1, 1)):
            A.append((pos == p).astype(float)); lo.append(lo_); hi.append(hi_)
        A.append(np.isin(pos, ["QB", "RB", "WR", "TE"]).astype(float)); lo.append(8); hi.append(8)
        if a.stack:
            for q in np.where(pos == "QB")[0]:
                row = ((m.team.values == m.team.values[q]) & np.isin(pos, ["WR", "TE"])).astype(float)
                row[q] = -1
                A.append(row); lo.append(0); hi.append(np.inf)
        if ban is not None:
            for prev in ban:
                row = np.zeros(n); row[list(prev)] = 1
                A.append(row); lo.append(0); hi.append(len(prev) - 1)
        res = milp(-score, constraints=LinearConstraint(np.array(A), lo, hi), integrality=np.ones(n),
                   bounds=Bounds(0, 1))
        if not res.success:
            return None
        return tuple(np.where(res.x > 0.5)[0])

    rng = np.random.default_rng(11)
    cands = {}
    base = solve(mean)
    if base:
        cands[base] = None
    for _ in range(a.tries):
        s = rng.integers(0, S, 3)
        score = 0.5 * mean + 0.5 * X[:, s].mean(1)
        lu = solve(score)
        if lu:
            cands[lu] = None
    if not cands:
        raise SystemExit("no legal lineup found: check the salary file columns and the cap")
    rows = []
    for lu in cands:
        t = X[list(lu)].sum(0)
        rows.append((lu, t.mean(), np.percentile(t, 90), np.percentile(t, 10)))
    key = 1 if a.mode == "cash" else 2
    rows.sort(key=lambda r: -r[key])
    out = []
    print(f"{len(rows)} distinct legal lineups built; showing the best {a.n} by {'average' if a.mode == 'cash' else '90th percentile'}")
    for rank, (lu, mu, hi, lo) in enumerate(rows[: a.n], 1):
        ps = sorted(lu, key=lambda i: ["QB", "RB", "WR", "TE", "DST"].index(pos[i]))
        print(f"\nLineup {rank}: avg {mu:.1f} | 10th {lo:.1f} | 90th {hi:.1f} | salary ${int(sa[list(lu)].sum()):,}")
        for i in ps:
            tag = "  (defense: file average, not simulated)" if pos[i] == "DST" else ""
            print(f"   {pos[i]:3s} {m.name[i]:<24s} {m.team[i]:4s} ${int(sa[i]):>6,}  avg {mean[i]:5.1f}{tag}")
            out.append(dict(lineup=rank, pos=pos[i], name=m.name[i], team=m.team[i], salary=int(sa[i]), avg=round(mean[i], 1)))
    pd.DataFrame(out).to_csv(OUT / f"dfs_lineups_{a.site}_{a.season}_wk{a.week}.csv", index=False)
    print("\nsaved", OUT / f"dfs_lineups_{a.site}_{a.season}_wk{a.week}.csv")


if __name__ == "__main__":
    main()
