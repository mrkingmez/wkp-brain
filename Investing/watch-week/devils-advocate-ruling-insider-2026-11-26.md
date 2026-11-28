# Devils-advocate ruling: SEC Form 4 cluster buys as a scored paper-test input (2026-11-26)

Requested by trading-director (Fawn Forest Investments). Read-only review. Paper only. Not advice, no promise of return.

Sources read, and nothing else:
- `D:\WKP\Investing\research\openinsider-cluster-buys-2026-11-26.md` (first pull, 17 rows shown)
- `D:\WKP\Investing\research\insider-data-terms-2026-11-26.md` (SEC terms, Form 4 facts, published findings)
- `D:\WKP\Investing\watch-week\WATCH-WEEK-PLAN.md` (stock plan, amendments, sizing rule)
- `D:\WKP\Investing\watch-week\devils-advocate-ruling-2026-11-26.md` (my stock ruling)
- `D:\WKP\Investing\CLAUDE.md` (venture file, loaded in context)

Plan under review (as stated in the request): Form 4 code P, 3+ distinct insiders in a 10-day window, insider type classified, filing lag recorded; forward returns at 1, 5, 20 trading days vs SPY from the first open after filing; regime tag; haircut 5/15/30 bps; a second "Zac can act" ledger; frozen config; one change per run; fewer than 30 counted clusters = no verdict; no sizing authority.

Arithmetic below is labeled EXAMPLE. It is my arithmetic on stated assumptions, not a retrieved figure.

## VERDICT: GO WITH CHANGES (gated)

The idea is legitimate. Insider purchases are the one corner of the AI-trading pile that has peer-reviewed support (the research file cites Lakonishok and Lee 2001, Jeng, Metrick and Zeckhauser 2003, Cohen, Malloy and Pomorski 2012). Running it with no sizing authority is the right posture. But as written the test cannot do what it implies. It can tell you "no" in a year. It cannot tell you "yes". And three mechanical defects (signal timing, who counts as an insider, what counts as a purchase) would let it say "yes" falsely. Fix those, and do not start building until the stock watch week has its first scorecard.

## THE ONE THING

**"Fewer than 30 counted clusters = no verdict" reads as "30 clusters = verdict". At 30, the test can only kill the idea, never confirm it.**

Why: the effect you are hunting is small next to the noise. The research file gives published abnormal returns of roughly 40 bp to 180 bp a month, before costs, on samples ending 2007 or earlier. A small or mid-cap stock's 20-day return relative to SPY swings far wider than that.

EXAMPLE (assumed figures, not retrieved): if 20-day excess return has a spread (standard deviation) of 12 percent and the true edge is 1.5 percent, the standard error at 30 clusters is about 12 / 5.5 = 2.2 percent. The true edge sits inside the noise. To get the edge to two standard errors you need about (2 x 12 / 1.5) squared = 256 clusters. Clusters also bunch on the same days and in the same market moods, and the 20-day windows overlap, so the real sample is smaller than the count.

How many will you get? The first pull shows about 15 rows with 3+ insiders and $1M+ in one month, before removing funds, sponsors, IPO buys, foreign and OTC names. EXAMPLE: if 5 to 10 a month survive the filters, a year gives 60 to 120. Still under the size that could confirm.

Fix:
1. Make the 30 rule asymmetric and say it in the scorecard header: "30 counted clusters can KILL this signal. No forward sample this year can PROMOTE it."
2. The real evidence test is a point-in-time backfill from the SEC quarterly Insider Transactions Data Sets (2006 onward, one download a quarter, allowed under SEC fair access per the research file). Same frozen rules, written before anyone looks at results. Forward paper then becomes the out-of-sample check: does live behavior land inside the backfill's range. A pass needs both.
3. The backfill has its own trap (item 2 below, delisted names). If price history for delisted names cannot be had free, the backfill result is biased upward and must be labeled so.

## HOLES

