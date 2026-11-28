"""Live DraftKings points for Zac's entries (added 2026-11-22).

Read only. Pulls the public ESPN scoreboard and per-game summaries (box scores), scores every
player under DraftKings NFL Classic rules, and totals each entry from the week folder's entries
file (picked by dfs_week.find_entries, the same pick the rest of the dashboard uses).
Nothing here talks to DraftKings, enters a lineup or spends. Output goes to dfs_live.json,
written by poller.py only while games are live (plus one refresh when a game goes final).

DraftKings NFL Classic rules used:
  pass 0.04/yd, 4/TD, -1 INT, +3 at 300 yds; rush and rec 0.1/yd, 6/TD, +3 at 100 yds each;
  rec 1/catch; fumble lost -1; 2-pt conversion 2; kick/punt return TD 6 (returner).
  DST: sack 1, INT 2, fumble recovery 2, defensive or special teams TD 6, safety 2, blocked kick 2,
  points allowed 0=10, 1-6=7, 7-13=4, 14-20=1, 21-27=0, 28-34=-1, 35+=-4.
Approximations (flagged on the page): DST fumble recovery = opponent fumbles lost. Points allowed
subtracts the opposing defense and special teams scores (return TDs with their kick, safeties).
Two-point conversions are read from play text and could not be checked against a live example yet.
"""
import json
import os
import re
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

import config
import dfs_week

SB_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"
SUM_URL = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/summary?event="
HEAD = {"User-Agent": "Mozilla/5.0"}
LIVE_PATH = config.DASHBOARD_DIR / "dfs_live.json"
TEAM_FIX = {"WAS": "WSH", "JAC": "JAX", "LA": "LAR", "ARZ": "ARI"}
MIN_SECONDS = 55  # do not refetch more often than this unless forced
_final_cache = {}  # event id -> parsed box score for finished games (never changes)
_proj_cache = {"mtime": None, "map": {}}
_last = {"t": 0.0, "finals": -1}


def _norm(name):
    n = re.sub(r"\b(jr|sr|ii|iii|iv|v)\b\.?", "", (name or "").lower())
    return re.sub(r"[^a-z0-9]", "", n)


def _t(ab):
    return TEAM_FIX.get(ab, ab)


def _g(url):
    r = requests.get(url, headers=HEAD, timeout=20)
    r.raise_for_status()
    return r.json()


def _f(v):
    try:
        return float(str(v).split("/")[0])
    except (TypeError, ValueError):
        return 0.0


def pa_points(pa):
    return 10 if pa == 0 else 7 if pa <= 6 else 4 if pa <= 13 else 1 if pa <= 20 else 0 if pa <= 27 else -1 if pa <= 34 else -4


def new_player():
    return {"pyd": 0.0, "ptd": 0.0, "int": 0.0, "ryd": 0.0, "rtd": 0.0, "rec": 0.0, "recyd": 0.0, "retd": 0.0,
            "fum": 0.0, "ret_td": 0.0, "two": 0.0}


def score_player(p):
    pts = p["pyd"] * 0.04 + p["ptd"] * 4 - p["int"] + (3 if p["pyd"] >= 300 else 0)
    pts += p["ryd"] * 0.1 + p["rtd"] * 6 + (3 if p["ryd"] >= 100 else 0)
    pts += p["recyd"] * 0.1 + p["retd"] * 6 + p["rec"] + (3 if p["recyd"] >= 100 else 0)
    pts += -p["fum"] + p["ret_td"] * 6 + p["two"] * 2
    return round(pts, 2)


def score_dst(d):
    return round(d["sk"] + 2 * d["int"] + 2 * d["fr"] + 6 * d["td"] + 2 * d["safety"] + 2 * d["blk"] + pa_points(d["pa"]), 2)


