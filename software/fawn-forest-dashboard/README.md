# Fawn Forest Investments dashboard

A page on your own PC that shows how the paper trading test is going. Paper only. It only reads files the watcher already wrote. It has no buttons that trade, no keys, and it never talks to the internet.

## Start it (the easy way)
1. Open File Explorer and go to `D:\WKP\software\fawn-forest-dashboard`.
2. Double-click `start-dashboard.bat`.
3. A black window opens and your browser opens the page. If the browser does not open, type `localhost:8790` in the address bar.
4. Leave the black window open while you look. Close it (or press Ctrl+C in it) to stop the dashboard.

## Start it (from PowerShell)
1. Open PowerShell.
2. Type: `cd D:\WKP\software\fawn-forest-dashboard` and press Enter.
3. Type: `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe -I server.py` and press Enter.
4. Open `http://localhost:8790` in your browser.

## On your phone
It only answers on this PC (localhost). It is not on the network on purpose. To see it on your phone you would need a private link such as Tailscale, which is a separate setup and a separate decision. Not done.

## Reading the page
- Yellow stripe at the top with DEMO DATA: the numbers are made up by the watcher's demo mode. They are not results and not real money.
- PAPER ONLY badge: always there. No real order is ever sent from anywhere here.
- JARVIS / ARES switch (top right, remembered by your browser): JARVIS is the calm blue look. ARES is the red and amber command-post look with different label words (for example MAIN LEDGER becomes MAIN ROSTER). The numbers are identical in both. The PAPER ONLY badge and the DEMO DATA banner stay in both looks.
- AUTO / LIVE / DEMO switch (top right): AUTO shows live numbers when the real watch-week log exists, otherwise the demo. LIVE shows only real files. DEMO always shows the fictional demo.
- Green is up or good. Red is down or bad. Amber is stale, low sample, or a warning.
- LOW SAMPLE means fewer than 50 counted trades. 20 means the plumbing works. 50 or more is needed before anyone calls it an edge.
- NOT AVAILABLE with a file path means that file is not on disk yet. The page never fills a gap with a guess.
- STALE strip: the last scan is old (over 5 minutes while the market was open, or over 4 days otherwise).

## What each card reads
| Card | File it reads (never writes) |
|---|---|
| Four-week test, ledgers, chart, haircut, trades, regime, heat map, freshness | `D:\WKP\Investing\watch-week\` : `decisions.jsonl`, `paper-trades.csv`, `state.json`, `config-history.jsonl` (demo mode reads the watcher's `demo-out\`). End date comes from `D:\WKP\software\wkt-alpaca-watcher\config.yaml` |
| GO-COUNTED flag | `D:\WKP\Investing\watch-week\GO-COUNTED.flag` (exists or not) |
| SPY baseline | the `spy_mark` on each scan in `decisions.jsonl` |
| Go-live checklist | `data\go-live-checklist.json` in this folder. The trading-director edits states by hand (PASS, FAIL, PENDING). It shows 0 of 7 today |
| Insider buys | `D:\WKP\Investing\watch-week\insider\clusters.jsonl` (demo mode: the insider scanner's `demo-out\`) |
| Crypto group | `D:\WKP\Investing\watch-week\crypto\paper-trades.csv`. Not there, so it says NOT BUILT |

The watcher's files may change shape. The page reads them each time it refreshes (every 30 seconds) and shows NOT AVAILABLE for anything it cannot find instead of crashing.

## Tests
1. Open PowerShell. 2. `cd D:\WKP\software\fawn-forest-dashboard` 3. `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe -I tests\test_dashboard.py`. Takes about a second. It uses temporary folders under `D:\WKP\scratch\ffdash-tests` and does not touch the real files.

## Safety design
- Binds to 127.0.0.1 only. Rejects any other Host name.
- GET only. POST, PUT, DELETE return 405.
- Serves five fixed files (page, two style files, script) and two JSON routes. No folder browsing.
- Reads no environment variables and no keys. The watcher's key names appear nowhere in this code.
- No outside network calls, no fonts or scripts from the internet. Page text is inserted as plain text only.
- Checklist and haircut numbers shown come from files. Nothing is computed from a guess.

## Known limits (honest)
- The equity curve is realized profit and loss at each closed trade. Open positions are not marked to market.
- The SPY line uses the SPY price marked on each scan, rebased to the starting book.
- Day count counts distinct trading dates with a scan while the market was open. The planned day total is only shown in live mode.
- The watcher's demo run is fictional (January to March 2026 dates). The demo shows the watcher's finished demo, so its "ended" tag shows.
- Heat map: most scans find no setup, so most symbols show a dash instead of a score. That is true to the log.
- Insider and crypto cards are stubs until their tools write output.
- Checked in headless Edge at desktop width in both looks. Phone width was only a cropped headless screenshot, so a real phone check is still owed (and the phone cannot reach the page yet, see On your phone).
- In DEMO view the End date shown comes from the real watcher config, so it differs from the demo run's own dates.
- Restyle: all colors, edges and fonts live in `static\themes.css`. Label words per look are in the WORDS table at the top of `static\app.js`.
- Reference look: drop screenshots in `D:\WKP\Investing\dashboard\reference\` and ask for a restyle.

## Cost to run
$0. Python standard library only. Nothing to install.
