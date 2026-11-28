# Firefly and video-model PROMPT STANDARD (v2, 2026-11-22)

> General parent: `D:\WKP\REFERENCE\PROMPTING-PLAYBOOK.md` (venture-neutral staged pipeline, bible, edit loop, kickoff checklist, test method). This file is its Firefly and video-model child, where the two disagree this file's PROVEN rules win.


Replaces the beginner rules in `QUICK-CARD.md` and the older `Firefly-Video-Prompting-Guide.md` where they disagree. Read this, then `LESSONS.md`, before writing any prompt for any image or video model. Sources with quotes and dates: `SOURCES-2026-11-22.md`. Why v1 failed: `AUDIT-2026-11-22.md`.

Tags on every rule: **SOURCED** (a maker's own page says it, source id given, read 2026-11-22), **PROVEN** (seen on Zac's clips in `firefly-prompt-log`, count given), **PROPOSED** (my rule, not yet tested). SOURCED and PROVEN together is the strongest. A rule that is only PROPOSED is a try, not a law.

## The standard in 10 lines
1. Write the picture you want, in positive observable words. Never write what you do not want (R1). No caps, no exclamation marks (R2).
2. Use the engine's own order: Veo [Cinematography] + [Subject] + [Action] + [Context] + [Style], then audio sentences. Other engines have their own template below (R3).
3. One body, one object, one action per clip. A handoff or swap is two clips and a cut, or two stills and a dissolve (R6).
4. The start frame decides who, where and which side. With a start frame the prompt describes motion only (R7).
5. For contact or a landing spot, give an end frame on an engine that takes one, and write the end as a resting picture (R8).
6. Always write one camera sentence that does not fight the action. A traveling body needs a cut, not a locked camera (R9).
7. Say what the audio is, in its own sentences, or switch audio off in the panel and write nothing about it (R10).
8. Name every object by its visible shape and color, once, the same way in every clip (R12).
9. Run the lint and the checklist BEFORE the prompt goes to Zac. Hand over settings.txt with the blanks he fills at the panel (pre-flight).
10. One change per retry. Three misses on one shot means redesign the shot, not a stronger sentence (R13).

## Rules

