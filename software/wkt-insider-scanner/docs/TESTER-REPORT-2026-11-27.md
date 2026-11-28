# Tester report: wkt-insider-scanner v0.2.0 (2026-11-27)

Tester: software-tester, for software-director. Report only. Nothing in the product was fixed or edited. No network call of any kind, no live SEC call, no LIVE-OK.flag or SEC-STOP.flag in any real folder, no real key or SEC_USER_AGENT value used (only the obviously fake value "SENTINELUAvalue99 sentinel@example.invalid", set inside scratch processes), nothing under the stock watcher folder touched, no git, no spend.

Scratch work: `D:\WKP\scratch\test-wkt-insider-scanner\` (a copy of the product, byte for byte the same as the product at test time, checked file by file) and `D:\WKP\scratch\tester-insider\` (probe scripts p1 to p6 and their output).

## VERDICT: PASS WITH NOTES for the offline v0.2.0 as delivered

No blocker for the offline build: the tests pass, every mutation is caught, the gates hold, no secrets, no network, no order code, and I could not build a counted entry that comes before its signal.

But one finding (F1) makes the counted list wrong once the tool runs live more than once, and two more (F2, F3) are cheap to fix and should be closed first. I recommend **F1, F2 and F3 are fixed before trading-director writes LIVE-OK.flag**. Everything else is a note.

## What I ran (real numbers)

| Check | Command | Result |
|---|---|---|
| Test suite | `python -I -W ignore tests\test_insider.py` in the product folder | `Ran 190 tests in 3.718s` then `OK`. README says about 3 seconds: true. |
| Mutation check | `python -I tests\mutation_check.py` | final line `41 mutations, 41 killed, 0 survived`. It works on a scratch copy. README says about 2 minutes; it took far longer here while other agents were running (QA saw over 14 minutes). I did not time it exactly. |
| Demo, run from my scratch copy using only the README | `python -I run.py --demo` | `demo: 9 clusters (4 counted), 13 skips, 4 forward records, scorecard ...\demo-out\insider-scorecard.md`, exit 0. All five output files were byte for byte identical to the product's own demo-out (clusters, skips, forward-returns, scorecard, config-history). |
| Watcher folder before and after the demo | 40 files, size, modified time and md5 snapshot before and after | identical. Note: another agent was editing the watcher folder at 11:39 (config.py, engine.py, config.yaml, README, tests, and their .pyc files). That was before my snapshot and was not me or the scanner. |
| Adversarial probes | six scripts, about 300 individual cases (below) | findings F1 to F14 |
| Look-ahead fuzz | 4,000 random three-insider clusters, acceptance times at all hours, weekends, four fake holidays, both ledgers, 8,000 entries checked | 0 violations (details in section 4) |

## Findings

Severity words: BLOCKER-FOR-LIVE means fix before LIVE-OK.flag. NOTE means worth fixing, not stopping. All fixes are suggestions only, none applied.

### F1. BLOCKER-FOR-LIVE. The clusters file is append-only, so a cluster that later disappears or moves keeps counting
Evidence (probe p4_files.py, section 4a, real functions, scratch folder):
- Run 1 finds a COUNTED cluster `C-1-2026-11-02`. Run 2 gets a 4/A that removes one buyer. In memory the cluster is now WATCH, but the file view still holds `C-1-2026-11-02 COUNTED` next to `W-1-2026-11-02 WATCH`. `run.py --score` reads that file and would score the removed cluster (output: "run_score would score cluster ids: ['C-1-2026-11-02']").
- Run 2 gets an extra, earlier insider (first trade date moves from 11-02 to 11-01). The cluster id is built from the first trade date, so the id changes: the file now shows two COUNTED ids (`C-1-2026-11-01` and `C-1-2026-11-02`) for the same buying. Count = 2 instead of 1.
- A WATCH cluster that later becomes COUNTED stays in the WATCH total as well.
Why it matters: K1, K4 and the primary test all use these counts, and the same buying would be counted and scored twice. It is silent. The scorecard shows a number, not a warning.
Suggested fix: make the cluster id stable (issuer CIK plus the accession that completed the signal), and when a new run no longer produces a COUNTED cluster for an issuer, append a RETRACTED line that `--score` and the scorecard honour. Add a test that replays two runs.

### F2. NOTE (close before live). Isolation guard runs too late
Evidence (p4_files.py 4b, using a FAKE watcher folder in scratch, never the real one):
- `run.py --score --outdir <folder inside the watcher folder>` exited 0 and wrote `config-history.jsonl` inside that folder (via `record_config`) before any guard ran. Only `--scorecard` refused. `--live` creates the folder and cache directory before the check as well.
- `--score` into a folder that already holds `state.json` also ran (exit 0) and wrote into it.
- A junction (Windows folder link) pointing into the watcher folder was not refused: `assert_own_ledger` compares `abspath`, not `realpath`.
- `forward.watcher_dir` is a config value, so one edited line moves the guard (it is hashed and logged, so it is visible, but nothing refuses it).
Needs a deliberate `--outdir`, so the real chance is low, but ruling 8 says the scanner writes nothing to the watcher.
Suggested fix: call `assert_own_ledger(outdir, cfg)` first thing in `main` for every mode, compare real paths, and pin the watcher folder in code instead of config.

### F3. NOTE (README is wrong, cheap fix). tzdata is missing from requirements.txt
`requirements.txt` lists only PyYAML and the README says that is the only extra. But `cluster.py`, `forward.py` and `config.py` use `ZoneInfo("America/New_York")`. On Windows without the `tzdata` package this fails at import. I simulated it (tzdata blocked, no system tz database): `ZoneInfoNotFoundError`. It works on this PC only because `tzdata 2026.3` is installed. A fresh machine, or the planned second machine, would stop on the very first command.
Suggested fix: add `tzdata` to requirements.txt and the README line.

### F4. NOTE. Acceptance time strings: offsets are ignored and a bare date counts as midnight
Evidence (p3_logic.py 3a):
- `accepted_utc = "2026-10-06T08:30:00-08:00"` (true time 11:30 ET) is read as 08:30 ET, so the cluster gets a same-day open entry that the real time would not allow. "+00:00" and "Z" are also read as ET. Only the first 19 characters are used.
- `accepted_utc = "2026-10-06"` (date only) is read as 00:00 and labeled `time`, so entry is the same-day open.
- `timing.accepted_tz` accepts any valid zone: UTC, Asia/Tokyo and "EST" all validate. If the real zone is ET and the config says UTC, entries move earlier than possible, and the K6 automated check cannot see it because it uses the same instant.
Today's real inputs (the 14 digit SGML header, no offset) are not exposed. The risk is a new source or a wrong zone setting. QA also flagged the zone as the likeliest silent error.
Suggested fix: require HH:MM:SS, refuse or convert offsets, and make "check one real accepted timestamp against the zone" a go-live item.

### F5. NOTE. A missing bar on the exit day removes a cluster from the primary figures and is not counted as MISSING
Evidence (p3_logic.py 3e): a stock with one missing bar on its 5 day exit day gets state UNKNOWN, `data_status` stays OK, the primary section drops it (`unknown 1`), and the line-one MISSING share reads `0 of 1`. So thin names with no IEX print on one day leave the sample without raising the BEST CASE label. Bars that END early are handled well (marked to last print), but a gap in the middle is not.
Suggested fix: mark to the last print for gaps too, or count UNKNOWN exits in the MISSING share.

### F6. NOTE. Same-day 4/A can fail to replace its original (dataset route)
Evidence (p3_logic.py 3c): when no acceptance time exists (the dataset route) and the amendment and original are filed the same day, order falls back to the accession string. An amendment whose accession sorts lower than the original does not supersede it. Both are kept and the cluster stays COUNTED although the amendment removed a buyer.
Suggested fix: when times are missing and the filing dates are equal, treat the 4/A as later.

### F7. NOTE. Offering-footnote keyword matching misses and over-matches
Evidence (p3_logic.py 3f), two same-day, same-price counting owners:
- NOT caught: "private placements", "underwriters discount", "subscriptions", "direct share program", "PIPE financing".
- Caught: "initial public offering", "Private Placement", "IPO", "IPO's", "Rights-offering".
- Over-matched (group excluded): "voting rights of common stock", "shareholder rights plan". The matcher joins ALL footnotes of the filing, not just the ones the row points to, so any boilerplate with the word "rights" can drop a genuine same-day same-price group.
- Correctly NOT matched: "COPYRIGHTS", "iPod", "open market purchase on the NYSE".
Suggested fix: match word stems (placement/placements), use only the footnotes the row references, add PIPE and direct-share terms to config.

### F8. NOTE. Config validation has gaps
Accepted by `validate` (p3_logic.py 3g), then crash or misbehave:
- `cluster.window_days = 10**7` loads fine and then crashes `find_clusters` with `OverflowError: date value out of range`.
- `forward.missing_best_case_over_pct = "x"` and `forward.min_counted_for_verdict = "abc"` load fine and crash later in the scorecard, after the clusters file is already written.
- `sec.backoff_seconds = -5` (a negative sleep crashes on the first retry), `sec.timeout_seconds = -1`, `sec.max_response_bytes = 10**12` (removes the gzip-bomb ceiling) and `ceo_regex = "("` all load.
- True is accepted where integers are expected (`window_days`, `max_filing_lag_business_days`).
- `sec.user_agent_env` can name any environment variable, for example the Alpaca secret variable. The only protection is the "must contain @" rule in `load_user_agent`. A variable with an @ in it would be sent to sec.gov as the User-Agent.
- Kill criteria and the freeze date can be loosened with a single value change (hashed and logged, and K7 counts resets). Deleting `config-history.jsonl` makes the next run look like a first run, so no reset is counted (p6_out.py).
Suggested fix: validate every key the code reads, cap `window_days`, restrict `user_agent_env` to a fixed name, and make a missing history file an error once clusters exist.

### F9. NOTE. Weak checks on filing values
- User-Agent check accepts "@" and "x@" (only "has an @").
- A P row with price 0 or a negative price is kept as a purchase (value 0.0 or -5000.0). Price text "1_0" reads as 10.
- A trade dated in the future of its filing (trades on 10-05 to 10-07 reported on 10-02) is kept, with negative lag, and forms a COUNTED cluster.
- A trade dated 0001-01-01 costs about 0.2 s per row (`business_lag` counts day by day, 528,493 steps measured). Many such rows in one 5 MB filing is a slow-down.
- Huge values (1e200 x 1e200) write `Infinity` into clusters.jsonl, which is not valid strict JSON.
Suggested fix: drop or flag non-positive prices and future-dated trades, count weekdays by arithmetic, and refuse non-finite values.

### F10. NOTE. Bad dataset zips and bad downloads crash instead of being logged
Evidence (p4_files.py 4d, p1_security.py):
- A zip table with one field over 131,072 characters raises `csv.Error` and kills the run (a footnote that long, or any long field). Not caught.
- A zip with a damaged compressed member raises `zlib.error`, uncaught.
- A truncated gzip body is accepted and cached as complete (no end-of-stream check). A body marked gzip that is not gzip raises `zlib.error` instead of the tool's own FetchError.
- `parse_form4(None)` raises TypeError (cannot happen from the real callers).
Good news in the same area: not-a-zip, empty zip, missing table, missing columns, short rows, NaN and inf values, NUL bytes, duplicate member names, odd member names and a 130 MB member streamed in 2.7 s all behaved (clean error or clean skip).
Suggested fix: catch `csv.Error`, `zlib.error`, `zipfile.BadZipFile` around the table reads and log a skip. Check the gzip stream finished.

### F11. NOTE (low). Daily index parsing and request volume
- The line pattern in `parse_daily_index` hangs on a pathological line: `"4" + 5000 spaces + "x"` ran over 25 seconds and did not finish (also at 10,000, 20,000, 40,000). SEC supplies this text so exposure is small, but there is no timeout.
- `--since` has no limit on the number of days, and the budget `max_filings_per_run` caps only the per-filing fetches, not the daily index fetches (one request per weekday in the range).
- Cache entries never expire, so a daily index fetched while still incomplete would be reused (not verified against the real SEC schedule).

### F12. NOTE. Housekeeping and portability
- The test suite creates a temp folder per test in `D:\WKP\scratch` and does not delete them. There are now 8,675 `insider-*` folders there (growing every run), many holding a `LIVE-OK.flag`. A search for LIVE-OK.flag under D:\WKP finds hundreds of fake ones (QA N7 raised the same trap). Real folder `D:\WKP\Investing\watch-week\insider\` is empty: no flag, no output (I checked with find).
- Hardcoded paths that also appear in LOCAL-PATHS territory: `run.py` line 26 (insider output folder), `config.yaml` line 64 (watcher folder), `tests\test_insider.py` line 29 and `tests\mutation_check.py` line 10 (`D:\WKP\scratch`). The tests will not run on a machine without a D: drive.
- Running tests or the demo from the product folder rewrites `__pycache__` inside the product.

### F13. NOTE. Process and text mismatches
- Ruling item 11 said no build until the stock watch week's first scorecard passed and Zac set the SEC User-Agent. The build exists. The live gate (LIVE-OK.flag) still enforces "no live", so this is a process note for trading-director to acknowledge, not a code defect.
- Ruling item 13 literally says dollar figures at $60. The tool prints them at the $15 position (QA N2 says the same). It is stated openly in README and CHANGES.
- README item 7 says "accepted before 09:00 ET"; code and config say "at or before 09:00:00". I tested 09:00:00 (same-day open) and 09:00:01 (next open).
- QA N1 (cluster status and type use filings accepted after the signal) I did not re-test; I agree with its description only from reading the code.

## Security pass (task item 2)

| Check | Result | Evidence |
|---|---|---|
| (a) No keys, tokens, passwords, SEC_USER_AGENT value | PASS | grep for AWS, key, token, bearer, private key, password and secret patterns over the whole product folder: no hits. Only email-like text is the README placeholder `your.email@example.com` and the test sentinel. demo-out: no hits. `D:\WKP\Investing\watch-week\insider\` is empty. No file in the product reads or stores the SEC_USER_AGENT value; env names used: `SEC_USER_AGENT` only through `guards.py` line 42. |
| (b) Host allowlist | PASS | `guards.py` lines 19 to 27. 23 URL tricks tried (p1_security.py): allowed only the plain https URLs on www.sec.gov and data.sec.gov (and port 443, and an uppercase host, which is the same host). Blocked: http, ftp, file, `user@evil`, backslash tricks, port 8443, trailing dot, lookalike hosts, newline injection, IPs. `https://www.sec.gov:abc/` raised ValueError instead of GuardError (still blocked). Redirects: to evil host, to http, scheme-less `//evil`, userinfo trick all refused; loop stops after 2 hops; redirect to data.sec.gov allowed; 429 on a redirect target stops the run. Config cannot widen: config listing `evil.com` and `*` still gave only the two SEC hosts; a string instead of a list gave no hosts (fails closed). Rate ceiling 2 per second even when config says 1000. Redirects are not followed by urllib (manual only). |
| (c) No order endpoint, broker import, POST/PUT/DELETE | PASS | grep of `insider\` and `run.py`: the only HTTP verb is `method="GET"` (sec_client.py line 39). The only broker-related imports are `wkt.alpaca.AlpacaReadOnly`, `wkt.guards.load_env`, `wkt.engine.parse_bars` inside `bars_live.py`, i.e. the watcher's read-only data client (I read its source: `method="GET"` only). `--score` is NOT run by me (needs real keys). |
| (d) Gate file | PASS | End to end `run_live` with a FAKE transport, socket and DNS patched to explode, in a scratch folder: no flag gives `GuardError ... locked until LIVE-OK.flag`; flag but no UA gives the UA refusal; a fake 403 stops the run, writes `SEC-STOP.flag` (text names the status and host, no UA), and a re-run is refused until the flag is deleted. `--dataset-url` with http or another host is refused. Real folders: `find /d/WKP -name LIVE-OK.flag -not -path "*/scratch/*"` and the same for SEC-STOP.flag returned nothing. (I made LIVE-OK.flag and SEC-STOP.flag only inside scratch temp folders, as the product's own tests do. If your rule meant not even there, say so.) |
| (e) User-Agent handling | PASS with note F9 | Env read by name only. Refused: unset, blank, spaces, no @, tab inside, non-ASCII, over 200 characters; none of the refusal messages echo the value. With the fake sentinel through the FAKE-transport run: every request carried the header, hosts were only www.sec.gov, and the sentinel is in none of the output files (cache bodies and meta, clusters, skips, config-history, flag file, scorecard). `repr(SecClient)` hides it. A network error message does not carry it (`gave up after 4 attempts (OSError)`). |
| (f) Writes stay in the output folder; traversal; torn files | PASS with F2 | Cache name is a sha256 of the URL, so accession numbers and URLs cannot make a path. Output names are fixed. Torn cache meta: refetched. Truncated cache body with a valid meta: served from cache (the `bytes` field is not checked, minor). Torn last line in clusters.jsonl: next write starts a fresh line and the torn piece is skipped on read. Torn config-history line: skipped, next record written. Scorecard is written with a plain open (not atomic). `--dataset-quarter` text lands in the URL path only, host fixed. See F2 for the one early-write gap. |
| (g) Injection from filing text | PASS with F9, F10 | DOCTYPE, ENTITY, billion laughs, external entity, mixed-case DOCTYPE: all refused (`forbidden_doctype`). Undefined entity, `&#0;`, NUL byte, UTF-16 bytes: clean error codes. 6 MB: `too_large`. 200,000 nested elements: clean error in 0.05 s. A filing with 10,000 transactions exceeded the 5 MB cap and was refused. Footnotes capped at 2,000 characters and 60 notes. A footnote full of instructions, script tags, markdown and 100,000 characters never appeared in any output; offering groups log only the fixed matched words. Names with CSV formulas, markdown headings and pipes, JSON-breaking quotes, line separators, a 300,000 character name and a ticker with a newline: every output line is valid JSON, and the scorecard contained none of that text (the scorecard prints no filing text, only counts). The 300,000 character name was copied whole into clusters.jsonl (no length cap on names, note). Numeric edges: negative, zero, NaN, inf, 1e999 shares are dropped as `P_unusable`; price edges see F9. Zip probes: see F10. |
| (h) Isolation | PASS with F2 | Demo run left the watcher folder identical (40 files, size, time, md5). Static read: writes are `open(..., "a"/"w")` to fixed names in the output folder, `os.remove` only of five named demo files, `os.replace` only for cache bodies. `logio.append_jsonl` refuses `decisions.jsonl`, `paper-trades.csv`, `state.json`. Gap: F2. Python may rewrite `.pyc` files inside the watcher folder when it imports its modules and they are stale; they were fresh in my run so nothing changed. |
| (i) Dependencies | PASS with F3 | `requirements.txt`: `PyYAML>=6.0`. Installed 6.0.3, license MIT. Code uses `yaml.safe_load` only (config.py line 31), so the old unsafe-load problems do not apply. I could not check a live advisory database (no network), so "no known issue" is from my own knowledge, not a lookup. The hidden dependency is `tzdata` (Apache-2.0), see F3. Everything else is the standard library. |

