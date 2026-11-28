# Devils-advocate ruling: WKT Crypto Watcher design (paper-only build)

Date: 2026-11-26. For: trading-director (FAWN FOREST INVESTMENTS).
Question ruled: may the crypto watcher continue to a PAPER-ONLY build?
Files read in full: `software\wkt-crypto-watcher\DESIGN.md`, `Investing\research\crypto-api-and-data-sources-2026-11-26.md`, `Investing\research\ai-bot-claims-check-2026-11-26.md`, `Investing\wkt-locked-rules.md`, `Investing\watch-week\WATCH-WEEK-PLAN.md`. Also read `Investing\CLAUDE.md` (loaded with the folder).
Nothing below was measured live. Every number is traced to one of those files or is arithmetic on them, and is labeled.
Paper only. Not financial advice.

---

## VERDICT: GO WITH CHANGES (paper-only build)

The safety design is strong: one GET-only network gate, an allowlist with no order or account path, no key in Phase A, startup asserts that refuse to run with a write path, UNKNOWN counts as FAIL, frozen config with hashes. Building it costs $0 and cannot touch money. That part earns a GO.

What does not earn a GO is the scoring. As written, the watcher can print "PASS" on a cost level lower than every cost Robinhood actually documents. A false PASS on a $60 account is the single most likely way this project pushes Zac toward real money early. Fix the pass line before step 2, and the build is fine.

Build steps 0 to 10 may proceed after changes 1 to 4 below are written into the design. The counted run (step 12) also needs changes 5 to 10.

---

## THE ONE THING

**The go-live pass line (Zac ledger positive at 30 bps each side, about 0.6 percent round trip) sits below every documented Robinhood cost.**

Traced:
- Research file, Fees row: exchange routing at $0 to $10K 30-day volume is 0.95 percent standard, 0.50 percent reduced. A $60 account never leaves that tier.
- Research file, API fee wrinkle row: "Market and stop orders always pay standard."
- Research file, Fees row: "Limit orders always use exchange routing." So any resting limit sell (Zac ledger variant B) pays an exchange fee.
- Market-maker routing (default for market orders) shows no fee line; the cost is the spread, and the spread is NOT RETRIEVED. Third parties claim about 2 percent round trip (unverified).
- DESIGN.md 4.2 sets `fee_bps_each_side` default 0 and runs 0.95 percent only as scenario F95.

So the only cost figures on file are about 1.0 to 1.9 percent round trip (fee routes) or an unknown spread (market-maker route, third-party claim near 2 percent). The pass line is 0.6 percent. A PASS at 30 bps proves nothing about Robinhood.

