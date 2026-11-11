# Legal transcription as a niche
Date: 2026-11-10. Read-only desk research. Nothing signed up, posted, or spent.
Labels: OBSERVED = read on the page this session. SECONDARY = vendor blog, aggregator, or search summary. NOT AVAILABLE = looked, did not find. INFERRED = my reasoning.
Warning: almost every legal transcription source is a vendor selling transcription. Treat their numbers and fear language as leads, not facts.

## Verdict first
Legal is worth a careful pilot, but only the uncertified lane, and not on the marketplaces. The prior brief lumped legal with medical. That was too broad. Legal has no HIPAA style law that blocks a freelancer, and the core uncertified work (dictation, interviews, recorded statements) is real and pays more than general work. The catch is not certification. It is confidentiality and the cloud AI step. Zac keeps Whisper local, which helps. Claude proofreading sends client words out, and that is the part a law office would object to.

Safeguards that make it viable: local-only pipeline with no Claude step on client text (or written client consent), signed NDA, never touch anything labeled "official" or "certified," disclose machine draft plus human check, and clear the day job question first.

## 1. Pay, legal versus general
| Item | Figure | Label and source |
|---|---|---|
| Rev legal transcriptionist role | 0.55 to 2.00+ per audio minute | OBSERVED, https://www.rev.com/freelancers/transcription |
| Rev general transcription, same page | 0.40 to 1.10 per audio minute | OBSERVED, prior brief, same URL |
| Agency price to a legal client, simple audio (one-on-one interviews, dictation, narratives), Ditto | 1.75 standard, 2.25 rush, 1.50 extended turnaround, per audio minute | OBSERVED, https://www.dittotranscripts.com/?p=1165 |
| Agency price, hard audio (3+ speakers, noise, court hearings, depositions), Ditto | 3.00 standard, 5.00 rush, 2.50 extended, per audio minute | OBSERVED, same page |
| Ditto order minimums | 100 dollars standard, 150 rush | OBSERVED, same page |
| Verbatim and timestamp add ons, Ditto | verbatim plus 0.25, timestamps plus 0.25 or 0.50 per minute | OBSERVED, same page |
| Freelancer pay for legal, per audio minute | 1.25 to 2.50 | SECONDARY, WealthVieu via search summary |
| Freelance legal per hour | 20 to 45 dollars, per-page common for court work | SECONDARY, https://www.transcribeanywhere.com/blog/how-much-do-transcriptionists-make-2026 |
| Glassdoor legal transcriptionist average | about 61,151 per year, about 29 per hour | SECONDARY, same article. Legal runs about 8,500 per year above general |
| Verbit legal freelance posting | NOT AVAILABLE (page returned 404 this session) | prior brief had SECONDARY 0.75 to 0.95 |

Reading it: legal pays roughly 1.5 to 2 times general at the same company on the page ceiling (Rev 2.00+ vs 1.10), and direct-to-firm prices (1.50 to 3.00 for common audio) sit at or above Zac's earlier 1.25 per minute pilot price. Ditto shows the price is driven by speaker count and noise, not by the word "legal."
INFERRED: a new freelancer with no legal references will land near the low end of these ranges. The Rev top range targets people with legal experience, which Zac does not have (his degrees are criminal justice and political science, which helps credibility but is not experience).
Effective hourly: legal audio has more speaker overlap and terminology, so my earlier 1 to 1.5 working hours per audio hour is optimistic for legal. One source says 3 to 4 working hours per audio hour for professionals on clean audio (SECONDARY, search summary). With Whisper that number should fall, but Zac must time a real file. NOT AVAILABLE: any retrieved dollars per working hour for an AI-assisted legal transcriber.

## 2. Uncertified work versus certified or court reporter work
General US norms (SECONDARY, vendor sources, jurisdictions vary):
- Legal transcriptionists generally need no mandatory credential. Court reporters hold certifications and often notary status. Court reporter transcripts carry evidentiary weight. Whether a transcriptionist's work counts depends on the court's rules. Source: search summary of https://uslegalsupport.com/blog/legal-transcriptionist-vs-court-reporter and https://www.gmrtranscription.com/blog/transcriptionist-vs-court-reporter
- Typical uncertified transcriptionist work: recorded statements, police body cam and jail calls, dictated legal notes. Same sources. Ditto's own page lists dictation, client meetings and interviews as simple category work, depositions as hard category (OBSERVED, URL in section 1).
- Credential that exists: AAERT certification for digital court reporters and transcribers. SECONDARY, career guide summaries. Not required for general legal transcription.

