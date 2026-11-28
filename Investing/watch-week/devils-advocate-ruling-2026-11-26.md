# Devils-advocate ruling: paper watch week plan (2026-11-26)

Requested by trading-director. Read-only review. Sources read, and nothing else:
- `D:\WKP\Investing\watch-week\WATCH-WEEK-PLAN.md` (the plan)
- `D:\WKP\Investing\wkt-locked-rules.md` (locked rules, 2026-10-19)
- `D:\WKP\Investing\CLAUDE.md` (venture file)
- `D:\WKP\Investing\watch-week\README.md`

Every claim below points back to one of those files. Where I say NOT VERIFIED, I could not check it from these files and it needs a lookup before anyone relies on it. Arithmetic examples are labeled as examples, not retrieved figures.

## VERDICT: GO WITH CHANGES

Paper only, no orders, keys read by name, so the downside of running it is close to zero. The danger is not the watch week. The danger is that its scorecard, as currently defined, could tick go-live checklist item 1 while proving nothing about what Zac would actually earn on Robinhood. Fix the items below before Monday 11/30 is counted as Day 1.

## THE ONE THING

**The score is never defined.** Every rule in force keys off a 0 to 100 score (no trade under 70, risk tiers at 70, 80, 90, Monday only at 90+). The plan logs "score parts" but no file I read says what the parts are, how they are weighted, or what stock universe is scanned. `Investing\CLAUDE.md` still has "[FILL IN, specific technical indicators/thresholds for oversold and breakout]". A watch week run against an undefined, editable score is a tuning session, not a test. Any later win rate is uninterpretable because nobody can show the score on Friday is the score from Monday.

Fix: before 9:30 ET Monday, write the score definition (components, weights, thresholds), the stock universe, and every filter into one file, record its git commit hash in `decisions.jsonl` on every line, and state the rule that any change to it resets the trade and decision counts to zero.

## HOLES

### 1. "50 decisions" is met in the first minute
Plan, Scoring method step 1: one line per symbol per scan, scans every minute, 9:30 to 4:00. With any universe above one symbol, 50 lines arrive almost immediately. Checklist item 1 then rests entirely on the 20 trades.
Fix: define a counted decision as a symbol crossing score 70 or higher (a TRADE or a SKIP-for-a-rule-reason at 70+), deduplicated per symbol per setup. Keep the raw per-minute log, but do not count it.

### 2. Twenty trades in one week is not realistic, and 20 is not enough anyway
The plan already says far fewer than 20 is likely. The throughput math makes it worse. Max 4 open positions and a 5-day stock time stop mean that if trades run to the time stop, the ceiling is about 4 new trades per week (example arithmetic, not a forecast). Monday only allows 90+. Friday 11/27 is a half day and not counted. Christmas week falls inside any extension. Realistic time to 20 trades is several weeks.
Bigger issue: plan step 5 says no rule changes until 50 to 100 trades, because that is the smallest sample worth judging. Checklist item 1 lets Zac go live at 20. The plan is willing to put real money behind a sample it says is too small to change a rule on.
Fix: label 20 trades as "plumbing proven" only. Any claim that the system has an edge needs at least 50 closed trades, matching step 5. State that in the scorecard header.

### 3. Optional stopping
Plan, Fri 12/4: the week "extends day by day until at least 50 decisions and 20 paper trades, or Zac ends it." An open-ended run that can be stopped when the numbers look good inflates the result. Trades still open at the end (up to 5 days) are also not addressed.
Fix: set the end rule in advance (the day the count is reached, with all open trades marked to market at that close and counted). No early end because results look good. If Zac ends it early, the scorecard says so on line one.

### 4. Sizing equity is not stated, and at $60 the risk ladder collapses
The plan does not say what account size the simulator sizes against. `Investing\CLAUDE.md` says the real account is about $60 (plan item 7 notes this was not retrieved today). The Alpaca paper account's own balance is not shown in the plan.
At $60 (example arithmetic): 25 percent cap = $15 per position. Risk at 0.5 percent = $0.30. With a 2 x ATR(1h) stop that is around 2 percent of price, 0.5 percent risk already sizes to the full 25 percent cap, so the 1 percent and 2 percent tiers are capped and identical. In that case the score tiers change nothing about size. Every position also needs fractional shares.
Fix: size the paper ledger against Zac's real account figure (use $60 until he writes his own number for checklist item 7), use fractional quantities, and log per trade which limit set the size (risk or the 25 percent cap). If paper sizes against a large paper balance, its results do not transfer.

