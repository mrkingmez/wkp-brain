"""Pull NFL + college spreads/totals from The Odds API into one JSON file (same shape run_week.py reads).

python fetch_odds.py <out.json>
Key comes from the ODDS_API_KEY environment variable only. It is never printed or written to disk.
"""
import json
import os
import sys

import requests

key = os.environ.get("ODDS_API_KEY")
if not key:
    raise SystemExit("ODDS_API_KEY not set: not available")
out = {}
for sport in ("americanfootball_nfl", "americanfootball_ncaaf"):
    r = requests.get(f"https://api.the-odds-api.com/v4/sports/{sport}/odds",
                     params=dict(apiKey=key, regions="us", markets="spreads,totals", oddsFormat="american"), timeout=30)
    r.raise_for_status()
    out[sport] = r.json()
    print(sport, len(out[sport]), "games | requests remaining:", r.headers.get("x-requests-remaining"))
json.dump(out, open(sys.argv[1], "w"), indent=1)
print("saved", sys.argv[1])
