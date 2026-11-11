# Godzilla Minus Zero: Logo Squash Sting, Firefly Prompt

**Built 2026-11-07 by wwd-vfx.** One shot: a colossal kaiju foot comes down and squashes the Winter Wolf logo. 6 to 8 seconds. Same logo look as the burning logo and the Clayface sting. Sounds for this sting are in the companion doc `Godzilla-Sound-Cue-Sheet.md`, Part A.

**Read this first: nobody can test this prompt without spending credits.** Matt paid for Zac's Firefly credits and I have no generation tool, so none of the prompts below has been run. Do the cheap test first (steps below), then one real take.

## What the existing stings look like (checked on disk, not guessed)

Read from `L:\Winter Wolfs Den review show\VFX\burning logo.mp4` (frames pulled and looked at) and `P:\WWD Kit\Clayface\Clayface Logo - Brown Start Frame.png`:

- Burning logo: 5.0 s, 1920x1080, 24 fps, no audio, pure black background.
- Logo sits **centered** in the frame, nearly full height (about 8 percent margin top and bottom), blue-purple werewolf badge, cyan outline, white WINTER lettering, teal WOLF'S DEN, soft cyan glow around the edge.
- Correction to the Clayface doc: that doc says the logo sits "top left" in the burning clip. The frames show it centered. The Clayface start frame is also centered, same size.
- Clayface start frame: 1920x1080, RGB, the same centered badge, turned brown.

The squash sting keeps all of that: black background, centered badge, same size, cyan glow, 16:9, 24 fps.

## Start frame (use exactly this file)

`P:\WWD Kit\Godzilla\Godzilla Logo - Black Start Frame.png`

- 1920x1080, RGB, built from `L:\Winter Wolfs Den review show\Pictures\logo.png` (the logo has a transparent background, so it was flattened on solid black first, same method as the Clayface start frame). Script: `D:\WKP\.claude\skills\wwd-review-photo-pull\scripts\make_godzilla_sound_pack.py`.
- If the old logo.png is already loaded in Firefly under References > Frames from the Clayface job, replace it with this file so the black is solid.

## Model and settings

