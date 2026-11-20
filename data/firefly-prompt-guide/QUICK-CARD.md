# Firefly Video QUICK CARD (one page, read before every video prompt)

2026-11-18. Tags: M maker-documented, C community, U untested. Full detail and sources in `Firefly-Video-Prompting-Guide.md`. Then read `LESSONS.md`.

## Rules for every engine
- Positive picture only. Write "stops against the outside of the boot", never "does not hit the toe". [M]
- One action per clip. Under 100 words. 4 to 5 seconds, cut it shorter in the edit. [M/U]
- Name the hand and side in camera-relative words ("his right hand, the one nearest the camera"). Fix it in a start frame. [U/C]
- Wrong hand, wrong foot, wrong side = fix the START FRAME, not the prompt. [C/M]
- Contact = give it an END frame if the panel has one, or cut on the contact, or frame it out. [M/U]
- Change one thing per try. Three failed tries = redesign the shot. [M/U]
- Write down model, resolution, ratio, fps, duration, audio, seed, credit readout. Read the credit number before you click.

## Per engine

**Firefly Video (Adobe)**
- DO: cover style, shot size, camera angle, camera motion. Keep panel presets and prompt text matching. [M snippet]
- DO: expect first frame to disable Shot size and Camera angle, end frame to disable Motion. [M snippet]
- DON'T: pick a motion preset that fights the text. DON'T count on audio. [M snippet/U]

**Veo 3.1 / Fast / Lite (Google)**
- DO: [Cinematography] + [Subject] + [Action] + [Context] + [Style]. Audio in separate sentences: quotes for speech, `SFX:`, `Ambient noise:`. [M]
- DO: first and last frame, describe the transition between them. Timestamps `[00:00-00:02]` for steps. [M]
- DON'T: "no X" wording. DON'T trust text on screen. Contact on a person can get softened, reword around the object. [M/C]
- Clips run 4, 6 or 8 seconds. Test on Fast or Lite first. Seed carry-over Fast to Standard: unverified. [M/C/U]

**Gemini Omni Flash**
- DO: describe the whole scene in plain language, state the purpose, plain camera words. [C]
- DON'T: write long prescriptive rules, Google says it needs less. DON'T use "Cut to" in a one-action clip. [C/U]
- Physics about 50 percent in one vendor test. Run takes, keep the best. [C]

**Kling 3.0 / 3.0 Omni / 2.5 Turbo**
- DO: subject, action, setting, camera, light, mood. Describe only what viewers can see. [M]
- DO: Firefly needs a START FRAME for Kling. Prompt = how the scene evolves from it. [M snippet/C]
- DO: one shot for one action. Multi-Shot (up to 6) is for sequences. [M/C]
- DON'T: pronouns for speakers, vague motion words. 2.5 Turbo is the cheap drafter. [C]

**Runway Gen-4.5**
- DO: image to video prompt = motion only. "The camera [move] as the subject [action]." [M]
- DO: clean start frame. Blurry hands get worse. Remove motion blur from the still. [M]
- DO: "locked-off camera remains perfectly still", "Continuous shot" for unwanted cuts. [M]
- DON'T: negatives, conflicting instructions, multi-paragraph prompts. No end frame for Gen-4.5 per Runway help. [M/M snippet]

**Luma Ray (3.14, 3.14 HDR, 3, 3 HDR, 2)**
- DO: mid-action verb ("rolling"), a secondary consequence (dust, wobble), a named camera move, 100 words, present tense. [M]
- DO: keyframes, describe only what CHANGES. Draft at 720p, final at 1080p. [M]
- DON'T: "begins to", "starts to", vibrant, whimsical, hyper-realistic, beautiful, stunning, any negative. No native audio. [M]
- End-frame slot in Firefly for Luma: not verified, check the panel. [U]

## Contact and hands, fastest fixes
1. Clean start still with the right hand on the wrench. 2. End still with the ball resting against the boot. 3. Prompt describes the roll only, positive end state. 4. Cut on the contact. 5. Flip the clip in Premiere ONLY if nothing in frame is text, plate or emblem.