## Task item 3: new logic, bad input (summary of what behaved and what did not)

Behaved correctly (real functions, offline):
- Acceptance at 08:59:59 and exactly 09:00:00 give same-day open; 09:00:01, 09:29:59, 16:00 and 23:59:59 give the next trading day. Saturday and Sunday signals go to Monday. Friday 18:00 goes to Monday. A day missing from the bars (holiday) falls to the next bar. Time zone garbage in config (`Not/AZone`, `../etc`, empty) is refused. Garbage accepted text (`garbage`, `25:99:99`, empty, compact digits) falls back to date-only (end of the filing date, next open).
- A filing accepted more than 4 days before its filing date, or after it, becomes date-only.
- Duplicate accessions: the second is logged `duplicate_accession`. Two filings with accession None: the second is logged as a duplicate and dropped (logged, not silent; real routes always set an accession).
- Two CIKs sharing a ticker produce separate clusters; a ticker that is empty becomes None and scores as MISSING and UNFILLED, no crash.
- Bars: stock bars shorter than 90 days, or starting mid-history, are excluded as new listing or unknown listing age (logged on the record). Stock bars that end early are marked to the last print. IWM missing: `score_run` refuses and writes nothing; `score_cluster` keeps the cluster and flags `bench_missing`, which the primary section counts. SPY with a missing day silently lengthens the hold by a calendar day (exit date 10-20 instead of 10-19; minor).
- Quotes: bid greater than ask, zero, negative, NaN, inf, strings, None all fall back to the 30 bps floor (`spread_unmeasured`); a very wide spread gives 9,802 bps each side without crashing. First trade on another day: FILL_UNKNOWN; exactly 30 minutes: FILLED; 30 minutes 1 second: UNFILLED; before the open: FILLED. A naive (no offset) first-trade time is read in the machine's own time zone (not tested under another zone).
- A COUNTED cluster whose members flip to WATCH when a buyer is removed: handled in memory, but see F1 for the file.

