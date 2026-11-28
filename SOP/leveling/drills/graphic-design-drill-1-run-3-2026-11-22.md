# Drill 1, attempt 3 (author: graphic-design, 2026-11-22). Attempts 1 and 2 FAILED (grade files kept). Awaiting qa-director re-grade.

UNDRILLED: until a grader signs PASS, every output of this agent carries the line UNDRILLED and goes through the director first.

Disclosure unchanged: Part A is a paper replay after reading the audit, so A7 is weak evidence. Tag meanings: SOURCED = maker or platform page retrieved 2026-11-22 (verbatim quote and id); PROVEN = two or more logged results in our own clips, paths named; PROPOSED = our idea, with the cheapest test. Source ids are in `D:\WKP\data\firefly-prompt-guide\SOURCES-2026-11-22.md` plus Y1, E1, C1 in the Craft Brief. No credit number appears anywhere; Zac reads it at Generate (NOT RETRIEVED).

Attempt 3 fixes (grade 2 items 1 to 8): wrench-failure citation corrected, composited-art tag changed, unverified A2 line unquoted, every instruction tagged, camera terms quoted or tagged PROPOSED, start frames come from the .mp4 first frame, the Luma figure removed, checklists ticked with proof.

## Part A (one action per clip, 4 s, Veo 3.1 Fast draft then Veo 3.1)
Settings, all three: RESOLUTION 720p draft, ASPECT 16:9, FPS 24, DURATION 4 s, AUDIO off, PANEL MODE frames, END FRAME none, SEED NOT SHOWN (Zac checks), CREDIT READOUT blank for Zac. Draft on Fast, keeper on full Veo 3.1 [PROPOSED, no maker page tested on our account; the first draft is the cheapest test]. 24 fps and 4 s are SOURCED G3: "Video lengths: 4, 6, or 8 seconds".

```prompt
ID: D2-garage4
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera at floor level. The man's right hand, the hand nearest the camera, holds a flat open-end combination wrench, a straight steel bar with a U-shaped jaw, on the bolt and turns it in small back-and-forth motions. His left hand rests open on the creeper. Dust drifts in warm light.
```
- Actions: 1 (the wrench turns). Beats: 1. The head turn is a separate clip with its own start frame (the last frame of this one) [SOURCED F4: "Keep each beat achievable [em dash in source] two or three for a 5-second clip."].
- Start frame: yes. The Video 4 log folder holds only the .mp4 and notes, so export its first frame with ffmpeg (ffmpeg -i <mp4> -frames:v 1 first.png) and check it at full size for the wrench shape [PROPOSED provenance].
- Camera: the maker page lists camera moves and angles but I hold no verbatim quote naming "static", so "Static camera" and "at floor level" are PROPOSED. One camera sentence first follows G2 [SOURCED G2: "[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]"].
- One hand on the tool, the other empty and resting [PROVEN, LESSONS F16, 3 clips: a second hand steadying the tool produced a wrench turning a wrench in garage 2 and 3, and clip 5 with one hand on it was the best result; log folders Video 2, Video 3, Video 5].
- Tool named by shape, once [SOURCED K1: "Describe visual details as explicitly as possible"].
- Audio off in the panel, no audio words [SOURCED G1: "Clearly specify if you want audio."]. Panel switch NOT VERIFIED, Zac checks.
- "His left hand rests open on the creeper" [PROVEN F16 as above]. "Dust drifts in warm light" is ambience [PROPOSED, no test]. Label: AI-generated if public [house rule, not a model tip].
- Cheapest test [PROPOSED]: this exact 4 s prompt at 720p on Fast. Credit cost NOT RETRIEVED.
- Predicted failure: wrench changes shape (known result: it vanished when he sat up) [PROPOSED]. Retry 1 changes only the wrench sentence; redesign after 3.

