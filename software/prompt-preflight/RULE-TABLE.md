# RULE TABLE (generated from rules.py by gen_rule_table.py, do not edit by hand)

Severity says the worst result a rule can give. Tags: PROVEN = seen on Zac's clips (count in the evidence), PROPOSED = our rule, not yet tested, UNTESTED = no failure of ours logged, SOURCED = a maker page says it.
R1 to R13 are the ids printed by `prompt_lint.py`. They are NOT the same numbers as STANDARD.md past R4 (see the standard_ref column). PF ids are new.

Evidence quotes are checked against the named files by the unit tests (`test_every_quote_is_in_its_file`).

| Id | Name | Severity | Tag | Applies | STANDARD ref | Fix | Emitted |
|---|---|---|---|---|---|---|---|
| R1 | negation word in the main prompt | FAIL | PROVEN (5 clips) | all prompts | R1 | Write only the picture you want. Delete the no/not/without/never part and describe what is there instead. Unwanted items go in the separate negative box, as plain nouns. | yes |
| R2 | shouting caps or exclamation marks | FAIL | PROVEN (2 clips) | all prompts | R2 (PF17 is folded in here, not counted twice) | Use normal case and full stops. If you were shouting about an object, take that object out of the whole prompt. | yes |
| R3 | prompt length | FAIL / WARN | SOURCED (Luma) / PROPOSED (others) | all prompts | R3 | Cut to one body, one object, one action. Move scene detail into the start frame. | yes |
| R4 | abstract or mental words | FAIL | SOURCED (maker pages) / PROVEN-ish | all prompts | R4 | Describe what a camera would see: posture, hands, light. | yes |
| R5 | em dash or en dash | FAIL | HOUSE RULE | all prompts | none (lint R5 is not STANDARD R5) | Use a comma or a full stop. | yes |
| R6 | garbled grammar (repeated word, stray punctuation, double space) | FAIL / WARN | PROVEN-ish | all prompts | R6 in lint = AUDIT F23 (not STANDARD R6) | Read the prompt aloud and fix it before pasting. | yes |
| R7 | no camera sentence (video) | FAIL | PROPOSED (maker-sourced) | video | R9 | Add one camera sentence that fits the action (static, locked-off, POV, dolly in). | yes |
| R8 | locked camera plus a travelling body (video) | WARN | PROVEN (F11) | video | R9 | Keep the subject in one place, or cut between two clips. | yes |
| R9 | impact verb (bumps, slams, taps...) | FAIL | PROPOSED | video | R8 | Write the resting end picture (the ball rests against the boot) and use an end frame, or cut on the contact. | yes |
| R10 | audio words vs the audio switch (video) | FAIL / WARN | SOURCED / PROVEN (F24) | video | R10 | Audio on: add SFX: and Ambient noise: sentences. Audio off: delete every sound line. | yes |
| R11 | start frame set but geometry also written in text (video) | WARN | PROPOSED | video with a start frame | R7 | Delete the left/right/nose-direction words; fix the still instead. | yes |
| R12 | timestamp ranges not continuous (video) | FAIL | SOURCED | video with [mm:ss-mm:ss] ranges | R11 | Make each range start where the last one ended. | yes |
| R13 | more than 9 sentences in a video prompt | WARN | PROPOSED (rough heuristic) | video | R6 | Count the actions out loud, keep one. | yes |
| PF01 | bare side words (left, right, leftmost...). NOT camera-relative or screen-relative wording | WARN | PROVEN (3+ cases) | video, still, edit | R7/R11 | Put the geometry in the start frame and check the still at full size. If you must say a side, say it camera-relative ('the hand nearest the camera', 'camera left'); those wordings do not fire this rule. | yes |
| PF02 | hand-held tool with hands but no hand named | WARN | PROVEN (garage 1; F16 3 clips) | video, still, edit | R12 / F16 | Name the tool by shape once, say which hand holds it ('one hand, nearest the camera') and that the other hand rests empty on the car. | yes |
| PF03 | rolling or sliding object ends at a body part or surface, and no last frame is claimed (video). A last frame counts as claimed when END_FRAME is yes, END_FRAME_FILE is filled in, or the text says last frame, end frame or final frame | WARN | PROVEN (garage 12); Ian V4 is a Zac report | video | R8 | Give an end frame with the ball resting against the boot (if the panel has an End slot) and write END_FRAME: yes, or plan to cut on the touch. | yes |
| PF04 | handoff or swap inside one video clip | FAIL | PROVEN (5 handoff clips) | video only | R6 | Split it: clip one, a hand holds the object out; cut; clip two, a different hand takes it. Or show the exchange as two stills with a dissolve. Make the second object a different color or shape. | yes |
| PF05 | implied second person | FAIL (video, offer or hand context) / WARN | PROVEN (garage 6 to 8) | video, still | R4/R6 | Do not mention the other person. If the shot needs them, make it a separate clip. | yes |
| PF06 | framing by hiding or negation (out of frame, face hidden...) | WARN | PROVEN (garage 6 to 10) | video, still | R1 | Say the shot positively: 'tight close-up of two forearms and hands, the car underside above them'. | yes |
| PF07 | history: same shot tried too often, or the same words again | FAIL (3+ earlier tries) / WARN (same words) | PROVEN (pattern) | any, needs --history and a SHOT id | R13 | Redesign the shot (new camera, a cut, two clips, another engine). With 1 to 2 tries so far, change exactly one thing before running again. | yes |
| PF08 | history: more than one change per retry | WARN | PROVEN (F18) | any with history | R13 | Change one sentence per try, write down which one, and compare to the last result. | yes |
| PF09 | real logo or on-screen text requested (logo, wordmark, lettering, license or number plate, numerals, title card, emblem painted on a shield, 'the words', 'text reading', 'letters spelling') | FAIL (video, no start frame) / WARN | PROVEN (F3 2 of 2; F7 1) | video, still | R14 | Composite the real logo or text in Photoshop (start frame) or Premiere (edit). Remove the word from the prompt. R14. | yes |
| PF10 | weak visual anchors (lance without a shape in its own sentence, coronal, three-pronged, spear) | WARN / FAIL for 'spear' | PROVEN (joust 2 to 5) | video, still | R12/F2 | Describe the visible shape: 'a long wooden pole as thick as a forearm, painted in red and white spiral stripes, ending in a wide round wooden cap'. Never write 'spear'. | yes |
| PF11 | locked or static camera plus a large body travel (video) | FAIL | PROVEN (F11); verb match is narrower than the count | video | R9 | Keep the person where he is for the whole clip. If the body must move, make two clips and cut. | yes |
| PF12 | floor-level camera plus reaches in / picks up / closes around (video) | WARN | PROVEN (1 clip) + PROPOSED fix | video | F13 | Raise the camera to hip height looking slightly down, or keep it low and have the hand lower from the top of the frame and lift the object straight up. | yes |
| PF13 | door, gate or lid as a light source with no state phrase (video) | WARN | PROPOSED (single case) | video | F14/F21 | State the door state ('the garage door is fully raised and rests overhead') and put the person in the start frame. | yes |
| PF14 | timing words that failed (at N seconds, accelerating, slow-motion, creeping, settles...and then) | FAIL / WARN | PROVEN (joust runs 1 to 6) | video | R11 | Use plain verbs for speed (gallops, drives) and 'from 0 to 2 seconds' ranges instead of one point time. Do not ask for slow motion unless you want it. | yes |
| PF15 | audio words in a video prompt while audio is off | WARN | PROVEN (F24, ffprobe) | video with audio off | R10 | Delete the audio words (or switch audio on and write SFX: and Ambient noise: sentences). | yes |
| PF16 | garble signals (lowercase after a full stop, '. .', unbalanced quotes, no end punctuation) | WARN | PROVEN-ish (F23) | any | F23 | Read the prompt aloud and fix the sentence. Run a spell check yourself. | yes |
| PF17 | shouting aimed at an object (alias of R2) | n/a (R2 fires) | PROVEN (2 clips) | any | R2 | See R2. | no (folded into another rule) |
| PF20 | edit prompt needs a change line and a keep line | FAIL / WARN | PROPOSED (structure SOURCED-book) | edit prompts | B4 | Write two lines: 'Change [one thing, as a picture].' then 'Keep [list] as in the source.' | yes |
| PF21 | one change per edit | FAIL / WARN | PROPOSED | edit prompts | R13/B5 | Split it into two passes, one change each. | yes |
| PF22 | 'do not change' wording in an edit | FAIL | PROVEN (R1, 5 clips) / UNTESTED on stills | edit prompts | R1 | Write 'Keep X as in the source.' | yes |
| PF23 | quality-stack spam and camera-body specs | WARN | PROPOSED (no Firefly test) | any | B17 | Remove them. Resolution is a panel setting. Plain '35mm', 'film grain', 'shallow depth of field' are fine. | yes |
| PF24 | missing master reference, or reference words without a role (info only, never a WARN) | INFO | PROPOSED (info only since 2026-11-24) | edit, video | R15 | Name the master file (MASTER: header or --master) and give each reference a role word (person, room, style, composition, first frame). | yes |
| PF25 | Firefly still main prompt over 750 characters | WARN | PROPOSED (limit NOT VERIFIED) | firefly still | none | Trim under 750 characters, one change, and log which words went. Zac checks the panel limit once. | yes |
| PF26 | negative field: panel box unverified, and negatives that contradict the main prompt | WARN / FAIL (contradiction) | PROPOSED (box) / structural (contradiction) | firefly still with a negative; contradiction check on any prompt given a negative | R5 (STANDARD: no contradictions) | Make the run work without the box. Remove from the negative field any term the main prompt uses. | yes |
| PF27 | negatives failed on video (context line added to R1) | n/a | PROVEN (5 clips) | video | R1 | See R1. | no (folded into another rule) |
| PF28 | Kling start-frame wording and single shot | WARN | PROPOSED (maker-sourced, not run) | kling video | K1 | Start with 'Use @Image1 as the first frame.' and say 'single shot' in the first sentence. | yes |
| PF29 | composition reference carries wrong content | WARN | PROVEN (single case) | still with reference type composition | F26 | Put the correction in the words of attempt 1, run at mid strength, and look at the hands at full size. | yes |
| PF31 | header or ALLOW value not recognised | WARN | PROPOSED (tester finding) | any prompt with a KIND, ENGINE or ALLOW value | none | Fix the header value to one of the allowed words (the message lists them), or fix the rule id in ALLOW. | yes |
| PF30 | settings file complete (--settings FILE) | FAIL / WARN | STRUCTURAL | any, needs --settings | R16 | Fill every field (write NOT SHOWN if the panel does not show it). Copy the credit number from the Generate button, never estimate. | yes |