Georgia specifics (SECONDARY to OBSERVED, from search results of Georgia Judicial Council and Board of Court Reporting pages, not read in full):
- Felony criminal cases require an official transcript (O.C.G.A. 5-6-41, cited by the Georgia Supreme Court). Civil cases generally do not require a court reporter or official transcript.
- The Board of Court Reporting position is that Georgia law requires a certified court reporter (or temporary permit holder) to certify a transcript, with a signed certificate that it is true, complete and correct. Where digital recording is used, a certified reporter must be available to transcribe it if a written transcript is required. Sources: https://ocp.georgiacourts.gov/?p=238 , https://ocp.georgiacourts.gov/wp-content/uploads/2020/06/BCR-Advisory-Opinions.pdf , https://codes.findlaw.com/ga/title-15-courts/ga-code-sect-15-14-5/ (results only, statute text not verified against current O.C.G.A.).
- NOT AVAILABLE: any Georgia source that says in plain words that a non-certified person may transcribe a private recorded statement or dictation. The inference that this is fine comes from the court reporter rules covering official proceeding transcripts, not private audio. INFERRED, and worth a one-line check with the Board of Court Reporting or a Georgia attorney before the first paid job.

Practical split for Zac (INFERRED from the above):
- Do: attorney dictation, client interviews, internal meeting audio, recorded statements for the firm's own use, investigator interviews.
- Do not: depositions, hearings, anything to be filed as an official transcript, anything the client wants "certified" or notarized.
- Be careful: audio that is later used as an exhibit. Ask the client at intake whether it will be filed anywhere.

## 3. Confidentiality, privilege, NDA, cloud AI
- Lawyers owe confidentiality (Model Rule 1.6) and must supervise nonlawyer helpers (Rule 5.3). ABA Formal Opinion 512 (29 July 2024) says a lawyer should not put confidential client information into a generative AI tool without adequate protection, and client consent can be part of the analysis. It does not ban any tool. ABA opinions are persuasive, not binding, and states differ. Source: SECONDARY summary at https://www.leanlaw.co/blog/ai-confidentiality-and-the-firms-money-what-aba-opinion-512-actually-requires/ (original opinion not read). Georgia State Bar position: NOT AVAILABLE, not searched.
- The same summary lists three vendor questions a firm should answer: does the tool train on inputs, where is data stored, who can access it. A public consumer AI tool that trains on user data can itself breach Rule 1.6.
- Vendor guidance (SECONDARY, sales content): NDA should define confidential information, permitted use, return and destruction. Ask about data location, breach notice timelines, retention periods. For AI-enabled vendors, a written agreement that restricts use to the engagement and prohibits training or sharing. Sources: https://gotranscript.com/en/blog/transcription-vendor-nda-security-questionnaire-template-legal , https://gotranscript.com/en/blog/legal-ethics-checklist-ai-transcription-confidentiality-waiver-best-practices , https://www.attorneyatwork.com/ai-transcription-confidentiality-lawyers/
- SOC 2 reports are mentioned as a common firm request for cloud-hosted transcripts. A solo freelancer will not have one. CJIS comes up for criminal justice information (criminal defense files, police audio). NOT verified from the FBI. INFERRED: skip anything holding CJI.
- Claim that the wrong vendor can waive privilege came from one unsourced vendor line. Unverified, do not rely on it.
- Is sending audio to a cloud AI accepted? NOT AVAILABLE as a settled rule. Best reading: acceptable only with the client's informed consent or a vendor that contractually does not train and isolates data, and many firms will say no. INFERRED: a local-only pipeline is a selling point. "Your audio never leaves my computer" is a real differentiator against Rev and similar.
- Consequence for Zac's workflow: Whisper local is fine. Claude proofreading of client text is the exposure. Options: (a) human proof only, no Claude on client text, (b) Claude only with written client consent, (c) local model proofing. Under (a) the working hours per audio hour go up and the hourly drops. Zac must time it.

## 4. Accuracy, format and turnaround buyers expect
- Accuracy: 99 percent is the claim most vendors make (Ditto states 99 percent, OBSERVED at the Ditto URL). That is a marketing number, not a standard. A 95 percent test pass appears for GoTranscript (prior brief, SECONDARY).
- Format: verbatim versus cleaned is an explicit choice and costs extra (Ditto: verbatim plus 0.25 per minute). Speaker labels and timestamps are standard options. Court-style page and line formatting is a separate court reporter product, NOT AVAILABLE as a requirement for private statements.
- Turnaround tiers on one OBSERVED rate card: rush 1 to 2 business days, standard 3 to 5, extended 6 to 10. Rush costs about 30 percent more on simple audio, 67 percent more on hard audio (my arithmetic from the Ditto numbers). Zac's 24 to 48 hour offer sits in the rush tier. He should charge for it.
- Speaker identification: Zac's pipeline gives Guest or Unknown labels, needs hand mapping. Legal buyers will expect named speakers.

