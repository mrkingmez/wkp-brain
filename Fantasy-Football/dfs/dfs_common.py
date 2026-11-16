"""Shared pieces for dfs_build.py and dfs_compare.py: sim join, defense rank vs QBs, QB gate, chalk pool, lineup stats."""
import re
from pathlib import Path
import numpy as np
import pandas as pd
from dfs_load import load, PROJ, SAL

SIM = Path(r"D:\WKP\data\ff-simulator\dfs_draws_2026_wk10.npz")
STATS = Path(r"D:\WKP\data\nfl\stats_player\stats_player_week_2026.parquet")
CAP = 50000
LOW_OWN = 10.0   # ASSUMPTION (Fantasy director): "low-owned" means projected ownership under 10 percent
TEAM_FIX = {"LAR": "LA", "JAC": "JAX", "WSH": "WAS"}


def norm(s):
    s = re.sub(r"[.,'’]", "", str(s).lower())
    s = re.sub(r"\b(jr|sr|ii|iii|iv|v)\b", "", s)
    return re.sub(r"\s+", " ", s).strip()


def defense_vs_qb(through_week=9):
    """DK points allowed per game to opposing QBs (QBs with 10+ attempts in the game), 2026 regular season weeks 1..through_week.
    Rank 1 = TOUGHEST defense (fewest points allowed). 'Top 8' defense = rank 1 to 8."""
    d = pd.read_parquet(STATS)
    q = d[(d.position == "QB") & (d.attempts >= 10) & (d.season_type == "REG") & (d.week <= through_week)].copy()
    fum = q.sack_fumbles_lost.fillna(0) + q.rushing_fumbles_lost.fillna(0)
    q["dk"] = (q.passing_yards * .04 + q.passing_tds * 4 - q.passing_interceptions + q.rushing_yards * .1 + q.rushing_tds * 6
               + (q.passing_yards >= 300) * 3 + (q.rushing_yards >= 100) * 3 - fum
               + 2 * (q.passing_2pt_conversions.fillna(0) + q.rushing_2pt_conversions.fillna(0)))
    g = q.groupby("opponent_team").agg(dk_allowed=("dk", "mean"), games=("dk", "size")).sort_values("dk_allowed")
    g["def_rank"] = range(1, len(g) + 1)
    g.index = [TEAM_FIX.get(t, t) for t in g.index]
    return g


def load_sim():
    z = np.load(SIM, allow_pickle=True)
    s = pd.DataFrame({"name": z["names"], "team": z["teams"], "pos": z["groups"]})
    s["key"] = s.name.map(norm)
    s["row"] = range(len(s))
    return s, z["dk"].astype(np.float32)


def build_pool(slate):
    """Chalk pool: top 6 RB, WR, TE by projected ownership, plus any top-6 by projection at that position not already in."""
    pool = set()
    for p in ["RB", "WR", "TE"]:
        d = slate[slate.pos1 == p]
        pool |= set(d.nlargest(6, "own")["DFS ID"])
        pool |= set(d.nlargest(6, "proj")["DFS ID"])
    return pool


def prepare(draws_n=20000, seed=7):
    """Returns slate with sim columns, the draw matrix aligned to slate rows, defense table."""
    slate, full, notes = load(PROJ, SAL, verbose=False)
    slate["key"] = slate.Name.map(norm)
    sim, D = load_sim()
    m = slate.merge(sim[["key", "team", "row"]], left_on=["key", "Team"], right_on=["key", "team"], how="left")
    m = m.drop(columns=["team"])
    rng = np.random.default_rng(seed)
    S = D.shape[1]
    X = np.zeros((len(m), S), dtype=np.float32)
    src = []
    for i, r in m.iterrows():
        if pd.notna(r.row) and r.pos1 != "DST":
            X[i] = D[int(r.row)]; src.append("sim")
        else:
            mu = r.proj; sd = r.dk_std if pd.notna(r.dk_std) and r.dk_std > 0 else max(2.5, 0.45 * mu)
            X[i] = np.maximum(-4, rng.normal(mu, sd, S)); src.append("friend-normal")
    m["sim_src"] = src
    m["sim_avg"] = X.mean(1); m["sim_p90"] = np.percentile(X, 90, axis=1)
    m["slots"] = m.slots
    m["pos"] = m.pos1
    defs = defense_vs_qb()
    m["opp_def_rank"] = m.Opp.map(defs.def_rank)
    m["opp_def_dk_allowed"] = m.Opp.map(defs.dk_allowed)
    m["pool"] = m["DFS ID"].isin(build_pool(m))
    # QB gate inputs
    allqb = sim[sim.pos == "QB"].copy()
    allqb["p90"] = np.percentile(D[allqb.row.values], 90, axis=1)
    allqb = allqb.sort_values("p90", ascending=False).drop_duplicates(["key"])
    allqb["ceil_rank"] = range(1, len(allqb) + 1)
    k = m.merge(allqb[["key", "team", "ceil_rank"]], left_on=["key", "Team"], right_on=["key", "team"], how="left")
    m["qb_ceil_rank"] = k.ceil_rank.values
    return m, X, defs, notes, len(allqb)


def qb_gates(m, confirmed):
    """confirmed: dict {QB name: bool starter confirmed}. Gate: confirmed starter, implied >= 21, top-12 sim ceiling, opp def rank > 8, salary >= 5000."""
    q = m[m.pos == "QB"].copy()
    q["g_salary"] = q.Salary >= 5000
    q["g_start"] = q.Name.map(lambda n: confirmed.get(n, False))
    q["g_imp"] = q.imp_team >= 21
    q["g_ceil"] = q.qb_ceil_rank <= 12
    q["g_def"] = q.opp_def_rank > 8
    q["gate_pass"] = q[["g_salary", "g_start", "g_imp", "g_ceil", "g_def"]].all(axis=1)
    q["low_owned"] = q.own < LOW_OWN
    return q


def lineup_stats(m, X, ids):
    idx = [m.index[m["DFS ID"] == i][0] for i in ids]
    t = X[idx].sum(0)
    L = m.loc[idx]
    qb = L[L.pos == "QB"].iloc[0]
    mates = L[(L.Team == qb.Team) & (L.pos != "QB") & (L.pos != "DST")]
    bring = L[(L.Team == qb.Opp) & (L.pos != "QB") & (L.pos != "DST")]
    return dict(L=L, salary=int(L.Salary.sum()), proj=float(L.proj.sum()), own_sum=float(L.own.sum()), own_avg=float(L.own.mean()),
                pool=int(L.pool.sum()), stack=len(mates), bring=len(bring), sim_avg=float(t.mean()), sim_p10=float(np.percentile(t, 10)),
                sim_p25=float(np.percentile(t, 25)), sim_p90=float(np.percentile(t, 90)), qb=qb, total=t)