Problems found are F1, F4, F5, F6, F7, F8, F9 above.

## Task item 4: look-ahead rule, checked by hand

Method: used the product's own helpers (`filing_at`, `three_at`, `clusters_of`) plus my own generator. 4,000 random clusters: three filings accepted at random second of random days (weekends included) over a calendar with four removed holidays; trade dates up to 1 day before acceptance; freeze moved out of the way for the test only. Each counted cluster scored on both ledgers with real bars.
- Entries checked: 8,000. Entry open (09:30 ET) at or before the signal instant: **0**.
- Contributing filing accepted after the signal instant: **0**.
- Zac-ledger entry not later than main entry: **0**. Entry on a weekend or removed holiday: **0**.
- Entry basis mix: 1,780 same-day opens, 6,220 next opens. The scorecard K6 check never fired.
- By hand, the boundary: accepted 09:00:00 enters that day's open (09:30), 09:00:01 enters the next day.
So the ruling's rule holds for the inputs the tool really produces. The two ways I found to break it (F4) need an input the real routes do not make, or a wrong zone setting.

## Task item 5: how Zac runs it, in plain words

Nothing here needs a key, a login or the internet.
1. Open PowerShell. Type `cd D:\WKP\software\wkt-insider-scanner` and press Enter.
2. Demo: type `python -I run.py --demo` and press Enter. (If PowerShell says it does not know `python`, use the full path from README: `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe -I run.py --demo`. The README gives the full path in the Python line but then writes only `python` in the steps, which is a small confusion.) It takes a couple of seconds and ends with a line like `demo: 9 clusters (4 counted), 13 skips, 4 forward records, scorecard ...`. All the data is invented.
3. Open `demo-out\insider-scorecard.md` in any text editor.
4. Tests: `python -I -W ignore tests\test_insider.py`. Success is the last line `OK` and `Ran 190 tests`. About 4 seconds.
5. Mutation check (optional): `python -I tests\mutation_check.py`. Success is `41 mutations, 41 killed, 0 survived`. Allow 5 to 15 minutes.
6. Do NOT try `--live`. It refuses until trading-director writes LIVE-OK.flag, and it also needs you to set SEC_USER_AGENT yourself.
Side effect to know: the tests leave thousands of small folders in `D:\WKP\scratch` (F12).

