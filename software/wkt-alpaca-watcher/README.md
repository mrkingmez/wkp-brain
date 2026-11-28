# WKT Alpaca paper watcher

Paper only. It watches a short list of stocks and ETFs, scores setups on 1-hour bars with the locked WKT rules, and records what a disciplined trader would have done. It never places an order, anywhere. Nothing here is financial advice and no result is a promise.

## What it does
- Every scan reads the market clock and IEX hourly bars (and, once a day, daily bars for the regime tag). `--smoke` also reads account and positions. Read-only calls only. Counted mode does not call account or positions.
- Every scan writes one line per symbol to `decisions.jsonl` (skips included, with the reason, the Alpaca X-Request-ID of the calls, the config hash and the regime tag).
- A passing signal becomes a simulated trade in `paper-trades.csv` on TWO ledgers:
  - **main**: fills at the next 1-hour bar open after the signal bar closes (the plumbing test).
  - **Zac can act**: fills only at the open of the next trading session, because Zac works 8 to 5 and enters by hand. Go-live is judged on this ledger. A waiting Zac-ledger signal expires if more than `zac_ledger.max_pending_sessions` (2) weekdays pass after its signal date (change 6): it is cancelled, never filled at a stale price.
  Both carry a haircut (placeholder 5 bps each side, labeled as an assumption in `config.yaml` and in the scorecard).
- `scorecard.md` counts decisions and trades per ledger, win rate, average R, gross and net P and L, drawdown, a 5 / 15 / 30 bps haircut view, a $60 small-account view, the split by regime, day trades, the buy-and-hold SPY baseline, and lists every closed trade with the decision lines it came from.
- `daily-notes.md` gets one note per session day. `config-history.jsonl` lists every config hash the folder has seen.

## Counting rules (devils-advocate ruling, 2026-11-26)
- Frozen config: the hash of the parsed `config.yaml` is on every decision line and trade row. Change any value and the hash changes: the scorecard counts only lines and trades under the current hash, and the change is listed with its date. Comment edits do not change the hash.
- A decision counts only when a setup reaches score 70 or more, once per setup (the same setup on consecutive bars is one decision). Per-minute and per-bar skips are still logged and never counted.
- Fixed end rule: `end_rule.last_day` (set in advance, currently 2026-12-24: four trading weeks from Monday 2026-11-30; Friday 12-25 is an NYSE holiday and Thursday 12-24 closes at 1:00 PM ET, so 12-24 is the last regular day. The end rule fires once the clock reports closed on or after that day, so an early close works). After that day's close the program cancels waiting signals, closes every open paper position at the last mark of the final scan (within about a minute of the close, not the official closing print), writes the notes and scorecard, and refuses to scan again. Changing the day changes the hash.
- 20 closed trades means the plumbing works. An edge claim needs 50 or more.

## Rules (rule and score thresholds are in `config.yaml`; indicator periods such as EMA 20/50, Bollinger 20, MACD 12/26/9, ADX 14 are fixed in code; rules come from `D:\WKP\Investing\wkt-locked-rules.md`)
Score under 70 no trade. Risk 0.5 / 1 / 2 percent at 70 / 80 / 90. Max position 25 percent. Stop 2 x ATR on 1-hour bars. Target 2.5R. Time stop 5 sessions. Daily kill switch at -5 percent (no new trades, open positions keep their own stops). Monday only at score 90 or higher. Max 4 open positions. Missing or UNKNOWN data counts as FAIL. Do not change a rule during the watch week.
Added limits: max loss per trade 3 percent of the book, weekly loss limit 6 percent from Monday's start (blocks new trades until next Monday), pattern day trader guard (3 day trades in 5 trading days and 3 per calendar month, the rule text is NOT confirmed), gap through a stop fills at the worse of the stop and the next open.

## Regime tag and step-up sizing
- Daily SPY plus the watch list: UPTREND_CALM, UPTREND_VOLATILE, RANGE, DOWNTREND_CALM, DOWNTREND_VOLATILE or UNKNOWN (short history, bad bars, too few symbols). The tag only matters to the sizing step-up. Thresholds are placeholders in `config.yaml`.
- Step-up (risk 2 to a hard 3 percent) is OFF (`sizing.step_up.enabled: false`). Even when turned on it needs score 90+, UPTREND_CALM, 20 counted Zac-ledger trades with positive net at 30 bps, no kill switch in 5 trading days and fewer than 2 open positions. Turning it on changes the hash.

