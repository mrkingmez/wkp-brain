# DFS LEARNING LEDGER

DFS ONLY. Nothing here touches the IRFL dynasty league, its sims, lineups or picks.
Why this file exists (Zac, 2026-11-22): the point of DFS is to train the agent to know what works and what does not, using free data. Entries are fun money. Paid feeds are a someday item, never pitched as a spend. See `memory\project-dfs-learning-goal.md`.
Agents never enter lineups or spend. Zac enters. This ledger records what he entered and what happened.

## 1. Slate ledger (one row per slate, newest at the bottom)

| Week | Contest | Entries and fee | Return | Winning score | Our best | Sim vs actual (our 7 lineups) | Rule tested | Result | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 2026 W11 Sun early | NFL $15K First Down (Early Only), 14 teams | 7 x $1 = $7 | $1.50 (Zac's word; which entry NOT KNOWN, no standings file on disk) | 205.6 (Zac's screenshot; rebuilt from ESPN box scores, matches to the decimal) | 153.9 (entry 5344796795, the Prescott, Lamb, Pickens, Pollard, Saints entry) | Lineup sim means 112.6 to 129.2 vs actual 93.7 to 153.9; per-lineup error -21.3 to +28.5, mean error about -0.9, no bias. Per-player bias +0.6 on 110 players (QB +0.4, RB +0.4, WR +1.6, TE -0.7, DST -0.1), MAE 4.75, corr 0.67 on projections of 8 or more | (a) exposure caps 4 / QB 2 / overlap 5 vs looser; (b) ownership cap +60; (c) chalk-pool minimum 5 to 4 | (a) not the lever: best score identical (152.8) in every cap variant; (b) lifted the 7-lineup mean in 3 of 3 seeds (avg +9.5, 123.3 to 132.8); (c) mixed (avg +2.1, one seed worse) | (a) DROP as a lever, keep caps; (b) RETEST on Week 12 test entries; (c) RETEST, no change yet |

Cash line, field size and payout table were not on disk for Week 11. Record them from DK's contest page when Zac has them, so the "cash" column becomes real.

## 2. Baselines (saved, compare every change to one of these)

