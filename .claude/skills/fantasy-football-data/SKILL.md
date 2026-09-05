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
```
https://{MFL_HOST}.myfantasyleague.com/{MFL_YEAR}/export?TYPE=rosters&L={MFL_LEAGUE_ID}&APIKEY={MFL_API_KEY}&JSON=1
```
Returns every franchise's roster by numeric player ID, salary,
contractStatus, contractYear, and status (ROSTER / TAXI_SQUAD /
INJURED_RESERVE). Franchise 0012 is Caerellius Lions.

## Player ID map
```
https://{MFL_HOST}.myfantasyleague.com/{MFL_YEAR}/export?TYPE=players&L={MFL_LEAGUE_ID}&APIKEY={MFL_API_KEY}&JSON=1
```
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
