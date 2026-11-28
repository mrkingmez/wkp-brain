# QA: wkt-alpaca-watcher, qa-director pass, 2026-11-26

Scope: D:\WKP\software\wkt-alpaca-watcher\. Code, data, claims. No network call, no --smoke or --counted, no APCA value read. Scratch scripts: D:\WKP\scratch\qa-check.py, qa-check2.py.

## Verdict: PASS WITH NOTES (safety and correctness). GO-COUNTED.flag: NOT created, see "What blocks the flag".

## Results I ran
- `python -I -W ignore tests\test_watcher.py`: Ran 49 tests, OK.
- `python -I run.py --demo`: 245 scans, 1225 decision lines (+50 non-evaluation lines = 1275), 26 opened, 24 closed. Wrote demo-out\ (decisions.jsonl, paper-trades.csv, scorecard.md, state.json). No daily-notes.md in demo-out (see N3).
- Scorecard recomputed by hand from paper-trades.csv and decisions.jsonl: gross 1557.33, net 945.73, wins 9 of 24, avg R 0.158, max drawdown 3695.24 (3.531 percent), evaluation lines 1225 (TRADE 27, WATCH 31, SKIP 1167), fresh 763 (27/31/705). All match scorecard.md. Per-trade gross and net recomputed from raw and filled prices: 0 mismatches of 24. Every close decision_id and every "signal Dxxxxxx" id resolves to a jsonl line. No duplicate decision ids.
- Rule checks on the demo data: no TRADE under 70; no Monday TRADE under 90 (15 Monday WATCH lines); max notional/equity at fill 0.2500 (cap holds; a fixed 25,000 test fails only because equity grows); 4 max concurrent; stop, target (2.5R) and 5 bps haircut match the config on all 26 opens. Kill switch never fired in the demo (0 KILL lines), proven only by unit tests (test_kill_switch_*, test_overnight_gap_counts_toward_kill_switch, test_pending_signal_is_cancelled_while_killed).
- GO-COUNTED.flag does not exist (checked). Counted gate is code-enforced for live, `--scorecard --counted` and `--daily-note` paths (F10 fixed, directory no longer opens the gate).
- No em dashes in README, config, code, tests.

## Locked rules versus config.yaml and code
| Rule (wkt-locked-rules.md) | config / code | Result |
|---|---|---|
| Score under 70 no trade | rules.min_score_to_trade 70, risk.gate_reason | MATCH |
| Risk 0.5/1/2 at 70/80/90 | risk_per_trade_pct, risk.risk_pct_for | MATCH |
| Max position 25 percent | max_position_pct, size_shares min of risk, cap, cash | MATCH |
| Stop 2 x ATR on 1h bars | atr_stop_multiple 2.0, engine._try_fill | MATCH |
| Target 2.5R | reward_multiple | MATCH |
| Time stop 5 days stocks | time_stop_sessions 5, _check_exit | MATCH (crypto 3 days is out of scope) |
| Kill switch -5 percent, open positions keep stops | daily_kill_switch_pct 5, engine step 1 and 2 | MATCH |
| Monday only at 90+ | watch_days [Mon], hot_score 90 | MATCH |
| Max 4 open | max_open_positions 4, slots count pending too | MATCH |
| 1-minute checks weekdays 9:30 to 5:00 PM | scan_interval 60, loop runs only while /v2/clock is open | DEVIATION: session close, not 5 PM. Plan explains it (extended hours unverified) but README and config do not say so (N5) |
| Data: yfinance for stocks | Alpaca IEX | DEVIATION authorised: Zac 2026-11-26 in WATCH-WEEK-PLAN |
| Twilio text on kill switch | not built | Plan says live phase only, fine |

## Hard requirement list
| Requirement | Result |
|---|---|
| Keys by env name only | PASS. guards.load_env names variables only, tester and tests prove no value in files, stdout, stderr. I did not read values. |
| Exact paper URL assert | PASS. `url != PAPER_URL`. A trailing slash on APCA_API_BASE_URL would refuse to start (fail closed, error names no value). I could not check Zac's value. |
| No order endpoint | PASS. Whitelist of 3 paper paths and 2 data paths, GET only, no redirects (F6 fixed), test greps source for order paths and write verbs. |
| X-Request-ID on every call line | PASS with note. Every decision line carries request_ids; in the clock-closed SKIP path and on a network error the list can be `[None]` (N7). Account and positions ids go to smoke-preflight.json, not decisions.jsonl. |
| Outputs decisions.jsonl, paper-trades.csv, daily-notes.md, scorecard.md | PARTIAL. First, second and fourth exist in demo. daily-notes.md is written only by the live loop at close or by `--daily-note`; the demo does not produce it (N3). |
| Scorecard numbers trace to lines | PASS (hand check above). |
| Demo offline | PASS. test_demo_made_trades_offline patches socket; demo imports no network code path. |
| Fri 2026-11-27 half day via /v2/clock | PASS in design. No hardcoded close; loop stops when clock says closed and a scan happened that day. Live behavior NOT VERIFIED (no network by order). |

