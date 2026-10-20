"""Simulate one NFL week end to end.

python run_week.py 2026 6 [--sims 4000] [--odds D:\\WKP\\scratch\\wk6_odds.json]

Reads: nflverse pbp / stats_player / schedules (cache), The Odds API pull (json),
       MFL injuries, Zac's roster bridge.
Writes: D:\\WKP\\data\\ff-simulator\\sim_<season>_wk<week>.npz (draws) and
        sim_<season>_wk<week>_summary.csv (mean, sd, p10, p50, p90 per player).
"""
import argparse
import json
import statistics as st
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import coach_model as cm
import simulate as sm

NAME2ABBR = {
    "Arizona Cardinals": "ARI", "Atlanta Falcons": "ATL", "Baltimore Ravens": "BAL", "Buffalo Bills": "BUF",
    "Carolina Panthers": "CAR", "Chicago Bears": "CHI", "Cincinnati Bengals": "CIN", "Cleveland Browns": "CLE",
    "Dallas Cowboys": "DAL", "Denver Broncos": "DEN", "Detroit Lions": "DET", "Green Bay Packers": "GB",
    "Houston Texans": "HOU", "Indianapolis Colts": "IND", "Jacksonville Jaguars": "JAX", "Kansas City Chiefs": "KC",
    "Las Vegas Raiders": "LV", "Los Angeles Chargers": "LAC", "Los Angeles Rams": "LA", "Miami Dolphins": "MIA",
    "Minnesota Vikings": "MIN", "New England Patriots": "NE", "New Orleans Saints": "NO", "New York Giants": "NYG",
    "New York Jets": "NYJ", "Philadelphia Eagles": "PHI", "Pittsburgh Steelers": "PIT", "San Francisco 49ers": "SF",
    "Seattle Seahawks": "SEA", "Tampa Bay Buccaneers": "TB", "Tennessee Titans": "TEN", "Washington Commanders": "WAS",
}
OUT = Path(r"D:\WKP\data\ff-simulator")
DATA_PLAYERS = Path(r"D:\WKP\data\nfl\players\players.parquet")
QUESTIONABLE_PLAY_RATE = 0.75
OFFENSE_WIDEN = 1.3


def market_lines(odds_path: str) -> dict:
    """{(away, home): (home_favored_by, total)} using the median across books."""
    d = json.load(open(odds_path))["americanfootball_nfl"]
    out = {}
    for g in d:
        a, h = NAME2ABBR[g["away_team"]], NAME2ABBR[g["home_team"]]
        sp, tot = [], []
        for b in g["bookmakers"]:
            for m in b["markets"]:
                if m["key"] == "spreads":
                    for o in m["outcomes"]:
                        if o["name"] == g["home_team"]:
                            sp.append(-o["point"])
                elif m["key"] == "totals":
                    for o in m["outcomes"]:
                        if o["name"] == "Over":
                            tot.append(o["point"])
        if sp and tot:
            out[(a, h)] = (st.median(sp), st.median(tot))
    return out


def injury_sets():
    """Out / IR / Doubtful / Suspended players (dropped) and Questionable players, as gsis ids."""
    sys.path.insert(0, r"D:\WKP\Fantasy-Football\dashboard")
    import mfl_client as m
    cache = json.load(open(r"D:\WKP\.claude\skills\fantasy-football-data\players-cache-details.json"))
    plist = cache["players"]["player"] if "players" in cache else cache
    espn = {p["id"]: p.get("espn_id") for p in plist}
    npl = pd.read_parquet(DATA_PLAYERS)[["gsis_id", "espn_id"]].dropna()
    npl["espn_id"] = npl.espn_id.astype(str).str.replace(r"\.0$", "", regex=True)
    e2g = dict(zip(npl.espn_id, npl.gsis_id))
    drop, quest = set(), set()
    for i in m.injuries().get("injuries", {}).get("injury", []):
        e = espn.get(i["id"])
        g = e2g.get(str(e)) if e else None
        status = (i.get("status") or "").lower()
        if not g:
            continue
        if status in ("out", "doubtful", "suspended", "holdout", "retired") or status.startswith("ir"):
            drop.add(g)
        elif "question" in status:
            quest.add(g)
    return drop, quest


