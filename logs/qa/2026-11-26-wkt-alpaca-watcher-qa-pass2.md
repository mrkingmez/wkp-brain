# QA pass 2: wkt-alpaca-watcher, qa-director, 2026-11-26 (after the amendment build)

Scope: D:\WKP\software\wkt-alpaca-watcher\ and D:\WKP\Investing\watch-week\. Code, data, claims. No network call, no --smoke or --counted, no APCA value read, GO-COUNTED.flag not created (checked: absent). Scratch: D:\WKP\scratch\qa-check3\ (recount.py, suite.out).

## Verdict: PASS WITH NOTES. Nothing in the code blocks the flag. Four pre-flag items for the trading-director are listed at the end.

## What I ran
- Suite: `python -I -W ignore tests\test_watcher.py` -> Ran 88 tests in 324.628 s, OK, 88 lines "ok". Matches the software-director's 88 in 372 s.
- Demo: `python -I run.py --demo` -> 245 scans, 1225 evaluation lines, 1362 decision lines in total, main 26 opened and 26 closed, Zac ledger 22 opened and 22 closed. Config hash 6af53aca8c3217ce on every line and row. Note: the demo hash differs from the real config hash 836a57e348a11b8a because the demo swaps in 5 fictional symbols.
- Hand recount with my own script (recount.py) straight from demo-out\decisions.jsonl and paper-trades.csv, compared to scorecard.md:

| Item | My count | Scorecard | Match |
|---|---|---|---|
| Evaluation lines (TRADE / WATCH / SKIP) | 1225 (27 / 31 / 1167) | same | yes |
| Fresh evaluations | 763 (27 / 31 / 705) | same | yes |
| Fresh by regime | RANGE 225, UPTREND_VOLATILE 538 | same | yes |
| COUNTED decisions (70+, once per setup) | 39 (TRADE 26, WATCH 13), lowest counted score 70.0 | same | yes |
| Main: opened / closed / wins / avg R | 26 / 26 / 11 / 0.1998 | 26 / 26 / 11 / 0.200 | yes |
| Main gross / net | 2202.81 / 1540.11 | same | yes |
| Main max drawdown | 3695.24, 3.532 pct | same | yes |
| Main haircut 5 / 15 / 30 bps | 1540.11 / 214.69 / -1773.44 | same | yes |
| Main $60 view 5 / 15 / 30 | 0.9493 / 0.1684 / -1.0030 | same | yes |
| Zac: opened / closed / wins / avg R | 22 / 22 / 9 / 0.1415 | same | yes |
| Zac gross / net | 1377.98 / 821.48 | same | yes |
| Zac max drawdown | 3497.58, 3.369 pct | same | yes |
| Zac haircut 5 / 15 / 30 | 821.46 / -291.55 / -1961.08 | same | yes |
| Zac $60 view 5 / 15 / 30 | 0.5206 / -0.1399 / -1.1307 | same | yes |
| Regime split main | RANGE 9 trades, 5 wins, 2504.88; UPTREND_VOLATILE 17, 6, -964.77 | same | yes |
| Regime split Zac | RANGE 8, 4, 1320.74; UPTREND_VOLATILE 14, 5, -499.26 | same | yes |
| End-rule closes | main T0021 (490.85), T0026 (109.87); Zac Z0018 (487.27) | main 2, Zac 1 | yes |
| SPY-gauge baseline | 390.218 to 432.034 = 10.716 pct | same | yes |
| Day trades | main 2, Zac 6 | same | yes |

Other checks on the demo files: all decision ids unique; 0 of 48 closed trades mismatch on per-trade gross and net recomputed from raw prices (tolerance 0.011); no TRADE under 70; 0 Monday TRADE under 90; max notional/equity 0.2499; 0 of 22 Zac fills on the same ET date as the signal; every Zac entry is the 09:00 ET bar; step-up reads "OFF in config" on every fill; no UNKNOWN regime in the demo (so the UNKNOWN path is proven by unit tests only).

