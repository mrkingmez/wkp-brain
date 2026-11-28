# Craft Brief: studio-director

Written 2026-11-22 by studio-director under `SOP\SOP-Agent-Leveling.md` and `SOP\leveling\studio-director.md`. Review by the director level (Jarvis) still owed. Retrieval method: curl from Bash, text stripped with `scratch\sd-level\strip.py` or `pdftotext`, raw files in `D:\WKP\scratch\sd-level\`. Retrieved dates are all 2026-11-22. Re-retrieve by 2027-02-20 (90 days), sooner if YouTube, the Copyright Office or EBU publish a revision. Versions seen: EBU R 128-2023 (V5), Copyright Office AI report Part 2 dated January 2025.

STATUS: 7 sources retrieved, 0 community. The SOP minimum (5) is met, so the brief is COMPLETE on count. It is thin on one thing the launch file asked for: production-management and delivery-spec pages (Adobe, Netflix, Producers Guild) could not be retrieved, see the NOT RETRIEVED list. This brief covers rights, disclosure, loudness and pipeline gates well, and covers "how a production is run" only through the MovieLabs overview.

## 1. What world-class looks like in this craft

1. A studio head treats the rights picture as part of the package, not a late check: the law has no safe amount, so every borrowed element needs a named owner or a permission on file (S3, S4).
2. Realistic AI content is disclosed at upload, and the disclosure is written into the package as a step with an owner (S1).
3. A claim on a video is a delivery risk to plan for, not a surprise: blocked or monetized by the claimant whatever the poster intended (S2).
4. Anything the package says about who owns the finished work is checked against the rule that prompts alone do not create authorship (S5).
5. A sound target is a number from a published standard, with its measurement named, and it is said whether the number is for broadcast or for a platform (S6).
6. A pipeline is judged by whether work moves from one desk to the next without re-keying and without waiting on a person who is not needed (S7). For us that means one named point man, one asset list, one source of truth per job.
7. Where a source could not be read, the package says NOT RETRIEVED and does not fill the number from memory (SOP-Agent-Leveling part 1; local rule, not a retrieved source).

## 2. Sources

Tags used here: SOURCED (verbatim quote from a page retrieved today). Nothing in this brief is PROVEN yet. PROVEN needs two logged outputs.

### S1. YouTube Help, "Disclosing use of GenAI content"
URL: https://support.google.com/youtube/answer/14328491?hl=en (retrieved 2026-11-22, HTTP 200)
- "We require creators to disclose AI-generated or altered content that seems realistic."
- "Creators don’t need to disclose non-realistic content that’s made with AI, or edits to realistic content that are minor."
- "Creators who consistently choose not to disclose this information may be subject to manual application of a label, or penalties from YouTube, including removal of content or suspension from the YouTube Partner Program."
- "Disclosing AI content alone won’t limit a video’s audience or impact its eligibility to earn money."
Also on the page, listed as must-disclose: "Makes a real person appear to say or do something they didn’t do." and "Generates a realistic scene that didn’t actually occur."

### S2. YouTube Help, "Learn about copyright claims"
URL: https://support.google.com/youtube/answer/6013276?hl=en (retrieved 2026-11-22, HTTP 200)
- "Claimed videos will be blocked if there is an active claim applied, regardless of policy. You will not receive a copyright strike for videos that contain active claims."
- "Copyright claims are different from likeness claims."
- "“Monetize” is the most common policy applied to music claims."

### S3. U.S. Copyright Office, "More Information on Fair Use"
URL: https://www.copyright.gov/fair-use/ (retrieved 2026-11-22, HTTP 200)
- "Courts evaluate fair use claims on a case-by-case basis, and the outcome of any given case depends on a fact-specific inquiry. This means that there is no formula to ensure that a predetermined percentage or amount of a work" (the source continues after a dash; quote cut there to keep this file dash-free) and "may be used without permission."
- "Additionally, “transformative” uses are more likely to be considered fair."

### S4. U.S. Copyright Office, Frequently Asked Questions, fair use and permission
URL: https://www.copyright.gov/help/faq/faq-fairuse.html (retrieved 2026-11-22, HTTP 200)
- "If you use a copyrighted work without authorization, the owner may be entitled to bring an infringement action against you."
- "However, in cases of doubt, the Copyright Office recommends that permission be obtained."

### S5. U.S. Copyright Office, "Copyright and Artificial Intelligence, Part 2: Copyrightability" (report dated January 2025)
URL: https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf (retrieved 2026-11-22, PDF, pdftotext); landing page https://www.copyright.gov/ai/ (HTTP 200)
- "Copyright does not extend to purely AI-generated material, or material where there is insufficient human control over the expressive elements."
- "Based on the functioning of current generally available technology, prompts do not alone provide sufficient control."
- "Human authors are entitled to copyright in their works of authorship that are perceptible in AI-generated outputs, as well as the creative selection, coordination, or arrangement of material in the outputs, or creative modifications of the outputs."

### S6. EBU Recommendation R 128 (2023), "Loudness normalisation and permitted maximum level of audio signals"
URL: https://tech.ebu.ch/docs/r/r128.pdf (retrieved 2026-11-22, PDF, pdftotext; document shows "November 2023", V5)
- "that the Programme Loudness Level shall be normalised to a Target Level of -23.0 LUFS."
- "the True Peak Level of a programme shall not exceed -1 dBTP"
- "The `Maximum True Peak Level' of an audio signal should be used to check compliance with the upper technical limit of the signal chain."
Note: R 128 is a broadcast recommendation. It does not give the -14 LUFS number used in WWD (that is a house platform target, PROPOSED, no source retrieved today).

