---
name: fantasy-football-data
description: Pulls live data for Zac's IRFL dynasty league and pick'em pool — MFL roster/player exports and current NFL/CFB odds. Use when the fantasy-football-director agent needs fresh roster status, player ID lookups, or a current line pull, or when Zac directly asks to "pull my roster", "check the odds", or "refresh my fantasy data". Read-only against both APIs; never writes to MFL or submits anything.
---

# Fantasy Football Data

## Config (safe to keep in plain text — not secret)
- MFL_HOST = www44
- MFL_LEAGUE_ID = 43094
- MFL_YEAR = 2026
- MFL_FRANCHISE_ID = 0012 (Caerellius Lions)

## Credentials (env vars only — see SETUP-TOKENS.md, never hardcode)
- MFL_API_KEY
- ODDS_API_KEY

## Roster pull
https://{MFL_HOST}.myfantasyleague.com/{MFL_YEAR}/export?TYPE=rosters&L={MFL_LEAGUE_ID}&APIKEY={MFL_API_KEY}&JSON=1
Returns every franchise's roster by numeric player ID, salary,
contractStatus, contractYear, and status (ROSTER / TAXI_SQUAD /
INJURED_RESERVE). Franchise 0012 is Caerellius Lions.

## Player ID map
https://{MFL_HOST}.myfantasyleague.com/{MFL_YEAR}/export?TYPE=players&L={MFL_LEAGUE_ID}&APIKEY={MFL_API_KEY}&JSON=1
Large, mostly-static file — every player MFL tracks, with id, name,
position, and current NFL team. Cache this locally (`players-cache.json`
in this skill's folder) and only re-pull if a roster ID doesn't resolve,
or once a week during the season to catch trades/signings. Don't re-pull
it on every call — it rarely changes.

## What MFL will NOT give you
Raw player stats (passing yards, tackles, etc.) are blocked by MFL's own
licensing terms — this is deliberate on their end, not a bug or a gap to
route around. For box scores, ask Zac for a screenshot of MFL's live-
scoring page and read the numbers off that.

## Odds pull
Current NFL and CFB spreads via The Odds API. Two paths depending on
where this is running:
- **In Claude chat**: use the connected Composio `the_odds_api` toolkit.
- **In Claude Code / local scripts**: call directly with `ODDS_API_KEY`
  as a query param or header per The Odds API's own docs — check
  api.the-odds-api.com/v4 endpoints for the current spec, since their
  API version can change.

Compare against Zac's uploaded Monday card. A line that's moved 2+
points from his frozen number is the signal to flag.

## Network note (chat environment only)
`web_fetch` in the chat interface cannot reach myfantasyleague.com
directly (domain not on the allowlist, and it also blocks robots).
When running from chat rather than Claude Code, ask Zac to paste the
URL into his browser and return the raw output — same workaround
already in use for this league.

## Pick'em card structure
The weekly card (an .xls file Zac uploads, saved to
`Fantasy-Football\cards\`) is not just 20 ATS games. Every card has
three parts, and they resolve on different timelines — don't conflate
them:

1. **20-game ATS pool** — the recurring weekly pick, spread across
   however many game-days that week has. Normally locks at Thursday
   kickoff; deviates when the NFL schedule deviates (Week 1 2026 is a
   Wednesday opener, so that week's lock moved up a day — always check
   the actual date on the card rather than assuming Thursday).
2. **Eliminator Challenge (EC)** — a single team picked each week,
   marked with an X in a yellow box next to that team on the card.
   Season-long survivor-style side pool, separate scoring from the ATS
   pool. Track picks week-to-week in case the pool disallows repeat
   picks — confirm the actual rule with Zac before assuming either way.
3. **Season-long futures (Week 1 card only, this season)** — Super Bowl
   winner, all 14 playoff seeds (7 AFC + 7 NFC), and the final NCAA CFP
   top 12 in exact predicted order. These do not resolve weekly. They
   resolve at season's end. Do not try to grade them against weekly
   results — they live in `FUTURES-PICKS.md` in the venture folder,
   checked only once real playoff seeding / CFP rankings / a Super Bowl
   winner actually exist.

The card also carries a point-value table for Super Bowl winner picks
(longshot teams score more if correct than favorites). Read that table
directly off whichever card carried it — don't assume it's the same
every season.

## Where picks actually get entered
Directly into the card file itself — the blank cells adjacent to each
label are the input fields (yellow-box legend on the card explains
this). Never build a parallel answer sheet; the card *is* the record.

## Sleeper (no key, read-only, free for non-commercial use)

Base: `https://api.sleeper.app`

**Current week and season state** — call this first, every session.
Everything else keys off it.
```
GET https://api.sleeper.app/v1/state/nfl
```
Returns season, week, season_type, display_week.

**Player metadata map** — large payload, roughly five megabytes.
```
GET https://api.sleeper.app/v1/players/nfl
```
Cache as `sleeper-players-cache.json`. Re-pull weekly at most, same
rule already in place for the MFL players cache. Never pull this
mid-session for a single lookup.

**Weekly projections** — undocumented endpoint, works, no auth.
```
GET https://api.sleeper.app/projections/nfl/{season}/{week}
    ?season_type=regular
    &position[]=QB&position[]=RB&position[]=WR&position[]=TE
    &position[]=K&position[]=DEF
    &position[]=DL&position[]=LB&position[]=DB
```
Returns pts_ppr, pts_half_ppr, pts_std plus component stats
(pass_yd, rush_yd, rec, and so on). Use **pts_ppr** — the IRFL is
full PPR.

The last three position parameters are the IDP block. The league runs
eight defensive starters, so they are not optional here.

**Weekly actuals** — for recap mode and for checking projection error.
```
GET https://api.sleeper.app/v1/stats/nfl/regular/{season}/{week}
```

**Season stats for one player**
```
GET https://api.sleeper.app/stats/nfl/player/{player_id}
    ?season_type=regular&season={season}
```

### ESPN public site API (no key, no auth)

Base: `https://site.api.espn.com/apis/site/v2/sports/football`

**Pro scoreboard** — current week if no parameters given.
```
GET .../nfl/scoreboard
GET .../nfl/scoreboard?seasontype=2&week={n}&dates={year}
```
Returns matchups, kickoff times, live and final scores, and status.

**College scoreboard** — `groups=80` limits to FBS, which is what the
pick'em card pulls from.
```
GET .../college-football/scoreboard?groups=80&limit=200
```

**Teams**
```
GET .../nfl/teams
```

## Player ID mismatch — the real work

MFL player IDs and Sleeper player IDs are **different numbering
systems**. A roster pull gives MFL IDs. A projection pull gives Sleeper
IDs. Nothing joins them out of the box.

Two paths, try in this order:

1. **Cross-reference IDs.** MFL's players export accepts `&DETAILS=1`,
   which returns third-party IDs on each player record. Sleeper's
   player objects carry `espn_id`, `gsis_id`, `rotowire_id`,
   `sportradar_id`, and others. If both sides expose the same
   third-party ID, join on that. Build the map once, save it as
   `id-bridge.json`, and reuse.

2. **Name plus position plus team fallback.** Normalize case, strip
   punctuation and suffixes (Jr, III, periods). Use only for players
   the ID bridge misses.

**Do not silently drop players that fail to match.** Write unmatched
players to a `unmatched.log` and surface the count to Zac. A lineup
call built on a roster where four IDP players quietly vanished is
worse than no lineup call.

### Verify before trusting, do not assume

These are undocumented or lightly documented endpoints. Confirm each
one returns real data before writing logic on top of it:

- Sleeper **IDP projections**. Sleeper accepts DL, LB, and DB
  positions, but IDP projection quality is thinner than offensive
  skill positions. Pull one week, eyeball it against a known
  high-tackle linebacker, and report whether the numbers look real.
  If IDP projections come back empty or obviously junk, say so — the
  optimizer needs to fall back to recent-usage ranking for those
  eight defensive slots rather than pretending it has projections.
- Sleeper **depth chart** endpoint. Referenced in third-party wrappers,
  not in official docs. Verify the URL shape before using it.
- ESPN **injury** data. Some team endpoints carry injury fields, some
  do not. Confirm before wiring it to anything.

### Rate limits

Neither source publishes limits. Both are free and unofficial and can
change or break without notice. Cache aggressively, pull once per
session, and fail loudly rather than retrying in a loop.

### Scope note

Do **not** install any of the "ESPN Fantasy Football MCP" servers on
GitHub. Every one of them targets ESPN-hosted leagues and wants
`espn_s2` and `SWID` cookies plus an ESPN league ID. The IRFL is on
MyFantasyLeague. They provide nothing here. Only ESPN's public *sports*
API is in scope, and that is a different service with no auth.