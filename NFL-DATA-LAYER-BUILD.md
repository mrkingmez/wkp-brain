# NFL Data Layer — Shared Build Spec

## DROP LOCATION
`D:\WKP\` (repo root — this is shared infrastructure, not a venture file)

## EXACT PHRASE FOR CLAUDE CODE
> Read NFL-DATA-LAYER-BUILD.md and build the nfl-data skill exactly as
> specified. Start with Section 3 — discover the real asset filenames
> from the GitHub releases API before writing any download logic. Do
> not hardcode filenames from this document. Report what you actually
> found, then build.

---

## Why this is shared and not inside a venture

Two unrelated consumers need the same data:

1. **Fantasy football venture** — team-level EPA for the pick'em
   tiebreaker on close calls.
2. **Sports content venture (unnamed, format undecided)** — play-level
   detail for statistical angles.

They pull the same files. Building it twice means two caches, two
update schedules, and two things to fix when nflverse changes a
filename. Build once, both read from it.

This has **nothing to do with WWD**. Do not wire it to any WWD agent,
skill, or production rule. Do not apply WWD style or SEO conventions to
anything it produces.

### Proposed paths (override if they clash with existing conventions)
- Skill: `D:\WKP\.claude\skills\nfl-data\SKILL.md`
- Cache: `D:\WKP\data\nfl\`

---

## SECTION 1 — The source

**nflverse** — `https://github.com/nflverse/nflverse-data/releases`

Automated data releases pushed via GitHub Actions. Free, MIT licensed,
no API key, no account. Files are published as CSV, compressed CSV,
parquet, and RDS depending on the release.

`github.com` and `api.github.com` are both on the allowed-domains list,
so this is directly reachable. No proxy workaround needed.

### Releases that matter here

| Release | What it holds | Which consumer |
|---|---|---|
| `pbp` | Play by play, one row per play, ~370 columns including EPA and win probability | Content |
| `stats_team` | Team stats in several aggregation levels | Pick'em |
| `stats_player` | Player stats, week and season level | Both |
| `schedules` | Game and schedule data, results, spreads | Both |
| `players` | Player info and cross-platform ID mappings | Both |
| `pfr_advstats` | Pro Football Reference advanced stats | Content |

`players` is worth flagging: it carries ID mappings across platforms.
That may solve part of the MFL-to-Sleeper bridge problem in the other
patch. Check it before building the name-matching fallback there.

---

## SECTION 2 — Format and size

**Use parquet where offered.** Play by play for a single season runs
roughly fifty thousand rows by about three hundred seventy columns. As
CSV that is order-of-magnitude a hundred megabytes per season. Parquet
is a fraction of that and reads faster.

Verify actual file sizes on first pull and report them. Do not download
ten seasons of play by play as a first step to see what happens.

**Start with the current season only.** Add historical seasons on
demand, not speculatively.

---

## SECTION 3 — Discover before you download

**Do not hardcode filenames from this document.** nflverse renames and
reorganizes release assets between seasons. The table above is a guide
to which releases exist, not a guarantee of what the files are called.

First call, every time you set this up or it breaks:
```
GET https://api.github.com/repos/nflverse/nflverse-data/releases
```

That returns every release with its full asset list — real filenames,
real download URLs, real byte sizes, real upload timestamps. Pick from
what is actually there.

Write the discovered filenames and URLs into a
`nfl-data-manifest.json` in the cache directory, with the date of
discovery. Re-run discovery when a download 404s, and at the start of
each season.

---

## SECTION 4 — Update cadence and the honesty rule

nflverse updates on an automated schedule after games are processed,
typically a day or more after games finish. **It is not live data.**

- Fine for: Tuesday or Wednesday analysis, weekly pick'em prep,
  content built on completed games.
- Not usable for: anything same-night, in-game, or live.

For live scores and game state, use ESPN's public scoreboard endpoint
already specified in the fantasy data patch. Different tool, different
job.

**Rule:** every cached file gets a timestamp. Any consumer reading this
data must state the age of the data it used. If the newest file is more
than ten days old, say the analysis is running on stale data rather
than presenting it as current. Same rule already in the root CLAUDE.md
for the performance drop — apply it here.

---

## SECTION 5 — What each consumer gets

### Fantasy lineup optimizer (IRFL) — PRIMARY USE

This is where the data layer pays off most. No market prices a start
or sit decision, so there is real edge here that does not exist on the
pick'em side.

Feed the optimizer these, layered on top of the Sleeper projection
baseline from the other patch:

**Opponent defense strength by position.** From `pbp`, compute how many
fantasy points each defense allows to each position, on a rolling four
to six week window. Recent form beats season totals — defenses change
as injuries and scheme changes land. Use this to adjust a player's
projection up or down against that week's opponent.

**Team pace and pass rate.** Plays per game and pass rate over
expectation, both from `pbp`. More plays means more opportunity. A
pass-heavy team in a projected shootout lifts its receivers and its
running back's reception total, which matters in full PPR.

**Usage trends.** Snap share, target share, and carry share over the
last three weeks from `stats_player`. This is the single best early
signal that a player's role changed. Weight recent usage above season
averages and above name recognition, per the existing rule in the
venture CLAUDE.md.

**IDP matchup data — do not skip this.** Eight of seventeen starters
are defensive, and Sleeper's IDP projections may be thin or missing
(the other patch has Claude Code verifying that). `pbp` gives a real
substitute: opponent plays per game, opponent pass rate, and how many
tackles and sacks that offense has surrendered. A high-tackle
linebacker facing a slow, run-heavy offense is a different call than
one facing a pass-heavy team running eighty plays.

If Sleeper IDP projections come back empty, this becomes the primary
IDP ranking method rather than a supplement. Say so plainly rather
than producing a lineup call with eight blank slots.

**Output requirement.** When the optimizer moves a player up or down
from the baseline projection, it must state which factor caused it and
by roughly how much. "Started him over the higher projection because
opponent allows the third most points to tight ends over the last five
weeks" is useful. A silently adjusted number is not.

### Pick'em (fantasy venture) — SECONDARY USE

Compute rolling EPA per play, offense and defense, on a four-to-six
week window from `pbp` or from `stats_team` if it is already
aggregated that way.

**Read this before building it:** Vegas already prices EPA. This will
not beat the spread on its own and it is not a second model. Use it
only as a tiebreaker on calls the line-movement check leaves at fifty-
fifty. If the build starts drifting toward a full predictive model,
stop and flag it to Zac rather than continuing.

The line-movement comparison remains the primary pick'em edge. Do not
let this displace it.

### Sports content (venture undecided)
Play-level data supports angles that broadcast commentary does not
cover — conversion rates by down and distance bucket, success rate
split by game state, drive-level rankings against a full season.

Format is undecided — on camera, faceless graphics, or something else.
**Build the data layer only.** Do not scaffold scripts, thumbnails,
posting schedules, or a content calendar. Do not name the venture.
Those decisions have not been made.

---

## SECTION 6 — Verification

Run these and report actual results before building anything on top.

```
1. GET https://api.github.com/repos/nflverse/nflverse-data/releases
   Report: which of the six releases in Section 1 exist, and the
   exact asset filenames available for the current season.

2. Download the smallest current-season stats_team asset.
   Report: real file size, row count, and the column names.
   State plainly whether an EPA column is present.

3. Download the current-season schedules asset.
   Report: row count and whether it carries betting lines.
```

If any release named in Section 1 does not exist, say so. Do not
substitute something that looks similar and continue.
