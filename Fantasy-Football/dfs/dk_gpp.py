"""dk_gpp.py - build N (default 7) DraftKings classic GPP lineups for an early-only slate and fill the DK entries template.

Decision support only. Never logs in, never enters, never spends. Zac uploads the filled file himself.
All DK files live in D:\\Draft Kings\\Week N\\ (outside the repo). This script holds method only, no slate data.

python dk_gpp.py --friend FRIEND.csv --template DK_ENTRIES.csv --slate SLATE.json --outdir OUTDIR            (friend mode)
python dk_gpp.py --own OWN_EST.csv --dk-salaries DKSalaries.csv --template ... --slate ... --outdir ...       (own-numbers mode)
   OWN_EST.csv = own_proj.py (our simulator percentiles + DST + DK IDs) then dk_own.py predict (our ownership ESTIMATE).
   Same rules and same lineup logic in both modes; only the source of projections and ownership changes.
   The QB gate's "confirmed starter" uses the dated qbs json given to own_proj.py.
                 [--dk-salaries DKSalaries.csv] [--n 7] [--sims 20000] [--seed 11] [--tries 120]
                 [--out "Name1;Name2"] [--drop-q] [--field 17800] [--name-id]

Inputs
  friend    the friend's projection CSV. Uses only: DFS ID, Name, Pos, Team, Opp, Status, Salary, My Proj, Value, My Own,
            Saber Team, Saber Total, dk_25/50/75/85/95/99_percentile, dk_std. Every other column (FanDuel, Yahoo, ob, extra) is ignored.
  template  DK entries CSV downloaded from the contest (Entry ID, Contest Name, Contest ID, Entry Fee, QB..DST). If it has no
            Entry ID column it is treated as a plain upload file.
  slate     JSON: {"early_teams": [...], "excluded_teams": [...], "source": "..."}. The early list comes from the NFL schedule
            (1:00 PM ET Sunday kickoffs). If --dk-salaries is given, its Game Info times are cross-checked against it.
Method (plain words in the explainer doc)
  1. Keep early-slate, active players (drop O, D, IR; Q kept and flagged unless --drop-q; names in --out dropped).
  2. Correlated simulation: each player's score distribution is the friend's own percentile curve (25/50/75/85/95/99,
     from his 100,000-sim file). Players are tied together with a game factor (shootouts lift both sides), a team passing
     factor (QB with his WR/TE) and a team rushing factor, and each DST moves against the offense it faces.
     The correlation weights are OUR assumption (listed in LOAD below), not the friend's.
  3. Candidate lineups by integer programming under the cap, three tiers:
       core      chalk pool >= 5, QB + 2 pass catchers, ownership sum <= 200
       balanced  chalk pool >= 4, QB + 1 or more, ownership sum <= 160, light ownership penalty
       leverage  chalk pool >= 3, QB must pass the friend's low-owned QB gate, 2+ players under 10 percent, own sum <= 135
     Every lineup: QB salary >= 5,000, max 2 bring-backs, a bring-back is REQUIRED when the game total is at or above the
     slate median, no DST facing any of our offensive players, max 4 offensive players from one team.
  4. Portfolio pick: in each simulated slate a lineup "wins" when it beats the top 1 percent of all candidate lineups.
     A win is worth 1 / (1 + expected duplicates in the field), so chalky lineups that win alongside many copies count less.
     Lineups are picked one at a time to cover the most new winning sims, with caps: a player in at most 4 of 7, a QB in at
     most 2, any two lineups share at most 5 players.
  5. Fill the template rows in order, write a plain upload file too, then run dk_validate.py on what was written.
"""
import argparse, csv, json, math
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.stats import norm as N
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))   # so python -I (isolated mode) still finds dk_validate and dfs_common
from dk_validate import validate, read_rows, lineup_rows, SLOTS, CAP

KEEP = ["DFS ID", "Name", "Pos", "Team", "Opp", "Status", "Salary", "My Proj", "Value", "My Own", "Saber Team", "Saber Total",
        "dk_25_percentile", "dk_50_percentile", "dk_75_percentile", "dk_85_percentile", "dk_95_percentile", "dk_99_percentile", "dk_std"]
