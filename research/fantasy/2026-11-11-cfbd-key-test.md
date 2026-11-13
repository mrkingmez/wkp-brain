# CFBD key test, 2026-11-11

Tested by data-sourcing. Key read from user env var CFBD_API_KEY in code only. It is not printed or saved anywhere. Calls used: 8 of the 10 budget. The server header showed 994 remaining after the 6th call, so the 1,000 a month counter matches. About 992 should be left.

Base: https://api.collegefootballdata.com, header `Authorization: Bearer <key>`. Auth works (HTTP 200 on every real endpoint).

## What I retrieved
| Endpoint | Result for 2026 |
|---|---|
| /calendar?year=2026 | 200, 16 weeks. Current week 11 = Nov 9 to Nov 16 (CFBD week numbering, not the pick'em card's Week 10). |
| /games?year=2026&week=11&classification=fbs | 200, 67 games, game ids, start times, completed flag, pregame Elo. |
| /lines?year=2026&week=11 | 200, 67 games with lines. DraftKings and Bovada, spread, spreadOpen, overUnder, overUnderOpen, moneylines. |
| /ratings/sp?year=2026&team=Oregon | 200, returns real rating and rank (Oregon rating 16.9, rank 1; offense 34.3, defense 17.8, special teams 0.3). Sub-fields (success, explosiveness, rushing, passing, havoc, sos) all null. Returned 2 rows (team plus a second row, not inspected). |
| /stats/season?year=2026&team=Oregon | 200, 63 stat rows (e.g. firstDowns 183). Team season totals. |
| /player/usage?year=2026&team=Oregon | 200, 23 players with usage share overall, pass, rush, by down. Example: Evan Stewart WR overall 0.096, pass 0.173. |
| /injuries | 404 "Cannot GET". No such endpoint. |
| /depth | 404 "Cannot GET". No such endpoint. |

Not tested to save calls: other teams' SP+ and usage, /player/season stats, /ratings/elo, /ratings/fpi, /metrics/wp, /game/box/advanced. The OpenAPI schema (api-docs.json) lists PlayerUsage and TeamSeasonPlayerUsage, and I saw no injury or depth chart schema in the first 100,000 of 284,974 characters. I did not read the rest, so this is not a full-schema confirmation.

## Zac's six card games
I could not find the six-game list for the card in the repo (the cfb json and snapshot script do not mark it), so I checked ten Week 11 games from the ESPN snapshot to prove coverage. CFBD has all ten with ids and lines. Examples (CFBD sign: negative spread = home favored):
- Michigan @ Oregon 401858523: DK Oregon -10.5, total 38.5; Bovada -11, 38.
- Missouri @ Georgia 401856883: DK -15.5, 47.5.
- Northwestern @ Ohio State 401858522: DK -14, 44.5; Bovada -13.5, 44.5.
- Florida State @ Pittsburgh 401858293: DK Pitt -3.5, 53.5; Bovada -3.5, 53.
- Also found with ids: Memphis @ South Florida, Illinois @ UCLA, Houston @ Colorado, Nebraska @ Rutgers, Alabama @ Vanderbilt, Tennessee @ Texas A&M.
If Jarvis gives me the six names, the ids are a free lookup from the 67-game list (no extra call needed, it is one cached pull).

Cross-check: DraftKings numbers match the ESPN snapshot on the games compared (Georgia, Ohio State, Pitt, Oregon). Sign convention differs: the snapshot uses positive spread_home = home favored, CFBD uses negative = home favored. Flip before comparing.

## Terms on caching (read 2026-11-11, https://collegefootballdata.com/terms)
- Allowed: privately cache, store, normalize and retain API responses. Server-side caching and scheduled polling are encouraged. Data kept from active access can stay in a private corpus after a subscription ends.
- Not allowed: selling, publishing or giving anyone bulk or standalone access to the data, public mirrors or proxies, giving others access to stored raw responses. Derived outputs (picks, models, predictions) are not covered by the restriction.
- Shared quota pool with CBBD. Excessive polling can get access suspended.
- Commercial use allowed. Attribution appreciated, not required: "Data provided by CollegeFootballData.com."
- Plain words: saving files in data\cfb\ for Zac's own picks is fine. Do not commit raw CFBD dumps to a public repo or share them. (wkp-brain visibility not checked, so keep raw CFBD files gitignored to be safe.)

## What cfb_snapshot.py should add
Budget: about 3 calls per snapshot (calendar is optional, cache it).
1. /games and /lines for the current CFBD week (2 calls). Adds a second line source, line open vs now, Bovada alongside DraftKings, and moneylines. The lines call also survives finals better than ESPN, which deletes odds once a game ends (verify before relying on it, not tested on finals).
2. /ratings/sp for the year (one call, no team filter returns all teams, not tested for size). Gives rating and rank per team. Treat as ratings only, sub-fields are null.
3. /player/usage, per team (one call per team, so expensive). Only fetch for teams in the card games, about 12 calls a week, or test whether the year-only call works first. Usage is share of plays, it is not injury or lineup status.
4. Optional weekly: /stats/season per team, only if the model uses it.
Keep the 'NO INJURY DATA' notice. CFBD has no injuries or depth chart, so injury and starting QB status still come from conference availability reports, labeled SECONDARY.
Monthly math: 3 calls x 7 days x 4.3 weeks is about 90, plus about 50 for usage. Well under 1,000.
Open flag: SP+ 2026 shows Oregon rank 1 with null subratings. Confirm the ratings are in-season updated and not preseason before the sim leans on them (not verified).
