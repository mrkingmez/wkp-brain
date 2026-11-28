# Read-only smoke checklist, Friday 2026-11-27 (half day: market 09:30 to 13:00 ET)

Status: the smoke was RUN on 2026-11-27 at about 11:14 ET by software-director (market open, so the forming bar was in play). This list is kept for the next market-hours smoke. Paper only, read-only GETs, no orders, no GO-COUNTED.flag.

## What to run (PowerShell, nothing else)
1. Open PowerShell. Type: `cd D:\WKP\software\wkt-alpaca-watcher` and press Enter.
2. Type: `powershell -File run_watcher.ps1 --smoke` and press Enter. (The script copies the three Alpaca variables from your User scope into the process and never prints them.)
3. Run it between 09:30 and 13:00 ET on a half day (09:30 and 16:00 on a normal day). Outside those hours the scan still runs in smoke mode but cannot show the forming bar.

## What PASS looks like
- Line starts `smoke scan:` with `calls: {'account': [200, ...], 'positions': [200, ...]}` (both 200).
- `account_safe_values` shows status ACTIVE, trading_blocked false, currency USD, equity 100000.
- `positions_count: 0`.
- `info` shows: `extended_hours_bars_dropped` above 0, `gauge_bar_start_times_et` between 09:00 and the last session hour only (no 08:00, no 16:00), `symbols_under_min_bars_now: []`, `projected_next_open_symbols_under_min_bars: []`.
- `regime` shows a date of today and a tag (UPTREND/RANGE/DOWNTREND).
- No error words: `blocked`, `network error`, `http 4xx or 5xx`, `FAIL`.
- The forming bar: the last gauge bar starts in the current hour. It is NOT scored (only bars whose hour has finished are scored). After 13:00 on a half day the 12:00 bar is the last full bar.

## Where the log lands
- `D:\WKP\Investing\watch-week\test\` (the smoke test folder, not the counted week): `smoke-preflight.json`, `decisions.jsonl`, `state.json`.
- The counted week folder `D:\WKP\Investing\watch-week\` is not touched by --smoke.

## Fail means
- Any 401 or 403: keys are wrong or missing in the User environment. Do not paste them anywhere. Tell trading-director.
- Any HTTP 5xx or `network error`: retry once in a minute, then tell trading-director.
- Never create GO-COUNTED.flag. That is Zac's own yes on TRADING-2026-11-26-02.