Observations on the scorecard itself (not errors):
- The Zac ledger shows 4 day trades in a rolling 5 trading days and 4 in one month against limits of 3, with 0 entries refused. That is S4 visible in the product. The scorecard reports it honestly.
- The baseline label says "SPY" in the demo although the demo gauge is DEMX (the scorecard is built from the real config). Cosmetic, demo only.
- The "versus baseline" lines compare ledger P and L as a percent of a book that is not fully invested with a buy-and-hold percent. Both numbers are shown, no excess is computed. Not misleading as worded, but it is not a like-for-like grade.
- The $60 view is size-bound by the 25 percent position cap on 26 of 26 trades, so at $60 the 0.5/1/2 risk tiers never bind. That is a true and useful fact, and the scorecard prints it.
- 13 of the 39 counted decisions are WATCH lines (Monday gate or no free slot), so the "50 decisions" bar is easier to reach than "20 trades". By the plan's own sentence this is correct.

## Smoke findings retrieved by the software-director (I read D:\WKP\Investing\watch-week\test\smoke-preflight.json, no new call)
| Claim | What the file shows | Status |
|---|---|---|
| Account equity 100000 | account_safe_values equity "100000", status ACTIVE, trading_blocked false, multiplier 2 | CONFIRMED |
| No pattern_day_trader or daytrade_count fields | account_fields_seen list has neither | CONFIRMED |
| Regular-hours closed bars 147 per symbol at 30-day lookback | min, median, max all 147 | CONFIRMED. 20 symbols x 147 = 2940 |
| Extended-hours bars dropped | extended_hours_bars_dropped 415. Raw hourly rows sum to 3355, 3355 minus 415 = 2940 = 20 x 147, so the arithmetic closes | CONFIRMED by arithmetic |
| IEX hourly bars start 08:00 ET and end 16:00 ET | the saved file only lists the AFTER-filter start times (09:00 to 15:00). The 08:00 and 16:00 starts are NOT in the file. The first smoke lines under hash b4979b9ab382ae1b show a bar_t of 2026-11-25T21:00Z (16:00 ET), which supports the after-hours part. 08:00 is not shown anywhere I read | PARTLY SHOWN. Repeat the smoke and record the raw start-hour set |
| Projected 126 at Mon 11/30 | projected_next_open_plus_3_days min/median/max 126 (145 at next open); both far above the 60-bar minimum. It excludes the Fri 11/27 half day, so it is conservative | CONFIRMED |
| Daily bars 275 per symbol | regime detail daily_bars 275 is the GAUGE (SPY) only. breadth_symbols 20 shows every symbol has at least 50 closed daily bars. The per-symbol min/median/max field is not in the file (the later smoke skipped the daily fetch because the regime for 11/26 was already cached in state.json from the earlier smoke) | SPY CONFIRMED, "per symbol" NOT shown |
| Test-run hash | smoke hash 836a57e348a11b8a equals the hash of the current config.yaml (I recomputed it). Last bar_t under that hash is 2026-11-25T20:00Z = 15:00 ET, so the session filter works on real data | CONFIRMED |

Regime on the real data: RANGE, SPY close 716.735 under its 50-day 757.93, 50-day above the 200-day 733.14, slope down, breadth 0.25, ATR percent 2.139 vs median 0.883. The tag follows the written rule (downtrend needs fast under slow). I did not check the SPY numbers against any outside source.

## Plan map: "Amendments after devils-advocate ruling"
Status words: BUILT, PARTLY, MISSING, TEXT (policy sentence, no code needed).

