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

## DFS week view (added 2026-11-19)

The DFS panel now reads Zac's DraftKings week folders, `D:\Draft Kings\Week N\` (set `DFS_DK_ROOT` to point it somewhere else for testing). It never connects to DraftKings, never logs in, never enters a lineup or spends. It moves, renames and deletes nothing in `D:\Draft Kings`. Code: `dfs_week.py`, `static\dfs_week.js`. Endpoints: `GET /api/dfs/weeks`, `GET /api/dfs/week?n=11`, `POST /api/dfs/manual`.

**Which week:** the dropdown lists every `Week N` folder, newest first, and opens on the latest one. The week in `state.json` is marked "(this week)", older weeks "(archive)".

**Files it looks for inside the week folder (top level and one subfolder down):**

| What | Pattern | Notes |
|---|---|---|
| Lineups (entries) | any `.csv` whose first column header is `Entry ID` and that has a `Contest ID` column, e.g. `DKEntries_week11_template - FILLED.csv` | Pick order: a name with `FINAL` in it, then a name with `FILLED`, then any other (the blank template). Newest wins inside a tier. The panel shows which file it used and lists the others. To lock the final set, save it as e.g. `DKEntries_week11 FINAL.csv`. |
| Player names, teams, salary | `DKSalaries*.csv` | Then any csv with `Name` plus `DFS ID` (or `ID` plus `Salary`) as a backup, then the salary block DraftKings prints on the right of the entries file. |
| Score and place | `contest-standings-*.csv` or `contest-standings-*.zip`, or any csv/zip with `standings` in the name | DraftKings GameCenter "Export Lineups to CSV". Columns used: `Rank, EntryId, EntryName, TimeRemaining, Points, Lineup` plus the right-side block `Player, Roster Position, %Drafted, FPTS`. A zip is read in place, not unpacked. Several contest files can sit side by side. |
| Typed results | `manual-results.json` | The only file the dashboard writes in the week folder. Previous copy kept as `manual-results.json.bak`. |

Skipped everywhere: any file or subfolder with `FAKE`, `MOCK`, `dryrun`, `smoketest` or `NEGATIVE_TEST` in its name.

**Status per entry:** `BUILT, NOT CONFIRMED ENTERED` until proof shows up. `IN CONTEST (standings file)` when the entry's Entry ID is in a standings export. `IN CONTEST (typed by hand)` when points and place were typed. If the standings file lineup is not the same nine players as the built file, the card says so and shows the lineup that is actually in the contest.

**Score and place shown:** points, place out of total entries (total = rows with an EntryId in that export), top x percent (place divided by total), time left as DraftKings gives it, and per player points and percent drafted when the export has them. A live export is unofficial live scoring at the moment it was downloaded.

**How Zac gets the standings file (from DraftKings help pages, checked 2026-11-19, not tested by us):** on a computer or mobile web browser, not the DraftKings app. Open the contest in GameCenter, then click **Export Lineups to CSV** under Standings. Available once the contest locks, also while it is live. Save the download into that week's folder. Leave the name DraftKings gives it if it starts with `contest-standings`; otherwise add the word `standings` to the name.

**Typed fallback:** "Type points and place by hand" under the entries. Pick the entry, type points, place, total entries, time left, who typed it (Zac, or Jarvis from a screenshot Zac sends). The Entry ID must be in that week's entries file. A standings file, when present, wins over a typed result.

## DFS Entries panel (added 2026-11-13, now the archive)

Moved under "Old tracker (before week folders, archive only)" at the bottom of the DFS panel, collapsed. Nothing deleted. The friend and A/B/C lines from 11/13 and 11/15 only show there.


A panel at the bottom of the page records Zac's DraftKings entries. The dashboard never enters a lineup, never spends, never contacts DraftKings. It reads and writes `..\tracker\dfs_tracker.csv` through `dfs_entries.py`.

**Start it (DFS only, no poller):**
```
cd D:\WKP\Fantasy-Football\dashboard
set DASHBOARD_NO_POLLER=1
python server.py
```
Open `http://localhost:8787`. Leave `DASHBOARD_NO_POLLER` unset on a real Sunday and server.py starts the poller as before. Other settings: `DASHBOARD_PORT` (default 8787), `DFS_TRACKER_PATH` and `DFS_BACKUP_DIR` (point at a copy for testing), `DFS_BANKROLL` (default 3.00).

**What it shows:** each entry's slate, line (our A/B/C, friend 1/2/3, or own), contest name or id, entry fee, status (entered or not entered), the nine names, actual points, rank, profit or loss. Above the table: bankroll ($3), spent (fees on entered rows), reserved (fees set on rows not yet entered), left. A row with no fee counts for nothing.

**Add or edit:** open "Add or edit an entry". Pick a line, press "Fill names from the chosen line" (reads our three and the friend's three from `D:\WKP\data\dfs-friend\`), set fee and status, Save. After the slate use Edit on the row to type points, rank, profit or loss. Every save copies the csv to `..\tracker\backups\dfs_tracker_<timestamp>.csv` first, then replaces the file in one step. Editing a row changes only the fields the form sends. Our A/B/C rows use the ids OA/OB/OC and the friend's F1/F2/F3, the same ids `dfs\dfs_review.py` uses, so one row per lineup. New own lineups get OWN-1, OWN-2 per date.

**Columns added to dfs_tracker.csv:** `line_label`, `lineup_players` (nine names joined by " | "), `status`. Rank uses the existing `finish` column. `dfs_review.py` COLS was extended with the same three so it no longer drops them when it rewrites the file.

**Safety:** the server binds to 127.0.0.1, accepts POST only from localhost on `/api/dfs`, caps the body at 20 KB.
