# CMMC Level 1 starter kit for tiny defense subs: fact brief

Date: 2026-11-03. Requested by: Jarvis / venture review. Nothing is being built. Facts only.
Tags: VERIFIED = read on an official or primary page this session. SECONDARY = law firm, consultancy, or press, not the primary text. UNVERIFIED = not confirmed.

## Access problem, read this first
Every dodcio.defense.gov, war.gov, dowcio.war.gov, media.defense.gov, open.defense.gov and sprs.csd.disa.mil page returned 403 or 404 to my fetch tool. A direct curl attempt was blocked by the permission system and I did not work around it. So the July 2026 DoW release, the implementing memo, the Level 1 Assessment Guide, and the SPRS guides were NOT read by me. Anything about them comes from law firm summaries and search excerpts, tagged SECONDARY. Someone with a browser should open those pages before any money is spent. The regulations (32 CFR 170, FAR 52.204-21, DFARS 252.204-7021, FAR 4.1901, the Sept 2025 Federal Register rule) I did read.

## 1. Answer in plain words
- Phase 2 (November 10, 2026) is suspended, not just paused in rumor. DoW announced it July 13, 2026. Level 1 self-assessment and annual affirmation are NOT suspended. They are the only CMMC level contracting officers can still require right now (some sources say Level 1 or Level 2 self).
- Level 1 is 15 practices from FAR 52.204-21, a self-assessment, six years of evidence kept, and a yearly affirmation in SPRS by a senior person, which carries False Claims Act risk.
- Free official help exists (Project Spectrum, APEX Accelerators, MEP), so a paid kit must beat free on convenience, not on facts.
- Biggest risk to the venture idea is policy: the Reform Task Force report went to the DoW CIO about September 11, 2026 and was still unpublished in the latest reporting I found (October 16, 2026). Level 1 could change.

## 2. The 15 Level 1 practices (FAR 52.204-21(b)(1))

Text of the clause read at https://www.acquisition.gov/far/52.204-21 (VERIFIED, page was paraphrased by my tool for the 15 items, verbatim clause is on the page). CMMC identifier mapping read at https://www.law.cornell.edu/cfr/text/32/170.15 Table 2 (VERIFIED). Objective counts per practice from https://myctrl.tools/frameworks/cmmc-l1-aos (SECONDARY, third party, CC BY 4.0, says 59 objectives total; cross-check against the official guide).

| # | CMMC ID | Plain words | NIST 800-171A map | Objectives (SECONDARY) |
|---|---|---|---|---|
| i | AC.L1-b.1.i | Limit system access to authorized users, processes, devices | 3.1.1 | 6 |
| ii | AC.L1-b.1.ii | Limit access to the transactions and functions users are allowed | 3.1.2 | 2 |
| iii | AC.L1-b.1.iii | Verify and control connections to external systems | 3.1.20 | 6 |
| iv | AC.L1-b.1.iv | Control information posted on public systems | 3.1.22 | 5 |
| v | IA.L1-b.1.v | Identify users, processes, devices | 3.5.1 | 3 |
| vi | IA.L1-b.1.vi | Authenticate them before access | 3.5.2 | 3 |
| vii | MP.L1-b.1.vii | Sanitize or destroy media with FCI before disposal or reuse | 3.8.3 | 2 |
| viii | PE.L1-b.1.viii | Limit physical access to systems and equipment | 3.10.1 | 4 |
| ix | PE.L1-b.1.ix | Escort and monitor visitors, keep physical access logs, manage access devices (one practice, three phrases) | 3.10.3, 3.10.4, 3.10.5 | 6 |
| x | SC.L1-b.1.x | Monitor, control, protect communications at external and key internal boundaries | 3.13.1 | 8 |
| xi | SC.L1-b.1.xi | Separate subnetworks for public-facing components | 3.13.5 | 2 |
| xii | SI.L1-b.1.xii | Find, report, correct flaws in a timely way (patching) | 3.14.1 | 6 |
| xiii | SI.L1-b.1.xiii | Malicious code protection at the right places | 3.14.2 | 2 |
| xiv | SI.L1-b.1.xiv | Update malicious code protection | 3.14.4 | 1 |
| xv | SI.L1-b.1.xv | Periodic scans plus real-time scans of external files | 3.14.5 | 3 |

