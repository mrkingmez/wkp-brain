# Firefly and video-model QUICK CARD (v2, 2026-11-22, one page)

Rewritten after the audit. The full standard is `STANDARD.md` (read it first for any real job). Sources and quotes: `SOURCES-2026-11-22.md`. Why the old card failed: `AUDIT-2026-11-22.md`. Tags: SOURCED (maker page), PROVEN (Zac's clips), PROPOSED (mine, untested).

## The 10 lines
1. Write the picture you want in positive, observable words. Never "no, not, never, without, nothing, nobody, does not". Never caps or exclamation marks. [SOURCED Google, Runway, Kling, Luma, Seedance. PROVEN 5 clips]
2. Use the engine's template: Veo = [Cinematography] + [Subject] + [Action] + [Context] + [Style], then audio sentences. [SOURCED Google]
3. One body, one object, one action per clip. A handoff or swap is two clips and a cut, or two stills and a dissolve. [PROVEN 6 of 6]
4. The start frame decides who, where, which side, the logo and the tool shape. With a start frame, the prompt gives motion only. [SOURCED Runway, BFL, Kling. PROVEN]
5. Contact or "ends resting against": give a last frame on an engine that takes one, write the end as a resting picture, or cut on the contact. Never write "bumps". [SOURCED Google, BFL, Luma. PROVEN garage 12]
6. One camera sentence in every prompt. A body that travels (roll out, stand up) needs a cut, not a locked camera. [SOURCED Google. PROVEN]
7. Audio: write `SFX:` and `Ambient noise:` sentences or switch Audio off and write nothing. Never "no music". [SOURCED Google]
8. Name each object by visible shape, once, same words every clip. [SOURCED Google, Kling. PROVEN]
9. Logos, lettering, plates: never the model. Composite in the start frame or in Premiere. [PROVEN]
10. One change per retry. Three misses = redesign the shot. Write settings.txt every attempt, read the credit number at the Generate button, never estimate it. [SOURCED Runway. PROVEN]

## Before a prompt goes to Zac (pre-flight, all of it)
`python D:\WKP\data\firefly-prompt-guide\prompt_lint.py --file <prompts.md>` must show no FAIL. Then the 13-point checklist in `STANDARD.md`. Then settings.txt from `SETTINGS-TEMPLATE.txt`.

## Engine one-liners (full templates in STANDARD.md)
- **Veo 3.1 / Fast / Lite**: 4, 6 or 8 s, 24 fps. First and last frame: Veo 3.1 and Fast yes. Reference images up to 3, 8 s only, not Lite. Timestamps `[00:00-00:02]`, continuous. [SOURCED Google]
- **Kling 3.0 / 4.0**: `Use @Image1 as the first frame, then describe what happens next.` Multi-shot is on by default in 4.0, ask for a single shot. Negatives only for subtitles and music. A PHYSICS sentence is in the maker's template. [SOURCED Kling]
- **Seedance 2.5**: one-sentence summary, then 1-second timeline with no gaps, `Image 1 is the first frame.` Negatives only for subtitles and audio. [SOURCED ByteDance, updated 2026-11-19]
- **Runway Gen-4.5**: image to video = motion only. "Continuous shot" for unwanted cuts. No contradictions. [SOURCED Runway]
- **Luma Ray3.14**: mid-action verb, about 100 words, present tense, start and end keyframes, describe only what changes, 720p drafts. No negatives. No audio. [SOURCED Luma]
- **Flux 3 Video**: subject and action, camera, scene, motion qualities, continuity sentence. Start frame sets the opening frame. Keep start and end frames close. [SOURCED BFL]
- **Firefly Video**: Shot type + character + action + location + aesthetic. One panel camera preset, say another in the text. A first frame turns off shot size and angle, an end frame turns off motion (snippet, panel check). [SOURCED Adobe Learn, partly SNIPPET]
- **Firefly Image**: short descriptive phrases, no command words, Composition reference = layout, Style reference = look, strength slider, 4 variations. Negative box and seed: not documented, panel check. [SOURCED Adobe Learn]

## Seen on Zac's clips (PROVEN)
- Named or negated things get drawn: spear, "does not get up", "NO ONE else", "NOTHING IN HIS HAND". (5 clips)
- Handoff or swap of two tools: objects vanish, duplicate, morph. (6 of 6)
- Locked camera plus a big body move re-frames the shot. Cut instead. (7 clips)
- Logo on a black start frame is shown as a title card and redrawn. Logo on the shield kept it. (2 of 2, 3 of 3)
- Our own words asked for three failures: "slow-motion beat" (slow strike), "settles ... and then strikes" (pause), "gently bumps" (bounce). Read your verbs.
- Best clip so far (garage 5): start frame, timed beats, a positive hold, one named tool.
- All 18 clips have 0 audio streams. Audio was off.
