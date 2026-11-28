# Gap audit: music

Date 2026-11-22. Auditor: the music agent (self-audit, the grader signs the drill, not this). Brief: `memory\agents\briefs\music-craft-brief.md`. Checked each licence claim in four outputs against the pages I retrieved today.

## Outputs audited (all on disk, paths read today)
1. `D:\WKP\Post-Production\reports\Ian-Wrench-Turner-Trailer-Draft3-3.md`, music appendix (lines 966 to 1041, plus lines 29, 250, 312, 584, 592).
2. `D:\WKP\WWD\reports\A-Knights-Tale-Sound-Plan.md` (lines 73 and 74, music options).
3. `D:\WKP\reports\2026-11-20-ElevenLabs-Month-Plan.md` (music rights rows 8 to 11, section 5).
4. `D:\WKP\data\assets\music-catalog.md` and `.csv` (header columns, `source_guess`).

## Findings per output

### 1. Ian trailer, Pixabay "Ambient" pick
- GOOD, verified today: the three Pixabay summary quotes, the track page licence line, "Content ID Registered", no AI label, 2:04 length and 2026-04-01 date all match the pages I retrieved (receipts file). It says plainly "READ ONLINE TODAY, but NOT on disk" and keeps the owned track as rough-cut only. It correctly keeps ElevenLabs music out ("Individual Use Only question open").
- GAP A: the licence claim rests on the SUMMARY page. That page itself says "only the full Content License is legally binding." The doc never cites the full terms. Cost: the question "does it cover Ian posting?" (lines 250, 592) stayed open when the terms page (Section 11 and the Content License wording "for commercial or non-commercial purposes") was one fetch away. It still does not answer the third-party handoff, but it should have been read.
- GAP B: the mitigation "file a dispute citing the Pixabay license" has no retrieved source. I did not retrieve YouTube's dispute page either. The Content ID help I retrieved says a claim can block, monetize or track. The doc says "annoying, not fatal" without saying blocks are one of the three outcomes. Cost: Zac could face a blocked launch video and the doc undersold it.
- GAP C: Pixabay terms Section 11 ("have to stop using the Content immediately, at your own expense") is not mentioned. No swap track is named on the same cue times for a takedown. (The doc does say swap `searching-for-hope`, but that track has no licence, so the fallback is weaker than stated.)

### 2. A Knight's Tale sound plan
- GAP D (biggest by reach): line 74 says the Adobe rock loops under `P:\Sounds\Music\adobe\Funk&Rock1\` are "license-clear (Adobe SFX library is OK per Zac)". The page I retrieved (Adobe free sound effects) covers sound effects ("Audition's sound effects are always royalty-free"). It does not mention music loops. The claim rests on Zac's statement and on a different library. Tag it UNPROVEN until the Adobe loop licence is read. The plan did flag "license files not on disk" for the other two owned tracks, which is correct.
- Not a gap: the plan says it did not pick for Zac and that Suno is lapsed, not used. Fine.

### 3. ElevenLabs month plan
- GOOD, verified today: Section 1.5 (rights stay with the plan at creation) exists on `https://elevenlabs.io/music-terms` (the old URL `eleven-music-model-specific-terms` redirects there, curl 200). Exhibit A matches: Creator "For Individual Use Only", media rights "except film, TV, radio, and Studio Games", Free "Required (denote Eleven Music when distributing)". The "Individual Use is not defined" claim is correct: the saved Music Terms text defines only the table cell.
- GAP E: the plan recommends a paid month ($11) before the Individual Use answer. It does say ask support first and keep the fallback, but the A1 generation (about 450 credits) for WWD runs before the answer comes back (the table says "Ask the question first" only for the Ian and client rows). For WWD, the LLC is Matt's and Zac is the account holder, same open question. Cost if wrong: credits and a month for output that may not be cleared. Fix: queue the question as a gate for every row, not just Ian.
- GAP F: the plan's SFX licensing row says "SFX-specific terms page: not retrieved". Correctly honest. Still open.

### 4. Catalog
- The catalog gives `source_guess` per file ("Storyblocks-style ID suffix (plan proof not on disk)", "unknown"). Honest: no licence column claims clearance. 
- GAP G: it has no licence-proof column and no loudness column, so a reader can still assume "owned" means "cleared". The spec says say "owned, license unproven" but the catalog does not carry it per row. Cost: the sound plan's loop claim (GAP D) came from that blur.
- The Main Channel Theme row exists (line 75, 117.2 s), so the 2026-11-19 miss is fixed.

## Where a licence claim rested on memory or a person instead of a retrieved page
- Adobe loops "license-clear" (Sound Plan line 74): Zac's statement, wrong library. UNPROVEN.
- Spec line "Zac's plan has lapsed, so a Suno track is not clear until he renews": written from third-party summaries, and the Suno ToS I retrieved says rights on a permitted Download are perpetual after cancellation. The line is right only for new tracks. Spec and `music-reference.md` need an edit (the reference file is mine, I edit it; the spec belongs to my director).
- "Content ID can still flag AI music" in the spec: not found in any retrieved page.
- "Adobe SFX library is free to use" (TASKS, Ian packet): now SOURCED for sound effects by the Adobe page quote, still not for loops.

## Top 3 gaps by cost
1. GAP D (Adobe loops called licence-clear from a different library plus Zac's word). If a loop ships in a WWD upload and the loop pack is not covered, the claim risk lands on a public video. Fix: read the loop pack licence or label loops "owned, license unproven" in every pick.
2. GAP A and C together (summary page, no Section 11, no swap on cue times). Fix: pick card requires the terms page quote and a named swap track with the same cut points.
3. GAP E (spend before the Individual Use answer for WWD rows). Fix: pre-flight item on the ElevenLabs request: "the Individual Use answer is in writing, or this is for a fallback-only test with an owned cut ready, and Zac sees the cost".
(GAP B, the undersold claim outcome, is folded into the Content ID line in the pick card.)

## Not verified
I did not open the Ian Appendix E steps against a browser. I did not re-measure any audio. I did not retrieve YouTube's dispute page.
