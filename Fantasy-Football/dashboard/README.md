# Sunday Dashboard — Phase 1

Local-only. Runs on this PC, opens in a browser at `localhost:8787`.
Nothing hosted, nothing public, no credentials leave the machine.

Built from `..\SUNDAY-DASHBOARD-BUILD.md`. Phase 1 only — see that file
for what Phase 2/3 add later, once Phase 1 has run clean through a full
real Sunday.

## Run it (two terminals)

```
cd D:\WKP\Fantasy-Football\dashboard
python poller.py
```
```
cd D:\WKP\Fantasy-Football\dashboard
python server.py
```
Then open `http://localhost:8787` in a browser.

The poller only talks to MFL/ESPN when a game is actually live (checks
ESPN's scoreboard first). The browser never triggers a data pull —
refreshing the page just re-reads the last `state.json` the poller
wrote.

## One-off test run (no live game required)

```
python poller.py --once --force
```
Writes `state.json` immediately, ignoring the "only when games are
live" gate. Use this to sanity-check the page outside of a Sunday.

## Files

| File | Purpose |
|---|---|
| `poller.py` | Polls sources on a timer, writes `state.json` |
| `server.py` | Serves `static/` + `state.json` on localhost. Never pulls data itself. |
| `config.py` | Ports, paths, polling intervals — no secrets |
| `mfl_client.py` | MFL export-API calls, verified 2026-09-12 |
| `espn_client.py` | ESPN scoreboard/teams/RSS calls, verified 2026-09-12 |
| `pickem_card.py` | Parses the weekly `.xls` pick'em card |
| `team_match.py` | Matches card team names to ESPN team objects |
| `state.json` | Current snapshot the browser reads (regenerated, gitignored) |
| `.raw_cache.json` | Poller-internal raw API cache, not served (regenerated, gitignored) |

## Pick-marking convention — resolved 2026-09-13

Stale note removed 2026-09-17. Picks are marked by **filled cell
background color** on the favored/underdog cell — confirmed by Zac and
verified against the real submitted card (`D:\Documents\Pickups
2026\Sanders_Week{N} Entry.xls`, not the blank templates in
`Fantasy-Football\cards\`). Any non-default fill color counts as the
pick; the specific RGB varies by week/card and isn't the signal.
`pickem_card.py`'s `read_card()` already implements this. Re-verified
2026-09-17 against a real filled Week 2 control card
(`Sanders_Week 2P Entry.xls`) — 19/19 games parsed cleanly, one
consistent fill color, zero ambiguous rows. Full history in
`..\..\logs\DECISIONS.md` entry `FF-2026-09-12-01` (closed).

**Known real gap:** `read_card()` currently returns only 19 games — it
does not yet parse game 20 (Monday Night Football), which per Zac's
2026-09-16 correction is always a real scored pick, not a separate
tiebreaker-only entry. Needs a fix before this parser can be trusted
for the full 20-game card.

## Credentials

`MFL_API_KEY` from the environment only, same as `fantasy-football-data`
SKILL.md. Never written into any file here, never into `state.json`
(that file is served to the browser).

## Endpoints this depends on (verified 2026-09-12)

- MFL `liveScoring`, `playerScores`, `standings`, `projectedScores` —
  league host (`www44`), require `L=43094`.
- MFL `injuries` — **`api.myfantasyleague.com`, no `L=` param.** Calling
  it at the league host errors ("must go to api.myfantasyleague.com");
  calling `api.myfantasyleague.com` *with* `L=` redirects back to the
  league host in a loop. `playoffChances` from the build doc is **not a
  real TYPE** — confirmed via MFL's own error message listing every
  valid TYPE. `standings` is the one that actually works.
- MFL rate limit: **not published**, "not fixed and will vary" per
  MFL's own api_info page. Space requests ≥1 second apart minimum,
  expect a lower ceiling as an unregistered client, expect the ceiling
  to drop further during live games, back off on 429 rather than retry.
  `config.MFL_LIVE_POLL_SECONDS` (default 90s) is a wide-margin guess
  given that, not a number MFL confirmed.
- ESPN `site.api.espn.com` (scoreboard, teams, CFB scoreboard) — **no
  custom User-Agent header.** This project's own descriptive UA gets a
  403; no UA or a generic one works fine.
- ESPN `www.espn.com` RSS feed — sits behind an AWS WAF bot challenge
  that blocks Python's `requests` regardless of UA (TLS fingerprint,
  not header-based) but never blocks `curl`. `espn_client.news_headlines()`
  shells out to `curl` for this one call.