## 5. Where legal buyers hire small transcribers
SECONDARY, career blogs, treat as leads. https://www.transcribeanywhere.com/blog/i-can-type-can-t-you-just-tell-me-how-to-get-clients , https://www.lilachbullock.com/legal-transcription-jobs/
- Referrals, professional directories and direct outreach. Legal buyers are relationship driven.
- Court reporting agencies that need scopists and proofreaders. Needs court reporting software skills, not Zac's skill set (INFERRED).
- Transcription companies (Rev, Verbit, Escribers, TranscribeMe). Their AI and tool rules are NOT AVAILABLE, and Verbit supplies its own ASR draft, so Zac's edge is lost there.
- AAERT and NCRA job boards. Mostly certified reporter roles.
- Upwork and Fiverr. An Upwork posting for a "Certified Legal Transcript Specialist" appeared in results, i.e. buyers there often ask for certification.
- NOT AVAILABLE: anything specific to solo or small-firm attorneys (local bar events, small-firm Facebook groups, paralegal associations). INFERRED best targets for Zac: solo and small-firm criminal defense, family law and personal injury attorneys and their paralegals in the Augusta and Aiken area, private investigators, and legal nurse consultants. Needs a small desk test, for example 10 firm websites checked for "outsourced transcription" language, not done.

## 6. Open questions (not answerable from desk research)
1. Day job conflict. UNKNOWN. Zac's day job is in cyber security. Whether outside work touching legal or criminal audio is allowed is open and he already has this question open for outside cyber products. Ask HR or read the outside employment policy before any legal job.
2. Georgia check that private recorded statements and dictation do not need a certified reporter (see section 2).
3. Georgia State Bar view on AI and nonlawyer vendors (not searched).
4. Whether his local Whisper plus human-only proof is fast enough to pay. Needs one timed legal-style file (public-domain audio is fine).
5. Insurance. NOT AVAILABLE. A solo freelancer handling legal audio may want errors and omissions coverage. Not researched, cost unknown.

## Verdict and safeguards
Pursue as a narrow, referral-led niche, after the day job answer, not as the first thing to build.
- Lane: uncertified, private-use audio for solo and small criminal, family and injury firms. No depositions, no hearings, no filed transcripts.
- Price test: 1.75 per audio minute standard, 2.25 for 48 hour, with a 100 dollar order minimum, mirroring the one OBSERVED rate card. Ask the first two buyers what they pay now.
- Pipeline: Whisper local only. Zero client text to Claude unless the client signs consent. Say so in the agreement.
- Paper: simple NDA, return and destroy audio and text after delivery, stated retention, breach notice, no subcontracting.
- Disclose: "machine draft, human verified."
- Do not claim certification, do not offer notarization (Ditto charges 150 dollars flat for it, a sign it needs a notary).
- Not for marketplaces: Rev, GoTranscript and Verbit either supply their own draft or have not said if outside tools are allowed.
- Expectation: higher price per minute than general work, same hard part (finding buyers), slower sales cycle because lawyers vet vendors. INFERRED, low confidence.

Confidence: medium that legal pays more and that the uncertified lane exists. Low on Georgia specifics, low on hourly dollars, low on the AI acceptance question.

## Sources
- Rev freelancers (OBSERVED): https://www.rev.com/freelancers/transcription
- Ditto legal prices (OBSERVED): https://www.dittotranscripts.com/?p=1165
- TranscribeAnywhere pay article (SECONDARY): https://www.transcribeanywhere.com/blog/how-much-do-transcriptionists-make-2026
- Georgia courts and board (search results only): https://ocp.georgiacourts.gov/?p=238 , https://ocp.georgiacourts.gov/wp-content/uploads/2020/06/BCR-Advisory-Opinions.pdf , https://codes.findlaw.com/ga/title-15-courts/ga-code-sect-15-14-5/
- Legal transcription vs court reporting (SECONDARY): https://uslegalsupport.com/blog/legal-transcriptionist-vs-court-reporter , https://www.gmrtranscription.com/blog/transcriptionist-vs-court-reporter , https://www.rev.com/blog/?p=18856
- ABA 512 and AI confidentiality (SECONDARY): https://www.leanlaw.co/blog/ai-confidentiality-and-the-firms-money-what-aba-opinion-512-actually-requires/ , https://www.americanbar.org/groups/litigation/resources/newsletters/ethics-professionalism/generative-ai-lawyers-part-2-maintaining-confidentiality/
- Vendor NDA and security (SECONDARY): https://gotranscript.com/en/blog/transcription-vendor-nda-security-questionnaire-template-legal , https://gotranscript.com/en/blog/legal-ethics-checklist-ai-transcription-confidentiality-waiver-best-practices , https://www.attorneyatwork.com/ai-transcription-confidentiality-lawyers/
- Where buyers hire (SECONDARY): https://www.transcribeanywhere.com/blog/i-can-type-can-t-you-just-tell-me-how-to-get-clients , https://www.lilachbullock.com/legal-transcription-jobs/
- Not fetched or failed: Verbit posting (404), Rev legal-specific page (404), the original ABA Opinion 512, Georgia statute text.
