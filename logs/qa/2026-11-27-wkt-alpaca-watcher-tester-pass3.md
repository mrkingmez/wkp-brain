# wkt-alpaca-watcher tester pass 3 (2026-11-27)
Verdict: PASS WITH NOTES. Paper only. No product file edited, no key value printed, no GO-COUNTED.flag, no push.

Smoke: run 12:30:17 ET (before the 12:50 cutoff), finished 12:30:23. PASS against smoke-2026-11-27-checklist.md: account 200, positions 200, status ACTIVE, trading_blocked false, USD, equity 100000, positions_count 0, extended_hours_bars_dropped 417, bar hours 09 to 15 only, no symbol under 60 bars now or at projected next open, regime RANGE dated 2026-11-27, last gauge bar 17:00Z (12:00 ET, forming), no error words.
Tests: Ran 101, OK, 1523 s (under load). Scratch adversarial script: D:\WKP\scratch\tester-pass3\adv2.py.

Findings
- F1 (note, medium) PDT guard uses the scan time's date, not the fill bar's date. engine.py:282-285. If a scan resumes the next morning (restart or outage over the 10:00 hour) and fills past bars, four same-day entries all fill (reproduced: 4 of 4 filled with now = next day 09:05; live same-day case correctly stops at 3). Exits on those bars then make 4 day trades against limit 3. Needs a restart or outage across the fill hour, so rare. Fix idea: use nxt["t"] date.
- F2 (note, medium) Zac-ledger pending signals never expire and the Zac ledger has no gap cancel (config.yaml zac_ledger max_gap_atr null). A signal with no usable bar for days fills at a stale price (reproduced: signal Jan 5, fills Jan 19 at +50 percent). engine.py:273 (ok has no date upper bound). Also if the day after a signal only a 09:00 bar ever arrives (data gap), the fill slips to the following session's 10:00. Real days always have a 10:00 bar for liquid names, so low odds.
- F3 (note, low) Bad entry_bar_t on an open position (missing, empty, garbage, non-string) crashes _try_fill (KeyError, ValueError, AttributeError). engine.py:284. Old state files from before change 4 are fine (entry_bar_t was already required by _check_exit, which would crash the same way). Exits are never blocked by the guard (it runs only in _try_fill).
- F4 (note, low) Holidays not modeled in bdays_between (stats.py). Around Dec 24/25 the 5 day window drops old day trades one day early. In this 4 week window the month limit of 3 catches it first (checked: trades Dec 21 to 23 then Mon Dec 28 still blocked by the month rule). Already stated in the scorecard.
- F5 (note, info) Month limit of 3 effectively caps the Zac ledger at 3 day trades per calendar month, tighter than the rolling rule. Intended per config, worth knowing when reading results.

Ways the Zac ledger can still exceed 3 in 5 days or 3 a month: only F1 (past-bar fills after restart). Normal live running: four same-day entries stop at 3 (reproduced), entry yesterday not counted (None returned), 2 closed plus 1 open blocks, enforce false never blocks, month limit blocks.

Checks passed
- Keys: grep for key patterns found only header NAMES (alpaca.py), SHA256 list, one test line. No values. No env values read.
- Orders: whitelist is account, positions, clock on paper host, stocks/bars and bars/latest on data host (feed=iex forced); transport method fixed GET; no POST/DELETE/PUT/order text in product code; redirects refused. alpaca.py:12-16, 31, 60-64.
- Paper URL assert exact match, guards.py:16-19; tests pass.
- Kill switch and weekly limit trip and cancel pending in both ledgers before fills (engine.py:168-184); suite tests pass.
- Stops: gap down through stop fills at min(stop, open) (reproduced: stop 95, open 90, exit at 90). Stops and targets live on the 09:00 bar of a time stop day; time stop fills at the 10:00 open (engine.py:346-350). Stop is checked before target on the same bar (conservative).
- Fills: main and zac never use a 09:00 bar open; same-day signal after 10:00 fills next bar; pending deleted at fill so no double fill; empty and all-None bars scan clean.
- Formats unchanged: decisions.jsonl key set, state.json and zac key sets identical to the earlier baseline copy in scratch\wkt-base2; paper-trades.csv header identical (27 columns); logio columns identical; scorecard headings identical. Only change is the removed S4 overshoot sentence in the PDT bullet, as CHANGES says.

NOT verified
- Real naive-timestamp and DST day data from Alpaca (parse_bars turns naive into an invalid row; ET conversion uses zoneinfo, only reasoned and lightly tested). Half day 12-24 only reasoned, not run with a real clock. Live clock behavior after 13:00 today (smoke ran at 12:30). Config hash value not recomputed. The folder is not in git, so no diff against the previous code; format comparison used the scratch baseline copy. Restart-from-saved-state for PDT only checked by unit calls, not a full process restart.
