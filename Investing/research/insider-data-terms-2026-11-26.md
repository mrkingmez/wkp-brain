# Insider-purchase data: SEC access terms, Form 4 facts, evidence (2026-11-26)

For: trading-director (Fawn Forest Investments). Author: trading-researcher. Read-only research, nothing was run against EDGAR, nothing placed, no keys. Not advice. All dates read 2026-11-26.

## Plain answer
- An automated SEC pull is allowed at up to 10 requests per second, with a declared User-Agent. The SEC says "We allow scripted access to sec.gov content" but "does not allow botnets or automated tools to crawl the site." Stay far under the cap (our need is a few requests a day).
- The best low-load route for "3+ insiders bought at one issuer" is the SEC Insider Transactions Data Sets (quarterly ZIP, 1 download a quarter), plus data.sec.gov submissions JSON for the daily top-up. Quarterly alone is too stale for a live scanner (lag below).
- User-Agent: SEC asks for a company name and a contact email. Zac must supply it himself, in an environment variable, never in the repo or in anything I write. DECISION to queue for trading-director (see end).
- OpenInsider: terms and robots.txt NOT RETRIEVED. No bypass attempted. Treat as not allowed to automate until read. We do not need it, because SEC data has the same Form 4 facts.

## Q1 SEC EDGAR fair access
| Item | What the page says | Source | Read |
|---|---|---|---|
| Rate limit | "Note that our current maximum access rate is 10 requests per second." Also "SEC reserves the right to limit request rates to preserve fair access for all users." | https://www.sec.gov/about/webmaster-frequently-asked-questions ; https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data | 2026-11-26 |
| User-Agent | Asks you to "declare your user agent in request headers". Sample value: "Sample Company Name AdminContact@<sample company domain>.com" (company name plus admin contact email), also Accept-Encoding gzip, deflate, and Host header | same two pages | 2026-11-26 |
| Violation | No penalty text found on either page. Two errors named: "Undeclared Automated Tool" (no declared user agent) and "Access Denied" (contact webmaster@sec.gov with error text and IP). "Internet Security Policy" (privacy.htm#security) NOT READ | same | 2026-11-26 |
| Crawling | "The SEC does not allow botnets or automated tools to crawl the site." Scripted access to content is allowed; "we do not offer technical support to programmatically download filings" | same | 2026-11-26 |

### Endpoints, ranked for our need (3+ distinct insiders, code P, role, transaction date vs filing date)
| Rank | Route | What retrieved sources say | Fit |
|---|---|---|---|
| 1 | Insider Transactions Data Sets (quarterly ZIP of Forms 3, 4, 5) https://www.sec.gov/data-research/sec-markets-data/insider-transactions-data-sets | Quarterly ZIPs Jan 2006 through Sept 2026 listed (2026 Q3 file 8.26 MB). "The data sets will be updated quarterly." Filings after 5:30 PM ET on a quarter's last business day go in the next quarter's posting. Extracted from the XML, "flattened", "without change from the as-filed submissions". July 2025 update added AFF10B5ONE to the SUBMISSION file. Table definitions are in a separate PDF (not read, my fetch got binary). | Best for the clustering history and backtest: one download per quarter, tiny load. Lag: up to about a quarter plus posting delay (exact posting delay after quarter end NOT RETRIEVED). Not for live alerts. |
| 2 | data.sec.gov submissions JSON (per company) | "Submissions by company and extracted XBRL data are available via RESTful APIs on data.sec.gov" (JSON). Limits are the same 10 per second. Per-filing XML still has to be fetched to read the transaction rows. | Good for a daily top-up on a short watchlist, not for market-wide discovery. |
| 3 | Latest filings feed (Atom "getcurrent") | The FAQ points to "Latest Filings and its associated RSS feed" for near-real-time. Feed details (parameters, entries per call) NOT RETRIEVED. | The only near-real-time discovery route. Poll rarely, one request per poll. |
| 4 | Daily and quarterly index files | "Indexes to all public filings are available from 1994Q3 through the present." Index lists filings by form type, not the transactions. | Finds Form 4 filings per day, but each one still needs its own XML fetch (thousands per day). Heavier than route 1. Use only to know which filings exist. |

Suggested low-load design (a suggestion, not tested): backfill from the quarterly ZIPs for the test, then a once-daily pass over index or feed entries for Form 4 filed that day, fetching only filings for issuers on our watchlist. Total well under 1 request per second.

## Q2 OpenInsider
- http://openinsider.com/robots.txt and the https version: connection refused (ECONNREFUSED, retried both). NOT RETRIEVED.
- Web search for a terms or scraping policy: nothing from OpenInsider found; results were about other sites. NOT RETRIEVED.
- Verdict: unknown. No header or user-agent tricks tried (locked rule). Recommend not using it for automation. It is only a re-presentation of SEC filings, which we can read directly.

## Q3 Form 4 facts (source: SEC Form 4 and General Instructions, SEC 1474 (03-26), https://www.sec.gov/about/forms/form4.pdf ; also https://www.sec.gov/files/form4data,0.pdf ; read 2026-11-26 by extracting the PDF text locally, so wording is as extracted)
| Item | What the form says |
|---|---|
| Code P | "Open market or private purchase of non-derivative or derivative security". Note: private purchases are also P, so P is not purely open market. |
| Code S | "Open market or private sale of non-derivative or derivative security" |
| Code A | "Grant, award or other acquisition pursuant to Rule 16b-3(d)" (company-issued, not an investment decision) |
| Code M | "Exercise or conversion of derivative security exempted pursuant to Rule 16b-3" (a separate code covers non-exempt exercises, not read) |
| Code F | "Payment of exercise price or tax liability by delivering or withholding securities incident to the receipt, exercise or vesting of a security" |
| Other | Code J for unlisted transactions. Code V flag = "Transaction voluntarily reported earlier than required". |
| Tables | Codes go in "Table I, Column 3 and Table II, Column 4". Table I holds non-derivative securities (common stock), Table II holds derivative securities (options, warrants). Only Table I code P rows count for a stock buy signal. A derivative P (Table II) is a different thing. |
| Deadline | Filed "before the end of the second business day following the day on which a transaction ... has been executed". So transaction date and filing date differ by up to 2 business days (late filings exist). |
| 10b5-1 | General Instruction 10: "Indicate by check mark whether a transaction was made pursuant to a contract, instruction or written plan for the purchase or sale of equity securities of the issuer that is intended to satisfy the affirmative defense conditions of Rule 10b5-1(c)". Adoption date goes in "Explanation of Responses". A planned buy is scheduled, so arguably less informative; that is our inference, not an SEC statement. |
| Relationship | Form box 5: "Director", "Officer (give title below)", "10% Owner", "Other (specify below)". Several can be ticked at once. XML element names isDirector, isOfficer, isTenPercentOwner, isOther: only isDirector and isOfficer confirmed (older spec v3, https://www.sec.gov/files/info/edgar/ownershipxmltechspec-v3.pdf). isTenPercentOwner, isOther and aff10b5One NOT confirmed from a primary page; current spec is v5.5 (March 18, 2026) at https://www.sec.gov/edgar/filer/technical-specifications, not downloaded. |
| Joint filings | "such owners may file Form 4 individually or jointly. Joint and group filings may be made by any designated beneficial owner." Box 6 "Form filed by More than One Reporting Person". One filing then has several reporting owners, so counting "distinct insiders" must count reporting owners, not filings, and must not double count the same insider across a joint filing and an individual one. Indirect holdings (trusts, family) can make one person appear as an entity. |
| Amendments | Box 4 "If Amendment, Date Original Filed". General Instruction on amendments: an amendment may "add one or more lines of transaction information to Table I or Table II". So a 4/A can add rows or restate; a parser must dedupe against the original. Full amend semantics NOT fully read. |

## Q4 Published evidence (published findings, not our result; no promise of return)
| Paper | Claim as stated | Effect size as stated | Caveats | Link |
|---|---|---|---|---|
| Lakonishok and Lee 2001, "Are Insider Trades Informative?", Review of Financial Studies 14(1) 79-111, data 1975-95 | Insiders are contrarians and "appear able to predict individual stock returns", with the predictive value from purchases, not sales. Little price movement around trade or report date. | Numeric effect NOT RETRIEVED (abstract summary only, no full text) | Concentrated in smaller firms | https://econpapers.repec.org/RePEc:oup:rfinst:v:14:y:2001:i:1:p:79-111 |
| Jeng, Metrick, Zeckhauser 2003, "Estimating the Returns to Insider Trading", Rev Econ Stat 85(2) 453-471 | Insider purchases earn abnormal returns; sales do not | Purchases "more than 6% per year" (abstract, via search summary). Working paper version: about 25 percent of abnormal return in first 5 days, half in first month. Earlier NBER version about 40 bp per month. Returns are for insiders' own trades (value-weighted, assumes trading at the transaction date) | Insider portfolio, not an outsider who sees the filing 2 days later; top execs did not earn more than other insiders | https://econpapers.repec.org/RePEc:tpr:restat:v:85:y:2003:i:2:p:453-471 ; https://www.nber.org/papers/w6913 |
| Cohen, Malloy, Pomorski 2012, "Decoding Inside Information", Journal of Finance 67(3) 1009-1043, data 1986-2007 | Split trades into routine (same calendar month for years) and opportunistic. Opportunistic trades carry the predictive power; routine are about zero. Routine are over half of trades | Opportunistic portfolio: value-weighted 82 bp per month abnormal (NBER digest); equal-weighted 180 bp per month (AQR summary). Whether the published version matches the working paper NOT confirmed | Those figures are before costs; the sample ends 2007 | https://www.nber.org/papers/w16454 ; https://hbswk.hbs.edu/item/decoding-inside-information |

Notes and what we could not verify:
- I read abstracts and summaries, not full papers. Clusters specifically (3+ insiders): none of the three summaries retrieved reports a cluster-only effect size. CLUSTER EFFECT SIZE NOT RETRIEVED.
- Caveats for our case: effects are strongest in small firms where spreads and fills are worst; no study retrieved here nets out trading costs for an outsider; return decay after publication and survivorship were not checked in these sources; all samples end by 2007 or earlier, so current relevance is untested. Our $60 account can buy only fractional or 1 to 2 shares; Robinhood stock routing was covered in the earlier brief.
- The "opportunistic" filter needs several years of each insider's history, which the quarterly sets (back to 2006) can supply.

## Risk notes
- Scraping or misdeclaring a User-Agent risks an SEC block ("Access Denied"). No penalty text retrieved.
- A code P row is a fact about a filing, not a signal of future price. Test on the paper ledger first.

## What trading-director could test on paper
1. Backfill 2023 to 2026 quarterly ZIPs, count distinct reporting owners with code P in Table I per issuer in a 10 or 30 day window, exclude 10b5-1 rows, record transaction date and filing date, then track forward returns from the filing date (not the transaction date).
2. Compare with and without the opportunistic filter. One change at a time.
3. Report fills and spreads with the watcher's measured quotes, small caps especially.

## Not verified
OpenInsider terms; SEC Internet Security Policy; Atom feed parameters; Form 345 table-definition PDF; full-text papers; cluster-only effects; posting delay of the quarterly set; XML element names beyond isDirector and isOfficer.

## Decision to queue
Zac supplies the SEC User-Agent company name and contact email himself, stored as an environment variable on his machine (suggest name SEC_USER_AGENT, value in his own config only). No agent types or stores it. Until he does, no live SEC calls.
