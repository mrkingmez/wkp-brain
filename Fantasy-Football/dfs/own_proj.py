"""own_proj.py - build OUR DraftKings projection table for one week from our own simulator (no friend file).

python own_proj.py --season 2026 --week 11 --slate SLATE.json --out OUT.csv [--dk-salaries DKSalaries.csv] [--qbs QBS.json]
                   [--sims 20000] [--seed 2026]

What it does
  1. Skill players (QB/RB/WR/TE): DK points draws from D:\\WKP\\data\\ff-simulator\\dfs_draws_<season>_wk<week>.npz
     (written by ff-simulator full_week.py). Percentiles dk_25/50/75/85/95/99, mean, std come straight from those draws.
  2. DST: our simulator has no team-defense scoring, so this script reruns the game simulator (same seed, so the same
     simulated games) and scores each defense on DK rules: sacks 1, INT 2, fumble recovery 2, defensive or return TD 6,
     safety 2, points-allowed tiers 0:+10, 1-6:+7, 7-13:+4, 14-20:+1, 21-27:0, 28-34:-1, 35+:-4. Turnover TDs, return TDs
     and safeties are drawn at league-typical rates (ASSUMPTION: 9 percent of takeaways, 0.04 return TDs, 0.02 safeties a game).
  3. Implied team total and game total from the same market lines the sim used (sim_<season>_wk<week>_env.json).
  4. Status from our merged injury file: Q, D, O (out, IR, reserve, practice squad, cut). p_play is our play chance.
  5. If --dk-salaries is given, every row is matched to a DK ID by name and team (DST by team) and gets Salary and DK ID.
     Unmatched DK players are listed (no projection = not playable). Unmatched sim players are listed too.
  6. --qbs: json {team: {"name":..., "source":..., "date":...}} of starting QBs confirmed from dated sources. Sets qb_confirmed.
Method only, no player data in this file. Output stays in D:\\Draft Kings\\ (outside the repo).
"""
import argparse, json, re, sys, unicodedata
from pathlib import Path
import numpy as np
import pandas as pd

SIM = Path(r"D:\WKP\.claude\skills\ff-simulator\scripts")
OUT = Path(r"D:\WKP\data\ff-simulator")
sys.path.insert(0, str(SIM))
PCTS = [25, 50, 75, 85, 95, 99]
TEAM_FIX = {"LA": "LAR", "JAC": "JAX", "WSH": "WAS", "LV": "LV"}
DST_NAMES = {"ARI": "Cardinals", "ATL": "Falcons", "BAL": "Ravens", "BUF": "Bills", "CAR": "Panthers", "CHI": "Bears",
             "CIN": "Bengals", "CLE": "Browns", "DAL": "Cowboys", "DEN": "Broncos", "DET": "Lions", "GB": "Packers",
             "HOU": "Texans", "IND": "Colts", "JAX": "Jaguars", "KC": "Chiefs", "LAC": "Chargers", "LAR": "Rams",
             "LV": "Raiders", "MIA": "Dolphins", "MIN": "Vikings", "NE": "Patriots", "NO": "Saints", "NYG": "Giants",
             "NYJ": "Jets", "PHI": "Eagles", "PIT": "Steelers", "SEA": "Seahawks", "SF": "49ers", "TB": "Buccaneers",
             "TEN": "Titans", "WAS": "Commanders"}