## Evidence per rule

### R1  negation word in the main prompt
- Evidence: LESSONS F1: "He does not get up and does not slide out" (garage 4): he sat up. "NOTHING IN HIS HAND" (garage 7, 8): wrench in hand anyway. STANDARD R1: zero of 24 old video prompts obeyed the maker advice, the lint failed all 24.
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): The model draws the thing you name, even when you say you do not want it.

### R2  shouting caps or exclamation marks
- Evidence: LESSONS F17: CAPS and exclamation marks (garage 7, 8) had no effect. Also covers PF17: if the shouted word is an object, remove that object from the WHOLE prompt (it contradicted "turns a wrench").
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): Capital letters and exclamation marks do not make the model obey harder.

### R3  prompt length
- Evidence: STANDARD R3: target 100 words or fewer, hard cap 150 (Luma 100). Still prompts warn at 125 and fail at 170 in the lint (PROPOSED). Garage 5 was 189 words and the best clip, so length alone is a risk, not a proven cause.
- Evidence status: CONFIRMED (limits for stills are our own)
- Source files: `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): Long prompts give the engine more things to contradict.

### R4  abstract or mental words
- Evidence: STANDARD R4: no "as if", "seems", "feels", "mood", "hesitation", "begins to". PROVEN-ish: garage 1 to 4 and 6 to 8 used "as if" and a person appeared.
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): The model cannot film a feeling or an intention, so it guesses.

### R5  em dash or en dash
- Evidence: Root CLAUDE.md writing rule: "No em dashes, anywhere, ever." (lint treats it as a hard fail; the rule is written for public copy, prompts are included as a safe habit).
- Evidence status: CONFIRMED (house rule, not a model finding)
- Source files: `CLAUDE.md`
- Why (plain words): House rule: no em or en dashes.

### R6  garbled grammar (repeated word, stray punctuation, double space)
- Evidence: LESSONS F23: garbled or contradictory grammar, joust runs 3 to 6 and garage 7, 8. PROVEN-ish, no clean control run.
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`
- Why (plain words): Broken sentences add ambiguity.

