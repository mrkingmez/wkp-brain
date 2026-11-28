# Percy Jackson intro "Trident Tide": optional Firefly and Veo shots (2026-11-23)

Author: wwd-vfx. Standard: `D:\WKP\data\firefly-prompt-guide\STANDARD.md` v2 (rules R1 to R17). NOTHING GENERATED. Credit cost: NOT RETRIEVED for every card (Zac reads the number at the Generate button and writes it in settings.txt, template `SETTINGS-TEMPLATE.txt`). Nobody can test a prompt without spending Zac's credits (Matt paid for them). The free code-built intro already ships without any of these shots, so both are upgrades, not needs. Anything made here is AI generated and gets the label if it goes public.

Tags: SOURCED (maker page, see SOURCES-2026-11-22.md), PROVEN (seen on Zac's clips), PROPOSED (my design, untested). Everything below is PROPOSED as a design, built on SOURCED rules.

Cheap-first order (all PROPOSED): 1) do nothing, ship the code version. 2) Shot A on Veo 3.1 Fast, 720p, 4 s as a draft only to judge the water. 3) Final on Veo 3.1 once. Shot B only if A is good.

Panel facts Zac checks once (Adobe help pages are blocked to me): Veo 3.1 Fast duration choices and the resolution list, audio switch present and OFF, seed field present, whether a Start frame slot exists next to the prompt (Shot B needs it). I do not know any of these from the panel.

## Shot A: deep water plate (replaces the code-drawn water behind the crest and title)

Why: the code water is clean and fast but flat. A real water plate gives true depth. Engine Veo 3.1 Fast for drafts then Veo 3.1 (PROPOSED, the only engine with evidence on this account, STANDARD says 18 clips). No start frame, so nothing to composite. One camera sentence, one action (a slow push in), no logo or text in the plate (R14).

```prompt
ID: PJ-A-plate
KIND: video
ENGINE: veo
START_FRAME: no
AUDIO: off
---
Slow dolly push in. Underwater in a deep blue sea, the camera looks slightly upward toward the surface. Sunlight breaks through the rippling surface at the top of the frame and falls as wide soft beams through dark blue water. Small white bubbles rise slowly. Shimmering light patterns drift across the water. The lower two thirds of the frame is calm deep navy water. Clean cinematic look, 35mm film grain.
```

Settings to enter (PROPOSED): Veo 3.1 Fast for the draft, then Veo 3.1. 16:9, 6 s (Veo lengths are 4, 6, 8 s, G3), 1080p for the final and 720p for the draft, 24 fps (Veo is 24 fps, G3, so the editor conforms it to the 30 fps timeline), audio OFF. Seed: record what the panel shows. Camera presets: none. Log folder `D:\WKP\data\firefly-prompt-log\pj-intro-plate\`.
Retry ladder: attempt 2 changes one thing, the beam sentence ("narrow shafts" in place of "wide soft beams"). Attempt 3 changes the engine to Kling 3.0 with the same words. After three misses, redesign: keep the code water.
How it is used: in Premiere or AE the plate replaces the background layer, the crest and title stay as built. Fit check: the plate must not be bright behind the title (grade it down 30 percent with a Lumetri exposure drop, PROPOSED).

## Shot B: a real bronze trident rising (replaces the vector trident head)

Why: the code trident reads as a clean vector. A lit bronze prop adds weight. Needs a start frame so the shape is fixed (R7, R12). Name the object by its visible shape, same words in the still and the video.

Still first (Firefly Image, Photo, 16:9, four variations), then Veo 3.1 with that still as the Start frame.

```prompt
ID: PJ-B-still
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph, underwater view in deep blue water. A bronze trident floats upright and centered in the frame, a long straight shaft with a three-pronged head, the middle prong a leaf-shaped point and two curved outer prongs with barbed tips. Pale beams of light fall from above, small bubbles drift, dark navy water below. Sharp focus on the trident, soft dark vignette.
```

```prompt
ID: PJ-B-video
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera. The bronze trident rises slowly and straight upward toward the light. Small bubbles stream from the three prongs. Pale beams of light drift across the water.
```

Settings to enter (PROPOSED): Veo 3.1 Fast draft, 16:9, 4 s, 720p, audio OFF, start frame `pj-intro-trident\start.png` (the chosen still). End frame none. Log folder `D:\WKP\data\firefly-prompt-log\pj-intro-trident\`.
Retry ladder: attempt 2 changes only the motion verb ("rises" to "lifts"). Attempt 3 changes the engine to Kling 4.0 with the maker's start-frame wording. After three misses keep the code trident.
Compositing note: the trident needs a clean cutout to sit behind the shield. A water background makes keying hard (PROPOSED). Option: use Shot B as a full-frame beat at 1.4 to 1.9 s and dissolve to the crest.

## Not requested on purpose
- Any wolf, any logo, any title text in a model clip (R14, the Clayface lesson in the spec).
- Any Percy Jackson actor face or studio art.

## Lint result
See the bottom of this file, pasted from the real command output.

## Lint output (real, 2026-11-23)

```
[PASS] PJ-A-plate (veo, 70 words)
[PASS] PJ-B-still (firefly, 61 words)
[PASS] PJ-B-video (veo, 28 words)
exit 0
```