PCT = ["dk_25_percentile", "dk_50_percentile", "dk_75_percentile", "dk_85_percentile", "dk_95_percentile", "dk_99_percentile"]
U = np.array([0.0005, 0.25, 0.50, 0.75, 0.85, 0.95, 0.99, 0.9995])
# factor loadings (ASSUMPTION, ours): game G, own-team pass P, own-team rush R; DST loads on the OPPONENT's P and R
LOAD = {"QB": (0.40, 0.75, 0.10), "WR": (0.30, 0.35, 0.0), "TE": (0.25, 0.30, 0.0), "RB": (0.25, 0.10, 0.55), "DST": (-0.30, -0.40, -0.20)}
LOW_OWN = 10.0      # friend's "low owned" for skill players (percent)
QB_LOW_OWN = 15.0   # low-owned QB (percent), carried over from the Week 10 build
DUPE_FACTOR = 12.0  # ASSUMPTION: rough positional-ordering factor in the duplicate estimate
# 2026-11-19: min_pool is 5 in EVERY tier. The friend's part 1 says "Every lineup needs at least 5 players from that pool";
# the first build had 4 (balanced) and 3 (leverage), which broke his rule. Leverage now comes only from ownership caps,
# the low-owned QB gate and the under-10-percent minimum, as he describes.
TIERS = {
    "core":     dict(min_pool=5, own_cap=200, lam=0.000, stack=2, gate=False, low=0, min_sal=48500, ceil_w=(0.3, 0.6)),
    "balanced": dict(min_pool=5, own_cap=160, lam=0.020, stack=1, gate=False, low=1, min_sal=48500, ceil_w=(0.4, 0.8)),
    "leverage": dict(min_pool=5, own_cap=135, lam=0.050, stack=2, gate=True, low=2, min_sal=47500, ceil_w=(0.6, 1.0)),
}
PLAN7 = ["core", "core", "balanced", "balanced", "leverage", "leverage", "leverage"]


def load_friend(path, slate, drop_q, out_names, log):
    raw = pd.read_csv(path)
    ignored = [c for c in raw.columns if c not in KEEP + ["Actual", "SS Proj", "Live Proj", "Adj Own", "Min Exp", "Max Exp", "dk_points"]]
    log.append(f"friend file: {Path(path).name}, {len(raw)} rows, {len(ignored)} extra columns ignored (FanDuel/Yahoo/ob/other)")
    p = raw[[c for c in KEEP if c in raw.columns]].copy()
    p["pos"] = p.Pos.str.split("/").str[0]
    p["Status"] = p.Status.fillna("").astype(str).str.upper()
    early, excl = set(slate["early_teams"]), set(slate.get("excluded_teams", []))
    not_early = p[~p.Team.isin(early) | p.Team.isin(excl)]
    if len(not_early):
        log.append(f"dropped {len(not_early)} rows from teams not on the early slate or in excluded games: {sorted(not_early.Team.unique())}")
    p = p[p.Team.isin(early) & ~p.Team.isin(excl)]
    missing_teams = early - set(p.Team)
    if missing_teams:
        log.append(f"WARNING: early-slate teams with no rows in the friend file: {sorted(missing_teams)}")
    bad = p.Status.isin(["O", "OUT", "D", "IR"])
    log.append(f"dropped {int(bad.sum())} players marked O/D/IR in the friend file")
    p = p[~bad]
    if out_names:
        hit = p.Name.isin(out_names)
        log.append(f"dropped by --out: {p[hit].Name.tolist()} | names not found: {sorted(set(out_names) - set(p[hit].Name))}")
        p = p[~hit]
    if drop_q:
        log.append(f"dropped Q (--drop-q): {p[p.Status == 'Q'].Name.tolist()}")
        p = p[p.Status != "Q"]
    # playable: DST always; QB projected starter; skill players with a real projection
    p = p[(p.pos == "DST") | ((p.pos == "QB") & (p["My Proj"] >= 10)) | (p.pos.isin(["RB", "WR", "TE"]) & (p["My Proj"] >= 3))]
    p = p.rename(columns={"My Proj": "proj", "My Own": "own", "Saber Team": "imp", "Saber Total": "total"}).reset_index(drop=True)
    p["own"] = p.own.fillna(0.0)
    log.append(f"playable pool: {len(p)} players ({p.pos.value_counts().to_dict()}), Q flagged: {p[p.Status == 'Q'].Name.tolist()}")
    return p


