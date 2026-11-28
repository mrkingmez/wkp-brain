# Rebuilt prompts for the failed shots (2026-11-22)

Author: graphic-design. Standard: `STANDARD.md` (rule ids R1 to R17). Audit: `AUDIT-2026-11-22.md`. Nothing generated, no credits spent, nothing posted. Credit cost: NOT RETRIEVED. Zac reads the number at the Generate button and writes it in settings.txt (template `SETTINGS-TEMPLATE.txt`). Every clip and still made from these is AI-generated and carries the label if it goes public.

Lint: every ```prompt block below is checked by `python D:\WKP\data\firefly-prompt-guide\prompt_lint.py --file D:\WKP\data\firefly-prompt-guide\REBUILT-PROMPTS-2026-11-22.md`. The result at the bottom of this file is the real output of that command.

Tags: SOURCED (maker page, ids in SOURCES-2026-11-22.md), PROVEN (seen in Zac's clips), PROPOSED (my design, untested). Everything below is PROPOSED as a design, built from SOURCED rules. None of it has been run.

## Panel checks, once, before the first click (30 seconds, no questions to anyone)
Adobe's help pages are blocked to me, so these four facts come only from the panel. Write them in the PANEL block of settings.txt.
1. After picking Veo 3.1 Fast, is there an End frame slot beside the Start frame? (Needed for garage D.)
2. Is there a Negative or Exclude box in Generate image? (Every still has a nouns-only list and also runs without it.)
3. Is there a Seed field under Advanced for video and for image?
4. Is the Audio switch present, and is it OFF? (Every card below assumes audio OFF, sounds added in Premiere from the Adobe SFX library.)

## How each card reads
ENGINE and WHY. START FRAME (a still, with its Firefly Image prompt). VIDEO PROMPT in a lint block. SETTINGS to enter. RETRY LADDER (one change per try, redesign after three). Tips are tagged.

---
# PART 1. WWD joust logo sting (A Knight's Tale): two shots, cut on the crack

Redesign, not a rewrite. The old plan asked one 8 s clip to hold a first-person gallop, a left-third shield, a logo, a hit at 4 s, a shatter and the camera riding past (AUDIT D3, D7, D11, D14). New plan: two 4 s clips and a cut. Shot 1 is the approach. Shot 2 starts already at the contact distance with the logo on the shield. The model never has to time the strike (R11) and never redraws the logo (R14). Total on the timeline is 6 s or less (Zac's intro rule, memory `feedback-intro-length.md`): about 2.5 s of the approach, the cut on the crack, about 3.5 s of the strike.

ENGINE: Veo 3.1 Fast for the drafts, Veo 3.1 (not Fast) for the keepers. Why: it is the only engine with evidence on this account (18 clips), POV is a listed camera term (G1), a start frame is supported (G3), and the format is Google's own (G2). Fast is the cheaper draft tier (Luma's opinion, L1, so COMMUNITY). Second engine if Veo fails three times on shot 2 (redesign): Kling 4.0, because its guide has a PHYSICS sentence and a start-frame wording (K1). Not run.

## Stills first (Firefly Image, Photo, 16:9, 4 variations). These carry the geometry, the lance shape and the shield.

Lance described by its visible shape, never by the word alone (AUDIT D12, F2). Shield with a smooth pale face so the real logo can be pasted on (R14, F3, F4).

```prompt
ID: JS-A-still
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph, first-person view from a horse's saddle at a medieval tournament, camera low and level. In the lower right foreground a gauntleted steel hand grips a long wooden jousting lance painted in red and white spiral stripes, thick behind a round steel hand guard and ending in a blunt rounded wooden head, the lance pointing forward across the horse's neck toward the left. Ahead down a packed-dirt lane, a rectangular wooden shield with a smooth pale oak face stands on a post in the left third of the frame. Wooden spectator stands blurred behind, warm low sun, dust in the air, 35mm film look, sharp focus on the shield.
```

```prompt
ID: JS-B-still
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph, first-person view from a horse's saddle, close. A rectangular wooden shield with a smooth pale oak face fills the center of the frame on a post. From the lower right a long wooden jousting lance painted in red and white spiral stripes, held in a gauntleted steel hand, points at the shield, its blunt rounded wooden head a forearm's length from the shield face at the lower right. Packed-dirt lane, wooden stands blurred behind, warm low sun, dust in the air, 35mm film look.
```

Optional negative box (nouns only, use only if the panel has the box, never paste into the main prompt): text, letters, spearhead, pointed blade, knight in frame, second rider, extra hands.

Check each still at full size before use. Reject a still if the lance reads as a spear (a sharp leaf blade), the shield is not rectangular, a rider is visible, or the shield face carries any drawing. Pick the one with the cleanest hand and lance (R17).

PHOTOSHOP logo composite, each still (PROPOSED, about 5 minutes each). The logo is the same WWD logo PNG with a transparent background used for the earlier joust tries.
1. Open the chosen still. File > Place Embedded, pick the logo.
2. Hold Shift and drag a corner until the logo is about 70 percent of the shield face width, centered on the face.
3. For JS-B, the lance head sits at the lower right of the face. Keep the logo left of and above it so the head does not overlap the logo.
4. In the Layers panel set the logo layer blend mode to Multiply at 90 percent if the logo is dark, or leave Normal at 100 percent if the logo is light.
5. File > Export > Export As, PNG, same pixel size. Save as `joust-startA-logo.png` and `joust-startB-logo.png` in the log folder `D:\WKP\data\firefly-prompt-log\joust-sting-v2\`.

## Shot 1, the approach (4 s)

```prompt
ID: J1-ride-in
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
First-person POV shot from the rider's eyes, level camera sweeping forward down the tilt lane with a light gallop sway. The horse gallops at full speed, hooves throwing up clods of dirt, and the striped wooden lance in the gauntleted hand stays pointed at the shield on its post ahead. The shield grows steadily larger until it fills a third of the frame. The shield and the painted wolf emblem stay exactly as in the first frame. Warm low sun, dust drifting, practical film look.
```
SETTINGS: Veo 3.1 Fast first, 4 s, 720p, aspect 16:9, Audio OFF, start frame `joust-startA-logo.png`, seed recorded. Then keeper on Veo 3.1. Zac copies the credit readout.
RETRY LADDER (one change each): A, if the shield is not growing, add one sentence "The camera moves straight toward the shield." B, if the lance leaves the frame, swap the start still for the sharpest JS-A variation. C, if the logo drifts, shorten to 4 s (already) and drop the last sentence's second half. After three, redesign: drop shot 1, open the sting on shot 2 with a 0.3 s whoosh.

## Shot 2, the strike (4 s)

```prompt
ID: J2-strike
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
ALLOW_IMPACT: yes
---
Close first-person POV shot, level camera pushing forward a short way. [00:00-00:01] The rider charges and the blunt wooden head of the striped lance drives into the center of the painted wolf emblem on the shield. [00:01-00:02] The lance splinters into long pale shards and fine cracks race outward across the shield through the emblem. [00:02-00:04] Wood chips and flecks of paint burst toward the camera and dust billows while the shield stands firm on its post. Warm low sun, practical film look.
```
SETTINGS: same as shot 1, start frame `joust-startB-logo.png`.
RETRY LADDER: A, if the strike is slow, shorten the first range to [00:00-00:01] and delete "pushing forward a short way". B, if a spear shape appears, change "blunt wooden head" to "round wooden cap" (one word change, the shape stays). C, if the emblem is redrawn, use the cracked-emblem still (make JS-C, the same still with fine cracks drawn in Photoshop) as the END frame if the panel shows an End slot on Veo 3.1. After three: engine redesign below.

ENGINE REDESIGN (only after three misses on shot 2). Kling 4.0 in its own template (K1), start frame mandatory in Firefly (A4 snippet):
```prompt
ID: J2-strike-kling
KIND: video
ENGINE: kling
START_FRAME: yes
AUDIO: off
ALLOW_IMPACT: yes
---
Use @Image1 as the first frame, then describe what happens next. Single shot, first-person POV, level camera. The blunt wooden head of the striped lance drives into the center of the painted wolf emblem on the shield. PHYSICS: the lance splinters lengthwise into long pale shards, fine cracks run outward across the pale oak and through the emblem, and wood chips and paint flakes fly toward the camera. The shield stays on its post as dust billows. Warm low sun, practical film look. No subtitles, no background music.
```

PREMIERE (every click). Sequence 1920x1080. Drop `J1` on V1, trim to its first 2.5 s. Drop `J2` after it, trim to 3.5 s. Cut point = the first frame of `J2`. Window > Essential Sound is not needed. From the Adobe sound effects library (media-manager finds the exact file) place a wood crack on A1 starting 2 frames before the cut, and a hoof gallop under shot 1. Add the real logo animation over the end of `J2` only if wanted, as a Premiere layer (R14). PROPOSED.

---
# PART 2. Garage shots (Ian "Wrench Turner" trailer)

Look and wording locked from `Ian-Trailer-Continuity-Chain-Prompts-2026-11-21.md` Part A: Brandon, present day, late thirties, lean, short dark brown hair, black crew-neck t-shirt, faded blue jeans smudged with grease, brown lace-up work boots. Car: candy-apple red 1965 Ford Mustang coupe, chrome bumpers, ownership never implied. Garage: oil-stained concrete, pegboard of hung tools, caged amber work lamp, red rolling creeper, sectional door raised onto green trees. Spoiler fence: no child, no family words. Same tool words in every card: "a flat open-end combination wrench, a straight steel bar with a U-shaped jaw" (R12).

Existing stills that can be start frames for the 9:16 deliverable (viewed today): `R2.png` (man under the car, right hand raised with a wrench, bright door at the left) and `R4.png` (the baseball on concrete, Mustang and open door behind). Folder: `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Pictures\`. Use them instead of new stills for a 9:16 clip. For 16:9 clips make the stills below.

## G-A. Under the car, hears something (replaces garage 1 to 5; keeps what worked in garage 5)
ENGINE Veo 3.1, 8 s. WHY: garage 5 was the one success and it used a start frame, timed beats, a positive hold and one named tool. Everything else stays and the faults are removed: "no camera movement" is now "static", the car and door are not re-described, the arms get a positive hold (garage 5 dropped his hands at 4 s).

```prompt
ID: GA-still
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph from floor level, side view, a lean man in his late thirties with short dark brown hair, a black crew-neck t-shirt and faded blue jeans lies flat on his back on a red creeper under the raised front of a candy-apple red 1965 Ford Mustang coupe. His right hand, the hand nearest the camera, holds a flat open-end combination wrench on a bolt under the car and his left hand rests on the underside of the car. The car's nose points to the right of the frame and the raised garage door with green trees in bright daylight sits at the left. Oil-stained concrete, a caged amber work lamp glowing beside him, pegboard of hung tools behind, warm golden light, fine film grain, 35mm.
```

```prompt
ID: GA-video
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera at floor level, wide frame. [00:00-00:03] The man turns the open-end wrench in small back-and-forth motions with his right hand, the hand nearest the camera, his left hand resting on the underside of the car. [00:03-00:04] Both hands hold the wrench still against the bolt. [00:04-00:06] Only his head moves, turning slowly toward the open garage door while his raised arms and hands stay on the wrench. [00:06-00:08] He holds that look, body and hands still, lying flat on the creeper. Dust drifts in the warm light. Photoreal, natural motion.
```
SETTINGS: Veo 3.1 Fast draft, 8 s, 720p, 16:9, Audio OFF, start frame = the chosen GA still. Keeper on Veo 3.1.
RETRY LADDER: A, if the head turns the wrong way, make a mirrored GA still (door at the right) and keep the text. B, if the wrench changes, name it once more as the first noun of the first range. C, if the hands drop at 4 s, change [00:03-00:04] hold to [00:03-00:05]. After three: cut it. Use the first 3 s (hands working) and a still of his face turning from R2 style. 

## G-B. He rolls out and sits up (replaces garage 2, 3): a cut, not a bigger prompt
The failure was a locked camera plus a body that travels (AUDIT D3, F11). Shot G-A ends with the head turn. Cut to a new clip where he is already sitting. The roll-out is carried by sound on the cut (creeper wheels on concrete, Adobe SFX).

```prompt
ID: GB-still
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph from floor level behind a lean man in his late thirties with short dark brown hair, a black crew-neck t-shirt and faded blue jeans, sitting upright on a red creeper beside the front tire of a candy-apple red 1965 Ford Mustang coupe, his back to the camera, looking out through the raised garage door at bright daylight and green trees. Oil-stained concrete, caged amber work lamp glowing at the side, warm golden light, dust in the air, fine film grain, 35mm.
```

```prompt
ID: GB-video
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera at floor level behind the man. The man sits upright on the red creeper, his back to the camera, looking out at the bright open doorway. His shoulders rise and fall with slow breaths and dust drifts through the light from the doorway. Warm golden light, soft film grain, photoreal.
```
SETTINGS: Veo 3.1 Fast, 4 s, 720p, 16:9, Audio OFF. RETRY LADDER: A, shorten to 4 s if it drifts (already 4 s), so instead change "slow breaths" to "one slow breath". B, change the still, not the words. After three: use the still alone with a 3 percent push in Premiere.

## G-C. Pick up the baseball (replaces garage 11)
The failure was a floor-level camera with a hand reaching in, so the body dropped to the floor (F13). Raise the camera and let the hand come down from above. Start frame: `R4.png` for 9:16, or this still for 16:9.

```prompt
ID: GC-still
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph at hip height looking slightly down, a worn white leather baseball with red stitching, scuffed and grass-stained, rests on oil-stained concrete in the foreground. Behind it, soft and out of focus, a candy-apple red 1965 Ford Mustang coupe with its nose toward the right of the frame and the bright raised garage door with green trees at the left. Warm low light, shallow depth of field, fine film grain, 35mm.
```

```prompt
ID: GC-video
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera at hip height looking slightly down at the baseball on the concrete. [00:00-00:02] Dust drifts in the warm light. [00:02-00:05] A man's right hand with a grease-marked forearm in a black t-shirt sleeve lowers from the top of the frame, closes its fingers around the baseball and lifts it straight up out of the frame, the scuffs and grass stains staying on the leather. [00:05-00:06] Dust drifts over the bare spot on the concrete.
```
SETTINGS: Veo 3.1 Fast, 6 s, 720p, 16:9, Audio OFF. RETRY LADDER: A, if the body appears, add "Only the hand and forearm are in the frame" as the last sentence. B, if dirt flickers, shorten to 4 s ([00:00-00:01] drift, [00:01-00:03] lift). C, change the still's camera to knee height. After three: cut on a hand entering the frame in the edit and show the ball gone in the next shot.

## G-D. The ball rolls to the boot and rests against it (replaces garage 12)
The failure was our own verb "bumps" plus no end frame. New design: first AND last frame (Google's method, G2, G3) and a resting end state. This is the only card that needs the panel's End slot (panel check 1). Two stills with the same framing and light.

```prompt
ID: GD-still-start
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph on a concrete garage floor at floor level, wide frame. A man in brown leather work boots and faded blue jeans lies on his back under the raised front of a candy-apple red 1965 Ford Mustang coupe, only his legs and boots sticking out toward the camera. A worn white leather baseball with red stitching, scuffed and grass-stained, sits on the floor at the left of the frame near the open garage doorway with bright daylight. Pegboard and workbench blurred behind, warm golden late-afternoon light, fine film grain, 35mm.
```

```prompt
ID: GD-still-end
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph on a concrete garage floor at floor level, wide frame, the same view as the first. A man in brown leather work boots and faded blue jeans lies on his back under the raised front of a candy-apple red 1965 Ford Mustang coupe, only his legs and boots sticking out toward the camera. A worn white leather baseball with red stitching, scuffed and grass-stained, rests on the floor touching the outer side of his left boot, level with the laces. Pegboard and workbench blurred behind, warm golden late-afternoon light, fine film grain, 35mm.
```
Make the end still from the start still with the Composition reference at a mid strength (Adobe's demo used about the midpoint, A2) so the framing matches. Check the two stills side by side at full size: same car, same boots, same light, only the ball has moved (BFL: keep the frames related, F3).

```prompt
ID: GD-video
KIND: video
ENGINE: veo
START_FRAME: yes
END_FRAME: yes
AUDIO: off
---
Static camera on the concrete floor, wide frame. The worn baseball rolls slowly along the floor from the left of the frame, losing speed with each turn, and comes to rest touching the outer side of his left boot. The brown boots stay in place. Dust drifts in the warm light.
```
SETTINGS: Veo 3.1 Fast first, first frame GD-still-start, last frame GD-still-end, 6 s, 720p, Audio OFF. If the Fast tier has no End slot, use Veo 3.1 for this clip. If neither has an End slot: no video model for the contact. Use the 3 s that worked in garage 12 (the roll) and cut to the resting still GD-still-end with a soft thud from the Adobe SFX library. RETRY LADDER: A, shorten to 4 s. B, replace "losing speed with each turn" with "slowing to a stop". C, make the ball start closer. After three: the cut above.

## G-E. The dust-covered Mustang with someone in the doorway (replaces garage 13)
Garage 13 was good except the door opened by itself and nobody stood there. Fix: state the door is already raised, put the man in the start frame, add one camera sentence (R9). One man, one hand on the frame, no action beyond breath and dust.

```prompt
ID: GE-still
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Photograph from floor level inside a dim two-car garage. A 1965 Ford Mustang coupe stands under a gray canvas dust cover with a thin layer of dust, the long hood and short rear deck clear under the cloth and the front pointing to the right of the frame. The sectional garage door is raised overhead and bright daylight pours across the concrete floor from the doorway at the left. In the doorway a man stands as a dark silhouette, one hand resting on the door frame, looking at the covered car. Pegboard of hung tools and a wooden workbench at the back, soft film grain, photoreal, natural light.
```

```prompt
ID: GE-video
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera at floor level inside the garage. A man stands in the open doorway as a dark silhouette against bright daylight, one hand resting on the door frame, looking at the gray canvas cover over the car. Dust motes drift through the beam of light across the cover and the concrete floor. The garage door rests fully raised overhead. Warm natural light, soft film grain, photoreal.
```
SETTINGS: Veo 3.1 Fast, 8 s, 720p, 16:9, Audio OFF. RETRY LADDER: A, if the door moves, remove its sentence and trust the still. B, if the man walks in, shorten to 4 s. C, if his hand moves, change "resting on the door frame" to "gripping the door frame". After three: use the still with a slow 4 percent push in Premiere.

---
# PART 3. The wrench handoff: a dissolve or a cut, not a morph

The old plan, garage 6 to 10, put two hands and a wrench swap in one generation. It failed six of six times (F8 to F10). Two safe designs, in order of preference. Neither asks a model to move a wrench between two hands.

## Option 1 (recommended): two stills and a cross dissolve, no video model at all
Stills: `R3.png` exists (older hand from the upper right and a child's small hand at the lower left, both on the wrench, viewed today). `R3b` is the still in `Ian-Trailer-Continuity-Chain-Prompts-2026-11-21.md` (older fingertips lifting away, a lean young man's hand closing on the shaft). The chain doc already has the card with the Composition reference, so the two stills line up. Edit steps below were updated 2026-11-22 (see the edit list).
PREMIERE (every click, PROPOSED): 1. Drag R3 onto V1 for 2 s. 2. Drag R3b onto V1 right after it for 2.5 s. 3. Effects panel > search Cross Dissolve > drag it onto the cut between them. 4. Click the transition, set Duration 2 s. 5. Select R3, Effect Controls > Scale, keyframe 100 at its start and 103 at its end. Do the same on R3b so the push in continues. 6. Add a soft metal touch sound on the middle of the dissolve from the Adobe SFX library.

## Option 2 (if Zac wants motion): two stills, two clips, one cut. Each clip has ONE hand and ONE wrench
Stills made with the R3 Composition reference at a mid strength (A2), 9:16, Photo. The older hand from the upper right holds the wrench out toward the lower left. In the second still only the young hand holds the wrench.

```prompt
ID: HO-still-a
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Close photograph looking up from beneath an old car, dark oily underside filling the frame, a caged work lamp glowing amber at the upper right. From the upper right an older man's thick creased hand and forearm in a rolled faded blue denim sleeve, gray hair on the forearm, holds a single steel combination wrench out toward the lower left, handle first, the open jaw at the bottom. The lower left of the frame holds only the dark underside. Warm amber grade, heavy fine film grain, shallow depth of field, 35mm, vertical frame.
```

```prompt
ID: HO-still-b
KIND: still
ENGINE: firefly
START_FRAME: no
AUDIO: off
---
Close photograph looking up from beneath an old car, dark oily underside filling the frame, a caged work lamp glowing amber at the upper right. From the lower left a lean young man's forearm and hand, short dark hair on the arm, grease on the knuckles, grips a single steel combination wrench by the handle, the open jaw at the bottom. The upper right of the frame holds only the dark underside. Warm amber grade, heavy fine film grain, shallow depth of field, 35mm, vertical frame.
```

```prompt
ID: HO-clip-1
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera, vertical frame. The older man's thick creased hand holds the steel wrench steady in the amber lamp light, then lowers it a few inches toward the lower left of the frame. Dust drifts across the glow of the caged lamp.
```

```prompt
ID: HO-clip-2
KIND: video
ENGINE: veo
START_FRAME: yes
AUDIO: off
---
Static camera, vertical frame. The young man's hand grips the steel wrench and draws it down and away toward the lower left corner of the frame, the open jaw swinging out of view. Dust drifts across the glow of the caged lamp.
```
SETTINGS (both): Veo 3.1 Fast, 4 s, 720p, 9:16, Audio OFF, start frame = the matching still. The match action: clip 1 ends with the wrench moving toward the lower left, clip 2 starts with a hand gripping it at the lower left. Cut between them with the metal touch sound. RETRY LADDER (each clip): A, make the still sharper, not the words. B, change "a few inches" to "slightly". C, shorten to 4 s. After three: Option 1.

---
# PART 4. The four Ian stills against the standard
Checked with the lint and by eye. Edits are made in `D:\WKP\Post-Production\reports\Ian-Trailer-Continuity-Chain-Prompts-2026-11-21.md`, listed in the report that came with this file and at the end of `AUDIT-2026-11-22.md`.

---
# LINT RESULT (real output of the command at the top of this file)
```
[PASS] JS-A-still (firefly, 109 words)
[PASS] JS-B-still (firefly, 85 words)
[PASS] J1-ride-in (veo, 85 words)
[PASS] J2-strike (veo, 89 words)
[PASS] J2-strike-kling (kling, 88 words)
[PASS] GA-still (firefly, 125 words)
[PASS] GA-video (veo, 100 words)
[PASS] GB-still (firefly, 82 words)
[PASS] GB-video (veo, 52 words)
[PASS] GC-still (firefly, 71 words)
[PASS] GC-video (veo, 82 words)
[PASS] GD-still-start (firefly, 90 words)
[PASS] GD-still-end (firefly, 94 words)
[PASS] GD-video (veo, 51 words)
[PASS] GE-still (firefly, 108 words)
[PASS] GE-video (veo, 67 words)
[PASS] HO-still-a (firefly, 93 words)
[PASS] HO-still-b (firefly, 86 words)
[PASS] HO-clip-1 (veo, 42 words)
[PASS] HO-clip-2 (veo, 42 words)
```

Result: 20 of 20 prompts PASS. A PASS means no negation, no shouting, no abstract word, no impact verb on the contact shots, a camera sentence, continuous timestamps and a length inside the limit. It does NOT mean the clip will work. Nothing here has been run on the account.
