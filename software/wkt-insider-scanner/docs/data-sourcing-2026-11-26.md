# Data sourcing: WKT insider scanner (SEC Form 4, code P clusters)
Read 2026-11-26 by data-sourcing. Docs pages only, no SEC data endpoint called. openinsider.com not used. `Investing\research\insider-data-terms-2026-11-26.md` did not exist, nothing to defer to.
Not legal advice. Cost: free. Credentials: none.

## 1. SEC fair access
Source: https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data (also https://www.sec.gov/os/accessing-edgar-data), retrieved 2026-11-26.
- Rate: "Current max request rate: 10 requests/second." SEC "reserves the right to limit request rates."
- User-Agent: must declare one. Sample format on the page: `Sample Company Name AdminContact@<sample company domain>.com` (company or app name plus a contact email). Use a generic app name and a role mailbox the owner chooses, not a personal name. Also shows Accept-Encoding and Host headers.
- Violation behavior: page does NOT mention 403 or 429 and does not describe blocks or IP bans. It says out-of-policy requests "will be managed." Observed 403/429 behavior: NOT VERIFIED (not tested, no bulk calls made).
- Hosts: sample header shows www.sec.gov; JSON served from data.sec.gov. efts.sec.gov is not mentioned on the page (full-text search is linked at www.sec.gov/edgar/search/). Treat efts as NOT VERIFIED, and do not use it.
- Automation: "The SEC does not allow botnets or automated tools to crawl the site." Asks for efficient scripting, "download only what you need," moderate requests. No technical support. robots.txt not mentioned (NOT VERIFIED).
- Read: a polite single-threaded script with a declared UA, throttled well under 10/s (suggest 2/s), is consistent with the page. Whether a scheduled scanner counts as a "crawler" is a judgment call for Zac, queue if unsure.

## 2. Routes compared (open-market P by 3+ insiders at one issuer)
(a) Insider Transactions Data Sets, https://www.sec.gov/data-research/sec-markets-data/insider-transactions-data-sets (retrieved 2026-11-26; layout from https://www.sec.gov/files/insider_transactions_readme.pdf, retrieved, text extracted).
- URL: `https://www.sec.gov/files/structureddata/data/insider-transactions-data-sets/{YEAR}q{N}_form345.zip` (e.g. 2025q4_form345.zip). The 2026 Q2 and Q3 zips sit under `/files/datastandardsinnovation/data/insider-transactions-data-sets/` instead. Check the page for the link each time.
- Cadence: quarterly; coverage 2006 to 2026 Q3. Filings after 5:30 PM ET on the last business day of a quarter roll to the next posting. Lag: up to about 3 months, so it is HISTORY and backtest data, not a live signal.
- Size: about 7 to 16 MB per quarter zip. Eight tab-delimited UTF-8 files plus a W3C metadata file.
- Tables and keys: SUBMISSION (ACCESSION_NUMBER), REPORTINGOWNER (ACCESSION_NUMBER, RPTOWNERCIK), NONDERIV_TRANS (ACCESSION_NUMBER, NONDERIV_TRANS_SK), NONDERIV_HOLDING, DERIV_TRANS, DERIV_HOLDING, FOOTNOTES, OWNER_SIGNATURE.
- SUBMISSION columns: ACCESSION_NUMBER, FILING_DATE, PERIOD_OF_REPORT, DATE_OF_ORIG_SUB, NO_SECURITIES_OWNED, NOT_SUBJECT_SEC16, FORM3_HOLDING_REPORTED, FORM4_TRANS_REPORTED, DOCUMENT_TYPE (4 vs 4/A), ISSUERCIK, ISSUERNAME, ISSUERTRADINGSYMBOL, REMARKS. Page says AFF10B5ONE was added to SUBMISSION for the 2023 to 2025 sets in July 2025 (not in the readme I extracted; exact column header NOT VERIFIED, read it from a real file).
- REPORTINGOWNER: ACCESSION_NUMBER, RPTOWNERCIK, RPTOWNERNAME, RPTOWNER_RELATIONSHIP (text such as OFFICER, DIRECTOR, TENPERCENTOWNER, OTHER, so no separate boolean flags), RPTOWNER_TITLE, RPTOWNER_TXT, address fields, FILE_NUMBER.
- NONDERIV_TRANS: ACCESSION_NUMBER, NONDERIV_TRANS_SK, SECURITY_TITLE, TRANS_DATE, DEEMED_EXECUTION_DATE, TRANS_FORM_TYPE, TRANS_CODE, EQUITY_SWAP_INVOLVED, TRANS_TIMELINESS, TRANS_SHARES, TRANS_PRICEPERSHARE, TRANS_ACQUIRED_DISP_CD, SHRS_OWND_FOLWNG_TRANS (post-transaction shares), VALU_OWND_FOLWNG_TRANS, DIRECT_INDIRECT_OWNERSHIP, NATURE_OF_OWNERSHIP, each with a _FN footnote id column.
- NOT in the data set: SIC code, issuer-level SIC, a per-transaction 10b5-1 flag (only the submission-level AFF10B5ONE; pre-2023 plans appear only in FOOTNOTES text). Filing date is in SUBMISSION, transaction date in NONDERIV_TRANS.
- Request load: 1 request per quarter. Lowest load. Use for backtest and for the cluster definition.

(b) Daily index + each Form 4 XML. Index dir linked from the fair-access page: https://www.sec.gov/Archives/edgar/daily-index/ (retrieved link only; file naming, form-index layout and publish time NOT VERIFIED, no file fetched). Full-index dir also linked: /Archives/edgar/full-index/. Form 4 volume is high (hundreds to thousands a day), each needs its own fetch: load is 1 plus N requests per day, highest of the live routes.

(c) getcurrent Atom feed (browse-edgar action=getcurrent, "Latest Filings"): link seen on the fair-access page only. Atom params, page size, lag and terms NOT VERIFIED. Near-live, but only the latest window, still needs per-filing XML fetches, and misses anything if a poll is skipped.

(d) data.sec.gov submissions API: https://www.sec.gov/search-filings/edgar-application-programming-interfaces (retrieved 2026-11-26). `https://data.sec.gov/submissions/CIK##########.json` (10-digit CIK, leading zeros), no key, no CORS, updated under a second typically. Gives name, former names, exchanges, tickers; recent filings (at least 1 year or 1,000) as columnar arrays, older in extra files. One request per issuer or insider CIK. Good for a targeted lookup of one issuer's recent Form 4 list, not for market-wide discovery. No rate figure given on that page beyond the 10/s policy.
Bulk alternative: `https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip`, republished nightly about 3:00 AM ET (size NOT VERIFIED, likely large, not fetched).

Lowest request load by use: (a) for history; for near-live, (c) or daily index to list new Form 4 accession numbers, then fetch only filings that pass a cheap filter, with (d) per issuer only after a cluster candidate appears. Best combo: a) backtest, then daily list plus XML for live.

