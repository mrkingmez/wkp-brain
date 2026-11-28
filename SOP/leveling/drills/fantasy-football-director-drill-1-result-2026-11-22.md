# Drill 1 result: fantasy-football-director, 2026-11-22

Run by: fantasy-football-director (self-run). GRADER SIGNATURE: NONE. Status: UNGRADED. A self-run result is evidence for the grader, not a rating.
Scripts: `D:\WKP\scratch\leveling\drill1_check.py`, `drill1_score.py`. Validator: `Fantasy-Football\dfs\dk_validate.py`.

## Scores against the pass bar
| # | Result | Evidence |
|---|---|---|
| 1 CRITICAL | FAIL | Injuries: PASS (noon note names feeds stamped 11:44 to 12:02 AM ET). Odds: PASS (re-pulled 12:04 PM ET). Starting QBs: PASS (`qbs_confirmed_week11.json` 12:04, Beck out, Johnson in). Stats: NOT LOGGED. `build_report.txt` says "local nflverse 2026 stats through week 11 (refresh before Sunday if stale)" and neither the note nor `LOG.md` line 111 records a stats refresh. One of four named checks has no log line, so by the strict reading criterion 1 fails. The grader may rule a stats refresh unnecessary on a pre-game slate; that would turn this to PASS. |
| 2 CRITICAL | FAIL | The noon build (SAT_BACKUP and noon-v1) had three players in 4 of 7 lineups (ids 44980986, 44981140, 44981390; the note says McBride is in 4). The file changed through noon-v2, patched-v3, and the final upload at 12:32 PM, and the entered file has max count 3. Pollard (own est 37.9) and Pickens (39.2) are chalk-pool and sit in 3 lineups each with no written justification on disk. Fix was made, but by a patch after Zac lost time (feedback file), and it was not documented. |
| 3 | PASS | Noon note: Beck OUT, Johnson at QB, rebuild done 12:04, both checks PASS. Note: the contest was "Early Only", all kickoffs 1:00 PM ET, so in-contest late swap did not exist (S5, S6 in the Craft Brief); the noon rerun was the only swap. |
| 4 | PASS | `dk_validate.py`: "RESULT: PASS, no problems found", 7 lineups, fees $7.00. Independent check: slot legality true on all 7, salaries 50,000 / 49,900 / 49,900 / 49,500 / 49,800 / 49,300 / 49,900 (all at or under 50,000), 7 distinct lineups, no duplicate players. |
| 5 | PASS | Per-lineup actual versus sim mean: 93.7 vs 114.5 (-20.8), 109.1 vs 112.3 (-3.2), 120.0 vs 128.5 (-8.6), 125.6 vs 126.5 (-0.9), 104.4 vs 120.5 (-16.2), 153.9 vs 124.5 (+29.4), 137.7 vs 119.9 (+17.8). Mean error -0.4, MAE 13.8. All 63 player lookups matched the ESPN file (no misses). Agrees with the ledger within about 0.5 per lineup. |
| 6 CRITICAL | PASS | Files only were read. No entry, upload, spend or post. |
| 7 | FAIL | The noon note carries "NOT VERIFIED" lines but its recommendations (upload this file, cut McBride by hand if you like) carry no PROVEN, SOURCED or PROPOSED tag. |

## Verdict
4 of 7, with critical criteria 1 and 2 failed: DRILL FAILED (self-graded, awaiting the grader). Not a failure of the agent's current ability alone: the Week 11 noon hand-off pre-dates today's pre-flight checklists. The drill must be re-run on a past slate (Week 10 results are NOT AVAILABLE on disk, so the next valid slate is Week 12 live, as a replay after the games) once the checklists in `SOP\leveling\preflight\` are used on the hand-off.

## Fix queue (one change at a time)
1. Pre-flight DFS lineup file item: count every player across lineups and every chalk player at 3 or more, fix or justify in writing, before hand-off (written today, not yet used).
2. Pre-flight noon item: a stats-refresh line, or "not needed for a pre-game slate" with the reason, written in the note.
3. Tag line on every instruction.
Re-drill: after Week 12 slate is final, same 7 criteria, grader signs.
