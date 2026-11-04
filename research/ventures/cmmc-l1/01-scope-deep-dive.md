# CMMC Level 1 starter kit: scope deep dive (research only)

Date: 2026-11-03. Author: venture-scout. Nothing built, nothing listed, nobody contacted, no accounts made.
Parent file: `D:\WKP\research\ventures\2026-10-26 venture scout first scan.md` (idea 1).
Not legal advice. Sources are cited inline. Anything I could not open is marked "not verified".

## 0. Bottom line up front

1. The regulatory driver is real but smaller and slower than the first scan implied. Phase 2 (the Nov 10, 2026 date I flagged) was suspended July 13, 2026. Level 1 is Phase 1 and was NOT paused. So the thing that scared people toward certification is on hold, while the thing Zac would sell for (Level 1 self-assessment plus annual SPRS affirmation) is still in force.
2. The "paperwork" part of Level 1 is already free and good. DoD's Project Spectrum, state APEX Accelerators, Secureframe's Level 1 kit, and Security Scientist's free policy template all cover it. Paid competitors sit at $12.99 to $269. This is a crowded, low-price niche, not an open gap.
3. The real pain I found is not the 15 practices. It is the plumbing: SAM.gov CAGE code, PIEE vendor group set up by phone with the help desk, getting the "SPRS Cyber Vendor" role approved, naming an Affirming Official. A step-by-step on that is the one angle where I did not find a clean free competitor. Not verified as unserved.
4. Demand is not proven from the buyer side. I found no buyer complaint threads (Reddit not retrievable) and no sales numbers for any competitor. The only hard demand number is a DoD estimate of how many small entities will be Level 1.
5. My honest read: marginal. Worth a one-weekend demand test, not a build.

## 1. What Level 1 actually requires

