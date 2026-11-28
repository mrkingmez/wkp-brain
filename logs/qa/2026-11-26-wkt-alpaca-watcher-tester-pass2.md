# WKT Alpaca watcher, tester pass 2 (2026-11-26)

Scope: D:\WKP\software\wkt-alpaca-watcher\. Report only, nothing fixed. No network call, no --smoke or --counted, no APCA values read, no GO-COUNTED.flag (checked: still absent in D:\WKP\Investing\watch-week\). Scratch only under D:\WKP\scratch\qa-wkt2\ (attack.py, attack2.py, edge_old.py, ts.py, outputs attack.out, suite.out).

## Verdict
No blocker found for the counted week. One should-fix I would close first (end rule not enforced inside the loop after a Friday after-close restart), plus five more should-fix items. Secret-leak and order-endpoint checks are clean.

## 1. Test suite (real output)
`python -I -W ignore tests\test_watcher.py` -> `Ran 85 tests in 667.671s`, `OK`, 85 of 85 lines "ok", 0 fail, 0 error. Run took about 11 minutes, not 5 (I was running my own scripts at the same time, so part of that is contention). Evidence: scratch\qa-wkt2\suite.out.

## 2. Old findings F1 to F17 (re-run of my 44 edge cases, adapted to the new signatures)
Old file ran 44 cases; two needed edits (loop case now needs client_factory and sleep, `_check_exit` signature changed). Output above in the run; summary:

| F | Was | Now | Evidence |
|---|---|---|---|
| F1 | one clock failure ends the run | FIXED | loop survived a failed 3rd clock call, still scanning after 6 clock calls |
| F2 | pending fills while killed | FIXED | killed=True, pending cleared, 0 positions opened |
| F3 | day baseline taken after gap losses | FIXED | start_equity 100000 stored, killed=True on the 30 percent gap |
| F4 | crash between writes duplicates ids | FIXED for real crashes | A1 (die after journal, before append): replayed, 0 duplicate ids. A2 (die after append, before clear): recovered 0, 0 duplicates. A3 (die after decisions, before trades): trade row replayed once, 0 duplicates. Old harness (state rolled back by hand) still duplicates, see N7 |
| F5 | unreadable state.json crashes with raw trace | MOSTLY FIXED | 7 corrupt-file cases all give a StateError with a readable message. Valid JSON with wrong types (cash as string, positions as list, pending null) still crashes with TypeError or AttributeError (A12), see N8. Scorecard: torn decision line is skipped with a warning, but a valid-JSON line that is a list, int, null, or lacks decision_id still crashes (J1) |
| F6 | redirects forward key headers | FIXED | redirect_request returns None |
| F7 | bars as list crashes | FIXED | returns "bad bars shape" |
| F8 | whitelist ignores port and `;x=1` | STILL OPEN, note | `:8443` and `;x=1` still allowed, same two hosts, GET only |
| F9 | client repr leaks keys | FIXED for repr, str, f-string | all print "AlpacaReadOnly(paper, keys hidden)". `vars(client)` still holds the secret in _headers (note) |
| F10 | directory as flag, --scorecard --counted bypass | FIXED | directory named GO-COUNTED.flag refused, `--scorecard --counted` raises GuardError |
| F11 | time stop counts dates present, not sessions | STILL OPEN, note | ts.py: all days present exits 2026-01-12, one missing session day exits 2026-01-13 |
| F12 | pending for a symbol with no data is silent | CHANGED, still open | each scan now logs "already holding or signal pending" for that symbol, but nothing says the data is missing, and the pending signal holds a slot forever (D4) |
| F13 | hardcoded thresholds, weak validation | PARTLY FIXED | negative and zero numbers now rejected. ADX period and indicator windows still hardcoded. New gaps in section 4 (N9) |
| F14 | exits can fire on a partial forming bar | STILL OPEN, note | engine.py `_check_exit` still reads forming bars. Not re-run (needs live data) |
| F15 | no requirements, hardcoded paths | PARTLY FIXED | requirements.txt and README step exist. run.py:25 `D:\WKP\Investing\watch-week` and run_watcher.ps1:9 Python path still hardcoded (LOCAL-PATHS says never hardcode) |
| F16 | non-trading-day loop, no lock file | STILL OPEN, plus the worse case in S1 | no lock file, two copies would double-write |
| F17 | tests leave temp folders | STILL OPEN, note | 754 `wkt-test*` folders in D:\WKP\scratch after this suite run. The suite also rewrites software\wkt-alpaca-watcher\demo-out\ in the repo |

## 3. Findings on the new code

