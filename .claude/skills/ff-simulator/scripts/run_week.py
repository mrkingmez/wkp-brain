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
import time
import zlib
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
TRANSFER_TGT = 0.6       # first game on a new team: share of his old target share (thin evidence, n=8)
TRANSFER_CAR = 0.3       # same for carries (n=3, a guess)
OFFENSE_WIDEN = 1.3


def market_lines(odds_path: str) -> dict:
    """{(away, home): (home_favored_by, total)} using the median across books."""
    age_h = (time.time() - Path(odds_path).stat().st_mtime) / 3600
    if age_h > 24:                      # 2026-11-12: a stale lines file used to be read without a word
        print(f"  WARNING: odds file is {age_h:.0f} hours old: {odds_path}")
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


UNAVAILABLE = {"OUT", "IR", "PUP", "NFI", "RESERVE", "SUSPENDED", "HOLDOUT", "RETIRED", "CUT", "PRACTICE_SQUAD", "INACTIVE"}
DOUBTFUL_PLAY_RATE = 0.25


def injury_sets(season=None, week=None, verbose=True):
    """Return (drop set, rates dict) as gsis ids.

    If the file data/ff-simulator/injuries_SEASON_wkWEEK.csv exists (build_injuries.py: MFL + nflverse + ESPN +
    transactions, latest source wins) it is used, then overrides_<season>_wk<week>.json (same folder) is applied on top.
    Otherwise falls back to the old MFL-only logic (Week 6 behaviour unchanged).
    rates maps gsis -> chance he plays (Questionable 0.75, Doubtful 0.25). It is a dict, so `in` checks still work.
    """
    f = OUT / f"injuries_{season}_wk{week}.csv" if season and week else None
    if f is not None and f.exists():
        d = pd.read_csv(f)
        d = d[d.gsis_id.notna()]
        drop, rates = set(), {}
        for r in d.itertuples():
            if r.category in UNAVAILABLE:
                drop.add(r.gsis_id)
            elif r.category == "DOUBTFUL":
                rates[r.gsis_id] = DOUBTFUL_PLAY_RATE
            elif r.category == "QUESTIONABLE":
                # 2026-11-12: the table's own play chance (0.40 when he did not practice, else 0.75)
                pp = getattr(r, "play_prob", QUESTIONABLE_PLAY_RATE)
                rates[r.gsis_id] = float(pp) if pp == pp and 0 < float(pp) < 1 else QUESTIONABLE_PLAY_RATE
        o = OUT / f"overrides_{season}_wk{week}.json"
        if o.exists():
            ov = json.load(open(o))
            for p in ov.get("players", []):
                m = d[(d.player.str.lower() == p["name"].lower()) & (d.team == p["team"])]
                gid = p.get("gsis_id") or (m.gsis_id.iloc[0] if len(m) else None)
                if not gid:
                    print("  OVERRIDE NOT APPLIED (no gsis match):", p["name"])
                    continue
                prob = p.get("play_prob")
                cat = p["category"]
                drop.discard(gid)
                rates.pop(gid, None)
                if cat in UNAVAILABLE or prob == 0:
                    drop.add(gid)
                elif prob is not None and prob < 1:
                    rates[gid] = prob
                elif cat == "QUESTIONABLE":
                    rates[gid] = QUESTIONABLE_PLAY_RATE
                elif cat == "DOUBTFUL":
                    rates[gid] = DOUBTFUL_PLAY_RATE
                if verbose:
                    print(f"  override: {p['name']} ({p['team']}) -> {cat} {prob if prob is not None else ''}")
        return drop, rates
    sys.path.insert(0, r"D:\WKP\Fantasy-Football\dashboard")
    import mfl_client as m
    cache = json.load(open(r"D:\WKP\.claude\skills\fantasy-football-data\players-cache-details.json"))
    plist = cache["players"]["player"] if "players" in cache else cache
    espn = {p["id"]: p.get("espn_id") for p in plist}
    npl = pd.read_parquet(DATA_PLAYERS)[["gsis_id", "espn_id"]].dropna()
    npl["espn_id"] = npl.espn_id.astype(str).str.replace(r"\.0$", "", regex=True)
    e2g = dict(zip(npl.espn_id, npl.gsis_id))
    drop, quest = set(), {}
    for i in m.injuries().get("injuries", {}).get("injury", []):
        e = espn.get(i["id"])
        g = e2g.get(str(e)) if e else None
        status = (i.get("status") or "").lower()
        if not g:
            continue
        if status in ("out", "doubtful", "suspended", "holdout", "retired") or status.startswith("ir"):
            drop.add(g)
        elif "question" in status:
            quest[g] = QUESTIONABLE_PLAY_RATE
    return drop, quest


