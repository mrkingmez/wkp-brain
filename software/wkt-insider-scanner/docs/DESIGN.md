# Design, short (software-director, 2026-11-26)

No separate software-architect run: the design was small and fixed by the trading-director order, so it is written here from the order, the SEC terms brief (`Investing\research\insider-data-terms-2026-11-26.md`) and data-sourcing's note (`data-sourcing-2026-11-26.md`). Say so honestly: the architect bench was not used.

## Route
Official SEC only. Two adapters make the same filing dict: (A) quarterly Insider Transactions Data Sets (one zip per quarter, history and backtests, lag up to about a quarter), (B) EDGAR daily index plus one `.txt` submission per Form 4 (fresh filings, request budget capped in config). Both are behind one SecClient: allowlist, 2 per second ceiling, cache, backoff, stop on 403 or 429. OpenInsider is not used by the tool. Atom getcurrent and data.sec.gov submissions JSON were left out because their layouts were not retrieved (NOT VERIFIED), not because they are bad.

## Data flow
filings (XML parse or zip adapter) -> supersede 4/A -> purchases (code P, non-derivative, acquired) -> clusters per issuer by sliding window of transaction dates -> clusters.jsonl and skips.jsonl -> (separately) forward returns for COUNTED clusters -> forward-returns.jsonl -> insider-scorecard.md.

## Decisions
- Window: inclusive N days (last minus first <= N-1). Signal date = earliest filing date at which the filings already seen held a qualifying window (point in time, day granularity), not the last filing of a growing cluster.
- Cluster id = tier letter + issuer CIK + first transaction date, stable across re-runs; a re-run appends a new line (one line per cluster per run, as ordered), the scorer keeps the latest line per id.
- Entry: first trading day strictly after the filing date (date-only data never justifies same-day entry). Zac ledger one more trading day (config assumption).
- Haircut on the stock leg only, SPY gross. Excess = net stock minus SPY gross.
- Regime: the watcher's `wkt.regime.compute`, imported by path from `forward.watcher_dir`, bars strictly before the entry date. Missing module or bars = UNKNOWN.
- Joint filings: every owner CIK counts (as ordered) but the cluster is flagged `joint_filing_inflated` when filings are fewer than insiders, so the scorecard reader can see it.
- UNKNOWN type fails the cluster. Sponsor and fund flags are labeled heuristics and only change the count if `exclude_sponsor_from_count` is true.
- Security: XML with DOCTYPE or ENTITY refused (stdlib parser, no defusedxml dependency), size caps before and after gzip, redirects by hand to allowlisted hosts only, UA in memory only.
- Not built: opportunistic versus routine insider filter (the research brief suggests it as a later one-change test), Atom feed, per-issuer data.sec.gov SIC lookup.

## Update 2026-11-27 (v0.2.0, devils-advocate ruling applied, see CHANGES-2026-11-27.md)
These lines replace the matching v0.1.0 bullets above.
- Signal: the acceptance instant (ET) of the filing that brings the distinct counting owners to the minimum, counting only rows accepted by then (`cluster._signal`). Window on trade dates. Late rows (more than 5 weekdays) dropped and counted. Date-only filings use the end of the filing date and are labeled.
- Entry: the first trade after the signal instant. Daily bars: same-day open if accepted before 09:00 ET, else the next trading day's open (`forward.entry_index`). The Zac ledger adds one trading day.
- Who counts: officer or director box ticked, not an entity name, issuer not a fund or trust. UNKNOWN type fails the cluster. The old `exclude_sponsor_from_count` switch is gone (replaced by `count_roles`, `exclude_entity_owners`, `exclude_fund_issuers`).
- Purchase screen: 10b5-1 out, offering-style same-day same-price groups out when a footnote word hits, UNKNOWN (unreadable footnote) fails the cluster, new listings out at scoring.
- Score record: data_status (OK, MISSING, DELISTED_OR_ENDED), excluded reason, per ledger the entry quote, cost each side, fill status (FILLED, UNFILLED, FILL_UNKNOWN), per horizon the excess against SPY and IWM net of cost.
- Scorecard: coverage line, asymmetric header, dollar figures, PRIMARY TEST, KILL CRITERIA STATUS, EXPLORATORY. No ticker or company name is ever printed.
- Config blocks added: timing, primary_test, isolation, kill_criteria, freeze. Config hash is computed over all of them.
- The freeze is applied in `runner.apply_freeze`, not in the pure cluster rules.