### Should-fix (fix before the counted week if cheap)
- S1 End rule not enforced inside the loop. run.py loop (the `confirmed_closed and last_date` branch, about line 190) applies the end rule only if THIS process scanned today. Test E3: process started Fri 2026-12-04 17:00 ET (after close) with an open position, last_day = 2026-12-04 -> loop polls the clock forever, ended=False, position still open (stopped my test after 7 polls). Same in E6: if the last day has no scan in this process (holiday, all-day data outage, restart after the close) the loop never ends and would trade the next Monday. The start-of-process check only fires when the date is already past last_day (E4 works: closes at last mark, rc 0, no scan). Fix idea: inside the loop, if now's ET date is past last_day, or it is last_day and the market is confirmed closed, apply close_out. Exposure is narrow (restart on last_day after the close) and no scheduler restart exists in the repo.
- S2 "ended" cannot be reset by a config change, and the message says it can. After close_out, changing config.yaml gives a new hash but `state.json` keeps `ended: true` (test: ended stays True, hash changed). run.py prints "Change config.yaml (new hash, counts restart) to run again", which is false. Combined with S3 this is a trap.
- S3 end_rule.last_day is not validated. validate() accepts "12/04/2026", "2026-12-4", "Friday", "" and an unquoted YAML date (which becomes a date object and raises TypeError at run.py start). `"12/04/2026"` compares as past, so a counted start would immediately close_out and set ended=True permanently (S2). Fix idea: validate as ISO date string.
- S4 PDT guard overshoots its own limit. engine `_try_fill` counts only CLOSED day trades; entries opened the same scan or still open are not counted (F2: with 2 booked, two entries both opened, `Z0001, Z0002`). The shipped demo shows it: Zac ledger "Most in any rolling 5 trading days: 4 (limit 3). Most in one calendar month: 4 (limit 3)", "Entries refused by the PDT guard: 0". The scorecard reports it honestly, but the guard did not do its job. Holidays not modeled means a 5-weekday window holds 4 trading days around a holiday (no holiday in 11/30 to 12/04).
- S5 Both ledgers fill at the open of the 09:00 ET bar. With first_bar_start_hour_et = 9, the first bar after the overnight gap is the 09:00 bar, whose open is the first IEX print after 09:00, a pre-market trade. Same for time-stop exits. The Zac ledger is meant to be "next trading session open" and is the go-live judge, and Zac works 8 to 5. Config comment admits the 30-minute pre-open part but the fill price is still the pre-market print. Could not verify against real bars (no network). This is a rule decision for trading-director.
- S6 config validation lets bad numbers through and the run keeps going. `.nan` and `.inf` accepted for starting_equity, daily_kill_switch_pct, max_loss_per_week_pct, max_loss_per_trade_pct, max_position_pct, haircut, atr_stop_multiple, reward_multiple (B3, 9 of 9 accepted). A NaN or inf kill switch or weekly limit never trips (loss_pct >= nan is False). Also accepted: step_up.min_counted_trades -1 or "20" (string, crashes later on compare), step_up.regime "BOGUS" (step-up silently never fires), min_score 0, no_kill_trading_days -3. Needs a typo to trigger, so should-fix not blocker.

