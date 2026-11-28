# Watch week scorecard (paper only)

Generated 2026-11-27 18:24 UTC. Config hash counted: 3452cb683492d6a1. Source files: decisions.jsonl (1364 lines, 1364 with this hash), paper-trades.csv (96 rows, 96 with this hash). DEMO: fictional data, not a result.

Not financial advice. No real order was ever placed. Trades are our own simulated fills.

## Frozen config
- Counting only lines and trades carrying hash 3452cb683492d6a1. Lines under any other hash (not counted): 0.
- 2026-11-27T18:22:19Z: hash 3452cb683492d6a1 (previous None). first start

## Labeled assumptions (placeholders, not measured)
- Fill at the next 1-hour bar open after the signal bar closes (main ledger) or at the next session open (Zac-can-act ledger), plus slippage 5 bps each side.
- Fee line 0 bps each side, sell regulatory fee 0.0 bps. Placeholders until set from a real source.
- Data feed iex (IEX only, thinner than the full tape). Simulated book start 100000.00 (a placeholder size, judge results in percent).
- Exits are checked against hourly high and low. If stop and target are both inside one bar, the stop is assumed to hit first. A gap through the stop fills at the worse of the stop and the bar open.
- End rule: last day 2026-12-24. Open trades are closed at the last mark seen by the final scan (close to, not equal to, the official close).

## Counts (each traceable to lines in decisions.jsonl)
- COUNTED decisions (score 70 or higher, once per setup): 40. TRADE 27, WATCH 13. These are the decisions that count toward the 50.
- Evaluation lines (TRADE, SKIP, WATCH), all logged, NOT the counted number: 1225. TRADE 28, WATCH 31, SKIP 1166.
- Fresh evaluations (a new closed bar was actually scored): 776. TRADE 28, WATCH 31, SKIP 717.
- Fresh evaluations by regime tag: RANGE 225, UPTREND_VOLATILE 551.

