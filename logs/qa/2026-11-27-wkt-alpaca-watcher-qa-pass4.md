# QA pass 4: wkt-alpaca-watcher after changes 6, 7, 8 (2026-11-27)

Verdict: PASS WITH NOTES. No blockers. Paper only: no network, no orders, no keys printed, GO-COUNTED.flag not created (not in D:\WKP\Investing\watch-week\), no push, no product file edited (no file in the product folder is newer than my scratch start). My scratch work: D:\WKP\scratch\qa4\ (suite\, demo\, base\, recount.py, dt.py, cmp.py, h.py, runcls.py).

## (a) Tests
- Full suite from a scratch copy, `python -I tests\test_watcher.py`: Ran 112 tests in 527.8 s, OK. 112 "ok" lines, 0 FAIL, 0 ERROR (suite.txt).
- New classes on the pre-change code (D:\WKP\scratch\sd-w678\base-copy, copy of it with the new test file dropped in, run by runcls.py): 11 tests ran, 9 fail or error, 2 pass.
  - TestZacPendingExpiry (4): 4 of 4 fail or error (3 FAIL, 1 ERROR on the missing config key).
  - TestBadEntryBarTOnOpenPosition (3): 2 fail or error, 1 passes. The pass is `test_good_entries_are_unchanged...`, a no-regression guard, expected.
  - TestPdtUsesFillBarDate (4): 3 fail, 1 passes (`test_live_same_day_case_is_unchanged`, a no-regression guard, expected).
  - Caveat: some of the change 6 and 7 failures on base come from the missing config key or KeyError, not only from behavior. The change 8 failures are pure behavior (4 of 4 filled), matching the claim.

## (b) Demo and my own recount
Ran `run.py --demo` in a scratch copy, wrote recount.py over paper-trades.csv and decisions.jsonl (not the scorecard code).

| Item | Claim | My recount |
|---|---|---|
| main opened / closed / wins | 26 / 26 / 10 | 26 / 26 / 10 |
| main gross / net | 1872.38 / 1210.87 | 1872.38 / 1210.87 |
| main day trades | 2 | 2 (entry bar date vs exit bar date, ET) |
| zac opened / closed / wins | 22 / 22 / 9 | 22 / 22 / 9 |
| zac gross / net | 1232.06 / 675.64 | 1232.06 / 675.64 |
| zac day trades | 5 | 5 |
| decision lines / counted | 1364 / 40 | 1364 / 40 |
| PDT cancels / expired / HOLD_UNKNOWN | 0 / 0 / 0 | 0 / 0 / 0 (4 CANCEL lines: 1 gap, 3 end rule) |
| demo hash | 3452cb683492d6a1 | 3452cb683492d6a1 in the output |

- Max entries opened in one day: 3 in both ledgers. Scorecard PDT lines: main peak 1, zac peak 3 of limit 3, 0 refused.
- Fresh demo vs the product's existing demo-out: paper-trades.csv and decisions.jsonl are byte-identical raw (same hash because same code and config), so equal after hash masking too. Behavior equals the earlier run.
- My first day-trade count used the exit timestamp and gave 3 and 4 because end-rule closes carry a later timestamp; counting by bar date gives 2 and 5. Claim stands, this was my script, not the product.
- Real hash differs from demo hash by design (run_demo swaps symbols, gauge, breadth setting). CHANGES says so.

## (c) CHANGES, README, config, code
- Config hash recomputed with the product's own config_hash on config.yaml: b559c847b5717f4a. Matches CHANGES, CODE-SHA256.txt header and README-free text.
- CODE-SHA256.txt: all 20 listed files match, none missing, only unlisted file is the list itself.
- README versus config.yaml and engine.py: expiry text (more than 2 weekdays after the signal date, CANCEL, never filled at stale price) matches config `zac_ledger.max_pending_sessions: 2` and `_expired` (cancel when waited > limit; checked in scan and in `_try_fill`). Main has no expiry, only the 1 ATR gap cancel: stated in README and true in code (`_expired` returns False unless ledger is zac). end_rule.last_day 2026-12-24 is a Thursday (checked by weekday arithmetic). Fill hour 10, session_bars 9 to 15, PDT 3 in 5 days and 3 a month, five whitelisted paths: all match. Change 8 in code: `fill_date = nxt["t"]` ET date passed to `pdt_block` and `_open_entry_dates`. Change 7 in code: try/except around `entry_bar_t`, HOLD_UNKNOWN, counted as opened on the fill date. Both as described. Test counts per step in CHANGES (101, 105, 108, 112) add up.
- README run-time statement "5 to 25 minutes": my run took 8.8 minutes, tester 7.5, earlier loaded run 25. Statement is a fair range.
- NYSE calendar facts (Dec 24 early close, Dec 25 closed, Fri 11-27 half day): NOT verified by me (no network). Weekdays confirmed only.

