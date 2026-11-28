# QA pass 3: wkt-alpaca-watcher after changes 4 and 5 (2026-11-27)

Verdict: PASS WITH NOTES. No blockers. Paper only: no orders, no keys printed, GO-COUNTED.flag not created, no push, product files not edited. My scratch work is in D:\WKP\scratch\qa3\.

## (a) Tests
- `python -I tests\test_watcher.py` run in the background from the product folder: Ran 101 tests in 1530 s (about 25 minutes, the machine was loaded and the other bench ran its suite at the same time). Result OK. 101 "... ok" lines, 0 FAIL, 0 ERROR. Matches the expected 101.

## (b) Demo rerun and my own recount
Ran `python -I run.py --demo` after my suite finished. Wrote my own recount script (D:\WKP\scratch\qa3\recount.py) over paper-trades.csv and decisions.jsonl, not the scorecard code.

| Item | CHANGES Final | My recount | Scorecard |
|---|---|---|---|
| main opened / closed / wins | 26 / 26 / 10 | 26 / 26 / 10 | 26 / 26 / 10 |
| main gross / net | 1872.38 / 1210.87 | 1872.38 / 1210.87 | same |
| main day trades | 2 | 2 | 2 |
| zac opened / closed / wins | 22 / 22 / 9 | 22 / 22 / 9 | same |
| zac gross / net | 1232.06 / 675.64 | 1232.06 / 675.64 | same |
| zac day trades | 5 | 5 | 5 |
| decision lines | 1364 | 1364 | 1364 |
| counted decisions | 40 | 40 | 40 |
| PDT cancels | 0 | 0 (only 4 CANCEL lines: 3 end rule, 1 gap) | 0 refused |

- One trade by hand: T0001 and Z0001 (same entry, 106 shares, raw in 234.34186, raw out 231.56729, 5 bps haircut each side, no fees): gross -294.10, net -318.80, logged -294.10 and -318.80. Match.
- Console line shows closed 24 + 21 plus 3 closed by end rule, which equals 26 and 22 once added. Consistent.
- Unclosed positions: none in either ledger.

## Day trades per rolling 5 trading days (the "demo never overshoots" claim)
From the CSV, entry bar date versus exit bar date in ET, weekday-only calendar:
- main: 2 day trades, peak 1 in any 5 trading days, peak 1 per month. Limit 3, not exceeded.
- zac: 5 day trades, peak 3 in any 5 trading days, peak 3 in a month (Feb 2, Mar 3). Limit 3, reached but not exceeded.
- Most entries opened in one day: 3 in both ledgers. No day with 4.
- Claim CONFIRMED. Note it is a weak proof by itself (peak sits exactly at the limit, and the demo never tries a 4th same-day entry); the engine test is the real proof, see (d).

## (c) README versus config.yaml
All match: PDT 3 in 5 trading days and 3 per month; fills.session_open_fill_hour_et 10 (session_bars first hour still 9, last 15); end_rule.last_day "2026-12-24"; stop 2 x ATR; target 2.5R; kill switch 5 percent; weekly limit 6 percent; max open positions 4; score 70 minimum, risk 0.5/1/2, max position 25, time stop 5, Monday only at 90; max loss per trade 3 percent; step-up off. README says five whitelisted paths, alpaca.py shows 3 paper-host paths plus 2 data-host paths, which is five.
- Config hash recomputed from the parsed config.yaml with the product's own config_hash: 7a0c25c7a871b79b. Matches.
- Dec 24 2026 being a Thursday and Dec 25 a holiday: I did not re-fetch the NYSE calendar (not retried), so NOT VERIFIED by me. Weekday arithmetic only.

