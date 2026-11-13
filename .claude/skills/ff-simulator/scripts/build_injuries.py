"""Build the merged injury / availability table for one NFL week from several live sources.

python build_injuries.py 2026 7 [--tx-days 10]

Sources (all fetched live, nothing from memory):
  MFL_INJ    MFL injuries export (api host, W=week). One response timestamp for all rows.
  MFL_ROSTER MFL rosters export (every franchise): the league's own IR/taxi slot, kept as a note only
             (a fantasy IR slot is not an NFL status).
  NFLV_INJ   nflverse injuries release, rows for this week (practice + game status). As-of = release timestamp.
  NFLV_ROST  nflverse weekly_rosters release, this week (ACT / DEV practice squad / RES reserve / CUT ...).
  ESPN_INJ   ESPN site API league-wide injuries (per-player timestamp, with ESPN's own comment).
  ESPN_TX    ESPN site API transactions, last N days (IR placements, activations, signings, cuts, PS moves).

Merge rule: per player, latest as-of wins. If two sources disagree on the CATEGORY, the conflict is
written into the note with each source and time. A table older than 24h is reported at the end.

Writes: D:\\WKP\\data\\ff-simulator\\injuries_<season>_wk<week>.csv   (merged, one row per player)
        D:\\WKP\\data\\ff-simulator\\injuries_<season>_wk<week>_allsources.csv  (every raw record)
Columns of the merged file: player, team, status, source, as_of, note, gsis_id, pos, category, play_prob
"""
import argparse
import datetime as dt
import io
import json
import re
import sys
import unicodedata
from pathlib import Path

import pandas as pd
import requests

sys.path.insert(0, r"D:\WKP\Fantasy-Football\dashboard")
OUT = Path(r"D:\WKP\data\ff-simulator")
SCR = Path(r"D:\WKP\scratch\inj")
PLAYERS_PQ = Path(r"D:\WKP\data\nfl\players\players.parquet")
MFL_CACHE = Path(r"D:\WKP\.claude\skills\fantasy-football-data\players-cache-details.json")
NFLV = "https://github.com/nflverse/nflverse-data/releases/download"
ESPN = "https://site.api.espn.com/apis/site/v2/sports/football/nfl"
UA = {"User-Agent": "wkp-ff-injury-layer/1.0"}

BAD_KEYS = {"nan", "None", "", "<NA>", "NaN"}
LOC2ABBR = {"Arizona": "ARI", "Atlanta": "ATL", "Baltimore": "BAL", "Buffalo": "BUF", "Carolina": "CAR", "Chicago": "CHI",
            "Cincinnati": "CIN", "Cleveland": "CLE", "Dallas": "DAL", "Denver": "DEN", "Detroit": "DET", "Green Bay": "GB",
            "Houston": "HOU", "Indianapolis": "IND", "Jacksonville": "JAX", "Kansas City": "KC", "Las Vegas": "LV",
            "Miami": "MIA", "Minnesota": "MIN", "New England": "NE", "New Orleans": "NO", "Philadelphia": "PHI",
            "Pittsburgh": "PIT", "San Francisco": "SF", "Seattle": "SEA", "Tampa Bay": "TB", "Tennessee": "TEN",
            "Washington": "WAS", "New York Giants": "NYG", "New York Jets": "NYJ", "Los Angeles Rams": "LA",
            "Los Angeles Chargers": "LAC", "N.Y. Giants": "NYG", "N.Y. Jets": "NYJ", "L.A. Rams": "LA", "L.A. Chargers": "LAC"}
TEAM_FIX = {"WSH": "WAS", "LAR": "LA", "JAC": "JAX", "ARZ": "ARI", "BLT": "BAL", "CLV": "CLE", "HST": "HOU", "SD": "LAC",
            "STL": "LA", "OAK": "LV"}
# category -> probability he plays (None = not in play)
PLAY_PROB = {"ACTIVE": 1.0, "QUESTIONABLE": 0.75, "DOUBTFUL": 0.25, "OUT": 0.0, "IR": 0.0, "PUP": 0.0, "NFI": 0.0,
             "SUSPENDED": 0.0, "HOLDOUT": 0.0, "RETIRED": 0.0, "CUT": 0.0, "PRACTICE_SQUAD": 0.0, "INACTIVE": 0.0,
             "RESERVE": 0.0, "NONE": 1.0}
