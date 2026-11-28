# Read-only smoke checklist, Monday 2026-11-30, BEFORE the open (first counted day)

Written 2026-11-27 by software-director. Paper only, read-only GETs, no orders, no GO-COUNTED.flag created by this list. Run it AFTER trading-director has the tester and QA verdicts on changes 6 to 8 and BEFORE GO-COUNTED.flag is created, so a surprise does not cost a restart of the counts.

## When
- Monday 2026-11-30, between 08:30 and 09:20 ET (the market opens at 09:30 ET; a normal full day, closes 16:00 ET). Not later than 09:20 so the counted loop can start at 09:25.
- Why before the open: nothing in the regular session is forming yet, so the smoke shows only finished bars from Friday 11-27 (a half day, last regular bar starts 12:00 ET). The 08:00 pre-market hourly bar may be forming; it must be dropped.

## What to run (PowerShell, nothing else)
1. Open PowerShell.
2. Type `cd D:\WKP\software\wkt-alpaca-watcher` and press Enter.
3. Type `powershell -File run_watcher.ps1 --smoke` and press Enter. The script copies the three Alpaca variables from your User scope into the process and never prints them. Do not paste a key anywhere.

## What PASS looks like
- Line starts `smoke scan:` and `calls:` shows `account` and `positions` both 200.
- `account_safe_values`: status ACTIVE, trading_blocked false, currency USD, equity 100000 (or the same value as 2026-11-27: 100000).
- `positions_count: 0`.
- `info`: `extended_hours_bars_dropped` above 0, `gauge_bar_start_times_et` only hours 09 to 15 (no 08, no 16), `symbols_under_min_bars_now: []`, `projected_next_open_symbols_under_min_bars: []`.
- `regime` shows a tag. Before 09:30 the regime may still carry Friday's date or be computed fresh for Monday; either is fine, a tag of UNKNOWN is NOT a pass for the regime line (tell trading-director).
- The last scored gauge bar is Friday 2026-11-27 12:00 ET (the half-day close bar) or earlier. No Monday bar is scored before 10:00 ET.
- Clock: the smoke reads `/v2/clock`. Before 09:30 expect `clock_open` false and the next open at 09:30 ET Monday. If the clock says open before 09:30, stop and tell trading-director.
- No error words: `blocked`, `network error`, `http 4xx or 5xx`, `FAIL`.
- No new line in `D:\WKP\Investing\watch-week\decisions.jsonl` (the counted folder). The smoke writes only to `D:\WKP\Investing\watch-week\test\`.

## Check the code is the tested code (read-only, 2 minutes)
1. In PowerShell run: `cd D:\WKP\software\wkt-alpaca-watcher` then `Get-ChildItem -Recurse -File | Where-Object { $_.FullName -notmatch '__pycache__|demo-out|\\logs\\' -and $_.Name -ne 'CODE-SHA256.txt' } | Get-FileHash -Algorithm SHA256 | Select-Object Hash, Path`.
2. Compare EVERY line with `CODE-SHA256.txt` (20 files, including wkt\alpaca.py and wkt\guards.py, the safety files). Get-FileHash prints UPPERCASE hex; compare ignoring case. Any mismatch means someone edited the code after the verdicts: do not start the counted run, tell trading-director.
3. The console does not print the config hash. Open `D:\WKP\Investing\watch-week\test\smoke-preflight.json` and read `config_hash`: expected `b559c847b5717f4a` (changes 6 to 8).
4. The last scored gauge bar date is in `info.gauge_last_bar_utc` (expect `2026-11-27T17:00:00Z`), not in `gauge_bar_start_times_et`, which lists times of day only.

## Fail means
- Any 401 or 403: keys are wrong or missing in the User environment. Tell trading-director. Never paste a key.
- Any HTTP 5xx or `network error`: wait a minute, run once more, then tell trading-director.
- Never create GO-COUNTED.flag from this list. That file is Zac's own yes (TRADING-2026-11-26-02).

## NOT verified by me
- The exact smoke output on a Monday pre-open (only Friday-midday and Friday-12:30 runs exist). The expectations above are reasoned from the 2026-11-27 runs.