### 1. Look-ahead in signal time (the most likely way to fake a win)
- **The cluster does not exist until the third insider's filing is accepted.** If the entry is "first open after filing" of the first insider, or after a date OpenInsider assigns to the group, you are trading on information that arrived later. OpenInsider's cluster page groups filings after the fact.
- **Filing date is not filing time.** A Form 4 accepted at 10:15 on day D cannot get day D's 9:30 open. One accepted at 21:00 cannot get anything until D+1. OpenInsider posts 6:00 to 22:00 ET (research file).
- **Amendments.** A 4/A can add rows later (research file, Q3). Counting a row that only appeared in an amendment, as of the original date, is look-ahead.
- **Late filers.** Deadline is 2 business days, late filings exist. A purchase reported 3 weeks late can complete a "10-day cluster" on trade dates that nobody could have seen inside the window.

Fix (all frozen in config): signal time = EDGAR acceptance date-time of the filing that brings the distinct-insider count to 3. The 10-day window is measured on transaction dates, and every contributing filing must be accepted no later than the signal time. Entry = first regular-session IEX print strictly after signal time. Amendments count only from their own acceptance time. Contributing rows with filing lag over a fixed number of business days (pick it now, for example 5) are excluded and counted in a "dropped, late" line. Whether the quarterly data set carries acceptance time of day is NOT VERIFIED; if it only carries a date, the backfill enters at the open of the NEXT business day after the acceptance date.

### 2. Survivorship and ticker reuse
- Form 4 data keys on issuer CIK. Tickers change, get reused, and get dropped. Joining on ticker can attach a 2015 filing to a different company's 2026 price.
- A cluster whose stock is delisted within 20 days disappears if its bars are missing. Losers vanish, the average looks better.
- Whether Alpaca's free historical bars cover delisted symbols is NOT VERIFIED.

Fix: key everything on CIK; map CIK to ticker as of signal date. A cluster with no price after entry is never dropped silently: mark it to the last available print, flag it DELISTED or MISSING, and report the count on line one of the scorecard. If more than 5 percent of backfill clusters are MISSING, label the backfill "survivor-biased, upper bound only".

### 3. Who is an "insider": funds, sponsors, entities
The first pull already shows the problem: BPRE and KYN are closed-end funds, BORR and GLXY rows are large holders or sponsors (research file cautions). A fund's own affiliates buying its discounted shares, or a private-equity sponsor topping up, is a different mechanism from three executives buying with their own money. The published findings are about officers and directors. Jeng et al. also found top executives did not beat other insiders, so slicing by title buys nothing.

Fix (one primary definition, frozen): a reporting owner counts only if isDirector or isOfficer is true. 10 percent owner only, Other only, and entity filers (LLC, LP, fund, trust names) do not count toward the 3. Issuers that are closed-end funds, BDCs, ETFs or trusts are excluded. Joint filings: count distinct reporting-owner CIKs, never filings (research file, Q3). The isTenPercentOwner and isOther field names are NOT VERIFIED in the current XML spec; read the v5.5 spec before the parser is written.

### 4. What is a "purchase": code P is not pure open market
The SEC form says code P is "open market or private purchase" (research file, Q3). Private placements, PIPEs, rights offerings and directed shares in an IPO all print as P. Look at the first pull: Teamshares, EquipmentShare and similar recent listings show 3-insider clusters at a single price, which is what buying in an offering looks like. That is a mechanical cluster, not a judgment call by three people.

Fix: Table I, code P, non-derivative only. Exclude 10b5-1 flagged rows. Exclude any issuer within 90 trading days of its first listed trade. Exclude same-day multi-insider buys at an identical price when a footnote mentions offering, placement, IPO, rights or subscription. If the footnote cannot be read, the row is UNKNOWN and UNKNOWN is FAIL (your own standing rule).

### 5. Tradability at $15 a position on an IEX-only feed
- At $60 the 25 percent cap is $15 a position (stock plan). COHR at $198 or TTMI at $73 needs fractional shares. Robinhood's fractional eligibility rules are NOT VERIFIED; some listed names will not be eligible. PAM, BORR and other foreign or ADR names may not quote on IEX at all (pull file).
- The literature says the effect lives in small firms (research file). Small firms are where spreads are widest, IEX prints are thinnest, and the first IEX print after 9:30 may come late or at a bad price. The IEX first print is not the official open.
- The 5/15/30 bps ladder was set for liquid stocks. For small caps a 30 bps round-trip pass line is likely below the real cost. My standing lesson: the pass line must be at or above the highest documented cost for the real account, never a placeholder below it.