Note: the eCFR table uses lowercase "b" (AC.L1-b.1.i). Older DoD guides use capitals (AC.L1-B.1.I). Same thing. Some sources say "17 practices" because the three phrases in item ix are listed separately in the NIST mapping (VERIFIED, 170.15 table note).

What an assessor or self-assessor expects as evidence
- Rule text (VERIFIED, 32 CFR 170.15(c)): score using the CMMC Scoring Methodology (170.24); use the objectives in NIST SP 800-171A (June 2018) for the mapped requirement, substituting FCI for CUI; artifacts used as evidence must be retained for six years from the CMMC Status Date.
- Level 1 is scored met or not met. No plan of action is allowed for Level 1 (SECONDARY, Secureframe excerpt: "no SSP, MFA, GCC High, or POA&Ms"; the rule text for POA&M applies to Level 2 and I did not confirm a Level 1 POA&M ban in the rule text. UNVERIFIED in primary).
- Per-practice evidence (examine / interview / test items) is in the DoD CMMC Assessment Guide Level 1, Version 2.13 (September 2024) at open.defense.gov. I could not read it (403). UNVERIFIED for specific evidence items. General pattern per NIST 800-171A is examine documents, interview staff, test the setting. Do not invent per-practice evidence lists from memory in the product. Pull them from the guide.
- Scoping: the Level 1 Scoping Guide is also on open.defense.gov (not read).

