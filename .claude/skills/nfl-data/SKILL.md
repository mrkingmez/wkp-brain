---
name: nfl-data
description: Shared nflverse data layer — play-by-play, team/player stats, schedules with betting lines, cross-platform player ID mappings, and PFR advanced stats. Free, MIT licensed, no API key. Used by the fantasy football venture (EPA-based pick'em tiebreaker, IDP matchup data for the lineup optimizer) and, separately, an undecided sports-content venture (play-level angles). Read-only, never writes anywhere. Has NOTHING to do with WWD — do not wire it to any WWD agent or skill.
---

# NFL Data (shared infrastructure, not a venture skill)

Source spec: `NFL-DATA-LAYER-BUILD.md` at the repo root.

This lives outside every venture folder on purpose — two unrelated
consumers (fantasy football, sports content) read the same cached
files. Build once, both read from it. **Do not** apply WWD conventions,
naming, or style to anything this skill touches, and do not surface it
in WWD planning.

## Source

**nflverse** — `https://github.com/nflverse/nflverse-data/releases`.
Automated releases via GitHub Actions. Free, MIT licensed, no API key,
no account. `github.com` and `api.github.com` are both directly
reachable — no proxy workaround needed here (unlike myfantasyleague.com
in the fantasy-football-data skill).

## Rule zero: discover before you download

**Never hardcode a filename from this doc or from memory.** nflverse
renames and reorganizes release assets between seasons. Confirmed
2026-09-12: `stats_team` and `stats_player` files are split into
`_week_`, `_reg_`, and `_regpost_` variants per season — that shape is
not guessable from the release tag name alone, and next season's
convention is not guaranteed to match.

Every session, or whenever a download 404s, or at the start of a new
season:
```
python scripts/nfl_data.py discover --season 2026
```
This calls `GET https://api.github.com/repos/nflverse/nflverse-data/releases`,
reads the real asset list off every tracked release, and writes
`D:\WKP\data\nfl\nfl-data-manifest.json` with a discovery timestamp.
All downloads read from that manifest, never from a filename typed
into a script.

## The six tracked releases (tags on the nflverse-data repo)

| Tag | Holds | Season-specific? | Consumer |
|---|---|---|---|
| `pbp` | Play by play, ~136+ columns incl. EPA | Yes — `play_by_play_{season}.*` | Content |
| `stats_team` | Team stats, EPA included | Yes — split into `_week_`, `_reg_`, `_regpost_{season}.*` | Pick'em |
| `stats_player` | Player stats, week + season | Yes — same week/reg/regpost split | Both |
| `schedules` | Games, results, full betting lines | **No** — one rolling `games.*` file, all seasons, filter by `season` column | Both |
| `players` | Player info + cross-platform ID mappings | **No** — one rolling `players.*` file | Both |
| `pfr_advstats` | PFR advanced stats | Yes — split into `_pass_`, `_rush_`, `_rec_`, `_def_{season}.*` | Content |

**`player_stats` (no underscore split) is a different, separate release
tag from `stats_player`. Confirmed deprecated** — its own release body
reads "DEPRECATED 2025-08-01: USE `stats_player` OR `stats_team`
INSTEAD." Never pull from it. This skill only ever touches
`stats_player`.

## Format

**Use parquet where offered** — confirmed present on every tracked
release. A season of play-by-play is a few hundred KB to low-MB in
parquet against ~90MB+ in raw CSV for the same data. `scripts/nfl_data.py`
defaults every `get` call to whatever filename you ask for; ask for the
`.parquet` variant.

Reading parquet locally requires `pyarrow` (installed on this machine
2026-09-12 via `pip install pyarrow` against the LOCAL-PATHS python).
If this skill runs on a machine without it, install it first — pandas
alone cannot read parquet.

**Current season only by default.** Add prior seasons on demand by
passing a different `--season` to `discover`/`get`, never speculatively.

## Commands

```
python scripts/nfl_data.py discover --season 2026
python scripts/nfl_data.py list <tag>
python scripts/nfl_data.py get <tag> <filename-substring> --season 2026
python scripts/nfl_data.py age <cached-file-path>
```

`get` downloads to `D:\WKP\data\nfl\<tag>\<filename>` and writes a
`.meta.json` sidecar with the download timestamp, source URL, and the
source's own `updated_at` — this is what `age` reads to answer the
honesty-rule question below.

## Update cadence and the honesty rule

nflverse updates on an automated schedule after games are processed —
typically a day or more after games finish. **It is not live data.**

- Fine for: Tuesday/Wednesday analysis, weekly pick'em prep, anything
  built on completed games.
- Not usable for: same-night, in-game, or live state. Use the ESPN
  public scoreboard endpoint from the fantasy-football-data skill for
  that — different tool, different job, do not conflate them.

**Every consumer of this data must state its age** (`python
scripts/nfl_data.py age <path>`). If the newest file used is more than
ten days old, say the analysis is running on stale data — do not
present it as current. Same rule as the root CLAUDE.md's weekly
performance-drop rule, applied here.

## What each consumer gets

### Fantasy lineup optimizer (IRFL) — primary use
Layer on top of the Sleeper projection baseline (fantasy-football-data
skill):
- **Opponent defense strength by position** — from `pbp`, points allowed
  per position on a rolling 4-6 week window. Recent form over season
  totals.
- **Team pace and pass rate** — plays per game, pass rate over
  expectation, from `pbp`.
- **Usage trends** — snap/target/carry share over the last 3 weeks from
  `stats_player`. Weight recent usage over season averages and over
  name recognition (existing venture rule).
- **IDP matchup data** — opponent plays per game, pass rate, and tackles
  /sacks surrendered, from `pbp`. If Sleeper's IDP `pts_ppr` is thin or
  junk (flagged in the fantasy-data-patch verification — Sleeper's
  `pts_ppr` field does not reflect the IRFL's actual 1pt/tackle,
  3pt/sack scoring), this becomes the **primary** IDP ranking method,
  not a supplement. Say so plainly rather than producing a lineup call
  with eight blank slots.
- **Output requirement**: any adjustment off the baseline projection
  must name the factor and rough magnitude. "Started him over the
  higher projection because opponent allows the third most points to
  tight ends over the last five weeks" — not a silently adjusted number.

### Pick'em — secondary use, tiebreaker only
Rolling EPA per play (offense and defense), 4-6 week window, from `pbp`
or `stats_team` (`passing_epa`, `rushing_epa`, `receiving_epa` columns
confirmed present on `stats_team`; defensive EPA is not a direct column
there — compute from `pbp` if a defensive-EPA figure is needed).

**Vegas already prices EPA.** This does not beat the spread on its own
and is not a second model — use only as a tiebreaker on calls the
line-movement check (fantasy-football-data skill) leaves at ~50/50. If
this starts drifting toward a full predictive model, stop and flag it
to Zac. The line-movement comparison remains the primary pick'em edge.

### Sports content (venture undecided)
Play-level angles — conversion rate by down/distance bucket, success
rate by game state, drive-level rankings — from `pbp`. **Data layer
only.** Do not scaffold scripts, thumbnails, posting schedules, a
content calendar, or a venture name. Those decisions have not been
made.

### Cross-platform ID bridge (`players` release)
Confirmed columns: `gsis_id, esb_id, nfl_id, pfr_id, pff_id, otc_id,
espn_id, smart_id` — no `mfl_id` or `sleeper_id` field. This does
**not** solve the MFL-to-Sleeper bridge in fantasy-football-data
directly (no MFL-native ID here), but `espn_id` and `gsis_id` overlap
with the same fields Sleeper's player objects carry, so it's a usable
third cross-check leg if the MFL `DETAILS=1` export doesn't carry a
matching ID. Check this before building out the name-matching fallback
in the other skill.

## Cache

`D:\WKP\data\nfl\<tag>\<filename>` per release, plus
`D:\WKP\data\nfl\nfl-data-manifest.json` at the root of the cache
recording what was last discovered and when. Every downloaded file
carries a `.meta.json` sidecar (download timestamp, source URL, source
`updated_at`) — this is what makes the honesty rule checkable rather
than assumed.