### R7  no camera sentence (video)
- Evidence: LESSONS F21: no camera sentence and the model invents motion (garage 13: the door raised itself). STANDARD R9: one camera sentence in every video prompt.
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): With no camera sentence the model invents camera and scene motion.

### R8  locked camera plus a travelling body (video)
- Evidence: LESSONS F11: "Locked camera, no camera movement" is not honored when the subject travels (garage 2, 3, 6 to 10). PF11 is the FAIL version for the proven verbs.
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`
- Why (plain words): A locked camera and a big body move fight each other.

### R9  impact verb (bumps, slams, taps...)
- Evidence: LESSONS F19: an impact verb ("bumps", "slams", "taps") asks for the impact. Garage 12 prompt said the ball "gently bumps against his boot" and the ball bounced onto the toe.
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/video 12/prompt and notes.txt`
- Why (plain words): The model plays the impact, then bounces.

### R10  audio words vs the audio switch (video)
- Evidence: LESSONS F24: audio never specified or negated, all 18 clips have 0 audio streams (ffprobe 2026-11-22). STANDARD R10: write SFX / Ambient lines or switch audio off and write nothing.
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): Audio on without sound sentences, or sound lines with audio off, is wasted or ignored.

### R11  start frame set but geometry also written in text (video)
- Evidence: LESSONS F22: start frame plus a full re-description of the scene, the words and the picture can disagree. STANDARD R7: with a start frame the prompt gives motion only.
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): The picture decides geometry; extra words can contradict it.