| # | Amendment | Code | Test | Status |
|---|---|---|---|---|
| 1 | Frozen config, hash on every log line, any change resets counts and is listed with its date | config.config_hash (parsed values), engine _common puts hash on every line incl. the closed-clock and data-failure lines in run.py, trade rows carry it, scorecard counts only the current hash, logio append_history writes config-history.jsonl with time | test_hash_is_stable_changes_with_a_value_and_is_on_every_line, test_config_change_restarts_counts_and_is_listed, loop test checks hash on every line | BUILT for config.yaml. PARTLY against the plan sentence "the score ... in ONE frozen file": indicator periods, the market-mood weights and all scoring code are in .py files and are NOT in the hash, and the folder is not in git (git ls-files returns nothing), so a code edit mid-week changes behavior with no reset and no record. See note A |
| 2 | A decision counts at score 70+, once per setup; skips logged not counted | engine step 3 (episodes), counting.min_score | test_decision_counts_once_per_setup_at_score_70_plus, test_demo_counted_only_70_plus_and_fewer_than_evaluations | BUILT. Caveats from the tester (Monday WATCH uses up the episode, a 75-69-75 dip counts twice, setup flip counts again) are real and not fixed. They inflate the count, they do not hide trades |
| 3 | 20 trades = plumbing, 50 = edge | scorecard "Plan checks" lines | test_go_live_lines_are_numbers_not_a_verdict | BUILT as text. Matches the plan |
| 4 | Fixed end rule, open trades closed at the final close | engine.close_out, run.py loop and late-start paths, config end_rule.last_day validated, ended resets on a new hash | test_close_out_closes_at_mark_cancels_pending_and_marks_ended, test_position_without_a_mark_is_left_open_and_logged_unknown, test_end_rule_applies_on_the_last_day_and_blocks_a_rerun, test_restart_after_close_on_last_day_applies_end_rule, test_ended_flag_resets_on_new_hash, test_end_rule_closed_open_trades_at_the_last_mark | BUILT. Closes at the last mark seen, not the official close print. Labeled in README and scorecard. Tester S1, S2, S3 closed and tested |
| 5 | Simulator account size stated, $60 view alongside | config paper_book.starting_equity, scorecard.sizing_view_equity, scorecard ledger_block | test_sixty_dollar_view_present_and_small | BUILT. The $60 view is sized per trade on its own and does not replay concurrency, cash across trades or the kill and weekly limits |
| 6 | Second ledger "Zac can act", next market open, go-live judged there | engine books(), _mirror_to_zac, _try_fill (name == zac) | test_main_fills_next_bar_zac_fills_next_session_open, test_demo_has_both_ledgers_with_distinct_ids_and_later_zac_entries | BUILT, with one real caveat: the "market open" it fills at is the open of the 09:00 ET bar (S5, below) |
| 7 | Gap rule: stop fills at the worse of stop and next open | engine _check_exit min(stop, open) | test_gap_down_fills_at_open_not_stop | BUILT |
| 8 | PDT counter | risk.pdt_block, engine day_trades, scorecard day-trade line | test_guard_rolling_and_monthly, test_same_day_exit_counts_a_day_trade_and_guard_cancels_a_fill | PARTLY. The COUNTER is built and honest. The GUARD only counts closed day trades, so it can overshoot (S4, shown in the demo: 4 in 5 days, limit 3, 0 refused). Rule text is itself unconfirmed |
| 9 | Missing bar or short history = UNKNOWN = FAIL, logged | scoring.hard_filters, bars_valid, evaluate, regime UNKNOWN, HOLD_UNKNOWN, risk.loss_limit_hit | TestUnknownIsFail (7 tests), test_unknown_is_fail_cases, test_position_without_a_mark... | BUILT |
| 10 | Haircut at 5, 15, 30; pass only if Zac ledger positive at 30 | config scorecard.haircut_views_bps and pass_haircut_bps, stats.net_at | test_haircut_view_matches_recompute_and_falls_with_slippage | BUILT. The line prints the number and "NOT positive", never a verdict |
| 11 | NOT VERIFIED items needing checks before live | n/a | n/a | TEXT. The README "Not verified" list carries them. Hourly depth on the free feed is now retrieved (147 and 126) |
| 12 | Robinhood vs Alpaca for live not decided | n/a | n/a | TEXT, not mine |

