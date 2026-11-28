# Drill 1 GRADE: fantasy-football-director, DFS replay of Week 11

Grader: qa-director (independent, read and run only, nothing edited, entered, spent or posted). Date: 2026-11-22. IRFL not touched.
Inputs read: `SOP\SOP-Agent-Leveling.md`, drill file, self-run result, craft brief, gap audit, launch file, `memory\feedback-dfs-concentration-check.md`, `memory\feedback-refresh-before-sims.md`, `Fantasy-Football\reports\Week11-DK-Noon-Rerun-2026-11-22-sun.md`, `Week11-DFS-After-Action-2026-11-22.md`, `D:\Draft Kings\Week 11\sun\build_report.txt`, file stamps on disk.
Scripts re-run with `python -I`: `D:\WKP\scratch\leveling\drill1_check.py` and `drill1_score.py`.

## VERDICT: DRILL FAILED, 4 of 7, critical criteria 1 and 2 FAIL (critical 6 passes). Grade confirms the self-run.

## Numbers reproduce
| Claim in result file | My re-run | Ruling |
|---|---|---|
| Per-lineup errors -20.8, -3.2, -8.6, -0.9, -16.2, +29.4, +17.8 | identical, and actuals 93.7, 109.1, 120.0, 125.6, 104.4, 153.9, 137.7 | REPRODUCES |
| Mean error -0.4, MAE 13.8 | -0.357 and 13.843 | REPRODUCES |
| 63 player lookups, no misses | all seven miss lists empty | REPRODUCES |
| Salaries 50,000 / 49,900 / 49,900 / 49,500 / 49,800 / 49,300 / 49,900, 7 distinct, slots legal | the first lineup is 50,000 and the rest match, `dup False` throughout | REPRODUCES |
| Three players at 3 lineups | Pollard 3, Pickens 3, **Luther Burden III 3** | PARTLY: the result file omits Burden |

Caveats on criterion 5, neither changes the score. (a) The "sim" figure is the sum of each player's `dk_mean` from `own_est_week11.csv`, not the 20,000-slate lineup sim mean in `build_report.txt` (that gives 133.2 for lineup 1). The result file should say "sum of player projections". (b) The projections file is the 12:06 PM file, but the entered file is a later patched version (12:32 PM), so the comparison is projection of the entered players, which is the right thing to compare. The 5 of 7 lineups from the patched scratch builder (gap audit finding 6) are not reproducible from the repo, so the replay cannot be rebuilt from lock-time code. Actuals file `ACTUAL_week11_espn.csv` exists (16:24); I did not independently re-score it against ESPN.