### R12  timestamp ranges not continuous (video)
- Evidence: STANDARD R11: prompt prose or ranges [00:00-00:02], continuous, no gaps. (Lint only reads mm:ss ranges, not 'From 0 to 3 seconds'.)
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): Gaps or overlaps in the timeline confuse the engine.

### R13  more than 9 sentences in a video prompt
- Evidence: STANDARD R6: two or three beats in a 5 to 8 s clip, one body, one object, one action. The 9-sentence line is a rough heuristic of the lint, no clip is tied to it.
- Evidence status: CONFIRMED (heuristic has no failure evidence)
- Source files: `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): Too many sentences usually means too many actions.

### PF01  bare side words (left, right, leftmost...). NOT camera-relative or screen-relative wording
- Evidence: LESSONS F5 (joust run 5: rider down the middle instead of a left-third shield; notes file runs 4 and 6 also name the shield centered), F11 (garage 6 to 10: car nose turned toward the camera or left, not the right as written), row 2026-11-18 Ian V1 "Wrong hand held the wrench", firefly-models.md "wrong hand on the wrench".
- Evidence status: CONFIRMED. Spec said F5 covers 'joust runs 3 to 6'; F5 itself names run 5 only, the notes file names runs 4 and 6. EXACT RULE (2026-11-24): these phrases are removed from the text first and never fire: camera left/right, screen left/right, frame left/right, left/right of (the) frame, nearest (the) camera, farthest (from) (the) camera. Any side word still left (bare left, right, leftmost, rightmost) fires, on every kind. With video and START_FRAME yes the message adds 'remove them from the text', so bare scene-geometry sides are always caught there. The 'all right' and 'right now/away' phrases are ignored as before.
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `memory/topics/firefly-models.md`; `data/firefly-prompt-log/wwd-joust-logo-sting/notes.txt`
- Why (plain words): Text cannot control which side things sit on; the model often flips them.

### PF02  hand-held tool with hands but no hand named
- Evidence: Garage 1 prompt: "His forearms work a steel wrench"; result per LESSONS F16 "the prompt said "steel wrench" only" and drifted to socket or ratchet. Zac note: "Hold Wrench in one hand and his other hand was doing the work". NOTE: LESSONS reads the note as socket vs open-end drift; Zac's sentence says it was supposed to use a socket wrench. Either way the tool and hand were underspecified.
- Evidence status: CONFIRMED (two readings of the same note, see text)
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/Video one/prompt and notes.txt`
- Why (plain words): A tool plus hands with no hand named lets the model pick which hand and which tool.