From `memory\topics\firefly-models.md` (Zac's real menu, screenshot 2026-10-25). Settings panel: Model, Resolution, Aspect ratio, Frames per second, Duration, Audio. References > Frames. Advanced > Seed.

- **Cheap test first:** Veo 3.1 Lite (or Veo 3.1 Fast), 720p, shortest duration the panel offers, audio off. One take only. You are checking one thing: does the foot come down onto the badge, and does the badge stay readable until it lands.
- **Real take:** Veo 3.1 (the default), highest resolution the panel offers (aim for 1080p), 16:9, 24 fps, audio off.
- **Duration:** 8 seconds if offered. Veo clips are usually offered in a few fixed lengths. I have not verified which lengths Zac's panel shows, so check. If 8 is not there, take 6.
- **Audio:** off. The sounds are built from owned files in the sound pack.
- **Seed:** leave blank for the first take, then write down the seed Firefly shows and keep it for any retry.
- **End frame:** I have not verified whether any model in the panel takes an end frame. Do not count on one. Check the panel. If a second slot appears, a good end frame would be the same black frame with a flat dark crushed badge, but the prompt works without it.
- **Fallback model:** Kling 3.0, which the menu describes as strong on start-frame consistency. Same prompt.
- Record in this doc after the run: model, resolution, seed, which prompt, pass or fail.

## Prompt A (main)

> Start with the exact start frame, the werewolf badge logo with the cyan outline and white WINTER lettering, glowing softly on a pure black background, perfectly still. The camera looks straight down and stays locked. The badge lies flat on dark ground. After a moment the glow trembles and dust jumps off the ground. Then one colossal reptilian kaiju foot comes down from above into the frame, charcoal scaly skin, rough dorsal-plate-like ridges up the ankle, four thick clawed toes. The foot lands once on the badge, hard. The badge cracks and flattens under the foot, the ground splits in lines out from the impact, a ring of dust and small chunks of debris bursts outward. The foot lifts straight up and out of the top of the frame. Heavy dust drifts and settles over the flattened, cracked badge, lit faintly cyan. The last second holds almost still, dust settled, the flattened badge centered, dark space around it. One continuous shot, no cuts.

## Prompt B (clean backup, shorter and more literal)

> The werewolf badge logo lies flat on a black floor, seen from straight above, camera locked. A giant reptilian monster foot with charcoal scaly skin comes down from above and stomps the badge once. The badge cracks and flattens. Dust and debris burst out, then settle. The foot lifts away out of the top of the frame. Last second still, dust over the flattened badge. One shot.

Use B if A gives a second foot, a body, a camera move, or a foot that wanders.

## Prompt C (second fallback, low front view, if top-down is ignored)

> The werewolf badge logo stands on a black floor, front view, camera locked. A giant reptilian monster foot with charcoal scaly skin drops from the top of the frame onto the badge and presses it flat into the floor. The ground cracks around it, dust and debris burst sideways. The foot stays planted for a second, then lifts out of frame. Dust settles over a flattened, cracked badge. One shot.

Note on C: from the front a flattened badge reads as a thin crushed shape, so the title hold is weaker. Top-down (A and B) is the better read.

## Avoid list (Negative prompt box if it exists, otherwise leave the phrases out of the main prompt)

> second foot, full monster body, head, tail, fire, flames, atomic glow, blue breath beam, city, buildings, people, cars, camera movement, zoom, shake cuts, new text, changed lettering, extra logos, studio logos, watermark, bright background, daylight, blood

Reasons: a wolf-comes-alive line in the Clayface job produced a wolf face, so no character-changing detail is added. No fire, because fire is the old burning sting. No body, because only the foot is the joke.

## Prompt rules used (from the Clayface lessons)

- Short and literal. One foot, one landing.
- The start frame is pinned in the first sentence.
- No trademark names. The monster is described by look only: colossal reptilian kaiju foot, charcoal scaly skin, dorsal-plate-like ridges. No studio name, no film title, no signature roar words.
- No word "puddle". Nothing should be left behind except the flattened badge, which the title sits over.

## If it goes wrong

- Badge letters turn to gibberish before the foot lands: fine for a sting that ends flattened, as long as the first second is clean. If the first second is not clean, rerun with the same seed and Prompt B.
- The foot never lands or lands twice: Prompt B, and add "lands exactly once".
- The badge is not flattened, just covered: that is acceptable if the dust settles over a dark crushed shape. If not, code-built fallback: I can build the squash in Python (badge scales flat under a foot silhouette, crack lines, dust particles) with no credits. Say the word.
- Ends on a dim frame: that is wanted. The title goes over the settled dust. Keep the last second clean, no text from Firefly.

## Timing for the editor

- The foot touch frame is called T in the sound plan. Scrub the Firefly clip, find the frame where the foot touches, mark it. Every sound in the sound plan is placed relative to T.
- Drop the sting right after the hook line. The cut transcript (`Godzilla Minus Zero -  Review - All Hail the King!.txt`) has no gap for a logo at the open: the hook runs 00:00:00 to 00:00:22:03 and the next line starts at 00:00:22:09. "Let's find out now" lands near 00:14 (estimate from word count). Zac decides where it goes.
- Aspect ratio 16:9, 1920x1080, 24 fps like the burning logo. The cut is 30 fps, Premiere will conform it.

## Open for Zac

- Run the cheap test first and tell me what you saw.
- Which model and which take you keep, so it gets logged.
- Whether the title text is added in Premiere over the settled dust.
- Credits are Matt's. One test, one real take, one retry at most.

*Not verified: every prompt above, because no one can test without credits. Not verified: the durations and the end-frame option in Zac's panel.*