Fix: log the IEX bid and ask at entry, the time of the first print, and a FRACTIONAL-ELIGIBLE flag (UNKNOWN until verified on Robinhood's own page). Net result on the Zac-can-act ledger uses the larger of 30 bps and the measured half spread each side. A cluster that the Zac-can-act ledger cannot buy (no IEX print in the first 30 minutes, OTC, foreign, not fractional-eligible) is logged as UNFILLED and counted in the denominator for the tradability rate, never dropped.

### 6. Benchmark is the wrong size
Most qualifying names are smaller than the average SPY company. In a month when small caps rally, every cluster "beats SPY". That is size, not insider skill.

Fix: report excess vs SPY and vs IWM (fetch IWM from the same IEX bars). The primary pass needs both positive. Requiring both is stricter, so it does not add false wins.

### 7. Multiple testing
Insider type (4) x regime tags (6) x horizons (3) x haircut levels (3) = 216 cells. At 30 clusters most cells hold zero or one. "It works for directors in UPTREND_CALM at 5 days" will show up by chance alone.

Fix: write ONE primary test into the frozen config before the first counted cluster:
- Population: officer and director clusters as defined in items 3 and 4.
- Metric: mean excess return vs SPY and IWM at ONE horizon, on the Zac-can-act ledger, net of the item 5 cost.
- Horizon: pick one now (see item 8 for why it matters). Every other horizon, type split and regime split is printed under a heading "EXPLORATORY, cannot change a rule or promote anything". No rule may be added from an exploratory cell until it has been re-tested on clusters accepted after the date it was proposed.

### 8. Phase-gate leakage: the horizon collides with the locked rules
The locked rules carry a 5-day time stop for stocks (stock plan, Rules in force). The published effect is about half in the first month (research file, Jeng et al. working paper). If the primary horizon is 20 days and it passes, it cannot be used under the locked rules without changing them. A quiet "insider names get a longer hold" is a rule change by the back door.

Second leak: "scored paper-test input". If the insider flag feeds the stock watcher's 0 to 100 score in any way, it changes which trades the watch week takes, which changes the frozen config and resets the stock counts. That is sizing authority in disguise.

Fix: the insider test runs in its own ledger with its own config file and its own hash. It writes nothing to the watcher's config, score or decisions.jsonl. State in the config: "A pass here is a request to Zac for a locked-rule change. It is never adopted automatically." Choose the primary horizon knowing that: 5 days fits the rules today, 20 days matches the literature but needs Zac.

### 9. It competes with the stock watch week for the same hands
The stock watch week is at 0 of 7 on its go-live checklist, the amendments build was still running at last report, no live scan has happened (stock plan; TASKS row 2026-11-26). This test needs a new parser (Form 4 XML, joint filers, amendments, footnotes), a CIK to ticker map, a quarterly backfill, and Zac's SEC User-Agent environment variable, which is already queued as his decision. That is a second build of similar size.

Fix: same gate as the crypto ruling. No build and no counted cluster until (a) the stock watch week's first scorecard passes qa-claims, and (b) Zac has set the SEC User-Agent himself. Before that, allowed: reading the v5.5 XML spec and the table-definition PDF, writing the frozen config, and writing strategies-tried rows. Nothing that needs software-director's time.

### 10. Confirmation bias, and the NEGG example
- NEGG is one 10 percent owner, not a cluster of officers and directors. It is not an instance of this signal, so it proves nothing either way. Keep it out of the reasoning.
- The bigger risk is the 17 rows already pulled. People will watch COHR, FUN and STWD over the next month and tell stories. Those rows were seen before the config exists.

Fix: count only clusters whose signal time is after the config freeze timestamp. Nothing from the 2026-10-26 to 2026-11-25 pull is counted. The scorecard carries no named-ticker anecdotes, only the counted table.

### 11. Even a real edge does not fund products at $60
This is not a reason to stop, but the goal stated in the request is growing capital to fund product building.
EXAMPLE: a 2 percent net excess on a $15 position is $0.30. Ten fills a month is about $3. A real edge at this size is a learning result, not a funding source. The scorecard should print the dollar figure at $60 next to the percent, so nobody mistakes one for the other.

## KILL CRITERIA (stated now, before any data)
Any one of these ends the forward test. trading-researcher logs it in `Investing\research\strategies-tried.md` as tried and failed, with the reason.

- **K1 (no edge):** at 30 counted clusters, the primary metric (item 7) is zero or negative AND the median is zero or negative. Stop.
- **K2 (untradable):** at 30 qualifying clusters, more than 40 percent are UNFILLED on the Zac-can-act ledger (item 5). Stop: it cannot be traded at this account size.
- **K3 (too expensive):** at 30 filled clusters, median measured round-trip cost (spread plus haircut) is above 1 percent. Stop.
- **K4 (too rare):** fewer than 30 counted clusters six months after the first counted day. Stop: too rare for this account to learn from.
- **K5 (backfill fails):** if the backfill is run and the primary metric is zero or negative net of costs under the point-in-time rules, no forward run starts. If the backfill is survivor-biased (item 2) and still only marginal, same result.
- **K6 (look-ahead found):** qa-claims finds any counted entry before its signal time, or any cluster that used an amendment row before its acceptance. All counts void, fix, restart from zero.
- **K7 (tuning):** the config is reset twice before 30 counted clusters. Stop and bring the list of resets to trading-director; that is tuning, not testing.

What a pass looks like (and it is still not adoption): backfill positive net of costs vs SPY and IWM, forward mean inside the backfill's range at the pre-stated cluster count, K2 and K3 clear. Then it goes to Zac as a locked-rule change request.

## WHAT IS WORKING (keep it)
- No sizing authority. Paper only. No orders.
- SEC data over OpenInsider for automation, with OpenInsider terms honestly marked NOT RETRIEVED and no bypass tried.
- Filing lag recorded, insider type classified, 10b5-1 flag noted in the research.
- Entry from the filing, not the trade date. The researcher caught that the insider's own price is not available to us.
- The Zac-can-act ledger and the 30 bps stress level carried over from the stock ruling.
- One change per run and a frozen config.
- The research file says plainly that no cluster-only effect size and no cost-net result was retrieved, and that every sample ends by 2007. That honesty is the reason this test is worth running at all.

## REQUIRED CHANGES (numbered)
1. Asymmetric rule in the scorecard header: 30 clusters can kill, nothing this year can promote from forward data alone.
2. Point-in-time backfill from the SEC quarterly sets as the main evidence test, frozen rules first; forward paper as out-of-sample check.
3. Signal time = acceptance time of the filing that completes the 3; window on transaction dates; entry at first IEX print after signal time; amendments from their own time; late rows over a fixed lag excluded and counted.
4. Key on CIK, ticker as of signal date; DELISTED and MISSING clusters marked, never dropped; over 5 percent missing labels the backfill an upper bound.
5. Count only isDirector or isOfficer owners; exclude 10 percent only, Other only, entities, and fund or trust issuers; count distinct owner CIKs.
6. Table I code P only; exclude 10b5-1, issuers within 90 trading days of listing, and offering-style identical-price buys; unreadable footnote = UNKNOWN = FAIL.
7. Log IEX spread and first-print time; net cost = larger of 30 bps and measured half spread each side; UNFILLED clusters stay in the denominator.
8. Benchmark vs SPY and IWM; primary pass needs both.
9. One primary test (population, metric, one horizon) written before the first counted cluster; everything else labeled EXPLORATORY.
10. Separate ledger and config file; writes nothing to the stock watcher; a pass is a request to Zac for a rule change, never automatic. Choose the horizon knowing the 5-day locked time stop.
11. No build and no counted cluster until the stock watch week's first scorecard passes qa-claims and Zac has set the SEC User-Agent himself.
12. Count only clusters after the config freeze; nothing from the 2026-11-26 pull; no named-ticker anecdotes in the scorecard.
13. Print the dollar result at $60 next to every percent.
14. Kill criteria K1 to K7 copied into the frozen config verbatim.

## NOT VERIFIED (needs a lookup before it is relied on)
- Robinhood fractional-share eligibility rules.
- Alpaca free historical bars for delisted symbols, and whether free historical SIP (not recent) is available.
- Whether the SEC quarterly data set carries acceptance time of day and footnote text.
- XML field names isTenPercentOwner, isOther, aff10b5One in the current v5.5 spec.
- Any cluster-only or cost-net published effect size (research file says not retrieved).

Ruling stands as GO WITH CHANGES, gated on item 11. The director or Zac decides.