### PF03  rolling or sliding object ends at a body part or surface, and no last frame is claimed (video). A last frame counts as claimed when END_FRAME is yes, END_FRAME_FILE is filled in, or the text says last frame, end frame or final frame
- Evidence: LESSONS F12: "The ball bounces up onto the toe and rolls away after contact (garage 12)". Row 2026-11-18 Ian V4: "Rolling ball hit the toe instead of resting against the foot". Zac on garage 12: "it some how rolled up on to his tow then rolled away again".
- Evidence status: CONFIRMED (one prompt on disk plus one Zac report)
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/video 12/prompt and notes.txt`
- Why (plain words): Contact physics is weak; a rolling thing that meets a boot gets a rebound.

### PF04  handoff or swap inside one video clip
- Evidence: LESSONS F8 "Never hand an object to another person in one generation", F10 "Five misses on the handoff shot" (garage 6 to 10, 5 clips; F8 counts 6 clips because garage 1 and 4 also lost the tool). Zac, garage 6: "both had the same wrench in there hands".
- Evidence status: CONFIRMED. Spec said '6 of 6'; the handoff shot is 5 clips (garage 6 to 10).
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/Video 6/prompt and notes.txt`; `data/firefly-prompt-log/video 10/prompt and notes.txt`
- Why (plain words): Object permanence breaks when a second hand and a second tool enter: tools duplicate, vanish or morph.

### PF05  implied second person
- Evidence: LESSONS F9: "As if ... someone" asks for the someone. Garage 6 prompt: "as if offering it to someone shorter beside him" produced a second hand and a duplicate wrench in 6, 7, 8.
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/Video 6/prompt and notes.txt`
- Why (plain words): Writing a someone that should not be there makes the model draw them.

### PF06  framing by hiding or negation (out of frame, face hidden...)
- Evidence: LESSONS F15: "His face is out of frame" is ignored, faces show in garage 6 to 10. Garage 7 prompt contains "his face out of frame".
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/video 7/prompt and notes.txt`
- Why (plain words): Hiding something by instruction does not work; the model draws it anyway.

