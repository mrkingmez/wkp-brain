# wkt-alpaca-watcher tester pass 4 (changes 6, 7, 8), 2026-11-27

Verdict: PASS WITH NOTES. Report only, product files not edited, no network, no --smoke, no key printed, GO-COUNTED.flag not created (none exists outside scratch test dirs), no push. Scratch: D:\WKP\scratch\tester-pass4\ (copy, copy2, adv4.py, adv5.py, keys.py).

## Results
| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Full suite on scratch copy, python -I tests\test_watcher.py | PASS | Ran 112 tests in 452.173s, OK, 0 FAIL/ERROR lines (suite.txt) |
| 2a | F2 Zac expiry boundaries | PASS | Mon signal: fill +1 and +2 weekdays fill, +3 and later cancelled. Fri signal: Mon (1) and Tue (2) fill, Wed (3) cancelled. Scan-level with no bars at all: Mon sig, Wed scan keeps, Thu scan cancels; Fri sig keeps over Sat and Mon 09:05 scan, cancels Wed. None-bar garbage plus expired signal: cancels, no crash. CANCEL reason text: "signal expired: 5 weekdays since the signal date 2026-01-05, limit 2, no fill" |
| 2b | F3 bad entry_bar_t | PASS | missing, None, garbage, empty, int, list, dict, True, date-only string, in main and Zac: no crash, fill proceeds, HOLD_UNKNOWN logged (seen in keys.py) |
| 2c | F1 backfill | PASS | 4 same-day pending, scan Wed 09:05 after Monday fills: 3 fill, 4th refused, main and Zac. Month limit uses the fill date (fill Jan 30, scan Feb 2, 3 Jan trades: refused; Jan 20 case refused). enforce false: 5 of 5 fill |
| 2d | Log and file formats | PASS | New CANCEL and HOLD_UNKNOWN lines use keys that are a subset of the baseline decision keys (no new-only keys). CANCEL keyset equals baseline. HOLD_UNKNOWN reuses the pre-existing _log call shape. Demo rerun in copy2: decisions.jsonl, paper-trades.csv, state.json identical to baseline demo-out after masking 16-hex hashes; paper-trades.csv header identical; scorecard 9 headings identical (only the two timestamp lines differ); state.json key set identical (ended_hash exists in both engines, set at run end); 1364 decision lines, 40 counted, 4 CANCEL (1 gap, 3 end rule), 0 expired, 0 PDT, 0 HOLD_UNKNOWN. Demo trades match the CHANGES numbers (26/26 main, 22/22 Zac) |
| 3 | Security greps | PASS | No key-like strings (PK/AK/CK ids, APCA_*=value) in py, yaml, md, ps1, txt. No order endpoints or POST/PATCH/DELETE in wkt or run.py. alpaca.py and guards.py byte-identical to the pre-change copy. ALLOWED stays GET-only: /v2/account, /v2/positions, /v2/clock (paper host), /v2/stocks/bars and /bars/latest (data host). assert_paper_url still used in the client |
| 4 | CODE-SHA256.txt and config hash | PASS | All 20 listed files match, none missing, only unlisted file is CODE-SHA256.txt itself (by design). Config hash recomputed from config.yaml: b559c847b5717f4a. Only config.py, engine.py and config.yaml (one line) differ from the pre-change copy; the other 11 wkt files are identical |
| 5 | New crash paths | NOTE | See N1 |

## Notes (none block the counted run)
- N1 (low) New crash path, needs a hand-damaged state file. `_expired` reads `sig["signal_bar_t"]` with no guard. A Zac pending signal with a None, garbage, empty, int or list `signal_bar_t` now raises (AttributeError or ValueError) from scan even when the symbol has NO bars; the pre-change code only crashed when bars existed (adv5.py, base vs new). The engine always writes this field, so only a damaged state.json triggers it. Fix idea: try/except in `_expired`, log HOLD_UNKNOWN, fail safe. Main ledger unaffected by `_expired` (returns early), and expiry on main is not applied by design (flagged in the change doc).
- N2 (known, stated by the developer) `_check_exit` still raises KeyError on a missing `entry_bar_t` (reproduced: a scan with such a position crashes). Same hand-damaged-state condition.
- N3 (low) Holidays are not modeled. Wed signal before a Thursday holiday then Friday fill counts as 2 (fills); a Wed signal across a long holiday gap (Christmas Thursday and Friday closed, Monday fill = 3) is cancelled. That errs conservative. Weekend bar in fake data fills on Saturday only because the test feeds Saturday bars; real feed has none.
- N4 (very low) A date-only naive `entry_bar_t` string parses and is dated in the machine's local time zone rather than ET. Not a real write path.
- N5 The main ledger has no date expiry (only the 1 ATR gap cancel). Stated and queued by the developer, unchanged.
- N6 The change doc says the suite takes up to 25 minutes; this run took 7.5 minutes (452 s).

## Not verified
- Live behaviour with real Alpaca data, holidays, DST changes around fill dates. No network, no --smoke.
- `run.py --loop` end to end after these changes (only scan, _try_fill, demo exercised).
- Windows Task Scheduler or run_watcher.ps1.
- Whether the Zac ledger conclusions (3 in 5 days, 3 a month) match the real broker PDT rule: rule text is not confirmed (per code comment).
- I did not run the demo in the product folder (by order); the product's own demo-out was only read, and it matches my fresh scratch run.