def norm_name(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[.'\-]", "", s)
    s = re.sub(r"\b(jr|sr|ii|iii|iv|v)\b", "", s)
    return re.sub(r"\s+", " ", s).strip()


def pa_points(pa):
    return np.select([pa <= 0, pa <= 6, pa <= 13, pa <= 20, pa <= 27, pa <= 34], [10, 7, 4, 1, 0, -1], -4)


def dst_draws(season, week, lines, sims, seed, teams):
    import run_week as rw
    tg, lg, pw, defs, lg_def, sched = rw.load_all(season, week)
    drops, quest = rw.injury_sets(season, week)
    boxes = {}
    rw.simulate_week(season, week, dict(lines), tg, lg, pw, defs, lg_def, sched, drops, quest, sims, seed, verbose=False,
                     boxes=boxes, team_now=rw.current_teams(season, week), qb_start=rw.qb_starts(season, week))
    rng = np.random.default_rng([seed, 991])
    out = {}
    for gk, bx in boxes.items():
        G = bx["_game"]
        for d, o in ((G["home"], G["away"]), (G["away"], G["home"])):
            if d not in teams:
                continue
            so = G["sim"][o]
            fum = sum(b["fum"] for pid, b in bx.items() if pid != "_game" and b.get("team") == o and b.get("group") in ("QB", "RB", "WR", "TE"))
            take = so["ints"] + fum
            td = rng.binomial(take.astype(int), 0.09) + rng.poisson(0.04, sims)
            saf = rng.poisson(0.02, sims)
            pa = np.rint(G["pts"][o])
            out[d] = (so["sacks"] + 2 * so["ints"] + 2 * fum + 6 * td + 2 * saf + pa_points(pa)).astype(np.float32)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, required=True); ap.add_argument("--week", type=int, required=True)
    ap.add_argument("--slate", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--dk-salaries"); ap.add_argument("--qbs"); ap.add_argument("--draws", help="override dfs_draws npz path")
    ap.add_argument("--sims", type=int, default=20000); ap.add_argument("--seed", type=int, default=2026)
    a = ap.parse_args()
    slate = json.loads(Path(a.slate).read_text(encoding="utf-8"))
    early = set(slate["early_teams"]) - set(slate.get("excluded_teams", []))
    env = json.load(open(OUT / f"sim_{a.season}_wk{a.week}_env.json"))["envs"]
    lines, imp, opp, gtot = {}, {}, {}, {}
    for k, v in env.items():
        aw, hm = k.split("@")
        sp, tot = float(v["spread_home"]), float(v["total"])
        lines[(aw, hm)] = (sp, tot)
        aw2, hm2 = TEAM_FIX.get(aw, aw), TEAM_FIX.get(hm, hm)
        imp[hm2], imp[aw2] = (tot + sp) / 2, (tot - sp) / 2
        opp[hm2], opp[aw2] = aw2, hm2
        gtot[hm2] = gtot[aw2] = tot
    z = np.load(a.draws or OUT / f"dfs_draws_{a.season}_wk{a.week}.npz")
    rows = []
    for pid, nm, tm, grp, dk in zip(z["ids"], z["names"], z["teams"], z["groups"], z["dk"]):
        tm = TEAM_FIX.get(str(tm), str(tm))
        if grp not in ("QB", "RB", "WR", "TE") or tm not in early:
            continue
        rows.append((str(pid), str(nm), tm, str(grp), dk))
    dd = dst_draws(a.season, a.week, lines, a.sims, a.seed, {t for t in early} | {k for t in early for k, v in TEAM_FIX.items() if v == t})
    for t, arr in dd.items():
        t2 = TEAM_FIX.get(t, t)
        rows.append((f"DST_{t2}", DST_NAMES.get(t2, t2), t2, "DST", arr))
    inj = pd.read_csv(OUT / f"injuries_{a.season}_wk{a.week}.csv").dropna(subset=["gsis_id"]).drop_duplicates("gsis_id", keep="last")
    cat = dict(zip(inj.gsis_id, inj.category)); pp = dict(zip(inj.gsis_id, inj.play_prob)); prac = dict(zip(inj.gsis_id, inj.practice))
    code = {"QUESTIONABLE": "Q", "DOUBTFUL": "D", "OUT": "O", "INJURED_RESERVE": "O", "RESERVE": "O", "PRACTICE_SQUAD": "O", "CUT": "O",
            "SUSPENDED": "O", "PUP": "O", "NFI": "O", "IR": "O"}
    qbs = json.load(open(a.qbs)) if a.qbs and a.qbs != "auto" else {}
    recs = []
    for pid, nm, tm, grp, d in rows:
        d = d.astype(np.float64)
        r = dict(gsis_id=pid, name=nm, team=tm, opp=opp.get(tm), pos=grp, status=code.get(str(cat.get(pid, "")).upper(), ""),
                 p_play=float(pp.get(pid, 1.0)) if pid in pp else 1.0, practice=prac.get(pid, ""),
                 dk_mean=d.mean(), dk_std=d.std(), implied=imp.get(tm), game_total=gtot.get(tm))
        for q in PCTS:
            r[f"dk_{q}_percentile"] = float(np.percentile(d, q))
        r["qb_confirmed"] = bool(grp == "QB" and tm in qbs and norm_name(qbs[tm]["name"]) == norm_name(nm))
        recs.append(r)
    P = pd.DataFrame(recs)
    if a.qbs == "auto":      # dry runs only: the sim's top QB per team with no injury tag counts as confirmed
        top = P[(P.pos == "QB") & (P.status == "")].sort_values("dk_mean", ascending=False).drop_duplicates("team").index
        P["qb_confirmed"] = P.index.isin(top)
    log = [f"own projections: {len(P)} rows ({P.pos.value_counts().to_dict()}) from {Path(a.draws or OUT / f'dfs_draws_{a.season}_wk{a.week}.npz').name} + DST rerun ({a.sims:,} sims, seed {a.seed})"]
    if a.dk_salaries:
        dk = pd.read_csv(a.dk_salaries, encoding="utf-8-sig")
        dk["TeamAbbrev"] = dk.TeamAbbrev.map(lambda t: TEAM_FIX.get(t, t))
        dk["key"] = np.where(dk.Position == "DST", "DST_" + dk.TeamAbbrev, dk.Name.map(norm_name) + "|" + dk.TeamAbbrev)
        P["key"] = np.where(P.pos == "DST", P.gsis_id, P.name.map(norm_name) + "|" + P.team)
        m = P.merge(dk[["key", "ID", "Salary", "Position", "Status"]].rename(columns={"Status": "dk_status"}), on="key", how="left")
        miss_sim = m[m.ID.isna() & (m.dk_mean >= 3)]
        if len(miss_sim):
            log.append(f"sim players with 3+ projected points NOT found in the DK file ({len(miss_sim)}): {miss_sim.name.tolist()}")
        miss_dk = dk[~dk.key.isin(P.key) & (dk.AvgPointsPerGame.fillna(0) >= 5)]
        if len(miss_dk):
            log.append(f"DK players averaging 5+ with NO sim projection, left out ({len(miss_dk)}): {miss_dk.Name.tolist()}")
        bad_pos = m[m.ID.notna() & (m.Position != m.pos)]
        if len(bad_pos):
            log.append(f"position differs sim vs DK (DK wins): {list(zip(bad_pos.name, bad_pos.pos, bad_pos.Position))}")
            m.loc[bad_pos.index, "pos"] = bad_pos.Position
        P = m[m.ID.notna()].copy()
        P["ID"] = P.ID.astype(int); P["Salary"] = P.Salary.astype(int)
        P["value"] = P.dk_mean / (P.Salary / 1000)
        P = P.drop(columns="key")
    P.to_csv(a.out, index=False)
    log.append(f"wrote {a.out}: {len(P)} rows")
    print("\n".join(log))


if __name__ == "__main__":
    main()