def add_transfers(team, tmodel, pw, tg, as_of, stat_team, last_order, team_now, drops, cache):
    """Players now on `team` whose stats were all earned somewhere else (trades, waiver claims). 2026-11-12.

    Before this they got no projection at all (Jordan Davis, PHI to JAX, Week 10, was read as a bye).
    Defenders carry their own per-game tackle and sack rates, so they move as they are. A quarterback moves with
    his attempt count so he can be the passer. Runners and receivers are NOT moved: their numbers are shares of the
    old team's offense and there is no evidence yet for a share on the new one. They are listed, not guessed."""
    added, skipped = [], []
    for pid, now_team in (team_now or {}).items():
        if now_team != team or pid in tmodel.players or pid in drops:
            continue
        prev = stat_team.get(pid)
        if prev in (None, team) or last_order.get(pid, 0) < as_of - 6:      # must have played in the last six weeks
            continue
        if prev not in cache:
            cache[prev] = sm.TeamModel(prev, pw, tg, None, as_of, None)
        v = cache[prev].players.get(pid)
        if v is None:
            continue
        if v["group"] in ("DL", "LB", "DB", "QB"):
            tmodel.players[pid] = dict(v, tgt_share=0.0, car_share=0.0, rec_td_share=0.0, rush_td_share=0.0, qb_share=0.0,
                                       new_team=True)
            added.append((team, v["name"], v["group"], prev))
        elif v["group"] in ("RB", "WR", "TE"):
            # 2026-11-12 afternoon: first game on a new team. 2024 to 2026, players with a real role who moved in season:
            # first-game target share was 0.54 of the old share (n=8; error 0.040 at a 0.6 factor against 0.106 for no
            # projection). Carries: 0 of 3 backs had a carry share in game one, so 0.3 is a guess on almost no data.
            tmodel.players[pid] = dict(v, tgt_share=v["tgt_share"] * TRANSFER_TGT, rec_td_share=v["rec_td_share"] * TRANSFER_TGT,
                                       car_share=v["car_share"] * TRANSFER_CAR, rush_td_share=v["rush_td_share"] * TRANSFER_CAR,
                                       qb_share=0.0, new_team=True)
            skipped.append((team, v["name"], v["group"], prev))
    return added, skipped


def game_rng(seed, key):
    """One random stream per game (and per player for the sit-out draw). 2026-11-12: with a single shared stream, a
    roster change in the first game changed the dice for every later game, so two runs differed even where nothing
    had changed. Now an untouched game gives the same numbers run to run."""
    return np.random.default_rng([int(seed), zlib.crc32(str(key).encode())])


def qb_starts(season, week):
    """{team: (gsis_id, name)} from the "qbs" block of overrides_<season>_wk<week>.json, {} if none."""
    o = OUT / f"overrides_{season}_wk{week}.json"
    if not o.exists():
        return {}
    return {t: (v["gsis_id"], v.get("name", v["gsis_id"])) for t, v in json.load(open(o)).get("qbs", {}).items()}