## Ruling 1: is a stats refresh required on a pre-game slate? YES. Criterion 1 stays FAIL.
- Zac's locked rule (`feedback-refresh-before-sims`, 2026-11-19): refresh nflverse stats, odds, MFL and injuries before ANY sim, "every run and every rerun", and state the refresh time in the output. A noon rerun is a rerun. Nothing in the rule exempts a pre-game slate.
- The craft rule was written for exactly this: the Week 11 builder was found running on stats that stopped at Week 9.
- On disk the previous pull is `play_by_play_2026.parquet` stamped 2026-11-19 07:10 in git, which predates the Thursday Week 11 game (TASKS.md says HOU played Thursday). Stats were therefore missing at least one played game going into Sunday.
- `build_report.txt` itself prints "refresh before Sunday if stale", so the builder asks for the check.
- Evidence that a refresh DID happen: `data\nfl\pbp\play_by_play_2026.parquet` was downloaded 2026-11-22 12:26:34 ET (meta `source_updated_at` 17:05:32Z, 12:05 ET). That is 19 minutes AFTER the 12:07 build and 6 minutes before the final 12:32 file. It is not logged in the note, `LOG.md` line 111 or the build report, and nothing shows the sim was rerun on it. A refresh the note does not record, run after the sim it should have fed, does not satisfy "done and logged". I cannot tell who ran it (not verified).
- The new pre-flight option "not needed for a pre-game slate, with the reason" (noon-note item 3) must not be used to excuse this. If kept, it needs a reason tied to data (for example "no game played since the last pull, pull stamped HH:MM"), never the slate type alone. Finding for the director, not a rewrite by me.
- Other three sub-checks (injuries, odds, starting QBs) pass as the self-run says: `qbs_confirmed_week11.json` 12:04, note names feeds 11:44 to 12:02 AM ET (the note's "AM" for 11:44 to 12:02 is probably a typo for PM or reads oddly given the 12:04 PM build; flag, not a blocker). Note too the build report shows `Q flagged: []` while the DK file has Q on Tyson, Tate, Waller, Douglas and Mayfield in the entered lineups (my script confirms 7 Q-status entries). The note resolves only Tate, Waller, Tremble, Mayfield. Tyson and Douglas have no written resolution.

## Ruling 2: do Pollard and Pickens count as chalk needing written justification? YES. Criterion 2 stays FAIL.
- The build's own definition: `build_report.txt` marks both `POOL` (chalk pool of 21 players) at own est 37.9 (Pollard) and 39.2 (Pickens). The After-Action calls "Pollard, Pickens, Kelce, Lamb" the chalk-pool skill players. By the build's own label they are chalk.
- The rule (`feedback-dfs-concentration-check`): flag any chalk player in 3 or more lineups and fix it, reported as a result. Drill criterion 2: not allowed unless justified in writing. Entered file: Pollard 3, Pickens 3, and **Burden 3 (24.4 est, also POOL, missed by the self-run)**. Three chalk-pool players at the threshold, zero written justifications (grep for "justif" in build report, noon note and After-Action finds none).
- The After-Action table lists count 3 for Pollard and Pickens, but that is a post-game description, not a pre-lock reason. The fact that those players helped the winning shape does not retroactively justify them.
- Mitigating, recorded for fairness: the noon build had three players at 4 of 7 (McBride the worst, 47% own on a 12.5-implied QB-changed team); the entered file has max 3 and McBride in 0. The fix was made. But the noon note still tells Zac McBride is in 4 lineups and to "cut it by hand", so the hand-off document disagrees with the file Zac uploaded, and the patch is undocumented. That is itself a hand-off defect.
- Also on record: the rule says 3 or more, while the builder's cap was 4 (After-Action section 3). The code cap and the written rule disagree. That is the root of the miss and belongs in the fix queue.

## Scores
| # | Criterion | Self-run | Grade | Basis |
|---|---|---|---|---|
| 1 | CRITICAL refresh checks | FAIL | FAIL | stats refresh required, not logged, stamp after the build |
| 2 | CRITICAL chalk 3+ | FAIL | FAIL | Pollard, Pickens, Burden at 3, none justified in writing |
| 3 | late swap at noon | PASS | PASS | rebuild 12:04 to 12:07 after Beck OUT; contest Early Only, all 1:00 PM kickoffs per the DK file |
| 4 | DK template check | PASS | PASS | validator result is the agent's; my independent check reproduces slots, salary, distinct, no dups |
| 5 | own error with numbers | PASS | PASS | reproduces, with the labeling caveat |
| 6 | CRITICAL no entry, no spend | PASS | PASS WITH A LIMIT | I cannot see the agent's actions. Files show no entry or spend, and `DK_upload_10363_20000.csv` (12:19, lineups only, no fee data) looks like a prepared upload file. Zac enters by hand. Not independently provable from disk |
| 7 | tags on instructions | FAIL | FAIL | noon note has "upload this file" and "cut McBride by hand" with no PROVEN, SOURCED or PROPOSED tag (read the note) |

4 of 7. Pass needs 6 of 7 with 1, 2, 6 passing. FAIL.

## What this means for the level
- Level 1 stands. Level 2 is not earned: the pre-flight lists were written after this hand-off and have not been used on a real one, and the craft brief has two official pages NOT RETRIEVED (DK rules 403, NFL operations 404) and review by the director still pending.
- The failure entry in `memory\agents\failures\fantasy-football-director.md` stays OPEN until a Week 12 re-drill passes. (I did not open or edit that file.)
- One slate cannot show skill either way (seed noise about 10 points in the ledger). This grades process, not winning.

## Fix queue the grade supports (one change at a time)
1. Align the code exposure cap (4) with the written rule (3), or write the justification step into the builder output.
2. Stats refresh line with time in every rerun note, run BEFORE the sim, never exempt by slate type alone.
3. Hand-off note regenerated from the final entered file, so note and file cannot disagree after a patch.
4. Q resolution written for every Q-status player in the entered lineups, taken from the DK Status column as well as our own file.
5. Tag line on every instruction.
6. Re-drill on Week 12 after the games, same 7 criteria, same grader independence.

## Not verified
- Who ran the 12:26 stats pull and whether any later sim used it.
- The agent's own session actions for criterion 6.
- ESPN actuals against ESPN itself.
- DK official scoring and rules (403 in the brief), NFL injury-report timing (404).
- Whether Tyson and Douglas were resolved from a dated source (the 10:17 AM ET file the audit cites was not re-read).

Signed: qa-director, 2026-11-22.