### PF07  history: same shot tried too often, or the same words again
- Evidence: LESSONS F18: "The three-failed-tries redesign rule was not applied for the handoff (5 tries) or the joust (6 plus)" and "The final three were three runs of the same text". STANDARD R13: three failed tries of one shot means redesign. firefly-models.md: "one video re-rendered nine times" (Zac report; the per-attempt prompts for that clip are NOT on disk). The three identical final joust texts ARE on disk in the big joust file.
- Evidence status: CONFIRMED (nine-times report is Zac's word, prompts not on disk)
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-guide/STANDARD.md`; `memory/topics/firefly-models.md`; `data/firefly-prompt-log/Joust opener/prompt and notes for all the rest this was very time consuming.txt`
- Why (plain words): More tries with the same words give the same result. After three misses a stronger sentence will not fix the shot.

### PF08  history: more than one change per retry
- Evidence: LESSONS F18: "The joust prompts changed shot, camera, speed, and wording at once."
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/Joust opener/prompt and notes for all the rest this was very time consuming.txt`
- Why (plain words): When several things change at once no run teaches a clean lesson.

### PF09  real logo or on-screen text requested (logo, wordmark, lettering, license or number plate, numerals, title card, emblem painted on a shield, 'the words', 'text reading', 'letters spelling')
- Evidence: LESSONS F3: "Never rely on the model to redraw a logo" (joust 1 and 5, logo on black, redrawn); F7: "a blank white license plate on the Mustang" (garage 12). STANDARD R14. NOTE: the Joust opener\Video 1 text file on disk is the misfiled garage 13 text; F3 refers to the Video 1 mp4.
- Evidence status: CONFIRMED (F3 count 2 from LESSONS; the Video 1 prompt text is misfiled so only Video 5 text is on disk)
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): The model redraws any text or logo in its own way, even from a start frame.

### PF10  weak visual anchors (lance without a shape in its own sentence, coronal, three-pronged, spear)
- Evidence: LESSONS F2: "A lance renders as a spear, a trident, or a striped hook"; "Coronal" is a rare word and read as a loop; F1: "Spear" drawn after the word "spear". Joust 4 prompt says "not a spear".
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/Joust opener/Video 4/prompt and notes.txt`
- Why (plain words): A rare word or a bare 'lance' gives the model no shape to draw, and the word 'spear' makes it draw one.

### PF11  locked or static camera plus a large body travel (video)
- Evidence: LESSONS F11: "Locked camera, no camera movement" is not honored when the subject travels; counts garage 2, 3, 4, 6, 7, 9, 10. Only garage 2 and 3 prompts carry the exact verbs (rolls out, sits up); 9 and 10 carry "crouches into the frame". The other clips re-framed for other reasons.
- Evidence status: PARTLY CONFIRMED: the 7-clip count is LESSONS' own; the prompts that match this rule's verbs are 2 (garage 2, 3) plus 2 crouch-in (garage 9, 10). Severity FAIL kept as the spec orders.
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/Video 2/prompt and notes.txt`
- Why (plain words): A big body move under a locked camera makes the model re-frame to follow it, and everything else changes with it.

### PF12  floor-level camera plus reaches in / picks up / closes around (video)
- Evidence: LESSONS F13: "Reaching down from a floor-level camera makes the person drop to the floor". Zac, garage 11: "why did he drop down to his hands and kness to pick up the ball".
- Evidence status: CONFIRMED (single clip)
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/video 11/prompt and notes.txt`
- Why (plain words): With the camera at floor level the model lays the whole body down to reach.

### PF13  door, gate or lid as a light source with no state phrase (video)
- Evidence: LESSONS F14: "Garage 13 starts with a closed door that rises by itself". Zac note: "Someone should have been standing there". Single case, fix untested.
- Evidence status: CONFIRMED (single case, PROPOSED)
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/Video 13/prompt and notes.txt`
- Why (plain words): With nothing to do, the model animates the door.

### PF14  timing words that failed (at N seconds, accelerating, slow-motion, creeping, settles...and then)
- Evidence: LESSONS F6: Hit "at 4 seconds" came out as a slow stop then a slow strike; F20: we asked for slowness or a pause and got it. STANDARD R11: do not ask for "no pause" or "accelerating". Seedance 2.5 documents point times (STANDARD B1), so "at N seconds" is allowed there only.
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): The engine reads timing words literally and builds a slow or paused shot.