### 5. The plan fills trades Zac cannot take (biggest Robinhood versus Alpaca mismatch)
Paper fills at the next bar open after a 1-minute signal (step 2). Real execution is manual by Zac on Robinhood (plan, Zac's decision; `Investing\CLAUDE.md`: Robinhood does not support programmatic orders for retail). Zac works a full-time 8 to 5 job (ME.md, loaded in context). A 10:42 AM signal filled at 10:43 in paper may be filled by Zac at lunch, after work, or never. The locked rules' Twilio YES/NO approval is for the live phase and is not built. The kill switch is supposed to "text Zac" (locked rules), with nothing built to send it.
Fix: keep two ledgers from the same signals. Ledger A is the plan as written (next bar open). Ledger B fills only at times Zac can act. Queue a decision for Zac to name those windows; until he does, default Ledger B to the next session open. Go-live checks use Ledger B. If A is positive and B is not, the system has no edge Zac can capture.

### 6. Stops are modeled as if Zac and Robinhood can hold them
Paper exits at the stop on IEX prints. Live, the stop is either a broker order or Zac watching at work. Whether Robinhood accepts stop orders on fractional share positions is NOT VERIFIED from these files. If it does not, every live stop is a mental stop during work hours, and Ledger B needs stop exits delayed to his windows too.
Also: the plan does not say how a stop fills when price gaps through it.
Fix: stop exits fill at the worse of the stop price and the next bar open. Before go-live, a research desk verifies Robinhood fractional stop-order support from Robinhood's own pages.

### 7. Pattern day trader count is missing
`Investing\CLAUDE.md` says the PDT rule applies to this account and limits it to 3 day trades. With 1-minute checks and ATR stops, a trade can open and stop out the same day. The plan has no same-day round-trip counter. Current PDT rule details are NOT VERIFIED from these files.
Fix: the paper ledger counts same-day round trips in a rolling 5 trading days and blocks the entry that would breach the limit, logged as SKIP with reason PDT. Have the rule's current wording checked before go-live.

### 8. IEX-only data makes volume filters and fills unreliable
Plan, Facts: SIP is denied (403), the feed is IEX, volume is IEX-only and thinner, some prices will differ. Effects the plan does not handle:
- Any volume filter run on IEX volume undercounts the full tape. A threshold tuned on IEX will not mean the same thing on Robinhood's tape, and one borrowed from consolidated volume will reject most names.
- "Next bar open" may not exist for a thin name on IEX in a given minute. UNKNOWN counts as FAIL for entries (good), but the plan does not say what an exit does when no bar prints.
- Stops can trigger or miss on IEX prints that differ from the consolidated price.
Fix: state in the frozen spec that volume filters are on IEX volume and name the threshold. Missing next bar on entry means no fill, logged. Missing bar on exit means fill at the first bar that prints, at its open. Limit the universe to names that print an IEX bar in most minutes. Historical bar depth is listed as NOT VERIFIED in the plan, so ATR(1h) needs that check before Monday, or ATR goes UNKNOWN and every trade fails.

### 9. The haircut is a placeholder with one value
Step 2: 5 bps each side, labeled a placeholder. Checklist item 3 asks whether results stay positive after the haircut. A single optimistic value makes that check easy to pass.
Fix: report net P and L at three levels, 5, 15 and 30 bps each side (my proposed stress levels, not measured figures). Item 3 passes only if Ledger B is still positive at 30 bps. Keep the regulatory-fee config value and say where its number came from.

### 10. The files disagree on the live broker for stocks
`wkt-locked-rules.md` Phase 4: stocks on Alpaca once open and funded. `Investing\CLAUDE.md`: stocks stay on Robinhood until the account crosses $25k. Plan: real execution on Robinhood unchanged. A paper week validated on Alpaca data against a Robinhood future, with a locked rule pointing at Alpaca, is the kind of drift that lets someone say "it passed" about the wrong setup.
Fix: queue one decision for Zac on which broker runs live stocks, and update whichever file loses. The plan's own TRADING-2026-11-26-01 closes the paper and data question only.

### 11. Same agents build, run, and grade
The plan routes the build through software-director and grading through qa-claims, qa-auditor and devils-advocate, which helps. The remaining risk is scoring the week, finding the score weak, tweaking it, and continuing the same count.
Fix: covered by the freeze and reset rule in THE ONE THING. In addition, the scorecard lists every spec change by commit hash with its date.

### 12. Status precondition
The plan correctly queues TRADING-2026-11-26-02: Investing is DORMANT and the watch week sits outside that. Monday should not be counted until Zac answers, or trading-director records that it is running on his standing word.

## WHAT IS WORKING (keep it)
- Paper only, no order endpoints, paper URL assert, keys read by name only, paper orders to Alpaca default NO.
- The IEX versus SIP probe is documented with request IDs, and NOT VERIFIED is written where it applies. That is the honest standard.
- UNKNOWN data counts as FAIL.
- Skips are logged with reasons, not just trades.
- "If paper looks too good, the simulator is suspected first."
- No rule change until 50 to 100 trades, one rule at a time.
- A no-trade week is allowed and reported honestly.
- The go-live checklist is marked FAIL across the board today instead of being dressed up.
- Item 7 (Zac's own words on what he can afford to lose) is on the list. Keep it as a hard gate.

## REQUIRED CHANGES BEFORE MONDAY 11/30 COUNTS
1. Freeze score definition, universe and filters in one file. Commit hash on every log line. Any change resets the counts.
2. Count a decision only at score 70+, deduplicated per setup.
3. Size against Zac's real account figure, fractional, and log which limit set the size.
4. Run Ledger B (fills at times Zac can act, default next session open) beside Ledger A. Go-live uses Ledger B.
5. Stop gap rule, missing-bar exit rule, PDT same-day counter.
6. Haircut reported at 5, 15 and 30 bps. Item 3 passes only at 30 bps on Ledger B.
7. Fixed end rule, open trades marked to market. 20 trades = plumbing, 50+ = edge claim.
8. Check historical 1-hour bar depth on the free feed before Monday.

## BEFORE GO-LIVE (not blocking the watch week)
9. Zac rules on the live stock broker (locked rules versus Investing\CLAUDE.md).
10. Verify Robinhood fractional stop-order support and current PDT wording from primary sources.
11. Zac answers TRADING-2026-11-26-02 (status) and writes item 7.

Ruling stands as GO WITH CHANGES. The director or Zac decides.