| Id | Rule | Tag | Evidence |
|---|---|---|---|
| R1 | Positive picture only. No "no, not, never, without, nothing, nobody, does not" in the main prompt. Unwanted things go only in a negative field, as plain nouns, and only for global items. Exception: "no subtitles" and "no background music" on Kling and Seedance. | SOURCED G1, R2, K1, L1, B1. PROVEN 5 clips (F1) | G1: "Describe what you don't want to see." Zero of 24 old video prompts obeyed |
| R2 | No capital-letter shouting, no exclamation marks. | PROVEN 2 clips (garage 7, 8: no effect). Not in any maker page | Mechanical |
| R3 | Use the engine template (below). Target 100 words or fewer. Hard cap 150 (Luma Ray3.14 cap 100). | Template SOURCED G2, A1, R1, K1, B1, F2. Length: Luma 100 SOURCED L1, others PROPOSED | Garage 5 was 189 words and the best clip, so length alone is a risk, not a cause |
| R4 | Observable words only. No "as if", "seems", "feels", "mood", "hesitation", "begins to", "starts to", no stacked adjectives. Describe what the camera would see. | SOURCED R2, K1, K2, L1. PROVEN-ish (garage 1 to 4, 6 to 8 used "as if", and a person appeared) | Lint R4 |
| R5 | No contradictions. If the object must be absent, remove it from the whole prompt, do not mention it. | SOURCED R2, B1. PROVEN 2 clips (garage 7, 8) | |
| R6 | One body, one object, one action per clip. Beats: two or three in a 5 to 8 s clip. No handoff, no swap, no two similar tools in one clip. | SOURCED F4 (two or three beats), B1 (too much packed). PROVEN 6 of 6 (garage 6 to 10, F8 to F10) | |
| R7 | With a start frame, geometry, identity, left and right, logo and tool shape live in the picture. The prompt gives motion only, not a second description of the scene. | SOURCED R2, F3, K1. PROVEN 3 clips (F5, F11) | |
| R8 | Contact, landing and "ends resting against" shots: use first AND last frame where the engine takes one, and write the end as a resting picture. Or cut on the contact. | Mechanism SOURCED G2, G4, F3, L1, K1, B1. NOT yet run on Zac's account (garage 12 had none) | Firefly panel exposure of an end frame per model: NOT VERIFIED |
| R9 | One camera sentence in every video prompt. Use the maker's terms: static, locked-off, POV, dolly, push in, handheld. A subject that travels (roll out, stand up, crouch in) gets a cut or a camera that follows, never "locked". One panel camera preset at most and the text must match it. | SOURCED G1, G2, R1, A1. PROVEN F11 (garage 2, 3, 6 to 10) | Garage 13 had none and the door moved by itself (PROPOSED link) |
| R10 | Audio: say it in its own sentences (`SFX:`, `Ambient noise:`, quoted speech) or turn Audio off in the panel and write no audio words. Never write "no music, no dialogue". | SOURCED G1, G2, K1, B1. All 18 clips have 0 audio streams (ffprobe 2026-11-22) | |
| R11 | Timing: prose or ranges `[00:00-00:02]`, continuous, no gaps. Point times ("at 4 seconds") are documented only for Seedance 2.5 (B1). Do not ask for "no pause" or "accelerating". Speed is a verb: gallops, pushes, snaps. Do not request slow motion unless wanted. | Ranges SOURCED G2, B1, R1. PROVEN: point time "at 4 s" and "accelerating" failed in 6 runs | |
| R12 | Name each object by visible shape and color, positive, once: "a flat open-end combination wrench, a straight steel bar with a U-shaped jaw". Same wording in every clip of the project. | SOURCED G1, K1. PROVEN 3 clips (F16, F2) | |
| R13 | Change one thing per retry. Three failed tries of one shot: redesign (new shot, new engine, or cut), do not strengthen the sentence. Record every try. | SOURCED R2 ("one element at a time"). PROVEN F18 | |
| R14 | Never rely on the model for a logo, lettering, plate or numerals. Composite them in the start frame (Photoshop) or on the edit (Premiere). | PROVEN F3 (2 of 2). SOURCED B1 (text misspelling FAQ) | |
| R15 | Reference images each get a role in the prompt. Veo: up to three asset images, 8 s clips only, Veo 3.1 Lite takes none. | SOURCED G2, G3, G4, K1, B1 | Not run on Zac's account |
| R16 | Draft cheap, final once. Draft at the lowest resolution that shows the idea (Luma: 720p drafts, 1080p finals; Adobe Firefly Video: 540p preview). Zac reads the credit number at the Generate button and writes it in settings.txt. No credit number is ever estimated by an agent. | SOURCED L1, A1 | |
| R17 | Faces and hands in a start frame must be clean. Fix the still, not the prompt. | PROPOSED (old guide cites Runway, snippet only). PROVEN-ish garage 1 (wrong tool in hand) | |

## Per-engine templates

Everything the engine takes is shown. "Panel check" = Zac confirms at the panel, Adobe's own help pages are blocked to me (A4).

### Veo 3.1, Veo 3.1 Fast, Veo 3.1 Lite (Google, engine of every clip so far)
Template (G2): `[Cinematography]. [Subject]. [Action]. [Context]. [Style and ambiance]. SFX: ... Ambient noise: ...`
Shot sequence (G2): `[00:00-00:02] shot... [00:02-00:04] shot...` continuous ranges.
- Durations 4, 6, 8 s. 24 fps. 720p and 1080p (4K on full Veo 3.1 only) (G3).
- First and last frame: Veo 3.1 and Fast yes (G3, G4). Lite lists it as a capability. Describe the transition between the two in the prompt (G2). Whether Firefly offers the End slot on each tier: panel check.
- Reference images: up to 3 asset images (a person, character or product), 8 s only, not on Lite (G3, G4). Firefly: "frames or reference images" per a snippet (A4). Panel check.
- Negative language: none in the main prompt (G1).
- Seed and credit: not in Google's pages. Read the panel.
Skeleton (video with start frame, motion only): `Static camera at floor level. The man's right hand, nearest the camera, turns the wrench in small back-and-forth motions. [00:03-00:05] His head turns slowly toward the doorway. He holds that look until the end. Warm work lamp light, dust drifting, film grain.`