### S7. MovieLabs, "The 2030 Vision"
URL: https://movielabs.com/production-technology/ (retrieved 2026-11-22, HTTP 200)
- "(replacing repetitive and menial tasks so they can focus on creative tasks)" (fragment of a longer sentence on the page that describes the 2030 Vision as a technology roadmap whose primary focus is empowering creative teams)
- "lays out 10 Principles for a more efficient media pipeline using cloud infrastructure, zero trust security and software-defined workflows."
Weak for our work (a studio-industry roadmap, not a how-to). Kept because it is the one pipeline source retrieved. It supports "remove repetitive hand-offs" and nothing more.

### NOT RETRIEVED (nothing below was summarized from memory)
- NOT RETRIEVED: https://helpx.adobe.com/premiere-pro/using/premiere-pro-project-workflows.html, HTTP 403 (also /team-projects.html, /premiere-pro-collaboration.html 403, /project-manager.html 404)
- NOT RETRIEVED: https://partnerhelp.netflixstudios.com/hc/en-us/articles/360000579527 and the sound mix article 360001794307: HTTP 200 but the body is a JavaScript shell (554 bytes), no text. The Zendesk JSON route returned 404.
- NOT RETRIEVED: https://pixabay.com/service/license-summary/, HTTP 403 (Draft 3.3 says the license was "read online" on 2026-11-20; I could not repeat that read today)
- NOT RETRIEVED: https://cmsimpact.org/code/documentary-filmmakers-statement-of-best-practices-in-fair-use/, connection failed (HTTP 000)
- NOT RETRIEVED: https://www.producersguild.org/page/green, HTTP 404
- NOT RETRIEVED: Adobe Firefly credit rate card (already NOT RETRIEVED in Draft 3.3, 403)
- Circular 21 (https://www.copyright.gov/circs/circ21.pdf) was retrieved but is about educator and library reproduction and the 1976 Act text. Not used as a source here beyond confirming the four factors list.

## 3. What this changes in our work

| # | Change | Source | Tag |
|---|---|---|---|
| 1 | Every package has a Rights table with one row per borrowed element (music, image, name, mark, clip) and a column "permission on file: yes, no, or doubt". A "doubt" row does not ship as cleared; the package says permission is the safe route. | S3, S4 | SOURCED |
| 2 | I do not overrule a clearance STOP on my own say. I record the STOP, the reason it may be wrong, and send the call to Zac as a queued decision unless the item is an own-work item with the owner's yes on file. (Draft 3.3 had me overrule the "Wrench Turner" caption STOP. QA judged it acceptable, but no source gave me the authority.) | S4 | PROPOSED (local rule, S4 supports "ask permission in doubt") |
| 3 | The package has an "AI disclosure" step with two parts: what the platform asks (realistic scenes, real person, altered real footage) and what each shot is (realistic or not). Non-realistic stylized shots are listed as not needing the label so the ask to a client is exact. | S1 | SOURCED |
| 4 | Warn the poster that undisclosed realistic AI can bring a label, penalties or loss of monetization eligibility. Do not claim that disclosing hurts reach or money: the page says it does not. | S1 | SOURCED |
| 5 | Music line in the package states the claim risk: a Content ID claim can block the video even with no strike. "License read" and "no claim possible" are separate lines. | S2 | SOURCED |
| 6 | The package never tells a client that they will own an AI-made trailer outright. It says human selection, arrangement and edits are protectable, raw prompts alone are not. Any ownership line goes to clearance as a flag. | S5 | SOURCED |
| 7 | Loudness line names the standard it comes from. -23 LUFS and -1 dBTP are broadcast (EBU). The WWD -14 LUFS target is a house platform number and is tagged PROPOSED until a platform page is retrieved. | S6 | SOURCED for -23 and -1; PROPOSED for -14 |
| 8 | The "source of truth read" step: before any fence is written, I read the primary story file for the job (Ian: `scratch\ian\wrench-turner-summary.txt`) and quote the lines the fence rests on. No source file, no fence, and the gap is queued. | none retrieved; Ian failure ledger | PROPOSED |
| 9 | Credit plan: every generation row carries "cost: NOT RETRIEVED" until the number is read from the tool's own page or the Generate button. No run count is planned against a balance I have not seen. | local rule, SOP-Agent-Leveling part 7 | PROPOSED |
| 10 | Hand-offs between desks use one asset list and one words-final file as the single source of truth, so a desk never re-keys another desk's output (Draft 3.3 did this well with `words-final`). | S7 (weak) | PROPOSED |

## 4. Open questions the sources did not answer
- Platform-specific loudness target for YouTube and for Instagram or TikTok: not retrieved. Do not state -14 LUFS as a platform rule until a page is.
- Whether Pixabay's license covers a third party (Ian) posting a video the studio made with the track: not retrievable today (403).
- TikTok's and Meta's AI label rules: not retrieved today. Only YouTube's page was read.
- The real Firefly and Veo credit cost per generation: not retrieved.
- What a professional delivery spec asks of a trailer package (Netflix, Adobe): not retrieved.
- Whether a book title in a caption inside the author's own trailer needs any clearance: no source retrieved, S3 and S4 speak only to general fair use and permission. This remains an attorney question, as Draft 3.3 already says.
- How to write a fence from a story that the client has told in two ways (summary versus Zac's reading): no source. Drill 1 tests a proposed method.
