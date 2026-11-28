# Drill 1 run (author: graphic-design, 2026-11-22). Awaiting qa-director grade.

Source ids: G1 to G4, A1, A2, A3, K1, R2, L1, F3 are in `D:\WKP\data\firefly-prompt-guide\SOURCES-2026-11-22.md`. New today in the brief: Y1 (YouTube thumbnail help), E1 (Etsy listing photo help), C1 (Adobe Community, negative prompting). Brief: `D:\WKP\memory\agents\briefs\graphic-design-craft-brief.md`.

Global for every video card: Engine Veo 3.1 Fast for the draft, Veo 3.1 for the keeper. Panel check by Zac before the first click: is Audio off, is there a Start slot, is there a Seed field. Credit cost: NOT RETRIEVED, Zac reads the number at the Generate button and writes it in settings.txt. No credit figure appears in this file. Draft size 4 s, 720p [PROPOSED, the cheapest sizes G3 lists; Luma advises 720p for iteration, L1 COMMUNITY]. AI-generated label if public.

## Part A

```prompt
ID: D1-garage4
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera at floor level. The man's right hand, the hand nearest the camera, holds a flat open-end combination wrench, a straight steel bar with a U-shaped jaw, on the bolt and turns it in small back-and-forth motions. [00:03-00:05] Both hands rest on the wrench. [00:05-00:08] His head turns slowly toward the open garage door and he holds that look until the end of the clip. Dust drifts in warm light, soft film grain.
```
- Engine and tier: Veo 3.1 Fast draft, Veo 3.1 keeper [engine PROVEN for this shot class, 18 clips; tier split PROPOSED].
- Start frame: yes, the red Mustang still with the man on the creeper. Geometry (car nose to the right, door at the left) lives in the picture [SOURCED R2, F3; PROVEN F5 and F11 in LESSONS]. Made from the existing garage still, or one Firefly Image generation checked at full size for the wrench shape and hand.
- Camera: "Static camera at floor level" [SOURCED G1 lists static as a camera term, G2 puts cinematography first]. Safe because the man does not travel, only hands and head move [PROVEN-ish, garage 5].
- Timing: ranges [00:03-00:05] [SOURCED G2; R1 says timestamps are rough, so a plain sentence is paired].
- Tool named by shape, once [SOURCED K1 "as explicitly as possible"; PROVEN F16].
- Cheapest test [PROPOSED]: one 4 s Veo 3.1 Fast draft at 720p with beat 1 only (wrench turn). If the wrench stays one object, add the head turn on draft 2. Credit cost NOT RETRIEVED, Zac reads it at Generate.
- Predicted failure (known result: the wrench vanished when he sat up): the tool changes shape in the hand [PROPOSED]. Mitigation: named shape, no sit-up in this clip.
- Retry: attempt 2 changes only the wrench sentence; redesign after attempt 3 (head turn becomes its own clip) [SOURCED R2 one element at a time].

```prompt
ID: D1-garage7
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera at floor level. The man's two weathered hands, gray hair on the forearms, turn one flat open-end wrench, a straight steel bar with a U-shaped jaw, on a bolt in small back-and-forth motions. [00:04-00:08] His hands lower the wrench and rest it against his chest. Warm work lamp light, dust drifting, soft film grain.
```
- Redesign, not a stronger sentence (R6): the offering and receiving of a second wrench is dropped. The handoff becomes a cut to a second clip whose start frame shows the extended hand [SOURCED B1 too much packed in one range; PROVEN garage 6 to 10, 6 of 6 failed].
- Start frame: yes, the working-hands still. End frame: if Zac's Veo panel shows an End slot, a still of the wrench resting at his chest [capability SOURCED G3, G4; panel exposure NOT VERIFIED, Zac checks].
- No other person is mentioned anywhere, so none is invited [PROVEN: "someone shorter" produced a second person].
- Cheapest test: one 4 s draft, 720p, beat 1 only. Credit cost NOT RETRIEVED.
- Predicted failure: a second wrench appears or the first doubles [PROPOSED]. Mitigation: "one wrench" by its shape and no second tool mentioned.
- Retry: attempt 2 changes only the camera sentence; redesign after 3 (hands-only close shot, no chest rest).

