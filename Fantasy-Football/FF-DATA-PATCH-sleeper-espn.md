# Fantasy Football Data Patch — Sleeper + ESPN public APIs

## DROP LOCATION
`D:\WKP\fantasy-football\` (alongside the venture CLAUDE.md)

## EXACT PHRASE FOR CLAUDE CODE
> Read FF-DATA-PATCH-sleeper-espn.md and apply it to the
> fantasy-football-data skill. Append the two new sections to the
> existing skill file — do not rewrite the MFL or Odds API sections.
> Then run the three verification calls at the bottom and report
> what actually came back.

---

## What this adds and why

The director agent currently has roster data (MFL) and betting lines
(Odds API). It has no player projections and no game state. That's the
gap. Two free sources fill it. Neither needs an API key, a signup, or a
credit card.

- **Sleeper** — weekly player projections, season and weekly stats,
  player metadata, injury status. This is the projection baseline the
  lineup optimizer was designed around but never got wired to.
- **ESPN public site API** — scores, schedules, game state for pro and
  college. This feeds the pick'em side and the recap mode.

Neither is wrapped as an MCP server on purpose. Both are plain
unauthenticated REST. An MCP wrapper would add a Python process, a
config file, and a failure point for zero capability gain.

---

## SECTION 1 — Append to `fantasy-football-data` skill

### Sleeper (no key, read-only, free for non-commercial use)

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

---

## SECTION 2 — The part that will break, read this first

### Player ID mismatch — the real work

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

---

## SECTION 3 — Verification calls

Run these three, report exactly what came back. Do not proceed to
wiring the director agent until all three are confirmed.

```
1. https://api.sleeper.app/v1/state/nfl
   Expect: current season and week as JSON.

2. https://api.sleeper.app/projections/nfl/2026/2?season_type=regular&position[]=RB&position[]=LB
   Expect: player-ID-keyed object with pts_ppr values.
   Report whether the LB entries have real numbers or empty fields.

3. https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard
   Expect: current week's games with teams and status.
```

If any call fails, report the actual status code and response body.
Do not substitute a different endpoint and continue.