def simulate_week(season, week, lines, tg, lg, pw, defs, lg_def, sched, drops=frozenset(), quest=frozenset(),
                  sims=4000, seed=2026, verbose=True, apply_quest_zero=True, boxes=None):
    as_of = season * 100 + week
    rng = np.random.default_rng(seed)
    wk = sched[(sched.season == season) & (sched.week == week)]
    latest = pw.sort_values("order").groupby("player_id").team.last().to_dict()
    results, envs, dropped = {}, {}, []
    for _, g in wk.iterrows():
        away, home = g.away_team, g.home_team
        if (away, home) not in lines:
            if pd.isna(g.spread_line) or pd.isna(g.total_line):
                if verbose:
                    print("  SKIPPED (no line):", away, home)
                continue
            lines[(away, home)] = (float(g.spread_line), float(g.total_line))
        sp, tot = lines[(away, home)]
        tm = {}
        for team in (away, home):
            coach = g.away_coach if team == away else g.home_coach
            t = cm.tendencies(tg, coach, team, as_of, lg)
            tm[team] = sm.TeamModel(team, pw, tg, t, as_of, latest)
            tm[team].avail = {i: QUESTIONABLE_PLAY_RATE for i in quest}
            names = {i: v["name"] for i, v in tm[team].players.items()}
            dropped += [(team, names[i]) for i in tm[team].drop(drops)]
        bx = {} if boxes is not None else None
        res, env = sm.simulate_game(tm[home], tm[away], sp, tot, defs, lg_def, rng, sims, box=bx)
        if boxes is not None:
            boxes[f"{away}@{home}"] = bx
        results.update(res)
        envs[f"{away}@{home}"] = dict(spread_home=sp, total=tot, **env)
        if verbose:
            print(f"{away:>3} @ {home:<3}  spread(home fav) {sp:+.1f}  total {tot:.1f}  "
                  f"sim pts {env['_pts'][away]:.1f}-{env['_pts'][home]:.1f}")
    ids = list(results)
    M = np.stack([results[i][3] for i in ids]).astype(np.float32)
    # Calibration from the 18-week backtest: offensive outcomes came out too tight (about 2/3 of
    # actual scores fell inside the simulated 10th-90th range instead of 80%). Widen them around
    # their own mean; the average is untouched.
    wide = np.array([results[i][2] in ("QB", "RB", "WR", "TE") for i in ids])
    mu = M[wide].mean(axis=1, keepdims=True)
    M[wide] = np.maximum(mu + OFFENSE_WIDEN * (M[wide] - mu), -4.0)
    if apply_quest_zero:
        for n, i in enumerate(ids):
            if i in quest and results[i][2] != "QB":     # QBs handled inside the game (backup steps in)
                M[n] *= (rng.random(M.shape[1]) < QUESTIONABLE_PLAY_RATE)
    return ids, results, M, envs, dropped


def summarize(ids, results, M, quest=frozenset()):
    return pd.DataFrame({
        "gsis_id": ids, "name": [results[i][0] for i in ids], "team": [results[i][1] for i in ids],
        "group": [results[i][2] for i in ids], "mean": M.mean(1), "sd": M.std(1),
        "p10": np.percentile(M, 10, axis=1), "p50": np.percentile(M, 50, axis=1), "p90": np.percentile(M, 90, axis=1),
        "questionable": [i in quest for i in ids]}).sort_values("mean", ascending=False)


def load_all(season, week):
    as_of = season * 100 + week
    p, tg = cm.build_tables()
    lg = cm.league_means(tg[tg.order < as_of])
    pw = sm.load_player_weeks()
    defs, lg_def = sm.defense_table(as_of)
    sched = pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet")
    return tg, lg, pw, defs, lg_def, sched


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("season", type=int)
    ap.add_argument("week", type=int)
    ap.add_argument("--sims", type=int, default=4000)
    ap.add_argument("--odds", default=r"D:\WKP\scratch\wk6_odds.json")
    ap.add_argument("--seed", type=int, default=2026)
    a = ap.parse_args()
    tg, lg, pw, defs, lg_def, sched = load_all(a.season, a.week)
    lines = market_lines(a.odds)
    drops, quest = injury_sets()
    print(f"{len(drops)} out/doubtful/IR flagged, {len(quest)} questionable")
    ids, results, M, envs, dropped = simulate_week(a.season, a.week, lines, tg, lg, pw, defs, lg_def, sched,
                                                   drops, quest, a.sims, a.seed)
    OUT.mkdir(parents=True, exist_ok=True)
    base = OUT / f"sim_{a.season}_wk{a.week}"
    np.savez_compressed(str(base) + ".npz", ids=np.array(ids), names=np.array([results[i][0] for i in ids]),
                        teams=np.array([results[i][1] for i in ids]), groups=np.array([results[i][2] for i in ids]),
                        draws=M)
    summarize(ids, results, M, quest).to_csv(str(base) + "_summary.csv", index=False)
    json.dump({"envs": envs, "dropped_out": dropped}, open(str(base) + "_env.json", "w"), indent=1, default=float)
    print("saved", base, "|", len(ids), "players,", a.sims, "sims each")


if __name__ == "__main__":
    main()