### Notes
- N1 Config hash. Key order and comments do not change it (good). Int vs float does: starting_equity 100000 vs 100000.0 gives a different hash, so retyping a value restarts the counts (B2). Mixed int and str dict keys raise TypeError in config_hash (B5). NaN hashes stably (B4). A hash change mid-experiment keeps the same book, cash and open positions (B7), only the counts restart, and a history row is written (good).
- N2 Float keys: haircut views `[5,15,30.0]` with expectancy 30 validates, then `str(30)` vs `str(30.0)` raises KeyError '30' at the first fill after a Zac-ledger close (B8). Default config uses ints, so not hit today.
- N3 Episode counting works as designed: same setup on consecutive bars counts once, a restart mid-episode keeps the episode, a skipped scan does not break it (C2, C3). Gaps: a Monday watch-day line at 75 is counted as WATCH (never tradable) and uses up the episode, so Tuesday's tradable TRADE line is "counted: False" (C4). A score that dips under 70 and returns counts again (75, 69, 75 gave True, False, True) so threshold whipsaw inflates the count. A setup that flips pullback to breakout counts again (C1). Demo: 39 counted of 1225 evaluation lines, min counted score 70.0, 13 of the 39 are WATCH lines.
- N4 Journal recovery edge cases: state with journal but files already ahead recovers 0 and writes no duplicates (A2). State rolled back to an older copy while the files are ahead gives repeating decision ids (A4: 3 duplicates in 6 lines) and nothing at startup detects it. Torn last row of paper-trades.csv (A6): the next row is appended onto the same line and the new row is lost from the parsed file, and recovery would treat the torn row as present. decisions.jsonl has the leading-newline protection (A5 fine), the CSV does not. Journal with a missing key or wrong type crashes at start (A7, A8). Only by file damage or hand edit.
- N5 Zac ledger. Signal on the last bar of Friday fills Monday 09:00 bar for both ledgers (D1). Mid-Friday signal: main fills the same day, Zac does not (D2). Thanksgiving gap fills Friday 11/27 (D3). Gap over 1 ATR cancels main, Zac still fills, as designed (D6). Main kill switch does not stop the Zac ledger (D7, separate books, by design). A stale pending signal (14 days old, data returns) fills at the old bar and replays the exit retroactively (D5): no staleness cancel.
- N6 Marks have no staleness check: the mark is the last bar's close even if that bar is days old (thin IEX symbol), and close_out uses it. Mark of NaN, 0 or negative is left open as HOLD_UNKNOWN (good, E2b). A mark of None or a string in state.json crashes equity().
- N7 Regime (regime.py): forming bar of today is dropped even with absurd values (G1). NaN, None, string, zero, negative in gauge bars give UNKNOWN (G4). Short or empty data gives UNKNOWN. Duplicate daily bars are not removed (G2: bars 260 to 520, SMA changes). Stale gauge history (last bar 12 days old) is accepted and tagged (G5), only the last date is logged. A bar stamped 00:00Z lands on the previous ET day (G7), real Alpaca stamps 04:00 or 05:00Z. An UNKNOWN from bad data is stored for the day, only a missing fetch is retried every 10 minutes (G9, G8).
- N8 State file wrong-type contents (cash string, positions list, pending null, zac a string) still crash (A12). Only by hand edit.
- N9 Step-up with enabled true: all conditions met gives 3.0 percent (H1). Each single failing condition returns None. Kill 3 days ago blocks, 5 weekdays ago passes. Step-up applies to the main ledger too, using the Zac ledger's expectancy (H4: both fills got 3.0). It is capped at max_loss_per_trade_pct by validate (risk_pct 5.0 rejected). OFF in config.
- N10 Weekly limit: hit on Friday, the Monday scan clears it and re-baselines at the lower equity (93000), so the limit is per week, not cumulative (I1, by design). Boundaries: 6.0 percent exactly trips, 5.99 does not (I3). NaN equity or start does NOT trip (returns False), unlike the docstring "UNKNOWN fails closed" (risk.py: `loss_limit_hit` guards None and start<=0 but not NaN). Blocked week cancels pending (I4).
- N11 Scorecard: mixed-hash folder counts only the requested hash and lists the rest as "not counted" (J3, 5 lines). Demo cross-check from raw files: counted lines 39 match; ids unique; main closed 26 sum 1540.11 matches the 5 bps haircut view 1540.11; Zac closed 22 sum 821.48 vs view 821.46 (0.02 rounding); 0 of 22 Zac fills on the same ET date as the signal bar; trade bar hours ET 9 to 15 only; one config hash. Damaged inputs: torn JSON line skipped with warning; valid JSON non-dict, missing decision_id, non-UTF8 bytes in the trades CSV, a bad ts_utc in daily-note, a damaged state.json in daily-note all raise (J1, J2, J5, J6). If daily-note raises at loop end the day's scorecard is skipped.
- N12 PyYAML is the only dependency (MIT, from memory, not verified online).

## 4. Security pass
- Keys: grep for APCA, key, secret, token, password, PK/AK key patterns across all .py, .ps1, .yaml, .md, .json, .jsonl, .csv in the watcher folder (excluding tests). Only variable NAMES appear (guards.py:5, run_watcher.ps1:5, README:30). No key value in any file, including demo-out. I did not read any environment variable values.
- Order endpoints: grep for orders, POST, DELETE, PATCH, PUT, requests, httpx, socket, subprocess, os.system, eval, exec finds nothing except `method="GET"` (alpaca.py:31) and the word "orders" in README and scorecard text (prose about stop orders). Whitelist is 3 paper paths (/v2/account, /v2/positions, /v2/clock) and 2 data paths, all GET. `/v2/orders`, base path, `/v2/`, other host, sip feed, missing feed all blocked (K3).
- Paper URL: assert_paper_url refuses trailing slash, uppercase, http, other host, empty, None, trailing space (K5). Exact string match only.
- Redirects: _NoRedirect.redirect_request returns None (K3, K4), so a 3xx raises instead of forwarding headers.
- Error text: transport exceptions report only the type; Result and client repr hide the secret. `vars(client)` and `client._headers` hold the secret in memory (note).
- Network: port 8443 and `;x=1` pass the whitelist (F8, same hosts, GET only).
- GO-COUNTED.flag does not exist. Counted gate holds.
- Absolute paths: run.py:25, run_watcher.ps1:9 (see F15). Not secrets.

## 5. Could not verify
- Real IEX bar behavior (09:00 bar open being a pre-market print, partial forming bars), clock calls, rate limits: needed network, forbidden.
- Whether anything auto-restarts the watcher (no scheduled task in the repo, I did not search Task Scheduler).
- That `--counted --loop` behaves over a real 5-day week. Only mocked clocks and fake clients.
- Whether Robinhood and FINRA PDT rules match the guard (README says not confirmed).
- Real PyYAML licence text.

## Counts
Suite 85 of 85 OK. Old edge cases: 44 adapted and re-run, 1 loop case rewritten, F1 to F17 table above. New attack cases: about 95 (A 12, B 9, C 4 plus 4 rerun, D 7, E 9, F 4, G 10, H 4, I 4, J 7, K 6) plus demo cross-check.