def load_own(path, slate, drop_q, out_names, log):
    """OWN-NUMBERS mode (2026-11-19): our simulator's projections + our ownership ESTIMATE, no friend file.
    Input is the csv written by own_proj.py (with --dk-salaries) then dk_own.py predict."""
    raw = pd.read_csv(path)
    need = ["ID", "name", "pos", "team", "opp", "status", "Salary", "dk_mean", "own_est", "implied", "game_total", "dk_std", "qb_confirmed"] + PCT
    miss = [c for c in need if c not in raw.columns]
    if miss:
        raise SystemExit(f"own projection file is missing columns {miss}: build it with own_proj.py --dk-salaries, then dk_own.py predict")
    p = raw[need].rename(columns={"ID": "DFS ID", "name": "Name", "team": "Team", "opp": "Opp", "status": "Status", "dk_mean": "proj",
                                  "own_est": "own", "implied": "imp", "game_total": "total"})
    p["Status"] = p.Status.fillna("").astype(str).str.upper()
    p["Pos"] = p.pos
    log.append(f"OWN-NUMBERS MODE: {Path(path).name}, {len(p)} rows. Projections = our simulator; ownership = our ESTIMATE (dk_own.py); no friend numbers used")
    early, excl = set(slate["early_teams"]), set(slate.get("excluded_teams", []))
    p = p[p.Team.isin(early) & ~p.Team.isin(excl)]
    if early - set(p.Team):
        log.append(f"WARNING: early-slate teams with no rows: {sorted(early - set(p.Team))}")
    bad = p.Status.isin(["O", "OUT", "D", "IR"])
    log.append(f"dropped {int(bad.sum())} players marked O/D in our injury file: {p[bad].Name.tolist()}")
    p = p[~bad]
    if out_names:
        hit = p.Name.isin(out_names)
        log.append(f"dropped by --out: {p[hit].Name.tolist()} | names not found: {sorted(set(out_names) - set(p[hit].Name))}")
        p = p[~hit]
    if drop_q:
        log.append(f"dropped Q (--drop-q): {p[p.Status == 'Q'].Name.tolist()}")
        p = p[p.Status != "Q"]
    p = p[(p.pos == "DST") | ((p.pos == "QB") & (p.proj >= 10)) | (p.pos.isin(["RB", "WR", "TE"]) & (p.proj >= 3))].reset_index(drop=True)
    p["own"] = p.own.fillna(0.0)
    log.append(f"playable pool: {len(p)} players ({p.pos.value_counts().to_dict()}), Q flagged: {p[p.Status == 'Q'].Name.tolist()}")
    log.append(f"confirmed starting QBs (dated sources, qbs json): {sorted(p[(p.pos == 'QB') & p.qb_confirmed].Name)}")
    return p


def write_reference(p, path):
    """Pool in the friend-file column layout so dk_validate can check IDs, slots, teams, statuses and salary."""
    p[["DFS ID", "Name", "Pos", "Team", "Status", "Salary"]].to_csv(path, index=False)
    return str(path)


def check_dk_salaries(path, p, slate, log):
    dk = pd.read_csv(path, encoding="utf-8-sig")
    times = dk["Game Info"].str.extract(r"(\d{1,2}:\d{2}[AP]M) ET")[0]
    late = dk[times != "01:00PM"]
    log.append(f"DK salary file: {len(dk)} players, kickoff times {sorted(times.dropna().unique())}")
    if len(late):
        log.append(f"WARNING: DK salary file has non-1PM games: {sorted(late['Game Info'].str.split(' ').str[0].unique())}")
    dk_teams = set(dk.TeamAbbrev)
    if dk_teams != set(slate["early_teams"]):
        log.append(f"WARNING: DK salary-file teams differ from the slate list. DK only: {sorted(dk_teams - set(slate['early_teams']))}, list only: {sorted(set(slate['early_teams']) - dk_teams)}")
    miss = p[~p["DFS ID"].isin(dk.ID)]
    if len(miss):
        log.append(f"WARNING: {len(miss)} pool players not in the DK salary file, removed: {miss.Name.tolist()}")
    dkst = dk.set_index("ID").Status.fillna("").astype(str).str.upper()
    out = p["DFS ID"].map(dkst).isin(["O", "OUT", "D", "IR"])
    if out.any():
        log.append(f"DK salary file marks OUT/D/IR, removed: {p[out].Name.tolist()}")
    sal_diff = p[p["DFS ID"].isin(dk.ID) & (p.Salary != p["DFS ID"].map(dk.set_index("ID").Salary))]
    if len(sal_diff):
        log.append(f"WARNING: salary differs between friend file and DK for {sal_diff.Name.tolist()} (DK wins)")
        p.loc[sal_diff.index, "Salary"] = sal_diff["DFS ID"].map(dk.set_index("ID").Salary)
    return p[p["DFS ID"].isin(dk.ID) & ~out].reset_index(drop=True)