Q_DNP_PLAY_PROB = 0.40
RECORDS = []
CLASS = {c: "UNAVAILABLE" for c in ("OUT", "IR", "PUP", "NFI", "RESERVE", "SUSPENDED", "HOLDOUT", "RETIRED", "CUT", "PRACTICE_SQUAD", "INACTIVE")}
CLASS.update({"DOUBTFUL": "DOUBTFUL", "QUESTIONABLE": "QUESTIONABLE", "ACTIVE": "ACTIVE", "NONE": "NONE"})


def tm(t):
    t = (t or "").upper()
    return TEAM_FIX.get(t, t)


def norm(n):
    n = unicodedata.normalize("NFKD", str(n)).encode("ascii", "ignore").decode().lower()
    n = re.sub(r"\b(jr|sr|ii|iii|iv|v)\b\.?", "", n)
    return re.sub(r"[^a-z]", "", n)


def iso(s):
    """Any ISO-ish string -> aware UTC datetime."""
    s = str(s).replace("Z", "+00:00")
    d = dt.datetime.fromisoformat(s if "+" in s[10:] or "-" in s[10:] else s + "+00:00")
    return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)


def add(source, as_of, name, team, status, category, gsis=None, pos=None, note="", espn_id=None, mfl_id=None):
    RECORDS.append(dict(player=name, team=tm(team), status=status, category=category, source=source,
                        as_of=as_of.strftime("%Y-%m-%dT%H:%MZ") if as_of else "not available", note=note,
                        gsis_id=gsis, pos=pos, espn_id=str(espn_id) if espn_id else None, mfl_id=mfl_id))


def get(url, **kw):
    r = requests.get(url, headers=UA, timeout=60, **kw)
    r.raise_for_status()
    return r


def refresh_mfl_players():
    """MFL players cache can miss recent signings; refresh it (DETAILS=1 carries espn_id)."""
    import mfl_client as m
    d = m._get(m.MFL_HOST, "players", {"L": m.MFL_LEAGUE_ID, "DETAILS": "1"})
    if MFL_CACHE.exists():
        MFL_CACHE.with_suffix(".json.bak").write_bytes(MFL_CACHE.read_bytes())
    json.dump(d, open(MFL_CACHE, "w"))
    return d


def espn_team_check(franchise, out, mfl_by_id, ros, e2g):
    """2026-11-12: ask ESPN's athlete page which team each player on one fantasy roster is on, and list every
    disagreement with the merged table. Nothing is changed automatically (ESPN's page can be stale too): it is a
    loud list to read before the lineup is built. One call per player, about 60 calls."""
    import time
    fix = {"WSH": "WAS", "LAR": "LA"}
    rt = dict(zip(out.gsis_id, out.roster_team))
    flags = []
    for f in ros["rosters"]["franchise"]:
        if f["id"] != franchise:
            continue
        pl = f.get("player", [])
        for r in ([pl] if isinstance(pl, dict) else pl):
            p = mfl_by_id.get(r["id"], {})
            e = str(p.get("espn_id") or "")
            if not e:
                flags.append(f"{p.get('name', r['id'])}: no ESPN id, team not checked")
                continue
            try:
                a = requests.get(f"https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{e}", timeout=20).json().get("athlete", {})
                et = (a.get("team") or {}).get("abbreviation")
                et = fix.get(et, et)
            except Exception as ex:
                flags.append(f"{p.get('name')}: ESPN not retrieved ({type(ex).__name__})")
                continue
            ours = rt.get(e2g.get(e))
            if et and isinstance(ours, str) and et != ours:
                flags.append(f"{p.get('name')}: ESPN says {et}, merged table says {ours}, MFL says {p.get('team')}")
            elif et and not isinstance(ours, str) and tm(p.get("team")) not in (et, "FA") and (a.get("status") or {}).get("name") != "Free Agent":
                flags.append(f"{p.get('name')}: ESPN says {et}, MFL says {p.get('team')}, no roster row this week")
            time.sleep(0.2)
    print("ESPN TEAM CHECK for franchise", franchise, "->", flags or "all teams agree")
    return flags


