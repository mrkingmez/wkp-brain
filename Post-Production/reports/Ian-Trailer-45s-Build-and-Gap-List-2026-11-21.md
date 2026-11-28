# Ian "Wrench Turner" trailer: 45 s build and gap list (2026-11-21)

Point man: assistant-editor. Free favor for Ian, Zac delivers files, Ian posts. Nothing generated, spent, posted or pushed. DO NOT FORWARD TO IAN: this file names the plot fence.

## BLUF

- **What exists today: 33.0 s** (26.0 s of picture, 3.0 s black text beat, 4.0 s end card). Probed, not played.
- **What is missing to reach 45 s: 12.0 s**, three beats: H1 homecoming 6 s, B1 brotherhood 3 s, W1 sweetheart 3 s. Plus one WEAK stand-in: the R3 hold (5.5 s on one still) wants R3b to split it.
- **NEED beats: 4** (R3b, H1, W1, B1). **Generations: 4 image runs** (4 variations each), credit cost NOT RETRIEVED, read it at the Generate button. Firefly credits were refilled 2026-11-20, amount unknown.
- **Cheapest path to 40 s: ONE generation, H1 (6 s).** 33.0 + 6.0 = 39.0 s, plus stretching R5 (+1.0 s) and R1 (+0.5 s) from existing stills = 40.5 s. R3b is a second run that fixes the weak hold but adds no time.
- **To 43.5 s:** add W1 (second run). **To 45 s:** add B1 (only after Ian says yes), or hold H1 longer.
- **Zero-credit path:** stretch V4, V1, R5, R1 holds and use the Polaroid (`picture old.png`) as a 2.5 s memory beat. Estimated 38 to 39.5 s by arithmetic, NOT built. Weak, and the Polaroid is a Zac creative call (see gap list).
- **Zac decides:** (1) spend on H1 only, or H1 plus R3b and W1; (2) ask Ian about B1 or let H1 take its 3 s; (3) use the Polaroid or not.

## Probe results (ffprobe, 2026-11-21)

| File | Result |
|---|---|
| Raw Footage V1, V2, V4, V7, 9Sa | each 1920x1080, 24 fps, 8.000 s, 192 frames, NO audio |
| Pictures R1, R3, R5 | 768x1376 stills. R2, R4: 848x1264. All no audio |
| `Raw Footage\picture old.png` | 1024x1024 still (Polaroid, man holding a toddler in front of the red Mustang) |
| `book cover.jpg` | 1365x2048 |
| v4 45 s 16x9 (old) | 45.000 s, 1080 frames, 24 fps, no audio. Slates stand in for H1, B1, W1 |
| NEW v5 with gap cards | 45.000 s, 1080 frames, 24 fps, 1920x1080, no audio |
| NEW v5 HAVE-only floor | 33.000 s, 792 frames, 24 fps, 1920x1080, no audio |

Frame checks on v5: contact sheet viewed. Black only 38 to 41 s (the text beat). Freezes only on the gap cards (16 to 28 s) and the black and end card. Gap card text legible. Caption slots are grey placeholders, not real captions. Not played, nothing heard.

