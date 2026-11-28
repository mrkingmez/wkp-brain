# WKT insider scanner scorecard

Price coverage: 1 of 3 scored clusters MISSING (no usable bars, 33.3%), 0 DELISTED_OR_ENDED (marked to the last print). Excluded at scoring (new listing or listing age UNKNOWN), not in any figure below: 1. **BEST CASE, SURVIVOR-BIASED: more than 5% of clusters are missing, so every result below is an upper bound only.**

**30 counted clusters can KILL this signal. Nothing this year can PROMOTE it from forward data alone** (the effect is small next to the noise: a forward sample this size can show no edge, never prove one).
A pass here is a request to Zac for a locked-rule change. It is never adopted automatically. This signal has NO sizing and NO trade authority and does not feed the stock watcher.
Dollar figures sit next to every percent, at a $15 position (25 percent of the $60 account). A real edge at this size is a learning result, not a funding source.

Generated: 2026-11-26 12:00 UTC. Mode: demo (FICTIONAL data, not a result). Config hash: fa8c320da986d0a1. Source: forward-returns.jsonl. Paper research only: this signal has NO sizing and NO trade authority.

## Counts
- COUNTED clusters scored under this config hash: 4 (of which excluded at scoring and in no figure below: 1). Clusters seen but not counted (WATCH tier, 2 insiders): 4. Counted clusters found in the latest clusters file: 4.
- Forward-return lines from older config hashes, not counted here: 0.
- Clusters with a signal at or before the config freeze (2026-01-01T00:00:00), recorded as PRE_FREEZE and never counted or scored: 0.

**NO VERDICT. Fewer than 30 counted clusters (4). Everything below is plumbing output, not evidence.**

## PRIMARY TEST (pre-registered 2026-11-27, frozen in config.yaml, the only result that can mean anything)

- Population: officer and director clusters as the cluster and filing rules define them. Ledger: Zac-can-act. Horizon: 5 trading days (hold from the entry open to the close of day 5).
- Metric: mean excess return net of cost (the larger of 30 bps and the measured half spread, each side) against SPY and against IWM. Pass condition: positive against BOTH.
- Clusters in the figures: 1 (FILLED 0, FILL_UNKNOWN 1). Not in the figures: UNFILLED 1, pending 1, unknown or missing price 0, a benchmark bar missing 0.

- Excess vs SPY: n=1, median -1.83% (-$0.27 on $15), mean -1.83% (-$0.27), hit rate 0%
- Excess vs IWM: n=1, median -0.80% (-$0.12 on $15), mean -0.80% (-$0.12), hit rate 0%

Forward leg: NOT ENOUGH CLUSTERS (1 of 30 needed). Nothing here is evidence yet.

## KILL CRITERIA STATUS (from config.yaml, written before any data)

| Id | Name | Status | Detail |
|---|---|---|---|
| K1 | no edge | NOT YET | 1 of 30 clusters in the primary figures |
| K2 | untradable | NOT YET | 2 of 30 qualifying clusters (UNFILLED 1, FILL_UNKNOWN 1) |
| K3 | too expensive | NOT YET | 0 of 30 FILLED clusters; 1 are FILL_UNKNOWN (no intraday first-trade data), so this cannot be checked yet |
| K4 | too rare | NOT TRIGGERED | first counted day 2026-10-15, deadline 2027-04-16, counted 3 of 30 |
| K5 | backfill fails | NOT EVALUABLE | no backfill has been run (design stub only, docs/BACKTEST-DESIGN.md). No forward run is justified by a backfill yet |
| K6 | look-ahead found | NOT TRIGGERED | automated checks clear (every scored entry is after its signal instant, every contributing filing was accepted by the signal time). qa-claims owns the real K6 finding |
| K7 | tuning | NOT TRIGGERED | 0 config reset(s) so far, 3 counted clusters |

No kill criterion is triggered. That is not a pass and promotes nothing.

## Rules used
- Entry: the first trade after the acceptance time of the filing that completed the cluster. With daily bars that is the open of the same day if accepted before the cutoff, else the open of the next trading day (labeled). If the acceptance time is missing, the open of the first trading day after the filing date (labeled). Zac-can-act ledger: 1 trading day later (assumption). Never the insider's own price.
- Hold h trading days (1, 5, 20): entry open to the close of day entry + h - 1. Excess = stock net of cost minus the benchmark gross over the same two dates.
- Cost each side: the larger of 30 bps and half the measured spread. Without a measured spread the floor is used and the cluster is tagged spread_unmeasured.
- Data: Alpaca IEX daily bars, read-only, feed=iex. IEX volume is thin, so dollar-volume tags are an under-count.
- Separate ledger and config: this scanner has its own folder, config file and hash. It writes nothing to the stock watcher and its flag never enters the watcher score, config, decisions or counts. A pass here is a request to Zac for a locked-rule change, never adopted automatically.

