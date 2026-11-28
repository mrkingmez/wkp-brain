# Drill 1: graphic-design (replay plus image prompts)

Written 2026-11-22 by graphic-design BEFORE the run. Grader: qa-director (qa-media for the clip comparison). Not the author. $0, no credits, no generation, nothing posted.

## Disclosure (contamination, stated up front)
The author had already read the AUDIT, LESSONS and the clip notes earlier the same day, so Part A is NOT a blind replay. It tests whether the new STANDARD can be applied to known shots, not whether the author can guess unseen failures. Part B has no result on disk, so it is graded only against the retrieved sources. The grader should weigh criterion A7 with this in mind.

## Part A: video replay, 3 shots with clips on disk
Shots: garage 4 (man under the Mustang turns a wrench, then turns his head toward the door), garage 7 (dad works a wrench, then passes it), garage 11 (a man picks the baseball up off the floor). Clips and notes: `D:\WKP\data\firefly-prompt-log\Video 4`, `video 7`, `video 11`. Contact sheets `D:\WKP\scratch\ffl\`.

Per shot, the author writes: engine and tier, start frame use, one lint-clean prompt, settings.txt top block, a tag on every instruction, a cheapest-test plan, one retry change.

Criteria (each pass or fail per shot, a criterion passes if it holds on all 3 shots, except A7 which needs 2 of 3):
- A1 CRITICAL: no unwanted item named in the positive prompt (lint R1 shows 0 hits).
- A2: positives only for what must appear, one body or one object, one action (no handoff or swap in one clip).
- A3: start frame and tier recorded, with how the start frame is made.
- A4: camera and motion terms taken from a maker page, the quote and source id written.
- A5 CRITICAL: every instruction tagged PROVEN, SOURCED or PROPOSED, and no credit number appears anywhere.
- A6 CRITICAL: a cheapest-test plan, with the credit cost marked NOT RETRIEVED and Zac reading it at the Generate button.
- A7: predicts the known failure in writing on at least 2 of 3 shots (see disclosure).

## Part B: image prompts, non-video (no result exists, graded against sources)
Items: B1 Etsy wall-art listing photo (room scene, landscape), B2 Instagram social graphic for a military homecoming post (house rules: flag in, people shown, all generations, no readable text), B3 YouTube thumbnail background for the WKP history channel (not WWD, empty zone for text added in code).
- B1c CRITICAL: no negation words in the main prompt, no negative-field text pasted into it. Lint 0 FAIL.
- B2c: structure follows Adobe's own order (subject, setting, then style, color, lighting, SOURCED A2 A3) and is under 100 words.
- B3c CRITICAL: text, logos and numerals are NOT asked of the model, an overlay zone is described as a plain picture and the overlay is planned in code or Express.
- B4c: platform spec on the card with its source (YouTube thumbnail Y1, Etsy photo E1), and the claim that the model output size is unverified is stated.
- B5c: every panel tip tagged, and the negative box is marked "does not exist or does not work until Zac sees it" (SOURCED C1, COMMUNITY).
- B6c: fallback and one-change retry written for each item.

PASS: Part A at least 6 of 7 with A1, A5, A6 passing; Part B at least 5 of 6 with B1c and B3c passing. Both parts must pass.