Files (Rough Cut folder, v1 to v4 untouched):
- `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Rough Cut\Ian-Trailer-D34-45s-16x9-v5-with-gap-cards-silent.mp4`
- `P:\01 Warrior King Productions\02 Video Project\Ian's Book Trailers\Rough Cut\Ian-Trailer-D34-45s-16x9-v5-HAVE-only-floor-silent.mp4`
- Build script `D:\WKP\scratch\ian\v5\build_v5.py`, contact sheets `D:\WKP\scratch\ian\v5\chk\`.

## Timeline (24 fps, 16:9, 45 s)

| # | Time | Dur | Source | Status | Words on screen (Draft 3.3 final only) | Sound and music | Transition |
|---|---|---|---|---|---|---|---|
| 1 | 0:00 to 0:03 | 3.0 | V1 0.0 to 3.0 | HAVE | He came home / from the war. | ratchet clicks, no music | opens |
| 2 | 0:03 to 0:06.5 | 3.5 | V4 0.8 to 4.3, warm grade, grain, narrower window | HAVE | none | ball roll, music enters | 1 s dissolve |
| 3 | 0:06.5 to 0:09.5 | 3.0 | R3.png push | HAVE | Back then, / he was the Wrench Turner. (Ian yes pending) | music | 8 frame dissolve |
| 4 | 0:09.5 to 0:12 | 2.5 | R3b (NEED). v5 holds R3 | WEAK, stand-in | none | wrench clink at crossfade | 1.5 s crossfade |
| 5 | 0:12 to 0:16 | 4.0 | V1 3.2 to 7.2 | HAVE | none | music low | hard cut |
| 6 | 0:16 to 0:22 | 6.0 | H1 (NEED), 3.5 s wide push then 2.5 s reframe | NEED | none | steps, screen door, cloth | cut |
| 7 | 0:22 to 0:25 | 3.0 | B1 (NEED, Ian yes first) | NEED | none | crickets | cut |
| 8 | 0:25 to 0:28 | 3.0 | W1 (NEED) | NEED | none | filtered fire | cut |
| 9 | 0:28 to 0:30.5 | 2.5 | R5 duffel and gloves, push | HAVE | none | duffel set down | cut |
| 10 | 0:30.5 to 0:34.5 | 4.0 | R1 garage, push | HAVE | none | garage at rest | cut |
| 11 | 0:34.5 to 0:38 | 3.5 | V1 0.6 to 4.1, punch-in | HAVE | none | ratchet returns | cut |
| 12 | 0:38 to 0:41 | 3.0 | black | HAVE (text) | The car was / the easy part. | final chord | cut |
| 13 | 0:41 to 0:45 | 4.0 | book cover end card | HAVE (buy link missing) | AVAILABLE NOW / [BUY LINK] | chord rings out | cut |

Sound and music cues are from the Draft 3.3 cue sheet (Appendix D). Nobody has heard any sound.

HAVE other WEAK notes (on disk, needs a fix):
1. V1 is reused three times (beats 1, 5, 11) from one 8 s source. Beat 11 starts mid-turn and punches in so it reads as a return, by design.
2. R1, R3 and R5 are vertical stills, so in 16:9 each fills about a third of the width on a blurred fill. Contain-fit rule, no cropping. head-editor call.
3. Captions are slots, not burned in. The Wrench Turner line waits on Ian's yes.
4. Not used on purpose: V2, 9Sa, R4 (present-day ball, fenced), V7 (door rise belongs to the cover story piece), R2 (not in the plan, usable present-day filler).

## Gap list, cheapest first

Rank key: (a) reuse or push-in on what exists, (b) edit trick, (c) new generation. Credit cost for every generation: NOT RETRIEVED. No spend without Zac's yes.

### Gap 1. H1 homecoming, 6.0 s (NEED, the biggest hole)
- (a) Reuse: nothing on disk shows a homecoming. R5 (duffel) already carries "home". Stretching R5 to 3.5 s and R1 to 4.5 s recovers 1.5 s only.
- (b) Edit trick: none that reads as a hug.
- (c) Generation: **1 image run, 4 variations.** Make this still first. Cheapest high-value run.
- Firefly Image, content type Photo, 16:9, 4 variations, no reference, newest Adobe commercially safe model. Positive only in the main prompt:
  > Golden hour photograph, early 2000s small-town America. A young soldier in plain tan desert camouflage, seen from behind in three-quarter back view, hugs his mother and his father on the front walk of a small white one-story house. An olive duffel bag rests at his feet. The mother, late forties, in a floral blouse, holds him tight, eyes closed, in profile. The father, fifties, in a plaid shirt, rests his hand on the back of the soldier's head. A small American flag hangs on the porch post. Low warm backlight, warm amber grade, gentle film grain, shallow depth of field, 35mm, horizontal frame. The three stand in the middle third.
- Negative field only (from `2026-11-20-firefly-prompts.md`, H1): text, captions, watermark, garbled letters, license plate, name tape, unit patch, rank insignia, medals, weapon, helmet, extra fingers, deformed hands, extra limbs, cartoon, illustration, 3D render look, lens flare, plastic look, any child, kids, toddler, baby, stroller, any other person, young woman, crowd, modern cars, smartphones, signs. The flag stays out of the negative.
- Reject checks: any child or small figure, any second woman, soldier facing camera, any patch or readable text, wrong flag.
- Optional paid motion (Veo 3.1 image to video, H1 still as start frame, one action, one camera move, cost NOT RETRIEVED, only if the still push disappoints): "Slow push in toward the three of them as the mother tightens her arms around the soldier's back." Veo softens contact between people, so cut on the embrace if it fails.

### Gap 2. R3b hand-off still, 2.5 s slot (WEAK now, NEED for the morph)
- (a) Reuse: hold R3 (what v5 does). Works, but 5.5 s on one still is long.
- (b) Edit trick: split the hold with a slow push then a second push (free, keeps the stand-in). Does not make the hand-off.
- (c) Generation: **1 image run, 4 variations.** Run second only if Zac wants the morph. R3.png as a Composition reference, mid to high strength (untested), change only that slider on a retry. Adds no runtime.
- Firefly Image, Photo, 9:16, 4 variations:
  > Low angle photograph looking up under an old car, one caged work lamp glowing amber at the upper right. A steel wrench stands vertical at the center, open jaw at the bottom, same size as the reference. An older man's hand in a faded blue rolled sleeve, from the upper right, releases the top of the handle. A lean young man's hand and forearm, from the lower left, takes the shaft just above the jaw, with a small gap between the hands. Warm amber grade, heavy film grain, shallow depth of field, 35mm, vertical frame.
- Negative field only (R3b block of the prompts file): text, watermark, any face, weapon, extra fingers, deformed hands, six fingers, fused fingers, hands gripping together, cartoon, 3D render look, lens flare, plastic look, toddler, baby, child, boy, small hand, wedding ring, watch, tattoo, black t-shirt, bright daylight, cool blue grade.
- Reject checks: wrong finger count, wrench off center, lamp moved, both hands gripping, young arm reads as a child, any text.

### Gap 3. W1 sweetheart, 3.0 s (NEED)
- (a) Reuse: none. (b) Edit trick: if cut, H1 holds 3 s longer or R1 and R5 stretch (about 3 s total). Reaches 43.5 s instead of 45 s without W1 only if H1 is already in.
- (c) Generation: 1 image run, 4 variations, run third. Photo, 16:9:
  > Photograph at night, a bonfire at a pasture party in the late 1990s. Across the fire, one young woman about twenty, long brown hair, denim jacket over a white tee, turns away from the camera, face in profile and half hidden by her hair, firelight orange on her cheek. Sparks rise and smoke drifts. Far behind her, out of focus, a few tall dark male silhouettes by two parked pickups. Warm firelight, deep black sky, heavy film grain, shallow depth of field, 35mm, horizontal frame. She is the only woman in the picture.
- Negative field only: the W1 line in the prompts file (two women, second woman, twins, any child, teenager, text, modern clothing, bottle).
- Reject checks: any second female figure, any child, she faces camera, readable text.

### Gap 4. B1 brotherhood glimpse, 3.0 s (NEED, Ian's yes first)
- (a) Reuse: none. (b) If Ian says no, H1 takes the 3 s (hold H1 to 9 s, or stretch holds). Zero cost.
- (c) Generation: 1 image run, 4 variations, run last and only after Ian says yes. Photo, 16:9:
  > Photograph at dusk, deep orange and purple sky over an open field. Two men in plain civilian clothes sit side by side on the lowered tailgate of an old dark pickup, seen from behind and the side, looking out toward the horizon in silence. The man on the left, thirties, in a faded flannel shirt and plain ball cap, rests one hand on the other man's shoulder. The man on the right, thirties, in a worn canvas jacket, has short dark hair. Faces half in shadow. Warm muted grade, heavy film grain, shallow depth of field, 35mm, horizontal frame. Only these two men are in the picture.
- Negative field only: the B1 line in the prompts file (weapon, uniform, camouflage, head in hands, crying, bottle, any woman, any child, truck lettering).

### Count and cost
- Generations: **4** image runs (R3b, H1, W1, B1). Cheapest 40 s: **1** (H1). 43.5 s: **3** (H1, W1, R3b optional so 2 for time). 45 s: **3 or 4**.
- Credit cost per run: **NOT RETRIEVED**. Read it at the Generate button, write it down. Nothing runs without Zac.
- Save winners to `Pictures\` as `R3b-handoff.png`, `H1-homecoming-v1.png`, `W1-sweetheart-v1.png`, `B1-brotherhood-v1.png`, then tell assistant-editor and v6 is built the same day.
- AI label applies to every generated still.

### Zero-credit stretch (not built, arithmetic only)
V4 from 3.5 to 4.7 s (+1.2, frames after 4.3 s seen only at 1 fps, check the ball bounce), R5 +1.0, R1 +0.5, V1 punch +0.5, Polaroid 2.5 s as a memory beat. About 38 to 39.5 s. The Polaroid shows a man holding a toddler beside the Mustang. It is past and Zac ruled past material fine, but it implies whose car it is (settled: never say) and the Draft 3.3 QA pass did not review it. CREATIVE CALL for Zac. Not recommended over generating H1.

## Head-editor notes
See the head-editor section appended below if received, or `Post-Production\projects\ian-trailer\2026-11-21-head-editor-notes-v5.md`.

## Not verified
Nothing played or heard. Credit costs not retrieved. Prompts untested. Zero-credit runtime not built. Ian's answers, buy link and cover license still open. V4 frames after 4.3 s viewed at 1 fps only.


UPDATE 2026-11-25: v7 45 s 16:9 built with the W1 rip v2-center at beat 8, see `Ian-Trailer-45s-v7-W1-Rip-Plan-2026-11-25.md`. W1 still is no longer a NEED for this cut (the rip uses W1a and W1b already on disk).