```prompt
ID: D1-garage11
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera at knee height, framing the man from the thighs down beside a white leather baseball on the concrete floor. [00:00-00:03] He bends from the waist and lowers his right arm, the arm nearest the camera, straight down. [00:03-00:06] His hand closes around the baseball and lifts it to hip height. He holds it in his palm until the end of the clip. Warm low light, dust drifting.
```
- Start frame: yes, the man standing, ball at his feet, framed thighs down. The old start frame showed only the ball, so the model invented how the hand arrived and the man dropped to his knees [PROVEN-ish, garage 11 notes; SOURCED R2 image-to-video prompts focus on motion].
- Camera: static at knee height so the bend stays inside the frame [SOURCED G1 camera terms; the link to the fix PROPOSED].
- One body, one object, one action: bend, grasp, lift [SOURCED F4 two or three beats].
- Dust flying off the ball and back (old failure) is not invited: only ambient "dust drifting" stays [PROPOSED].
- Cheapest test: 4 s draft ending at the grasp, 720p. Credit cost NOT RETRIEVED.
- Predicted failure: he drops to hands and knees again [PROPOSED]. Mitigation: thighs-down frame and "from the waist".
- Retry: attempt 2 changes only "bends from the waist" to "crouches on his heels"; redesign after 3 (hand-only plate, cut to him standing).

settings.txt top block for all three (copy of SETTINGS-TEMPLATE.txt): ENGINE Veo 3.1 Fast, RESOLUTION 720p, ASPECT 16:9, FPS 24 [SOURCED G3], DURATION 4 s, AUDIO off, PANEL MODE frames, START FRAME file named, END FRAME none (garage 7 optional), SEED NOT SHOWN until Zac checks, CREDIT READOUT BEFORE CLICK blank for Zac. Log folders `garage-4`, `garage-7`, `garage-11` in `D:\WKP\data\firefly-prompt-log\` are made when run.

## Part B (Firefly Image, no result exists)
Panel facts for all three [tags]: Content type Photo [SOURCED A2]. Four variations per click [SOURCED A2]. Negative or Exclude box: not relied on. Adobe's own tutorial does not mention one [SOURCED A2], and an Adobe Community reply dated Sep 18, 2025 says the model "doesn't understand negative prompts, so adding it to a prompt will add it to your image" [C1, COMMUNITY, the poster is not an Adobe employee]. So every card runs with NO negatives. Output pixel size NOT VERIFIED, Zac reads it from the download.

```prompt
ID: D1-B1-etsy
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph of a bright living room wall, a tall empty natural oak frame with a white mat hung at the center of a pale gray plaster wall, a green linen sofa below it, a small wooden side table with a ceramic vase of dried grasses at the right, soft daylight from the left, shallow depth of field, calm warm neutral colors.
```
- Landscape 4:3 [A2 tutorial uses 4:3; E1: "The first photo in a listing should be horizontal (landscape) or square."]. Subject centered with space around it [E1: "Make sure the most important part of the item is focused in the center."; "Try to capture images of your item further back than you think you'll need."].
- Art goes into the empty mat in Photoshop or Express, never model-made (R14) [PROVEN F3].
- Size: E1 "We recommend your listing photos have a width and height of at least 2000 pixels or more." Zac checks the download [PROPOSED upscale if short].
- Fallback: Generative Fill on the frame area. Retry: change only the lighting phrase.

```prompt
ID: D1-B2-social
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph at golden hour of a homecoming at a small town park, an American flag with thirteen stripes and white stars on a blue field flying high on a tall pole at the right, a crowd of service members of every age in uniform, a gray-haired veteran, a young soldier, a woman sailor and a middle-aged Marine, embracing their families, warm sunlight, the top third of the frame a smooth clear pale evening sky, shallow depth of field, rich warm colors.
```
- House rules met: flag in, people shown, all generations and branches [memory feedback-always-include-flag]. No weapons, no readable text, no insignia written. No flag term is negated.
- Overlay: top third described as plain smooth sky, headline set in code or Express [PROVEN-ish: memory feedback-code-made-art; the 2026-11-21 AKT pair used the same method, result NOT SEEN].
- Platform size: spec source for Meta NOT RETRIEVED (the Meta help page returned no body text). Zac confirms the ratio.
- Fallback: Generative Fill the top third with a plain gradient. Retry: change only the sky sentence.

```prompt
ID: D1-B3-thumb
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph of a bronze-armored cavalry officer on a rearing chestnut horse at dawn on a dusty plain, the rider and horse in the right third of the frame, a long line of mounted soldiers fading into haze behind, the left third of the frame an open dark brown plain and low orange sky, dramatic side light, sharp focus, cinematic color grade.
```
- 16:9 [Y1: "try to upload a thumbnail with an aspect ratio of 16:9"]. Y1 also: "2 MB for video thumbnails" on mobile, JPG or PNG, minimum width 640. Zac checks the file is under 2 MB.
- Not WWD (Matt makes WWD thumbnails). For the WKP history channel or another Zac venture only.
- Headline, numbers and any logo are set in code over the left third (R14).
- Fallback: Generative Fill the left third. Retry: change only the lighting phrase.
- Predicted weakness: "longer prompts aren't always better" [A2]. If horse anatomy fails, drop the soldiers phrase first [PROPOSED].

## Lint
Real output of `python D:\WKP\data\firefly-prompt-guide\prompt_lint.py --file <this file>` is saved in `graphic-design-drill-1-lint-2026-11-22.txt`.