## Plan map: "Learning loop, regime detector and sizing rule"
| Plan sentence | Code | Test | Status |
|---|---|---|---|
| L1a Every trade row carries parts, score, regime, entry rule, exit rule, R and dollars, config hash | TRADE_COLUMNS (parts, score, setup, regime, reason, r_net, pnl_net, config_hash) | test_open_rows_cite_decision_lines, demo recount (all columns present) | BUILT |
| L1b Weekly self-grade vs SPY buy-and-hold from the same IEX bars, and vs the Zac ledger | scorecard baseline from scan marks; both ledgers side by side | test_baseline_uses_spy_marks_from_the_lines | PARTLY. The grade is one cumulative scorecard, not per week, and no excess-over-baseline figure is computed |
| L1c scorecard-baseline-<date>.md saved copy | none (grep finds no such file or code) | none | MISSING. Only matters before the first rule change, after 50 trades |
| L1d strategies-tried.md kept by trading-researcher | file exists at Investing\research\strategies-tried.md | n/a | TEXT, file present (content not reviewed) |
| L1e One change per run after 50 counted trades, change resets counts | hash reset enforces the reset; the 50-trade and one-rule limits are policy | hash tests | PARTLY by design (policy cannot be coded) |
| R1 Regime from daily SPY, 50 and 200 averages, slope, ATR percent vs 60-day median, breadth proxy of the watch list above its 50-day | regime.compute | test_all_five_tags, test_unknown_is_fail_cases | BUILT for daily SPY and breadth. The plan also says "and hourly SPY" and "the scanned symbol where useful": hourly and per-symbol are not used. PARTLY by wording, harmless |
| R2 Six tags, UNKNOWN is FAIL, no step-up | regime.TAGS, risk.step_up_check requires regime == UPTREND_CALM | test_every_condition_must_hold | BUILT |
| R3 Thresholds in config, frozen with the score | config regime block | test_new_sections_are_required_and_checked | BUILT |
| R4 Tag logged on every decision and trade | _common regime, TRADE_COLUMNS regime | test_regime_on_every_evaluation_line_and_split_table | BUILT. I counted 763 fresh lines all tagged, 0 untagged |
| R5 Tag changes behavior only through sizing | grep: regime is read only in step_up_check and logging | n/a | BUILT (code read) |
| S1 Base risk 0.5/1/2, 25 percent cap | risk.size_shares | test_risk_tiers, test_position_cap_25_percent_in_sizing | BUILT |
| S2 Step-up only if score 90+, UPTREND_CALM, 20+ counted trades in this config with Zac-ledger net-of-haircut expectancy positive, no kill in 5 trading days, fewer than 2 open | risk.step_up_check (hash-filtered nets at the 30 bps view) | test_every_condition_must_hold, test_hard_cap_per_trade_and_stepped_size | BUILT. Note N9: the same Zac-ledger expectancy gates BOTH ledgers. OFF in config |
| S3 Risk steps 2 to a hard 3 percent, 25 percent cap still applies | min(pct, max_loss_per_trade_pct), validate rejects risk_pct above 3 | test_hard_cap_per_trade_and_stepped_size | BUILT |
| S4 Max loss per trade 3 percent | caps the risk PERCENT at sizing. A gap through the stop can lose more, which the plan's gap rule already says | n/a | BUILT as sizing cap, not as a loss guarantee. Say so if anyone quotes it |
| S5 Weekly limit 6 percent, no new trades until next Monday | risk.weekly_limit_hit, engine WEEK_LIMIT, pending cancelled | test_weekly_loss_limit_blocks_new_trades | BUILT |
| S6 Daily kill -5, max 4 open | risk, engine | TestRules, TestMaxPositions | BUILT |
| S7 PDT counter blocks the 4th day trade in a rolling 5 days | risk.pdt_block | TestPdt | PARTLY (S4 below) |
| S8 $60 view reported next to the paper-account view | scorecard | test_sixty_dollar_view_present_and_small | BUILT |
| S9 Step-up OFF in the first counted week and until 20 trades | config enabled false | test_default_is_off_and_demo_never_steps_up | BUILT. Turning it on is a config change, so it resets the counts |