### Kling 3.0, 3.0 Omni, 4.0 (Kuaishou)
Template (K1, 4.0): `[Asset Roles] [Overall Settings] [Sequence of Events] [Audio]`. Start frame: `Use @Image1 as the first frame, then describe what happens next.` Both frames: `Use @Image1 as the first frame and @Image2 as the last frame, then describe the process in between.`
- Multi-shot is on by default in 4.0 (K1). For one clean action ask for a single shot in the first sentence. Whether the panel has a switch: panel check.
- Firefly: a first frame is mandatory for Kling (A4 snippet). Negatives: only "no subtitles" and "no background music" (K1). 4.0: 3 to 30 s, keyframes up to 10 (K1). 3.0: 3 to 15 s (K3).
- Physics is written as its own sentence describing how a body or material responds (K1 example "PHYSICS: ...").

### Seedance 2.5 (ByteDance, Firefly menu since 2026-11-22)
Template (B1): one-sentence summary `Subject + Location + Event + Genre/Style + Camera movement`, then timeline in 1-second integer ranges `0-3 seconds ... 3-7 seconds ...` with no gaps, then "Additional Notes" (what must stay constant).
- First and last frame by text: `Image 1 is the first frame.` `Image 3 is the first frame, and Image 5 is the last frame.` Keyframes: `Use Images 1 to 7 in order as keyframes.` (B1)
- Camera terms written directly, "first-person perspective" is listed (B1). Negatives: only subtitles and audio. Up to 30 s. Point-time control ("At the 2-second mark ...") is supported (B1).
- Do not use timestamps for high-frequency actions (B1). Panel check for which inputs Firefly exposes.

### Runway Gen-4.5
Text to video (R1): `[Camera] shot of [a subject] [action] in [environment]. [Supporting descriptions]`. Image to video (R2): motion only, `The camera [move] as the subject [action].` Unwanted cuts: add the phrase "Continuous shot" (R2 gives "Continuous, seamless shot").
- Positive phrasing, no conflicts (R2). Timestamps are rough, pair them with a plain sentence (R1). End frame for Gen-4.5: NOT VERIFIED (Runway page blocked).

### Luma Ray3.14, Ray3.14 HDR, Ray3
Template (L1, old guide S6): `Create a video of [SUBJECT] [MID-ACTION VERB] in [SETTING], [SECONDARY MOTION], [CAMERA], [LIGHTING]`. About 100 words, present tense. Positive only. With keyframes describe only what changes (L1). 5 s image to video, 720p for drafts (L1). Start frame `frame0`, end frame `frame1` (L2). No native audio (add sound in the edit).

### Flux 3 Video (Black Forest Labs, Firefly menu since 2026-11-22)
Five-part checklist (F2): subject and action; camera direction; scene and atmosphere; motion qualities; continuity constraints. Write the continuity line as a positive sentence ("The shield, the wolf emblem and the lane stay as in the first frame"). Start frame: "your image sets the opening frame and the prompt drives the motion" (F3). Start plus end: keep the two frames close in subject, scene and camera, a wide gap is less predictable (F3). Two or three beats for a 5 s clip (F4). Hard cut word: "Mark a hard cut where the angle changes" (F4).

### Firefly Video (Adobe first-party model)
Template (A1): `Shot type description + character + action + location + aesthetic`. Panel: Shot size, Camera angle, one Motion preset, first and optional last frame. A first frame turns off Shot size and Camera angle, an end frame turns off Motion (A4, snippet only, panel check). Text must match any preset chosen. Default 540p for a preview (A1).