def quantile_curve(r):
    q = r[PCT].values.astype(float)
    if np.isnan(q).any():
        mu, sd = r.proj, max(2.0, 0.5 * r.proj)
        return mu + sd * N.ppf(U)
    lo = max(-4.0 if r.pos == "DST" else -1.0, q[0] - 1.5 * (q[1] - q[0]))
    hi = q[-1] + 0.6 * (q[-1] - q[-2])
    v = np.concatenate([[lo], q, [hi]])
    return np.maximum.accumulate(v)


def simulate(p, sims, seed):
    rng = np.random.default_rng(seed)
    games = sorted({tuple(sorted((a, b))) for a, b in zip(p.Team, p.Opp)})
    gi = {g: i for i, g in enumerate(games)}
    teams = sorted(set(p.Team) | set(p.Opp)); ti = {t: i for i, t in enumerate(teams)}
    G = rng.standard_normal((len(games), sims)).astype(np.float32)
    P = rng.standard_normal((len(teams), sims)).astype(np.float32)
    R = rng.standard_normal((len(teams), sims)).astype(np.float32)
    X = np.empty((len(p), sims), dtype=np.float32)
    for i, r in p.iterrows():
        a, b, c = LOAD[r.pos]
        g = G[gi[tuple(sorted((r.Team, r.Opp)))]]
        t = ti[r.Opp] if r.pos == "DST" else ti[r.Team]
        z = a * g + b * P[t] + c * R[t] + math.sqrt(max(0.0, 1 - a * a - b * b - c * c)) * rng.standard_normal(sims).astype(np.float32)
        X[i] = np.interp(N.cdf(z), U, quantile_curve(r))
    return X


def defense_rank(log):
    """Optional: DK points allowed to QBs by defense, from local nflverse stats (dfs_common). Rank 1 = toughest."""
    try:
        from dfs_common import defense_vs_qb, STATS
        d = pd.read_parquet(STATS)
        wk = int(d[d.season_type == "REG"].week.max())
        log.append(f"defense vs QB ranks: local nflverse 2026 stats through week {wk} (refresh before Sunday if stale)")
        return defense_vs_qb(wk).def_rank.to_dict()
    except Exception as e:  # stats file missing or unreadable
        log.append(f"defense vs QB ranks NOT available ({e.__class__.__name__}); the defense part of the QB gate is skipped")
        return {}


def chalk_pool(p):
    pool = set()
    for pos in ("RB", "WR", "TE"):
        d = p[p.pos == pos]
        pool |= set(d.nlargest(6, "own").index) | set(d.nlargest(6, "proj").index)
    return np.array([i in pool for i in p.index])


def qb_gate(p, drank):
    q = p.pos == "QB"
    ceil_rank = p[q]["dk_95_percentile"].rank(ascending=False)
    g = pd.DataFrame(index=p[q].index)
    g["salary"] = p.Salary[q] >= 5000
    g["starter"] = (p.Status[q] != "Q") & (p.proj[q] >= 10)
    if "qb_confirmed" in p:          # own-numbers mode: confirmed starter = named in the dated qbs json
        g["starter"] = g["starter"] & p.qb_confirmed[q].astype(bool)
    g["implied21"] = p.imp[q] >= 21
    g["ceil_top12"] = ceil_rank <= 12
    g["def_outside8"] = p.Opp[q].map(lambda t: drank.get(t, 99) > 8) if drank else True
    g["pass"] = g.all(axis=1)
    return g


