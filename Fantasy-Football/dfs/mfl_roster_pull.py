"""python mfl_roster_pull.py <week> <outdir>   (copied 2026-11-19 from the Week 11 Thursday pull so the DK refresh step can run it)
Thursday pulls: MFL roster (mine), saved starters for me (0012) and the opponent, ESPN current team for every rostered player.
Read-only. Keys come from the environment and are never printed."""
import json, sys, time
import requests
sys.path.insert(0, r"D:\WKP\Fantasy-Football\dashboard")
import mfl_client as m
B = sys.argv[2] if len(sys.argv) > 2 else r"D:\WKP\scratch\mfl"
W = int(sys.argv[1])
import os; os.makedirs(B, exist_ok=True)
cache = json.load(open(r"D:\WKP\.claude\skills\fantasy-football-data\players-cache-details.json"))
byid = {p["id"]: p for p in cache["players"]["player"]}
inj = m.injuries()
injmap = {i["id"]: (i.get("status"), i.get("details")) for i in inj.get("injuries", {}).get("injury", [])}
pmap = {p["id"]: p.get("score") for p in m.projected_scores(W)["projectedScores"]["playerScore"]}


def rows_for(fid):
    ros = m.rosters(fid)["rosters"]["franchise"]
    ros = ros["player"] if isinstance(ros, dict) else ros[0]["player"]
    rows = []
    for r in ros:
        p = byid.get(r["id"], {})
        rows.append((p.get("position"), p.get("name"), p.get("team"), r["status"], r["salary"], r["contractYear"],
                     pmap.get(r["id"]), injmap.get(r["id"], ("", ""))[0], r["id"], p.get("espn_id")))
    rows.sort(key=lambda x: (str(x[0]), -(float(x[6]) if x[6] else 0)))
    return rows


mine = rows_for("0012")
json.dump(mine, open(B + r"\thu_roster.json", "w"))
print("my roster rows:", len(mine))
wr = m._get(m.MFL_HOST, "weeklyResults", {"L": m.MFL_LEAGUE_ID, "W": str(W)})
json.dump(wr, open(B + r"\thu_weeklyResults.json", "w"))
lv = m._get(m.MFL_HOST, "liveScoring", {"L": m.MFL_LEAGUE_ID, "W": str(W)})
json.dump(lv, open(B + r"\thu_liveScoring.json", "w"))
opp = None
st = {}
for mt in lv["liveScoring"]["matchup"]:
    ids = [f["id"] for f in mt["franchise"]]
    if "0012" in ids:
        opp = [i for i in ids if i != "0012"][0]
        for f in mt["franchise"]:
            st[f["id"]] = [p["id"] for p in f["players"]["player"] if p["status"] == "starter"]
st2 = {}
for mt in wr["weeklyResults"]["matchup"]:
    for f in mt["franchise"]:
        if f.get("id") in ("0012", opp):
            st2[f["id"]] = [p["id"] for p in f["player"] if p["status"] == "starter"]
print("opponent franchise:", opp)
for fid in ("0012", opp):
    print(fid, "liveScoring starters", len(st.get(fid, [])), "| weeklyResults starters", len(st2.get(fid, [])), "| agree:", set(st.get(fid, [])) == set(st2.get(fid, [])))
    print("   " + "; ".join(f'{byid.get(i, {}).get("name", i)} ({byid.get(i, {}).get("position", "?")} {byid.get(i, {}).get("team", "?")})' for i in st.get(fid, [])))
json.dump([byid[i]["name"] for i in st["0012"]], open(B + r"\thu_saved_sheet.json", "w"))
opp_rows = rows_for(opp)
json.dump(opp_rows, open(B + r"\thu_opp_roster.json", "w"))
json.dump({"opp": opp, "mine": st["0012"], "theirs": st[opp]}, open(B + r"\thu_starters.json", "w"))

# ESPN current team per rostered player (catches trades the MFL team tag misses)
out = []
for pos, name, nfl, status, sal, cy, proj, injs, mid, espn in mine:
    if not espn:
        out.append((name, nfl, None, "no espn id")); continue
    try:
        r = requests.get(f"https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/athletes/{espn}", timeout=20)
        a = r.json().get("athlete", {})
        t = (a.get("team") or {}).get("abbreviation")
        stt = (a.get("status") or {}).get("name")
        out.append((name, nfl, t, stt))
    except Exception as e:
        out.append((name, nfl, None, f"not retrieved: {type(e).__name__}"))
    time.sleep(0.25)
json.dump(out, open(B + r"\thu_espn_teams.json", "w"))
FIX = {"GBP": "GB", "NOS": "NO", "TBB": "TB", "KCC": "KC", "NEP": "NE", "LVR": "LV", "SFO": "SF", "LAR": "LAR", "WAS": "WSH", "JAC": "JAX"}
print("\nESPN team check (only mismatches and failures):")
for name, nfl, t, stt in out:
    if t is None or FIX.get(nfl, nfl) != t:
        print(f"   {name}: MFL says {nfl}, ESPN says {t} ({stt})")


