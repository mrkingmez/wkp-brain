# Premiere Pro built-in video transitions

Source: Adobe Help Center, "List of Video transitions" and "List of Video
Dissolve transitions" (both last updated 7 Jan 2026), read 2026-10-11 through
Zac's Chrome. Zac is on the Adobe defaults, so recommendations come ONLY from
this list. Never recommend a third-party pack or a transition not named here.

Adobe's newer "modern transitions" set (a separate group of ~90 effects) is
NOT in the list above. If Zac says he has it, ask for the names before using it.

## Full list by category (Effects panel > Video Transitions)

| Category | Transitions |
|---|---|
| Dissolve | Additive Dissolve, Cross Dissolve, Dip To Black, Dip To White, Film Dissolve, Morph Cut, Non-Additive Dissolve |
| Immersive Video | VR Chroma Leaks, VR Gradient Wipe, VR Iris Wipe, VR Light Leaks, VR Light Rays, VR Mobius Zoom, VR Random Blocks, VR Spherical Blur |
| Iris | Iris Box, Iris Cross, Iris Diamond, Iris Round |
| Page Peel | Page Peel, Page Turn |
| Slide | Band Slide, Center Split, Push, Slide, Split, Whip |
| Wipe | Band Wipe, Barn Doors, Checker Wipe, CheckerBoard, Clock Wipe, Inset, Paint Splatter, Pinwheel, Radial Wipe, Random Blocks, Random Wipe, Spiral Boxes, Venetian Blinds, Wedge Wipe, Wipe, Zig-Zag Blocks |
| Zoom | Cross Zoom |

## What the dissolves actually do (Adobe's descriptions)

- **Cross Dissolve** - fades A out while B fades in. The safe default.
- **Dip To Black** - A to black, then black to B. Warning from Adobe: it also
  affects video on lower tracks, so on a stacked timeline Cross Dissolve may
  be the better choice.
- **Dip To White** - A to white, then white to B. A flash.
- **Film Dissolve** - blends in linear color space, so it looks more natural
  than Cross Dissolve. Good on dark, moody footage.
- **Additive Dissolve** - adds clip B's color to A, then subtracts A from B. Brightens and glows.
- **Non-Additive Dissolve** - crossfade without the brightening glow.
- **Morph Cut** - face-tracked smoothing for a jump cut on ONE person talking.
  Talking-head cuts only, never between stills.

## Picking for a WWD review (horror and dark material)

Default to restraint. A review is two guys talking over images, and the
images should support the joke or the point, not draw attention to themselves.

| Moment | Use | Why |
|---|---|---|
| Image fades in over commentary, neutral beat | Cross Dissolve, 10 to 15 frames | Invisible, safe |
| Dark, moody film still, atmosphere talk | Film Dissolve | Cleaner blend on dark frames, no gray mid-fade |
| Topic change, new act of the review | Dip To Black | Reads as a chapter break |
| Jump scare, shock, big reveal talk | Dip To White (short, 6 to 8 frames) or a hard cut | The flash sells the hit |
| Fast joke, quick back-to-back images | Hard cut, or Whip | Whip keeps the energy up |
| Gag where one image answers another | Push or Slide | Directional, reads as call and response |
| Jump cut inside one host's sentence | Morph Cut | Only for talking heads |
| Poster at the open or close | Cross Dissolve, slow (20 to 30 frames) | Gives it weight |

Avoid for a horror review: Page Peel, Page Turn, Iris (all four), Checker
Wipe, CheckerBoard, Random Blocks, Spiral Boxes, Pinwheel, Paint Splatter,
Venetian Blinds, Zig-Zag Blocks, and every VR transition. They read as
cheesy or as a 2000s slideshow and fight the tone.

Rule of thumb for the report: roughly 6 of every 10 placements are a hard cut
or Cross Dissolve. If every image has a different transition, it is too busy.

## Always include one "fun" transition (Zac's standing rule, 2026-10-13)

Every placement report gets at least one creative, on-theme transition
(usually the poster open or close) so the review is entertaining, not just
clean. Zac's words: "I always want some fun one in there to make it more
entertaining." This is the one exception to the "restraint" rule above, and
it can be built from Premiere's own effects, not just the transitions list.

Horror recipes (all stock Premiere effects, keyframed on the image clip):

- **Melt away:** Effects > Distort > Turbulent Displace (Displacement: Twist
  or Vertical Displacement, Amount 0 to ~120, Size ~40) plus Distort > Wave
  Warp (Wave Type Smooth Noise, Zac confirmed 2026-10-13, there is no "smooth wave"; Direction 0, slow). Keyframe Amount up while Opacity drops 100 to 0 over
  ~24 to 36 frames. Add Transition > Linear Wipe (Direction 180, Feather
  ~25%) moving top to bottom so it drips away instead of fading flat.
- **Blood oozing away:** Put the image on V2. Add a red solid or Color Matte
  (dark red) above it with Linear Wipe (180 degrees, Feather ~15%, keyframed
  0 to 100%) so red runs down over the poster, then Cross Dissolve the red
  into the next shot. Blend Mode Multiply on the red layer keeps the poster
  detail visible under the blood. Optional: Turbulent Displace on the red
  layer for a ragged edge.
- **Cheat that looks great:** a free blood-drip or ink-bleed overlay clip
  (any stock pack, set Blend Mode to Multiply or use Track Matte Key with
  Luma Matte) on the layer above the poster. Needs a clip Zac supplies, so
  name it as optional.