Form 4 XML elements to parse. Official spec: Ownership XML Technical Specification v5.5 (18 Mar 2026), https://www.sec.gov/files/edgar/filer-information/specifications/ownershipxmltechspec-v5-5.zip, listed at https://www.sec.gov/edgar/filer-information/current-edgar-technical-specifications (retrieved). I did NOT open the zip. v5.5 added issuerForeignTradingSymbol, rptOwnerNonUSAddressFlag, rptOwnerNonUSStateTerritory, rptOwnerCountry (retrieved from that page). A draft v5.6 dated 2026-11-06 exists. The names below are from the SEC data sets readme (which cites nonDerivativeTable) plus your list, otherwise NOT VERIFIED against the spec: ownershipDocument, documentType (4 vs 4/A), issuer (issuerCik, issuerName, issuerTradingSymbol), reportingOwner (reportingOwnerId/rptOwnerCik, reportingOwnerRelationship: isDirector, isOfficer, isTenPercentOwner, isOther, officerTitle), nonDerivativeTable/nonDerivativeTransaction (transactionDate, transactionCoding/transactionCode, transactionAmounts shares and pricePerShare and acquiredDisposedCode, postTransactionAmounts/sharesOwnedFollowingTransaction). 10b5-1 indicator element name since the 2023 change: believed `aff10b5One` (matches the data set's AFF10B5ONE column), NOT VERIFIED in the schema. Action: unzip v5.5 into its own empty folder and read the .xsd before coding.

## 3. Allowlist hosts
- www.sec.gov (data set zips, Archives, daily-index, getcurrent, docs). Fair-access page uses this host.
- data.sec.gov (submissions API).
- efts.sec.gov: NOT needed, not documented here, leave off.
- Redirects to other hosts: NOT VERIFIED (no data requests made). One observed: http://www.sec.gov links on the page upgrade to https. Use https only.

## 4. SIC code, low cost
- Not in the Insider data sets (readme shows no SIC field).
- data.sec.gov submissions JSON: an unofficial third-party OpenAPI listing (apis.io) shows `sicDescription` next to name and tickers; the SEC page itself does not name `sic`. NOT VERIFIED from SEC. Cost: 1 request per issuer, cache forever (SIC rarely changes). Alternative: submissions.zip bulk (one download, all CIKs, fields not checked). Check one real response before relying on it.

## Gaps for the build owner
403/429 behavior, daily-index file format, getcurrent params, exact XML names, AFF10B5ONE column header, SIC field name: each marked above. Next step: one small, throttled test with the declared UA after Zac approves the UA string.