## Judgments on the items left open on purpose
| Item | My read | Blocks the flag? |
|---|---|---|
| S4 PDT guard counts only closed day trades, can overshoot | Real and visible in the demo (4 in 5 days, limit 3, 0 refused). The counter and scorecard line are honest. It matters when go-live is judged on the Zac ledger, because at $60 those extra day trades could not have happened. Fix idea: count open positions that are on track to close same day, or label the ledger "guard not enforced for entries opened the same day" in the scorecard | No for the plumbing week. Fix or label before anyone reads the Zac-ledger result as go-live evidence |
| S5 Both ledgers fill at the open of the 09:00 ET bar, which is the first IEX print after 09:00 (pre-open), not the 09:30 open | The config comment and the smoke arithmetic agree the 09:00 bar is kept. The Zac ledger and every first-hour time stop use that pre-open print. IEX pre-open prints are thin, so the fill can sit away from the real 09:30 price in either direction. The haircut at 30 bps may or may not cover it. I could not check real bars (no network) | Not a code blocker. A claim blocker: README line 48 says the first bar "holds only 9:30 to 10:00", which is false against config line 17 and the smoke. The scorecard assumption line also says "next session open" without the pre-open caveat. Correct both before the week and have the trading-director rule: accept, or fill the Zac ledger at the 10:00 bar open (hash changes, one rule at a time) |
| F8 whitelist ignores port and `;x=1` | Same two hosts, GET only, no redirects, keys never printed. No order path | No, note |
| F11 time stop counts dates present, not sessions | Documented in README limits. Affects the exit day by at most one on a missing-session day. Thanksgiving is before the week | No, note |
| F14 exits can read a forming bar | A touched stop or target on a partial bar is a real touch, so exits are not fantasy. The demo never exercises partial bars (view_at gives the forming bar only its open), so this path is proven by neither demo nor the live data. Friday's half day is the one chance to see it | No, note |
| F16 holiday start or double start: no lock file | README says start only on trading days. A double start would write two copies of every line and corrupt state.json. Operator risk, small. Fix idea: a lock file or a refusal if state.json was written in the last 2 minutes | No, but start exactly one copy |
| Torn paper-trades.csv row (tester N4) | A hard kill in the middle of one row write is the only trigger; decisions.jsonl has the newline guard, the CSV does not. Low probability, silent damage (a lost trade row). Fix idea: same leading-newline guard for the CSV and treat a row that fails to parse as absent | No, note |
| N9 step-up uses Zac-ledger expectancy for both ledgers | OFF by default and off for the first week. Harmless today. Decide before it is ever turned on | No |
| Marks have no staleness check | The end rule and equity use the last close however old. With 20 liquid symbols and a 4-day stale filter on scoring (not on marks) the risk is small this week. Fix idea: log the age of the mark when closing out | No, note |

## Earlier flag-holds from my first report (N1, N2, N4)
- N1 loop test: FIXED. TestLoopRegression drives run.main(--counted --loop) with a clock sequence True, fail, True, False and checks the sleeps [60, 30, 60], 4 clock calls, one daily fetch, the five output files, the hash on every line and no key text in any file or stdout.
- N2 F4 duplicates: FIXED. logio journals the scan inside state.json, appends, then clears. TestCrashSafety kills the write three ways and compares the result byte for byte with an uncrashed run (same decisions.jsonl, same paper-trades.csv, no duplicate or missing ids). The CSV torn-row case above is the leftover.
- N4 amendments not built: now BUILT apart from the partial items in the maps.
- N3 (demo daily note): FIXED, demo-out\daily-notes.md exists.