## 3. Who must comply, FCI, flow-down
- Applies to all DoD contract and subcontract awardees that process, store, or transmit FCI or CUI on contractor information systems (VERIFIED, 32 CFR 170.3(a)(1), https://www.law.cornell.edu/cfr/text/32/170.3).
- Commercial item acquisitions are covered except those exclusively for COTS items, above the micro-purchase threshold (VERIFIED, 170.3(c), as summarized by my fetch tool; confirm the exact wording).
- FCI definition (VERIFIED, FAR 4.1901, https://www.law.cornell.edu/cfr/text/48/4.1901): "information, not intended for public release, that is provided by or generated for the Government under a contract to develop or deliver a product or service to the Government, but not including information provided by the Government to the public (such as that on public Web sites) or simple transactional information, such as that necessary to process payments."
- Flow-down, FAR (VERIFIED, 52.204-21(c)): include the substance of the clause in subcontracts, including commercial products and services other than COTS, where the sub may have FCI residing in or transiting its system.
- Flow-down, DFARS 252.204-7021 (VERIFIED, https://www.acquisition.gov/dfars/252.204-7021-contractor-compliance-cybersecurity-maturity-model-certification-level-requirements., clause date NOV 2025, page effective date 05/07/2026): primes insert the clause substance in subcontracts that involve FCI or CUI, flow down the correct level, and must ensure the sub has a current CMMC certificate or status before award.
- Federal Register preamble (VERIFIED, https://www.govinfo.gov/content/pkg/FR-2025-09-10/html/2025-17359.htm, published Sept 10, 2025, effective Nov 10, 2025): DoD does not require flow-down to subs that do not receive FCI or CUI; subs comply the same way as primes; subs do not submit CMMC UIDs to the contracting officer; subs must complete the annual affirmation.
- Small-entity note from the same notice: the requirement to post the self-assessment to SPRS prior to award applies to small entities that have a requirement.

## 4. Self-assessment, affirmation, who signs, SPRS
- Eligibility (VERIFIED, 170.15(b)): before award of a contract or subcontract with a Level 1 (Self) requirement, the organization must have achieved Level 1 (Self) status and submitted an affirmation in SPRS for all information systems in the assessment scope.
- Annual (VERIFIED, 170.15(a)(1)): conduct a Level 1 self-assessment annually and submit results in SPRS. Minimum SPRS data: CMMC level, status date, assessment scope, CAGE code(s), compliance result.
- Affirming Official (VERIFIED, 170.4 and 170.22): "the senior level representative from within each Organization Seeking Assessment." Must ensure compliance with CMMC program requirements and have authority to affirm continuing compliance. Attests the organization "has implemented and will maintain implementation of all applicable CMMC security requirements" for the scope. Affirmation includes name, title, contact information.
- When (VERIFIED, 170.22(a)(3) as read via Cornell): on achieving Conditional status, on achieving Final status, annually after Final status date, after a POA&M closeout. DFARS 7021(d)(3) also requires annual affirmation, entered in SPRS per CMMC UID (VERIFIED). The Federal Register preamble adds "or when CMMC compliance status changes occur" (VERIFIED).
- Level 2 (Self) status also satisfies Level 1 for the same scope (VERIFIED, 170.16 text).
- SPRS steps (SECONDARY, search excerpts of the official SPRS Quick Entry Guide, not read): need a PIEE account with the "SPRS Cyber Vendor User" role; in SPRS go to the CMMC Assessments tab, "Add New Level 1 CMMC Self-Assessment"; if the entrant is not the affirming official, the record is passed to the AO; AO name and details come from the AO's PIEE profile and cannot be edited on screen. Official SPRS training exists ("AffirmingOfficialCMMCL1" transcript at sprs.csd.disa.mil; the exact URL I tried returned 404, so locate it on the SPRS training page). Treat exact screen names as UNVERIFIED until someone clicks through. Also pre-requisite items such as a CAGE code and SAM registration are UNVERIFIED here.
- Contracting officer notification: DFARS 7021(e) says CMMC UIDs issued by SPRS go to the contracting officer (VERIFIED). Subs do not (VERIFIED, preamble).

## 5. Phase-in dates and the Phase 2 suspension
Regulatory schedule (VERIFIED, 32 CFR 170.3(e)): four phases, each one calendar year after the prior.
- Phase 1 starts on the effective date of the 48 CFR rule: Level 1 (Self) or Level 2 (Self) as a condition of award.
- Phase 2: adds Level 2 (C3PAO), possibly Level 3.
- Phase 3, Phase 4: later years, full implementation.
- The 48 CFR (DFARS) rule was effective November 10, 2025 (VERIFIED, Federal Register Sept 10, 2025). So Phase 1 = Nov 10, 2025 to Nov 9, 2026, Phase 2 would have been Nov 10, 2026 (SECONDARY for these end-dates; DoD CIO page excerpt said "Phase 1 (Nov 10, 2025 – Nov 9, 2026)", page not read by me).

Suspension
- Date and content (SECONDARY, multiple law firms and a war.gov search excerpt; primary page war.gov article 4542329 returned 403): announced July 13, 2026, signed by DoW CIO Kirsten Davies. Search excerpt of the release: "Effective immediately, the Department will suspend the transition to Phase II requirements of CMMC, as well as pending and future CMMC implementation milestones across the Department of War solicitations and contracts." Davies quote: "...we are today suspending the CMMC Phase II requirements and initiating a 60-day study of the future of this program."
- Primary links to check by hand: https://www.war.gov/News/Releases/Release/Article/4542329/forging-the-arsenal-of-freedom-department-of-war-suspends-cmmc-phase-ii-require/ and the memo https://dowcio.war.gov/Portals/0/Documents/Library/ImplementingSuspensionCMMC-PhaseII.pdf (memo ID 26-P-1023). I did not read either.
- Memo content as reported (SECONDARY, Morgan Lewis https://www.morganlewis.com/pubs/2026/07/department-of-war-suspends-cmmc-phase-ii-requirements-but-cybersecurity-obligations-remain and Crowell): Level 1 (Self) and Level 2 (Self) stay; contracting officers may not require Level 2 (C3PAO) or Level 3 (DIBCAC); no waivers during the review; Phase 3 and 4 on hold; existing solicitations amended as soon as practicable; DFARS 252.204-7012 unchanged. Crowell quotes DoW as saying Phase I self-assessment requirements "remain firmly in place."
- Conflict: BDO (SECONDARY) says the memo limits program offices to Level 1 (Self) only; other sources say Level 1 or Level 2 (Self). Unresolved without the memo.
- Review status: RFI responses were due Aug 14, 2026; Task Force report was due to the CIO September 11, 2026 and not public as of the Sept 21, 2026 post (https://www.insidegovernmentcontracts.com/2026/09/cmmc-reform-task-force-updates-september-2026/, SECONDARY). Latest search summary dated October 16, 2026 said still suspended, no restart date, report unpublished (SECONDARY, search summary, single source). I found nothing newer. Today is Nov 3, 2026, so there is a 2 to 3 week gap.
- Class deviation: Elevate calls it 2026-O0025 Revision 3, dated Sept 3, 2026, telling contracting officers to remove third-party requirements (SECONDARY, https://www.brightdefense.com/?p=17988 and Elevate). An earlier July 29 white paper said no deviation yet. Not verified on an official DPCAP page. UNVERIFIED.
- Net for Nov 10, 2026: nothing official says Phase 2 starts. All found sources say it is suspended with no new date. Verify on the day at https://dodcio.defense.gov/CMMC/.

## 6. Penalties and False Claims Act exposure
- Statute: 31 U.S.C. 3729. "Knowingly" includes actual knowledge, deliberate ignorance, or reckless disregard; no intent to defraud needed (SECONDARY, Holland & Knight, Jan 23, 2026, https://www.hklaw.com/en/insights/publications/2026/01/cmmc-affirmation-trap-fca-exposure). Treble damages plus per-claim penalties. Whistleblower relators can receive 15 to 25 percent (same source, citing 31 U.S.C. 3730).
- Per-claim penalty: $14,308 to $28,619 per claim, DOJ rule effective July 2025, 28 CFR 85.5 (SECONDARY, search summary of Sidley and Federal Register 90 FR 29445). Possibly stale; a later adjustment may exist. UNVERIFIED for 2026.
- The CMMC rule text itself has no FCA or penalty language in 170.22 (VERIFIED by fetch of the section summary; the fetch noted none). The exposure comes from general law. Commentary says the affirming official is personally attesting (SECONDARY). Whether an individual can be personally liable is a lawyer question.
- Cyber-fraud settlements (SECONDARY unless noted): Georgia Tech Research Corporation $875,000, DOJ release Sept 30, 2025, alleged false summary-level assessment score to DoD (VERIFIED on justice.gov; allegations only, no liability determination). MORSECORP $4.6 million, April 2025, alleged false SPRS score reported positive when actual was negative 142 (Holland & Knight; DOJ headline seen in search, body not read). Health Net Federal Services $11.25 million, Raytheon/Nightwing $8.4 million, an Illinois machining subcontractor about $421,000 (first supply-chain case) per Holland & Knight, not independently checked. Search results also listed LOGZONE $507,144 (June 18, 2026), Honeywell Aerospace about $2.04 million and ILC Dover $13 million with an odd date of November 3, 2026 (UNVERIFIED, snippet only).
- DOJ Civil Cyber-Fraud Initiative announced October 6, 2021 (SECONDARY, search summary).
- Disclaimer implication: a template seller does not remove the signer's exposure. The kit should say the signer must verify each practice in their own environment and that the kit is not legal or assessment advice. Have a lawyer write the final wording. I did not find any case where a template vendor was held liable. UNVERIFIED, absence of evidence only.

## 7. Who may sell CMMC advice or templates
- 32 CFR 170 sets up the assessment ecosystem (C3PAO, assessors, Cyber AB). I found NO provision in what I read requiring a business to be an RP or RPO to sell templates, guides or software to the public, and no provision saying DoD requires contractors to use an RPO. This is absence of evidence from search and partial reads, not a confirmed negative. Mark UNVERIFIED and ask counsel.
- Cyber AB RPO and RP program (SECONDARY-high, Cyber AB's own page, https://cyberab.org/CMMC-Ecosystem/Ecosystem-Roles/Consulting-and-Implementation, no updated date, footer 2026): RPO must register with Cyber AB, pass an organizational background check (DUNS), associate at least one RP, sign the Code of Professional Conduct and an RPO agreement. Fees on that page: RPO $6,000 application and $5,000 annual renewal; RP $600 and $500 renewal; RPA $1,000 and $750. RPs and RPOs may use a Cyber AB logo to show they are familiar with the CMMC standard. Fees may be out of date.
- Independence limit on that page: a person holding an RP/RPA designation and an assessor certification cannot assess a company they previously helped implement. That affects assessors, not a Level 1 template seller, since Level 1 is self-assessed.
- Cyber AB is rebuilding the RP, RPA and RPO programs on a roadmap into 2027 (SECONDARY, Secureframe). Requirements may change.
- Not found: trademark or logo limits on using the term "CMMC" in product names. UNVERIFIED. Do not imply DoD or Cyber AB endorsement.
- Not found: any rule that a kit must be "certified". There is no certification of templates that I found.

## 8. Free competitors
- Project Spectrum: DoD funded, no-cost training, assessments and cyber readiness checks for Level 1 and Level 2 (SECONDARY, event flyers and presentations; official site projectspectrum.io not read).
- APEX Accelerators (formerly PTAC): free one-on-one counseling; help deliver Project Spectrum training (SECONDARY; eligibility and services vary by office; one source was a non-official page).
- NIST MEP centers: state-level cyber help for manufacturers, NIST SP 800-171 training in some states, availability varies, may charge (SECONDARY).
- DoD CIO CMMC site: Level 1 Assessment and Scoping Guides, FAQs (a document titled CMMC Level 2 Self Certification FAQs is dated Aug 26, 2026 on media.defense.gov, not read) (SECONDARY, search results).
- SPRS itself has official tutorials for the Level 1 affirming official (SECONDARY, search results).
- Vendor kits already exist, for example Secureframe's Level 1 kit and evidence spreadsheet (SECONDARY, search results). Competition is real.
- Implication: the free guides already cover the facts. A paid product has to win on plain English, done-for-you evidence folders, reminders, and the annual re-affirmation workflow.

## 9. What authors usually get wrong (common misreads)
- "Phase 2 starts Nov 10, 2026." Suspended as of July 13, 2026.
- "CMMC is paused so Level 1 is off." Level 1 self-assessment and affirmation remain in force. The underlying FAR 52.204-21 duty has existed since 2016 regardless.
- "Level 1 needs a third-party assessor." No, self-assessed.
- "Level 1 needs NIST 800-171's 110 controls." No, 15 practices; 110 is Level 2.
- "Any small sub must file in SPRS." Only where a contract or subcontract carries a CMMC requirement or FCI flow-down. The preamble says subs not receiving FCI/CUI need no flow-down.
- "Templates make you compliant." The affirming official attests to actual implementation.

## 10. If a template kit were built (not asked, noted for the director)
Not a recommendation. Just the constraints these facts produce: stale-date risk is high (policy under review), keep a visible "as of" date, route disclaimers to a lawyer, keep the kit tied to the official Assessment Guide wording, and recheck the Task Force outcome before any launch.

## Sources
- FAR 52.204-21: https://www.acquisition.gov/far/52.204-21 (read 2026-11-03)
- DFARS 252.204-7021: https://www.acquisition.gov/dfars/252.204-7021-contractor-compliance-cybersecurity-maturity-model-certification-level-requirements. (read 2026-11-03)
- 32 CFR 170.3, 170.4, 170.15, 170.16, 170.22 via Cornell LII, https://www.law.cornell.edu/cfr/text/32/170.15 and siblings (read 2026-11-03; eCFR itself would not load)
- FAR 4.1901: https://www.law.cornell.edu/cfr/text/48/4.1901
- Federal Register DFARS rule, Sept 10, 2025: https://www.govinfo.gov/content/pkg/FR-2025-09-10/html/2025-17359.htm (first 100,000 of about 125,000 characters read)
- DOJ Georgia Tech release: https://www.justice.gov/opa/pr/georgia-tech-research-corporation-agrees-pay-875000-resolve-civil-cyber-fraud-litigation
- Morgan Lewis, July 2026: https://www.morganlewis.com/pubs/2026/07/department-of-war-suspends-cmmc-phase-ii-requirements-but-cybersecurity-obligations-remain
- Crowell, July 13-14, 2026: https://www.crowell.com/en/insights/client-alerts/department-of-war-immediately-suspends-cmmc-phase-ii-requirements-launches-60-day-reform-review
- Inside Government Contracts, Sept 21, 2026: https://www.insidegovernmentcontracts.com/2026/09/cmmc-reform-task-force-updates-september-2026/
- Holland & Knight, Jan 23, 2026: https://www.hklaw.com/en/insights/publications/2026/01/cmmc-affirmation-trap-fca-exposure
- Cyber AB: https://cyberab.org/CMMC-Ecosystem/Ecosystem-Roles/Consulting-and-Implementation
- myctrl.tools L1 objectives: https://myctrl.tools/frameworks/cmmc-l1-aos
- Bright Defense, updated Oct 4, 2026: https://www.brightdefense.com/?p=17988
- Official pages NOT read (403/404): dodcio.defense.gov/CMMC/, war.gov release 4542329, dowcio.war.gov memo PDF, open.defense.gov Assessment Guide L1 v2.13 and Scoping Guide L1, sprs.csd.disa.mil guides.

## Open questions for the author
1. Can someone open the five unread official pages in a browser and paste the text? That settles the suspension wording, the Level 1 only versus Level 1 and 2 conflict, and the per-practice evidence.
2. Does the venture target subs under a prime's flow-down (prime asks for proof) or direct small prime awardees? The rules differ slightly.
3. Is a lawyer review of disclaimers budgeted? I cannot give legal advice.
4. Re-check the Task Force outcome the day before any decision.
