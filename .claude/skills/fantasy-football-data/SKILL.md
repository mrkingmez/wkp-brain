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