def solve(p, score, tier, pool, gate, bb_thr, ban=None, overlap=()):
    """ban: players that may not be used (exposure caps already hit). overlap: lineups already picked; the new one may
    share at most 5 players with each (added 2026-11-19 so the portfolio caps are met by solving, not by luck)."""
    n = len(p); pos = p.pos.values; team = p.Team.values; opp = p.Opp.values; own = p.own.values
    skill = np.isin(pos, ["RB", "WR", "TE"]); off = pos != "DST"
    A, lo, hi = [], [], []
    add = lambda row, l, h: (A.append(row), lo.append(l), hi.append(h))
    for k in overlap:
        row = np.zeros(n); row[list(k)] = 1; add(row, 0, 5)
    add(p.Salary.values.astype(float), tier["min_sal"], CAP)
    for ps, l, h in (("QB", 1, 1), ("RB", 2, 3), ("WR", 3, 4), ("TE", 1, 2), ("DST", 1, 1)):
        add((pos == ps).astype(float), l, h)
    add(skill.astype(float), 7, 7)
    add((pool & skill).astype(float), tier["min_pool"], 9)
    add(own, 0, tier["own_cap"])
    if tier["low"]:
        add(((own < LOW_OWN) & off & (pos != "QB")).astype(float), tier["low"], 9)
    for t in np.unique(team):
        add(((team == t) & off).astype(float), 0, 4)
    for q in np.where(pos == "QB")[0]:
        mates = ((team == team[q]) & np.isin(pos, ["WR", "TE"])).astype(float); mates[q] = -tier["stack"]
        add(mates, 0, np.inf)
        back = ((team == opp[q]) & skill).astype(float)
        cap = back.copy(); cap[q] = 5; add(cap, 0, 7)                      # at most 2 bring-backs
        if p.total.values[q] >= bb_thr:
            need = back.copy(); need[q] = -1; add(need, 0, np.inf)       # bring-back required in a high-total game
    for d in np.where(pos == "DST")[0]:
        row = ((team == opp[d]) & off).astype(float); row[d] = 9; add(row, 0, 9)   # no DST facing our own players
    ub = np.ones(n)
    ub[(pos == "QB") & (p.Salary.values < 5000)] = 0
    ub[(pos == "QB") & (own < QB_LOW_OWN) & ~gate] = 0                # friend's rule, every tier: a low-owned QB must pass the gate
    if tier["gate"]:
        ub[(pos == "QB") & ~(gate & (own < QB_LOW_OWN))] = 0
    if ban is not None:
        ub[ban] = 0
    res = milp(-score, constraints=LinearConstraint(np.array(A), lo, hi), integrality=np.ones(n), bounds=Bounds(np.zeros(n), ub))
    return tuple(np.where(res.x > 0.5)[0]) if res.success else None


def order_slots(p, idx):
    L = p.loc[list(idx)]
    qb = L[L.pos == "QB"].index[0]; dst = L[L.pos == "DST"].index[0]
    rb = L[L.pos == "RB"].sort_values("Salary", ascending=False).index.tolist()
    wr = L[L.pos == "WR"].sort_values("Salary", ascending=False).index.tolist()
    te = L[L.pos == "TE"].sort_values("Salary", ascending=False).index.tolist()
    flex = (rb[2:] + wr[3:] + te[1:])
    assert len(flex) == 1, "lineup does not have exactly one FLEX"
    return [qb, rb[0], rb[1], wr[0], wr[1], wr[2], te[0], flex[0], dst]


def describe(p, idx):
    L = p.loc[list(idx)]; q = L[L.pos == "QB"].iloc[0]
    mates = L[(L.Team == q.Team) & L.pos.isin(["WR", "TE", "RB"])]
    back = L[(L.Team == q.Opp) & L.pos.isin(["WR", "TE", "RB"])]
    return f"{q.Name} + {len(mates)} ({', '.join(mates.Name)})" + (f" | bring-back {len(back)} ({', '.join(back.Name)})" if len(back) else " | no bring-back")


