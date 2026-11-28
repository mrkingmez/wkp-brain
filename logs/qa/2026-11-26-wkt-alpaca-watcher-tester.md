# QA: wkt-alpaca-watcher, software-tester pass, 2026-11-26

Scope: D:\WKP\software\wkt-alpaca-watcher\ (security and correctness, report only). No network call, no --smoke or --counted, no APCA value read. Extra tests: D:\WKP\scratch\qa-wkt\edge_tests.py and demo_guard.py.

## Real results
- tests: `python -I tests\test_watcher.py` -> Ran 44 tests, OK.
- demo offline: copy of the project in scratch\qa-wkt\copy run with socket.socket, create_connection and getaddrinfo replaced by raisers, and an os.environ wrapper that records APCA names. Result: demo ran (245 scans, 26 opened, 24 closed), no socket opened, APCA names touched: none, wrote only copy\demo-out\ (4 files).
- edge tests: 44 cases run, see findings.

## Verdict
No path found for a key to reach a file, log, print or exception text. No path found to an order, write or non-paper endpoint. GO-COUNTED.flag does not exist right now. One blocker for the counted week (F1), several should-fix.

## Findings (file, line, severity)
- F1 BLOCKER for counted week. run.py:42-46 and 118-121. One failed or unreadable /v2/clock call after the first scan of the day makes live_scan return None, and the loop treats that as market closed: writes the daily note and scorecard, then exits. Test: market open all along, 3rd clock call fails once, run ended after 3 calls with rc 0. A 429 or network blip kills the watch mid-session and the day is lost.
- F2 should-fix. engine.py:75-82 vs 89-93. Pending signals fill in step 1, before the kill-switch check, and nothing blocks fills while killed. Test: killed=True with a pending signal, it still filled. Window is one scan normally, longer if the next bar is missing.
- F3 should-fix. engine.py:75-91. Day-roll baseline is taken after overnight stop-outs and after gap marks. Test: 1000 shares gapping 100 to 70 on a 100k book, start_equity stored 69,965, kill switch not tripped. A gap loss never counts toward the -5 percent.
- F4 should-fix. logio.py:32-47 and engine.py:137. Decision line and trade row are appended before state.json is saved at end of scan. Test: restore the pre-scan state and replay, paper-trades.csv shows OPEN ids T0001, T0002, T0001, T0002 and 5 duplicate decision ids. Scorecard pair_trades (scorecard.py:32-36) then overwrites by id.
- F5 note. logio.py:20-24. state.json is loaded with no validation. Empty, text, binary, `[]`, `{}`, `null`, truncated all crash (JSONDecodeError, UnicodeDecodeError, TypeError, KeyError). Fail closed, but no readable message and atomic save only guards the writer. scorecard.py:19 same for a bad decisions.jsonl line.
- F6 note. alpaca.py:25. urlopen uses the default opener, which follows redirects and forwards custom headers. Verified in the stdlib: redirect_request copies APCA-API-KEY-ID and APCA-API-SECRET-KEY to the new host. Only reachable if Alpaca (or a proxy) answers 3xx. Fix is a no-redirect handler.
- F7 note. alpaca.py:88. `(r.data.get("bars") or {}).items()` crashes with AttributeError if "bars" is a non-empty list. Uncaught, ends the loop (fail closed, but see F1 for what that does to the run).
- F8 note. alpaca.py:48-51. Whitelist checks scheme, hostname, path, feed but not port or url params: `:8443` and `;x=1` pass. Harmless GETs to the same two hosts. Uppercase host passes (urlparse lowercases), trailing dot, trailing slash, userinfo trick, dot-dot and double feed all blocked.
- F9 note. alpaca.py:43, 70. The client object keeps the secret in `_headers`. No code prints or logs it today (tests prove files, stdout, stderr clean for sentinel values), but any future repr of the client or a debug print of vars() would leak.
- F10 note. guards.py:34. Gate is os.path.exists only: a directory named GO-COUNTED.flag passes. run.py:79-86: `--scorecard --counted` and `--daily-note` write into the counted folder without the flag (test: scorecard.md created with no flag).
- F11 note. engine.py:186-194. Time stop counts distinct dates present in the data, not sessions. Test: one missing session day moved the exit from the 6th calendar session to the 7th (2026-01-13 vs 2026-01-12).
- F12 note. engine.py:75-77. A pending signal whose symbol returns no bars stays forever and logs nothing (positions log HOLD_UNKNOWN, pending do not). A position whose symbol is later removed from config also sits at HOLD_UNKNOWN forever.
- F13 note. Hardcoded thresholds that should be config or are undocumented: indicators.py EMA 20 and 50 (line 126), BB 20 and 2.0 (70, 127), MACD 12/26/9 (77), stochastic 14 and 3 (83), ADX period 14 (98, and enrich line 128 calls adx(bars) so rules.atr_period does not reach it), volume average window 20 (122), hi20 lookback 20 (124); scoring.py mood weights 0.4/0.3/0.3 (51-53), average dollar volume window 20 (35), range epsilon 1e-12 (105). scoring.py docstring and README claim every deciding number is in config. Config validation (config.py:22-33) has no type or range checks: negative kill switch, string max_open_positions and equity 0 were accepted.
- F14 note. Live and demo differ. Demo view_at shows the forming bar with open only; live Alpaca returns the partial bar, so exits in step 1 can fire on partial highs and lows (real-time, not look-ahead, but the demo never exercises it).
- F15 note. No requirements.txt and README never mentions the one dependency (PyYAML, MIT). A fresh machine fails at import. README steps use hardcoded Python path and run.py:24 hardcodes D:\WKP\Investing\watch-week, run_watcher.ps1:9 hardcodes the Python path (LOCAL-PATHS says never hardcode).
- F16 note. run.py:110-122. Started on a non-trading day the loop sleeps 30 s forever. No lock file, two instances would double-write.
- F17 note. Tests leave temp folders in D:\WKP\scratch (wkt-test-*), never cleaned.

## Checked and fine
Fills at next bar open, closed-bar filter b.t+1h<=now (engine.py:96), indicators causal, hi20 excludes the current bar, stop-first when both in one bar, gap-down fills at open, 25 percent cap and cash bind in sizing, pending counted in slots, NaN/inf/None/string/impossible bars give UNKNOWN FAIL, out-of-order bars sorted, endless pagination stops at 20, exception text type-only, secrets absent from every output in tests.

## Not verified
Live behavior of any kind (no network by order). Alpaca response shapes, extended-hours bars in IEX hourly data, rate limits, early-close days. Duplicate-timestamp bars are not de-duplicated or flagged (case ran, no error, effect on indicators not measured). Concurrency. Windows file-lock behavior. PyYAML version and license read from nothing on disk (stated from knowledge, MIT).
