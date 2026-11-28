# Drill 1, attempt 2 (author: graphic-design, 2026-11-22). Attempt 1 FAILED (grade file kept). Awaiting qa-director re-grade.

UNDRILLED: until a grader signs PASS, every output of this agent carries the line UNDRILLED and goes through the director first.

Disclosure unchanged: Part A is a paper replay after reading the audit, so A7 is weak evidence. Tag meanings: SOURCED = maker or platform page retrieved 2026-11-22 (verbatim quote and id); PROVEN = two or more logged results in our own clips, paths named; PROPOSED = our idea, with the cheapest test. Source ids are in `D:\WKP\data\firefly-prompt-guide\SOURCES-2026-11-22.md` plus Y1, E1, C1 in the Craft Brief. No credit number appears anywhere; Zac reads it at Generate (NOT RETRIEVED).

Fixes made after the FAIL (numbered as in the grade file): 1 tags cleaned, 2 one action per clip, 3 start-frame provenance, 4 verbatim quotes, 5 durations match, 6 image order, 7 C1 completed, 8 Y1 resolution, 9 checklists ticked below, 10 checklist items trimmed, 11 garage 11 trimmed.

## Part A (one action per clip, 4 s, Veo 3.1 Fast draft then Veo 3.1)
Settings, all three: RESOLUTION 720p draft, ASPECT 16:9, FPS 24, DURATION 4 s, AUDIO off, PANEL MODE frames, END FRAME none, SEED NOT SHOWN (Zac checks), CREDIT READOUT blank for Zac. Engine tier [PROPOSED: Fast for the draft is Luma's opinion L1 "Use Veo 3.1 Fast model (~70% cheaper and 2x faster) for testing", COMMUNITY]. 24 fps and 4 s are SOURCED G3: "Video lengths: 4, 6, or 8 seconds".

```prompt
ID: D2-garage4
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera at floor level. The man's right hand, the hand nearest the camera, holds a flat open-end combination wrench, a straight steel bar with a U-shaped jaw, on the bolt and turns it in small back-and-forth motions. His left hand rests open on the creeper. Dust drifts in warm light.
```
- Actions: 1 (the wrench turns). Beats: 1. The head turn is a separate clip with its own start frame (the last frame of this one) [SOURCED F4: "Keep each beat achievable — two or three for a 5-second clip."].
- Start frame: yes, the existing red Mustang still in the garage-4 log folder `D:\WKP\data\firefly-prompt-log\Video 4` (the first frame Zac used), checked at full size for the wrench shape. Geometry lives in it [SOURCED F3: "your image sets the opening frame and the prompt drives the motion."].
- Camera: "Static camera" [SOURCED G1 lists static among camera terms; maker quote in G1: "Some advanced camera angles are not officially supported."]. "at floor level" is our wording [PROPOSED].
- One hand on the tool, the other empty and resting [PROVEN: wrench turning a wrench when two hands held tools, garage 6 and 7 in `Video 6`, `video 7`; two logged results].
- Tool named by shape, once [SOURCED K1: "Describe visual details as explicitly as possible"].
- Audio off in the panel, no audio words [SOURCED G1: "Clearly specify if you want audio."]. Panel switch NOT VERIFIED, Zac checks.
- Label: AI-generated if public [house rule, not a model tip].
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
- Start frame: yes, the working-hands still from `Video 7` log folder (first frame), or one Firefly Image generation made from the D2-B-style prompt rules, checked at full size [PROPOSED].
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
- Actions: 1 (bend, grasp, lift read as one reach). Predicted failure: he drops to hands and knees again [PROPOSED, mitigated by the framing]. Retry 1 changes only "bends from the waist" to "crouches on his heels"; redesign after 3 (hand-only plate and a cut).
- Cheapest test: this 4 s draft at 720p. Credit cost NOT RETRIEVED.

## Part B (Firefly Image; order used: subject, setting, style, colour, lighting, as the Adobe labels list them [SOURCED A3: Subject, Background, Image type, Style, Colour, Lighting, Action])
Panel facts: Content type Photo [SOURCED A2: Photo is "to generate a photorealistic image instead of an illustration"]. Four variations per click [SOURCED A2]. Negative box: not relied on. C1 full Sep 18, 2025 reply (COMMUNITY, not an Adobe employee): "Right now, the model doesn't understand negative prompts, so adding it to a prompt will add it to your image." and the same reply then suggests a parameter written "[avoid=xxx]". Whether that parameter works is UNTESTED. Test for Zac, one try, only if he wants it: add "[avoid=text]" to the end of one prompt and compare the four variations to a run without it. Output pixel size NOT VERIFIED.

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
- Art placed in the mat in Photoshop or Express [PROVEN: F3 logos drawn wrong 2 of 2, `Joust opener` notes]. Fallback: Generative Fill the frame. Retry changes only the lighting phrase.

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

## Checklists run on this file (video card, image card, redo plan), ticked with proof
Video card: 1 lint (see lint file attempt 2) ticked; 2 template order, ticked (camera, subject, action, context); 3 one action per clip, ticked, counts written; 4 start frame provenance, ticked for all four; 5 contact: no contact shots in this set, n/a; 6 camera sentence, ticked; 7 audio off, ticked; 8 ranges: none used, plain verbs, ticked; 9 no negation, no "as if", ticked by lint; 10 settings block, ticked, credit blank; 11 tags, ticked; 12 removed from the look-at-file list (lesson row happens after a result).
Image card: 1 lint ticked; 2 zero negation ticked; 3 order ticked (subject, setting, style, colour, lighting); 4 no text asked ticked; 5 spec lines ticked with E1 and Y1, Meta NOT RETRIEVED; 6 tags ticked; 7 house rules ticked on B2; 8 not WWD ticked; 9 fallback and retry ticked; 10 no credit figure ticked; 11 slop and em dash: grep shows none in new text, ticked.
Redo plan: applies to the retry lines above, items 1 to 7 ticked, 8 and 9 happen after a result.
