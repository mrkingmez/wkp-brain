# WKT insider scanner

Paper research only. It reads official SEC data, finds stocks where 3 or more different officers or directors bought shares on the open market within 10 days, and writes a dated, auditable list. It never places an order, anywhere, and has no sizing and no trade authority. Nothing here is financial advice.

Ordered by trading-director (Fawn Forest Investments), built by software-director 2026-11-26 (v0.1.0), reworked 2026-11-27 to apply the devils-advocate ruling (v0.2.0, GO WITH CHANGES list items 1 to 11, see `CHANGES-2026-11-27.md`). The ruling is `D:\WKP\Investing\watch-week\devils-advocate-ruling-insider-2026-11-26.md`.

**Read this first: 30 counted clusters can KILL this signal. Nothing this year can PROMOTE it from forward data alone.** A pass is a request to Zac for a locked-rule change, never adopted automatically. The insider flag does not feed the stock watcher in any way.

## What it does
1. Reads Form 4 filings from SEC sources only (host allowlist: `www.sec.gov`, `data.sec.gov`). OpenInsider is never touched by the tool.
2. Keeps only non-derivative rows with transaction code P (purchase). S, A, M, F, G and every derivative row are dropped and counted in the skip log. (The SEC form says private purchases also use code P, so P is not purely open market.)
3. A 4/A amendment replaces the original (matched by issuer, the same set of reporting owners and period of report, a heuristic). Amendment rows count only from their own acceptance time.
4. **Who counts (ruling 3):** only owners who tick Officer or Director count toward the 3. 10 percent owner only, Other only, and entity filers (name looks like an LLC, LP, fund or trust, a name heuristic) do not count, and each is logged with its reason. Closed-end funds, BDCs, ETFs and trusts as issuer are excluded whole and logged (SIC or name heuristic). No box ticked at all = UNKNOWN = the cluster FAILS.
5. **What counts as a purchase (ruling 4):** 10b5-1 purchases are excluded and logged (a missing flag on older filings is recorded as unknown, not excluded). Same issuer, same trade date, same price, 2 or more counting owners = an offering-style group: excluded if its footnotes mention offering, placement, IPO, rights or subscription, UNKNOWN and the cluster FAILS if the footnotes cannot be read. Issuers within 90 trading days of their first price bar are excluded at scoring (a heuristic for the listing date), and not enough history to tell = UNKNOWN = excluded. Footnote text is only matched against a word list, never copied to any output.
6. **When a cluster exists (ruling 1):** only at the acceptance time of the filing that brings the distinct count to 3, counting only rows already accepted by then. The 10 day window is measured on trade dates. Purchases reported more than 5 weekdays after the trade are dropped and counted ("dropped, late"). Acceptance time missing = the end of the filing date, labeled `date_only`.
7. **Entry (ruling 1):** the first trade after that acceptance time. With daily bars: the same day's open if accepted at or before 09:00:00 ET on a trading day, otherwise the next trading day's open (labeled, because daily bars cannot price an intraday first trade, so this is never earlier than the real first trade). The Zac-can-act ledger enters one more trading day later (assumption).
8. **Matching (ruling 2):** everything keys on issuer CIK. The ticker is the one on the filing that completed the cluster. Bars that start after the signal (ticker reuse or a new listing) are MISSING, not scored. Bars that end early are marked to the last print and flagged DELISTED_OR_ENDED. The scorecard's first line gives the MISSING share, and more than 5 percent MISSING labels every result BEST CASE, SURVIVOR-BIASED.
9. **Cost and fills (ruling 5):** the scorer logs the entry quote (bid, ask, first-trade time) when it can. Cost each side = the larger of 30 bps and half the measured spread. Bid and ask are NOT available through the watcher client (the quotes path is not on its whitelist), so the floor is used and the cluster is tagged `spread_unmeasured`. A cluster with no IEX print on the entry day, or whose first print comes more than 30 minutes after the open, is UNFILLED and stays in the denominators. With daily bars only, fill is FILL_UNKNOWN, never FILLED.
10. **Benchmarks (ruling 6):** excess against SPY and against IWM. The primary pass needs both positive.
11. **One pre-registered test (ruling 7):** in `config.yaml` under `primary_test`: Zac-can-act ledger, 5 trading days, mean excess net of cost against both benchmarks, officer and director clusters. Every other horizon, split or ladder is printed under EXPLORATORY and cannot change a rule or promote anything. The 5-day pick fits the locked 5-day time stop of the stock rules; 20 days matches the literature but would need a locked-rule change from Zac.
12. **Separate ledger (ruling 8):** own folder, own config, own hash. The code refuses to write inside the stock watcher folder or onto its output file names. It reads only the watcher's regime module, config and read-only bar client.
13. **Kill criteria (ruling 10):** K1 to K7 are values in `config.yaml` and the scorecard has a status table for them.
14. **Freeze (ruling 11):** only clusters whose signal time is after `freeze.counted_signals_from_et` count. Earlier ones are recorded as PRE_FREEZE. Nothing from the 2026-11-26 pull counts. The scorecard names no ticker and no company.
15. Writes to `D:\WKP\Investing\watch-week\insider\`: `clusters.jsonl`, `skips.jsonl`, `forward-returns.jsonl`, `insider-scorecard.md`, `config-history.jsonl`, `cache\`. Every line carries config hash, tool version, run id and mode.
16. The scorecard prints a dollar figure next to every percent at a $15 position.

## Rules of the road
- SEC: User-Agent comes from the environment variable `SEC_USER_AGENT` by name only. The tool refuses to run if it is unset, blank or has no email in it. The value is never printed, logged, cached or hardcoded. Zac sets it himself (DECISIONS TRADING-2026-11-26-27).
- Rate: SEC allows 10 requests per second; this tool is capped at 2 per second in code. Responses are cached on disk. Retries back off 2, 4, 8 seconds. A 403 or 429 stops the run at once, writes `SEC-STOP.flag`, and the tool will not run again until a human deletes that flag.
- Live pull is locked until `LIVE-OK.flag` exists in the insider folder (trading-director writes it after the security pass and QA). This build never created it.
- GET only, https only, redirects only to allowlisted hosts, XML with a DOCTYPE or ENTITY is refused, size capped. No broker code, no order endpoints, no keys of any kind in the scanner. Scoring uses the watcher's read-only Alpaca client (needs the paper keys in the environment by name, never read by this tool directly).
- Learning loop: `config.yaml` is frozen by hash. Any value change starts new counts under a new hash and is dated in `config-history.jsonl`. One value may change per run; several at once are refused unless `--allow-multi-change --reason "why"` is given. Two resets before 30 counted clusters is kill criterion K7.

## Run it (every step)
Python: `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe` (needs PyYAML, `pip install -r requirements.txt`, may already be installed).
1. Open PowerShell. `cd D:\WKP\software\wkt-insider-scanner`
2. Offline demo, no keys, no network, fictional data: `python -I run.py --demo`. Output goes to `demo-out\`. The demo replaces the network socket so any network attempt fails loudly. The demo moves the freeze date back (fictional data is old) so its hash differs from the real one.
3. Tests (about 3 seconds, 190 tests): `python -I -W ignore tests\test_insider.py`. Mutation check (about 2 minutes, 41 mutations): `python -I tests\mutation_check.py`.
4. Live (NOT run yet, locked): set `SEC_USER_AGENT` in your user environment as `Your App Name your.email@example.com`, ask trading-director for `LIVE-OK.flag`, then
   - fresh filings: `python -I run.py --live --route daily --since 2026-11-28 --until 2026-12-05` (one daily index per day plus one filing per Form 4, budget `sec.max_filings_per_run` = 300 per run)
   - history: `python -I run.py --live --route dataset --dataset-quarter 2025q4 --since 2025-10-01 --until 2025-12-31` (one bulk zip; 2026 Q2 and Q3 files use a different path, pass `--dataset-url`). History before the freeze date is recorded as PRE_FREEZE, so it is for looking at the plumbing only.
   - score: `python -I run.py --score` (needs `APCA_API_KEY_ID`, `APCA_API_SECRET_KEY`, `APCA_API_BASE_URL` set as for the watcher), then `python -I run.py --scorecard`.
5. `python -I run.py --backtest` refuses: backtest mode is a design stub only, see `docs\BACKTEST-DESIGN.md`.

## Known limits (honest)
- NOT VERIFIED against a live SEC file: the daily index layout, the bulk data set column names and whether a footnote table exists in them, the Form 4 XML element names beyond what the SEC form page names (`aff10b5One` is believed), the time zone of the acceptance time (`timing.accepted_tz` is an assumption, America/New_York), whether `data.sec.gov` is ever needed (SIC code is not in the data sets, so the fund-issuer flag uses name words only).
- NOT VERIFIED: whether Alpaca IEX daily bars cover delisted symbols or reach back to a given date, whether the first 1-minute IEX bar is a fair first-trade time, Robinhood fractional-share eligibility (logged as UNKNOWN, not used).
- Bid and ask are not available, so every cluster costs the 30 bps floor, and FILL_UNKNOWN is the best fill status daily bars can give. Kill criteria K2 and K3 need intraday data and cannot be fully evaluated until the watcher whitelist allows it (decision queued).
- The bulk data sets lag up to about a quarter. They suit history and backtests, not alerts. Fresh data costs one request per Form 4.
- 4/A matching, entity detection, fund-issuer detection, offering detection and the listing-age check are heuristics. Clusters share market days and are not independent samples. A cluster that existed only before an amendment is dropped when the amendment lands (the as-of replay is not built), which is conservative.
- Cost floor, liquidity floors, the `tiny_base_usd` limit and the Zac extra day are placeholders, not measured.
- The live SEC pull, the live Alpaca scoring (`--score`) and the live quote provider were NOT RUN: no `SEC_USER_AGENT`, no gate file, no keys used by this build. Only the offline demo and tests ran.
- Published studies show effects in insiders' own trades, mostly small firms, samples ending 2007. They say nothing about this tool's result. The cluster-only effect size was not retrieved.

## Cost to run
$0. Free SEC data, free Alpaca IEX data, PyYAML (free).

## Files
`run.py`, `config.yaml`, `insider\` (form4, classify, cluster, sources, sec_client, guards, config, forward, scorecard, runner, bars_live, logio, demo), `tests\test_insider.py`, `tests\mutation_check.py`, `docs\DESIGN.md`, `docs\BACKTEST-DESIGN.md`, `docs\data-sourcing-2026-11-26.md`, `CHANGES-2026-11-27.md`.