## Claims check: README and config.yaml against the code (earlier N5)
| Claim | Result |
|---|---|
| config.yaml header: rule and score thresholds live here, indicator periods fixed in code | TRUE and now said plainly |
| README: indicator periods fixed in code, rules come from wkt-locked-rules.md | TRUE |
| README: counted mode does not call account or positions, smoke does | TRUE (run.py: acct, pos only inside `if a.smoke`) |
| README: session window 9:30 to 16:00 from /v2/clock, locked 5 PM outside the session | TRUE, stated in README and config |
| README: log lines go into state.json first, never duplicated or lost | TRUE (logio, tested) |
| README: end rule closes at the last mark of the final scan, refuses to scan again | TRUE, tested |
| README: tests take about 5 minutes | TRUE (325 s here) |
| README step 0 pip install PyYAML, requirements.txt present | TRUE |
| README: first bar of the day "holds only 9:30 to 10:00" | FALSE. The kept bar starts 09:00 (config line 17, smoke). See S5 |
| README: whitelist of five paths, GET only, no redirects | TRUE (tester K3, K4, and the source grep test) |
| Hardcoded paths in run.py line 25, run_watcher.ps1 | STILL TRUE (F15 note). LOCAL-PATHS says never hardcode. Paths are correct for this machine |
| No em dashes in README, config, code, tests | TRUE (0 found) |
| Repo hygiene | software\wkt-alpaca-watcher is not in git (git ls-files empty), so there is no commit to point at. Tests leave 755 wkt-test folders in D:\WKP\scratch (F17) and rewrite demo-out inside the project folder, as the tool's own default |

## Findings new this pass
- A (note, hold-worthy). The frozen config covers config.yaml only. Indicator periods, mood weights and all scoring code are outside the hash and the folder is not under version control. A code edit during the week would change behavior silently and nothing on any line would say so. Fix idea: log a SHA-256 of the wkt\*.py files and run.py in config-history.jsonl and on the scorecard header, or commit the folder and print the commit hash. Cheap, and it makes the "frozen" claim true.
- B (note). README line 48 false claim (see S5).
- C (note). end_rule.last_day is 2026-12-04, a one-week end. The plan says the week extends until 20 trades and 50 decisions, "weeks, not one week". Extending the day later changes the hash and restarts the counts (by design, tested). So the last day must be chosen before Monday 9:30 ET, or the first week ends with the forced close and a restart. This is the trading-director's call, not code.
- D (note). Zac-ledger "day trades" at 4 in a rolling 5 days would not be possible at $60 under any current rule reading. Repeats S4.

## Not verified by me
Any live behavior: IEX hourly bar timing right after the hour, the 08:00 start hour, whether the 09:00 bar open is really a pre-open print, forming-bar exit behavior, rate limits, the Friday 11/27 half day through /v2/clock, a real multi-day loop. Alpaca response shapes beyond what the smoke file shows. The accuracy of the real SPY figures in the smoke file. PyYAML licence. Task Scheduler (nothing was searched for an auto-restart). Content of Investing\research\strategies-tried.md. FINRA and Robinhood day-trade rules. The tester's 95 attack cases were not re-run by me (I re-ran the suite and the demo recount).

## What blocks GO-COUNTED.flag
Safety bench: nothing. No key path, no order path, non-paper URL refused, gate holds.
Items I would clear first (all cheap, all the trading-director's or the software-director's, before Mon 11/30 9:30 ET):
1. Correct README line 48 and add the pre-open caveat to the scorecard assumption line (S5), then rule on S5: accept or move the Zac fill. A text edit does not change the config hash. A rule change does, so do it before the flag, not during the week.
2. Fix the "frozen" gap (note A): record a source hash or commit the folder, then freeze the code.
3. Choose end_rule.last_day for the real length of the run (note C) before the first counted scan.
4. One more read-only `--smoke` during market hours Friday 11/27 (half day, 09:30 to 13:00 ET), run by Zac or the trading-director, not by me: it is the only way to see a forming bar, the 08:00 and 09:00 start-hour set, and the real 09:00 bar open. Record the raw start-hour set this time. Not run by me, per order.
5. The flag is the trading-director's file. Zac's status confirmations (TRADING-2026-11-26-02 and -28, Investing is DORMANT) are not mine to judge and are still OPEN in DECISIONS.md.

Not blocking, but should be read before anyone judges go-live: S4 (PDT guard), the missing scorecard-baseline copy (needed before the first rule change), and the CSV torn-row guard.
