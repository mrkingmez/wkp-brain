# Crystal Lake Opening: Firefly Plate Prompts

Date 2026-10-20. The opening runs **19.0 seconds and starts at 0:01** of the video.

## The idea

A girl alone in a canoe on a night lake. Calm, then the water bulges, the **Crystal Lake poster launches out of the lake**, grabs her and drags her under. The canoe is left empty and the ripples settle. She just disappears, no blood. It is a wink at the canoe scare that ends Friday the 13th (1980).

## What does what

- **Firefly makes the lake footage** (the "plates"). Five short clips.
- **Claude adds the poster**, the splash and spray, the camera shake, the white flash, the cut, and the owned sounds. The real poster pixels go in, so the title is never garbled by AI.
- A finished fallback already exists: `P:\WWD Kit\Crystal Lake\Opening - Lake Scare (Option 1).mov` (stylized, 19.0 s). Use it if the Firefly version is not ready.

## Before you start (click by click)

1. Open Firefly in the browser and choose **Video**, then **Generate video**.
2. Set the aspect ratio to **16:9** and the resolution to **1080p** if offered.
3. In the model list, pick the most realistic video model your plan shows. Water at night is hard, so a newer partner model usually beats the basic one. The price in credits shows on screen before you click Generate. Check it first.
4. Camera: **locked off, no movement** on plates 1, 3, 4 and 5. Plate 2 can have a very slow push in. **Camera position (fixed 2026-10-20): every wide plate is shot from the beach looking out at the canoe, canoe seen from the side. Never from behind the canoe or from on the water.** If a clip still comes out from behind the canoe or shows two canoes, regenerate it, do not trim it.
5. **First make one still** with Firefly Image using the Still prompt below, 16:9. Use that still as the **start frame** (image to video) for plates 1, 3, 4 and 5 so the lake, moon and canoe match in every clip.
6. Save every clip into `L:\Winter Wolfs Den review show\Raw Footage\mass record crystal LAke Vision Quest\Crystal Lake\opening plates\` and name them `plate-1.mp4` to `plate-5.mp4`.

## The still (start frame)

> Wide cinematic night photograph taken from the sandy beach at the water's edge, camera low and looking straight out across the lake. A few feet of dark wet sand and shoreline reeds in the bottom foreground. About 40 yards out, exactly ONE old wooden canoe seen from the SIDE (full profile, the whole length of the canoe visible), with ONE young woman in a dark jacket sitting upright in it, seen from the side, small in the frame. The canoe is on the left third of the frame, open water on the right third. Full moon low over a dense pine forest on the far shore, thin mist on the water, moonlight reflection on the water. Natural film grain, muted blue and teal tones, realistic, photographic. Only one canoe, only one person, no second boat.

## The five plates

| Plate | Length | Prompt |
|---|---|---|
| 1. Calm | about 6 s | Using the start frame. The camera stays fixed on the beach, looking out across the lake, and does not move, pan or turn. The single canoe floats in place on the left third of the frame, seen from the side, drifting only a few inches and rocking very slightly on the water. The young woman sits perfectly still in the canoe with her hands in her lap. She has no paddle, and there is no paddle anywhere in the canoe. Soft ripples roll across the lake toward the beach and wash up on the sand in the foreground. Mist drifts slowly across the water from right to left. Calm and quiet. Exactly one canoe and one person, no paddle, no second boat. |
| 2. Her face | about 4 s | Medium close shot of the young woman in the canoe at night, moonlight on her face, she slowly turns her head toward the dark water off camera right, her breathing visible, uneasy, eyes widening slightly. Very slow push in. Water ripples softly behind her. |
| 3. The burst | about 3 s | Using the start frame. Locked camera. The calm water to the right of the canoe swells, bulges upward, then **violently erupts in a column of spray and white water**, droplets flying across the frame, the canoe lurches. No creature and no object visible in the spray, just the explosion of water. |
| 4. Empty and thrashing | about 3 s | Same wide shot, locked camera. The **canoe is empty** and rocking hard from side to side, the paddle floating nearby, churning white water around it, spray falling back onto the lake. |
| 5. Settling | about 3 s | Same wide shot, locked camera. The empty canoe drifts and slowly stops rocking, widening ripples fade, mist rolls back over the water, the moon reflection steadies. Silence. |

Add to **every** prompt: *no text, no logos, no watermark, no other people, no animals, no masks, photorealistic, natural film grain.*

## Timeline once you have the plates (Claude builds this)

| Time in opening | What plays |
|---|---|
| 0:00 to 0:06 | Plate 1, fade up from black, lake ambience |
| 0:06 to 0:10 | Plate 2, her face, low tension sound |
| 0:10 to 0:13 | Plate 3, the burst. The poster launches out of the spray, flash, cymbal stab, splash |
| 0:13 to 0:15 | The poster lunges, grabs her and drags her down (Claude's composite over the burst plate, scream, cut off) |
| 0:15 to 0:16 | Big splash, thud, hard cut to plate 4 |
| 0:16 to 0:18 | Plate 4, empty canoe thrashing |
| 0:18 to 0:19 | Plate 5, settles, fade to black |

All sounds are owned (P: drive): water splash, cymbal stab, scream, dark thud, lake and cricket ambience. No music bed.

## If a plate comes out wrong

- Water looks like glass or the canoe morphs: shorten the clip to 3 seconds and regenerate. Do not stretch it.
- A person appears in plate 3 or 4: add "empty lake, no people" and regenerate that plate only.
- Do not accept a plate with fake text or a logo.

## Tell Claude when the plates are saved

Say "plates are in". Claude checks each clip, builds the 19.0 s version, and puts it next to the Option 1 file in `P:\WWD Kit\Crystal Lake\`.

## Flags

- **The poster is also run sheet stop 2** (PNG 1 at 00:07). No picture twice, so the run sheet needs a swap for that stop once this opening is locked. The whole run sheet also shifts later by about 19 seconds. Tell Claude to re-time it.
- Firefly clip length, model names and credit costs change. Confirm what your plan shows on screen.