### Firefly Image (stills and start frames)
Template (A2, A3): short descriptive phrases, subject, action, setting, then style, color, lighting. No command words, full sentences not needed, longer is not better. References: Composition controls arrangement, Style controls look, a strength slider, four variations per click (A2). Content type Photo for photoreal. Negative or Exclude box and seed: not documented in the pages I could read (A2), panel check. Never paste negatives into the main prompt.

## Which engine for which job (PROPOSED unless noted)
| Job | First choice | Why | Second choice |
|---|---|---|---|
| Static or slow scene with a person and one small action, 8 s | Veo 3.1 with a start frame | Only engine with evidence on Zac's account (18 clips). Best clip (garage 5) is this | Kling 4.0 with the start frame (maker template for start frame) |
| A shot that must END in a given picture (rest against the boot) | Veo 3.1 or 3.1 Fast with first and last frame | Both frames supported (G3, G4). Method is Google's own (G2) | Luma Ray3.14 keyframes, describe only what changes (L1) |
| First-person charge, fast camera | Veo 3.1 Fast draft then 3.1 | Evidence in hand. POV is a listed camera term (G1) | Seedance 2.5 ("first-person perspective" is listed, B1). Untested |
| Impact with debris (the lance strike) | Veo 3.1 from a start frame at the contact | One short beat, 4 s, one object | Kling 4.0, write a PHYSICS sentence (K1) |
| A logo, text, plate | Never a model. Photoshop and Premiere (R14) | F3 | none |
| Stills and start frames | Firefly Image (Photo), Composition or Style reference | Adobe documents both (A2) | none |

## PANEL facts, Firefly Generate image (Zac read them off his panel 2026-11-25, tag PROVEN)
- No negative or exclude box. Every still prompt must work alone, and the unwanted list becomes a short "reject when you eyeball the variations" note for Zac.
- A Seed field exists (Zac never used it). Record the seed per attempt in settings.txt. Keeping the same seed on a one-change redo: UNTESTED, and UNTESTED whether it helps with Nano Banana.
- Prompt character limit: unknown to Zac. Keep prompts under 730 characters, tell Zac "paste it, if the panel cuts it, tell us where it stopped".
- References: NO strength slider. Up to THREE reference images, OR a first frame and last frame, never both at once. So write each reference's job into the prompt in plain words ("take only the grade and grain from the first image", or a two-line edit: change, then keep as in the source). Do not write Composition or Style strengths.
- Image model Zac uses: Nano Banana, a Google partner model inside Firefly, not Adobe's own model. Plain-language edit wording for it: UNTESTED on our account. Commercial safety and indemnity of partner models: NOT VERIFIED (only Adobe's own Firefly models are marked commercially safe in `memory	opicsirefly-models.md`). Say so on any sheet that uses a partner model.
- End slot: not used for stills.
First used on the Ian 16:9 sitting sheet v2, 2026-11-25.

