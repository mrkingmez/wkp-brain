# College football data sources for the pick'em card
Date: 2026-11-11. Owner: software-director, bench: data-sourcing. Read-only research. No accounts, keys, downloads or spend.
Labels: OBSERVED = fetched and saw 2026 data. SECONDARY = read about it, not fetched. NOT RETRIEVED = missing, reason named.

## Part 1. What went wrong

| Item | Verdict | Evidence |
|---|---|---|
| `mcp__espn__*` tools reject college | Simply unsupported by the connector (nfl, nhl, nba only). Not a bug. | Given by Jarvis. |
| `www.espn.com/college-football/injuries` 404 | Page does not exist at that URL. Wrong guess. Also www.espn.com robots.txt disallows Anthropic-named crawlers, so HTML pages are the wrong door anyway. | Given, plus bench robots.txt read. |
| WebSearch returned old seasons | Search is not a data feed. Never built a proper source. | Given. |
| Odds API for college | WORKS. `ff-simulator\scripts\fetch_odds.py` pulls `americanfootball_ncaaf` with regions=us, markets spreads,totals. The Week 10 file `data\fantasy-wk10-odds-2026-11-11-wed.json` holds 74 CFB games (kickoffs 11/12 to 11/22), 9 books: DraftKings (74 games), FanDuel (68), BetMGM (64), Bovada (64), MyBookie.ag (64), BetRivers (61), BetOnline (61), LowVig (59), BetUS (57). OBSERVED in the file. | Current line only. No history, no injuries. |
| ff-simulator, nfl-data skills | NFL only. No college string anywhere in their code or SKILL.md (grep of all three skills: only fetch_odds.py and the data skill's SKILL.md mention CFB). Never built for college. | Grep. |
| fantasy-football-data skill | Mentions CFB odds (Odds API) and the ESPN CFB scoreboard (`groups=80`) for scores only. No injury, depth, QB or stats pull. Never built. | SKILL.md lines 3, 39, 147. |
| Repo scripts | `tracker\espn_games.py` and `dashboard\espn_client.py` already call `site.api.espn.com/.../college-football/scoreboard` for scores and grading (ATS only, added 2026-10-21). That call works (bench saw 200 for 2026). Used for results, not for pre-game research. | Code and bench test. |
| Director log | `logs\fantasy-football-director.md` has no college entry at all. Week 10 report line 57 states "College games have no injury, odds-history or sim data beyond the 9-book line." Fantasy CLAUDE.md says college has no market data in the tracker, so always NO EDGE. | Grep. |

Truly broken: nothing in the scripts. The ESPN injuries endpoint is stale (below), which is ESPN's gap, not ours.
Never built: any college injury, starting QB, depth, stats or lines-history collection. The Week 9 and Week 10 reports only compared two Odds API snapshots by hand.

## Part 2. Sources tested

### ESPN unofficial JSON (site.api.espn.com and sports.core.api.espn.com)
- OBSERVED 200, season 2026 week 11: scoreboard. `?dates=20261107&groups=80&limit=200` gave 51 events (week 10 finals). `?dates=20261114&groups=80&limit=200` gave 56 events, all 56 with odds.
- Odds in scoreboard JSON for upcoming games, e.g. Illinois at UCLA, DraftKings, UCLA -10, O/U 47.5, open -12.5. Odds vanish once a game is final (51 finals had 0 odds). So lines history must be self-saved each Wed and Thu.
- Scoreboard `leaders` present (pass, rush, receive yards). `probables` empty.
- `/summary?event=<id>`: 200, boxscore, leaders, pickcenter, againstTheSpread, predictor. `injuries` is null.
- Rosters `/teams/<id>/roster`: 200, season 2026, class year, position, jersey. Per-athlete `injuries` empty for UCLA. Rankings (CFP, AP, Coaches): 200.
- Core `seasons/2026/types/2/weeks/10/events`: 200, 16 events. `seasons/2026/athletes`: about 103,740.
- Injuries: `/teams/130/injuries` returned `{}`. Site `/injuries` returned 3 teams with 2020 and 2022 dates (stale). Core injuries 404. Depth charts: 400 "not supported for college-football 2026".
- Cost, key: free, no key. Rate limit: none published (NOT RETRIEVED).
- Terms: no published terms cover these API hosts. Disney Terms of Use was fetched and a text search found no scraping or automated-access language (inconclusive). www.espn.com robots.txt disallows GPTBot, anthropic-ai, CCBot and similar by name; it does not cover the API hosts, whose own robots.txt was NOT RETRIEVED. Verdict: unofficial and undocumented, legally unclear. Low volume, personal use, about 20 calls a week, repo already does this for scores.

### CollegeFootballData.com (CFBD)
- `api.collegefootballdata.com/games?year=2026&week=10` returned 401, key required. 2026 data NOT RETRIEVED.
- Free key: `collegefootballdata.com/key`, email only, no card. Free tier 1,000 calls a month. Tier 2 is 30,000 calls via Patreon (price NOT RETRIEVED).
- Terms (collegefootballdata.com/terms, effective 2026-08-12, OBSERVED): commercial use allowed, caching and scheduled polling encouraged, scraping and excessive polling prohibited, redistribution of raw data as a dataset prohibited. Our use fits.
- Endpoints: OpenAPI paths tried returned 404. Lines, stats, roster coverage SECONDARY (from memory: /lines, /stats, /roster, /games/players; no injuries, no depth). Unverified.

### NCAA data
- `data.ncaa.com/casablanca/...` guessed path 404. Third-party `ncaa-api.henrygd.me` returned 200 with 63 week-10 games and box scores (OBSERVED), limit 5 requests per second. Scores and box scores only. ncaa.com terms NOT RETRIEVED. Redundant with ESPN.

### sports-reference.com/cfb
- 403 Cloudflare challenge (OBSERVED). Bot policy: max 20 requests a minute, no API. Do not scrape. Paid Stathead price NOT RETRIEVED.

### Conference availability reports
- SECONDARY only (one web search): Big Ten requires reports Wed, Thu, Fri by 8 pm ET plus a final 2 hours before kickoff. SEC publishes a Wednesday night initial report. Aggregators (Roundtable.io, Saturday Down South, RotoBaller) repost them.
- Official pages and machine-readable format NOT RETRIEVED. Big 12 and ACC NOT RETRIEVED. No feed found. This is the best injury signal but is a manual lookup today.

### CBS, Yahoo, 247Sports, On3, Rivals
- CBS injuries page 200, titled 2026-27, but static HTML had no rows (script-loaded). robots.txt does not disallow the path; GPTBot disallowed. CBS terms NOT RETRIEVED. Yahoo 200 but no injury list in HTML. 247Sports gated by bot challenge. On3 robots permits general access; its injury content NOT RETRIEVED. None usable as a feed.

### The Odds API
- Sport keys `americanfootball_ncaaf` and `americanfootball_ncaaf_fcs` exist. Already working in this repo (Part 1).
- Historical odds paid only. Pricing page (OBSERVED): Starter free 500 credits a month; 20K plan $30 a month with historical; 100K $59; 5M $119; 15M $249. Per-call credit cost and ToS NOT RETRIEVED. Zac's current plan tier not known to me.

### Other
- `sportsdataverse/cfbfastR-data` on GitHub: updated 2026-11-09 (OBSERVED via API), play-by-play and schedules, good for modeling backtests. File contents and license NOT RETRIEVED. Paid feeds (SportsDataIO etc.): NOT examined.

## Ranking for 6 games a week, Wed and Thu
1. ESPN site and core JSON. Free, keyless, OBSERVED 2026: schedule, results, odds with open and current line, rankings, rosters, box-score leaders. Needs a weekly self-saved snapshot for lines history. Caveats: no usable injuries or depth, unofficial status.
2. CFBD API. Free key, official, terms read and compatible. Likely adds team stats, lines history and player game stats. Coverage unverified until a key exists.
3. The Odds API (already in use). Keep as the 9-book line source and the cross-check against ESPN odds. Historical needs the $30 a month plan, not recommended for 6 games.

Gap that nothing fills: injuries, starting QB changes, depth charts. Practical route today: conference availability reports and news items, read by a person or by the director with WebSearch aimed at the Wednesday and Thursday reports, labeled SECONDARY.

## Proposed build (not started, Jarvis decides)
Small `cfb_snapshot.py` in the fantasy tools folder: for the pick'em dates, fetch ESPN scoreboard (groups=80), save open and current line, ranking, leaders to `data\cfb\cfb-<date>.json`. About 20 calls a week. Add last week's passing leader per card team as a QB-change flag. Queued as decision SW-2026-11-11-01.

## What Zac must do
- Nothing required. Optional: request a free CFBD key at collegefootballdata.com/key (email only) and set it as an environment variable, then the bench verifies coverage. Decide whether the unofficial ESPN API is acceptable (it already is for scores).