def parse_game(ev, d):
    """One game's box score into {players: {(team, normname): stats}, dst: {team: stats}, plus bookkeeping}."""
    comps = ev["competitions"][0]["competitors"]
    score = {_t(c["team"]["abbreviation"]): int(c.get("score") or 0) for c in comps}
    teams = list(score)
    players, dst = {}, {t: {"sk": 0.0, "int": 0.0, "fr": 0.0, "td": 0.0, "safety": 0.0, "blk": 0.0, "pa": 0,
                            "def_pts_scored": 0} for t in teams}
    roster = {t: {} for t in teams}  # team -> {normname: displayName}, for 2-pt text matching
    for tb in d.get("boxscore", {}).get("players", []):
        ab = _t(tb["team"]["abbreviation"])
        for cat in tb.get("statistics", []):
            keys, nm = cat["keys"], cat["name"]
            for a in cat.get("athletes", []):
                name = a["athlete"]["displayName"]
                v = dict(zip(keys, a["stats"]))
                p = players.setdefault((ab, _norm(name)), dict(new_player(), name=name, team=ab))
                roster[ab][_norm(name)] = name
                if nm == "passing":
                    p["pyd"] += _f(v.get("passingYards")); p["ptd"] += _f(v.get("passingTouchdowns")); p["int"] += _f(v.get("interceptions"))
                elif nm == "rushing":
                    p["ryd"] += _f(v.get("rushingYards")); p["rtd"] += _f(v.get("rushingTouchdowns"))
                elif nm == "receiving":
                    p["rec"] += _f(v.get("receptions")); p["recyd"] += _f(v.get("receivingYards")); p["retd"] += _f(v.get("receivingTouchdowns"))
                elif nm == "fumbles":
                    p["fum"] += _f(v.get("fumblesLost"))
                elif nm in ("kickReturns", "puntReturns"):
                    p["ret_td"] += _f(v.get("kickReturnTouchdowns" if nm == "kickReturns" else "puntReturnTouchdowns"))
                elif nm == "defensive":
                    dst[ab]["sk"] += _f(v.get("sacks"))
                elif nm == "interceptions":
                    dst[ab]["int"] += _f(v.get("interceptions"))
    # fumble recoveries by the defense = the other team's fumbles lost
    lost = {t: sum(p["fum"] for p in players.values() if p["team"] == t) for t in teams}
    for t in teams:
        dst[t]["fr"] = sum(v for k, v in lost.items() if k != t)
    # scoring plays: defensive and special teams touchdowns, safeties
    for s in d.get("scoringPlays", []):
        ab = _t(s.get("team", {}).get("abbreviation", ""))
        if ab not in dst:
            continue
        ty = (s.get("type", {}).get("text", "") + " " + s.get("scoringType", {}).get("name", "")).lower()
        txt = s.get("text", "")
        if "safety" in ty:
            dst[ab]["safety"] += 1
            dst[ab]["def_pts_scored"] += 2
        elif "touchdown" in ty and any(k in ty for k in ("return", "interception", "fumble", "blocked", "missed")):
            dst[ab]["td"] += 1
            extra = 1 if re.search(r"kick\)", txt, re.I) else 0
            dst[ab]["def_pts_scored"] += 6 + extra
    # blocked kicks and 2-point conversions come from the play by play
    drives = d.get("drives", {})
    dl = list(drives.get("previous", []))
    if isinstance(drives.get("current"), dict):
        dl.append(drives["current"])
    for dr in dl:
        off = _t(dr.get("team", {}).get("abbreviation", ""))
        for pl in dr.get("plays", []):
            ty, txt = pl.get("type", {}).get("text", ""), pl.get("text", "")
            if "blocked" in ty.lower() and off in dst:
                for t in teams:
                    if t != off:
                        dst[t]["blk"] += 1
            if re.search(r"two.?point", txt, re.I) and re.search(r"attempt succeeds|conversion is good|\bgood\b", txt, re.I) and not re.search(r"fails|no good|failed", txt, re.I):
                for tok in re.findall(r"\b([A-Z])\.\s?([A-Z][A-Za-z'\-]+)", txt):
                    ini, last = tok
                    for key, name in roster.get(off, {}).items():
                        parts = name.split()
                        if parts and parts[0][0].upper() == ini and _norm(parts[-1] if _norm(parts[-1]) not in ("jr", "iii", "ii") else parts[-2]) == _norm(last):
                            players[(off, key)]["two"] += 1
    for t in teams:
        opp = [x for x in teams if x != t][0]
        dst[t]["pa"] = max(0, score[opp] - dst[opp]["def_pts_scored"])
    st = ev["status"]["type"]
    per = ev["status"].get("period") or 0
    clk = ev["status"].get("clock") or 0
    if st["state"] == "post":
        frac = 0.0
    elif st["state"] == "pre":
        frac = 1.0
    else:
        frac = max(0.0, min(1.0, ((4 - min(per, 4)) * 900 + clk) / 3600.0)) if per <= 4 else 0.1
    return {"players": players, "dst": dst, "state": st["state"], "detail": st["detail"], "frac": frac,
            "teams": teams, "score": score}