Why it is the weakest link: DESIGN.md section 1 itself says a 2 x ATR stop on hourly bars is "only about 1 percent away" (the design's estimate, not measured by me). On that figure, illustrative arithmetic:

| Round-trip cost | Cost in R (stop 1 percent) | Net win at 2.5R target | Net loss at stop | Break-even win rate |
|---|---|---|---|---|
| 0.6 percent (30 bps each side, current pass line) | 0.6R | +1.9R | -1.6R | about 46 percent |
| 1.0 percent (0.50 reduced fee each side) | 1.0R | +1.5R | -2.0R | about 57 percent |
| 1.9 percent (F95, 0.95 standard each side) | 1.9R | +0.6R | -2.9R | about 83 percent |

At the documented standard fee, the locked rule set needs to win about 5 of every 6 trades just to break even. The current pass line hides that.

**Fix.** Before build step 2:
1. The Zac ledger pass line becomes the F95 scenario (95 bps each side plus haircut), not 30 bps. If Zac later shows in the app that his real route is cheaper (change 4), the pass line moves DOWN to the measured figure through a logged config change. It never starts optimistic.
2. The `max_cost_to_risk` filter (DESIGN.md 6.5) is computed at the pass-line cost, not at 30 bps. Today it lets through trades where the documented cost is about 1.6R.
3. The scorecard prints the F95 row first and the 30 bps row as "optimistic, not a Robinhood cost".

Expected result: the filter will SKIP most hourly setups, and the ledger may show no edge. That is the honest answer the design itself says is acceptable (section 1, "Biggest honest worry"). If it happens, the finding for Zac is "the locked 1-hour 2 x ATR stop does not fit Robinhood costs at $60", which is a rules question for Zac, not something to tune away.

---

## HOLES

### 1. Variant B exits carry no fee (defect)
DESIGN.md 8.2 variant B exits a touched target at the target on a resting limit sell. Per the research file, limit orders always use exchange routing, so that exit pays at least 0.50 percent (reduced, if it rests as maker) or 0.95 percent. The design applies only the haircut.
**Fix:** variant B target exits add the exchange fee at the standard tier unless Zac's app check (change 4) shows reduced. Test O gets a variant B case.

### 2. Proxy prices shift the triggers, not just the fills
Coinbase BTC spread tested at 0.01 USD (data-sourcing, carried in DESIGN.md 3.1), so the Coinbase ask is effectively the mid. Robinhood quotes are spread-inclusive (research file, spec mirror). A Robinhood bid sits below the Coinbase bid, so in reality a stop triggers sooner and a target later than the Coinbase feed shows. DESIGN.md 4.3 tests triggers on RAW Coinbase prices and applies the haircut only to the fill. That understates stop-outs and overstates target hits.
**Fix:** on the Zac ledger only, trigger tests use the haircut-adjusted bid (stop hit when bid times (1 minus h) is at or below the stop; target hit when bid times (1 minus h) is at or above the target). Keep the raw-trigger main ledger for replay exactness. Kraken cross-check does not help here; it catches a bad feed, not Robinhood's markup.

### 3. The main ledger at 15 bps answers a question nobody can act on
Main ledger fills 24/7 at Coinbase ask plus 15 bps. Zac cannot trade 24/7 and cannot get Coinbase prices on Robinhood. Its numbers will be the best-looking numbers in the scorecard.
**Fix:** keep it as a plumbing check, but the scorecard never shows main-ledger P and L above the Zac-ledger F95 row, and labels it "not tradeable by Zac".

### 4. The cheapest decisive fact is a five-minute app check, and it is not first
Q9 (DESIGN.md 13.4) has Zac open the Robinhood crypto order screen. That one look answers fee route, stop support, resting limit support, minimum order and increments, with no key and no order. It is listed as a blocker but sits alongside 19 other questions.
**Fix:** Q9 goes first in the decision list, and it adds three items:
- Preview a small BTC buy (no order placed) and write down the shown price next to the Coinbase ticker at the same minute, three times on different days. That is a rough spread markup without any key or Phase B.
- Write down whether the default order type in the app is market (market-maker route, spread cost) or limit (exchange route, fee).
- Read the list of coins the app offers. The universe becomes the overlap of Robinhood app, Coinbase and Kraken. A paper trade in a coin Zac cannot buy on Robinhood is not a result.
Phase B can then stay deferred, because the main cost question is answered roughly without a key.

### 5. Small account: the result is measured in cents
Traced arithmetic at $60 (DESIGN.md 4.1 and 6.1):
- 25 percent cap = $15 per position (tier 3 cap 10 percent = $6).
- Risk at score 70 to 79 = 0.5 percent = $0.30. With a stop about 1 percent away, the risk-sized position is about $30, so the $15 cap binds almost always. Real risk becomes about $0.15 a trade (0.25 percent).
- At F95, one round trip on $15 costs about $0.29, which is more than the $0.15 at risk. A full 2.5R win is about $0.37 gross, about $0.09 net.
The $60 view will show that even a perfect run earns cents. The 100000 view, in percent, will look far better.
**Fix:** the scorecard leads with the `zac_60` ledger in dollars at F95, then percent. Every report line that quotes a percent return also states the dollar figure at $60. This is not an argument to stop; the project's value is learning and the plumbing. It is an argument to say so plainly on page one.

### 6. 24/7 on a home PC is mostly unnecessary for the ledger that matters
DESIGN.md 13.2 risk 9 and Q16: the PC must stay on 24/7. It is also the transcription GPU, the editing machine and the stock watcher host, and Windows Update reboots it.
The Zac ledger fills only inside acting windows and checks stops "on closed bars and quotes" since the last window (DESIGN.md 8.2). Closed hourly candles can be re-fetched after the fact (300 per call, DESIGN.md 3.2). So the Zac ledger needs the PC on during acting windows plus a candle backfill, not round the clock. Only the main ledger and the live revision watch need 24/7.
**Fix:** make the Zac ledger survive gaps by design: on each start, backfill closed bars since the last run and replay stop and target checks. Report "watched hours percent" on the scorecard; a counted week below a set coverage (trading-director picks the number, written in config) is reported as partial. Answer Q16 with this, not with "buy an always-on machine".

### 7. Scope creep from 12 pairs
Locked rules say "scans the whole list" (wkt-locked-rules.md). The design already cut that to about 12 (Q6). Twelve correlated crypto pairs bring: Kraken mapping per pair, liquidity tiers, the correlation module, the stablecoin heuristic, and a breadth proxy. DESIGN.md 6.6 itself says four alt positions "can behave like one big position", and missing correlation data counts as correlated. Fifty trades taken across 12 coins in one BTC trend are far fewer than 50 independent observations, so more pairs buy speed at the cost of meaning.
**Fix:** first frozen config holds BTC, ETH and at most 4 more, each on Robinhood (change 4), Coinbase and Kraken, all tier 1 or tier 2. Tier 3, the stablecoin heuristic (no stablecoin will be in a hand-picked list) and the breadth override wait for v2. The regime detector stays log-only as designed (multipliers 1.0, DESIGN.md 5.4), so it can be built late or trimmed to the BTC daily trend leg without losing anything in the first count. The memecoin guide test (DESIGN.md 10) stays out of this build entirely.

### 8. Vectors toward real money early, traced
- **False PASS at 30 bps** (The One Thing).
- **The 20-trade gate does double duty.** "20 trades = plumbing works" (WATCH-WEEK-PLAN amendment 3) is also the trigger for the size step-up (DESIGN.md 6.1). A plumbing number should not unlock risk. Fix: step-up needs 50 counted trades at the F95 pass line on the Zac ledger.
- **Locked rule "Twilio YES/NO approval with auto-execute if no reply (for the live phase)"** (wkt-locked-rules.md, Operation). Silence placing a real order conflicts with the root rule that Zac pulls the trigger on anything irreversible and any spend. The paper build has no live path (DESIGN.md 2.4), good. Fix: nothing in the crypto build may include a Twilio or reply-timeout module, and trading-director queues this locked rule in `logs\DECISIONS.md` for Zac to re-confirm or change before any Phase 3 talk. Flagged, not ruled; it is Zac's rule.
- **The emotional driver is on file.** The $52 to $4,392 memecoin claim has nothing retrievable behind it, and the CFTC treats such claims as a fraud signal (ai-bot-claims-check). Fix: the scorecard's first block prints buy-and-hold BTC over the same days (already in DESIGN.md 10) next to the Zac ledger at F95, so "beat doing nothing" is the first comparison, not "how much did it make".
- **Go-live checklist item 7** (Zac's own words on what he can afford to lose) stays FAIL until written. Keep it.

### 9. The unverified Robinhood list is longer than the verified one
DESIGN.md 13.3 lists 13 Robinhood unknowns, including stop support for crypto, resting limits, minimum order, increments, the pair list, the real spread, the fee tier for app market orders, Georgia availability and any day-trade rule. None blocks a paper build. All of them block reading a paper result as tradeable.
**Fix:** the scorecard header carries a line "Robinhood items verified: N of 13" with the list. A result with fewer than the five that change fills (stop support, resting limit, fee route, minimum order, pair list) verified is labeled "proxy result, not a Robinhood result". Change 4 closes most of the five in one sitting.
Side note: `Investing\CLAUDE.md` still says Robinhood "doesn't support programmatic/automated order placement for retail accounts" and that PDT applies. The research file shows a Crypto Trading API exists and FINRA Notice 26-10 replaced the PDT rule (Robinhood's own enforcement not verified). That file is stale; trading-director should correct it.

### 10. Sequencing against the stock watch week
The stock watcher's counted week starts Monday 2026-11-30 (WATCH-WEEK-PLAN). DESIGN.md 7.4 found the stock scorecard does not yet count "score 70 or higher, once per setup" and has no config hash on log lines (Q14). The crypto design copies the stock modules.
**Fix:** the crypto build may proceed in parallel (copy plus parity test protects the stock run), but no counted crypto run starts until the stock watch week's first scorecard has been through qa-claims, so the counting and hash fixes land on both sides first. Also, Q17 (Investing is DORMANT) is a hard blocker on any build work in Zac's own words, as the design already says.

---

## CHANGES (the list for trading-director)

Before build step 2:
1. Zac ledger pass line = F95 (95 bps each side plus haircut). 30 bps relabeled optimistic. Lower it only to a measured figure, by logged config change.
2. `max_cost_to_risk` computed at the pass-line cost.
3. Variant B target exits pay the exchange fee.
4. Q9 first, extended: three app price previews against the Coinbase ticker (no order), default order type, Robinhood coin list. Universe = Robinhood app overlap with Coinbase and Kraken.

Before the counted run:
5. Zac-ledger triggers use haircut-adjusted bids.
6. Scorecard order: Zac ledger at F95 in dollars at $60, then buy-and-hold BTC, then percent views; main ledger labeled "not tradeable by Zac" and never shown above the Zac F95 row.
7. Zac ledger backfills closed bars after any gap; scorecard shows watched-hours percent and a coverage floor set in config.
8. First frozen universe: BTC, ETH and at most 4 more. Tier 3, stablecoin heuristic, breadth override and the memecoin test wait for v2.
9. Step-up needs 50 counted trades positive at the F95 line, not 20.
10. No Twilio or auto-execute code in this build; the locked auto-execute rule is queued for Zac to re-confirm before any Phase 3 discussion. "Robinhood items verified N of 13" on the scorecard header. No counted crypto run before the stock watch week's first scorecard clears qa-claims. Q17 answered by Zac first.

---

## WHAT IS WORKING (do not edit these out)

- One GET-only `http_gate` with a host-plus-path allowlist, and Robinhood accounts, holdings and orders forbidden even though they are GETs (DESIGN.md 2.1, 2.2). This is the right shape.
- Phase A needs no key at all. Key values never printed, logged or stored, test K plants a fake key to prove it.
- UNKNOWN is FAIL, with a full list of causes, plus a circuit breaker and OUTAGE_GAP tagging. Honest about outages instead of hiding them.
- The Zac-can-act ledger with no resting stops (variant A) and the `realized_r_vs_planned` field. This is the most honest thing in the design and it carries the ruling from the stock plan correctly.
- `cost_r` on every trade and the haircut ladder that re-prices the same trades exactly. Once the pass line is moved, this machinery tells the truth quickly.
- Copy-with-parity-test instead of editing the stock watcher mid-count.
- Section 14's plain statement that "no edge after costs" is an acceptable result. Keep that sentence on the scorecard.
- The design flags its own gaps (13.3) instead of filling them with guesses.

---

Ruling scope: paper-only build. This is not a ruling on any real-money phase. Any real-money crypto test needs a separate written decision by Zac (DESIGN.md Q18) and a new ruling.