## Pre-flight checklist (every prompt passes ALL of it before it goes to Zac)
Run by the agent that wrote the prompt, in this order. Record the result on the settings line `preflight`.
1. `python D:\WKP\data\firefly-prompt-guide\prompt_lint.py --file <prompts.md>` returns PASS or WARN, never FAIL. A WARN is explained in one line next to the prompt.
2. Engine and tier named. The template for that engine used (R3).
3. One body, one object, one action. Count the actions out loud. Handoffs and swaps absent (R6).
4. Geometry, side, logo, tool shape sit in the start frame, and the start frame exists as a file or a still prompt is attached (R7, R12, R14).
5. Contact or landing: end frame written, or a cut planned (R8).
6. Camera sentence present and compatible with the action (R9).
7. Audio decided: off, or written as SFX and Ambient lines (R10).
8. Timing written as ranges or plain verbs, no point times on Veo, no slow motion unless wanted (R11).
9. Every object named by its visible shape, same words as earlier clips (R12).
10. The panel facts the prompt depends on are checked against the PANEL facts block above. Any fact not in that block is listed as "Zac checks at the panel", not assumed.
11. settings.txt filled in as far as an agent can, blanks left for Zac (below). A log folder exists in `D:\WKP\data\firefly-prompt-log\`.
12. Every tip handed over is tagged SOURCED, PROVEN or PROPOSED. No credit number appears anywhere.
13. Retry rule written on the card: which ONE thing changes on attempt 2, and the redesign after attempt 3.

## settings.txt format (one per attempt, in the log folder; template `SETTINGS-TEMPLATE.txt`)
Plain `key: value` lines. An agent fills the top block, Zac fills the PANEL and RESULT blocks. Every field must be present, write `NOT SHOWN` if the panel does not show it. Never leave a field out.
- SHOT, ATTEMPT, DATE, ENGINE (exact menu name), TIER (Fast, Lite, Standard), RESOLUTION, ASPECT, FPS, DURATION, AUDIO (on or off)
- PANEL MODE (text, frames, reference), START FRAME file and how it was made, END FRAME file, REFERENCE files with role and strength, SEED, camera presets set in the panel, NEGATIVE FIELD text if the panel has one
- PROMPT FILE name, WORD COUNT, LINT result, PREFLIGHT result
- CREDIT READOUT BEFORE CLICK (copied from the Generate button, never estimated), CREDITS AFTER (from the account page, optional)
- RESULT (kept or failed), FAILURE CODES (F or D codes), ONE CHANGE FROM LAST ATTEMPT, OUTPUT FILE

## Workflow rules
- Ladder: draft on the cheapest tier at the lowest resolution that shows the idea, record the seed, change the words only. Final once on the target tier (R16). Same seed across tiers: UNTESTED.
- A start frame costs an image generation. Make it, check it at full size (hands, tool, logo, side), then use it.
- Cut-based redesign beats a stronger sentence. Two easy clips beat one hard clip (PROVEN, garage 12: the first 3 s were usable).
- After any result Zac reports, add a row to `LESSONS.md` the same turn.

## From the book (added 2026-11-24, candidates, NOT tested on Zac's account)
Source: C.N. Scott, AI Filmmaking Keyframe Prompt Library, pages Zac chose. Full notes and page cues: `BOOK-NOTES-CN-SCOTT-2026-11-24.md`. Nothing here overrides R1 to R17. Where the book conflicts with a rule above, the rule above wins until a test says otherwise (tests T1 to T12 in the notes, one change per run). Tags: SOURCED-book means the book says it, PROPOSED means our rule.

| Id | Rule | Tag |
|---|---|---|
| B1 | Work in stages: place, extra views of the place, characters, group scenes, sketch, keyframes from the sketch, narrow edits, then video. | SOURCED-book |
| B2 | One master reference image per character and per location. Reuse it as the reference for every later still. Fits R15. | SOURCED-book |
| B3 | A bible per character (face, hair, build, costume, lens, light, grade) and per place (architecture, layout, materials, props, light, lens, grade). | SOURCED-book, fields only |
| B4 | An edit prompt has two lines: the one change, then what stays the same, written positively ("keep X as in the source"). | structure SOURCED-book, wording PROPOSED |
| B5 | One edit per pass. Same idea as R13. | SOURCED-book pattern, strict rule PROPOSED |
| B6 | Pose and framing matter: make a plain black and white sketch first and render from it. | SOURCED-book, UNTESTED |
| B7 | Back view, plan view and a 3 by 3 sheet of camera positions of a place before placing people. | SOURCED-book, UNTESTED |
| B8 | Same lens focal length across the shots of one sequence. | SOURCED-book |
| B9 | Change time of day or light as its own pass, architecture and objects kept. | SOURCED-book |
| B10 | Nine-point check before any frame becomes a start frame: identity, costume, place, camera language, light direction, grade, scale, perspective, time of day. | SOURCED-book |
| B11 | Compare each new image with its master, write the differences as the next prompt, change only those. | SOURCED-book, wording PROPOSED |
| B14 | Fix hands in a dedicated pass with pose and face kept, check at full size before the still becomes a start frame. Extends R17. | PROPOSED (book is silent on hands) |
| B17 | No long quality stacks or camera-body specs until a test shows they change a Firefly still. | PROPOSED |