What the demo scorecard says, top to bottom:
- Line one, "Price coverage: 1 of 3 scored clusters MISSING (33.3%) ... BEST CASE, SURVIVOR-BIASED". The demo includes a made-up stock with no price history on purpose, so this warning is expected here.
- The bold header: 30 counted clusters can kill the idea, nothing this year can prove it; any pass is only a request to you; no sizing, no trading.
- Dollar figures sit next to every percent, based on a $15 position.
- Counts: 4 counted clusters, 4 watch-tier, 0 before the freeze date. Then "NO VERDICT, fewer than 30".
- PRIMARY TEST: the one pre-registered test (5 trading days, you-can-act ledger, after costs, against SPY and IWM). In the demo it has 1 cluster, so it prints "NOT ENOUGH CLUSTERS (1 of 30)". The -1.83% (-$0.27) number is made up.
- KILL CRITERIA table K1 to K7: in the demo most say NOT YET, K5 says NOT EVALUABLE (no backfill exists), K6 says NOT TRIGGERED (no look-ahead found), K7 NOT TRIGGERED.
- EXPLORATORY section: other horizons and splits, labeled as unable to change any rule.
- Tags and honest limits at the bottom.
Plain-language problems a non-technical reader would hit: many unexplained terms (FILL_UNKNOWN, spread_unmeasured, UNFILLED, PRE_FREEZE, binding benchmark), and the "Pending / Unknown" columns look like errors. The demo card has a changing "Generated" date and a hash that differs from the real config hash (explained in README but easy to miss). A short glossary at the bottom of the scorecard would help.

## What I could NOT verify (not guessed)
- Anything about real SEC data: the daily index layout, the data-set column names, whether FOOTNOTES.tsv exists, the real `aff10b5One` element name, the zone of the acceptance time. No network was allowed.
- The live `--score` path and `make_quote_provider` with the real watcher client and real Alpaca bars: needs keys, not used. Whether IEX bars cover delisted names, whether the first 1-minute bar is a fair first-trade time.
- Naive first-trade times under a different machine time zone.
- Whether `.pyc` files inside the watcher folder would be rewritten when they are stale (they were fresh).
- Any live advisory database for PyYAML (offline).
- QA N1 (status and type use later filings), K4 behavior over real months, K7 across real resets.
- Exact mutation-check run time.
- I did not write a `logs\agent-runs.md` row (the hard limit allowed one report file and the lessons line), so the ledger row for this job is still owed.

## Counts
Tests run: 190 (190 pass). Mutations run: 41 (41 killed). Probe cases written and run: about 300 across p1 to p6 (URL and redirect 23 plus 13 client cases, 9 UA cases, about 45 parser cases, about 110 logic and config cases, 20 dataset and file cases, 6 output cases), plus a 4,000-cluster fuzz (8,000 entries checked).
