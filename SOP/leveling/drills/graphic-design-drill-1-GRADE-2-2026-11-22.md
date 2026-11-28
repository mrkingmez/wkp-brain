# Grade 2: graphic-design drill 1, attempt 2

Signed: qa-director (independent grader, not the author), 2026-11-22. Attempt 1 grade kept at `graphic-design-drill-1-GRADE-2026-11-22.md`.
VERDICT: FAIL, close. Part A 5 of 7 (needs 6 of 7 with A1, A5, A6 passing; A5 still fails). Part B 6 of 6, PASS. Both parts must pass. Attempt 1 fixes 1, 2, 5, 6, 7, 8, 10 and 11 are genuinely done. What blocks is evidence quality: tags that point at the wrong evidence, and one quote I cannot trace.

Ran: lint on run 2 myself (7 of 7 PASS, exit 0, matches author's file); read all three edited checklists and the brief C1 edits; compared start-frame and PROVEN citations against the log folders and LESSONS.md; tried to re-fetch A2 (Adobe page returns a 438 byte shell by curl, so A2 is NOT re-verifiable by me).

## Part A
| ID | Result | One-line proof |
|---|---|---|
| A1 CRITICAL | PASS | Lint R1 0 hits on all four video prompts; no unwanted thing named. |
| A2 | PASS (note) | Garage 4 is wrench only, head turn split into 4b, garage 7 is turn only, F16 one-hand rule applied. Garage 11 still reads bend, grasp, lift (three verbs, called "one reach"); allowed by STANDARD R6 but arguably not one action. |
| A3 | PASS (narrow) | How each start frame is made is now stated, tier stated. BUT garage 4 and 7 point at "the existing still in the Video 4 / Video 7 log folder". Those folders hold only the .mp4 and notes.txt, no still (checked on disk). Say "export the first frame of the clip with ffmpeg" or find the original still; as written the card names a file that is not there. |
| A4 | FAIL | Only garage 4 gives a quote, and it does not support the term: "Some advanced camera angles are not officially supported." says nothing about "static" being a camera term (SOURCES G1 has no verbatim "static" quote). Garage 7 and 11 give camera terms ("Static camera at floor level", "Static camera") with no quote or id at all. |
| A5 CRITICAL | FAIL | No credit number, and "PROVEN-ish" is gone (good). Still failing: (a) false PROVEN citation, line 24: "wrench turning a wrench when two hands held tools, garage 6 and 7 in Video 6, video 7". LESSONS F16 puts that failure in garage 2 and 3; garage 6 and 7 show a second person and second wrench (I viewed the video 7 sheet). (b) Line 82: "PROVEN: F3 logos drawn wrong 2 of 2" is used to justify putting art in a wall-art mat; F3 is about a Veo logo start frame and LESSONS calls it "Partly PROVEN", so it does not prove this. (c) Line 70 puts "to generate a photorealistic image instead of an illustration" in quotation marks as an A2 quote; it appears in no saved source (SOURCES A2 says only "Content type Photo or illustration", the brief paraphrases), and the page cannot be re-fetched, so the quote is invalid under SOP part 1. (d) Untagged instructions remain: "Dust drifts in warm light" (4, 4b, 7), "left hand rests open on his chest" (7, close to the garage 1 failure shape), "Static camera." and the bend and lift wording (11), the Part B prompt bodies. (e) Line 10 repeats Luma's "~70% cheaper" cost figure (COMMUNITY, labeled, not a credit number, but an unretrieved cost claim). |
| A6 CRITICAL | PASS | All prompts carry a cheapest test (4 s draft, 720p), credit "NOT RETRIEVED", Zac reads at Generate. Durations now match (4 s, no ranges). |
| A7 | PASS | Predicts known failures on 4, 7, 11. Weak evidence, as disclosed. |
Part A: 5 of 7. FAIL.

## Part B
| ID | Result | One-line proof |
|---|---|---|
| B1c CRITICAL | PASS | No negation words in any main prompt, lint 0 FAIL. |
| B2c | PASS | All three now run subject, setting, style, colour, lighting, lighting last; 58, 79, 56 words. |
| B3c CRITICAL | PASS | No text, logo or numeral requested; overlay zones are plain sky or plain plain; overlay named as code or Express. |
| B4c | PASS | E1 and Y1 verbatim (verified live last round), Y1 3840 x 2160 added, Meta NOT RETRIEVED, output size NOT VERIFIED. |
| B5c | PASS (note) | C1 full reply now quoted with the "[avoid=xxx]" sentence, tagged COMMUNITY, UNTESTED, with a one-try test for Zac; brief updated (lines 29, 46). The A2 "photorealistic" quote problem sits here too. |
| B6c | PASS | Fallback and one-change retry for each. |
Part B: 6 of 6. PASS.

## Checklists (edited)
| File | Items | Usable? |
|---|---|---|
| graphic-design-firefly-image-prompt-card.md | 11 | Yes. Item 3 now matches Adobe's labels and the prompts; item 6 has a concrete proof (every bullet starting with a panel verb ends in a bracket tag). |
| graphic-design-firefly-video-prompt-card.md | 12 | Yes. Item 12 is now checkable on the card. |
| graphic-design-redo-plan.md | 9 | Yes. Items 8 and 9 reduced to what is checkable on the card. |
Run 2 pastes the checklists but ticks without the one-line proof SOP part 4 asks for, and some ticks are wrong: video item 11 (tags) ticked while A5 above fails; item 4 "provenance ticked for all four" while two named stills do not exist. The UNDRILLED line is present (good).

## What the author must fix for attempt 3 (nothing else needs changing)
1. Correct the line 24 PROVEN: cite garage 2 and 3 (LESSONS F16, log folders `Video 2`, `Video 3`), or tag it PROPOSED.
2. Retag line 82 (art in the mat) as PROPOSED with the cheapest test, or cite two actual logged results for a still with composited art.
3. Remove the quotation marks on the A2 "photorealistic" line and paraphrase it as unverified, or paste the retrieved text with a saved retrieval note.
4. Tag every remaining untagged instruction (dust and light lines, left hand on chest, camera sentence on 7 and 11, bend and lift on 11), or delete the ones that are not needed.
5. A4: write a verbatim maker quote with id beside the camera term on every card, or say the maker page gives no verbatim quote for "static" and tag it PROPOSED; drop or retag "at floor level".
6. Fix start-frame provenance: say "export the first frame of the .mp4 in the log folder" (ffmpeg), or locate the original stills; do not name stills that are not there.
7. Drop the "~70% cheaper" figure or keep it out of the run file.
8. Tick the checklists with a one-line proof each, and only after items 1 to 7.
Minor: garage 11 is three verbs; consider "he reaches down and lifts the baseball" only if the test shows it works.

Not verified by me: G1 to G4, A1 to A3, K1, R2, L1, F3, F4 quotes (small-model fetch text, no raw page); A2 quote (page not fetchable by curl).
