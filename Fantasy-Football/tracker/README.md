# Accuracy Tracker — Phase 1

Built from `..\ACCURACY-TRACKER-BUILD.md`. **Phase 1 only**: logging
structure + grader. No backtest, no .docx report, no scheduled task —
those are Phase 2/3, not started, per the build doc's explicit
"do not start a phase before the one before it has run correctly."

Verified against one real week (2026 week 1, the two games already
final — SEA/NE and SF/LAR) with hand-checked numbers before this was
trusted. See "What was verified" below.

## Files

| File | Purpose |
|---|---|
| `predictions.csv` | The append-only log. One row per game per prediction source. Currently header-only — real production use starts fresh from here. |
| `logger.py` | Writes prediction rows (`log_model_picks`, `log_card_picks`) |
| `grader.py` | Grades a week (`python grader.py <season> <week>`), prints a console summary |
| `espn_games.py` | Shared ESPN scoreboard fetch/normalize |
| `biases.md` | Human-written pattern log — nothing here is automatic |

## Usage

```
cd D:\WKP\Fantasy-Football\tracker

# log model picks (every game, not just the card) -- picks come from
# wherever the model lives; this only logs and validates them
python -c "import logger; logger.log_model_picks(2026, 2, [
    {'team': 'KC', 'pick_su': 'KC', 'pick_ats': 'KC', 'line_used': -2.5, 'confidence': 0.7},
])"

# log the control card or assisted card -- plain text, one team per
# line, no spread, no formatting. Matched against this week's real
# card automatically.
python -c "import logger; logger.log_card_picks(2026, 2, 'control_card', '''
SEATTLE
KANSAS CITY
'''.strip())"

# grade a week once its games are final
python grader.py 2026 1
```

## Real bugs found and fixed while building this (2026-09-13)

1. **ESPN's `odds` field disappears once a game goes final.** Confirmed
   by direct comparison — pre-game events carry a full odds block,
   post-game ones carry none. Since grading happens Tuesday morning
   (after games are over), ESPN cannot be the closing-line source.
   Fixed by pulling closing lines from nflverse's `schedules` release
   instead (via the `nfl-data` skill), which updates same-day and isn't
   subject to the multi-day lag that rules nflverse out for scores.

2. **ESPN and nflverse disagree on two team abbreviations.** Verified
   by diffing all 32 real codes from both sources: `LAR` (ESPN) vs `LA`
   (nflverse) for the Rams, `WSH` (ESPN) vs `WAS` (nflverse) for
   Washington. Every other code matches. `grader.py`'s
   `ESPN_TO_NFLVERSE_ABBR` map handles the translation when looking up
   a closing line — without it, both teams' closing lines would come
   back blank or wrong, silently, forever.

3. **The closing-line lookup wasn't filtered by season.** nflverse's
   `schedules.parquet` holds every season since 1999 in one file, and
   team codes repeat every year. An early version matched NE@SEA and
   silently returned the **2008** meeting's line (-7.5) instead of
   2026's (3.0) — caught by hand-verifying the test grade against the
   real final score, not by any assertion in the code. `season` and
   `week` are now mandatory filter arguments, and a second safety net
   raises if more than one match is somehow still found rather than
   silently taking `.iloc[0]`.

## Sign convention (decided here — the build doc didn't pin one)

`line_used` and `closing_line` are both stored using **nflverse's own
documented convention**: positive = home team favored by that many
points, negative = away team favored. Confirmed against nflverse's
published data dictionary, then cross-checked against ESPN's own odds
for all 14 pending week 1 games — exact sign and magnitude match on
every one — before this was trusted for grading logic. `logger.py` is
the only place that converts from "friendly" input (a card's
favored/spread/underdog format) into this convention; everything
downstream just compares `home_score - away_score` against a signed
number.

## Design decisions worth a second look

- **The assisted card is logged exactly like the control card** — plain
  text, one team per line, not auto-extracted from the real `.xls`
  card. This was a deliberate choice, not a shortcut: the pick-marking
  convention on that file is still an open question (see
  `..\..\logs\DECISIONS.md` entry `FF-2026-09-12-01` — the Week 1 card
  reads as fully blank, no confirmed way to tell which side got
  picked). Auto-extracting from an unconfirmed format risked logging
  picks Zac never actually made, which is a worse failure than asking
  him to paste the same plain-text list twice. Revisit this once that
  decision is resolved.
- **NCAA games aren't wired into the tracker yet.** `log_card_picks`
  only queries the NFL scoreboard; a college team name is refused
  loudly (not silently dropped) rather than guessed at. Section 1 asks
  for "whatever college is in scope" — extending to the CFB scoreboard
  (same approach as the dashboard's `team_match.match_cfb_team`) is
  straightforward but wasn't built since Phase 1's stated goal was
  "grade one real week correctly," which didn't require it.
- **`pick_su` is left blank for card-sourced picks** unless a line is
  explicitly prefixed `SU:` in the pasted text. A plain team-name list
  from a spread pool is an ATS pick by construction; assuming it also
  means "and I think they win outright" would be inventing data Zac
  never gave.

## What was verified (Section 7's "grade one real week" requirement)

Four synthetic test rows (2 sources × 2 already-final week 1 games,
backdated `logged_at` to before their real kickoffs) were logged,
graded, and hand-checked against the real final scores (SEA 13–10 NE,
SF 27–7 over LAR) before being deleted. All of it checked out:
correct/incorrect/push logic, the season/week bug above (caught this
way), and the integrity-abort check (tested directly against the exact
mutation it exists to catch). `predictions.csv` was reset to
header-only afterward — no test data is in the real log.