## (d) Claims for changes 4 and 5, traced
- Pre-fix code: four same-day entries all fill. CONFIRMED. I copied the product to scratch, removed only `open_entry_dates=open_today` from the pdt_block call, and ran the new test class. The new four-entry test fails with `['AAA','BBB','CCC','DDD'] != ['AAA','BBB','CCC']`. The other tests in that class and the main-fill tests passed (7 tests, 1 failure). With the real code the test passes in my full run.
- Old demo-out was stale: not provable now (old file overwritten). Consistent with this: I reran the demo with change 5 reverted in a scratch copy and got main gross 2077.96 / net 1415.48 and zac 21 opened, zac net 1063.64, which equals the CHANGES "before change 5" numbers (2077.96, 1415.48, Zac 21). So the before and after story for change 5 is CONFIRMED.
- Demo effect of change 4 (0 entries refused before and after): after, 0 PDT cancels confirmed. The before side I did not rerun separately (pre-fix demo peak 3 and 5 day trades stated in CHANGES): NOT VERIFIED.
- S4 label removal: scorecard PDT bullets (lines 56 and 121) have no overshoot label, README Known limits says FIXED. Justification (demo shows 0 overshoots, engine test) holds per my count above. Bullet format otherwise looks as before.
- Change 5 code: `_try_fill` main branch is `b["t"] >= due and hour >= fh`, matches the description. All main opens fill at ET hours 10 to 15 (counts 10:8, 11:5, 12:4, 13:5, 14:1, 15:3), Zac opens all at hour 10. CONFIRMED.
- Guard logic read in risk.pdt_block: open entries opened on `today` count against both the rolling and monthly limits; yesterday's open entry is not counted. Matches the text.
- "No output file format changed": CSV columns in logio.TRADE_COLUMNS are 27 columns including mode and day_trade, no new key seen in jsonl or state. There is no git history for the folder, so I cannot diff against the earlier version. See (f).

## (e) CODE-SHA256.txt
Recomputed SHA-256 of all 20 files (sorted, excluding __pycache__, demo-out, logs and the list file): all 20 match the list, none missing, none extra.

## (f) Format drift versus earlier QA reports
Earlier reports (qa, qa-pass2, tester, tester-pass2) name TRADE_COLUMNS fields (parts, score, setup, regime, reason, r_net, pnl_net, config_hash) and the scorecard PDT line; all still present. A full before and after diff is NOT POSSIBLE: the folder is untracked in git (`?? software/wkt-alpaca-watcher/`) and the old demo-out was overwritten.

## Notes (none block)
1. The demo scorecard and decisions carry config hash f0e3a3e57d6920cc, not 7a0c25c7a871b79b, because run_demo swaps the symbol list, market gauge and regime.min_breadth_symbols. That is by design but CHANGES Final could say so: the demo does not exercise the real hash or the 20 symbol list.
2. README says tests take about 5 minutes. With the machine loaded it took 25 minutes. Not wrong at idle, but the tester and next reader should expect more time.
3. The PDT proof in the demo is thin (peak equals the limit, no 4th same-day attempt). The engine test carries the proof, and it fails on the pre-fix code as it should.
4. The guard is conservative (can refuse an entry that would never have been day-traded) and the PDT rule text is unconfirmed. README says both. Open item for trading-director, not a defect.
5. CODE-SHA256 covers files only. Nothing logs the code hash into config-history.jsonl or the scorecard header (pass 2 suggested this idea). The SHA list is manual, so a code edit during the watch weeks is only caught if someone reruns the check.
6. Another bench ran the suite and a smoke at the same time in the same folder. My demo numbers are self-consistent (recount equals scorecard) and I reran the demo only after my own suite finished, but I cannot rule out a concurrent write by the other bench to demo-out.

## Could not verify
- NYSE Dec 24 early close and Dec 25 holiday (not re-fetched).
- Live Alpaca behaviour (no network smoke run by me; the tester bench owns that).
- Pre-fix demo for change 4 (only the engine test reproduced).
- Old demo-out and file format diffs (no copy, no git history).
- PDT rule text itself (stated unconfirmed in the product).