def main():
    ap = argparse.ArgumentParser()
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--friend", help="friend's projection CSV (friend mode)")
    src.add_argument("--own", help="OWN-NUMBERS mode: csv from own_proj.py --dk-salaries + dk_own.py predict (needs --dk-salaries)")
    ap.add_argument("--template", required=True); ap.add_argument("--slate", required=True)
    ap.add_argument("--outdir", required=True); ap.add_argument("--dk-salaries")
    ap.add_argument("--n", type=int, default=7); ap.add_argument("--sims", type=int, default=20000); ap.add_argument("--seed", type=int, default=11)
    ap.add_argument("--tries", type=int, default=120, help="randomized solves per tier")
    ap.add_argument("--out", default="", help="names to remove, separated by ;  (Sunday inactives)")
    ap.add_argument("--drop-q", action="store_true"); ap.add_argument("--field", type=int, default=17800, help="contest size for the duplicate estimate")
    ap.add_argument("--name-id", action="store_true", help="write 'Name (ID)' instead of the bare ID")
    a = ap.parse_args()
    out = Path(a.outdir); out.mkdir(parents=True, exist_ok=True)
    log = []
    slate = json.loads(Path(a.slate).read_text(encoding="utf-8"))
    log.append(f"slate: {slate.get('label', '')} early teams {sorted(slate['early_teams'])}, excluded {slate.get('excluded_teams', [])}; source: {slate.get('source', 'not stated')}")
    outs = [s.strip() for s in a.out.split(";") if s.strip()]
    if a.own:
        if not a.dk_salaries:
            raise SystemExit("--own needs --dk-salaries (DK IDs, salaries and kickoff times come from DK's own file)")
        p = load_own(a.own, slate, a.drop_q, outs, log)
    else:
        p = load_friend(a.friend, slate, a.drop_q, outs, log)
    if a.dk_salaries:
        p = check_dk_salaries(a.dk_salaries, p, slate, log)
    ref = write_reference(p, out / "reference_pool.csv") if a.own else a.friend
    X = simulate(p, a.sims, a.seed)
    log.append(f"simulation: {a.sims:,} correlated slates, seed {a.seed}, marginals from "
               + ("OUR simulator's dk percentiles (ff-simulator 20,000 sims)" if a.own else "the friend's dk percentiles") + ", numpy/scipy on this PC")
    drank = defense_rank(log)
    gate = np.zeros(len(p), bool)
    gt = qb_gate(p, drank); gate[gt.index] = gt["pass"].values
    pool = chalk_pool(p)
    # 2026-11-19: the slate middle (median game total), as the rule says. The first build also had a 44-point floor (ours, not his).
    bb_thr = float(np.median(p.drop_duplicates("Team").total))
    log.append(f"chalk pool: {int(pool.sum())} players | bring-back required when game total >= {bb_thr:.1f}")
    log.append("QB gate (salary>=5000, projected starter not Q, implied>=21, top-12 ceiling by dk_95, opp defense outside top 8):")
    for i, r in gt.iterrows():
        log.append(f"   {p.Name[i]:<22} {p.Team[i]:3} own {p.own[i]:5.1f}% implied {p.imp[i]:4.1f} -> {'PASS' if r['pass'] else 'fail: ' + ', '.join(c for c in gt.columns[:-1] if not r[c])}")
    rng = np.random.default_rng(a.seed)
    mean = X.mean(1); proj = p.proj.values; own = p.own.values
    p85 = p.dk_85_percentile.fillna(p.proj * 1.4).values; p95 = p.dk_95_percentile.fillna(p.proj * 1.8).values
    cands = {}
    for name, tier in TIERS.items():
        found = 0
        for _ in range(a.tries):
            w = rng.uniform(*tier["ceil_w"])
            draw = X[:, rng.integers(0, X.shape[1], 4)].mean(1)
            score = (1 - w) * (0.5 * proj + 0.5 * mean) + w * (0.5 * p85 + 0.5 * p95) * 0.75 + 0.25 * draw - tier["lam"] * own * 3
            lu = solve(p, score, tier, pool, gate, bb_thr)
            if lu and lu not in cands:
                cands[lu] = name; found += 1
        log.append(f"candidates {name}: {found} unique legal lineups from {a.tries} solves")
    keys = list(cands)
    if not keys:
        raise SystemExit("no legal lineups: check the slate and filters")
    S = np.stack([X[list(k)].sum(0) for k in keys])                 # candidates x sims
    cut = np.percentile(S, 99, axis=0)
    dupes = np.array([a.field * DUPE_FACTOR * float(np.prod(np.clip(own[list(k)], 0.05, 100) / 100)) for k in keys])
    V = (S >= cut) / (1 + dupes)[:, None]
    plan = (PLAN7 if a.n == 7 else (PLAN7 * 3)[:a.n])
    chosen, best = [], np.zeros(S.shape[1])
    expo, qbcount = {}, {}
    def fits(k):
        qb = [i for i in k if p.pos[i] == "QB"][0]
        return (qbcount.get(qb, 0) < 2 and all(expo.get(i, 0) < 4 for i in k)
                and all(len(set(k) & set(keys[c])) <= 5 for c in chosen))

    def best_of(tiers):
        pick, gain = None, -1
        for j, k in enumerate(keys):
            if j in chosen or cands[k] not in tiers or not fits(k):
                continue
            g = np.maximum(best, V[j]).sum() - best.sum() + 1e-6 * S[j].mean()
            if g > gain:
                pick, gain = j, g
        return pick

    for slot_tier in plan:
        pick = best_of({slot_tier})
        # 2026-11-19 fix: when no stored lineup meets the caps, solve fresh ones with the caps written in as constraints,
        # first in this slot's tier, then in the other tiers. The first build relaxed to "any tier" and dropped the
        # exposure caps too, which let one player into 7 of 7 lineups. The caps are never relaxed now.
        order = [slot_tier] + [t for t in ("balanced", "core", "leverage") if t != slot_tier]
        for tname in order:
            if pick is not None:
                break
            if tname != slot_tier:
                pick = best_of({tname})
                if pick is not None:
                    log.append(f"NOTE: {slot_tier} slot filled with a stored {tname} lineup, caps met")
                    break
            ban = np.zeros(len(p), bool)
            ban[[i for i, c in expo.items() if c >= 4]] = True
            ban[[q for q, c in qbcount.items() if c >= 2]] = True
            tier = TIERS[tname]; added = 0
            for _ in range(max(20, a.tries // 4)):
                w = rng.uniform(*tier["ceil_w"])
                draw = X[:, rng.integers(0, X.shape[1], 4)].mean(1)
                score = (1 - w) * (0.5 * proj + 0.5 * mean) + w * (0.5 * p85 + 0.5 * p95) * 0.75 + 0.25 * draw - tier["lam"] * own * 3
                lu = solve(p, score, tier, pool, gate, bb_thr, ban=ban, overlap=[keys[c] for c in chosen])
                if lu and lu not in cands:
                    cands[lu] = tname; keys.append(lu); added += 1
                    s_new = X[list(lu)].sum(0)
                    d_new = a.field * DUPE_FACTOR * float(np.prod(np.clip(own[list(lu)], 0.05, 100) / 100))
                    S = np.vstack([S, s_new]); dupes = np.append(dupes, d_new); V = np.vstack([V, (s_new >= cut) / (1 + d_new)])
            pick = best_of({tname})
            log.append(f"NOTE: {slot_tier} slot: solved {added} new {tname} lineups with the caps as constraints"
                       + (", one picked" if pick is not None else ", none legal"))
        if pick is None:
            elig = sorted(p.Name[i] for i in np.where(p.pos.values == "QB")[0]
                          if p.Salary[i] >= 5000 and (p.own[i] >= QB_LOW_OWN or gate[i]))
            msg = (f"STOPPED: could not fill lineup {len(chosen) + 1} ({slot_tier}) in any tier without breaking the caps "
                   f"(player 4 of 7, QB 2, overlap 5). Lineups built: {len(chosen)}. QBs allowed by the QB rules: {elig}. "
                   "With a QB cap of 2, 7 lineups need at least 4 allowed QBs.")
            log.append(msg)
            (out / "build_report.txt").write_text("\n".join(["DK GPP BUILD FAILED (nothing written for upload)"] + log), encoding="utf-8")
            raise SystemExit(msg)
        chosen.append(pick); best = np.maximum(best, V[pick])
        for i in keys[pick]:
            expo[i] = expo.get(i, 0) + 1
        qb = [i for i in keys[pick] if p.pos[i] == "QB"][0]; qbcount[qb] = qbcount.get(qb, 0) + 1
    # ---------- outputs ----------
    detail, lines = [], []
    for n, j in enumerate(chosen, start=1):
        k = keys[j]; slots = order_slots(p, k); t = S[j]
        sal = int(p.Salary[list(k)].sum())
        lines.append(f"\nLINEUP {n}  [{cands[k]}]  salary {sal:,} | proj {proj[list(k)].sum():.1f} | own sum {own[list(k)].sum():.0f}% | "
                     f"sim mean {t.mean():.1f} p90 {np.percentile(t, 90):.1f} p99 {np.percentile(t, 99):.1f} | top-1% rate {(t >= cut).mean() * 100:.2f}% | est. dupes {dupes[j]:.2f}")
        lines.append(f"   stack: {describe(p, k)}")
        for s, i in zip(SLOTS, slots):
            r = p.loc[i]
            flag = " Q" if r.Status == "Q" else ""
            lines.append(f"   {s:4} {r.Name:<24} {r.Team:3} v {r.Opp:3} ${int(r.Salary):>5,} proj {r.proj:5.1f} own {r.own:5.1f}%{' POOL' if pool[i] else ''}{flag}")
            detail.append(dict(lineup=n, tier=cands[k], slot=s, name=r.Name, dfs_id=int(r["DFS ID"]), team=r.Team, opp=r.Opp, salary=int(r.Salary),
                               proj=round(r.proj, 2), own=round(r.own, 2), pool=bool(pool[i]), status=r.Status))
    port = np.maximum.reduce([S[j] >= cut for j in chosen])
    lines.append(f"\nPORTFOLIO: at least one of the {len(chosen)} lineups beats the top-1% cutoff in {port.mean() * 100:.1f}% of {a.sims:,} sims")
    ex = pd.DataFrame(detail).groupby(["name", "team"]).size().sort_values(ascending=False)
    lines.append("EXPOSURE (lineups out of %d):" % len(chosen))
    lines += [f"   {nm:<24} {tm:3} {c}" for (nm, tm), c in ex.items()]
    pd.DataFrame(detail).to_csv(out / "lineups_detail.csv", index=False)
    # fill template
    rows = read_rows(a.template)
    hdr, entries = lineup_rows(rows)
    q0 = hdr.index("QB")
    cell = lambda i: f"{p.Name[i]} ({int(p['DFS ID'][i])})" if a.name_id else str(int(p["DFS ID"][i]))
    ordered = [order_slots(p, keys[j]) for j in chosen]
    filled_n = min(len(entries), len(ordered))
    for (ri, *_), slots in zip(entries, ordered):
        row = rows[ri] + [""] * max(0, q0 + 9 - len(rows[ri]))
        row[q0:q0 + 9] = [cell(i) for i in slots]
        rows[ri] = row
    stem = Path(a.template).stem
    filled = out / f"{stem} - FILLED.csv"
    with open(filled, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)
    with open(out / "upload_new_lineups.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(SLOTS); w.writerows([[cell(i) for i in s] for s in ordered])
    log.append(f"template: {len(entries)} entry rows; filled {filled_n}; lineups built {len(ordered)}")
    if len(entries) < len(ordered):
        log.append(f"WARNING: template has only {len(entries)} entries. Lineups {len(entries) + 1}-{len(ordered)} are in upload_new_lineups.csv only.")
    if len(entries) > len(ordered):
        log.append(f"WARNING: template has {len(entries)} entries, only {len(ordered)} lineups built. Extra rows left as downloaded.")
    ok1, rep1 = validate(filled, ref, a.slate, a.dk_salaries, quiet=True)
    ok2, rep2 = validate(out / "upload_new_lineups.csv", ref, a.slate, a.dk_salaries, template=a.template, quiet=True)
    head = ["DK GPP BUILD (decision support only, nothing entered)"]
    if a.own:
        head.append("OWN-NUMBERS MODE: every 'own' percent below is OUR ESTIMATE of field ownership (dk_own.py), not a measured number")
    report = head + log + lines + [""] + rep1 + [""] + rep2
    (out / "build_report.txt").write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report))
    raise SystemExit(0 if ok1 and ok2 else 1)


if __name__ == "__main__":
    main()