## (d) Tester notes N1 and N2
- N1 (`_expired` reads `sig["signal_bar_t"]` unguarded, so a damaged pending Zac signal now raises in scan even with no bars). I read the code: confirmed at engine.py line 272. The engine always writes `signal_bar_t` (line 239) and state is journaled and rewritten in whole, so only a hand-damaged state.json triggers it. Severity LOW. Does NOT block the counted run. If run.py loop has no per-scan try/except (I saw none), a trigger would stop the loop, which is loud and not silent, and a restart would hit it again; this is an acceptable fail-loud for an input only a human edit can create. Optional fix after the run window opens is not wanted (it would change code hash mid-count): leave it, record it.
- N2 (`_check_exit` still raises on a missing `entry_bar_t`, line 372). Same hand-damaged condition, stated by the developer. LOW. Does not block.
- Other tester notes N3 to N6 (holidays not modeled, naive date string, main has no expiry, suite time) agree with what I read. Holidays: the counted window 2026-11-30 to 2026-12-24 contains no NYSE holiday, so N3 cannot bite in it (my reasoning from the calendar claim, which I did not re-fetch).

## (e) smoke-2026-11-30-checklist.md against run_watcher.ps1 and code
Accurate on: the command (`powershell -File run_watcher.ps1 --smoke` from the product folder), ps1 copies the three variables User to Process and prints none; smoke writes to watch-week\test (`test_dir()`), not the counted folder; smoke prints `smoke scan:`, `calls:` (status and request id for account and positions), `facts` with `account_safe_values` and `positions_count`, `info` with `extended_hours_bars_dropped`, `gauge_bar_start_times_et`, `symbols_under_min_bars_now`, `projected_next_open_symbols_under_min_bars`, and `regime`; smoke runs with `clock_required=False`, so it scans before the open, as the checklist expects; counted loop start 09:25 matches README.
Notes (none block):
1. `gauge_bar_start_times_et` holds times of day only ("09:00" and so on), so it cannot show that the last scored bar is Friday 12:00 ET. The date is in `info.gauge_last_bar_utc` (expect 2026-11-27T17:00:00Z) and in `smoke-preflight.json`. The checklist should name that key.
2. The code check covers only engine.py, wkt\config.py and config.yaml. alpaca.py and guards.py (the safety files) and the other 17 are not checked; a one-line loop over the whole list would be better. Get-FileHash prints uppercase, the list is lowercase: say compare ignoring case.
3. The expected config hash is left as "see the Final section"; give b559c847b5717f4a directly and say to read `config_hash` in `smoke-preflight.json` (the console does not print it).
4. "No Monday bar is scored before 10:00 ET" is trivially true before 09:20; harmless.
5. Fri 11-27 half day and 12:00 last bar: not verified by me. The author says it is reasoned from the 11-27 runs, no Monday pre-open run exists.

## Other notes
- Change 8 leaves `step_up_check` on the scan date, step-up is OFF, no effect.
- Each scan with a bad open-position `entry_bar_t` writes a new HOLD_UNKNOWN line (log noise only, fails safe).
- Security: no key-like strings or APCA values in py, yaml, md, ps1, txt; no order or write verbs in wkt or run.py (only a scorecard sentence mentioning "minimum order").

## NOT verified
- Real Alpaca behavior, holidays, DST around fill dates (no network, no --smoke by me).
- `run.py --loop` end to end, Task Scheduler.
- NYSE calendar facts quoted above.
- Whether the PDT rule text matches the broker (unconfirmed in the product itself).
- Before and after file-format diff beyond what the demo output and the tester's key-set check show (folder is untracked in git).

Counted run: nothing here blocks it. Suggested small doc fixes in the checklist (notes e1 to e3) can be made without touching code or the code hash.