## EXPLORATORY (cannot change a rule or promote anything; a rule from here must be re-tested on clusters accepted after it was proposed)

Haircut ladder (bps each side, assumption): 5, 15, 30. Headline column uses 30 bps. Excess here is against SPY only.

### Zac-can-act ledger, all horizons

| Horizon | Excess vs SPY at 30 bps (all) | Excluding illiquid-tagged | At 5 bps (all) | Pending | Unknown |
|---|---|---|---|---|---|
| 1 days | n=1, median -0.09% (-$0.01 on $15), mean -0.09% (-$0.01), hit rate 0% | n=1, median -0.09% (-$0.01 on $15), mean -0.09% (-$0.01), hit rate 0% | n=1, median +0.41% (+$0.06 on $15), mean +0.41% (+$0.06), hit rate 100% | 1 | 1 |
| 5 days | n=1, median -1.83% (-$0.27 on $15), mean -1.83% (-$0.27), hit rate 0% | n=1, median -1.83% (-$0.27 on $15), mean -1.83% (-$0.27), hit rate 0% | n=1, median -1.34% (-$0.20 on $15), mean -1.34% (-$0.20), hit rate 0% | 1 | 1 |
| 20 days | n=1, median +2.68% (+$0.40 on $15), mean +2.68% (+$0.40), hit rate 100% | n=1, median +2.68% (+$0.40 on $15), mean +2.68% (+$0.40), hit rate 100% | n=1, median +3.17% (+$0.48 on $15), mean +3.17% (+$0.48), hit rate 100% | 1 | 1 |

Split by insider type, 5-day horizon, 30 bps:

- ceo_cfo_involved: n=1, median -1.83% (-$0.27 on $15), mean -1.83% (-$0.27), hit rate 0% (pending 0, unknown 0)  (n under 5: anecdote)
- officers_directors: no data (pending 1, unknown 1)

Split by regime at entry, 5-day horizon, 30 bps:

- DOWNTREND_VOLATILE: no data (pending 0, unknown 0)
- RANGE: n=1, median -1.83% (-$0.27 on $15), mean -1.83% (-$0.27), hit rate 0% (pending 1, unknown 1)  (n under 5: anecdote)

### Main ledger (first possible entry), all horizons

| Horizon | Excess vs SPY at 30 bps (all) | Excluding illiquid-tagged | At 5 bps (all) | Pending | Unknown |
|---|---|---|---|---|---|
| 1 days | n=2, median +0.23% (+$0.03 on $15), mean +0.23% (+$0.03), hit rate 100% | n=2, median +0.23% (+$0.03 on $15), mean +0.23% (+$0.03), hit rate 100% | n=2, median +0.73% (+$0.11 on $15), mean +0.73% (+$0.11), hit rate 100% | 0 | 1 |
| 5 days | n=1, median -4.49% (-$0.67 on $15), mean -4.49% (-$0.67), hit rate 0% | n=1, median -4.49% (-$0.67 on $15), mean -4.49% (-$0.67), hit rate 0% | n=1, median -4.00% (-$0.60 on $15), mean -4.00% (-$0.60), hit rate 0% | 1 | 1 |
| 20 days | n=1, median +2.76% (+$0.41 on $15), mean +2.76% (+$0.41), hit rate 100% | n=1, median +2.76% (+$0.41 on $15), mean +2.76% (+$0.41), hit rate 100% | n=1, median +3.25% (+$0.49 on $15), mean +3.25% (+$0.49), hit rate 100% | 1 | 1 |

Split by insider type, 5-day horizon, 30 bps:

- ceo_cfo_involved: n=1, median -4.49% (-$0.67 on $15), mean -4.49% (-$0.67), hit rate 0% (pending 0, unknown 0)  (n under 5: anecdote)
- officers_directors: no data (pending 1, unknown 1)

Split by regime at entry, 5-day horizon, 30 bps:

- DOWNTREND_VOLATILE: no data (pending 0, unknown 0)
- RANGE: n=1, median -4.49% (-$0.67 on $15), mean -4.49% (-$0.67), hit rate 0% (pending 1, unknown 1)  (n under 5: anecdote)

## Tags (kept in, never dropped silently)

- no_bars_at_all(possible_delisting_not_on_iex_or_bad_ticker): 1
- no_entry_bar: 1
- spread_unmeasured: 3

## Honest limits
- Clusters cluster in time and share the same market days, so they are not independent samples.
- Survivorship: a delisted or non-IEX ticker returns no bars and shows as MISSING. Results are labeled best case when more than 5% are missing.
- Haircut ladder, liquidity floors and the cost floor are placeholders. Sponsor, fund and entity detection are name heuristics. Bid and ask are not available through the watcher client, so spreads are unmeasured.
- Fewer than 30 counted clusters is no verdict, and even more is evidence about this one rule set only, not advice.
- Any config change resets these counts (new hash). One change per run.