### PF15  audio words in a video prompt while audio is off
- Evidence: LESSONS F24: all 18 clips have 0 audio streams (ffprobe 2026-11-22); the joust prompts all ended "No music, no dialogue."
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/Joust opener/Video 2/prompt and notes.txt`
- Why (plain words): With audio off those words do nothing, and they are negations.

### PF16  garble signals (lowercase after a full stop, '. .', unbalanced quotes, no end punctuation)
- Evidence: LESSONS F23 (joust runs 3 to 6): the audit lists "stircking", "stright", "the camera Paint flakes". This rule cannot catch typos (no dictionary).
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/Joust opener/prompt and notes for all the rest this was very time consuming.txt`
- Why (plain words): Broken sentences add ambiguity. This check reads punctuation and case only, it cannot spell-check.

### PF17  shouting aimed at an object (alias of R2)
- Evidence: LESSONS F17: "NOTHING IN HIS HAND!!!!" no effect (garage 7, 8). Kept as a note inside R2 so it is not counted twice.
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`; `data/firefly-prompt-log/video 7/prompt and notes.txt`
- Why (plain words): See R2.

### PF20  edit prompt needs a change line and a keep line
- Evidence: PLAYBOOK C1: "Line 1 names the one change. Line 2 names what stays, written positively." STANDARD B4: an edit prompt has two lines. No failure of ours is logged: UNTESTED.
- Evidence status: UNTESTED (no failure evidence from our logs)
- Source files: `REFERENCE/PROMPTING-PLAYBOOK.md`; `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): An edit with no keep line lets the model change everything; one with no change line does nothing.

### PF21  one change per edit
- Evidence: PLAYBOOK C1: "One change per pass (R13, B5)." STANDARD B5: "One edit per pass." UNTESTED.
- Evidence status: UNTESTED (no failure evidence from our logs)
- Source files: `REFERENCE/PROMPTING-PLAYBOOK.md`; `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): Two changes in one pass means you cannot tell which one broke the picture.

### PF22  'do not change' wording in an edit
- Evidence: PLAYBOOK C1: Do not write "do not change X". Write "keep X as in the source". R1 PROVEN on 5 video clips; on Firefly stills the negation question is UNTESTED (book test T1).
- Evidence status: CONFIRMED for the wording; effect on stills UNTESTED
- Source files: `REFERENCE/PROMPTING-PLAYBOOK.md`; `data/firefly-prompt-guide/LESSONS.md`
- Why (plain words): A negative keep instruction names the thing and invites the change.

### PF23  quality-stack spam and camera-body specs
- Evidence: PLAYBOOK B4: "Do not paste long quality lists". STANDARD B17: "No long quality stacks or camera-body specs until a test shows they change a Firefly still." No failure of ours logged.
- Evidence status: UNTESTED (no failure evidence from our logs)
- Source files: `REFERENCE/PROMPTING-PLAYBOOK.md`; `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): Quality lists and camera-body names are not shown to change a Firefly still.

### PF24  missing master reference, or reference words without a role (info only, never a WARN)
- Evidence: PLAYBOOK B1: "Every later still uses it as a reference with a named role". STANDARD R15: "Reference images each get a role in the prompt." Not run on Zac's account.
- Evidence status: UNTESTED (no failure evidence from our logs). Made INFO-only 2026-11-24: it fired on 10 of 28 known-good prompts, so it is printed as a note and never counts toward the verdict
- Source files: `REFERENCE/PROMPTING-PLAYBOOK.md`; `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): A reference with no role, or no named master, lets the identity drift.

### PF25  Firefly still main prompt over 750 characters
- Evidence: graphic-design.md 2026-11-21: "two prompts ran over 750 until trimmed". Sitting sheet 2026-11-23: "The H1 prompt runs about 770 characters: if the panel refuses the length". The panel limit itself is NOT VERIFIED.
- Evidence status: CONFIRMED text; limit unverified
- Source files: `memory/agents/graphic-design.md`; `Post-Production/reports/Ian-Trailer-Firefly-Sitting-Sheet-2026-11-23.md`
- Why (plain words): The Firefly panel may refuse or cut a long prompt. The real limit has not been read off the panel.

### PF26  negative field: panel box unverified, and negatives that contradict the main prompt
- Evidence: graphic-design.md 2026-11-22: "Do not run a prompt that depends on a Firefly negative box"; an Adobe Community reply says negatives get added to the image. SOURCES: "Negative/exclude prompt and seed settings are not mentioned." The contradiction test (a negative term also in the main prompt) is mechanical.
- Evidence status: CONFIRMED text; box existence NOT VERIFIED
- Source files: `memory/agents/graphic-design.md`; `data/firefly-prompt-guide/SOURCES-2026-11-22.md`
- Why (plain words): The negative box may not exist or may add the words to the picture. A term in both fields cancels itself.

### PF27  negatives failed on video (context line added to R1)
- Evidence: LESSONS F1: PROVEN (5 clips) (garage 4, 7, 8, joust 4, run 6). No separate finding: the sentence "negatives failed on video 5 of 5 clips" is added to the R1 message.
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/LESSONS.md`
- Why (plain words): See R1.

