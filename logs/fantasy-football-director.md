
## 2026-11-10 | fantasy-football-director | Five fixes after Week 9 (Jarvis task)
Ran (all in Fantasy-Football\fixes-2026-11-10\, read-only against MFL and nflverse, nothing submitted, predictions.csv untouched):
- MFL API probe: TYPE=lineup/myfranchise/lockedLineup/franchises/nflSchedule rejected. liveScoring and weeklyResults with W=10 return franchise 0012's 17 saved starters (agree). playerScores, projectedScores, weeklyResults for weeks 1-10 cached in mfl_cache\.
- build_dataset.py: 1,990 player-weeks (wk 6-9, proj>=3) sim vs MFL playerScores. Bridge: espn_id via sleeper cache, then name+team (88% matched). Old sim bias +0.08, blend +0.08, MFL proj +0.24. recal.py: leave-one-week-out recal RMSE 5.528 to 5.509, shrink factors no gain. Top-ranked per position bias +0.20 (n=720).
- lineup_calib.py: 47 lineups, bias +13.6, SD 29.6. Zac +21.7, +33.4, -5.4, -34.6.
- injury_rule_test.py (nflverse 2024-26): Q/DNP 0.43, LP 0.58, FP 0.72, healthy 0.94; QB1 out 0.80 vs 0.93 (n=113). wed_dnp_check.py (Thursday captures wk 7, 9): DNP 0.48 n=57 zero 67%, LP 1.41 n=54. injury_rule_zac.py: rule +5.3/wk over model lineup, saved lineup avg 139.9 beat model 131.5; rule would not have saved Week 9 (116.5 vs 116.4).
- pickem_labels.py, pickem_backtest.py, pickem_rules_test.py: 57 NFL games wk 6-9, 38 NO EDGE; LEAN+SLIGHT market side 13/19 (SE 11.5); coin-flip rule NOT adopted (4 weeks conflict with 2,635-game history, dog 51.6% half-point lines).
- dfs_study.py, dfs_optimize_v2.py, dfs_eval_w9.py, dk_realized.py: correlations QB-WR1 +0.44 etc; proxy stacking backtest 35 slates; real slate n=1 (wk9): v2 lineups 98-108 vs Zac 121/143 (no DST). Refreshed nflverse stats_player 2026 cache (week 8 to 9) via nfl_data.py (shared cache, intended use).
- Delegated: market-research (research\fantasy\2026-11-10-dfs-methods-market-research.md), fact-research (...-dfs-facts-brief.md). Both mostly SECONDARY.
Found: nflverse closing_line JAX@BAL wk9 = +3.0 vs market home -10 (FF-2026-11-10-01). Lunch notes not in any file (FF-2026-11-10-02). Zac's wk9 DFS lineup 1 (107) does not reconcile with the csv (FF-2026-11-10-03). Week 9 report's 17 differed from the saved lineup at TE and DL.
Changed: Fantasy-Football\CLAUDE.md (new section "Weekly workflow fixes"). New: reports\Fixes-2026-11-10-Report.md and -DFS.md, docx in D:\WKP Reports\Fantasy Football\.
Not done: no git commit or push, nothing in DraftKings/FanDuel/MFL.
