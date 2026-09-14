# Accuracy Tracker — Build Spec

## DROP LOCATION
`D:\WKP\fantasy-football\`

## EXACT PHRASE FOR CLAUDE CODE
> Read ACCURACY-TRACKER-BUILD.md and build it. Phase 1 only — the
> logging structure and the grader. Do not build the backtest or the
> scheduled report until Phase 1 has graded one real week correctly.
> Read Section 6 before you build anything; it names the things that
> will silently corrupt this if you get them wrong.

---

## What this is

A record of what we predicted, what actually happened, and how far
apart those were. Two purposes:

1. **Measurement** — is the model better than guessing, and by how much
2. **Repair** — find the specific situations where it is consistently
   wrong, so those can be corrected in the rules

It is not a learning system. Nothing here trains automatically. The
output is a weekly report that surfaces patterns a human then encodes
as rule changes.

---

## SECTION 1 — What gets logged

Three separate prediction sets, logged independently every week.

**A. Model picks — every game.** All pro games plus whatever college is
in scope, whether or not it makes the card. Predicting only the twelve
to twenty card games means a season produces too little data to say
anything. Predicting every game roughly quadruples the sample and
reveals whether the model is good at games Zac would never have chosen.

**B. Assisted card — what Zac actually submitted.** Twenty picks, pro
games plus college to round out. This is the real-money-equivalent
record, graded against the Monday line he is locked into.

**C. Control card — Zac's own picks, no model input.** Made before
seeing the model output. This is the comparison that matters most: it
answers whether the model beats Zac unaided.

Plus, on the fantasy side:

**D. Lineups — model lineup and Zac's lineup, both logged before
kickoff.** Same roster, two sets of starters. Both scored Tuesday under
IRFL rules.

---

## SECTION 2 — Storage

Append-only CSV files in `D:\WKP\fantasy-football\tracker\`.

```
predictions.csv    one row per game per prediction set
lineups.csv        one row per player per lineup set per week
biases.md          running list of identified patterns and fixes
```

CSV rather than a database so Zac can open it in Excel without asking
anyone.

### predictions.csv columns
```
logged_at          timestamp, ISO format
season, week
game_id            ESPN game id
away_team, home_team
source             model | assisted_card | control_card
pick_su            team picked to win outright
pick_ats           team picked against the spread
line_used          the spread the pick was made against
line_source        monday_card | closing | model_only
confidence         model only, 0 to 1, blank for human picks
on_card            true if this game appeared on the submitted card
-- filled in after the game --
graded_at
away_score, home_score
closing_line
result_su          correct | incorrect
result_ats         correct | incorrect | push
```

### The integrity rule

**Predictions are written before kickoff and never edited afterward.**
The grader only ever fills the post-game columns. If any process
rewrites a `pick_su`, `pick_ats`, or `line_used` value after
`logged_at`, the entire record is worthless and every percentage
computed from it is a lie.

Make the file append-only in practice: the grader reads, computes, and
writes graded rows to a separate pass rather than rewriting history in
place. Refuse to grade any row whose `logged_at` is after kickoff and
log that refusal loudly.

---

## SECTION 3 — Grading

**Results come from ESPN's scoreboard, not nflverse.** nflverse updates
on a lag measured in days. ESPN has final scores immediately. For a
Tuesday morning report covering Monday night, nflverse will not have
the data yet. This matters and is not optional.

```
https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?seasontype=2&week={n}&dates={year}
```

**Straight up:** did the picked team win. Ties count as incorrect
unless Zac says otherwise.

**Against the spread:** apply `line_used` to the final score. Exact
landing on the number is a push and counts as neither. Pushes must be
excluded from the denominator, not counted as losses.

**Record the closing line too**, even though Zac plays the Monday line.
It costs nothing and it answers the most valuable question this tracker
can answer: if the assisted card beats the Monday line but loses to the
closing line, the edge is real and it is specifically about timing. If
it beats both, something else is working. If it beats neither, we know
that too.

---

## SECTION 4 — Baselines, mandatory on every number

A raw percentage is meaningless without the comparison. Every rate in
the report shows its baseline beside it.

| Metric | Baseline | Meaning |
|---|---|---|
| Straight up | Always pick the favorite | Historically lands near two thirds. Anything under that is worse than not thinking. |
| Against the spread | 52.4 percent | Roughly break-even once standard juice is accounted for. Fifty percent is a loss. |
| Model versus control card | Control card's rate | The only comparison that says whether the model helps Zac specifically. |
| Model lineup versus Zac's lineup | Zac's points | Same question, fantasy side. |

Compute the favorite baseline from the same games in the same weeks,
not from a historical constant. That way it moves with the actual
slate.

---

## SECTION 5 — The Tuesday report

Generated by a scheduled script, not by a chat session.

**Windows Task Scheduler**, Tuesdays at six in the morning. Runs the
grader, then writes a .docx using `python-docx` to
`D:\WKP\fantasy-football\reports\Week{N}-Accuracy.docx`.

Register it with `schtasks`. Confirm it survives a reboot.

### Report contents, in this order

1. **Headline.** Three records for the week — assisted card, control
   card, model — each shown against its baseline.
2. **Season to date**, same three, same baselines.
3. **Sample size statement.** Games graded so far, and a plain sentence
   saying whether that is enough to mean anything. Under roughly a
   hundred and fifty graded games, it is not, and the report must say
   so in words rather than presenting a percentage as if it were
   settled.
4. **Disagreements table.** Every game where model and Zac picked
   differently, and who was right. This is the most useful page in the
   document. After enough weeks it answers whether Zac should be
   deferring to the model or overruling it.
5. **Monday line versus closing line.** How the assisted card scored
   against each.
6. **Fantasy lineup comparison.** Model lineup points, Zac's lineup
   points, and points left on the bench by each.
7. **Biggest misses.** Three or four, with a one-line diagnosis of what
   the model got wrong. Weather, injury not priced in, usage change,
   whatever it was.
8. **Open bias list.** Carried forward from `biases.md`. Patterns
   identified, whether a fix has been applied, and whether the fix
   worked.

### Timing caveat, printed in the document

Monday night games finish late and official stat corrections land
Tuesday and Wednesday. A Tuesday six a.m. report is **preliminary** on
the Monday game and on any close fantasy matchup. Print that line in
the document. Optionally re-run Thursday and note any changes.

---

## SECTION 6 — Read before building

### The core edge cannot be backtested

The pick'em edge is the gap between the frozen Monday line and where
the market moves by kickoff. **nflverse historical data carries closing
lines, not Monday openers.** There is no free historical record of the
line Zac's card froze at.

So the backtest can validate team-strength and EPA-based prediction. It
**cannot** validate the line-timing edge, which is the main thing
working. Do not present backtest results as if they measured the whole
model. State this limitation in the backtest output itself.

### Backtest scope

Use `schedules` from nflverse, which carries results and closing lines
across many past seasons. Run the model's non-timing components against
them.

Report the honest version: how the model does against closing lines
historically. If that number is near or below fifty-two point four
percent, that is not a failure — it means the edge lives in the timing,
which is what we already believed. Say that rather than tuning the
model until the number looks better.

**Do not tune on the backtest and then report the tuned number as a
result.** That is fitting to noise and it will feel like success right
up until live picks start losing.

### Keep Zac's weekly effort small

The control card and the gut lineup only work if they stay cheap. A
list of team names and a list of player names. No form, no ratings, no
justification. If it becomes homework it gets skipped, and a skipped
week is a hole in the record that cannot be filled in later.

Accept the control card as plain text pasted into a file. Parse
loosely. Do not make Zac format anything.

---

## SECTION 7 — Build phases

**Phase 1.** Logging structure, the three prediction sets, the grader,
and a plain text summary printed to console. Grade one real week and
verify the numbers by hand before trusting them.

**Phase 2.** The .docx report and the Task Scheduler job.

**Phase 3.** The backtest, with the limitation from Section 6 stated in
its output.

**Phase 4.** Lineup comparison, once the scoring function from
FF-SCORING-RULES.md is verified working.

Do not start a phase before the one before it has run correctly on real
data.