def simulate_week(season, week, lines, tg, lg, pw, defs, lg_def, sched, drops=frozenset(), quest=frozenset(),
                  sims=4000, seed=2026, verbose=True, apply_quest_zero=True, boxes=None, team_now=None, ol_missing=None,
                  qb_start=None, notes=None):
    as_of = season * 100 + week
    wk = sched[(sched.season == season) & (sched.week == week)]
    latest = pw.sort_values("order").groupby("player_id").team.last().to_dict()
    stat_team = dict(latest)
    last_order = pw.groupby("player_id").order.max().to_dict()
    latest.update(team_now or {})      # current NFL team from the injury/roster layer beats the stat-history team
    results, envs, dropped = {}, {}, []
    prev_cache = {}
    notes = notes if notes is not None else {}
    notes.setdefault("transfers_added", [])
    notes.setdefault("transfers_reduced_share", [])
    notes.setdefault("qb_named", [])
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
            tm[team].avail = dict(quest)
            tm[team].ol_missing = (ol_missing or {}).get(team, 0.0)
            names = {i: v["name"] for i, v in tm[team].players.items()}
            dropped += [(team, names[i]) for i in tm[team].drop(drops)]
            add, skip = add_transfers(team, tm[team], pw, tg, as_of, stat_team, last_order, team_now, drops, prev_cache)
            notes["transfers_added"] += add
            notes["transfers_reduced_share"] += skip
            if qb_start and team in qb_start and qb_start[team][0] not in drops:
                tm[team].set_qb(*qb_start[team])
                notes["qb_named"].append((team, qb_start[team][1]))
        bx = {} if boxes is not None else None
        rng = game_rng(seed, f"{away}@{home}")
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
                M[n] *= (game_rng(seed, i).random(M.shape[1]) < quest[i])
    if verbose:
        for k in ("transfers_added", "transfers_reduced_share", "qb_named"):
            if notes[k]:
                print(f"  {k}: {notes[k]}")
    return ids, results, M, envs, dropped


def summarize(ids, results, M, quest=frozenset()):
    return pd.DataFrame({
        "gsis_id": ids, "name": [results[i][0] for i in ids], "team": [results[i][1] for i in ids],
        "group": [results[i][2] for i in ids], "mean": M.mean(1), "sd": M.std(1),
        "p10": np.percentile(M, 10, axis=1), "p50": np.percentile(M, 50, axis=1), "p90": np.percentile(M, 90, axis=1),
        "questionable": [i in quest for i in ids]}).sort_values("mean", ascending=False)


def current_teams(season, week):
    """gsis -> current NFL team from the merged injury table (nflverse weekly roster). {} if no table (Week 6 behaviour)."""
    f = OUT / f"injuries_{season}_wk{week}.csv"
    if not f.exists():
        return {}
    d = pd.read_csv(f)
    d = d[d.gsis_id.notna() & d.roster_team.notna()]
    return dict(zip(d.gsis_id, d.roster_team))


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
    ap.add_argument("--odds", required=True, help="this week's Odds API pull (no default since 2026-11-12: the old default was the Week 6 file)")
    ap.add_argument("--seed", type=int, default=2026)
    ap.add_argument("--ol", default="", help="offensive-line layer: 'full', 'yds' (no sack effect) or a number; output gets an _ol suffix")
    a = ap.parse_args()
    tg, lg, pw, defs, lg_def, sched = load_all(a.season, a.week)
    lines = market_lines(a.odds)
    ol_miss, suffix = None, ""
    if a.ol:
        import ol_model
        zero = ("sack_rate",) if a.ol == "yds" else ()
        sm.set_ol(1.0 if a.ol in ("full", "yds") else float(a.ol), zero)
        ol_miss = ol_model.week_miss(a.season, a.week)
        suffix = "_ol" + a.ol
        print("OL missing share by team:", {k: round(v, 2) for k, v in ol_miss.items() if v > 0})
    drops, quest = injury_sets(a.season, a.week)
    print(f"{len(drops)} unavailable flagged, {len(quest)} questionable/doubtful (rate < 1)")
    ids, results, M, envs, dropped = simulate_week(a.season, a.week, lines, tg, lg, pw, defs, lg_def, sched,
                                                   drops, quest, a.sims, a.seed, team_now=current_teams(a.season, a.week), ol_missing=ol_miss,
                                                   qb_start=qb_starts(a.season, a.week))
    OUT.mkdir(parents=True, exist_ok=True)
    base = OUT / f"sim_{a.season}_wk{a.week}{suffix}"
    np.savez_compressed(str(base) + ".npz", ids=np.array(ids), names=np.array([results[i][0] for i in ids]),
                        teams=np.array([results[i][1] for i in ids]), groups=np.array([results[i][2] for i in ids]),
                        draws=M)
    summarize(ids, results, M, quest).to_csv(str(base) + "_summary.csv", index=False)
    json.dump({"envs": envs, "dropped_out": dropped}, open(str(base) + "_env.json", "w"), indent=1, default=float)
    print("saved", base, "|", len(ids), "players,", a.sims, "sims each")


if __name__ == "__main__":
    main()
