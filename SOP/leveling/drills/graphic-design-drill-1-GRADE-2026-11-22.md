# Grade: graphic-design drill 1

Signed: qa-director (independent grader, not the author), 2026-11-22.
VERDICT: FAIL. Part A 3 of 7 (needs 6 of 7 with A1, A5, A6 passing; A5 fails). Part B 5 of 6 (B1c and B3c pass), which would pass on its own. Both parts must pass, so the drill fails and must be re-run after the fixes below.

What I read and ran: SOP-Agent-Leveling parts 3, 4, 6; the drill (pass bar written first, contamination disclosure noted); the run; the lint output; the Craft Brief; the gap audit; the three checklists; notes.txt and contact sheets for Video 4, video 7, video 11; SOURCES-2026-11-22.md; LESSONS.md and STANDARD.md for the F and R ids the run cites. No credits, no generation, nothing posted.

## Independent checks
- Lint rerun by me: `prompt_lint.py --file` on the run file gives 6 of 6 PASS, exit 0 (same as the author's saved output). R1 count is 0 on all six prompts.
- Y1 re-fetched live (support.google.com/youtube/answer/72431): REAL. "try to upload a thumbnail with an aspect ratio of 16:9", "2 MB for video thumbnails or 10 MB for podcasts" (Mobile only, Desktop is 50MB), "a minimum width of 640 pixels for videos", "JPG or PNG" all appear. Not carried over: the page also recommends 3840 x 2160 pixels, which the card omits.
- E1 re-fetched live (help.etsy.com/hc/en-us/articles/115015663347): REAL. All five quotes match ("at least 2000 pixels or more", "horizontal (landscape) or square", "focused in the center", "further back than you think you'll need", "clear in all 3 views").
- C1 re-fetched (community.adobe.com negative-prompting thread): quotes are real (Sep 18 2025 reply, Mar 1 2025 reply, May 12 2026 "prompt to edit"). BUT the Sep 18 2025 reply continues in the same paragraph: "You can use the parameter "[avoid=xxx]" in your prompt, where xxx is the thing you want the image to veer away from." The brief and run quote only the first sentence and say the model has no negative mechanism. The omitted sentence (a COMMUNITY-tagged avoid parameter) changes the advice and appears nowhere in the brief, the run or the open questions (grep for "avoid=" finds nothing). Selective quoting, not invention, but it is a real fault.
- G1 to G4, A1 to A3, K1, R2, L1, F3, F4: NOT re-fetched by me. They were extracted by a small model ("fetcher"), the author never saw raw pages. Treat as unconfirmed.
- Contact sheets match the known failures: Video 4 man sits up and holds the wrench out; video 7 a second hand with a second wrench enters; video 11 an arm lies along the floor and drags the ball. The author's A7 predictions describe these correctly (contaminated, as disclosed).

## Part A (video replay)
| ID | Result | One-line proof |
|---|---|---|
| A1 CRITICAL | PASS | Lint R1 0 hits on all 3, I reran it. No unwanted item named in any positive prompt. |
| A2 | FAIL | Garage 4 stacks wrench turn, rest, head turn in 8 s; garage 7 stacks turn then lower and rest the wrench at his chest (the garage 1 failure shape, F8); neither is one action. The run's own cheapest test says "beat 1 only", conceding the prompt is too much. Garage 4 also says "Both hands rest on the wrench", which contradicts the author's PROVEN F16 (second hand on the tool produced a wrench turning a wrench). Garage 7 puts both hands on the wrench too. |
| A3 | FAIL (narrow) | Tier and start frame stated for all 3, but "how the start frame is made" is missing for garage 7 ("the working-hands still", no source) and garage 11 (a standing man thighs down with the ball at his feet, a frame that does not exist on disk, no method given). Garage 4 gives two options but does say how. |
| A4 | FAIL (narrow) | Criterion needs the quote and the source id. The run gives ids (G1, G2) and a paraphrase ("G1 lists static"), no verbatim quote, and garage 7 and 11 give none. "Floor level" and "knee height" are not maker terms. |
| A5 CRITICAL | FAIL | No credit number anywhere (good). But tags are not clean: "PROVEN-ish" is used three times (lines 21, 52, 89) and is not an allowed tag under SOP part 7 and the pre-flight. Untagged instructions: "AI-generated label if public", "Audio off", the panel check, the lighting and dust lines in all three prompts. "PROVEN for this shot class, 18 clips" and "PROVEN: someone shorter produced a second person" cite no clip path, and the second is one clip, not two. |
| A6 CRITICAL | PASS | All three name a cheapest test, 4 s draft at 720p, credit "NOT RETRIEVED"; the global block says Zac reads the number at the Generate button. Weakness: garage 4 and 7 prompts run to [00:08] while the test and settings block say 4 s, and no beat-1-only prompt is written. |
| A7 | PASS | 3 of 3 predicted: tool changes shape, second wrench appears, he drops to hands and knees. Matches the clips. Weight is low (contamination disclosed). |
Part A: 3 of 7. FAIL (A5 fails, and 3 of 7 is under 6).

## Part B (image prompts)
| ID | Result | One-line proof |
|---|---|---|
| B1c CRITICAL | PASS | No negation words in any of the three main prompts, no negative text pasted in, lint 0 FAIL. |
| B2c | FAIL (narrow) | All under 100 words (61, 81, 61). But each prompt ends lighting, then style, then colour ("soft daylight ... shallow depth of field ... warm neutral colors"), the reverse of the stated style, colour, lighting order, and "Photograph" (image type) opens the prompt rather than following the setting. The run never says which order it is following. |
| B3c CRITICAL | PASS | No text, logo or numeral requested; empty zones are plain sky or plain plain (top third, left third); overlay named as code or Express. "Thirteen stripes" is a flag count, not text. |
| B4c | PASS | Y1 and E1 on the cards, both verified real; Meta marked NOT RETRIEVED; output size marked NOT VERIFIED. |
| B5c | PASS (note) | Content type and four variations tagged SOURCED A2; negative box tagged C1 COMMUNITY and "not relied on". Note: untagged lines remain (Generative Fill fallbacks) and the C1 quote omits the avoid parameter (see above). |
| B6c | PASS | Fallback and a one-change retry written for all three. |
Part B: 5 of 6 with B1c and B3c passing. PASS.

## Checklists
| File | Items | Usable? | Notes |
|---|---|---|---|
| graphic-design-firefly-image-prompt-card.md | 11 | Yes, with fixes | Mostly checkable by looking at the file. Item 3 ("order is subject, background, then style, colour, lighting") would fail the author's own three prompts, so it is either wrong or unenforced; make it specific. Item 6 proof ("grep for untagged set/use lines") is vague. Item 8 "copied artist look" is a judgment. Item 7 is conditional and fine. |
| graphic-design-firefly-video-prompt-card.md | 12 | Yes, at the top of the range | Items 3, 4, 7, 9, 11 are good and checkable. Item 12 (lesson row planned) cannot be checked by looking at the file. Item 2 "one-line mapping" fine. The author's own run fails items 3, 4 and 11, which shows the checklist works but was not run. |
| graphic-design-redo-plan.md | 10 | Partly | Items 8 and 9 (settings-N.txt, LESSONS row, failures file) live in other files and happen later; they are not checkable on the redo file. Item 1 needs Zac's note, item 6 says "where possible". Trim to items checkable on the card, move 8 and 9 to the job close step. |

SOP part 4 also requires the ticked checklist pasted into the hand-back. The run file has none, and no UNDRILLED line.

## Faults the author must fix (then re-run the drill)
1. A5: replace every "PROVEN-ish" with PROVEN, SOURCED or PROPOSED; tag the prompt-body style lines, audio, label and panel-check instructions; cite clip paths for each PROVEN (and PROVEN needs two logged results).
2. A2: rewrite garage 4 and 7 as one action per clip (garage 4: wrench only, head turn its own clip; garage 7: hands turn the wrench, nothing lowered to the chest). Remove "both hands on the wrench" in 4 and 7 and use one hand on the tool, other hand empty and resting, per F16. Write the beat count on each card.
3. A3: state how each start frame is made (source file path, or the still prompt) for garage 7 and 11.
4. A4: write the verbatim maker quote next to each camera or timing term with its id, and drop or tag as PROPOSED the non-maker terms ("floor level", "knee height").
5. A6 tidy: either write a 4 s beat-1-only prompt, or set DURATION to match the 8 s ranges. Do not leave an 8 s prompt beside a 4 s settings block.
6. B2c: put image prompts in the stated order (subject, setting, style, colour, lighting) or write which Adobe order is used and why; fix pre-flight item 3 to match.
7. C1: quote the full Sep 18 2025 reply including the "[avoid=xxx]" sentence, tag it COMMUNITY, add it to the open questions as a thing for Zac to test, and correct the brief section 3 line that says images run with no negatives only.
8. Y1: add the 3840 x 2160 recommendation to the B3 card, or say why it is not used.
9. Run all three checklists on the revised run and paste them ticked into the hand-back with proof lines; add the UNDRILLED line until a drill passes.
10. Trim redo-plan items 8 and 9 and video-card item 12 out of the "look at the file" list.
11. Minor: the brief line 26 has an em dash inside a verbatim F4 quote. It is a true quote, but flag it so it is not mistaken for house style. Also garage 11 re-describes the start frame ("framing the man from the thighs down beside a white leather baseball") against the author's own F22/R2 "motion only" rule; trim it.

Not verified by me: G1 to G4, A1 to A3, K1, R2, L1, F3, F4 quotes (fetcher text, not re-fetched); the author's drill file Part B has no result, so B items were graded against sources only.
