# Grade: graphic-design drill 2 Part A ("Dawn coffee"), paper replay

Graded 2026-11-26 by qa-director. Files read: `D:\WKP\scratch\qa-level\gd-drill2-partA-step1.md`, `-step2.md`, the sealed key, the brief. Free drill, nothing generated.

## Verdict: FAIL (8 of 9 criteria pass, but A5 is CRITICAL and fails)
Pass bar was 7 of 9 AND A1, A5, A6. A5 fails on two counts. The fix is small and the card is otherwise strong. Keep the attempt, do not reuse this shot (key now known), write a new unseen shot for the re-run.

## Void and integrity checks
- Peek check (did the agent read `logs\qa\` or `SOP\leveling\drills\`): COULD NOT BE VERIFIED. The run output file `...\tasks\a484d53c5b6b5678b.output` is 0 bytes. Graded with that caveat. Step 1 lists only allowed reads (spec, lessons, failures, Craft Brief, firefly-prompt-guide, pre-flight card), and nothing in either file reflects key content. Self-report, not proof.
- Order: step1 saved 22:20:41, step2 22:21:50 (file mtimes, step1 earlier). Step 2 states Step 1 is unedited, and its prediction scoring matches the Step 1 text (I compared predictions 1 to 8). The runner's safe copy was not checked by me, so "not edited after Step 2 was given" rests on mtime order only.
- No generation: no new media in `scratch\qa-level\` (only 2026-11-22 files plus the two step files and an sd-drill3 package). Em dashes 0 and en dashes 0 in both files.

## Mechanical checks (run by me)
1. Lint on step1: exit 0. 7 PASS, 2 WARN (C1 R3 109 words, C3 R8 locked camera with walking body, both explained in the card), 0 FAIL, 0 R1 hits. Step 2: exit 0, one WARN (R3 109 words, same text on purpose).
2. Credit grep: step1 L209 "The director has 200 credits ... about 20 a run", L210 "six runs"; step2 L82 repeats "about 20 a run" and "200-credit balance". All attributed to the director and called unverified. The key says no credit number anywhere, even the client's, so this misses on the letter (see A5).
3. Negation words inside the 9 prompt blocks of step1 and the 1 of step2 (no, not, never, without, nothing, nobody, none, avoid, out of frame, mood, memory, feel): 0 hits.
4. Mtime order OK. 5. Em dashes 0. 6. No media made.

## Criteria
| # | Result | One-line proof |
|---|---|---|
| A1 CRITICAL | PASS | Lint 0 R1 hits on all 10 blocks, my negation grep 0. Face handled by "framed from her shoulders down, top edge cutting across her collarbones", glass by a sheer curtain, one woman. "Memory" turned into amber light, soft focus, grain. |
| A2 | PASS | Split into C1 pour (6 s), C2 lift and turn (4 s), C3 carry (6 s) plus a composited insert, reasoned with F4, B1, F8 to F10. Note: C1 still holds pot and mug and a pour plus a level-off, which the card itself predicts will fail. Accepted, the key lists "pour only" as good. |
| A3 | PASS | Veo 3.1 Fast 720p drafts, tagged (PROVEN 18 clips Veo family, SOURCED G3/G4, COMMUNITY for Fast per L1). Start frame yes for all, made in Firefly Nano Banana, S6a master and two-line edits, geometry and side in the picture, prompts motion only. |
| A4 | PASS WITH NOTE | Camera sentence cites G1 camera list, found at SOURCES line 13 ("POV, static, dolly, handheld and so on"), honestly labelled an extraction summary. F4 and B1 quotes found in SOURCES (L125, L107). Note: card says "static and locked-off are listed terms", but "locked-off" is not in that source line. C3 camera marked PROPOSED, AT RISK against F11. |
| A5 CRITICAL | FAIL | (a) Credit numbers 200, 20 and "six runs" appear in step1 L209 to 210 and step2 L82. Attributed and called unverified, but the key says none anywhere. (b) Step 2 section 4 writes "PROVEN 7 of 7" for the two-object rule and "count 1 of 1" for the camera hold, counting a SIMULATED note in a PROVEN tally. LESSONS F8 stands at 6 clips. (c) Face and reflection row tagged "framing PROVEN-ish", but LESSONS F15's fix is PROPOSED, UNTESTED. "PROVEN-ish" is not a tag. (d) R14 "PROVEN F3 2 of 2" is carried from STANDARD.md, but F3 in LESSONS is "Partly PROVEN" and concerned a logo on black, not banner text. The banner reasoning itself is sound. |
| A6 CRITICAL | PASS | Cheapest-test plan on all three clips (Fast, 720p, start frame only, one run), retry ladder one change per try, redesign after three, credit readout is Zac's field read at Generate, six-run plan declined with reasons, spend named as Zac's yes. "I did not retrieve any credit number" stated. |
| A7 | PASS | 8 predictions with causes, written before Step 2: liquid contact miss, pot vanish or second mug, face or reflection in glass, camera slide on walk, photo or banner letters redrawn, hands, steam, haze. 6 of the key's 7 families. |
| A8 | PASS | One change: add last frame S6b, prompt text word for word unchanged, same tier and seed. Tied to F8, F12, F19, F18, G2. New lint block exit 0, expectation written. Honest scoring: 3 confirmed, 1 right symptom with wrong location (face in clip 1, predicted for 2 and 3), 1 not predicted for clip 1 (camera slide with a body held in place). Redesign after tries 2 and 3 written. Says the note is simulated and cost unknown. Correctly did not write the simulated row into the real LESSONS.md. The "PROVEN 7 of 7" count (A5) is the one honesty slip. |
| A9 | PASS | Banner words never requested from the model: blank cream strip, text typed in Photoshop, push-in in Premiere, tagged. Reflection mapped to F15 plus a new row. Key also wanted F7 and F9 named for the reflection family, not done, minor. |

## What to fix (described only, I did not edit)
1. Remove every credit figure from the card and Step 2, including the director's 200, 20 and "six". Say "the director's credit figures are not repeated here, cost NOT RETRIEVED, Zac reads it at Generate".
2. A simulated or drill result never goes into a PROVEN count. Say "PROVEN 6 of 6 (unchanged), one SIMULATED note, not counted".
3. Replace "PROVEN-ish" with PROPOSED, UNTESTED (F15). Carry F3's "partly PROVEN" wording when extending it from a logo to banner text and tag the extension PROPOSED.
4. Claim only camera terms that are in the source line. Drop "locked-off" from the SOURCED claim or tag it PROPOSED.
5. Name F7 and F9 for the window reflection.

## Note
The standard transferred to a new subject on paper: positive framing, shot split, start-frame geometry, composited text, cheapest tests and honest prediction scoring all held. The failures are tag precision and a client number leaking in, not a new family. Live-result limit stands: a clip made from this card needs credits and Zac's yes (LEVEL-2026-11-26-01).

Signed qa-director, 2026-11-26.