def build(season, week, tx_days, check_franchise=None):
    now = dt.datetime.now(dt.timezone.utc)
    report = {"fetched_at": now.strftime("%Y-%m-%dT%H:%MZ"), "sources": {}}
    import mfl_client as m

    # ---------------- ID bridges
    mfl_players = refresh_mfl_players()
    plist = mfl_players["players"]["player"]
    mfl_by_id = {p["id"]: p for p in plist}
    report["sources"]["MFL_players_refresh"] = f"{len(plist)} players"
    npl = pd.read_parquet(PLAYERS_PQ)
    npl["espn_id"] = npl.espn_id.astype(str).str.replace(r"\.0$", "", regex=True)
    # 2026-11-12 fix: 8,395 players have no ESPN id. astype(str) turned those into the key "nan", so every record that
    # could not be matched was given one bogus shared player id (about 100 records a week collapsed into one row).
    e2g = {e: g for e, g in zip(npl.espn_id, npl.gsis_id) if e not in BAD_KEYS and g == g}

    # nflverse weekly roster (week) -- also the name/team lookup for transactions
    rw_url = f"{NFLV}/weekly_rosters/roster_weekly_{season}.csv"
    rw = pd.read_csv(io.StringIO(get(rw_url).text), low_memory=False)
    rw_rel = get("https://api.github.com/repos/nflverse/nflverse-data/releases/tags/weekly_rosters").json()
    rw_ts = max(iso(a["updated_at"]) for a in rw_rel["assets"] if f"_{season}." in a["name"])
    # every real gsis id a name has carried this season, any team (used to find a traded player under his old team)
    name_any, last_team = {}, {}
    for r in rw.sort_values("week").itertuples():
        if isinstance(r.gsis_id, str) and r.gsis_id.startswith("00-"):
            name_any.setdefault(norm(r.full_name), set()).add(r.gsis_id)
            if r.week < week:
                last_team[r.gsis_id] = tm(r.team)
    rw = rw[rw.week == week].copy()
    rw["espn_id"] = rw.espn_id.astype(str).str.replace(r"\.0$", "", regex=True)
    for e, g in zip(rw.espn_id, rw.gsis_id):
        if g == g and e not in e2g and e not in BAD_KEYS:
            e2g[e] = g
    rw["team"] = rw.team.map(tm)
    rw["key"] = rw.full_name.map(norm)
    name_team = {(r.key, r.team): r.gsis_id for r in rw.itertuples() if r.gsis_id == r.gsis_id}
    npl["key"] = npl.display_name.map(norm) if "display_name" in npl.columns else ""
    gsis_info = {r.gsis_id: (r.full_name, r.team, r.position) for r in rw.itertuples() if r.gsis_id == r.gsis_id}

    def mfl_gsis(mid):
        p = mfl_by_id.get(mid)
        if not p:
            return None, None
        e = str(p.get("espn_id") or "")
        g = e2g.get(e)
        if not g:
            parts = [x.strip() for x in p["name"].split(",")]
            nm = " ".join(reversed(parts)) if len(parts) == 2 else p["name"]
            g = name_team.get((norm(nm), tm(p.get("team"))))
        return g, p

    # ---------------- (a) MFL injuries
    inj = m._get(m.MFL_API_HOST, "injuries", {"W": str(week)})
    mts = dt.datetime.fromtimestamp(int(inj["injuries"]["timestamp"]), dt.timezone.utc)
    CAT_MFL = {"out": "OUT", "doubtful": "DOUBTFUL", "questionable": "QUESTIONABLE", "ir": "IR", "ir-r": "IR",
               "ir-pup": "PUP", "ir-nfi": "NFI", "suspended": "SUSPENDED", "retired": "RETIRED", "holdout": "HOLDOUT"}
    n = 0
    for i in inj["injuries"]["injury"]:
        g, p = mfl_gsis(i["id"])
        if not p:
            continue
        cat = CAT_MFL.get(i["status"].lower(), "NONE")
        nm = " ".join(reversed([x.strip() for x in p["name"].split(",")]))
        add("MFL_INJ", mts, nm, p.get("team"), i["status"], cat, g, p.get("position"),
            note=f"{i.get('details', '')}; exp return {i.get('exp_return', 'n/a')}", espn_id=p.get("espn_id"), mfl_id=i["id"])
        n += 1
    report["sources"]["MFL_INJ"] = f"{n} rows, response timestamp {mts:%Y-%m-%dT%H:%MZ}, week {inj['injuries']['week']}"

    # ---------------- (a2) MFL roster statuses (note only)
    ros = m._get(m.MFL_HOST, "rosters", {"L": m.MFL_LEAGUE_ID})
    n = 0
    for f in ros["rosters"]["franchise"]:
        pl = f.get("player", [])
        pl = [pl] if isinstance(pl, dict) else pl
        for r in pl:
            if r.get("status") in ("INJURED_RESERVE",):
                g, p = mfl_gsis(r["id"])
                if p:
                    nm = " ".join(reversed([x.strip() for x in p["name"].split(",")]))
                    add("MFL_ROSTER", now, nm, p.get("team"), "league IR slot", "NONE", g, p.get("position"),
                        note=f"franchise {f['id']} has him in the fantasy IR slot (not an NFL status)", espn_id=p.get("espn_id"),
                        mfl_id=r["id"])
                    n += 1
    report["sources"]["MFL_ROSTER"] = f"{n} fantasy-IR-slot rows (note only), pulled {now:%Y-%m-%dT%H:%MZ}"

    # ---------------- (b) nflverse injuries
    ni = pd.read_csv(io.StringIO(get(f"{NFLV}/injuries/injuries_{season}.csv").text), low_memory=False)
    ni_rel = get("https://api.github.com/repos/nflverse/nflverse-data/releases/tags/injuries").json()
    ni_ts = max(iso(a["updated_at"]) for a in ni_rel["assets"] if f"_{season}." in a["name"])
    wk_rows = ni[ni.week == week]
    CAT_NV = {"out": "OUT", "doubtful": "DOUBTFUL", "questionable": "QUESTIONABLE"}
    for r in wk_rows.itertuples():
        st = str(r.report_status) if r.report_status == r.report_status else ""
        cat = CAT_NV.get(st.lower(), "NONE")
        prac = str(r.practice_status) if r.practice_status == r.practice_status else ""
        injt = r.report_primary_injury if r.report_primary_injury == r.report_primary_injury else r.practice_primary_injury
        add("NFLV_INJ", ni_ts, r.full_name, r.team, st or f"practice: {prac}", cat, r.gsis_id, r.position,
            note=f"game status '{st or 'none yet'}', practice '{prac}', injury {injt}")
    report["sources"]["NFLV_INJ"] = (f"{len(wk_rows)} rows for week {week} (weeks present: {sorted(ni.week.unique())}), "
                                     f"release updated {ni_ts:%Y-%m-%dT%H:%MZ}")

    # ---------------- (b1) nflreadpy injuries (same nflverse data via the loader, cross-check)
    try:
        import nflreadpy
        nr = nflreadpy.load_injuries([season]).to_pandas()
        nr = nr[nr.week == week]
        for r in nr.itertuples():
            st = str(r.report_status) if r.report_status == r.report_status else ""
            cat = CAT_NV.get(st.lower(), "NONE")
            add("NFLR_INJ", ni_ts, r.full_name, r.team, st or "practice only", cat, r.gsis_id, r.position,
                note=f"nflreadpy game status '{st or 'none yet'}'")
        report["sources"]["NFLR_INJ"] = f"{len(nr)} rows for week {week} via nflreadpy"
    except Exception as e:
        report["sources"]["NFLR_INJ"] = f"not available: {e}"

    # ---------------- (b2) nflverse weekly roster status
    CAT_RW = {"DEV": "PRACTICE_SQUAD", "RES": "RESERVE", "CUT": "CUT", "RET": "RETIRED", "EXE": "SUSPENDED", "INA": "INACTIVE",
              "W04": "CUT", "TRD": "NONE"}
    cnt = 0
    for r in rw.itertuples():
        cat = CAT_RW.get(r.status)
        if r.status == "ACT":
            cat = "ACTIVE"
        if cat is None:
            continue
        add("NFLV_ROST", rw_ts, r.full_name, r.team, f"{r.status}/{r.status_description_abbr}", cat, r.gsis_id, r.position,
            note=f"nflverse roster status {r.status} ({r.status_description_abbr})", espn_id=r.espn_id)
        cnt += 1
    report["sources"]["NFLV_ROST"] = f"{len(rw)} week-{week} roster rows, {cnt} records, release updated {rw_ts:%Y-%m-%dT%H:%MZ}"

    # ---------------- (c) ESPN injuries league-wide
    ej = get(f"{ESPN}/injuries").json()
    ets = iso(ej["timestamp"])
    CAT_E = {"active": "ACTIVE", "questionable": "QUESTIONABLE", "doubtful": "DOUBTFUL", "out": "OUT", "injured reserve": "IR",
             "suspension": "SUSPENDED"}
    n = 0
    for t in ej["injuries"]:
        tabbr = tm(t.get("abbreviation") or "")
        for i in t["injuries"]:
            a = i["athlete"]
            eid = None
            for lk in a.get("links", []):
                mm = re.search(r"/id/(\d+)/", lk.get("href", ""))
                if mm:
                    eid = mm.group(1)
                    break
            team = tm(a.get("team", {}).get("abbreviation")) or tabbr
            g = e2g.get(eid) or name_team.get((norm(a["displayName"]), team))
            d = i.get("details", {}) or {}
            cat = CAT_E.get(i["status"].lower(), "NONE")
            note = f"{d.get('type', '')} {d.get('detail', '') if d.get('detail') not in (None, 'Not Specified') else ''}".strip()
            note += f"; return {d.get('returnDate', 'n/a')}; {i.get('shortComment', '')[:160]}"
            add("ESPN_INJ", iso(i["date"]), a["displayName"], team, i["status"], cat, g, (a.get("position") or {}).get("abbreviation"),
                note=note, espn_id=eid)
            n += 1
    report["sources"]["ESPN_INJ"] = f"{n} rows, feed timestamp {ets:%Y-%m-%dT%H:%MZ}"

    # ---------------- (d) ESPN transactions
    cutoff = now - dt.timedelta(days=tx_days)
    tx = []
    for p in range(1, 80):
        r = get(f"{ESPN}/transactions", params={"page": p}).json()
        tr = r["transactions"]
        tx += tr
        if not tr or iso(tr[-1]["date"]) < cutoff:
            break
    tx = [t for t in tx if iso(t["date"]) >= cutoff]
    ets2 = iso(r["timestamp"])
    n = 0
    POS = r"(?:QB|RB|FB|WR|TE|OT|OG|OL|C|G|T|DE|DT|NT|DL|OLB|ILB|MLB|LB|CB|S|FS|SS|DB|K|P|LS|PK|EDGE)"
    nm_re = re.compile(rf"\b({POS})\s+((?:[A-Z][\w'’.\-]*)(?:\s+(?:[A-Z][\w'’.\-]*|Jr\.|Sr\.|III|II|IV|V))*)")
    sent_re = re.compile(r"(?<=\.)\s+(?=(?:Placed|Designated|Activated|Signed|Released|Waived|Elevated|Claimed|Suspended|Reinstated|"
                         r"Traded|Re-signed|Reverted|Removed|Retired|Added|Agreed|Acquired|Cut)\b)")
    trade_in = {}                  # gsis -> (new team, when): a trade in the transaction feed moves the player at once
    for t in tx:
        team = tm(t["team"]["abbreviation"])
        when = iso(t["date"])
        for s in sent_re.split(t["description"]):
            low = s.lower()
            if low.startswith("acquired"):
                # "Acquired DT X from Philadelphia for a pick": X arrives. "Acquired a pick from Y for WR Z": Z LEAVES.
                # Before 2026-11-12 both were logged as "signed" with this team, and a traded-in player whose nflverse
                # row still had a placeholder id was lost (Jordan Davis PHI to JAX, Week 10).
                head = re.split(r"\bfrom\b", s, maxsplit=1)[0]
                mfrom = re.search(r"\bfrom (?:the )?([A-Z][A-Za-z. ]+?)(?= for\b| in exchange\b|,|\.|$)", s)
                old = None
                if mfrom:
                    loc = mfrom.group(1).strip()
                    old = LOC2ABBR.get(loc) or next((v for k, v in LOC2ABBR.items() if loc.startswith(k)), None)
                for pos, nm in nm_re.findall(head):
                    nm = nm.strip().rstrip(".")
                    cands = name_any.get(norm(nm), set())
                    g = next((c for c in cands if old and last_team.get(c) == old), None)
                    if g is None and len(cands) == 1:
                        g = next(iter(cands))
                    if g is None:
                        g = name_team.get((norm(nm), team))
                    add("ESPN_TX", when, nm, team, "acquired by trade", "ACTIVE", g, pos,
                        note=f"ESPN transaction {when:%Y-%m-%d}: {s.strip()[:180]}")
                    if isinstance(g, str) and g.startswith("00-"):
                        trade_in[g] = (team, when)
                    n += 1
                continue
            if low.startswith("placed") and "injured reserve" in low and "practice squad" not in low:
                cat, st = "IR", "placed on injured reserve"
            elif "pup" in low or "physically unable" in low:
                cat, st = "PUP", "PUP move"
            elif "non-football" in low or " nfi" in low:
                cat, st = "NFI", "NFI move"
            elif low.startswith("designated") and "return from" in low:
                cat, st = "ACTIVE", "designated to return (still on reserve until activated)"
                cat = "IR"       # designated != activated; stays out until the 21-day window opens him up
            elif low.startswith("activated") or low.startswith("reinstated"):
                cat, st = "ACTIVE", "activated/reinstated"
            elif low.startswith("elevated"):
                cat, st = "ACTIVE", "elevated from practice squad"
            elif low.startswith("signed") and "from the practice squad to the active roster" in low:
                cat, st = "ACTIVE", "promoted from practice squad"
            elif low.startswith("signed") and "practice squad" in low:
                cat, st = "PRACTICE_SQUAD", "signed to practice squad"
            elif low.startswith("signed") or low.startswith("re-signed") or low.startswith("claimed") or low.startswith("acquired"):
                cat, st = "ACTIVE", "signed/claimed (roster status of the new deal unconfirmed)"
            elif low.startswith("released") or low.startswith("waived") or low.startswith("cut"):
                cat, st = "CUT", "released/waived" + (" from practice squad" if "practice squad" in low else "")
            elif low.startswith("suspended"):
                cat, st = "SUSPENDED", "suspended"
            elif "practice squad/injured" in low:
                cat, st = "PRACTICE_SQUAD", "practice squad injured list"
            else:
                continue
            for pos, nm in nm_re.findall(s):
                nm = nm.strip().rstrip(".")
                g = name_team.get((norm(nm), team))
                add("ESPN_TX", when, nm, team, st, cat, g, pos, note=f"ESPN transaction {when:%Y-%m-%d}: {s.strip()[:180]}")
                n += 1
    report["sources"]["ESPN_TX"] = (f"{len(tx)} team-transaction lines in last {tx_days} days -> {n} player moves, "
                                    f"feed timestamp {ets2:%Y-%m-%dT%H:%MZ} (dates are date-only, midnight ET)")

    # ---------------- merge
    df = pd.DataFrame(RECORDS)
    df["gsis_id"] = df.gsis_id.where(df.gsis_id.notna(), None)
    # fill missing gsis from espn_id / mfl bridge / name+team
    miss = df.gsis_id.isna()
    df.loc[miss, "gsis_id"] = [e2g.get(e) if isinstance(e, str) and e not in BAD_KEYS else None for e in df.loc[miss, "espn_id"]]
    miss = df.gsis_id.isna()
    df.loc[miss, "gsis_id"] = [name_team.get((norm(a), b)) for a, b in zip(df.loc[miss, "player"], df.loc[miss, "team"])]
    df["asof_dt"] = pd.to_datetime(df.as_of.replace("not available", pd.NA), utc=True, errors="coerce")
    df["key"] = df.gsis_id.fillna(df.player.map(norm) + "|" + df.team)
    merged = []
    mon = (now - dt.timedelta(days=now.weekday())).replace(hour=4, minute=0, second=0, microsecond=0)
    cycle_start = pd.Timestamp(mon)      # Monday 00:00 ET of this NFL week: designations since then are "this week's"
    rw_lag = pd.Timestamp(rw_ts) - pd.Timedelta(hours=60)
    for key, g in df.groupby("key"):
        # status-bearing records only (a bare 'NONE' practice row never overrides a designation)
        gg = g.sort_values("asof_dt", ascending=False)
        # A roster line saying ACT only proves he is not on reserve / practice squad. It must not wipe a game-day
        # designation (Out/Doubtful/Questionable) posted this week; it can still beat older or reserve-type records.
        desig = gg[gg.category.isin(["OUT", "DOUBTFUL", "QUESTIONABLE"]) & (gg.asof_dt >= cycle_start)]
        if len(desig):
            gg = gg[~((gg.source == "NFLV_ROST") & (gg.category == "ACTIVE"))]
        real = gg[gg.category != "NONE"]
        top = real.iloc[0] if len(real) else gg.iloc[0]
        # 2026-11-12: the nflverse roster file is stamped with its release time but trails real moves by a day or more
        # (Nick Folk waived 11/11, roster still ACT on 11/12). A release, IR or suspension in the transaction feed inside
        # the 60 hours before the roster stamp wins, unless a newer ESPN note has him active again.
        if top.source == "NFLV_ROST" and top.category == "ACTIVE":
            txs = gg[gg.source == "ESPN_TX"]
            if len(txs) and txs.iloc[0].category in ("CUT", "IR", "SUSPENDED") and txs.iloc[0].asof_dt >= rw_lag:
                newer_ok = gg[(gg.source == "ESPN_INJ") & (gg.category == "ACTIVE") & (gg.asof_dt > txs.iloc[0].asof_dt)]
                if not len(newer_ok):
                    top = txs.iloc[0]
        cats = {}
        for r in gg.itertuples():
            if r.category != "NONE":
                cats.setdefault(r.category, []).append(f"{r.source} {r.status} @{r.as_of}")
        conflict = ""
        if len({CLASS[c] for c in cats if CLASS[c] != CLASS[top.category]}) > 0:
            conflict = " | CONFLICT: " + "; ".join(f"{c}: {', '.join(v)}" for c, v in cats.items())
        extra = "; ".join(f"{r.source}: {r.note}" for r in gg.itertuples() if r.source in ("NFLV_INJ", "MFL_ROSTER") and r.category == "NONE")
        # team: prefer the newest roster-type record
        team = top.team
        merged.append(dict(player=top.player, team=team, status=top.status, source=top.source, as_of=top.as_of,
                           note=(top.note or "") + conflict + (" | " + extra if extra else ""),
                           gsis_id=top.gsis_id if top.gsis_id == top.gsis_id else None, pos=top.pos, category=top.category,
                           roster_team=(trade_in[top.gsis_id][0] if top.gsis_id in trade_in
                                        else gsis_info.get(top.gsis_id, (None, None, None))[1]),
                           practice=next((str(r.note).split("practice '")[1].split("'")[0] for r in gg.itertuples()
                                          if r.source == "NFLV_INJ" and "practice '" in str(r.note)), ""),
                           play_prob=PLAY_PROB.get(top.category, 1.0), n_sources=len({r.source for r in gg.itertuples()})))
        # 2026-11-12 (FF-2026-11-12-01): a Questionable player who did not practice plays far less than 75 percent.
        # Three seasons, n=57: zero 53 percent of the time, 0.39 of his usual points. Limited and full stay at 0.75
        # (raising them to 0.85 made the backtest worse: MSE 65.2 flat, 64.0 with this rule, 68.8 with 0.85).
        if merged[-1]["category"] == "QUESTIONABLE" and str(merged[-1]["practice"]).startswith("Did Not"):
            merged[-1]["play_prob"] = Q_DNP_PLAY_PROB
    out = pd.DataFrame(merged).sort_values(["team", "player"])
    OUT.mkdir(parents=True, exist_ok=True)
    base = OUT / f"injuries_{season}_wk{week}"
    out.to_csv(str(base) + ".csv", index=False)
    df.drop(columns=["asof_dt", "key"]).to_csv(str(base) + "_allsources.csv", index=False)
    newest = max(pd.to_datetime(out.as_of, utc=True, errors="coerce").dropna())
    report["merged_rows"] = len(out)
    report["raw_rows"] = len(df)
    report["unresolved_gsis"] = int(out.gsis_id.isna().sum())
    report["newest_as_of"] = newest.strftime("%Y-%m-%dT%H:%MZ")
    report["age_hours_of_newest"] = round((now - newest).total_seconds() / 3600, 1)
    report["stale_over_24h"] = report["age_hours_of_newest"] > 24
    report["conflicts"] = int(out.note.str.contains("CONFLICT").sum())
    report["trades_in"] = {gsis_info[g][0] if g in gsis_info else g: t for g, (t, _w) in trade_in.items()}
    if check_franchise:
        report["espn_team_check"] = espn_team_check(check_franchise, out, mfl_by_id, ros, e2g)
    json.dump(report, open(str(base) + "_report.json", "w"), indent=1)
    print(json.dumps(report, indent=1))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("season", type=int)
    ap.add_argument("week", type=int)
    ap.add_argument("--tx-days", type=int, default=10)
    ap.add_argument("--check-franchise", default="0012", help="fantasy franchise whose players get the ESPN team check ('' to skip)")
    a = ap.parse_args()
    build(a.season, a.week, a.tx_days, a.check_franchise or None)