## Safety design
- Keys are read only from `APCA_API_KEY_ID`, `APCA_API_SECRET_KEY`, `APCA_API_BASE_URL`, by name. Nothing writes, prints or logs a value.
- The base URL must be exactly `https://paper-api.alpaca.markets` (no trailing slash) or the program refuses to start. There is no live path.
- The client is GET-only with a whitelist of five paths and a forced `feed=iex`, never follows redirects. A test greps the source and fails if any order endpoint or write verb appears.
- Counted scans are locked until you (or the trading-director) create the file `D:\WKP\Investing\watch-week\GO-COUNTED.flag`, which should happen only after the security pass and the qa-director check.
- Crash safe: each scan's log lines go into `state.json` first, then to the log files, so a restart never duplicates or loses a line.

## Run it (every step)
0. One time: `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe -m pip install -r requirements.txt` (PyYAML, free, may already be installed).
1. Open PowerShell.
2. Offline demo, no keys, no network: `cd D:\WKP\software\wkt-alpaca-watcher` then `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe -I run.py --demo`. Results go to `demo-out\` (fictional data, not a result).
3. Tests (5 to 25 minutes: about 5 when the machine is idle, up to 25 under load or with other test runs going; 112 tests): `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe -I tests\test_watcher.py`.
4. One read-only smoke scan (not counted, writes to `D:\WKP\Investing\watch-week\test\`): `powershell -File D:\WKP\software\wkt-alpaca-watcher\run_watcher.ps1 --smoke`. It prints the real response shapes and how many hourly bars each symbol has against the 60-bar minimum.
5. Counted watch week (only after the flag file exists): `powershell -File D:\WKP\software\wkt-alpaca-watcher\run_watcher.ps1 --counted --loop` at 9:25 AM ET on a trading day. It scans every 60 seconds while `/v2/clock` says the market is open, writes the daily note and scorecard after the close, then stops. Start it again the next trading day. Start it only on trading days (on a holiday it keeps writing "market closed" lines).
6. Rebuild the scorecard any time: `... run.py --scorecard --counted`.

## Known limits
- IEX feed only (thin volume, SIP is denied on the free account). Volume and some prices differ from the full tape.
- Exits are tested on hourly high and low only. If stop and target both sit in one bar, the stop is assumed to hit first. Real intrabar order is unknown.
- Hourly bars from Alpaca start on the hour. The 09:00 bar holds 09:00 to 10:00, so it includes about 30 minutes of pre-open IEX trades. Changed 2026-11-27 (Jarvis decision 2026-11-26, reversible, config `fills.session_open_fill_hour_et: 10`): the Zac-can-act entry fill and the time-stop exit fill now use the OPEN OF THE 10:00 BAR, not the 09:00 bar. Scoring is unchanged: `session_bars.first_bar_start_hour_et` is still 9, so the 09:00 bar is still scored. Stops and targets stay live on the 09:00 bar of a time-stop day. Changed 2026-11-27 (change 5, trading-director decision, same reason): the MAIN (plumbing) ledger entry also fills at the first bar open at or after 10:00 ET, never a 09:00 bar. Bars starting 08:00 and 16:00 exist on the feed and are dropped by `session_bars`. The last bar of the day is not scored as a closed bar until the next morning's first scan.
- Session window is 9:30 to 16:00 ET from `/v2/clock` (the locked 5 PM window is outside the regular session).
- Slippage, fees, the book size and the regime thresholds are placeholders, not measured. The haircut views at 15 and 30 bps are stress levels.
- The scoring logic is a port of the old WKT idea and is unverified as an edge. Expect few trades in one week.
- Long only. Stocks and ETFs only (crypto is a later phase).
- Not verified: IEX hourly bar latency right after the hour, websocket limits, early-close behavior beyond what `/v2/clock` reports, Robinhood fractional stop orders, the current day trading rule, daily-bar depth on the free feed (the smoke run reports it).
- PDT overshoot (S4) FIXED 2026-11-27 (change 4): the guard now counts entries opened the same ET day as potential day trades, so the ledger cannot exceed the limit (3 in 5 trading days, 3 per month). Cost: it can refuse an entry that would never have been day-traded. Rule text still NOT confirmed.
- Changes 6 to 8 (2026-11-27, tester pass 3 F2, F3, F1): Zac-ledger pending signals expire (the MAIN ledger has no date expiry, only the 1 ATR gap cancel); a missing or unreadable `entry_bar_t` on an open position is logged HOLD_UNKNOWN and counted as opened today by the PDT guard instead of crashing the fill (the exit check still needs a readable `entry_bar_t`); the PDT guard dates a fill by its fill bar, not the scan time. Demo hashes differ from the real run hash by design (the demo swaps in fake symbols, gauge and breadth setting).
- Holidays are not modeled in the PDT window or the sixth-trading-day count (a missing session day can shift the time stop by one day).

## Cost
$0. Alpaca paper account and IEX data are free. No paid service is used.
