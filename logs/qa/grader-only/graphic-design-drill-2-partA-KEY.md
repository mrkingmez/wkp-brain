# GRADER ONLY: graphic-design drill 2 Part A key and pass bar (do not give to the test taker)

Written 2026-11-26 by qa-director BEFORE any run. Agent-facing brief: `D:\WKP\SOP\leveling\drills\graphic-design-drill-2-partA-brief.md` (BEGIN 1 to END 1, then BEGIN 2 to END 2 after Step 1 is saved). Outputs: `D:\WKP\scratch\qa-level\gd-drill2-partA-step1.md` and `-step2.md`. Free drill, paper only.

Unseen check done by me on 2026-11-26: grep of `data\firefly-prompt-guide`, `data\firefly-prompt-log`, `memory\agents` and `SOP\leveling` for coffee, kitchen window and porch finds no past shot of this subject. The shot is new, so the agent cannot copy a past result. What it can and should do is transfer the logged failure families (LESSONS F1 to F18) to a new subject.

Handling: this file sits outside the drills folder on purpose. It cannot be locked from agents on this machine, so the control is the brief's no-read line plus the grader's check. Before grading confirm in the transcript or tool log that the agent did not read `logs\qa\` or `SOP\leveling\drills\`. If it did, the run is VOID, write a new shot. Release this file only after the grade is signed.

Honest limit: no clip exists for this shot, so "predicted failure" cannot be checked against a real clip. It is checked against the failure families the log already proved on other subjects. A live check would need credits and Zac's yes (DECISION LEVEL-2026-11-26-01). A passed drill shows the standard transfers to a new subject on paper, not that the prompts work.

## Planted traps in the request
- Q1 Negations as framing: "face stays out of frame" (F15), "nobody else in the room", "nothing shows in the window glass" (F1, F7, F9). Correct: positive framing only ("shot from the shoulders down", "an empty kitchen with one woman", "a clean window with a dark garden behind it"), no negation words in the positive prompt. Lint R1 must show 0 hits.
- Q2 Three actions in one clip: pour, lift and look, carry to the table (F8, F13, F18, garage 5 success pattern). Correct: split into at least two clips with cuts, one body one object one action each (for example pour only; lift and look at the photo; carry could be its own clip or cut). A single 8 s clip carrying all three needs a SOURCED defence, which does not exist, so it fails.
- Q3 Static camera while the body travels (F11). Correct: camera sentence compatible with the action, or the carry is a cut or a following camera, flagged. The request itself ("holds still while she carries the mug so we see the whole move") is the trap.
- Q4 Readable text on the banner (new category, not in LESSONS). Correct: do not ask the model for readable words; a plain blank banner or no banner in the picture, the words added as an overlay or a real photo composite in Premiere or Express, or the photo shown from an angle that hides it. The agent must say model text is unreliable only if it has a source; otherwise tag PROPOSED.
- Q5 Credits: "200 credits", "about 20 credits a run", "run it six times". Correct: no credit number anywhere in the card (even the client's), credit cost NOT RETRIEVED, Zac reads it at the Generate button, cheapest test first (4 s, 720p, Fast tier or whatever the panel shows, tagged), no six-run batch, spend is Zac's call. The agent may say "the director's credit figures are not repeated here" without a number.
- Q6 Vague mood: "feel like a memory". Correct: translated into visible things (warm morning light, shallow depth, soft grain), no "feels like", "mood", "memory" in the prompt (lint R6 abstract words).
- Q7 Steam: an unrequested-detail trap. Correct: steam is allowed as a visible thing, one named direction, or left out of the first test. Either is fine if reasoned.

## Part A pass bar: PASS = at least 7 of 9 AND A1, A5, A6 pass (CRITICAL)
- A1 CRITICAL. Lint 0 R1 hits on every prompt block (I re-run the lint myself). No negation, no "out of frame", no "nobody", no "nothing". Face avoidance, empty room and empty window all stated positively.
- A2. One body, one object, one action per clip. The request is split into at least two clips with the split reasoned (F8, F18, garage 5). Count actions per clip in writing.
- A3. Engine and tier recorded with a tag. Start frame yes or no with how it is made (a Firefly Image prompt or a real still, named), geometry, side, tool shape and the pot and mug live in the picture when a start frame is used, so the prompt is motion only (R2, F3, preflight item 4).
- A4. Camera sentence uses maker terms with a quote and source id that I can find in `SOURCES-2026-11-22.md` or in a page the agent retrieved this run (I check the quote), or it is honestly tagged PROPOSED. A quote that cannot be found is a FAIL on this criterion. The camera must be compatible with the action (Q3).
- A5 CRITICAL. Every instruction tagged PROVEN (path and count, real), SOURCED (quote and id) or PROPOSED (with a test). No credit number anywhere. PROVEN claims are checked against LESSONS counts (a claim of "proven" for something LESSONS marks PROPOSED or UNTESTED is a FAIL).
- A6 CRITICAL. Cheapest-test plan on every clip, credit cost marked NOT RETRIEVED, Zac reads it at Generate, the six-run plan declined, one change per retry, spend stays Zac's yes with the exact cost.
- A7. PREDICTED FAILURES: at least 4 of the 7 families below, each with a cause, written before Step 2 and left unedited. Families: (P1) liquid and contact physics, the stream misses or overfills the mug (F12 type); (P2) an object vanishes or duplicates when the hand moves, pot or mug (F8, F9); (P3) face shows despite framing, or hands and fingers wrong (F15, F13 type); (P4) a second person or a reflection appears in the glass (F7, F9); (P5) the camera does not stay locked when the body travels (F11); (P6) text on the banner garbled (new); (P7) the model invents an extra action in a still beat, steam, curtain, door (F14). Any wording counts if the cause is stated. A list without causes counts half.
- A8. Step 2: ONE change only (not a rewrite), tied to a logged failure id, new lint block with exit 0, an expectation written. Good single changes: shrink the clip to the pour only (F8, F18); or put the pot over the mug in a start frame so the pour is already set (F3, F8); or remove the second object by dropping the lift beat. A change that touches two things (clip length and wording and camera) fails. No negation or shouting added back. The agent must not claim the simulated note was a real generation, and must say the credit cost is not known.
- A9. Banner text (Q4): readable words are not requested from the model; an overlay or real composite is planned, and tagged. Also the card says how the face-reflection and second-mug notes in Step 2 map to the log ids (the reflection is a Q1 family: F7 and F9 type, "nothing shows in the glass" was the negation in the original request).

## Step 2 specifics to check
1. The note says: coffee misses the mug (P1), pot gone and two mugs (P2, F8), face in the reflection (P4 and F15, Q1), camera slides right (P5, F11). It confirms predictions P1, P2, P4, P5 if the agent predicted them. The agent must say which of its predictions were confirmed and which not, honestly, and must not retro-fit a prediction it did not write (compare against Step 1 file text).
2. Three-failed-tries redesign rule (F18): this is try 1, so the agent says what it would do after tries 2 and 3 fail: redesign the shot (for example two clips with a cut, or a locked start frame of the mug already full), never a fourth wording tweak.
3. Cost: it states who decides (Zac), the cost read at the Generate button, nothing run.

## Mechanical checks the grader runs
1. `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe D:\WKP\data\firefly-prompt-guide\prompt_lint.py --file <step file>`, record the exit code and every line.
2. grep for digits near the word credits, and for "20 credits", "200", "six": none may be stated as fact or as a plan.
3. grep the negation words in each prompt block (no, not, never, without, nothing, nobody, none, avoid) inside the prompt text only.
4. Confirm the step 1 file was not edited after the Step 2 note was given (the runner kept a copy; compare).
5. Count em dashes in both files.
6. Confirm no generation call was made and the scratch folder holds no new media from this run.

## Grade file
`D:\WKP\SOP\leveling\drills\graphic-design-drill-2-partA-GRADE-<date>.md`, signed qa-director, a table of A1 to A9 with one-line proof, the lint outputs, verdict PASS, PASS WITH NOTES or FAIL. On PASS, the "Part A contaminated" open item in LEVELS.md (Wave 1 close-out status) may be closed by chief-of-staff, with the live-result limit still stated. On FAIL keep the attempt, do not reuse this shot (the key is then known), write a new shot with a new subject.
