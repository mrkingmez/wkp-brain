# Fantasy Fixes 1 to 4, after a bad Week 9 (10 NOV 2026)

Decision support only. Nothing was submitted, posted or changed on MFL, DraftKings or FanDuel. No graded row in predictions.csv was touched. Code and data: `D:\WKP\Fantasy-Football\fixes-2026-11-10\`. Fix 5 (DFS) is its own document: `Fixes-2026-11-10-DFS.md`.

## The short version

1. The sims are not broken. Over weeks 6 to 9 the player projections are unbiased (average miss +0.08 points on 1,990 player-weeks). Shrinking them does not help. What was missing was an honest range: a 17-man lineup has a one-sigma miss of about 30 points. Week 9 (152 projected, 116 actual) was a 1.2 sigma bad week, not a model collapse.
2. The one place the sim is wrong in a way that matters is how it treats Questionable players. It plays every one at 75 percent. Questionable players who did not practice Wednesday scored 48 percent of the sim value (n=57); Questionable players who were limited scored 141 percent (n=54).
3. The pick'em model has no demonstrated edge. 38 of 57 NFL games in weeks 6 to 9 were within one point of the frozen line, a coin flip. The card now says so game by game.
4. Zac's saved lineups out-scored the model's re-optimized lineups in 3 of 4 weeks (139.9 vs 131.5 average). Four weeks is too few to conclude anything, but nothing here says the model beats his judgment.

## Fix 2 first (it changes how everything else is quoted): calibration

Method: every sim projection for weeks 6 to 9 (old sim, play sim, the blend at the backtest weights, MFL's own projection) joined to the actual league-scored points from MFL `TYPE=playerScores` (allowed by MFL, it is points, not raw stats). 1,990 player-weeks with projection of 3 or more.

| Source | n | Bias (actual minus projected) | MAE | Correlation |
|---|---|---|---|---|
| Old sim | 1,990 | +0.08 | 4.03 | 0.59 |
| Play sim | 1,494 | +0.14 | 4.04 | 0.60 |
| Blend (what the reports use) | 1,990 | +0.08 | 3.98 | 0.61 |
| MFL projection | 1,803 | +0.24 | 4.04 | 0.61 (QBs overprojected by 5.6) |

By position (blend): DB -0.26, DL -0.48, LB -0.06, K +0.08, QB -0.60, RB +0.23, TE +0.36, WR +1.00.

**Does shrinking help? No.** Leave-one-week-out test: raw RMSE 5.528, per-position linear recalibration 5.509 (0.3 percent), global shrink toward the position mean 0.95/0.90/0.85/0.80 gives 5.525/5.527/5.533/5.542. Nothing worth adopting. Highest-ranked players per position (the ones the optimizer picks) are also not over-projected: +0.20 (n=720). No winner's curse found. If anything QBs (+2.1, n=48) and WRs (+0.9) at the top were slightly low.

**Lineup level (all 12 franchises, 47 lineups with almost all starters projected):** actual minus blend projection: bias +13.6, standard deviation 29.6, MAE 25.9, slope 0.94. The old sim alone is +15.0, so the play sim trims about 1.4. Zac's four lineups missed by +21.7, +33.4, -5.4, -34.6 (mean +3.8). The sim's own quoted 10th to 90th range for the Week 9 lineup (115 to 191) matched the observed spread; it was just not what the headline number said.

**What to quote from now on:** projection plus or minus 38 is an 80 percent range. Head-to-head win probability = Phi((mine minus theirs) / 42). At 152 vs 147 that is about 55 percent. A 5-point edge is a coin flip.

**Where is the bias?** Not in the old sim vs play sim (1.4 points of 17 players). Not in position slopes (RB 0.73, DB 0.79, DL 0.82 are the only ones below 0.85, and recalibrating them did not improve out-of-sample error). Injury handling is the weak spot: sim-tagged Questionable players overall are on target (bias +0.02, n=234), but that average hides the split in Fix 3. League-wide lineups running 13 points above the sim (3 sigma, SE 4.3) probably reflects managers choosing starters with late information; I did not correct upward because the cause is unproven and Zac's own lineups do not show it (+3.8, SE 15).

**Runs every week:** `python -I run_weekly_calibration.py <last completed week>` on Tuesdays after MNF. It pulls MFL weeklyResults, playerScores and projectedScores read-only, rebuilds the dataset, prints bias, spread, the range to quote and per-position slopes, and appends to `calibration_log.csv`. Rule for acting on it: shrink a position only if its slope stays below 0.85 for 3 more weeks and the leave-one-week-out error improves.

Caveats: 4 weeks. Week 6 has no play sim. Rows where the sim player could not be matched to an MFL id (about 12 percent, mostly backups and kickers) are dropped. MFL projections are whatever MFL had when pulled today, not necessarily the pre-game number.

## Fix 3: injury-risk rule

Large sample, three seasons (nflverse 2024 to 2026, QB/RB/WR/TE, trailing 4-game average of 6 or more as the proxy projection): actual divided by proxy.

| Group | n | Ratio | 90% CI |
|---|---|---|---|
| Healthy, no report | 5,694 | 0.94 | 0.93 to 0.96 |
| Questionable, did not participate | 57 | 0.43 | 0.32 to 0.55 |
| Questionable, limited | 293 | 0.58 | 0.52 to 0.65 |
| Questionable, full | 71 | 0.72 | 0.61 to 0.84 |

Caveat: nflverse keeps the last practice status of the week (usually Friday), not Wednesday. So I also tested the exact timing on our own Thursday captures (weeks 7 and 9, all positions including IDP, ratio to the sim's blend): Questionable plus Wednesday DNP, n=57, ratio 0.48 (CI 0.31 to 0.65), zero rate 67 percent. Questionable plus limited, n=54, ratio 1.41 (CI 1.17 to 1.66), zero rate 13 percent. The week 8 capture was overwritten on Sunday and is unusable.

Backup QB: pass catchers and backs when the team's QB1 is Out or Doubtful, 113 player-weeks over 3 seasons: 0.80 vs 0.93 when QB1 plays. Haircut about 14 percent. Smaller sample, confidence lower.

**Rule adopted (in Fantasy-Football\CLAUDE.md):** Questionable plus no Wednesday practice, multiply the blend by 0.55 (a start only if his blend is 1.8 times the healthy bench option). Questionable plus limited or full: no change (the evidence says the sim is too pessimistic, the large sample says otherwise, so neutral). QB1 Out or Doubtful: teammates' RB/WR/TE times 0.86.

**Backtest on Zac's roster, weeks 6 to 9** (MILP lineup from the blend, with and without the rule, scored with MFL points; Out and Doubtful treated as Wednesday-DNP, not zero, to avoid hindsight):

| Week | Zac's saved lineup | Model (blend) | Model plus rule | Hindsight best |
|---|---|---|---|---|
| 6 | 140.6 | 126.9 | 128.7 | 170.7 |
| 7 | 159.9 | 151.8 | 166.4 | 197.8 |
| 8 | 142.8 | 135.4 | 135.4 | 179.5 |
| 9 | 116.4 | 112.0 | 116.5 | 146.8 |
| Average | 139.9 | 131.5 | 136.8 | 173.7 |

The rule beat the plain model lineup by 1.8, 14.6, 0.0 and 4.5. Week 7 carries most of it (Dowdle in, Robinson out). It would NOT have rescued Week 9: the rule lineup scored 116.5 against the saved 116.4. The Week 9 collapse was Goff (5.3 vs 22.8), Flowers and Jameson Williams, none of which an injury rule touches, plus Okereke and Robinson, which no alternative could replace. Honest verdict on the backtest alone: four weeks, three swaps, uses end-of-week injury status that flatters it, too small to prove anything. The support for the rule is the 57-player exact-timing check and the 420-player large sample, not these four weeks. Note the saved lineups beat the model lineups: do not treat the blend as better than Zac's own picks.

## Fix 1: pick'em labels

Weeks 6 to 9, 57 NFL games with a market read. Model as logged: 28 of 57 (49 percent). Weekly ATS 12, 9, 8 of 20 (29 of 60, 48 percent) includes college. College has no market data, so it is always NO EDGE.

The model's picks are mostly line movement. In 27 of 57 games it picked against the way the market moved from the frozen line, and went 12 of 27 (44 percent); where it agreed it went 16 of 30 (53 percent).

**Labeling** (`pickem_labels.py <week>`): gap to current market, probability = Phi(gap/13.2) where 13.2 is the real standard deviation of NFL results around the closing line (2016 to 2025). LEAN gap 2 or more (56 to 60 percent). SLIGHT gap 1 to 1.9 (53 to 55 percent). Under 1: NO EDGE, COIN FLIP, with a column for Zac's own read. Expected right out of 20: about 10.3, standard deviation 2.2. Week 9 would have labeled 1 LEAN (ARI +11.5), 6 SLIGHT, 8 NFL NO EDGE and 5 college NO EDGE.

**Test of the labels on weeks 6 to 9** (market side, tie to underdog): LEAN 6 of 9, SLIGHT 7 of 10, together 13 of 19 (68 percent against a stated 56). The standard error at n=19 is 11.5 points, so this neither proves nor disproves it. About 1,250 games are needed to tell a true 53 percent from 50. NO EDGE games, market side: 20 of 38.

**Coin-flip rule, tested:** long-run (nflverse, 2,635 games, closing line as the stand-in for the frozen line, league tie rule underdog wins): underdog side 52.4 percent, favorite 47.6. On integer lines the underdog is 53.3 percent (CI 51.0 to 55.7) but this swings by season (2024 45.5, 2025 47.8 partial). On half-point lines underdog 51.6 percent (n=1,358, not separable from 50). On the 38 recent NO EDGE games: underdog 17, favorite 21, market side 20. Conflicting small signals, so no mechanical rule is adopted. Tiebreak for NO EDGE games: Zac's read; if none, the frozen underdog (tiny long-run lean, costs nothing). Worth knowing: all 57 card lines were half-point lines (0 integers), so the commissioner appears to hook the market number; a card +3.5 on a market 3 hands the underdog the ties.

**Data error:** nflverse closing line for JAX at BAL Week 9 reads +3.0 while the Thursday market was home -10 (JAX won 33-10). Grades use the frozen line so they are unaffected. Queued as FF-2026-11-10-01. The labeler prefers the Thursday Odds API market and falls back to nflverse.

## Fix 4: Thursday saved-lineup workflow

Updated in `Fantasy-Football\CLAUDE.md` (new section "Weekly workflow fixes", point 1). Zac sends the saved-lineup screenshot every Thursday; the Thursday rerun starts from it; if it does not arrive the rerun still runs from the API read, is labeled "SAVED LINEUP NOT CONFIRMED BY SCREENSHOT" and asks for it in the first line.

**API test, 2026-11-10:**
- `TYPE=lineup`, `myfranchise`, `lockedLineup`, `franchises`, `nflSchedule`: rejected ("Invalid request", on both the api and www44 hosts).
- `TYPE=liveScoring&W=10` and `TYPE=weeklyResults&W=10` both return franchise 0012's 17 starters flagged `starter`, and they agree with each other. The Week 10 saved lineup is the Week 9 lineup carried forward (Goff, Robinson, White, Flowers, Golden, Jefferson, J. Williams, LaPorta, Bates, Davis, Hutchinson, Gibbens, Okereke, Strnad, Mukuba, Sanker, Scott). `read_saved_lineup.py <week>` prints it with names.
- Not verified: whether a lineup edited Thursday morning shows up here before kickoff. The earlier Week 9 Thursday attempt reported nothing, so test it Thursday and trust the screenshot if they differ.
- Useful by-product: `weeklyResults` also returns each franchise's `optimal` lineup after the week, and `playerScores` returns every player's league-scored points. Both are in the calibration.
- Week 9 finding: the saved lineup differed from the report's 17 (TE LaPorta not Hockenson, DL Davis not Wonnum). The report assumed an older sheet.

## Could not verify

- Wednesday practice status for historical weeks other than 7 and 9 (nflverse keeps only the last status).
- Frozen Monday lines for any game before week 6 (nflverse has no opening lines; Odds API history is not confirmed available on the key).
- Whether the saved lineup is readable pre-lock after a Thursday edit.
- Why league lineups run 13 points above the sim.
- The Week 6 play-sim comparison (no play sim file).

## Files

`Fantasy-Football\fixes-2026-11-10\`: `run_weekly_calibration.py`, `build_dataset.py`, `lineup_calib.py`, `recal.py`, `injury_rule_test.py`, `injury_rule_zac.py`, `wed_dnp_check.py`, `pickem_labels.py`, `pickem_backtest.py`, `pickem_rules_test.py`, `read_saved_lineup.py`, plus the csv outputs. Log: `D:\WKP\logs\fantasy-football-director.md`. Decisions queued: FF-2026-11-10-01 to 03 in `D:\WKP\logs\DECISIONS.md`.
