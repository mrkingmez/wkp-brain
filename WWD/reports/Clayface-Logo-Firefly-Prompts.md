# Clayface Logo Sting - Firefly Prompts and Sound Plan

**Built 2026-10-25.** Goal: the same Winter Wolf's Den logo sting, but the logo shape-shifts like Clayface skin, turns brown, then melts away. Replaces the burning version for the Clayface review only.

## What the burning logo does (read from `L:\Winter Wolfs Den review show\VFX\burning logo.mp4`)

- 5 seconds, 1920x1080, 24 fps, black background.
- Seconds 0 to 1: the full logo sits still. Blue-purple werewolf, cyan outline, white WINTER lettering, "WOLF'S DEN" in teal below, soft cyan glow, logo placed in the top left of the frame in this export.
- Seconds 1 to 2.5: fire starts at the lower letters and climbs. Embers and dark char eat the logo from the bottom up.
- Seconds 2.5 to 4: mostly gone, a few glowing embers and smoke.
- Seconds 4 to 5: black.
- **The file has no audio.** The sound was added in the edit, so I cannot read which effects you used. The picks below are from your owned library, not a copy of what you did.

## How to run it in Firefly

1. Open **Firefly > Generate video > Image to video**.
2. Upload the logo as the **start frame**: `L:\Winter Wolfs Den review show\Pictures\logo.png`. If the PNG has a transparent background, put it on solid black first so the glow reads.
3. Aspect ratio **16:9**, length **5 seconds**, camera **locked / static**.
4. Paste the prompt below. Generate 2 or 3 takes and pick the best. Run the Negative prompt box if Firefly shows one.

## Clayface look (what to aim for)

- The film Clayface and the 1992 Batman animated series version both read as **wet, glossy, lumpy clay that ripples and reshapes**. Sculpted, not liquid. Surface tension, thick folds, fingerprints and tool marks.
- **Color: warm brown clay**, like river mud, with lighter tan highlights and dark brown shadows (your call that it turns brown). I could not confirm the animated series color from the sources I found, so brown is your direction, not a quote from the show.
- The series trick Zac named: a limb **turns into a club or weapon**. The wolf's raised claw is the right spot for it.

## Which model (from Zac's real Firefly menu, 2026-10-25)

Menu: Firefly Video (commercially safe); partner models Veo 3.1, Veo 3.1 Fast, Veo 3.1 Lite, Gemini Omni Flash, Kling 3.0, Kling 3.0 Omni, Kling 2.5 Turbo, Runway Gen-4.5, Ray3.14, Ray3.14 HDR, Ray3, Ray3 HDR, Ray2.

1. **Kling 3.0** first. Built for consistency and precise control, so it should hold your logo and still morph it.
2. **Veo 3.1** second, for the most realistic wet clay and drips. Its Fast and Lite versions are cheaper for a test take.
3. **Runway Gen-4.5** if both mangle the logo and you want more control.
4. Skip Kling 3.0 Omni and Veo audio, you add your own sounds. Skip Firefly Video unless you need commercially safe.
5. In the panel: your logo is already in References > Frames. Set aspect 16:9, duration 5 s, audio off, and check whether a second end frame slot appears.

## Prompt A (main, the full sting)

> Start with the exact logo frame, an esports werewolf badge with cyan outline and white WINTER lettering, glowing softly on a pure black background, perfectly still for one second. Then the surface of the badge turns into wet brown sculpting clay, spreading from the bottom edge up across the letters and the wolf, glossy highlights, thick lumpy folds, visible fingerprints and sculpting marks. The clay rippling and shape-shifting: the wolf's raised claw swells and stretches into a heavy club, the face bulges and reforms, the lettering sags and melts into soft brown ridges but stays readable at first. Then the whole badge slumps and softens, thick brown clay drips and slides downward, the shape collapses into a slow melting puddle, the puddle sinks and thins away to nothing, leaving pure black. Locked static camera, dark moody lighting with a faint warm rim light, cinematic, smooth organic motion, no text added, no extra objects, no people.

## Prompt B (shorter, if A overcooks it)

> The logo stays still, then turns into glossy wet brown clay from the bottom up, the clay ripples and shape-shifts, the wolf's claw stretches into a club, then the whole logo melts and drips away to black. Static camera, black background, dark moody lighting.

## Prompt C (second pass, tighter melt, use if the first pass looks too liquid)