### PF28  Kling start-frame wording and single shot
- Evidence: STANDARD Kling template: "Use @Image1 as the first frame, then describe what happens next." and "Multi-shot is on by default in 4.0 (K1)". Not run on Zac's account.
- Evidence status: UNTESTED (maker page only)
- Source files: `data/firefly-prompt-guide/STANDARD.md`
- Why (plain words): Kling needs the first-frame sentence, and 4.0 cuts into several shots unless told to keep one.

### PF29  composition reference carries wrong content
- Evidence: LESSONS F26: "A Composition reference carries the arrangement including an unwanted hand size" (Ian R3b: R3 has a child's hand where an adult arm is wanted). Single case.
- Evidence status: CONFIRMED (single case)
- Source files: `data/firefly-prompt-guide/LESSONS.md`
- Why (plain words): Composition copies everything in the reference, including its mistakes.

### PF31  header or ALLOW value not recognised
- Evidence: Tester report 2026-11-24: a typo in a block header (for example ENGINE: veoo or KIND: vidio) silently switched off every rule that depends on the engine or kind, and an unknown id in ALLOW overrode nothing and said nothing. SPEC input section lists the allowed keys and values: "ALLOW (comma list of rule ids the author explicitly overrides, shown as OVERRIDDEN, never silent)".
- Evidence status: CONFIRMED (tester report; single case type)
- Source files: `software/prompt-preflight/SPEC.md`
- Why (plain words): A typo in the header changes which rules run, and nothing told you.

### PF30  settings file complete (--settings FILE)
- Evidence: STANDARD: "Every field must be present". R16: "No credit number is ever estimated by an agent." Checks every key line of SETTINGS-TEMPLATE.txt exists, and that a typed credit number has a panel readout.
- Evidence status: CONFIRMED
- Source files: `data/firefly-prompt-guide/STANDARD.md`; `data/firefly-prompt-guide/SETTINGS-TEMPLATE.txt`
- Why (plain words): A missing field means a lesson cannot be learned from the run; a typed credit number may be an estimate.

## Info printed for every video prompt (not scored)

- 1 Identity: face, age and build match the master
- 2 Costume: every garment and accessory matches the bible
- 3 Place: layout, props and materials match the place master
- 4 Camera language: shot size, angle and lens habit match the shot list
- 5 Light direction: shadows fall the same way as the shot before and after
- 6 Grade: color and contrast match the sequence
- 7 Scale: people and objects have believable size against each other
- 8 Perspective: verticals straight, horizon level, feet on the floor
- 9 Time of day: sky, light color and shadows fit the hour
- 10 Hands and face are clean at full size (R17)
- 11 No text, logo or plate in the picture unless it will be replaced (R14)
- 12 The geometry the video needs (which hand, which side) is visible in the frame (R7)
- RETRY RULE (STANDARD R13): attempt 2 changes ONE thing and you write down which. After attempt 3 fails, redesign the shot, do not write a stronger sentence.

LIMIT: this tool reads words. It cannot predict what an engine draws.
