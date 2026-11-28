# WKT Crypto Watcher: Design

Department: FAWN FOREST INVESTMENTS (boss: trading-director). Written by software-architect for software-director, 2026-11-26.
Status: DESIGN ONLY. No code, no config file, no install, no key, no git, no spend was made for this document.
Paper only. Not financial advice. No promise of returns.

---

## 1. One-page summary

**What it is.** A program that watches a short list of crypto pairs 24 hours a day and records what a strict rule set would have done. It writes its own pretend trades to a ledger file. It judges them with a cost haircut at several levels. It never touches real money.

**What it is NOT.**
- No order endpoint. Ever. No account-write endpoint. No trading endpoint. No function that could send an order.
- Not a trading bot. Not connected to Robinhood in Phase A.
- Not a prediction of profit. The research file found no audited AI-bot track record (section 14).

**The plan in six lines.**
1. Prices come from Coinbase Exchange public candles and quotes. No key needed. Kraken is the cross-check. (Phase A.)
2. Only fully settled hourly bars are used. Anything doubtful becomes UNKNOWN, and UNKNOWN counts as FAIL (no trade).
3. Pretend trades fill at the ask plus a haircut and exit at the bid minus a haircut. The haircut is a placeholder until measured.
4. Two ledgers. Main ledger: fills 24/7. "Zac can act" ledger: fills only when Zac could really be at his phone. Go-live is judged on the second one, and only if it is positive at 30 bps each side.
5. Risk numbers are the locked ones: risk 0.5 / 1 / 2 percent by score, 25 percent max position, stop 2 x ATR on 1-hour bars, target 2.5R, daily kill -5 percent, weekly cap 6 percent, max 4 open, 3-day time stop.
6. Phase B (later, only if Zac says yes): read Robinhood's best bid and ask with a read-only key to measure the real spread markup. The key is read by variable name only.

**Biggest honest worry.** Costs. If Robinhood's real round trip is near 2 percent (unverified claim, a stress level here) and a 2 x ATR hourly stop is only about 1 percent away, costs may eat most of the edge. The design measures this on purpose (a cost-to-risk figure on every trade) so a "no edge after costs" answer is a valid, useful result.

**Code reuse.** The stock watcher (`D:\WKP\software\wkt-alpaca-watcher`) is about to run its counted week. This design copies its pure modules (with a parity test) instead of importing them, so the stock watcher is never edited. Details in section 9.

**Skills check (my reading of your reading, section 9).** Your reading holds. All five trader skills are stock day-trade tools. None runs on crypto. None may be used to produce an order file. Four ideas are reused as patterns.

**Decisions needed from Zac and trading-director:** 20 short items in section 13. The five that block the build are Q1, Q8, Q9, Q16 and Q17.

---

## 2. Hard rules (non-negotiable, each has a test in section 11)

### 2.1 No orders, no writes
- The future code contains no order, cancel, account-write or trading endpoint and no function that could send one.
- Every HTTP call in the whole program goes through ONE module (`http_gate`). No other module may import a network library. A test proves it.
- The gate allows only the GET method. Any other method name, anywhere in the source, fails the test.
- The gate holds an allowlist of host plus path. Anything not on it raises an error BEFORE any network call.

### 2.2 The allowlist (Phase A, written here as a proposal, finalized at build step 1)
| Host | Path | Use |
|---|---|---|
| api.exchange.coinbase.com | /products/{id}/candles | hourly and daily bars (read in the Coinbase docs 2026-11-26) |
| api.exchange.coinbase.com | /products/{id}/ticker | bid, ask, price, time |
| api.exchange.coinbase.com | /time | server clock for the skew check |
| api.exchange.coinbase.com | /products/{id} | trading status flag (halt, disabled). Field names NOT VERIFIED, confirm at build step 1 or drop this row |
| api.kraken.com | /0/public/OHLC | cross-check bars |
| api.kraken.com | /0/public/Ticker | cross-check quote |