## Tester findings status (checked in code)
- F1 fixed in run.py (unreadable clock is not "closed", sleeps 30 s). No regression test drives the main loop (N1).
- F2, F3, F6, F7, F10 fixed and tested (TestTesterFindings).
- F4, F5, F8, F9, F11 to F17 still open as stated.

## Findings and notes (none is a safety blocker)
- N1 should-fix. F1 fix has no test that runs `main(--counted --loop)` with a clock that fails once. The counted week depends on it. Fix: a loop test with a fake client.
- N2 should-fix. F4 open: decision and trade rows are appended before state.json is saved. A crash mid-scan then restart duplicates T-ids and decision ids and the scorecard pairing overwrites by id. A counted week that crashes once has a corrupted ledger. Fix: write state first or make appends idempotent, or log restarts.
- N3 note. README says daily-notes.md is written per session day; demo-out has none, so the output set was not shown end to end. Fix: have the demo call write_daily_note, or say so in the README.
- N4 note. Devils-advocate amendments adopted in WATCH-WEEK-PLAN are not in the build: config hash on every log line (amendment 1), decision count at score 70+ once per setup (2), Zac-can-act ledger (6), haircut 5/15/30 view (10), $60 sizing view (5), end rule closing open trades at last close (4), PDT counter (8), regime tag. grep for hash, regime, PDT, baseline finds nothing in code. Gap rule (7) and UNKNOWN is FAIL (9) are built. The scorecard counts every fresh evaluation, not the plan's "decision".
- N5 note. README and config.yaml claims that are not true: config.yaml line 1 "every threshold lives here, not in code" contradicts F13 and the README; README says indicator periods are "from wkt-locked-rules.md" but that file lists none (they are the ported old WKT numbers); README says the program "reads account status" but counted mode never calls /v2/account or /v2/positions (smoke only); session window is 9:30 to 4:00, not the locked 5 PM, unstated.
- N6 note. F15 half fixed: requirements.txt exists, README still never says to pip install PyYAML, and the Python path and D:\WKP\Investing\watch-week are hardcoded in run.py, run_watcher.ps1 and README.
- N7 note. `[c.request_id]` in the closed-clock SKIP line can be `[None]`.
- N8 note. F16 open: started on a holiday or weekend the loop writes a "market closed" SKIP line and saves state every 30 s forever (no stop, no lock file). Start only on a trading day.
- N9 note. The final bar of each day (15:00 to 16:00 ET, 12:00 to 13:00 on a half day) is never scored as a closed bar because the loop stops when the clock closes; its signal is first seen at the next 9:31 scan. Not verified against live timing. Exits on that bar only see the partial bar.
- N10 note. Running `--demo` as instructed wrote demo-out\ inside the project folder (outside D:\WKP\scratch). It is the tool's own default; demo-out is untracked in git with the rest of the folder (not committed).

## What blocks creating GO-COUNTED.flag
Nothing in the safety bench blocks it: no key leak path, no order path, no non-paper URL, gate works. What I would hold the flag for, in order:
1. N4: the plan says the frozen config hash and the Zac-can-act ledger exist before Monday 9:30 ET and go-live is judged on that ledger. They do not exist. Either build them or the trading-director logs an explicit scope cut. Without them the week can prove the plumbing only, not go-live.
2. N1 and N2: a loop regression test and the crash-replay duplicate (cheap, Sat/Sun).
3. software-tester re-pass on the fixed code (the tester report predates the fixes; I re-ran tests but did not redo their 44 edge cases).
4. One read-only `--smoke` run by Zac or the trading-director (not run by me, per rules) to confirm real response shapes, bar counts after the Thanksgiving gap, and that APCA_API_BASE_URL has no trailing slash. NOT VERIFIED by me.
5. Flag is the trading-director's file to create, only after the above and Zac's status confirmation (TRADING-2026-11-26-02).

## Not verified
Any live behavior, Alpaca response shapes, IEX hourly bar timing, 20-day lookback yielding 60+ bars on Nov 30, rate limits, PyYAML licence, concurrency, Windows file locks. Env var values (not read by order).