## MAIN ledger (fills at the next hourly bar open)
- Paper trades opened: 26. Closed: 26 (of those closed by the end rule at the last mark: 2). Still open, not in P and L: 0.
- Win rate (net above zero, at the run's own 5 bps haircut): 10 of 26 = 38.5 percent.
- Average R (net P and L over risk at entry): 0.172 over 26 trades.
- Gross P and L (before slippage and fees): 1872.38
- Net P and L (after slippage and fees): 1210.87 (1.211 percent of the simulated book)
- Max drawdown on realized net P and L: 3843.68 (3.674 percent of peak equity). Open positions and unrealized swings are not in this figure.

Haircut view (slippage each side recomputed from raw prices; 15 and 30 are stress levels, not measured; share counts were sized at the run's own haircut):

| Slippage each side | Net P and L | Per trade | Percent of book | Positive |
|---|---|---|---|---|
| 5 bps | 1210.86 | 46.57 | 1.211 | yes |
| 15 bps | -112.13 | -4.31 | -0.112 | no |
| 30 bps | -2096.61 | -80.64 | -2.097 | no |

Small-account sizing view: the same signals sized as if the account were $60 (fractional shares allowed, same risk tiers, same 25 percent cap; fractional stop orders and the broker's minimum order are NOT VERIFIED):

| Slippage each side | Net P and L on $60 | Percent of $60 |
|---|---|---|
| 5 bps | 0.7499 | 1.250 |
| 15 bps | -0.0308 | -0.051 |
| 30 bps | -1.2020 | -2.003 |

Sizing view detail: size bound by position cap 26. Positions under $1 of notional (likely below a broker minimum): 0 of 26.

Results split by regime tag at entry:

| Regime | Trades | Wins | Net P and L |
|---|---|---|---|
| RANGE | 9 | 5 | 2522.02 |
| UPTREND_VOLATILE | 17 | 5 | -1311.15 |
- Day trades (opened and closed the same ET day): 2. Most in any rolling 5 trading days: 1 (limit 3). Most in one calendar month: 1 (limit 3). Entries refused by the PDT guard: 0. Rule text NOT confirmed, holidays not modeled.

Every closed trade (trace):

| Trade | Symbol | Opened by decision (jsonl line) | Closed by decision (jsonl line) | Exit | Gross | Net | R |
|---|---|---|---|---|---|---|---|
| T0001 | DLTA | D000042 (42) | D000084 (84) | stop | -294.1 | -318.8 | -1.04 |
| T0003 | DEMX | D000060 (60) | D000183 (183) | target | 994.58 | 969.24 | 2.467 |
| T0005 | ALFA | D000136 (136) | D000200 (200) | stop | -452.69 | -477.24 | -1.026 |
| T0004 | CHAR | D000081 (81) | D000201 (201) | target | 859.82 | 834.4 | 2.462 |
| T0002 | BRVO | D000062 (62) | D000225 (225) | target | 833.61 | 808.25 | 2.461 |
| T0008 | DEMX | D000270 (270) | D000333 (333) | stop | -380.03 | -405.08 | -1.032 |
| T0007 | CHAR | D000262 (262) | D000386 (386) | target | 1001.73 | 975.95 | 2.467 |
| T0009 | ALFA | D000306 (306) | D000432 (432) | stop | -403.99 | -429.16 | -1.03 |
| T0006 | BRVO | D000249 (249) | D000439 (439) | time_stop | 590.11 | 564.46 | 1.58 |
| T0010 | DEMX | D000388 (388) | D000550 (550) | time_stop | 6.42 | -18.96 | -0.051 |
| T0011 | BRVO | D000473 (473) | D000573 (573) | target | 823.51 | 797.4 | 2.459 |
| T0012 | DEMX | D000566 (566) | D000664 (664) | stop | -381.95 | -407.26 | -1.032 |
| T0013 | BRVO | D000744 (744) | D000849 (849) | target | 951.21 | 925.08 | 2.465 |
| T0014 | DEMX | D000742 (742) | D000882 (882) | target | 836.48 | 810.58 | 2.46 |
| T0015 | DEMX | D000916 (916) | D000958 (958) | stop | -381.44 | -407.37 | -1.033 |
| T0018 | CHAR | D000950 (950) | D000988 (988) | stop | -400.24 | -426.01 | -1.031 |
| T0016 | BRVO | D000925 (925) | D001027 (1027) | stop | -432.46 | -458.35 | -1.029 |
| T0019 | DEMX | D001021 (1021) | D001039 (1039) | stop | -382.63 | -408.2 | -1.032 |
| T0017 | ALFA | D000937 (937) | D001126 (1126) | time_stop | -287.1 | -313.02 | -0.848 |
| T0020 | BRVO | D001129 (1129) | D001175 (1175) | stop | -344.36 | -369.69 | -1.035 |
| T0022 | BRVO | D001207 (1207) | D001243 (1243) | stop | -330.92 | -356.2 | -1.037 |
| T0024 | BRVO | D001258 (1258) | D001307 (1307) | stop | -371.78 | -397.07 | -1.033 |
| T0025 | DEMX | D001256 (1256) | D001319 (1319) | stop | -338.9 | -363.76 | -1.035 |
| T0023 | DLTA | D001241 (1241) | D001347 (1347) | stop | -318.82 | -344.01 | -1.038 |
| T0021 | CHAR | D001201 (1201) | D001360 (1360) | end_rule | 343.32 | 317.68 | 0.735 |
| T0026 | DEMX | D001331 (1331) | D001361 (1361) | end_rule | 133.0 | 108.01 | 0.269 |

## ZAC-CAN-ACT ledger (fills only at the next trading session open; go-live is judged here)
- Paper trades opened: 22. Closed: 22 (of those closed by the end rule at the last mark: 1). Still open, not in P and L: 0.
- Win rate (net above zero, at the run's own 5 bps haircut): 9 of 22 = 40.9 percent.
- Average R (net P and L over risk at entry): 0.127 over 22 trades.
- Gross P and L (before slippage and fees): 1232.06
- Net P and L (after slippage and fees): 675.64 (0.676 percent of the simulated book)
- Max drawdown on realized net P and L: 3500.94 (3.371 percent of peak equity). Open positions and unrealized swings are not in this figure.

Haircut view (slippage each side recomputed from raw prices; 15 and 30 are stress levels, not measured; share counts were sized at the run's own haircut):

| Slippage each side | Net P and L | Per trade | Percent of book | Positive |
|---|---|---|---|---|
| 5 bps | 675.64 | 30.71 | 0.676 | yes |
| 15 bps | -437.19 | -19.87 | -0.437 | no |
| 30 bps | -2106.42 | -95.75 | -2.106 | no |

Small-account sizing view: the same signals sized as if the account were $60 (fractional shares allowed, same risk tiers, same 25 percent cap; fractional stop orders and the broker's minimum order are NOT VERIFIED):

| Slippage each side | Net P and L on $60 | Percent of $60 |
|---|---|---|
| 5 bps | 0.4263 | 0.710 |
| 15 bps | -0.2341 | -0.390 |
| 30 bps | -1.2248 | -2.041 |

Sizing view detail: size bound by position cap 22. Positions under $1 of notional (likely below a broker minimum): 0 of 22.

Results split by regime tag at entry:

| Regime | Trades | Wins | Net P and L |
|---|---|---|---|
| RANGE | 8 | 4 | 1306.93 |
| UPTREND_VOLATILE | 14 | 5 | -631.29 |
- Day trades (opened and closed the same ET day): 5. Most in any rolling 5 trading days: 3 (limit 3). Most in one calendar month: 3 (limit 3). Entries refused by the PDT guard: 0. Rule text NOT confirmed, holidays not modeled.

Every closed trade (trace):

| Trade | Symbol | Opened by decision (jsonl line) | Closed by decision (jsonl line) | Exit | Gross | Net | R |
|---|---|---|---|---|---|---|---|
| Z0001 | DLTA | D000042 (42) | D000088 (88) | stop | -294.1 | -318.8 | -1.04 |
| Z0003 | CHAR | D000081 (81) | D000202 (202) | target | 853.85 | 828.6 | 2.462 |
| Z0005 | ALFA | D000136 (136) | D000208 (208) | stop | -459.77 | -484.47 | -1.026 |
| Z0004 | DEMX | D000060 (60) | D000219 (219) | target | 994.62 | 969.2 | 2.467 |
| Z0002 | BRVO | D000062 (62) | D000284 (284) | time_stop | 201.12 | 176.12 | 0.545 |
| Z0007 | DEMX | D000270 (270) | D000344 (344) | stop | -380.09 | -405.03 | -1.032 |
| Z0006 | CHAR | D000262 (262) | D000387 (387) | target | 994.53 | 968.91 | 2.467 |
| Z0008 | ALFA | D000306 (306) | D000433 (433) | stop | -402.51 | -427.6 | -1.03 |
| Z0010 | BRVO | D000473 (473) | D000574 (574) | target | 814.1 | 788.29 | 2.459 |
| Z0009 | DEMX | D000388 (388) | D000591 (591) | time_stop | 85.71 | 60.61 | 0.165 |
| Z0011 | BRVO | D000744 (744) | D000850 (850) | target | 933.95 | 908.02 | 2.464 |
| Z0012 | DEMX | D000742 (742) | D000900 (900) | target | 823.11 | 797.39 | 2.46 |
| Z0014 | DEMX | D000916 (916) | D000977 (977) | stop | -375.23 | -400.65 | -1.033 |
| Z0016 | CHAR | D000950 (950) | D000989 (989) | stop | -400.33 | -425.92 | -1.031 |
| Z0013 | BRVO | D000925 (925) | D001028 (1028) | stop | -429.7 | -455.43 | -1.029 |
| Z0015 | ALFA | D000937 (937) | D001067 (1067) | stop | -349.76 | -375.33 | -1.035 |
| Z0017 | DEMX | D001021 (1021) | D001078 (1078) | stop | -382.9 | -407.94 | -1.031 |
| Z0018 | BRVO | D001129 (1129) | D001191 (1191) | stop | -344.45 | -369.6 | -1.035 |
| Z0020 | BRVO | D001207 (1207) | D001269 (1269) | stop | -333.17 | -358.3 | -1.036 |
| Z0022 | DEMX | D001256 (1256) | D001320 (1320) | stop | -338.9 | -363.76 | -1.035 |
| Z0021 | DLTA | D001241 (1241) | D001348 (1348) | stop | -318.82 | -344.01 | -1.038 |
| Z0019 | CHAR | D001201 (1201) | D001364 (1364) | end_rule | 340.8 | 315.34 | 0.735 |

## Buy-and-hold baseline (SPY, same IEX bars, from the scan marks in decisions.jsonl)
- SPY mark 390.22 at 2026-01-19T14:31:00Z (line 1) to 432.03 at 2026-03-06T20:00:00Z (line 1364): 10.716 percent.
- main ledger net P and L as percent of the book: 1.211 percent (versus baseline 10.716).
- zac ledger net P and L as percent of the book: 0.676 percent (versus baseline 10.716).

## Plan checks (the numbers, not a verdict)
- Counted decisions: 40 (the plan asks for 50).
- Zac-ledger closed trades: 22. About 20 means the plumbing works, 50 or more is needed before any edge claim.
- Zac-ledger net P and L at 30 bps each side: -2106.42 (NOT positive). The plan passes only if this is positive.
- This scorecard is evidence for the trading-director and Zac. It never says go live.

## Skip reasons (SKIP lines)
- no setup on the latest closed bar: 717
- already holding or signal pending: 428
- max open positions reached: 21

Checks for QA: totals above equal the sums of the table rows; decision ids resolve to decisions.jsonl lines; if results look too good, check the haircut and the stop-first assumption before believing them.
