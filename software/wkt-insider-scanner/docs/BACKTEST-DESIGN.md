# Backtest mode: design stub (documented plan only, NOT BUILT, NOT RUN)

Written 2026-11-27 by software-director for the trading-director order that applied the devils-advocate ruling (`D:\WKP\Investing\watch-week\devils-advocate-ruling-insider-2026-11-26.md`, required change 2). `python -I run.py --backtest` refuses and points here. Nothing in this file has been run. No SEC call was made to write it.

## Why it exists
The ruling says a forward sample this year can only KILL the signal. The real evidence test is a point-in-time backfill with the same frozen rules, written before anyone looks at results. Forward paper then becomes the out-of-sample check: does live behavior land inside the backfill's range. A pass needs both. Kill criterion K5 says: if the backfill is run and the primary metric is zero or negative net of costs, no forward run starts.

## Rules frozen BEFORE the data is touched
1. Use the config hash printed on the current scorecard. Any change to a rule after the first backfill run voids the backfill (it is then a tuning run, K7 territory). One value may change per run, with a written reason.
2. Write down, in a dated file in the insider folder, before the first run: the quarters to be used, the config hash, the primary test (already in `config.yaml`: Zac-can-act ledger, 5 trading days, net of cost, excess vs SPY and IWM), and the sentence "results will be read once, after the full run".
3. Do not look at any cluster, ticker or return before the run finishes. The scorecard prints counts and statistics only, no tickers (ruling 11).
4. Do not choose quarters by their outcome. Take every complete quarter in a stated block (suggested: 2016 Q1 through the latest posted quarter, because Alpaca IEX bars start around then, NOT VERIFIED) or state why a quarter is left out before the run.

## Data
- Source: the SEC Insider Transactions Data Sets, one zip per quarter (the adapter `insider/sources.filings_from_dataset_zip` already reads them; offline tests cover it). One request per quarter, cached, under the fair access ceiling. Needs the `SEC_USER_AGENT` environment variable set by Zac and `LIVE-OK.flag`, same as the live pull.
- 2026 Q2 and Q3 files use a different path (pass `--dataset-url`).
- NOT VERIFIED: whether the data sets carry the acceptance time of day. The adapter sets `accepted_utc` to None, so every backfill cluster has `basis date_only`: the signal is the END of the filing date and entry is the open of the next trading day. That is later than the real first trade, never earlier, and the scorecard labels it.
- NOT VERIFIED: the data set column names (matched by alias) and whether it carries footnote text. Without a footnote table the offering screen is UNKNOWN and any same-day same-price group fails the cluster (UNKNOWN = FAIL). That makes the backfill stricter than the live rule; the count of such clusters must be printed.
- Prices: Alpaca IEX daily bars through the watcher's read-only client. NOT VERIFIED: delisted symbol coverage on the free account. Clusters with no bars are MISSING and counted. If more than 5 percent are MISSING the scorecard labels the whole backfill BEST CASE, SURVIVOR-BIASED, upper bound only (config `forward.missing_best_case_over_pct`).
- Join on issuer CIK. The ticker is the one on the completing filing; bars bought by ticker are checked for starting after the signal (ticker reuse) and tagged.

## Steps (when it is built, one at a time, tests after each)
1. `--backtest --dataset-quarter YYYYqN` loops a stated list of quarters, one zip each, cached, writes clusters to a SEPARATE folder `Investing\watch-week\insider\backtest\` with its own `config-history.jsonl` and `LIVE-OK.flag` check. Never mixes with forward files.
2. Clusters are built per quarter with a one-quarter lead-in (the previous quarter's filings are loaded so a window that crosses a quarter edge is complete). Late and amendment rules identical to live.
3. Scoring reuses `insider/forward.py` unchanged (pure functions). Fill status is FILL_UNKNOWN for every backfill cluster (no intraday data), so K2 and K3 cannot be evaluated from a backfill. The scorecard says so.
4. The scorecard is the same builder. Header adds: BACKFILL, dates covered, quarters used, MISSING share.
5. Read once. Write the result and the config hash to `Investing\research\strategies-tried.md` through trading-researcher, whatever it says.

## What a backfill cannot tell us (print this on its scorecard)
- It cannot confirm tradability (no fills, no spreads).
- Clusters share market days, so the sample is smaller than the count.
- Published studies it echoes end by 2007 and are about insiders' own trades, not an outsider acting after the filing.
- A backfill that passes is still only half of a pass. It becomes a request to Zac for a locked-rule change, never adopted automatically.

## Cost
$0 (free SEC data, free Alpaca IEX data). Time: one download per quarter, minutes of scoring.

## Decisions needed before it is built
See `D:\WKP\logs\DECISIONS.md` (TRADING-2026-11-26 entries added 2026-11-27): which quarters, and who writes the pre-registration file.
