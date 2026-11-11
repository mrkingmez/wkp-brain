"""Fix 4: read the SAVED MFL lineup for franchise 0012 through the read-only API (no writes).
    python -I read_saved_lineup.py [week]
Uses TYPE=liveScoring (status 'starter' per player) and cross-checks TYPE=weeklyResults. Finding 2026-11-10: both return the saved starters
for the CURRENT week as soon as the week is open (Tuesday), W=10 returned 17 starters. NOT yet verified: whether a lineup EDITED on Thursday morning
shows up here before kickoff (the earlier Week 9 Thursday attempt reported nothing). Test that Thursday and trust the screenshot over this if they differ.
TYPE=lineup, myfranchise, lockedLineup and franchises are rejected by this key/host ('Invalid request')."""
import json, os, sys, urllib.request
from pathlib import Path
key=os.environ["MFL_API_KEY"]; w=sys.argv[1] if len(sys.argv)>1 else "10"
det={p["id"]:p for p in json.load(open(r"D:\WKP\.claude\skills\fantasy-football-data\players-cache-details.json",encoding="utf-8"))["players"]["player"]}
def get(t): return json.loads(urllib.request.urlopen(f"https://www44.myfantasyleague.com/2026/export?TYPE={t}&L=43094&APIKEY={key}&JSON=1&W={w}",timeout=60).read().decode("utf-8-sig"))
st={}
lv=get("liveScoring")["liveScoring"]; 
for m in lv["matchup"]:
    for f in m["franchise"]:
        if f.get("id")=="0012": st["liveScoring"]=[p["id"] for p in f["players"]["player"] if p["status"]=="starter"]
wr=get("weeklyResults")["weeklyResults"]
for m in wr["matchup"]:
    for f in m["franchise"]:
        if f.get("id")=="0012": st["weeklyResults"]=[p["id"] for p in f["player"] if p["status"]=="starter"]
for k,v in st.items():
    print(k,len(v),"starters:"); print("  "+"; ".join(f'{det.get(i,{}).get("name",i)} ({det.get(i,{}).get("position","?")} {det.get(i,{}).get("team","?")})' for i in v))
print("sources agree:",set(st.get("liveScoring",[]))==set(st.get("weeklyResults",[])))