- **Blood recipe fix (Zac, 2026-10-13):** a Multiply color matte on its own tints everything below, including the host cams. Add Track Matte Key to the matte (Matte = the poster's track, Composite Using = Matte Alpha) so the red only lands on the poster's pixels. Works because our PNGs have transparent padding.

- **Update 2026-10-13:** Track Matte Key's Matte list showed only None on Zac's build. Use Crop on the matte instead: our PNG posters sit centered in 1920x1080 (portrait 2:3 poster = pixels 600 to 1320), so Left 31.25% and Right 31.25% trims the red to the poster. Compute from the real alpha bbox for any other aspect. Also: while troubleshooting a doc, edit the same file in place, do not make a new versioned copy per change (Zac 2026-10-13).

## Fun layer is mandatory, with sound (Zac, 2026-10-14)

Zac reviewed the Carrie report and said it had no fun: all hard cuts and dissolves, no sound effects, and only a blood close. Every placement report now ships a fun layer, not just one creepy transition:

- At least five built moments (poster open, a recurring award sticker, a spoiler or act-break alarm, a blood or horror transition WITH sound, a closing card), tiered so the cheap ones come first.
- A timecoded sound cue map (about 1 cue per 70 seconds), every cue tied to a line the hosts actually said (puns, counts, nicknames, gotchas). Dialogue wins, silence counts as a cue.
- The Den Kit, eight recurring sounds (Stamp Thud, Record Needle, Phone Ping, Shutter Burst, Heartbeat, Magnet Groan, Gavel, Blood Splat) so the sound becomes ours. No vine boom or airhorn style meme sounds.
- The Wolfie Awards sticker is the standing recurring graphic. Keep the same sticker shape, change the text.
- **Music is intro and outro only (LOCKED 2026-10-17, Zac, from viewer feedback: music under the talk is distracting, "we are not a movie").** No beds or loops under the conversation, no thinking or spoiler music. Short sound effects and stings of a few seconds on a gag are fine. Suno prompts are for the intro and outro only (instrumental, no artist or film names, check the Suno plan for commercial rights) and Firefly prompts for any sticker or card art. Firefly makes flat images, so generate on green and key it, add text in Premiere.
- Template: see Parts A to F of `WWD\reports\Carrie-Image-Placement.md`.
- **Tone check on every cue (Zac, 2026-10-14):** Match the tone of the movie, not just the joke. The fun comes from the hosts' lines, but the sound underneath must fit what is on screen. No comedy music or cartoon sounds over death, abuse, bullying violence or school-shooting talk. Dry and dark beats funny there: a silence, a heartbeat, a low hit, or no cue at all. Zac's example: no Benny Hill chase music while counting dead bodies.

## UPDATE 2026-10-14: overrides the "Adobe defaults only" and "6 of 10 plain" lines above

Zac: "Premiere has more than those three transitions... 90% is cross dissolve, hard cut, film dissolve. Lets mix up the transitions... I want this for every one moving forward. Remember we are competing to keep peoples attention."

- **Adobe's Modern transitions are available and are the main palette.** Source: Adobe Help Center, "Modern transitions in Premiere on desktop", last updated Aug 18, 2026, read through Zac's Chrome (WebFetch gets 403). Names, all ending in "Impacts" except where noted:
  - Essentials: Mosaic, Star Wipe, Chaos, Burn Alpha, Flash, Blur to Color, Roll, Stretch, Dissolve, Push, Burn Chroma, Blur Dissolve, Neon Wipe, Luma Fade, Clock Wipe, Linear Wipe, Frame.
  - Transformers: Film Roll, Page Peel, Louver, 3D Spin, 3D Roll, Panel Wipe, Split, Plateau Wipe, Slice, Wave, Stretch Wipe, Mirror, 3D Spinback, Slide.
  - Animation: Pull Motion, Block Motion, Travel Motion, Spin Motion, Flip Motion, Spring Motion, Pop Motion, Fold Motion, Typewriter.
  - Lights & Blurs: Chroma Leak, Light Sweep, Solarize, Ray, Radial Blur, Directional Blur, Glow, Flare, Zoom Blur, Stripe, Soft Wipe, Light Leak, Phosphor.
  - Smart Tools (not transitions, effects): Motion Tween, Motion Camera, Text Animator, Shape Flow, Shape Dissolve.
- **Target:** about half of placements (Carrie: 25 of 44) get a designed transition chosen to match the picture, each paired with a sound. The rest stay hard cut, Cross Dissolve or Film Dissolve so the designed ones pop. No back-to-back repeats, no designed transition more than twice per video.
- **Meaning map** (Carrie plan, Part H of its placement doc): social media or phone = Mosaic, Chaos, Zoom Blur, Flash plus Glitch Buzz; powers = Stretch, Wave, Radial Blur; fire or finale = Burn Alpha, Burn Chroma, Light Leak, Flare; prom or glam = Star Wipe, Glow, Light Sweep; two sides = Split, Mirror; quick jokes = Pop, Spring, Flip; dark or religious = Luma Fade, Blur Dissolve, Film Dissolve; flashbacks = Film Roll, Clock Wipe; discovery = Ray.
- **The old classic avoid list** (Page Peel, Iris, Checker Wipe and so on) still applies to the classic versions. The Impacts versions are different looks, use them by meaning.
- **Zac's own glitch transition:** he uses a glitch transition with a buzzing sound on posters in other videos. It is NOT on Adobe's modern list, so it is probably a third-party pack. Ask him for the exact name once and add it here.
- **Verdict stickers (standing kit with the Wolfie nominee badge):** Recommend Watch, Do Not Watch, Dumpster Fire, same wolf-mascot sticker style. Use each only where a host actually says it. Do not force all three into every video. Prompts and animation are in Part G of `WWD\reports\Carrie-Image-Placement.md`.