### The rule stack
- Contract clause: 48 CFR 52.204-21, Basic Safeguarding of Covered Contractor Information Systems (Nov 2021). Fetched at [acquisition.gov](https://www.acquisition.gov/far/52.204-21). Paragraph (b)(1) lists 15 requirements (i to xv).
- CMMC program rule: 32 CFR Part 170. Level 1 is defined at 170.15; affirmation at 170.22. Fetched via the eCFR API (2026-10-01 snapshot). 170.14(c)(2) says Level 1 requirements are "those set forth in 48 CFR 52.204-21(b)(1)(i) through (xv)".
- Contract insertion: DFARS rule, Federal Register Sept 10, 2025, [govinfo](https://www.govinfo.gov/content/pkg/FR-2025-09-10/html/2025-17359.htm). Effective Nov 10, 2025. Clauses 252.204-7021 (flows down to subs) and provision 252.204-7025. The program office, not the contracting officer, picks the required level. Last 25k characters of that page not read.

### The 15 practices (FAR 52.204-21(b)(1), short form, verified from the clause text)
1. Limit system access to authorized users
2. Limit access to the types of transactions and functions users may perform
3. Verify and control connections to external systems
4. Control information posted on publicly accessible systems
5. Identify users, processes, devices
6. Authenticate those identities
7. Sanitize or destroy media containing FCI
8. Limit physical access to systems and equipment
9. Escort visitors and monitor visitor activity
10. Monitor, control, protect communications at boundaries
11. Subnetworks for publicly accessible components
12. Identify, report, correct system flaws in a timely manner
13. Protection from malicious code
14. Update malicious code protection
15. Periodic scans and real-time scans of files from external sources

Count discrepancy: sources say 15 requirements, 17 NIST SP 800-171 controls, and 59 assessment objectives. Greenberg Traurig says 15 requirements "align with 17 controls in NIST SP 800-171 rev. 2" and the assessment uses 800-171A objectives with FCI substituted for CUI ([GT Law](https://www.gtlaw.com/en/insights/2025/10/recapping-cmmc-level-1-considerations-for-government-contractors)). Secureframe says 15 requirements and 59 objectives ([kit page](https://secureframe.com/cmmc-level-1-compliance-kit)). Security Scientist's page says "17 practices". Anyone who sells must state the 15 / 17 / 59 split correctly. Official DoD Level 1 Assessment Guide: not verified (dodcio.defense.gov returned 403 to me).

### What a tiny contractor must produce (32 CFR 170.15 and 170.22, eCFR text)
- A self-assessment against NIST SP 800-171A objectives. Every requirement must be MET. No POA&Ms allowed at Level 1.
- Repeat every year.
- Report in SPRS: CMMC level, status date, assessment scope, all associated CAGE codes, compliance result.
- An affirmation in SPRS by the Affirming Official (senior person responsible for compliance with authority to affirm). Content: name, title, contact, plus a statement that the organization "has implemented and will maintain implementation of all applicable CMMC security requirements" across the scoped systems. Affirm at completion and annually.
- Keep evidence artifacts six years from the status date.
- Level 1 asks for no formal written policy set by name. Policies and an informal system description are what people produce as evidence. The rule text I read requires MET objectives and evidence, not a specific document list. Treat a "required document list" as not verified.

### SPRS plumbing (from SPRS/vendor guides, not the official PDFs, which I did not open)
- SAM.gov registration gives a UEID and CAGE code; the Electronic Business POC must match the PIEE user.
- PIEE help desk must add the CAGE code to a vendor group before anyone can self-register; then someone gets the "SPRS Cyber Vendor" role approved by the Contractor Administrator.
- Official guide: [SPRS CMMC Quick Entry Guide](https://www.sprs.csd.disa.mil/pdf/CMMCQuickEntryGuide.pdf) (listed in search, not opened). Tutorials at sprs.csd.disa.mil/nistsp.htm (not opened).
- SAM hierarchy errors show up in SPRS, per the same search results.

### Cost context
DoD's own estimate: about $5,977 per small entity per year for Level 1 assessment plus affirmation, $4,042 other than small (secondary sources, search result; GT Law says "about $6,000" / "about $4,000"). Affirmation alone $560 small / $584 other (GT Law). Excludes implementation cost. Primary Federal Register figure not verified (federalregister.gov redirect blocked me). The rule's own paperwork burden figure is 5 minutes per system for SPRS entry and affirmation (govinfo DFARS text), which tells you how DoD thinks of the effort versus what a tiny firm experiences.

### Who is and is not covered
- Applies when contractor systems process, store or transmit FCI. FCI excludes public info and simple transactional data (GT Law).
- Search results state COTS-only sellers and contracts at or under the micro-purchase threshold ($10,000) are outside CMMC (Ohio APEX presentation summary). Verify against the DFARS text before ever writing it into a product.
- DFARS text says by Year 4 offerors need "a minimum of a CMMC Level 1 self-assessment" or the level the solicitation states.

## 2. Current status, with dates

| Date | Event | Source |
|---|---|---|
| Oct 15, 2024 | 32 CFR 170 final rule published (89 FR 83092) | search summary; Federal Register page blocked, not verified firsthand |
| Nov 10, 2025 | DFARS rule effective; Phase 1 begins (self-assessments Level 1 and 2) | govinfo Sept 10, 2025 DFARS notice, fetched |
| Jul 13, 2026 | DoW suspends Phase 2 (C3PAO Level 2, DIBCAC Level 3 requirements) and creates CMMC Reform Task Force, 60 day review. Phase 2 had been due Nov 10, 2026 | DWT law blog Jul 16, 2026 ([link](https://www.dwt.com/blogs/privacy--security-law-blog/2026/07/department-of-defense-suspends-cmmc-phase-ii)); Crowell ([link](https://www.crowell.com/en/insights/client-alerts/department-of-war-immediately-suspends-cmmc-phase-ii-requirements-launches-60-day-reform-review)) |
| Jul 14, 2026 | Implementing memo 26-P-1023: remove Level 2 C3PAO and Level 3 from solicitations and contracts at next option or admin mod | Crowell; memo PDF 403, not read |
| Aug 14, 2026 | RFI comments closed, about 1,100 responses | search summary of Secureframe, secondary |
| Sep 3, 2026 | Class Deviation 2026-O0025 Rev 3 carries the pause into contract text; Level 1 and 2 self-assessments are the accepted path | Secureframe news page (secondary) |
| Sep 11, 2026 | 60 day review window closed; report promised, no date | Secureframe (secondary) |
| Oct 27, 2026 | Federal News Network reported unofficial restart options (narrower Phase 2 in about 90 days, 270 day POA&M, Rev 3). Deliberative, not decisions | Secureframe (secondary) |
| Latest I can see | Official task force report still unreleased. Nothing after Oct 27 retrieved | not verified past Oct 27 |

What still applies (Crowell, DWT, Secureframe agree): Phase 1 Level 1 and Level 2 self-assessments, DFARS 252.204-7012, NIST 800-171 Rev 2, SPRS affirmations, False Claims Act exposure, prime flowdown. Level 1 specifically: no Level 1 change reported in Sept or Oct.

Official URLs I could not open (403 or blocked) and need a human browser check: dodcio.defense.gov/cmmc/about, the war.gov suspension release (4542329), the war.gov change release (4542849), memo 26-P-1023 PDF, federalregister.gov. DoD CIO "Phase 1 ran Nov 10, 2025 to Nov 9, 2026" is from the first scan's search summaries, not re-verified here.

Implication for the venture: the statement "Phase 2 is two weeks away" in the first scan is wrong. Nov 10, 2026 is now just the date when nothing changes unless the task force publishes. The restart scenario, a narrower Phase 2, would mostly drive Level 2 interest, not Level 1. Level 1 demand depends on how many solicitations actually carry the clause, which no source counted (search found no number).

Market size claim: DFARS notice estimates 142,487 small entities at Level 1 self and 209,540 total in a Year 4+ snapshot, mix "likely to change" (govinfo, fetched). Rule-wide estimate about 337,968 entities, 229,818 small (search summary). These are DoD planning estimates of covered entities, not buyers or searches.

## 3. What the product line could be

All of this is a design map, nothing is drafted. Competitor prices below are what I saw listed; none had sales numbers.

### Competitor map (what exists)
| Competitor | Where | Price seen | Notes |
|---|---|---|---|
| Project Spectrum (DoD) | projectspectrum.io | Free | Free Level 1 and 2 courses and assessments, advisors, per DoD small business office ([business.defense.gov](https://business.defense.gov/Resources/Be-Cyber-Smart/)). Not opened firsthand. |
| State APEX Accelerators | Kentucky, Ohio, Washington (Snohomish), Alabama | Free | Level 1 workshops and cohorts (search summary). Cannot do the work for the firm. |
| Secureframe Level 1 kit | secureframe.com | Appears free, may be email-gated (not stated) | Guide, checklist (15 req / 59 objectives), evidence spreadsheet, public info policy. Opened. |
| Security Scientist | templates.securityscientist.net | $12.99 per Word template, $7.99 XLSX, $249 for 731-template library, 3 free downloads | Has a Level 1 FCI Safeguarding Policy template. Says "do not resell". Opened. |
| Sentinelle | Gumroad (link was a placeholder when I looked) | $59 | L1+L2+800-53+SOC2 pack plus a free in-browser scorer. Opened. Possibly a stub. |
| TalonPoint | Payhip | $149 (6 templates), $269 (12 templates) | From first scan, not reopened. |
| ComplianceForge | own site | $5,344 Level 1 bundle | From first scan, not reopened. |
| Fiverr gig | Fiverr | not verified | From first scan. |
| Etsy | none seen in one search | not verified | Zero results is not a count. Needs a manual Etsy search. |

### Possible tiers (hypothetical)
| Tier | Contents | Price idea | Format | Build effort | Maintenance |
|---|---|---|---|---|---|
| Free lead magnet | "Level 1 in 15 questions" plain-English checklist | $0 | PDF | 3 to 5 hr | Low, rule is stable |
| Core kit | Scorer workbook (15 requirements / objectives, MET or NOT MET, evidence tracker, scope sheet), FCI identification worksheet, short policy set | $39 to $79 | .xlsx + .docx | 15 to 25 hr | Annual refresh, plus whenever Rev 3 or the rule changes |
| Plumbing guide | SAM.gov to CAGE to PIEE to SPRS to affirmation walk-through with screenshots and a "who is my Affirming Official" page | $19 to $39 standalone or inside core kit | PDF | 8 to 12 hr, but screenshots need a real account and Zac must not mock them | HIGH: screens change. I must not create accounts, so Zac would do this himself |
| Annual refresh | Re-do reminder, updated forms | $9 to $19 or free to buyers | file update | 2 hr/yr | |
| Upsells (higher risk) | Done-for-you review, "pre-affirmation check call" | not priced | service | n/a | This is where liability and the day-job conflict bite hardest. Not recommended without counsel. |
| Level 2 adjacent | NIST 800-171 SSP/POA&M pack | n/a | n/a | big | Competitive and paused-uncertain. Out of scope. |

Opinion: a $39 to $79 scorer is only defensible if it adds what Secureframe's free kit does not, and I have not seen an apples-to-apples comparison of the Secureframe workbook versus a new one. Plumbing guide is the only differentiator I can name, and it is the one with a maintenance cost and a "Zac must click through it himself" cost.

## 4. Legal and compliance guardrails (list of what to check, not advice)

Required stance for any product: "Not legal advice. Not a certification. Not a guarantee of passing anything." That wording is mine; whether a disclaimer limits liability was NOT answered by any source I found.

What the sources support:
- Level 1 is self-assessed. No third party certifies it. A seller cannot "certify" anyone and must not use the word "certified" for the buyer's status. ([GT Law](https://www.gtlaw.com/en/insights/2025/10/recapping-cmmc-level-1-considerations-for-government-contractors), 32 CFR 170.15.)
- The affirmation is personal and legal. Search summaries say the Affirming Official cannot delegate to IT and carries personal accountability; DOJ's Civil Cyber-Fraud Initiative uses the False Claims Act, with seven cybersecurity FCA settlements in 2025 per one source. Secondary only. Holland & Knight has a Jan 23, 2026 piece called "CMMC affirmation trap, FCA exposure" ([link](https://www.hklaw.com/en/insights/publications/2026/01/cmmc-affirmation-trap-fca-exposure)), not opened.
- A kit that says "you pass" when the buyer's real environment does not match is the obvious risk. One vendor blog argues assessors compare policy to configuration (search summary). So a template cannot honestly promise a pass.
- RPO / Registered Practitioner: RPOs and RPs are consulting-only, cannot perform assessments, and are bound to the Cyber AB Code of Professional Conduct. A consultant and an assessor of the same company conflict ([Smithers](https://www.smithers.com/resources/2026/april/why-can-t-a-cmmc-assessor-offer-consultation-servi), [Secureframe RPO](https://secureframe.com/blog/cmmc-rpo), secondary). Primary Cyber AB text not retrieved (cyberab.org page was nav only). Whether anyone may sell Level 1 templates without being an RP or RPO: nothing I found says it is forbidden; no source stated it is permitted either. Not verified. Also not verified: Cyber AB rules on logo and trademark use and on describing yourself as "CMMC" something. Do not use Cyber AB, DoD, or CMMC logos without checking.
- Reseller licensing: Security Scientist's terms bar resale. Do not copy or lightly rewrite anyone's template. Any DoD or NIST text used must be checked for reuse terms (NIST publications are generally public; not verified here).
- Platform terms: Payhip and Gumroad accept digital documents. Each has terms on regulated advice; not verified.
- Sales tax and entity: separate WKP question (LLC research is already in TASKS.md). A cyber document seller with no entity is exposed personally.
- Insurance: whether $0 budget can include professional liability cover: not verified, probably no.

Day-job conflict checklist (do NOT assume the answer; queued as DECISIONS VENTURE-2026-11-03-01):
1. Employment agreement: any clause on outside business, moonlighting, or conflicts of interest.
2. Whether outside work needs written approval or HR/ethics disclosure, even if unpaid or tiny.
3. Whether the employer is a DoD contractor, a subcontractor, a CMMC assessor, a managed service provider, or a consultancy. If so, selling CMMC prep to that employer's competitors or customers may conflict.
4. IP ownership: any assignment of work product related to the employer's field, even made on personal time and equipment.
5. Use of any knowledge gained at the day job (client info, internal methods) in the product. Must be zero.
6. Whether the job holds a clearance or has contract terms barring commercial advice in the field.
7. Whether CySA+ study materials or exam terms limit use of that credential in marketing. Check CompTIA terms before ever putting "CySA+" on a listing.
8. Does the employer's social media or public-speaking policy cover posting in LinkedIn groups?

## 5. Distribution: where tiny defense subs actually look

Verified in search (secondary unless noted):
- APEX Accelerators (formerly PTAC) run free Level 1 workshops: Kentucky, Washington (Snohomish), Alabama (UAH ACCESS), Ohio. They are a competitor and also a channel. They cannot do the work for the firm, which leaves room for tools. Georgia APEX: not looked up. Needs a lookup.
- SBA hosts "CMMC Level 1 for Small Businesses" and "Live Q&A: A Practical Approach to CMMC Level 1" events ([SBA event 80798](https://www.sba.gov/event/80798), [74682](https://www.sba.gov/event/74682)); pages redirect, details not opened. SBA's Office of Advocacy filed an Aug 14, 2026 RFI comment letter ([PDF](https://advocacy.sba.gov/wp-content/uploads/2026/08/Comment-Letter-Reforming-CMMC-and-Reducing-Compliance-Burden-081426.pdf)), a sign of small-business pressure; not opened.
- NAVOBA ran a Project Spectrum webinar for veteran-owned businesses ([link](https://www.navoba.org/project-spectrum-webinar-helps-veteran-owned-businesses-navigate-cmmc-compliance)). Date and attendance not verified. This proves veteran business groups host CMMC content, which means (a) there is audience and (b) free competition is already in the room.
- Payhip and Gumroad: competitors already listed (table above). Etsy: none seen in one search; not a B2B buyer venue.
- Prime supplier pages: Lockheed Martin has a cyber quick reference guide for suppliers (listed in search, not opened). Primes sending flowdown notices create "I got an email, now what" moments. L3Harris and Elbit are named in Secureframe for supplier notices.

Not verified at all, but plausible places to look by hand (Zac or a later run):
- Reddit r/CMMC and r/govcon, LinkedIn groups for veteran contractors, SDVOSB and VOSB owners (VetCert), Georgia APEX Accelerator events, Augusta and Fort Eisenhower small business events, Georgia Tech MEP / GaMEP. Search volume for "CMMC Level 1 template": not retrievable (no keyword tool access). Reddit threads: none retrieved.

## 6. Work breakdown (free only)

| Step | Task | Hours | Cost | Who |
|---|---|---|---|---|
| 0 | Day-job conflict check (section 4) | 1 to 2 | $0 | Zac |
| 1 | Manual demand check: Etsy, Gumroad, Payhip, Google, Reddit searches, write real counts | 1.5 | $0 | Zac or a later scout run |
| 2 | Read Secureframe kit, Project Spectrum Level 1 materials and DoD Level 1 Assessment Guide end to end; list gaps | 3 | $0 | agent |
| 3 | Open official PDFs blocked to me (SPRS quick entry guide, war.gov releases, memo 26-P-1023) and confirm status | 1 | $0 | Zac (browser) |
| 4 | Lead magnet: 1-page checklist | 3 to 5 | $0 | not started, needs Zac's go |
| 5 | Post to 2 to 3 veteran business groups, measure replies for 14 days | 1 plus 14 days | $0 | Zac |
| 6 | If 5 passes: core kit build | 15 to 25 | $0 | agent + Zac review |
| 7 | Plumbing guide with real screenshots | 8 to 12 | $0 (needs Zac's SAM/PIEE access or a willing owner) | Zac |
| 8 | Listing, store, terms page, disclaimer | 3 to 4 | $0 (Payhip/Gumroad free tiers; fees per sale, rates not verified) | Zac |
| 9 | Annual refresh | 2 per year | $0 | agent |
Totals: steps 0 to 5 are roughly 10 to 14 hours and $0. Full build to first sale about 35 to 50 hours. Time to first dollar: unknown; the first scan's 3 to 8 weeks is a guess I cannot back.

Where the bottleneck is: Zac's clicks (steps 0, 3, 5, 7, 8). The agent cannot create accounts, contact anyone, or post.

## 7. Risks and kill criteria

Risks, ranked:
1. Free competition is strong and official (Project Spectrum, APEX, Secureframe, Security Scientist). Paying $39 to $79 needs a reason that a free kit does not give.
2. Demand is not demonstrated. Level 1 clause usage in solicitations is uncounted. A small contractor may ignore Level 1 until a prime or contracting officer forces it.
3. Regulatory flux: pause, possible restart, Rev 3, FAR CUI rule (re-proposed June 23, 2026, finalization intended by year end per Secureframe). Level 1 itself looks stable because it equals FAR 52.204-21, but marketing copy can age.
4. Liability: FCA exposure sits with the buyer, but a kit that implies "follow this and you are compliant" invites blame. Guardrails help, certainty unknown.
5. Day-job conflict (section 4).
6. Plumbing guide maintenance and the need for a real SAM/PIEE walk-through.
7. B2B discovery: buyers search and are found via LinkedIn, groups, and primes, not marketplaces. Marketplace search traffic unverified.
8. Platform: low (Payhip/Gumroad). Etsy not recommended.

Kill criteria (set now so they are not negotiated later):
- Day-job check says no or unclear and Zac will not seek written OK: stop.
- Step 1 shows 10 or more established sellers at $39 to $79 with visible reviews, or a free kit that already includes a scorer plus plumbing: stop.
- Step 5: fewer than 10 real replies or email signups in 14 days from the lead magnet across at least 2 audiences: stop. (The threshold is my suggestion; Zac may move it.)
- Official task force output drops or narrows Level 1 (for example exempts FCI-only firms): stop and re-scope.
- More than 40 hours spent before a first paid sale: stop.
- Any counsel or Cyber AB source says unaccredited sellers may not do this: stop.

## 8. Opinion

Do steps 0 to 2 first (about 6 hours, $0, mostly reading and a policy check). They answer the three questions that decide this: may Zac do it, is the niche already filled, and does anything beat the free kits. I would not start the lead magnet before step 1 because the competitive landscape looks worse than the first scan said. If the plumbing guide is still unserved after step 2, that is the only angle I would build around, priced low or bundled, and I would treat the 15-practice scorer as table stakes, not the product.

## Decisions queued
- VENTURE-2026-11-03-01 in `D:\WKP\logs\DECISIONS.md`: Zac checks day-job conflict before any build or public sale.

## Sources not opened or blocked (need human browser)
dodcio.defense.gov/cmmc/about (403), war.gov releases (403), dodcio memo 26-P-1023 PDF (403), federalregister.gov (redirect), cyberab.org RPO pages (nav only), SPRS Quick Entry Guide (listed, not opened), SBA events (redirected).