```prompt
ID: D2-garage4b
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera at floor level. The man's head turns slowly toward the open garage door and holds that look until the end of the clip. Dust drifts in warm light.
```
- Start frame: the final frame of D2-garage4 exported from the accepted clip (Premiere Export Frame, or ffmpeg last-frame grab). Actions: 1.

```prompt
ID: D2-garage7
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera at floor level. The man's right hand, the hand nearest the camera, holds one flat open-end wrench, a straight steel bar with a U-shaped jaw, on a bolt and turns it in small back-and-forth motions. His left hand rests open on his chest. Dust drifts in warm light.
```
- Redesign: the old clip packed a turn, an offering and a return [PROVEN failed 6 of 6, `Video 6` to `video 10` notes]. The offering becomes a later clip (start frame: a still of the extended hand) joined by a cut. Actions: 1.
- Start frame: yes, first frame exported with ffmpeg from the .mp4 in the video 7 folder (it holds no still), checked at full size [PROPOSED provenance]. "His left hand rests open on his chest" [PROPOSED, one hand on the tool follows F16]. Camera and ambience lines as garage 4, PROPOSED.
- No second person or tool is named, so none is invited [PROVEN: "someone shorter" produced a second person, `video 7` note].
- Cheapest test: this 4 s draft. Credit cost NOT RETRIEVED. Predicted failure: wrench doubles [PROPOSED]. Retry 1 changes only the camera sentence; redesign after 3.

```prompt
ID: D2-garage11
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera. The man bends from the waist and lowers his right arm, the arm nearest the camera, straight down. His hand closes around the baseball and lifts it to hip height. He holds it in his palm until the end of the clip.
```
- Start frame: yes. Made as one Firefly Image generation, Photo, 16:9: a man in a black t-shirt standing in a dim garage framed from the thighs down, a worn white leather baseball on the concrete floor at his feet, the red Mustang out of focus behind [PROPOSED prompt, the old start frame showed only the ball and the model invented how the hand arrived, `video 11` note]. The prompt does not re-describe the picture [SOURCED R2: "Effective image to video text prompts focus almost exclusively on motion."].
- Camera "Static camera" PROPOSED (no verbatim maker quote held). Bend, grasp and lift are one reach but three verbs, a test risk [PROPOSED]; if draft 1 shows two sub-actions, the one change on attempt 2 is to shorten to "he reaches down and lifts the baseball". Predicted failure: he drops to hands and knees again [PROPOSED, mitigated by the framing]. Retry 1 changes only "bends from the waist" to "crouches on his heels"; redesign after 3 (hand-only plate and a cut).
- Cheapest test: this 4 s draft at 720p. Credit cost NOT RETRIEVED.

## Part B (Firefly Image; order used: subject, setting, style, colour, lighting, as the Adobe labels list them [SOURCED A3: Subject, Background, Image type, Style, Colour, Lighting, Action])
Panel facts: Content type Photo [A2 presents Photo as the photorealistic choice, paraphrase from the 2026-11-22 fetcher text, wording unverified; Zac confirms the setting at the panel]. Four variations per click [SOURCED A2]. Negative box: not relied on. C1 full Sep 18, 2025 reply (COMMUNITY, not an Adobe employee): "Right now, the model doesn't understand negative prompts, so adding it to a prompt will add it to your image." and the same reply then suggests a parameter written "[avoid=xxx]". Whether that parameter works is UNTESTED. Test for Zac, one try, only if he wants it: add "[avoid=text]" to the end of one prompt and compare the four variations to a run without it. Output pixel size NOT VERIFIED.