> Thick brown modeling clay with fingerprints and tool marks, slowly sagging and sliding off a werewolf badge logo, folds of clay pushing outward and reshaping, slow heavy melt, the logo dissolving into brown mud and fading to black, static camera, black background.

## Negative prompt (if the box exists)

> fire, flames, smoke, blood, extra text, watermark, new letters, people, faces other than the wolf, camera movement, zoom, bright background

## If the logo gets mangled

- Firefly often redraws text. If the letters turn to gibberish before the melt, that is fine for a sting that melts away, but the first second must stay clean. If it does not, build the melt in After Effects with your `burning logo.aep` project: replace the fire layers with a brown clay texture and a Turbulent Displace plus a Liquify. I can write the steps if you want.
- Match the length to the burn: 5 seconds. Drop it on V2 right after the intro line at 00:20.

## Sound plan (owned, from P:\Sounds\Sound FX)

All paths start with `P:\Sounds\Sound FX\`. Levels are starting points, adjust by ear.

| Time | Moment | Sound | Level |
|---|---|---|---|
| 0.0 s | Logo sits still | `low-long-background-rumble_fJ0TNBVO.mp3` fades in under the whole sting | -22 dB |
| 1.0 s | Clay starts crawling up | `splat-juicy-wet_fJlSm3EO.mp3` | -12 dB |
| 1.3 s | Ripple and shape-shift | `splat-juicy-wet_fJlSm3EO.mp3` again, pitch down 20 percent (Effect Controls, Pitch Shifter) | -16 dB |
| 2.0 s | The claw swells into a club | `deep-fast-whoosh_GyZDnHNu.mp3` | -14 dB |
| 2.6 s | Club lands, the logo slumps | `jg-032316-sfx-horror-style-impact-2.mp3` | -10 dB |
| 3.0 s to 4.2 s | Melt and drip | `splat-juicy-wet_fJlSm3EO.mp3` three times, 0.4 s apart, each a little quieter | -18, -22, -26 dB |
| 4.2 s | Gone, black | rumble fades out | 0.5 s fade |

- If you want a heavier thud on the slump: `P:\Sounds\Sound FX\Adobe\Drones\Drone Production Element Imaging Deep Subsonic Rumble Bass 02.wav` at 2.6 s, -18 dB.
- The burning sting probably used a fire sound. Your library has `fireball-whoosh_GknWsSNu.mp3` and `fire-wood-crackle-flames_G1y2ewE_.mp3`. Tell me which ones you used and I will list them here.
- Firefly video has no sound of its own for this use. Add every sound in Premiere.

## Gross mud sounds (added 2026-10-25, Zac: "like mud running down someone's skin")

All paths start with `P:\Sounds\Sound FX\Adobe\`. These replace the plain splat where you want it wetter and nastier.

| Use | File | Level |
|---|---|---|
| Clay crawling over the logo (the main mud-on-skin sound) | `Foley\Foley Mud Suction Wet 01.wav` | -12 dB |
| Slow drag, thick mud sliding | `Foley\Foley Mud Suction 01.wav` with 40 percent slow-down (Effect Controls > Speed/Duration) | -14 dB |
| Skin-like stretch while the claw swells into the club | `Horror\Horror Scary Skin Peeling Off Slowly.wav` | -16 dB |
| Squelchy drips during the melt | `Household\Household Sponge Squish Short 01.wav` x3, 0.4 s apart, pitch down 30 percent | -18, -22, -26 dB |
| Wet slap when the club lands | `Impacts\Impact Body Hit Wet 01.wav` | -12 dB |
| Optional, grossest: heavy wet tear on the first ripple | `Horror\Horror Scary Skin Rip Wet 01.wav` | -18 dB |

- The rip and peel sounds are the gross end. Skip the rip if it feels like too much over the logo.
- Layer the mud suction under your existing rumble. Same sounds work on PNG 9 and 14 in the Clayface run sheet if you want them wetter there too.

## Open for Zac

- Which sounds did you use on the burning logo? The video file is silent.
- Pick the take, then tell me and I will log it in TASKS.md.
- Matt paid for the credits, so run 2 or 3 takes of Prompt A, not a long chain of retries.

**All sounds in one folder (2026-10-25):** `P:\WWD Kit\Clayface\Sounds\` holds copies of every sound named above, plus the fire ones from your library. Pick and match in Premiere.
