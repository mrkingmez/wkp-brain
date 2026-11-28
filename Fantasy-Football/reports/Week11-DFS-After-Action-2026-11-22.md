# Week 11 DFS After-Action (2026-11-22)

DFS only. Fun money, no QA pass, nothing entered, nothing spent, no IRFL files touched, no shared code or defaults changed. Permanent record: `Fantasy-Football\dfs\LEARNING-LEDGER.md`. Code: `dfs\wk11_after_action.py`, `dfs\wk11_backtest.py` (import dk_gpp unchanged); scratch runs in `scratch\wk11\`.

Sources: ESPN final box scores (all eight early games final, HOU played Thursday) via `dashboard\dfs_live.py`; entries `D:\Draft Kings\Week 11\DKEntries_week11_LINEUPS_UPLOAD.csv`; pool and sim `sun\own_est_week11.csv` and `data\ff-simulator\dfs_draws_2026_wk11.npz`. The harness reproduces the 7 entered lineups and their scores exactly, so the baseline is valid.

## 1. Our 7 entries (actual DK points)

| Entry | Actual | Sim mean | Error | Source label |
|---|---|---|---|---|
| 5344796795 (Prescott, Lamb, Pickens, Pollard, Saints, Henry) | 153.9 | 125.4 | +28.5 | rotowire |
| 5344796823 (Mahomes, E. Johnson, Kelce) | 137.7 | 120.8 | +16.9 | rotowire |
| 5344796753 | 125.6 | 127.1 | -1.5 | rotowire |
| 5344796345 | 120.0 | 129.2 | -9.2 | model |
| 5344796338 | 109.1 | 112.6 | -3.5 | rotowire |
| 5344796776 | 104.4 | 120.8 | -16.4 | model |
| 5344786514 | 93.7 | 115.0 | -21.3 | rotowire |

Cash: Zac says $1.50 back on $7. No standings file exists in the week folder and the cash line is not on disk, so WHICH entry cashed is NOT KNOWN. The 153.9 is the likely one (inference, unverified).
Seed correction: Shakir WAS in an entry (5344796345, 18.3). Kelce was in only one entry (5344796823, with E. Johnson; Johnson was also in 5344796753).

## 2. The winner's 9 players (205.6, salary $50,000)

| Slot | Player | Salary | Sim mean | Sim p90 | Actual | Pct of sim draws at or below actual | Our own-est % | Our exposure | Pos rank by sim mean |
|---|---|---|---|---|---|---|---|---|---|
| QB | Prescott | 6700 | 21.7 | 36.2 | 38.9 | 93 | 31.5 | 1 | 2 of 14 |
| RB | E. Johnson | 6000 | 15.4 | 29.0 | 27.3 | 88 | 13.1 | 2 | 8 of 25 |
| RB | Pollard | 6500 | 21.5 | 37.6 | 14.0 | 30 | 37.9 | 3 | 2 of 25 |
| WR | Bateman | 3200 | 4.9 | 11.5 | 14.7 | 96 | 0.5 | 0 | 34 of 44 |
| WR | Pickens | 6800 | 16.7 | 31.9 | 26.8 | 82 | 39.2 | 3 | 3 of 44 |
| WR | Shakir | 5100 | 11.2 | 22.8 | 18.3 | 83 | 12.0 | 1 | 11 of 44 |
| TE | Kelce | 4700 | 10.4 | 21.5 | 25.4 | 95 | 23.2 | 1 | 2 of 19 |
| FLEX | Lamb | 8800 | 21.5 | 38.1 | 33.2 | 83 | 49.3 | 2 | 1 of 44 |
| DST | Saints | 2200 | 4.7 | n/a | 7.0 | n/a | 1.0 | 2 | 11 of 14 |

Sim mean of the winner lineup 128.8 (p90 173.8, p99 215.2); 205.6 sits at the 98.2 percentile of our own 20,000 correlated sims. The sim called it a possible but rare outcome. Eight of nine were in the pool, all nine were playable; Bateman at $3,200 was a minimum-salary punt (rank 32 of 44 WR on points per dollar), Shakir was rank 8.
Why Bateman and Shakir: no injury or role gap. Bateman was a low-sim punt (4.9 projected) who hit his 96th percentile; Shakir was a modest value pick (rank 11 by sim) that we used once. The sim was right about both on average.
Slate calibration: per-player bias +0.6 on 110 players (QB +0.4, RB +0.4, WR +1.6, TE -0.7, DST -0.1), MAE 4.75, corr 0.67. The mean is fine; this slate's miss was variance in the highest-total game (DAL v TEN total 54.5, finished 81).

## 3. Why the builder could not make the winner

Our own rules rejected it before any cap mattered:
- Ownership sum 207.7 (our estimate) is over every tier cap (core 200, balanced 160, leverage 135).
- Only 4 chalk-pool skill players (Pollard, Pickens, Kelce, Lamb); the pool minimum is 5 in every tier.
The exposure caps (player 4 of 7 in code, the brief said 3; QB 2; overlap 5) did not bind: highest actual exposure was 3.

## 4. Hindsight backtest, one change at a time (selection on the pre-game sim, scored on actual; one slate = noise)

Control (model only, caps 4/2/5, seed 11): 152.8, 149.2, 120.0, 116.8, 104.4, 98.2, 82.2, mean 117.6. Seeds 12 and 13 controls: means 124.2 and 128.2. So the seed noise alone is about 10 points of mean.

| Variant (seed 11) | Best | Mean | Lineups at 140 or more |
|---|---|---|---|
| player cap 3 (tighter) | 152.8 | 129.0 | 2 |
| player cap 5 | 152.8 | 126.2 | 3 |
| player cap off | 152.8 | 122.3 | 2 |
| QB cap 3, QB cap off, overlap 6, overlap off | 152.8 | 117.6 | 2 |
| all three off | 152.8 | 119.9 | 2 |

Hypothesis from the brief (caps kept the core out): NOT SUPPORTED. The best lineup never changes, and mean moves in both directions (tighter cap scored higher than looser), which is fallback-solve noise.

| Variant | Seed 11 mean (best) | Seed 12 | Seed 13 | Avg mean vs control avg 123.3 |
|---|---|---|---|---|
| Control | 117.6 (152.8) | 124.2 (153.7) | 128.2 (146.6) | 123.3 |
| C1 ownership caps +60 (260/220/195) | 137.8 (152.5) | 125.7 (164.3) | 134.9 (150.7) | 132.8 (+9.5), better in 3 of 3 |
| C2 chalk-pool minimum 5 to 4 | 129.0 (171.9) | 117.7 (141.9) | 129.5 (166.5) | 125.4 (+2.1), 2 of 3 |
| C3 both (seed 11 only) | 132.5 (174.9) | | | |

Hindsight oracle (best possible lineup on actuals under the rules): core as coded 216.6, balanced 207.3, leverage 182.7; with the ownership cap off, core is still 216.6; with pool minimum 4, 228.3. Hindsight, not a target.
Also: stored candidates containing all of Prescott, Lamb, Pickens, Pollard: 5 (C1), 6 (C2), 9 (C3); control count not taken; the sim's top-ranked candidate by mean scored 126.9 to 134.2.
Other checks: punts (25 sub-$3,500 skill players) averaged 5.0 actual vs 5.2 projected, only 3 reached 13 or more (12 percent): no punt rule needed. RotoWire-sourced entries averaged 124.0 (5), model-built 112.2 (2), noise.

## 5. Rule changes for Week 12 (none applied; dk_gpp.py defaults unchanged)

1. R1 TEST: ownership caps +60 as one labeled test entry vs control, same slate. Strongest signal, still one slate and our own ownership estimate.
2. R2 TEST: chalk-pool minimum 4 as one labeled test entry, lower priority.
3. R5 TEST: two lineups as full game stacks in the highest-total game vs control.
4. R3 DROP the cap hypothesis; keep caps 4/2/5. R4 DROP punt rule.
5. Process fix: label every lineup with its source (model, rotowire, test and rule ID) before lock and archive the exact entered file; the entered 7 came from a patched scratch copy (`scratch\noon\dk_gpp_rw.py`) not the repo script, so the repo cannot reproduce them without it. Decision for the owner of shared code: whether to fold the RotoWire injection into dk_gpp.py as an option (not done here).

## 6. Not verified

Which entry cashed; the cash line, field size and payout; the real ownership of the winner (ours is an estimate); six zero-actual pool players (see ledger). Local nflverse Week 11 stats are incomplete so ESPN box scores were the source. Nothing here was QA-checked.
