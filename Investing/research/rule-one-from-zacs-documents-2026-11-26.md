# Rule One, as stated in Zac's own course documents

Date: 2026-11-26. Author: trading-researcher. For: trading-director (Fawn Forest Investments). Internal notes, not public copy.
Source folder: `D:\Documents\Rule 1 Documents\` (21 files, dated 2016 to 2019). Zac's private course materials. Read-only. Working copies and text extracts sit in `D:\WKP\scratch\rule1\` (gitignored). Originals untouched.
Status: EDUCATION AND PAPER DESIGN ONLY. No orders, no keys, no spend. Nothing here is advice, and no win rate or return below is a fact. Every number from a document is tagged DOCUMENT CLAIM (not verified).

## BLUF

1. The documents teach two separate things. (A) Stock quality: the Three Ms (Meaning, Management, Moat/MOS) with numbers from financial statements. (B) A monthly options income system: sell a bull put spread (BPS) on the Russell 2000 index (RUT) on expiration Friday, size it to a target "ARORC" of about 48 percent, exit on two rules.
2. Part A is thin on formulas. The documents never print the sticker price formula, the 50 percent margin of safety rule, or the label "Big Five". They send the reader to the Rule One Toolbox web calculator. Only part of A can be rebuilt from these files alone.
3. Part B is fully rule-based and easy to code, which is also why its claims are easy to attack. Every performance number is the author's own backtest, built on prices of "Mark" mid-points with no commissions and no bid-ask cost, and the PDF and the spreadsheet disagree with each other year by year.
4. $500 account fit is poor for the system as written. A RUT 5-point spread risks about $470 per contract (document inputs), about 94 percent of $500 in one position. A 10-point spread risks about $957. A smaller underlying (XSP or an ETF) is the only design route, and none of that is in the documents.
5. Proposal: a four-stage paper track (Section 5), separate files, zero change to the stock watcher or its frozen config.

## File reading status

All 21 files opened. Text from PDFs via pdftotext, docx via python-docx, pptx by XML text, xlsx by openpyxl (formulas and cached values, copies only). Several PDFs are slide decks whose screenshots carry meaning that text cannot show (RUT presentation, options matrices): I read text only, plus I looked at the backtest table image on page 8 of the BPS PDF. Screenshots inside the RUT presentation were NOT read.

| File | Pages or sheets | Status |
|---|---|---|
| Technical Indicators.pdf | 16 | Read (text) |
| TI EXPIRATION DAY BPS SYSTEM BETA .92 PDF-Updated.pdf | 8 | Read, backtest image viewed |
| TIW RUT System Trade Presentation.pdf | 20 | Text read; most pages are screenshots, NOT read |
| Tools for Analyzing the Three Ms.pdf | 1 | Read |
| Rule 1 BPS KELLY WORKSHEET.xlsx | 1 sheet, A1:W263 | Structure and formulas read |
| Rule One ARORC Calculator v3.2.xlsx | 1 sheet | Read |
| RUT Backtesting Spreadsheet JAN17v1.xlsx | 1 sheet, 2008 to 2017 blocks | Read, 2008 to 2012 filled, 2013 on blank |
| TI RULE OF 72.docx | 1 | Read |
| Introduction to Credit Spreads.pdf | 14 | Read (text, image slides partly) |
| NEW Options Matrix.pdf, Phils Options Matrix.pdf | 1 each | Phils read (sell/buy, call/put grid); NEW is an empty grid |
| Reduction of Basis (3).pdf and PPT | 11 and 13 slides | Read |
| Track Reduced Basis.xlsx | ATW sheet | Read |
| 4 Step ARORC Calculation2.pdf | 4 | Read |
| Understanding Fin Statements August 2016.pdf | 31 | Read (text; many image pages) |
| Rule One Story Form Resources.pdf | 1 | Read |
| HOW TO GO FROM 2K TO 3M STEPS.xlsx | 1 sheet | Read |
| TIW 3 Arrows SPY Sept 2017.xlsx | 1 sheet | Read |
| Zac Rule 1 BPS KELLY WORKSHEET.xlsx | 1 sheet | Read |
| Think or Swim setup docx | 1 | Read |

## (a) Stock-quality method, as the documents state it

| Item | What the documents say (paraphrase) | Tag and location |
|---|---|---|
| Three Ms | Moat, Management, Margin of Safety. A "Story Form" adds Radar (find the company, check which gurus hold it) and Meaning (do I understand it, do I like it) ahead of the three | DOCUMENT CLAIM. Tools for Analyzing the Three Ms p1; Story Form Resources p1 |
| Moat | Five types named: brand, price, secrets, switching cost, toll bridge. Test: if the numbers look good there must be some moat; compare to peers; read the 10-K Business section and earnings calls. Questions include durability for twenty years | DOCUMENT CLAIM. Story Form p1; Three Ms p1 |
| Management | Honest, experienced, owner-minded; read the CEO letter, last earnings call (remarks and Q and A), and the CEO's "Big Audacious Goal" | DOCUMENT CLAIM. Story Form p1 |
| Management numbers | Return on equity (net income over common equity) 10 percent or more, often over 20; return on invested capital (net income over long-term debt plus equity) 10 percent or more; debt payback (long-term debt over net income) about 3 years or less | DOCUMENT CLAIM. Fin Statements pp22 to 26 |
| Growth numbers | "Big 4" growth rates: equity per share plus dividends per share, earnings per share, operating cash flow per share, sales per share. Document uses the name Big 4, not Big Five | DOCUMENT CLAIM. Fin Statements pp16 and 21 |
| Margin of safety | EPS-based; the reader uses the Rule One Toolbox "MOS calculator", checks TTM EPS against a second page, picks a future growth rate (the lower of own estimate and the calculator's), and sets the future P/E at double the growth rate, capped at the stock's high P/E | DOCUMENT CLAIM. Story Form p1 |
| Payback time | "8 Year Payback Time" uses free cash flow per share, checked against GuruFocus TTM | DOCUMENT CLAIM. Story Form p1; Fin Statements p27 |
| Sticker price, 50 percent MOS rule, tangible book price, cap rate | Named as questions or items, never defined or computed | NOT IN THE DOCUMENTS. Three Ms p1 asks for them; Fin Statements p27 lists Cap Rate |
| Rule of 72 | Years to double equals 72 over growth rate, table 2 to 10 years | DOCUMENT CLAIM. TI RULE OF 72.docx |
| Basis reduction | Six ways to lower cost basis: buy in four tranches, sell puts at the entry price (ROP), sell covered calls above sticker (ROC), sell some shares at or above sticker, dividends, buybacks. Worked 10-year example ends with adjusted basis near $4,815 (PDF) or $2,092 (PPT), two different illustrations | DOCUMENT CLAIM (hypothetical inputs). Reduction of Basis PDF pp2 to 10; PPT slides 3 to 10 |
| Real-example claim | A single Atwood Oceanics position in 2016 reportedly reached negative basis within 11 months; the tracking sheet shows purchases of about 5,850 shares at roughly $6 to $7 and sales of puts, calls and shares | DOCUMENT CLAIM, one case, cherry-picked by nature. PPT slide 13; Track Reduced Basis.xlsx |

What is not here: the sticker price formula, any stated historical results for the stock method, any screen criteria for what counts as "wonderful", and any mention of how often picks failed. The two tool references (Rule One Toolbox, GuruFocus 30-year financials) are paid or partly paid websites; I did not check their prices or terms.

## (b) Options system as documented

### The Expiration-Day BPS system on RUT (author: Phil Town, copyright 2014, release 0.92 beta)

| Element | What the document says | Tag, file and page |
|---|---|---|
| Purpose | Educational, "not trading advice", students should complete the back-test worksheet themselves | DOCUMENT CLAIM. BPS PDF p1 |
| Underlying | Russell 2000 index (RUT) | BPS PDF p2 |
| Timing | Open on the third Friday (current expiration day), choose the next month's expiration (about 27 to 35 days; sheet shows 27, 33, 34, 35) | BPS PDF p2; RUT Backtesting row 6 |
| Structure | Sell one put, buy a lower put, same expiration. Spread width 10 points | BPS PDF pp3 to 4 |
| Strike choice | Start at the strike with about 93 percent "Probability OTM" (acceptable 89 to 95 percent; delta between 0.04 and 0.10). Probability OTM is read from ThinkOrSwim | BPS PDF p3; Intro to Credit Spreads p13 |
| Credit | Net credit = short put mark minus long put mark; marks are rounded up to the next penny | BPS PDF p4 |
| Return maths | Risk capital (RC) = spread minus net credit. RORC = net credit over RC. Multiplier = 365 over days to expiration. ARORC = RORC times multiplier | BPS PDF pp4 to 5; 4 Step ARORC pp1 to 4 |
| Target | Move down the probability ladder until ARORC is at or above about 48 percent, then recheck probability is at least about 90 percent. Worked example reaches 48 percent at a net credit of $0.43 on a 10-point spread | BPS PDF pp5 to 6 |
| Exit trigger 1 | Close both legs if the short strike's Probability OTM falls below 70 percent at any time | BPS PDF p7; RUT presentation p18 |
| Exit trigger 2 | In the final week, exit if RUT is within 3 percent of the short strike (mandatory on the Thursday before expiry, because settlement uses Friday's opening prices) | BPS PDF p7; RUT presentation p18 |
| No adjustments | Losses are taken, not repaired. The document says this is by design because Probability OTM "is wrong big" when wrong | BPS PDF p1 |
| Stated loss size | Average loss claimed about $2.30 per 10-point spread after credit, about 24 percent of risk capital, average RC about $9.50 | DOCUMENT CLAIM (not verified). BPS PDF p7 |
| Stated track record | Text says "84 wins against 4 losses over 7 years" on page 1, but "4 losses out of 72 trades across 6 years" on page 7. These do not agree | DOCUMENT CLAIM, internally inconsistent. BPS PDF pp1, 7 |
| Stated yearly returns 2008 to 2013 | Table: 33, 55, 41, 21, 59, 56 percent; six-year CAGR 43 percent | DOCUMENT CLAIM (not verified). BPS PDF p8 |
| System's own warning | Even a system with this record can lose all capital; Probability OTM rests on assumptions the author calls a fiction | BPS PDF p1 |
| Tool | ThinkOrSwim: ThinkBack tab for historical practice, paper money account for forward practice, "Chart-Charts" layout (setup video linked, 2019 note) | RUT presentation pp8 to 12; ThinkOrSwim docx |
| Data caveat | Probability OTM data in ThinkBack only goes back to 2013 per the PDF, yet the sheet's 2008 to 2012 rows carry probabilities, so provenance of those inputs is not shown | BPS PDF p1; RUT Backtesting rows 7 to 8 |

### Related teaching pieces

| Piece | What it does | Tag, file and page |
|---|---|---|
| Credit spread intro | Insurance analogy: a hedged policy cuts capital needed. Example: RUT, 5-point spread, 24 days, net credit $0.22, "RORC 4.6 percent, ARORC 70 percent" | DOCUMENT CLAIM (example only). Intro p5 to 8 |
| Trend check before entry | Check chart trend and floors and ceilings before a BPS; use the prob range 90 to 95 percent and ARORC near 48 percent | Intro p9 to 10 (text typo gives delta as ".4 - .10") |
| Technical indicators | 3 Arrows (10-period simple moving average, MACD 8,17,9, slow stochastic 14,5,0 on a 10-year monthly chart, for broad funds only, not single stocks: enter on three green arrows, exit on three red). Floors and Ceilings (support and resistance with 2 or more touches), trendlines, Fibonacci retracements drawn between a floor and ceiling on 6 to 9 month day charts | DOCUMENT CLAIM. Technical Indicators pp3 to 15 |
| 3 Arrows SPY test | Claims about 7.9 percent CAGR arrows against 3.3 percent buy-and-hold over roughly 2000 to Sept 2017 on SPY; slide title says Sep 2007 to Sep 2017 but the sheet starts January 2000 | DOCUMENT CLAIM. Technical Indicators p5 and p8; TIW 3 Arrows xlsx |
| Kelly worksheet | See next table | |
| "2K to 3M" sheet | Compounds $2,000 at a flat 23 percent a year, then adds partnerships of $200,000, $2,000,000 and $18,000,000 in years 2 to 4 with a 25 percent general-partner share, ending near $3.07 million in year 5. It is an illustration, not a result | DOCUMENT CLAIM (assumption sheet). HOW TO GO FROM 2K TO 3M xlsx |

### What the three spreadsheets compute (formulas only; originals untouched)

**Rule One ARORC Calculator v3.2.** Inputs: spread S (default 5), net credit NC (default 0.43), days D (default 27). Computes RC = S minus NC; RORC = NC over RC (guarded for zero); M = 365 over D; ARORC = RORC times M (default cells give about 127 percent, while the note text beside it still shows an older $45-spread example). Second block: given a target ARORC (default 48 percent), S and D, the minimum net credit NC = (ARORC x D x S) / (365 + ARORC x D), rounded up to the cent. At S=5, D=27 that is $0.18. I checked this algebra: it is the exact inverse of the RORC and ARORC definitions.

**Rule 1 BPS KELLY WORKSHEET (original and Zac's copy).** One column per trade, 23 columns, trade types BPS, BCS (bear call spread), iron condor, ROP, ROC. Row order:

| Block | Rows | What it computes |
|---|---|---|
| Setup | 2 to 8 | date, underlying, price, expiration, days, floor or ceiling |
| Safety band | 9 to 10 | 3 percent of the floor or ceiling, then a minimum or maximum strike |
| Inputs | 11 to 12 | probability and delta typed from ThinkOrSwim |
| Strikes | 13 to 17, 20 to 22 | short, long, % OTM, % OTM scaled to 45 days (divide by DTE over 45), spread, credit minus debit, minus commission, net credit |
| Returns | 23 to 26 | RC, RORC, multiplier, ARORC |
| Kelly | 31 to 39 | W = Probability OTM; "% RC at risk" is typed (30 percent in the RUT columns, a guess for ATM or 70 percent exit); average loss l = RC x that %; R = NC over l; Kelly % = W minus (1 minus W) over R; times bankroll gives maximum bet; divide by RC gives theoretical shares and contracts |
| Actual | 41 to 45 | contracts actually used, total net credit and total risk |
| Result | 46 to 56 | result text, debit when closing, final RORC and ARORC |
| Summary | 57 to 68 | "YTD" total trades, open, wins, losses, win percent, total credit over bankroll, annualized |

What the Kelly rows imply: inputs are (1) the broker's Probability OTM as win chance and (2) a typed guess for average loss. With W near 0.89 and NC 0.30 on a 5-point spread, the sheet outputs a Kelly fraction near 37 percent of bankroll. That sizing is the author's tool, not a safe size; Kelly sizing with an estimated win chance the BPS PDF itself calls unreliable is the first thing a devils-advocate will attack.

**Zac Rule 1 BPS KELLY WORKSHEET.** Same layout as the original. The first six columns hold RUT 5-point spreads dated June 2018 to April 2019 (and one older iron condor from 2015). In the April 2019 column the bankroll is typed as $25,207, two contracts, net credit $0.30, result "closed". Net credit cells in these columns are typed numbers (0.3), not computed from the premium rows, which are mostly empty, and one column reads "Cancled", one "open". The file does not say whether these were real trades or paper. I did not assume either. The summary block still says "YTD 2014" with a 2015 date, 20 trades, 20 wins and 0 losses, bankroll $600,000, and the 20 wins include 4 trades the same block lists as open. That counts open trades as wins, so the 100 percent win rate shown there is not a measured rate.

**RUT Backtesting Spreadsheet JAN17v1.** One block per year from 2008 to 2017, twelve monthly columns each: date, days, probability, delta, short strike, long strike (short minus 10), credit and debit (typed from ThinkBack), net credit, RC, RORC, multiplier, ARORC, "finish OTM" yes or no, then a loss-exit block. Contracts equal starting cash divided by 1,000, rounded, and cash compounds month to month. A note says the 2008 to 2012 years are pre-filled, the student redoes them, then does 2013 to 2017, about 15 to 20 hours of work. Years 2013 onward are blank in this copy.
What the cached values show for the pre-filled years: starting cash $10,000 ends 2012 at about $57,493, with three months flagged "NO" (2008 month 9, 2010 month 3, 2011 month 7 by column order). Compounded, that is the sheet's output, not a verified result. Two checks of my own:
1. Year-by-year returns in the sheet differ from the PDF table. Example: 2009 is about 67 percent in the sheet against 55 percent in the PDF; 2010 about 35 against 41; 2011 about 15 against 21; 2012 about 67 against 59. They do not reconcile, probably because the PDF figure is credit over average RC per contract and the sheet compounds with rounded contract counts.
2. Position size: at the sheet's own rule (cash over 1,000 contracts of a 10-point spread with RC of about 9.5, about $950 risk per contract), the maximum loss per month is roughly 95 to 100 percent of the account. The system survives only because losses are cut early by the exit rules, which assume the market lets you exit.

**Other sheets.** Track Reduced Basis.xlsx: running cost basis after purchases, option premiums sold and share sales (running total, per-share basis). TIW 3 Arrows SPY: buy and sell price pairs by month, shares and portfolio value; CAGR through the RATE function against a buy-and-hold using prices only.

### Position size, win rate and return claims to carry forward (all DOCUMENT CLAIM, not verified)

- Win rate claims: 84 of 88, 68 of 72, "20 and 0" (open trades counted). Three different numbers in three places.
- Return claims: 43 percent six-year CAGR; yearly 21 to 59 percent; 48 percent ARORC target; example 70 percent ARORC.
- Loss claims: average 24 percent of RC, average about $2.30 per 10-point spread.
- Position size claims: Kelly outputs near 37 percent of bankroll; backtest sheet sizes near 100 percent of cash at max loss.
- Arithmetic from the documents' own inputs (mine, not a claim about results): with a $0.43 credit on a 10-point spread the break-even win rate is about 95.7 percent if every loss were a full loss. With the document's own stated average loss of about $2.30 the break-even win rate is about 84 percent. The system therefore needs a very high win rate or tightly capped losses, and its documented edge is almost entirely the exit rule.

## (c) What can be tested on free data, and what cannot

| Piece | Free route | Verdict |
|---|---|---|
| Stock-quality numbers (equity per share, EPS, operating cash flow per share, sales per share, ROE, ROIC, debt payback) | SEC filings via the free EDGAR data (rules and 10 requests per second limit with a declared User-Agent were retrieved in `insider-data-terms-2026-11-26.md`); prices from the Alpaca stock data already used by the watcher | TESTABLE on paper, but only the numbers. The sticker price and MOS rule are not defined in the documents and cannot be rebuilt from them (see Decision 29) |
| Moat, management quality, "Meaning" | Judgment from 10-K text and calls | NOT testable as a rule; skip in code, keep as a human checklist |
| 3 Arrows on SPY | Daily or monthly bars for SPY and a standard 10-period SMA, MACD (8,17,9) and slow stochastic. How far back Alpaca's free stock bars go was not retrieved this job | TESTABLE if the history reaches back to 2000; if not, NOT RETRIEVED for the early years. Stochastic "(14,5,0)" setting meaning is ambiguous in the document |
| Options spread simulation, ETF or equity options | Alpaca documents historical option bars, trades, quotes, Greeks and chain snapshots, but only from February 2024. The free "indicative" feed is delayed and derived, not true OPRA quotes; the full OPRA feed needs a subscription (source below) | PARTLY TESTABLE. About two years of history, a bull market for most of it, and quote quality on the free feed is a stated limit. A paper trade log is possible (Alpaca paper accounts support multi-leg orders per its changelog, January 2025) |
| RUT index options 2008 to 2017 (the actual backtest) | No free source retrieved | CANNOT BE TESTED. Index options history is not in Alpaca's free data as far as retrieved; whether Alpaca lists RUT index options at all was NOT RETRIEVED |
| ThinkOrSwim ThinkBack and Probability OTM | Needs a ThinkOrSwim account. Whether the paper-money signup still exists after the platform's later ownership change was NOT RETRIEVED. The document's link is from 2019 | CANNOT BE TESTED under our free-only rule. A proxy (delta from the Greeks) is possible but it is not the same number |
| 3 percent and 70 percent exit rules | Need intraday option quotes in the final week | PARTLY testable on the post-2024 sample only |
| Kelly worksheet | Pure spreadsheet maths | TESTABLE as arithmetic. The inputs (win chance, loss size) are the weak part |

Sources used for the options data facts: Alpaca docs, Historical Option Data (https://docs.alpaca.markets/docs/historical-option-data) and its multi-leg paper changelog (https://docs.alpaca.markets/us/changelog/multi-leg-level-3-options-trading-in-paper). A forum answer says the free plan includes OPRA data older than 15 minutes; that is a community post and I did not confirm it in official docs.

## (d) Gaps and risks, with the $500 account fit

### What a devils-advocate should attack

1. Provenance: every performance figure is the author's backtest, from 2014 and earlier, 2008 to 2013 only. The sample is dominated by a long rising market after early 2009. Nothing in the documents covers 2014 onward other than a note that 2014's first trade lost.
2. Internal contradictions: 84 of 88 versus 68 of 72 trade counts; PDF yearly returns versus spreadsheet; the "20 of 20" summary that counts open trades; a slide title that does not match its dates; data-source note says no probability data before 2013 but 2008 to 2012 rows have it.
3. Fill assumptions: credits are marks rounded up to the next penny, no bid-ask, no commissions (the Kelly sheet has a commission row that is blank), no slippage on exit, which is exactly when markets are fast and wide.
4. Tail risk: a credit of about $0.43 against about $9.57 at risk. The exit rule needs a clean exit. Index gaps overnight, or the 3 percent rule firing too late, break the claimed 24 percent loss size. Settlement uses Friday's opening prices (document p7), so a gap against the position can exceed what a Thursday exit rule can control.
5. Probability OTM is the key input, and the document says it is a fiction. Kelly then multiplies that unreliable number into a size.
6. Survivorship and selection: the course gives one system that worked; failed variants and live results are not shown. Independent verification of any Rule One options claim was NOT RETRIEVED this job. Treat the whole of Part B as an untested hypothesis.
7. Promotion context: the files include income-multiplication illustrations (2K to 3M) that are assumption sheets, not records.
8. Age: 2016 to 2019 materials. Tool names (ThinkOrSwim, Rule One Toolbox) and broker features may have changed; the exact setup steps cannot be assumed current.

### $500 account fit (arithmetic on the documents' inputs plus retrieved Robinhood facts)

| Check | Result |
|---|---|
| RUT 10-point spread, credit $0.43 | risk per spread about $957 (RC 9.57 x 100). Larger than the whole account. NOT feasible |
| RUT 5-point spread, credit $0.30 (Zac's sheet) | risk per spread about $470. One contract is about 94 percent of $500 at max loss. Feasible only as one contract and zero diversification |
| Documented average loss 24 percent of RC | about $113 on the 5-point case, which is about 23 percent of $500 in one loss; the 70 percent probability exit can fire after several smaller drops |
| Credit actually received | $0.30 x 100 = $30 gross on a $470 risk, before any contract fees (fee amounts NOT RETRIEVED; Robinhood says contract and exchange fees apply and refers to its fee page) |
| Approval | Robinhood: credit spreads are a Level 3 strategy; approval depends on experience and finances, set at the broker's discretion |
| RUT available | Robinhood lists RUT index options (cash settled, European style, cannot be exercised early) per its index options support page. Collateral for a credit spread: NOT RETRIEVED (the options collateral article was not read) |
| Bid-ask on RUT | NOT RETRIEVED. On a $0.30 credit, a spread of a few cents on each leg is a large share of the premium |
| Smaller alternatives | Index minis (XSP) or ETF options exist as ideas, but nothing in the documents covers them; their strike spacing, liquidity and cost were NOT RETRIEVED. Any $500-friendly version is a new design, not Rule One as documented |
| Stock-quality side at $500 | Whole shares only on Robinhood (per the trading plan notes); a $500 account holds at most a few positions; position sizing for "tranching in four slices" is not workable at that size |

PDT note: the retrieved plan notes say the FINRA PDT rule was replaced 2026-06-04. The BPS system holds to expiration or exits in days, so day-trade counts matter little, but the current rule text for options accounts was not re-read here.

## 4. Fit with the Fawn Forest plan

Zac's own terms: Rule One joins when options start; options start only at a real account balance of $500; verticals (BPS). Before then, education and paper design. Nothing proposed below touches `software\wkt-alpaca-watcher\`, its frozen config or its tests.

## 5. Proposed staged track (paper only)

| Stage | What | Gate to move on | Cost, risk |
|---|---|---|---|
| 0. Reading (now) | This brief becomes the study note. Zac reads the 8 named files with the glossary below. | None | $0 |
| 1. Paper design doc | Trading-director writes `Investing\rule-one\DESIGN.md` (new folder, separate from the watcher): entry rules, strike choice using delta from free Greeks as a stand-in for Probability OTM, exit rules, size cap such as "never more than X percent of account at max loss" (a number Zac sets, not me), a ledger layout copied from the Kelly worksheet columns plus real bid, ask and mid | Devils-advocate GO WITH CHANGES or better | $0 |
| 2. Free-data replication | (a) 3 Arrows on SPY with free bars, compared with the document claim. (b) Stock-quality numbers from SEC filings for a short watch list, computed and logged only. (c) A credit-spread paper simulation on Alpaca option data from 2024 on, on an ETF underlying, measuring mark-versus-bid/ask cost. Each result goes in `strategies-tried.md` with verdict | Stage 2 results reviewed; claims either supported or marked unsupported | $0, software-director builds, no keys typed by agents |
| 3. Paper-trade log | Hand ledger or Alpaca paper multi-leg orders, one underlying, one spread, monthly, same rules, logged against the frozen design. No real orders | At least 12 monthly cycles or a Zac-set smaller bar, and a QA pass on the ledger | $0 |
| 4. Zac's gate | Real account at $500 is Zac's own event. Level 3 approval, collateral rules and fees read from Robinhood's own pages first. Any live step is Zac's call in his own config | Zac only | his money |

Stage 2 and 3 conflict with nothing in the stock watch week, but each needs a separate frozen config file under the new folder so that the watcher's config hash is unaffected.

## Glossary (my words)

- BPS, bull put spread: sell a put, buy a cheaper lower put, keep the credit if the index stays above the sold strike.
- ROP and ROC: sell a put below the price you would happily buy at, sell a call above the price you would happily sell at.
- RC: spread minus credit, the money at risk per share.
- RORC: credit over risk capital. ARORC: RORC scaled to a year by 365 over days held (a headline rate, not a forecast).
- Probability OTM: the broker's estimate that the option expires worthless.

## Not verified

- Every document claim in this brief.
- Screenshots inside the RUT presentation, the NEW Options Matrix content, and image-only slides in the Fin Statements and Credit Spreads decks.
- The sticker price and MOS formulas (not in the documents).
- Fee per contract, Robinhood collateral for spreads, RUT bid-ask, Alpaca support for RUT index options, how far back Alpaca stock bars go, ThinkOrSwim paper account availability today, Alpaca's historical quotes for the free feed beyond the doc statement.
- Any independent evidence on Rule One options results.

## Open decisions queued (logs\DECISIONS.md)

TRADING-2026-11-26-29 to 31, see the log. (Section (c) cites 'Decision 29' for the sticker price formula.)