Phase B adds exactly one row: Robinhood best_bid_ask. The full path is NOT VERIFIED (I saw the endpoint name in the researcher's file, not the full path). It is copied from the official docs at the Phase B step, by a reviewed change. Not before.

Forbidden on purpose, even though they are GETs: Robinhood accounts, holdings, orders. The watcher does not need them, so the gate does not allow them.

### 2.3 Keys
- Phase A needs no key at all.
- Phase B reads keys by environment variable NAME only. Proposed names: `ROBINHOOD_CRYPTO_API_KEY` and `ROBINHOOD_CRYPTO_PRIVATE_KEY`. (Names are proposals, Zac may rename.)
- A key value is never printed, never logged, never written to a file, never put in an error message (errors report the exception type only, same as the stock client).
- `config.yaml` may hold the variable NAMES, never a value. The config validator rejects a value that looks like a secret.
- Redaction runs on every log line before it is written (section 11, test K).
- Zac creates the key himself, with no trade permission if Robinhood lets him choose (the researcher's file says permissions are chosen at creation). Agents never see it.

### 2.4 No live path
- Startup asserts: mode is paper, the allowlist has no write path, no order-related name exists in the source tree. If any assert fails the program refuses to start.
- A real-money crypto test is Zac's call, in his own config, and needs a written decision in `logs\DECISIONS.md` first. This design contains no code path for it.

---

## 3. Data layer

### 3.1 Sources and why
| Source | Role | Why |
|---|---|---|
| Coinbase Exchange public candles and ticker | PRIMARY | Keyless, locked rules say Coinbase public candles, liquid USD books, tested spread 0.01 USD on BTC |
| Kraken public OHLC and Ticker | CROSS-CHECK | Keyless, second venue, catches a bad feed |
| Robinhood best_bid_ask | PHASE B ONLY | Real price Zac would pay. Needs key plus signature |
| Alpaca crypto data | REJECTED as primary | Worked keyless but docs show keys, unauthenticated behavior undocumented, thin Alpaca-only volume, 11.8 USD spread on 0.001 BTC in the data-sourcing test |
| CoinGecko | NOT USED | Limits conflict between sources, needs a key and attribution |

Terms of use: Coinbase terms NOT RETRIEVED (403), Kraken and Alpaca terms not read. This is a risk (section 13) and a pre-count check (Q11).

### 3.2 What the Coinbase docs say (read 2026-11-26, docs.cdp.coinbase.com candles page)
- Query parameters: granularity (60, 300, 900, 3600, 21600, 86400 seconds), start and end. Start is ignored unless end is also sent.
- Max 300 candles per request. No pagination, so use several start/end ranges.
- Rows are time, low, high, open, close, volume. The docs prose omits volume in one place and lists it in another, so the parser must check for six values and treat anything else as UNKNOWN.
- Some returned candles may precede the requested start, so trim.
- No candle exists for an interval with no trades. History may be incomplete.
- The docs do not say whether the current unfinished bucket is included. So never assume. Use the closed-bar rule below.
- Docs say do not poll candles frequently. So candles are fetched once per bar, not once per minute.

### 3.3 Polling cadence
- **Candles:** one fetch per pair per new settled hour, plus one daily-bar fetch per pair per day. 12 pairs is about 12 to 24 calls an hour. Far under 10 per second.
- **Quotes:** only for what needs one right now. Open positions, pending signals, the two gauges (BTC, ETH), and any pair at the moment of evaluation or fill.
  - Weekday window (Mon to Fri, 09:30 to 17:00 ET, from the locked rules): every 60 seconds.
  - All other times and weekends: every 900 seconds (15 minutes, from the locked rules).
  - Worst case 12 pairs plus gauges, one call each, paced at 150 ms apart: a burst of 2 to 3 seconds a minute. That is about 5 per second for 3 seconds, under the 10 per second limit (burst 15).
- **Self limit:** the gate runs a token bucket at 5 requests per second for Coinbase (half the published limit) and 1 per second for Kraken (limit NOT RETRIEVED, so conservative). On HTTP 429 or 5xx: back off, log, mark UNKNOWN for that scan. No retry storm.
- Phase B Robinhood: at most one call a minute, batched if the endpoint allows (NOT VERIFIED). The Robinhood agreement says access can be disabled for excessive market data usage (researcher's file), so keep it light.

### 3.4 Closed-bar rule and settle delay
- A bar is USED only if its end time is at least `bar_settle_minutes` in the past. Default 60 (one full interval), as ordered. Reason: candle revision behavior is NOT VERIFIED, and the candles response is cached up to 5 minutes (max-age 300 per the data-sourcing facts).
- The price of this safety: a signal is acted on about one hour after its bar closed. That is slower than the stock watcher. The gap rule (section 4.5) cancels the signal if price ran away.
- A faster setting (for example 6 minutes, just past the cache) is possible later, but only as a one-change test after Phase A measures revisions (Q2).
- **Bar hash:** every bar used by a decision is hashed (sha256 of pair, start time, o, h, l, c, v as text). The decision line carries the hash of the last bar and a hash over the whole window used.
- **Revision watch:** each scan re-fetches the recent overlap and compares to stored hashes. A changed closed bar writes a REVISION line (pair, bar time, old hash, new hash). One REVISION flags every decision that used that bar as TAINTED in the scorecard, and trading-director is told.

### 3.5 Gaps
- A missing hour in the middle of the history (no trades, or an outage) is a gap. Default: more than `max_gap_bars_in_window` (default 1) missing bars in the last 60 bars = UNKNOWN.
- One missing bar is tolerated for thin pairs only if the pair passed the volume filter, and the indicator code treats it as a missing value, never as a zero-volume bar with a carried-forward price. Simplest safe rule for the first config: any missing bar inside the last 60 hours = UNKNOWN. Config `max_gap_bars_in_window: 0`. Loosening it is a later one-change test.
- Short history (fewer than `min_bars`, default 60 hourly and 210 daily for the 200-day average) = UNKNOWN.

### 3.6 Clock skew
- Each scan calls /time. Skew = server time minus the midpoint of the local send and receive times. If the absolute skew is over `max_clock_skew_seconds` (default 5) the scan is UNKNOWN for new entries and the line says so.
- Quote age is computed with the skew-corrected local clock.

### 3.7 Quote health and the UNKNOWN rule
A quote is HEALTHY only if all of these hold:
- Age at most `quote_max_age_seconds` (default 10).
- Bid and ask are present, positive, and bid is below ask. Bid at or above ask = UNKNOWN (crossed book).
- Spread is under the hard sanity ceiling `spread_insane_bps` (default 500). Above it = UNKNOWN. A merely wide spread (above the filter in section 6.5) is a SKIP, not UNKNOWN.
- The quote timestamp moved since the last quote for that pair (a frozen quote with the same timestamp is stale even if its "age" looks fine because we re-fetched it).
- Its mid is within `source_disagree_bps` (default 50) of the Kraken mid. If not, UNKNOWN for that pair.

Everything below becomes UNKNOWN, counts as FAIL, is logged with the reason, and blocks any new trade on that pair:
- quote older than the allowed age
- bid at or above ask
- missing bar or gap in the window
- short history
- the two sources disagree beyond the threshold
- a source is down, rate limited, or returns bad data
- clock skew too large
- product flagged halted, disabled or in maintenance (if that field verifies at build step 1)

A pair with no Kraken mapping is excluded from the scan with the reason "no cross-check source" (Q6 lists the alternative). BTC and ETH must always be known, because they are the gauge.

### 3.8 Outage handling and circuit breaker
- **Per-source down:** logged on the first failed call, then once per scan, not once per call.
- **Circuit breaker:** if the primary source is UNKNOWN for `breaker_scans` consecutive scans (default 3), the breaker opens. While open: NO new paper entries and no new signals are queued. It closes after `breaker_clear_scans` clean scans (default 2). Opening and closing are logged lines.
- **Open positions during an outage:** they are still marked with the last good price, every log line for them carries `STALE_MARK` and the age of that mark. Stop and target checks cannot run on stale data, so they are flagged "unchecked". The kill switch and caps still run on the stale marks and say so.
- **On recovery:** the closed-bar backstop (section 4.6) checks every missed bar. If a stop was passed during the outage, the exit price is the worse of the stop price and the first fresh bid (gap rule), and the line is tagged `OUTAGE_GAP`.
- **Watcher offline** (the PC was off or asleep): the next start writes an OFFLINE line with the gap start and end. Counts do not include a period the watcher was down for a missed entry. Open positions go through the same recovery as above.
- **Exchange maintenance windows:** if the status field verifies, a non-online status is UNKNOWN. If it does not verify, maintenance shows up as failed calls and the circuit breaker covers it. NOT VERIFIED either way.

---

## 4. Simulated paper ledger (main ledger, 24/7 fills)

Our own file. It places nothing anywhere. Every price is a real quote read from the public feed.

### 4.1 Account
- `starting_equity` in config. Default 100000 (a placeholder, same as the stock watcher, judged in percent).
- A **$60 view** runs the same rules on the same signals with `starting_equity` 60. At $60 the 25 percent cap is $15. Crypto allows fractional quantity, but Robinhood's minimum order and quantity increments are NOT VERIFIED, so config holds placeholders (`min_order_usd` 1.00, `qty_decimals` 8). Signals that cannot fill at $60 (below minimum, or fee larger than a set share of the position) are logged as `NOT FILLABLE_AT_60`. They are results, not errors.
- Ledger instances are listed in config, so adding one is a config change. Phase A default: `main` (24/7 fills, 100000), `zac` (Zac-can-act, 100000), `zac_60` (Zac-can-act, 60).

### 4.2 Fills (entries)
- A signal needs a HEALTHY quote at the moment of fill. No fresh quote means no fill, and the signal waits up to `signal_max_age_minutes` (default 120) then CANCELs.
- Buy fills at the ask plus the haircut: `fill = ask * (1 + haircut_bps/10000)`.
- Fee line: `fee = notional * fee_bps_each_side/10000`, default 0 (market-maker routing shows no fee line per the researcher's reading of the Robinhood schedule; the spread is the cost). The 0.95 percent exchange-routed fee is run as a scenario, not the base (section 4.7).
- Difference from the stock watcher, on purpose: the stock watcher fills at the next bar open from bar data. Here a live ask exists, so the fill uses it. The next bar's open (from candles, read later) is logged next to it as `bar_open_ref` so QA can compare. The gap rule is the same idea: cancel if the fill-time mid is more than `max_gap_atr` (default 1.0) ATR from the signal bar close.

### 4.3 Exits
Checked on every quote poll and again on closed bars. All decisions use RAW prices (bid, bar high and low), then the haircut is applied to the fill. That keeps haircut replays exact.
- **Stop:** raw bid at or below the stop. Fill is the worse of the stop and the bid, minus the haircut. This is the gap rule.
- **Target:** raw bid at or above the target. Fill at the target minus the haircut (a resting limit sell fills at the target or better; taking the target is the conservative choice).
- **Time stop:** 3 days (`time_stop_days: 3`, locked rules, crypto). Exit at the first fresh bid after 72 hours from the entry fill. The 24/7 market has no "sessions", so it counts elapsed hours.
- **End rule:** at the scorecard's final day, open trades are closed at that day's final price (the last good bid at the close of the final ET day), tagged `END_RULE`, and reported separately so they are visible.
- **Kill switch and weekly cap** do not force-close positions (locked rule: open positions keep their own stops). They only block new entries.

### 4.4 Sell-side math
`sell_fill = raw_exit * (1 - haircut_bps/10000) - fee`. Net P and L = (sell_fill minus buy_fill) times quantity minus fees. R = net P and L over the risk at entry (quantity times (buy_fill minus stop)).

### 4.5 Gap rule
Entry: cancel if the fill-time mid is more than `max_gap_atr` ATR from the signal close. Exit: worse of the stop and the next fresh bid (4.3).

### 4.6 Closed-bar backstop
Between quote polls, a wick can touch the stop without any poll seeing it. Each time a new settled bar is read, the ledger checks the bars since entry:
- low at or below the stop, and no exit yet: exit at the stop price minus haircut, tagged `BAR_BACKSTOP`.
- high at or above the target plus the haircut distance, and no exit yet: exit at the target minus haircut, tagged `BAR_BACKSTOP`.
- both in one bar: the stop is assumed first (same as the stock watcher).

### 4.7 Haircut ladder and survivors
Every closed trade is re-priced at each level, same quantity and same exit path (exact, because exits use raw prices):

| Level (bps each side) | Label |
|---|---|
| 5 | optimistic, same as stocks |
| 15 | base for the main ledger (placeholder, ASSUMPTION) |
| 30 | pass line for go-live (placeholder, ASSUMPTION), base for the Zac ledger |
| 50 | STRESS, not measured |
| 100 | STRESS, not measured. About the 2 percent round trip third parties claim for Robinhood. UNVERIFIED claim |
| scenario F95 | fee only: 95 bps each side with a 5 bps haircut (Robinhood exchange-routed standard tier from the researcher's reading of the 20261102 fee schedule, snippet-level confidence on my side because I did not reopen the PDF). A scenario, not a fact |

The decisions log and trade log carry, per trade, one field per level: net P and L and a survive flag (net above zero). The scorecard prints, per level, trade count, net P and L, win rate, average R, and "survives: yes or no" for the whole set. The pass line is the 30 bps row on the Zac ledger.

Also logged per trade: `cost_r` = (round-trip cost at the 30 bps level) divided by the risk per unit. If `cost_r` is large, the scorecard says so first. See the filter in 6.5.

---

## 5. Regime detector for crypto

Gauge = BTC-USD, with ETH-USD as a second opinion. Same six tags as the stock plan: UPTREND_CALM, UPTREND_VOLATILE, RANGE, DOWNTREND_CALM, DOWNTREND_VOLATILE, UNKNOWN. UNKNOWN is FAIL.

### 5.1 Inputs
- Daily candles (granularity 86400): at least 210 days, so the 200-day average exists.
- Hourly candles: at least 20 days (480 bars, two or three calls).
- Breadth proxy: share of the watch list whose daily close is above its own 50-day average.

### 5.2 Rules (every number below is a config placeholder, frozen with the score)
- **Trend leg (per gauge coin), from daily:** UP if close above the 50-day and the 50-day above the 200-day and the 50-day slope over 10 days is positive. DOWN if the mirror. Otherwise RANGE.
- **Hourly agreement:** hourly EMA20 versus EMA50 and hourly close versus EMA50 must point the same way as the daily trend. If they disagree, the trend leg becomes RANGE.
- **Two gauges:** if BTC and ETH trend legs differ, RANGE. If either is UNKNOWN, the regime is UNKNOWN.
- **Volatility leg:** daily ATR percent (14 days) divided by its own 60-day median. Hourly ATR percent (14 bars) divided by the median of its last 20 days. VOLATILE if either ratio is above `vol_ratio_volatile` (default 1.25), otherwise CALM. Needs 14 plus 60 daily values.
- **Breadth override:** UP with breadth under `breadth_min_up` (default 40 percent) becomes RANGE. DOWN with breadth over `breadth_max_down` (default 60 percent) becomes RANGE.
- RANGE has no CALM or VOLATILE split (same as the six tags in the stock plan).

### 5.3 Crypto tags (not regimes)
- `WEEKEND`: Saturday or Sunday by the ET calendar (config: `weekend_days`).
- `LOW_LIQ_HOURS`: default 00:00 to 06:00 ET. This window is an ASSUMPTION. Only secondary sources say liquidity thins at weekends or overnight (data-sourcing: unverified). Phase A also records volume and spread by hour of day from our own data, so the window can be set from evidence later.
- Both tags are written on every decision and trade. They change behavior only through the weekend rule in 6.7.

### 5.4 How the tag affects behavior
Only through sizing, and in the first frozen config it changes nothing: `regime_size_multiplier` is 1.0 for all five known tags, and the step-up is OFF. UNKNOWN blocks the trade (FAIL). The point of the first count is to log the tag and learn. Changing a multiplier is a later one-change test after 50 counted trades.

---

## 6. Risk

Every threshold is in `config.yaml`. None is in code.

### 6.1 Per-trade caps (locked rules and the stock plan)
- Risk per trade: 0.5 percent at score 70 to 79, 1 percent at 80 to 89, 2 percent at 90 and up. Score under 70: no trade.
- Max position 25 percent of equity (BTC and ETH). Lower for thin alts (6.6).
- Stop: 2 x ATR(14) on 1-hour bars below the fill. Target 2.5R above.
- Max loss per trade: 3 percent of equity measured at the stop. A planned trade over it is refused, never shrunk by moving the stop.
- Size = the smallest of: risk size, position cap, cash, and open-risk headroom (6.6). Fractional quantity rounded down to the pair increment (increment NOT VERIFIED, config placeholder).
- Step-up (risk 2 up to a hard 3 percent) stays OFF until 20 counted trades with positive net expectancy on the Zac-can-act ledger, and then only under the stock plan's conditions: score 90 or more, regime UPTREND_CALM, no kill switch in the last 5 days, fewer than 2 open. The 25 percent cap still applies.

### 6.2 Per-day and per-week caps
- **Daily kill switch:** equity down 5 percent from the day-start equity (marks included) = no new trades until the next day boundary. Open positions keep their stops. A KILL line is logged. (The locked rules say "text Zac". Text alerts are not built, same as the stock watcher.)
- **Weekly cap:** equity down 6 percent from the week-start equity = no new trades until next Monday 00:00 ET.
- **Max 4 open positions** (open plus pending signals).

### 6.3 Day boundary for a 24/7 market (decision)
The day and week boundary is **ET midnight**. The week starts Monday 00:00 ET.
Why: the locked rules, the Monday watch-day rule, the stock watcher and Zac's own life are all on Eastern time. UTC midnight (the exchange habit) is 7 or 8 PM ET, inside Zac's evening acting window, so the kill switch would reset in the middle of his evening. ET midnight resets while he sleeps. Daylight saving makes two days a year 23 or 25 hours long. The code uses a real timezone database for that, never a fixed offset.

### 6.4 Monday watch-day rule
Carried over by default: on Monday (ET calendar day), only a score of 90 or higher may trade. It is stock-plan wording, locked for crypto too until Zac says otherwise (Q5).

### 6.5 Crypto filters (hard filters, cheap, run before scoring; failures are SKIP lines, logged, not counted)
- Minimum 24-hour dollar volume (sum of close times volume over the last 24 hourly bars): `min_24h_usd` placeholder 5,000,000.
- Maximum spread at evaluation: `max_spread_bps` placeholder 20 on weekdays. A wider spread is SKIP "wide spread".
- Cost-to-risk filter: skip if round-trip cost at the 30 bps level divided by the stop distance in percent is above `max_cost_to_risk` (placeholder 0.5). This is the "costs eat the stop" protection. It will remove many setups on purpose and every removal is a logged SKIP.
- Minimum stop distance: the stop must be farther than `min_stop_to_spread` (placeholder 4) times the current spread (pattern from trader-exit's "too tight to survive the spread").
- No stablecoins: config denylist (USDT, USDC, DAI, PYUSD and similar bases), plus a heuristic: price within 0.98 to 1.02 and a 7-day range under 0.5 percent is flagged stable-like and excluded, with a log line.
- Never chase: cancel if the gap at fill time is over `max_gap_atr` (4.5).
- Delisting or halt flag: product status not online = UNKNOWN (3.7), or SKIP if the status says "post only" or "cancel only" (field names NOT VERIFIED).

### 6.6 Correlation and thin-alt rules (cap risk, not only count)
BTC and alts move together, so four open positions can behave like one big position.
- `total_open_risk_cap_pct` (placeholder 4.0): the sum of risk-at-stop across open positions may not exceed it. A new entry that would pass it is refused.
- `max_correlated_alts` (placeholder 2): "correlated" = hourly return correlation to BTC at or above 0.7 over the last 30 days. Missing data = counted as correlated.
- Position cap by liquidity tier (placeholders): tier 1 (BTC, ETH) 25 percent, tier 2 (24-hour volume at least 50,000,000 USD) 15 percent, tier 3 (everything else that passed the volume filter) 10 percent.

### 6.7 Weekend and overnight rule (PROPOSAL, needs Zac, Q3)
Default proposed: weekends and LOW_LIQ_HOURS are allowed only at score 90 or higher, with an extra haircut `weekend_extra_bps` (placeholder 20) added to the fill and a stricter spread filter (`max_spread_bps_weekend`, placeholder 10). Reason: the locked rules already scan crypto on weekends every 15 minutes, but weekend liquidity claims are unverified, so the cost of being wrong is controlled by a high bar and a bigger haircut. Alternative: block entries on weekends entirely. Either way exits are never blocked.

### 6.8 PDT
Crypto has no pattern day trader counter in the stock sense, so the counter is dropped here. The researcher's file says no PDT rule applies to crypto but gives no rule citation, and what Robinhood enforces for crypto accounts is NOT VERIFIED. The check list in section 13 includes it.

---

## 7. Frozen config, hashes, counting

### 7.1 One file, hashed
- `config.yaml` holds every threshold. A copy of the key names is validated at startup (same style as the stock `validate`).
- On EVERY log line (decision, trade, scan, revision, outage) the watcher writes:
  - `config_sha256` (hash of the exact file bytes),
  - `code_sha256` (hash over the package source files, added because the stock plan freezes the config but not the code),
  - `commit` (git commit hash if available). The launcher script reads git and passes it in an environment variable. The Python code never shells out, so the no-subprocess test stays simple. The repo has many uncommitted changes today, so the file hashes are the authority and the commit is a note.
- Any change to the config changes the hash. The counts reset. A `CONFIG-CHANGES.md` lists each hash with its date, what changed and why. Same one-change-at-a-time policy as the stock plan.

### 7.2 What counts
- A decision COUNTS only when a symbol reaches score 70 or higher, once per setup. A "setup" is one pair plus one setup type plus one continuous run of bars where the condition holds. It ends when a closed bar no longer meets the condition, and a new run can count again.
- Every other scan line (below 70, filters, UNKNOWN, already holding) is logged with its reason and is NOT counted.
- Trades count from the first fill in the current config hash.
- 20 counted trades means "the plumbing works". An edge claim needs 50 or more. (Stock amendment 3.)

### 7.3 Counted gate
Same pattern as the stock watcher's `counted_gate`: counted scans need the explicit flag AND a release file (`GO-COUNTED.flag`) written by trading-director after the security pass and qa-director check. Without it the program runs only in test mode and tags every line `mode: test`.

### 7.4 A gap I found in the stock watcher (for trading-director)
I read the stock watcher's code and scorecard. The scorecard counts "fresh evaluations" (every symbol scored on a new bar), not "score 70 or higher, once per setup" as the devils-advocate amendment 2 says. The stock code also has no weekly cap, regime tag or config hash on log lines yet (the config key list has none). This may be intended for a later version, but it means the two scorecards would not compare until the stock side catches up. Flagged as Q14.

---

## 8. Two ledgers

### 8.1 Main ledger
Section 4: 24/7 fills at a fresh quote. Answers "does the rule set work at all, with costs".

### 8.2 "Zac can act" ledger
Answers "could Zac have done this by hand and made money". It is the go-live judge.

- **Acting windows** (config, ET, proposed): lunch 12:00 to 13:00 and evening 18:00 to 21:00. Zac works 8 to 5 and enters by hand in the Robinhood app. He confirms the real windows (Q8).
- **Entry:** the signal becomes a ticket at signal time. At the first quote poll inside the next acting window the ticket may fill, if still valid:
  - ticket age under `ticket_max_age_hours` (placeholder 20),
  - fill-time mid within `max_gap_atr` of the signal close,
  - stop not already passed,
  - quote HEALTHY and regime not UNKNOWN.
  Fill = ask plus the Zac-ledger haircut (default 30 bps, an ASSUMPTION, includes the Robinhood-style spread markup). Weekend extra applies if the window falls on a weekend.
- **Robinhood order behavior:** per the data-sourcing summary of Robinhood support pages, market orders are converted to limit orders collared 1 percent on buys and 5 percent on sells, and a market buy may fill at the ask and a sell at the bid. The ledger does NOT model the collar (no way to know when it bites). It records the note, and a ticket whose price moved more than 1 percent between ticket price and fill is flagged `COLLAR_RISK`.
- **Exits:** Robinhood stop order support for crypto is NOT VERIFIED. So the base design has NO resting stops:
  - At each acting window the ledger checks the whole period since the last window on closed bars and quotes.
  - If the low touched the stop at any time since entry: exit at the first fresh bid in the window minus haircut. That is usually worse than the stop. The loss will often be larger than 1R, and that is the honest picture.
  - If the target was touched: exit at the target minus haircut, only if Zac could have left a resting limit sell. Limit sells exist on Robinhood (the fee article says limit orders use exchange routing), but whether he can leave them for crypto here is NOT VERIFIED. So variant A (base, conservative) exits a touched target at the first window bid, not the target. Variant B (if Zac confirms a resting limit works) exits at the target.
  - Time stop (3 days): exit at the first window after 72 hours.
- Variants A and B are separate ledger instances. Go-live is judged on A.
- The planned risk per trade still uses the stop distance, but the log adds `realized_r_vs_planned`, and the scorecard counts trades that lost more than 1.5R.
- **Pass line:** the Zac ledger is positive in net P and L at the 30 bps level, with at least 20 counted trades (plumbing) and 50 for an edge claim. It also reports 5, 15, 50, 100 and the F95 scenario. Passing at 30 does not mean passing at the stress levels, and the scorecard says which levels survive.
- Real-money use is a separate written decision by Zac. A pass is information, not a recommendation.

---

## 9. Skill reuse and code reuse

### 9.1 The five trader skills (I read each SKILL.md and checked the code lines named)
| Skill | Verdict | Reason |
|---|---|---|
| trader-scanner | PATTERN ONLY | Builds its universe from Nasdaq Trader symbol files, reads Yahoo spark and chart data, scans daily closes and a 5-minute opening-range breakout on the 9:30 session open, writes `trader/watchlist.json`. No NYSE open exists in crypto. Reusable ideas: the closing-high breakout rule, the oversold bounce and reclaim rules (our scoring already has hourly versions), and the habit of reporting counts (fetched, usable, failed) so a partial scan is never called complete. Not reused as code. |
| trader-budget | PATTERN ONLY | Its docstring says it writes `trader/orders.json` "in the shape of Alpaca's place_stock_order", whole shares only (size.py lines 6 to 7 and 419). The crypto watcher must never produce an order file of any shape, so the tool itself is out. The reusable idea is size = smallest of four limits, and a refusal (not a smaller order) when the stop is too far. The stock watcher's `risk.size_shares` already implements that idea, and the crypto sizer reimplements it with fractions, tiered caps and open-risk headroom in place of max order. |
| trader-entry | PATTERN ONLY | Yahoo 1 and 5-minute bars, opening range after 9:30, no entries after 15:30. Reusable idea: the trigger is the first COMPLETED bar that CLOSES above the level (a wick or an equal close does not count), one trigger per setup, closed bars only, and say so if the trigger is old. The stock and crypto breakout setups already use close-above-high on closed bars. |
| trader-exit | PATTERN ONLY | Needs the opening range or a Yahoo session, rounds to the cent, forces flat by 15:55. Crypto has no session and no flat-by (replaced by the 3-day time stop). Reusable: ATR stop K times below entry, target as an R multiple, stop rounded away from the entry, refuse a stop too tight for the spread, stop and target set before entry. Price rounding uses the pair's own increment (NOT VERIFIED). |
| trader-risk | PATTERN ONLY | Its asset check blocks crypto (its own SKILL.md says it blocks "crypto or anything that is not a US stock or ETF ticker"), its window is NYSE hours, it reads `orders.json`. Reusable: gate returns PASS or BLOCK with ALL reasons, each check names the number and the limit, and exits are never blocked by day limits (the kill switch must never trap a position). |

**Your reading holds on all five.** None can run unchanged on crypto, none may be used to produce an order file, and the four ideas you named (min-of-four sizing, close-above-level on closed bars, ATR stop and R target, gate with reasons) are the reusable ones. The watcher never imports, calls or reads from these skills, and never reads or writes a `trader\` folder or an `orders.json`. A test checks this (test E).

### 9.2 Code reuse from the stock watcher: copy with a parity test, not a shared library (decision)
Reason: the stock watcher's counted week starts Monday 2026-11-30 with frozen config and code. Making it import a shared library, or refactoring it into one, edits the thing being counted and risks that run. A copy costs duplicate bug fixes, which I control as follows.
- The crypto folder holds copies of the pure modules plus `SYNC.md` listing each copied file, the stock file hash it was copied from, and every deliberate divergence.
- A parity test compares the copied files to the stock originals and fails if an UNLISTED difference appears. It also prints a "stock changed since copy" notice.
- After both watchers have 50 or more counted trades each, extract a shared `wkt_common` library in one reviewed step (new open item, not now).

| Stock module | Treatment in crypto |
|---|---|
| `indicators.py` (ema, rsi, atr, bollinger, macd, stochastic, adx, enrich; pure math) | COPIED unchanged |
| `config.py` (required-key validate) | COPIED, new REQUIRED list and secret-looking-value check |
| `logio.py` (decisions.jsonl, paper-trades.csv, atomic state) | COPIED, changed to stamp config hash, code hash and commit on every line, add redaction, new trade columns |
| `scorecard.py` | COPIED then generalized (venue-neutral wording, ledger name, haircut survivors, baseline). This is the one shared scorecard FORMAT (section 10) |
| `risk.py` | COPIED: `risk_pct_for`, `kill_switch_tripped`, `gate_reason`. REWRITTEN: `size_*` (fractions, tiers, open risk). NEW: weekly cap |
| `guards.py` | PATTERN: `counted_gate` copied. The Alpaca paper-URL assert is replaced by the allowlist and no-order asserts |
| `scoring.py` (hard filters, market mood, three setups) | COPIED setup logic with crypto config and new hard filters. Score weights are the stock placeholders, UNVERIFIED, tuned only by the one-rule policy |
| `alpaca.py` | NOT reused (Alpaca specific). The idea (GET only, whitelist, request id kept) is kept in `http_gate` |
| `engine.py` | PATTERN ONLY (loop shape, one line per symbol per scan). Crypto engine is new: quote health, two ledgers, breaker |
| `demo.py` | PATTERN (synthetic data, section 11) |

### 9.3 New crypto-only modules
`http_gate` (allowlist, GET only, rate limit, redaction hook), `coinbase_client`, `kraken_check`, `quote_health`, `bars` (closed-bar rule, gaps, hashes, revision watch), `ledger` (fill modes, haircut ladder), `regime`, `filters`, `clock`, `rh_quotes` (Phase B only, not built until its gate).

### 9.4 Folder layout (list only, for later build)
```
D:\WKP\software\wkt-crypto-watcher\
  DESIGN.md
  README.md
  SYNC.md
  CONFIG-CHANGES.md
  config.yaml
  run.py
  run_watcher.ps1
  wkt_crypto\
    __init__.py
    config.py
    clock.py
    http_gate.py
    redact.py
    coinbase_client.py
    kraken_check.py
    quote_health.py
    bars.py
    indicators.py
    scoring.py
    filters.py
    regime.py
    risk.py
    ledger.py
    engine.py
    logio.py
    scorecard.py
    guards.py
    demo.py
    rh_quotes.py          (Phase B, added only at its gate)
  tests\
    test_security.py
    test_data.py
    test_ledger.py
    test_regime.py
    test_replay.py
    test_parity.py
    fixtures\
D:\WKP\Investing\watch-week\crypto\   (proposed output folder: decisions.jsonl, paper-trades.csv, state.json, scorecard.md, daily-notes.md, revisions.jsonl, spread-measure.csv, GO-COUNTED.flag)
```

---

## 10. Shared learning loop

- **Every trade row carries:** ledger name, pair, setup, signal parts and score, regime tag, WEEKEND and LOW_LIQ flags, entry rule, exit rule used (stop, target, time, bar backstop, end rule, kill, outage), outcome in R and dollars, `cost_r`, net P and L and survive flag at each haircut level, bar hashes, `config_sha256`, `code_sha256`, commit, mode.
- **One scorecard format for stocks and crypto** (the generalized `scorecard.py`): same sections and column names, with a venue field. That lets results be compared side by side. The stock watcher adopts it at its own next counted-config change, not mid-week.
- **Weekly self-grade** in the scorecard: results versus buy-and-hold BTC over the same days (from the same Coinbase hourly candles, one buy and one sell haircut at the same level), and versus the Zac-can-act ledger. If paper looks too good, suspect the simulator first (same line as the stock scorecard).
- **strategies-tried ledger:** `D:\WKP\Investing\research\strategies-tried.md` gets a row BEFORE any rule idea is tried (owner trading-researcher, I read the file and it exists). The row names the idea, source, test, date and verdict.
- **One change at a time after 50 or more counted trades:** save `scorecard-baseline-<date>.md` first, change one rule or one number, run 50 more trades, compare, record the verdict. Each change resets the counts (frozen-config rule).
- **Memecoin guide test, later and fixed:** trading-researcher writes the guide's rules down as a fixed rule set in its own config and its own hash (the researcher's file says nothing retrievable stands behind the $52 to $4,392 claim, so the rules must be taken from the guide Zac has, and if they are not testable as written the test cannot run). Limits: only coins listed on our sources can be tested (new on-chain memecoins are not on Coinbase or Robinhood from what I know, availability NOT VERIFIED), and no verdict under 30 trades.

---

## 11. Test plan (to run later, no code now)

Letters match the build steps.

| Test | What it proves |
|---|---|
| A. Endpoint allowlist | Scans the source tree. Fails on any network import outside `http_gate`, any HTTP method name other than GET, any URL literal whose host or path is not on the allowlist, and any banned word (order, orders, cancel, place_order, holdings, accounts, POST, PUT, DELETE, PATCH) outside tests. Also a runtime check with a fake transport: every disallowed host, path and method raises BEFORE the transport is called. |
| B. No live path | Startup asserts fail the run if mode is not paper or any write path exists. |
| C. Kill switch | Equity down 5 percent from day start stops new entries, positions stay, a KILL line is written, day rolls at ET midnight (including a daylight saving day). |
| D. Weekly cap | Down 6 percent from week start blocks entries until Monday 00:00 ET. |
| E. No skill or order file | The source never imports or reads from the five trader skills, never touches a `trader\` folder or an `orders.json`. |
| F. 25 percent cap and tiers | Size never exceeds the tier cap, the open-risk cap or the correlated-alt cap. Max loss at the stop never exceeds 3 percent. |
| G. Stale quote is FAIL | Quote older than the limit, crossed book, frozen quote timestamp each produce UNKNOWN, a logged reason, and no trade. |
| H. UNKNOWN is FAIL | Missing bar, short history, source disagreement, source down, clock skew each block entry and are logged. |
| I. Gap fill | A stop passed by a gap exits at the worse of stop and next bid. An entry beyond the gap limit is cancelled. |
| J. Outage breaker | N UNKNOWN scans open the breaker, no new entries, open positions flagged STALE_MARK, clean scans close it, missed stop on recovery is OUTAGE_GAP. |
| K. Key redaction | Plants a fake key value and a fake private key in the environment, runs a full demo with errors forced, and proves neither value, nor any long base64-like token (except exact 64 or 40 character hex hashes), appears in any file the program wrote or any text it printed. |
| L. Clock skew | A fake server clock 10 seconds off makes new entries UNKNOWN. |
| M. Demo with synthetic candles | Includes a weekend gap, a flash crash with a quick recovery, and a frozen quote. Checks the expected UNKNOWN lines, the stop fill, the backstop and the weekend rule. |
| N. Deterministic replay | Same synthetic input plus same config gives byte-identical logs (timestamps from the injected clock). |
| O. Haircut ladder | A hand-built trade re-prices at 5, 15, 30, 50, 100 and F95 to the expected dollars. |
| P. Zac ledger | A signal at 14:00 ET does not fill until 18:00. A stop touched at 15:00 exits at the 18:00 bid, not the stop. Variants A and B differ as described. |
| Q. Counting | Score 69 never counts. Score 72 counts once, the same setup run does not count twice, a new run after a break counts again. |
| R. Parity | Copied modules match the stock originals except for the listed divergences. |
| S. Config freeze | Editing one number changes the hash, resets the counts and requires a CONFIG-CHANGES row. |

---

## 12. Build order (small steps, each with its proof, and who checks)

| Step | Work | Proof |
|---|---|---|
| 0 | Decisions Q1, Q8, Q9, Q16, Q17 answered (section 13) | Entries in `logs\DECISIONS.md` |
| 1 | trading-researcher and data-sourcing read-only probes: confirm candle ranges and the "current bucket" behavior, product status fields, Kraken pair names for the watch list, price and size increments, and read the Coinbase and Kraken terms by another route if the first is blocked | Saved raw samples in `tests\fixtures`, written note. NOT VERIFIED items updated |
| 2 | Skeleton: config loader, hashes, `http_gate`, redaction, clock | Tests A, B, K, L, S |
| 3 | Data layer on fixtures: bars, closed-bar rule, gaps, hashes, quote health, source disagreement | Tests G, H |
| 4 | Copy indicators and scoring, set up the parity check | Test R, plus the stock demo vectors reproduce |
| 5 | Regime and filters | Tests with fixtures for each tag and each filter |
| 6 | Main ledger: fills, exits, gap rule, backstop, caps, kill switch | Tests C, D, F, I, O |
| 7 | Zac ledger and the $60 view | Test P |
| 8 | Circuit breaker and outage recovery | Test J |
| 9 | Demo mode and deterministic replay | Tests M, N |
| 10 | Scorecard, survivors, baseline versus buy-and-hold BTC, counting | Tests Q, plus scorecard totals equal the sum of trade rows |
| GATE 1 | software-tester security pass (keys, order paths, allowlist), devils-advocate ruling on the plan and the haircut assumptions, qa-director check of the build | Written results in `logs\`. trading-director writes `GO-COUNTED.flag` only after all three |
| 11 | One uncounted live smoke scan (read-only public calls, writes to a test folder), watch the logs for UNKNOWN rates and revisions | Short note from trading-director |
| ZAC | Zac says when the counted run starts | His own message |
| 12 | Counted run, daily notes, weekly self-grade, hour-of-day volume and spread study | qa-claims traces the scorecard, qa-auditor grades it |
| GATE 2 (Phase B, separate) | Only if Zac says yes (Q10): add `rh_quotes` with the one Phase B allowlist row. Separate security pass, new test K cases with the real variable names, devils-advocate ruling | Spread measurement file only. It changes no fill until a reviewed config change swaps the haircut for a measured percentile, which resets the counts |

What Zac decides along the way: the open questions in section 13, the counted start date, whether to create a read-only Robinhood key, and anything touching real money (not covered here).

---

## 13. Cost, risks, unverified items, open questions

### 13.1 Cost to run
Expected $0.
Assumptions: Coinbase and Kraken public endpoints stay free and keyless (terms unread, Coinbase returned 403 to the data-sourcing fetch); Python standard library plus PyYAML (already used by the stock watcher; license of PyYAML NOT re-checked today); Zac's home machine; Phase B uses his existing Robinhood account and the API has no charge I could find (NOT VERIFIED); Phase B signing needs an Ed25519 library, license and size to be checked at that step. Disk is small (my estimate: 12 pairs, one line each per hour, a few hundred bytes per line, tens of MB a year; not measured). No paid scanner, no paid data. Time and QA token use are not money.

### 13.2 Risks (honest list)
1. Paper results may not translate to real Robinhood fills. Robinhood prices include a spread markup and Coinbase prices are a proxy.
2. Spread markup unknown until Phase B. Third parties say about 2 percent round trip on BTC (unverified). Costs may exceed the edge.
3. Thin liquidity on alts and at weekends (secondary sources only). A $15 position is small, but quotes can still be bad.
4. Terms of use unread (Coinbase 403, Kraken and Alpaca not read). Automated polling might be restricted.
5. Keyless Alpaca crypto data worked but is undocumented without keys, so it could change. It is not used.
6. Candle revision behavior NOT VERIFIED. Mitigated by the settle delay and hash watch.
7. One-venue dependence: Coinbase is the only primary. Kraken disagreement or Coinbase outage stops new entries.
8. The settle delay (one hour) makes signals slower than the stock plan. This may cost edge. Measured, not guessed, in Phase A.
9. The PC must be on 24/7 for a clean run. Sleep or reboot creates gaps (logged as OFFLINE, not hidden).
10. Hourly bars with a 2 x ATR stop may be too tight for crypto noise. The locked rules fix the numbers, so the test shows whether they work. It does not tune them.
11. Zac-ledger exits may be much worse than 1R without resting stops, because stop support is unverified. That is a feature of the honest ledger.
12. Overfitting and small samples: under 50 counted trades there is no edge claim (stock amendment 3).

### 13.3 What could not be verified (all marked NOT VERIFIED above)
- Coinbase terms of use (403), Kraken terms, Alpaca terms.
- Whether a closed candle can change after it closes (revision), and whether the current bucket appears in the candles response.
- Coinbase product status and trading-flag field names, price and size increments.
- Kraken pair names for the watch list.
- Robinhood: pair list, minimum order, quantity increments, stop order support for crypto, resting limit sells for crypto, collar behavior in practice, 24/7 API availability, rate limits, Georgia availability, best_bid_ask full path and batching, the real spread, the real fee tier that applies to market orders, and whether any PDT-style rule applies to crypto.
- Weekend and overnight liquidity, and the right low-liquidity window.
- The 2 percent round trip (third party claim).
- Licenses and sizes of any Phase B signing library.
- I did not call any live endpoint myself. The only thing I fetched today was the Coinbase candles documentation page. Everything about live behavior (tested spread, quote age, cache header) comes from the data-sourcing brief and is carried with its caveats.

### 13.4 Open questions for Zac and trading-director (copy into `logs\DECISIONS.md`)
1. Q1. Blocked: build step 2 (code layout). Recommendation: copy the pure stock modules with a parity test now, extract a shared library after both watchers have 50 counted trades.
2. Q2. Blocked: bar settle setting in the frozen config. Recommendation: 60 minutes (one full interval) for the first count; measure revisions in Phase A; test a faster setting later as a one-change.
3. Q3. Blocked: weekend rule. Recommendation: allow weekend and overnight entries only at score 90 or higher, plus 20 bps extra haircut and a 10 bps spread limit. Alternative: block them.
4. Q4. Blocked: day and week boundary. Recommendation: ET midnight, week starts Monday 00:00 ET.
5. Q5. Blocked: Monday watch-day for crypto. Recommendation: carry it over (Monday ET, score 90 or higher only).
6. Q6. Blocked: universe. Recommendation: a frozen list of about 12 liquid USD pairs (BTC, ETH and a few large alts, availability on Coinbase and Kraken confirmed at step 1), reviewed monthly, with any change counted as a config change. The locked rule "scan the whole list" conflicts with a frozen config. Pairs with no Kraken pair are excluded.
7. Q7. Blocked: correlation limits. Recommendation: total open risk cap 4 percent, max 2 correlated alts, tiered position caps 25 / 15 / 10 percent, all as placeholders in the config until the first review.
8. Q8. Blocked: Zac-ledger definition (Zac). Recommendation: acting windows 12:00 to 13:00 and 18:00 to 21:00 ET. Zac confirms the real times and whether lunch entries are possible at his job.
9. Q9. Blocked: stop and limit assumptions (Zac, 5 minutes, no order placed). Recommendation: open the Robinhood crypto order screen and report: can a stop or stop-limit be set on crypto, can a resting limit sell be left, what is the minimum order and the quantity increment, and what does the order preview show as fee or spread on a small BTC buy.
10. Q10. Blocked: Phase B (spread measurement). Recommendation: defer until Phase A has two clean weeks. If yes, Zac creates a read-only key himself, names `ROBINHOOD_CRYPTO_API_KEY` and `ROBINHOOD_CRYPTO_PRIVATE_KEY`, and no agent sees it.
11. Q11. Blocked: counted start (terms). Recommendation: trading-researcher reads Coinbase and Kraken terms by another route (not the one that returned 403) before the counted run, and the watcher keeps its call rate low.
12. Q12. Blocked: haircut labels. Recommendation: main 15 bps, Zac ledger 30 bps, ladder 5 / 15 / 30 / 50 / 100 plus F95, all placeholders, 50 and above labeled STRESS. Pass line is the Zac ledger at 30. Expect that the 100 bps row may fail everything, and treat that as information.
13. Q13. Blocked: simulated account size. Recommendation: 100000 for the percent-based main and Zac ledgers, plus the $60 view on the Zac ledger.
14. Q14. Blocked: comparing stock and crypto scorecards (trading-director). Recommendation: confirm whether the stock watcher implements "score 70 or higher, once per setup" counting and the config hash on every line before Monday 2026-11-30. My read of its code and scorecard shows it counts all fresh evaluations and has no hash field.
15. Q15. Blocked: memecoin guide test (later). Recommendation: trading-researcher first writes the guide's rules as a fixed rule set. If they are not testable as written, drop the test. Limit it to listed coins.
16. Q16. Blocked: hosting (Zac). Recommendation: say whether the PC runs 24/7. If not, accept logged OFFLINE gaps, count only fully watched stretches, and consider whether a different always-on machine is worth it later.
17. Q17. Blocked: venture status (Zac). The Investing venture is DORMANT (TRADING-2026-11-26-02). Recommendation: cover the crypto watcher with the same standing exception as the stock watch week, in his own words.
18. Q18. Blocked: real-money crypto test. Recommendation: NO, outside this design. It needs a written decision and his own config first.
19. Q19. Blocked: first frozen config behavior. Recommendation: step-up OFF, all regime size multipliers 1.0, regime logged only.
20. Q20. Blocked: PDT status for crypto. Recommendation: Zac checks Robinhood's own crypto trading rules page; until then no PDT counter is applied (none is needed for crypto from the research file, which cites no rule).

---

## 14. Limits statement

Paper only. Not financial advice. No promise of returns. The watcher only records what a rule set would have done, with assumed costs, on public prices. A paper pass does not mean a real pass.

The research check (`D:\WKP\Investing\research\ai-bot-claims-check-2026-11-26.md`, read in full) found no audited or broker-verified AI-bot track record turning a small account into thousands. It notes that the CFTC advisory treats such claims as a fraud signal, that Alpha Arena Season 1 (press only) had 4 of 6 models lose over about two weeks, and that independent papers show LLM trading edges shrinking with longer tests and with costs. The same file says regulators found "AI bots" that were not real. Nothing in this design assumes a profit, and a result of "no edge after costs" is an acceptable outcome.

---

## 15. Sources

Read in this session (2026-11-26):
- `D:\WKP\Investing\watch-week\WATCH-WEEK-PLAN.md` (rules, amendments 1 to 12, learning loop, regime, sizing, crypto group note).
- `D:\WKP\Investing\wkt-locked-rules.md` (locked 2026-10-19).
- `D:\WKP\software\wkt-alpaca-watcher\config.yaml` and the modules `config.py`, `guards.py`, `alpaca.py`, `risk.py`, `scoring.py`, `logio.py`, `scorecard.py`, `engine.py`, plus the function list of `indicators.py`, and `README.md`.
- Skills in `D:\WKP\.claude\skills\`: SKILL.md for trader-scanner, trader-budget, trader-entry, trader-exit, trader-risk, and selected lines of size.py, check.py, entry.py.
- `D:\WKP\Investing\research\ai-bot-claims-check-2026-11-26.md` (trading-researcher, 2026-11-26).
- `D:\WKP\Investing\research\crypto-api-and-data-sources-2026-11-26.md` (trading-researcher, 2026-11-26). Its Robinhood claims (fee schedule dated 20261102, 100 requests a minute, no sandbox, key creation) are the researcher's retrieval; I did not re-fetch them.
- `D:\WKP\Investing\research\strategies-tried.md` (exists, owner trading-researcher).
- Coinbase Exchange candles documentation, https://docs.cdp.coinbase.com/api-reference/exchange-api/rest-api/products/get-product-candles (fetched 2026-11-26): parameters, 300 candle limit, six-value rows, empty buckets, no pagination, current bucket not described.

Carried from the data-sourcing brief (retrieved 2026-11-26 by data-sourcing, with its caveats, NOT re-tested by me):
- Coinbase Exchange candles at granularity 3600 return [time, low, high, open, close, volume] newest first, 300 max, public rate limit 10 per second per IP (burst 15) per docs.cdp.coinbase.com/exchange/rest-api/rate-limits, candles response Cache-Control max-age 300, no candle for no-trade hours, ticker with bid, ask, price and microsecond time (tested spread 0.01 USD, quote 1 second old), /time gives server clock. Coinbase terms NOT RETRIEVED (403), verdict UNCLEAR.
- Alpaca crypto data worked keyless but undocumented without keys, thin Alpaca-only volume and 11.8 USD spread on 0.001 BTC versus 0.01 on Coinbase. Terms not read.
- Kraken public OHLC and Ticker worked keyless. Terms not read. CoinGecko limits conflict.
- Robinhood Crypto API market data needs an API key plus Ed25519 signature. Spec mirror (not official docs) shows spread-inclusive bid and ask fields. Support article: app shows mid, market buy may fill at ask and sell at bid, market orders become limit orders collared 1 percent buy and 5 percent sell. Fee tiers 0.00 to 0.95 percent by 30-day volume (snippet only). Third parties claim about 2 percent round trip (unverified). No paper or sandbox mode found.
- Weekend share of BTC volume about 13 to 17 percent and wider weekend spreads: secondary sources only, unverified.
