# Gap audit: fantasy-football-director, DFS side only

2026-11-22, self-audit by fantasy-football-director. Not graded. IRFL files not used. Compared against the Craft Brief (`fantasy-football-director-craft-brief.md`). Dollar cost of any gap is NOT KNOWN unless stated; Zac's time cost comes from his own words in `memory\feedback-dfs-concentration-check.md`.

## Outputs audited (all on disk)
1. `Fantasy-Football\reports\Week11-DK-Noon-Rerun-2026-11-22-sun.md` (12:04 PM ET note)
2. `D:\Draft Kings\Week 11\sun\build_report.txt` and the entered file `DKEntries_week11_LINEUPS_UPLOAD.csv`
3. `Fantasy-Football\reports\Week11-DFS-After-Action-2026-11-22.md`
4. `Fantasy-Football\dfs\LEARNING-LEDGER.md`
5. `Fantasy-Football\reports\Week10-DFS-Friend-vs-Ours-2026-11-13.md`
Week 10 results (what Zac entered, score, return): NOT AVAILABLE on disk, so no Week 10 score audit. Only the Week 11 results are recorded.

## Findings (departure from the brief, what it cost)

| # | Output | Departure | Brief line | Cost |
|---|---|---|---|---|
| 1 | Noon note | Shipped McBride (ARI) in 4 of 7 lineups after Beck went OUT, Josh Johnson at QB, ARI implied 12.5. The note names the risk itself, then says "Cut it by hand if you do not like it." The fix was handed to Zac instead of made. | Our fixed rule (flag and fix any chalk or QB-change player before hand-off) | Zac lost errand time before the 1 PM lock, his words 2026-11-22. Entered file has McBride in 0 lineups, so he or a patch fixed it. |
| 2 | Noon note | Q players in the entered 7 per the DK salary file Status column: Tyson (2 lineups), Tate (2), Waller, Douglas, Mayfield. The note records resolution only for Tate, Waller, Tremble, Mayfield. Tyson and Douglas appear as ACTIVE with full practice in `injuries_2026_wk11.csv` stamped 2026-11-22T15:17Z (10:17 AM ET, about 1 hr 45 min before the note, so the data was in hand). No status line with source and time for them in the note. | S3/S4/S6: resolve Q with a dated report and write it down | No loss shown (Tyson and Douglas were fine), but a Q-tagged player entered with no written resolution is a repeat risk. |
| 3 | Build report | `Q flagged: []` while the DK file marks 5 entered players Q. The builder's Q filter reads our own file, not DK's Status column, so the two disagree silently. | S3 | None shown. Silent disagreement. |
| 4 | Entered file | Pollard (own est 37.9) and Pickens (39.2) are chalk-pool players, each in 3 of 7 lineups. Rule says flag chalk in 3 or more. No written justification exists in any file I read. Entered max count is 3, so the cap 4 did not trip. | Our fixed rule, S2 portfolio view | The slate winner shape needed these two (After-Action sec 2), so no loss shown. A flag without a justification is still a miss. |
| 5 | Noon note | "NOT VERIFIED: weather, depth-chart roles (no dated web source)." Depth chart and role were not retrieved for the lineups. | Mandatory current-info rule in the spec | Unknown. |
| 6 | Entries | 5 of 7 entered lineups came from a patched scratch copy of the builder (RotoWire injection), not the repo script; the repo could not reproduce them. | Source labelling | Fixed 2026-11-22 (flag in `dk_gpp.py`, `lineup_sources.csv`, `entered_archive`). Not re-drilled. |
| 7 | Week 10 report | Kenneth Walker III (Q, no practice, NFL.com Week 10) was not flagged by our salary or status files; the report said "I have not fixed it." Whether it was fixed later is NOT VERIFIED. | S3 | Unknown. |
| 8 | Week 10 report | "Our sim ranks ours above his, but we built ours on that sim, so that ranking is flattered." It says so itself. No outside check existed for Week 10. | one slate is noise | None. Honest note. |

Per-lineup projected-versus-actual error, recomputed this session from files (script `D:\WKP\scratch\leveling\drill1_score.py`): errors -20.8, -3.2, -8.6, -0.9, -16.2, +29.4, +17.8; mean -0.4, mean absolute error 13.8 per lineup. The ledger says mean about -0.9 and a range of -21.3 to +28.5 (different sim-mean source, about 0.5 apart per lineup). Both agree there is no bias and the spread is large.

## Top 3 gaps by cost
1. Fix handed to Zac instead of made (finding 1). Real cost, in his words. Closed in the spec only by the feedback file; no checklist existed until today's pre-flight.
2. Q and role status not resolved in writing for entered players, and the builder's Q filter disagrees with DK's own Status column (findings 2, 3, 5). Risk cost, not yet a loss.
3. Chalk in 3 lineups with no stated reason, and the lineup-count check was a lesson, not a step in a checklist (finding 4). Process cost.