| Baseline | What it is | Where |
|---|---|---|
| WK11-CONTROL | dk_gpp.py as coded 2026-11-22: tiers core/balanced/leverage, own caps 200/160/135, chalk-pool min 5, player cap 4, QB cap 2, overlap 5, seed 11, 120 solves per tier, field 17800. Model-only 7 scored 152.8, 149.2, 120.0, 116.8, 104.4, 98.2, 82.2 (mean 117.6); seeds 12 and 13 means 124.2 and 128.2 | `dfs\wk11_backtest.py`, `dfs\wk11_after_action.py`, scratch runs in `scratch\wk11\` |
| WK11-AS-ENTERED | the 7 Zac entered, reproduced exactly by the harness (scores 153.9, 137.7, 125.6, 120.0, 109.1, 104.4, 93.7). 5 of the 7 were RotoWire-file lineups injected as extra candidates by the patched copy `scratch\noon\dk_gpp_rw.py`, not by repo dk_gpp.py | `D:\Draft Kings\Week 11\DKEntries_week11_LINEUPS_UPLOAD.csv` |

dk_gpp.py defaults are UNCHANGED. No default changes until the retest in section 3 repeats on at least two more slates.

## 3. Rule queue (tested or testable, one change at a time)

| ID | Rule | Evidence so far | Status | How to test in Week 12 |
|---|---|---|---|---|
| R1 | Raise the lineup ownership caps by 60 points (core 260, balanced 220, leverage 195) | The winning lineup has our ownership estimate sum 207.7, over every tier cap (core 200), so the builder could never produce it. With the cap raised the 7-lineup mean rose in all 3 seeds: 137.8 vs 117.6, 125.7 vs 124.2, 134.9 vs 128.2. Single slate, hindsight, ownership numbers are our own estimate | RETEST | One test entry labeled "R1 own cap +60" against WK12-CONTROL, same slate |
| R2 | Chalk-pool minimum 5 to 4 | Winner has only 4 chalk-pool skill players (Pollard, Pickens, Kelce, Lamb), so it also fails min 5. Seeds: +2.1 average, one seed worse. Oracle lineup with min 4 scored 228.3 vs 216.6 with 5 | RETEST, lower priority than R1 | One test entry labeled "R2 pool min 4", compare to control |
| R3 | Player cap 4, QB cap 2, overlap 5 | Brief hypothesis was that these capped the Prescott/Lamb/Pickens/Pollard core. Not supported: best score stayed 152.8 under cap 3, 5, off, QB cap 3 or off, overlap 6 or off. Mean moved 117.6 to 129.0 only through which fallback lineups got solved | DROP the hypothesis, keep the caps | none |
| R4 | A cheap punt rule (a sub-$3,500 pass catcher on purpose) | Bateman ($3,200, rank 34 of 44 WR on sim mean, 96th percentile of his sim draws) and Ted Hurst ($3,000, 22.6 points, 0.3 percent owned) hit, but across 25 sub-$3,500 skill players the share reaching 13 or more was 12 percent (3 of 25) and the sim mean (5.2) matched the actual mean (5.0). The sim was right about them, they were lottery tickets | DROP, nothing to fix | none |
| R5 | Force 2 of 7 lineups to be full game stacks in the slate's highest-total game (QB plus 2 pass catchers plus 2 bring-backs) | DAL v TEN had the top total (54.5) and finished 81 points, 26 over. Three of our 7 lineups held the DAL core, only one held it together with Pollard. The winner total was at the 98.2 percentile of our own 20,000 sims (sim p99 215.2), so the sim did not call it impossible | RETEST | Two test entries labeled "R5 game stack" vs the model-only control, same slate |
| R6 | Candidate source: RotoWire lineups injected | The 5 RotoWire entries averaged 124.0, the 2 model entries 112.2 (n=2 vs 5, noise). The one 153.9 came from a RotoWire lineup. No conclusion | RETEST, keep the source label on every lineup | Label each lineup "model" or "rotowire" in the ledger before lock |

## 4. Test entries (free and cheap contests)

Free and cheap contests are where we A/B rules.
- Every test lineup carries ONE label: the single rule it tests and the baseline it is compared to (example: "R1 own cap +60 vs WK12-CONTROL").
- Change one rule per test lineup. Two changes in one lineup means nothing is learned.
- Compare only inside the same slate. Free and paid fields differ in size and ownership (field size and ownership NOT measured here; record both from the contest page), so a result from a free contest is not compared to a paid contest or to a past week. The same-slate pair (test vs control) is the only valid comparison.
- Log the pair in section 1 and the rule queue status in section 3 the same day.
- Agents never enter lineups. Zac enters. The agent hands over a labeled file and a one-line note per test lineup.

## 5. How to run each week

1. **Before lock:** save the exact lineups Zac enters (copy the uploaded file into the week folder under `D:\Draft Kings\Week N\`), with source labels (model, rotowire, test and its rule ID). Save the pool, sim and ownership files used. Do this before the first kickoff of the slate, not after.
2. **After the slate is final:** score every entry and every pool player from final box scores (`dashboard\dfs_live.py` parse_game, ESPN, free). Record the winning score and Zac's return and the cash line if he has them.
3. **Review:** sim mean and p90 vs actual for the winner's players and for our lineups; which rule rejected the winning shape (oracle and constraint checks as in `dfs\wk11_backtest.py`); who was in the pool and at what rank.
4. **One change at a time:** change one rule, compare to the saved baseline on the same slate, rerun on 3 seeds so noise shows. Never edit dk_gpp.py defaults off one slate.
5. **One slate is noise.** Judge across weeks. A rule moves from RETEST to KEEP only after it helps on at least 3 slates and does not hurt on the others. A rule moves to DROP after 3 slates with no help.
6. Update section 1 (row), section 3 (status), the lessons file DFS section, and one row in `logs\agent-runs.md`.

## 6. Data and honesty notes (Week 11)

- Actual points come from ESPN box scores via `dashboard\dfs_live.py` parse_game. The local nflverse stats file only held the Thursday game at the time, so `dk_actual.py` could not be used. Saved as `D:\Draft Kings\Week 11\ACTUAL_week11_espn.csv`. Hand check: Prescott 38.9 and Lamb 33.2 match Zac's screenshot; the rebuilt winning lineup sums to 205.6.
- Six pool players showed 0 actual because they were missing from the box score or truly scored 0 (Kevin Coleman Jr., Ja'Kobi Lane, Roschon Johnson, Juwan Johnson, Isaac TeSlaa, Reggie Virgil). Juwan Johnson is in the box score at 0.0 and sat in entry 1. The other five were never in an entered lineup.
- The ownership numbers are our own estimate (dk_own.py), not measured. The winning lineup's real ownership is NOT KNOWN.
- The seed note said we had neither Bateman nor Shakir: Shakir WAS in our entry 5344796345 (18.3 points). Bateman was in the pool (rank 32 of 44 WR on points per dollar) but in no lineup.

## 7. Tool change log

| Date | Change | Default | Regression | Baseline kept |
|---|---|---|---|---|
| 2026-11-22 | `dk_gpp.py` gains `--rotowire <csv>` (RotoWire lineups added as extra candidates, label rotowire; same rules and sim) and `--patched "1,3"` (lineup numbers a person hand-edited), plus two new output files per build: `lineup_sources.csv` (source label per lineup: own, rotowire, patched) and `entered_archive\<timestamp>_<template> - FILLED.csv` (exact built file, copied into the outdir before lock). Approved by Jarvis for Zac. dk_gpp.py is used only by the DFS build (`dk_own_build.py` runs it as a subprocess; `wk11_backtest.py` imports it; `dk_validate.py` only mentions it in a comment). No IRFL or other cycle imports it. | flag OFF: existing outputs byte-identical | Same Week 11 inputs, seed 11, flag off, pre-change file (git HEAD) vs new: build_report.txt, lineups_detail.csv, upload_new_lineups.csv, FILLED, reference_pool.csv all IDENTICAL. Flag ON with `D:\Draft Kings\Week 11\DK_upload_10363_20000.csv` reproduces the 7 entered lineups exactly (sun6), labels: lineups 1, 2, 4, 6, 7 rotowire, 3 and 5 own | WK11-CONTROL is the flag-off output; pre-change copy `scratch\wk11\dk_gpp_before_rotowire.py` |

Manual step each slate: if Zac uploads a file that differs from the built FILLED (hand patch, different template), copy the exact uploaded file into the week folder's `entered_archive\` before lock and re-run with `--patched` or note the change in section 1.

## Note 2026-11-22 (Zac): no DFS Week 12
Zac is not playing DFS in Week 12 (starts Wed 2026-11-25). The queued Week 12 tests (ownership cap +60, two game stacks, pool minimum 4) and the fantasy-football-director's graded re-drill are on hold until Zac says DFS resumes. Do not build Week 12 DFS lineups.