```prompt
ID: D2-B1-etsy
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph of a tall empty natural oak frame with a white mat hung at the center of a pale gray plaster wall in a living room, a green linen sofa below it and a small side table with a ceramic vase of dried grasses at the right, photographic style, calm warm neutral colors, soft daylight from the left.
```
- Spec [E1 verbatim]: "The first photo in a listing should be horizontal (landscape) or square."; "We recommend your listing photos have a width and height of at least 2000 pixels or more."; "Make sure the most important part of the item is focused in the center." Aspect 4:3 landscape [SOURCED A2 tutorial uses 4:3].
- Art placed in the mat in Photoshop or Express [PROPOSED. Reason: LESSONS F3 shows a model redraws a logo it is asked to make (Partly PROVEN, 2 clips); there is no logged still with composited art. Cheapest test: place one finished print in the first image and check it at 100 percent].

```prompt
ID: D2-B2-social
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph of a homecoming at a small town park, an American flag with thirteen stripes and white stars on a blue field flying high on a tall pole at the right, service members of every age in uniform, a gray-haired veteran, a young soldier, a woman sailor and a middle-aged Marine, embracing their families, the top third of the frame a smooth clear pale evening sky, photographic style with shallow depth of field, rich warm colors, golden hour sunlight.
```
- House rules [memory feedback-always-include-flag.md]: flag in and correct, people shown, all generations and branches, no weapons, no insignia text; label AI-generated. Overlay headline in code or Express [house rule feedback-code-made-art.md]. Meta spec NOT RETRIEVED. Fallback: Generative Fill the top third. Retry changes only the sky sentence.

```prompt
ID: D2-B3-thumb
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph of a bronze-armored cavalry officer on a rearing chestnut horse at dawn on a dusty plain, rider and horse in the right third of the frame, mounted soldiers fading into haze behind, the left third an open dark brown plain under a low orange sky, cinematic style, warm orange and brown colors, dramatic side light.
```
- Spec [Y1 verbatim]: "try to upload a thumbnail with an aspect ratio of 16:9"; "Have a resolution of 3840 x 2160 pixels for videos" is the page's recommendation, Firefly output size NOT VERIFIED so Zac upscales or exports to 1920 x 1080 minimum and keeps the file under "2 MB for video thumbnails" on mobile; "a minimum width of 640 pixels for videos".
- Not a WWD thumbnail. Text and logo in code over the left third. Fallback: Generative Fill the left third. Retry changes only the lighting phrase.

## Checklists run on this file, each tick with its one-line proof
Video card (D2-garage4, 4b, 7, 11):
1. Lint: PASS 7 of 7 (graphic-design-drill-1-lint-3-2026-11-22.txt).
2. Template: each prompt is camera, subject, action, context.
3. One action per clip: 4 turns the wrench, 4b turns the head, 7 turns the wrench, 11 one reach (three verbs, risk noted).
4. Start frame: first frame of the named .mp4 via ffmpeg for 4 and 7, the last frame of 4's accepted clip for 4b, a Firefly Image still for 11 (prompt written).
5. Contact or landing: none in this set, n/a.
6. Camera sentence present on every prompt, tagged PROPOSED.
7. Audio: off, no audio words in any prompt.
8. Timing: no ranges, plain verbs only.
9. Negation: lint R1 count 0.
10. Settings block: written once at the top, credit blank.
11. Tags: every bullet ends in a tag; ambience, camera and hand lines are tagged PROPOSED or PROVEN (F16).
12. Log folder names: garage-4, garage-4b, garage-7, garage-11 under D:\WKP\data\firefly-prompt-log\.
Image card (D2-B1, B2, B3):
1. Lint PASS. 2. Zero negation (lint R1). 3. Order subject, background, style, colour, lighting, the last clause is lighting in all three. 4. No text or logo asked, overlay planned in code or Express. 5. Spec lines with E1 and Y1 quotes, Meta NOT RETRIEVED. 6. Panel lines tagged, the A2 photo line marked unverified. 7. House rules on B2: flag, people, generations. 8. B3 is not a WWD thumbnail. 9. Fallback and retry on each card. 10. No credit number. 11. No em dash in new text (grep).
Redo plan: each card names retry 1 (one change) and a redesign after 3.