def _projections():
    p = Path(r"D:\WKP\data\ff-simulator\dfs_projections_2026_wk11.csv")
    try:
        mt = p.stat().st_mtime
    except OSError:
        return {}
    if _proj_cache["mtime"] != mt:
        import csv
        m = {}
        try:
            with open(p, newline="", encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    try:
                        m[(_t(r["team"]), _norm(r["name"]))] = float(r["dk_mean"]) * float(r.get("p_play") or 1)
                    except (ValueError, KeyError):
                        pass
        except OSError:
            m = {}
        _proj_cache.update(mtime=mt, map=m)
    return _proj_cache["map"]


def compute(week, force=False):
    """Returns the dfs_live dict, or None when it was throttled or nothing needs doing."""
    now = time.time()
    sb = _g(SB_URL)
    games = {}
    finals = 0
    for ev in sb.get("events", []):
        st = ev["status"]["type"]["state"]
        eid = ev["id"]
        if st == "post":
            finals += 1
            if eid not in _final_cache:
                _final_cache[eid] = parse_game(ev, _g(SUM_URL + eid))
            games[eid] = _final_cache[eid]
        elif st == "in":
            games[eid] = parse_game(ev, _g(SUM_URL + eid))
        else:
            comps = ev["competitions"][0]["competitors"]
            tm = [_t(c["team"]["abbreviation"]) for c in comps]
            games[eid] = {"players": {}, "dst": {}, "state": "pre", "detail": ev["status"]["type"]["detail"], "frac": 1.0,
                          "teams": tm, "score": {}}
    any_live = any(g["state"] == "in" for g in games.values())
    if not force and not any_live and finals == _last["finals"]:
        return None
    if not force and now - _last["t"] < MIN_SECONDS:
        return None
    _last.update(t=now, finals=finals)

    team_game = {}
    for eid, g in games.items():
        for t in g["teams"]:
            team_game[t] = g
    proj = _projections()

    folder = dfs_week.week_dir(week)
    out = {"generated_at": datetime.now(timezone.utc).isoformat(), "week": week, "games_live": any_live,
           "notes": [], "entries": [], "games": [{"teams": "@".join(g["teams"]), "state": g["state"], "detail": g["detail"]}
                                             for g in games.values()]}
    ent_files = dfs_week.find_entries(folder) if folder.is_dir() else []
    if not ent_files:
        out["notes"].append(f"No entries file in {folder}.")
        return out
    sal_files = dfs_week.find_salaries(folder)
    ents, raw = dfs_week._entries(ent_files[0])
    pmap = dfs_week._player_map(sal_files, raw)
    out["entries_file"] = ent_files[0].name
    for i, e in enumerate(ents):
        if not any(e["ids"]):
            continue
        plist, total, rem = [], 0.0, 0.0
        for slot, pid in zip(dfs_week.SLOTS, e["ids"]):
            pm = pmap.get(pid, {})
            name, team = pm.get("name") or f"ID {pid}", _t(pm.get("team", ""))
            g = team_game.get(team)
            state = g["state"] if g else "unknown"
            pts, flag = None, ""
            if g is None:
                flag = "game not found"
            elif state == "pre":
                pts, flag = 0.0, "not started"
            elif slot == "DST":
                d = g["dst"].get(team)
                pts = score_dst(d) if d else 0.0
            else:
                p = g["players"].get((team, _norm(name)))
                if p is None:
                    pts, flag = 0.0, "no stats yet"
                else:
                    pts = score_player(p)
            if slot == "DST":
                pr = 0.0
            else:
                pr = proj.get((team, _norm(name)), 0.0)
            pr_rem = None if g is None else round(pr * g["frac"], 1)
            total += pts or 0.0
            rem += pr_rem or 0.0
            plist.append({"slot": slot, "name": name, "team": team, "pts": None if pts is None else round(pts, 2),
                          "game_state": {"pre": "not started", "in": "live", "post": "final"}.get(state, state),
                          "game": g["detail"] if g else "", "flag": flag, "proj_remaining": pr_rem})
        out["entries"].append({"entry_id": e["entry_id"], "contest_name": e["contest_name"], "entry_fee": e["entry_fee"],
                               "total": round(total, 2), "proj_remaining": round(rem, 1), "players": plist,
                               "all_final": all(p["game_state"] == "final" for p in plist),
                               "live_count": sum(1 for p in plist if p["game_state"] == "live"),
                               "not_started": sum(1 for p in plist if p["game_state"] == "not started")})
    out["entries"].sort(key=lambda x: -x["total"])
    out["notes"].append("Projected remaining is rough: the sim's DK mean times the share of the game clock left. DST has no projection.")
    out["notes"].append("DST fumble recoveries are the opponent's fumbles lost, and points allowed drops the opposing defense and special teams scores. Two-point conversions come from play text.")
    return out


def write(obj):
    fd, tmp = tempfile.mkstemp(dir=str(config.DASHBOARD_DIR), suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1)
    os.replace(tmp, LIVE_PATH)


if __name__ == "__main__":
    import sys
    wk = int(sys.argv[1]) if len(sys.argv) > 1 else 11
    r = compute(wk, force=True)
    print(json.dumps(r, indent=1) if "--json" in sys.argv else
          "\n".join(f"{e['entry_id']} {e['total']}  rem {e['proj_remaining']}" for e in r["entries"]))
