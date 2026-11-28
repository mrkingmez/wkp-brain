# Watch week plan (trading-director, written 2026-11-26)

Paper only. Nothing here is financial advice and no result is a promise. The agent never places an order, never prints or stores a key, never uses a live URL.

## Zac's decision of 2026-11-26 (recorded, TRADING-2026-11-26-01)
- Data and paper account: Alpaca Trading API, paper account (NOT the Broker API). This closes the Robinhood versus Alpaca open item. Stocks data comes from Alpaca market data instead of yfinance (locked rules said yfinance; Zac's newer word wins for stocks). Crypto data stays Coinbase public candles until a later phase.
- Real execution on Robinhood is unchanged for now and stays manual by Zac. Phase 3 and 4 are still not mine to start.
- Keys: user environment variables APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_API_BASE_URL (paper). Read by name only.

## Facts retrieved 2026-11-26 (read-only calls, keys never printed)
| Check | Result | X-Request-ID |
|---|---|---|
| GET paper /v2/account (Zac's check, from brief) | 200, ACTIVE, trading_blocked False | 4232117874c7b0c8fdeb21811263d703 |
| GET paper /v2/account (mine) | 200 | 91038f5ee30db8c885c8e550459db9fe |
| GET paper /v2/positions | 200, empty list | 6f81f4ae2fefb8e307f396929cf47e80 |
| GET paper /v2/clock | 200, market closed, next open 2026-11-27 09:30 ET, next close 2026-11-27 13:00 ET (half day) | 120fcf53352523939d2761b4f083afa6 |
| GET data /v2/stocks/bars/latest SPY feed=iex | 200, bar returned (last bar 2026-11-25 21:13Z) | b744a0a1105db563eb16cc4ae0135d02 |
| Same, feed=sip | 403 "subscription does not permit querying recent SIP data" | 9cde85340d3520f7f62f5b669010c989 |
| Same, no feed param | 200, same IEX bar | f0db6c11191b4b4fc93221101b145e17 |

Data feed for the free paper account: IEX (real-time but only IEX exchange volume, so thinner than the full tape; volume and some prices will differ from SIP). Recent SIP is denied. Not tested: websocket streaming limits, historical bar depth, options data, crypto data. Those are NOT VERIFIED.
Note: the Bash tool did not see the user env vars (set after the session started); the probe loaded them into the process from the User scope with PowerShell. The watcher must do the same on Windows (or be started from a fresh shell).

## Rules in force (wkt-locked-rules.md, unchanged)
Score under 70 no trade; risk 0.5 / 1 / 2 percent at 70-79 / 80-89 / 90+; max position 25 percent; stop 2 x ATR on 1-hour bars; target 2.5R; time stop 5 days for stocks; daily kill switch -5 percent; Monday trades only at score 90+; max 4 open positions. UNKNOWN data counts as FAIL.

## Scoring method
1. Every scan writes one line to decisions.jsonl per symbol per scan: time, symbol, data feed, score parts, score, action (TRADE, SKIP, WATCH), reason, Alpaca X-Request-ID of the data call. Skips are logged.
2. A paper trade is opened ONLY in paper-trades.csv (our own file), filled at the next bar open after the signal, with a haircut: configurable slippage (starting assumption 5 bps each side, a placeholder, not a measured figure) and fee line (Robinhood stock commission is $0; regulatory fees on sells modeled as a config value). The assumption is labeled and QA checks it.
3. Exits: stop, target, time stop, kill switch. All logged with reason.
4. scorecard.md: counts (decisions, trades), win rate, average R, gross and net-of-haircut P and L, max drawdown, how many skips and why. Every number traced to a log line. If paper looks too good, the simulator is suspected first.
5. No rule is changed until 50 to 100 trades; then one rule at a time.

## Day by day
| Day | Steps |
|---|---|
| Thu 11/26 (today) | Plan written, decision recorded, probes done, build ordered through software-director. |
| Fri 11/27 (half day, closes 1 PM ET) | Build, offline `--demo` run, unit tests (kill switch, 25 percent cap, stop logic, UNKNOWN is FAIL). No scoring week yet. Optional dry scan outside trading hours writes only a test log, not counted. |
| Sat 11/28 to Sun 11/29 | software-tester security pass (no keys in files, no order endpoints in code, paper URL assert). devils-advocate ruling on the plan. qa-director check of the build. Fixes. |
| Mon 11/30 | Day 1 of the counted watch week. Monday is a watch day: only score 90+ may trade. Scans every minute 9:30 to 4:00 ET (the locked 5 PM window is outside the regular session; extended hours data not verified). Daily note written after the close. |
| Tue 12/1 to Fri 12/4 | Days 2 to 5. Daily note, kill switch check, positions marked with latest bars. |
| Fri 12/4 evening | First scorecard. Expectation: far fewer than 20 trades in one week is likely with these filters, so the watch week extends day by day until at least 50 decisions and 20 paper trades, or Zac ends it. A no-trade week is allowed and is reported honestly. |
| After | qa-claims traces the scorecard, qa-auditor grades it, devils-advocate rules, checklist status reported. |

## Go-live checklist status (2026-11-26)
1. Watch week with a real log, 50 decisions and 20 trades, scorecard: FAIL (not started, 0 of 50, 0 of 20).
2. QA PASS on scorecard: FAIL (no scorecard).
3. Haircut applied and still positive: FAIL (nothing to test).
4. Watcher software-tester security pass: FAIL (watcher not built or tested; the zip is unverified code and is built around Robinhood and Twilio and yfinance).
5. Kill switch and 25 percent cap proven in demo mode: FAIL (not built).
6. Devils-advocate ruling on file: FAIL (ordered, not yet ruled).
7. Zac's own words on account size and what he can afford to lose: FAIL (not written; also the real Robinhood account is about $60 per Investing\CLAUDE.md, NOT RETRIEVED today).

## Open items queued for Zac (logs\DECISIONS.md)
- TRADING-2026-11-26-01: Alpaca Trading API paper chosen (recorded).
- TRADING-2026-11-26-02: Investing status DORMANT. Running the watch week is outside DORMANT; Zac to confirm a status change or accept it as a standing exception.
- TRADING-2026-11-26-03: Optional later, never needed for the watch week: allow paper orders to Alpaca's paper account in addition to the local log. Default is NO.

## Amendments after devils-advocate ruling (GO WITH CHANGES, 2026-11-26, `devils-advocate-ruling-2026-11-26.md`)
Adopted into the build order and counting rules:
1. The score, symbol list and filters are written into ONE frozen file (config.yaml) before Monday 9:30 ET. Its commit hash or file hash goes on every log line. Any change resets the counts and is listed with its date.
2. A "decision" counts only when a symbol reaches score 70 or higher, once per setup. Per-minute skip lines are still logged but are not counted.
3. 20 trades means "the plumbing works". An edge claim needs 50 or more. Expect weeks, not one week (max 4 open, 5-day holds).
4. Fixed end rule set in advance; open trades closed at the final day's closing price for the scorecard.
5. Simulator account size stated in config; a $60 sizing view reported alongside (25 percent cap is $15, fractional shares needed).
6. Second ledger "Zac can act": fills only at the next market open (Zac works 8 to 5 and enters by hand). Go-live judged on that ledger.
7. Gap rule: stop fills at the worse of stop price and next bar open.
8. Pattern day trader counter added.
9. Missing bar or short history = UNKNOWN = FAIL, logged.
10. Haircut reported at 5, 15 and 30 bps (15 and 30 are stress levels, not measured). Pass only if the Zac-can-act ledger is positive at 30.
11. NOT VERIFIED and needing checks before live: Robinhood fractional stop orders, the current day trading rule, hourly history depth on the free feed. Text alerts for approval and kill switch are not built.
12. Robinhood versus Alpaca for LIVE stock execution is still not decided by Zac (his 11-26 word covers the paper watch week). Queued as TRADING-2026-11-26-04.

## Learning loop, regime detector and sizing rule (added 2026-11-26 on Zac's order)
Not a promise of returns. Paper only. Account about $50 to $60, PDT limit 3 day trades per month (rule status being re-checked by trading-researcher, brief `research\ai-bot-claims-check-2026-11-26.md`).

### 1. Learning loop
- Every paper trade row in paper-trades.csv carries: signal parts and score, regime tag at entry, entry rule, exit rule used (stop, target, time, kill switch), outcome in R and dollars, config hash.
- Weekly self-grade in scorecard.md against a buy-and-hold baseline (SPY over the same days, from the same IEX bars) and against the "Zac can act" ledger.
- trading-researcher keeps `Investing\research\strategies-tried.md` so losing ideas are not repeated; every rule idea gets a row before it is tried.
- One change per run: a change is made only after 50 or more counted trades, one rule at a time, compared to the saved baseline scorecard (baseline copy saved as scorecard-baseline-<date>.md), then 50 more trades. Changes reset the counts per the frozen-config rule.

### 2. Regime and trend detector (free Alpaca IEX bars only)
Daily and hourly SPY (and the scanned symbol where useful): trend = price vs 50-day and 200-day averages and slope; volatility = ATR percent vs its 60-day median; breadth proxy = share of the watch list above its 50-day. Tags: UPTREND_CALM, UPTREND_VOLATILE, RANGE, DOWNTREND_CALM, DOWNTREND_VOLATILE, UNKNOWN. UNKNOWN (short history, missing bars) counts as FAIL, so no size step-up. Thresholds go in config.yaml, frozen with the score. The tag is logged on every decision and trade, so results can be split by regime. A regime tag only changes behavior through the sizing rule below, nothing else.

### 3. Sizing rule: "strike hard" defined
- Base: locked rules (0.5 / 1 / 2 percent risk by score, max position 25 percent).
- Step-up is a pre-set, capped step, never all-in: allowed only when ALL are true: score 90 or higher, regime UPTREND_CALM (or the pre-set tag in config), at least 20 counted trades in the current frozen config with net-of-haircut expectancy positive on the Zac-can-act ledger, no kill switch in the last 5 trading days, fewer than 2 open positions. Then risk steps from 2 percent to a hard cap of 3 percent of account, and the 25 percent position cap still applies.
- Hard limits regardless: max loss per trade 3 percent of account; max loss per week 6 percent, after which no new trades until next Monday; daily kill switch -5 percent unchanged; max 4 open positions; PDT counter blocks any trade that would be a 4th day trade in a rolling 5 days if the account is under $25k (rule text to be confirmed).
- At $50 to $60 the 25 percent cap is $12 to $15 a position, so sizing steps are often capped by the position cap and fractional shares; the sizing view at $60 is reported next to the paper-account view.
- The step-up stays OFF during the first counted watch week and until the 20-trade condition is met; it is tested in demo mode and on paper only.

### Evidence check result (trading-researcher, 2026-11-26, `research\ai-bot-claims-check-2026-11-26.md`)
- No audited or broker-verified AI-bot track record turning a small account into thousands was found. The $52 to $4,392 memecoin guide has nothing retrievable behind it. CFTC calls such claims a fraud signal. Alpha Arena Season 1 (press only): 4 of 6 models lost over about two weeks. Independent papers (FINSABER, Alpha Illusion) show LLM trading edges shrinking over longer tests and costs.
- PDT: FINRA Notice 26-10 replaces the $25k day-trading rule with intraday margin standards, effective 2026-06-04, firm phase-in up to 2027-10-20. The "3 day trades a month" assumption is possibly stale. What Robinhood enforces today is NOT VERIFIED. The plan's PDT counter stays as a conservative guard (3 per month) until Zac checks Robinhood.
- Robinhood stop orders: official article says whole shares only; fractional stops not confirmed. At $50 to $60 this may break the 2x ATR stop. Zac can look at the order screen in the app without placing an order.
- Suggested paper test (crypto memecoin guide rules as a fixed rule set vs buy-and-hold) is a phase 2/3 item, not part of the stock watch week; no verdict under 30 trades.

## Department name and crypto group (2026-11-26, Zac's order via coordinator)
- Department name: FAWN FOREST INVESTMENTS. trading-director stays the boss. Board row updated.
- Separate CRYPTO group: Robinhood Crypto API for crypto, Alpaca for stocks (Zac's intent). Per the locked rules crypto live is Phase 3, which I never start. Work now: research (`research\crypto-api-and-data-sources-2026-11-26.md`) and a design only (`software\wkt-crypto-watcher\DESIGN.md`), own simulated ledger, no paper mode assumed. Devils-advocate rules before any phase gate.

## Crypto design ruling (devils-advocate, GO WITH CHANGES, 2026-11-26)
Paper-only build may continue after these changes (full list in `devils-advocate-ruling-crypto-2026-11-26.md`): pass line at Robinhood standard fee 0.95 percent (F95), not 30 bps; Zac previews a small BTC buy three times with NO order placed to measure the real spread (Q9); first universe BTC, ETH and at most 4 more; step-up needs 50 counted trades; no Twilio or auto-execute code; no counted crypto run before the stock week's first scorecard passes qa-claims. At $60 a round trip at F95 costs about $0.29, more than the amount at risk (devils-advocate arithmetic). Note: Investing\CLAUDE.md is out of date (says Robinhood has no programmatic orders and PDT applies). Stock build: 49 tests pass, security pass and QA PASS WITH NOTES; amendments build running.
