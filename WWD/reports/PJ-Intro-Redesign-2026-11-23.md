# Percy Jackson intro redesign: "Trident Tide" (2026-11-23)

Author: wwd-vfx, for wwd-director. Date: 2026-11-23. Nothing generated, no credits, nothing posted, nothing pushed. Adobe apps and Zac's AE files were never opened. Originals were only read; frames and audio were pulled to `D:\WKP\scratch\pj-intro2\`.

Tags: PROVEN (I measured or saw it), SOURCED (a named file or page says it), PROPOSED (my design, not yet tested by anyone).

## 1. Which intro, and where it lives

PRIMARY (Zac named it, coordinator message): `L:\Winter Wolfs Den review show\Final\Percy Jackson Ep 4 recap and review.mp4`. PROVEN by ffprobe: 1920x1080, 59.94 fps, 2356.3 s, AAC 48 kHz stereo.

What it does (frames every 0.5 s, first 14 s, plus full-size pulls at 0.2, 3.4, 3.6, 8 s):
- 0.0 to about 3.5 s: a stock-looking underwater plate (sun rays, rippling surface, sandy floor). Small, dark, blurry text "PERCY JACKSON & THE OLYMPIANS" sits in the middle and scales up slowly to full size.
- About 3.5 s: the two host webcams appear stacked on the left (about 535 px wide each, 1/3 of the frame), the title snaps to the right panel and stays there. The same frame is the background for the whole talking stretch (I checked 14 s of it, it did not change).
- No logo sting in Ep 4. No sound design (see section 2).

Sibling candidates, covered briefly (PROVEN by frame pulls of the first 40 s):
- `Final\Percey Jackson 1 and 2.mp4` (59.94 fps): opens with a Winter Wolf's Den logo sting, the shield burns away in embers (about 0 to 3.4 s), then the same underwater title zoom, cams join at about 6 s. Its sound: audio exists 1.1 to 3.4 s (the burn), silence 3.4 to 6.6 s (the title zoom), voices from about 6.6 s.
- `Final\Percey Jackson EP 3.mp4`: three frames of an "Episode 3" thumbnail card (Medusa and Percy), then the same underwater title and cams.
- Eps 5 to 7 and 8 use the same plate (contact sheets final3 to final7 in the scratch folder). I did not zoom each one.
- Source of the plate: a project `Seabed UnderWater.aep` with converted copies and a 10 s `_UnderWater.mp4` (1920x1080, 25 fps) sit in `L:\...\Raw Footage\Percey Jackson\Season 1\Percey Jackson 1 & 2\Seabed-UnderWater-folder\`. It is a template project (the file name pattern looks like a store template). I did not open it (Adobe file, read-only rule) and its license is NOT KNOWN. Treat it as unlicensed until Zac has the receipt.
- Zac said his own AE build is the intro. I found no AE project named for the PJ intro. Other AE projects on L: (`After Effects\burning logo.aep`, `Frost-Cast\Title\Frozen Winter Logo Reveal.aep`) are other shows. Season 2 (edited Ep 1&2) has a different intro (ice wave, "Let the Hunt Begin", per the coordinator's earlier pull). I did not rescan Season 2 or 3.
- P:\WWD Kit holds no Season 1 intro export (kit folders listed, none match).

Why Ep 4 is the show intro: Zac pointed to it, and it is the version with no extra sting, so it shows the pure title design that every episode shares.

## 2. Frame by frame analysis (Ep 4, first 12 s)

PROVEN measurements:
- Audio, first 12 s: integrated loudness -19.6 LUFS, loudness range 4.2 LU, true peak -6.1 dBFS. The spectrogram is all speech (voice formants, no sustained music bed, no swell, no impact). In other words the intro has NO sound of its own in Ep 4. I cannot hear audio, this is from the spectrogram and levels only.
- The title text is olive green-gold on mid blue: low contrast. At 0.2 s it is a smudge about 180 px wide.
- Scene-change detection finds no hard cut, so the "cams join" at 3.5 s is a pop, not a designed move (I did not see an ease or slide in the half-second frames).

What works (honest):
- The show title is clear after 4 s and the cams are readable at once.
- A water theme is right for Percy Jackson.
- It is short.

What looks amateur, specific:
1. Layout: the title sits in a plain two-thirds panel with no frame, no brand, no hierarchy. "& THE" and "OLYMPIANS" are three stacked lines in the same size class. Nothing says Winter Wolf's Den.
2. Typography: a decorative fantasy face with a flat olive fill and a faint bevel. Contrast against the blue is weak, the fill color is close to the water color. Letter spacing is default.
3. Motion: a slow linear scale up from a speck. There is no anticipation, no impact, no settle, so it looks like a plug-in preset.
4. Easing: the scale looks even speed; the cams pop in with no slide or ease.
5. Color: one blue gradient, one olive text. No accent, no second light. The WWD cyan and white is missing.
6. Depth: the plate is a flat stock loop, the title sits on top with no light interaction, no depth blur, no bubbles or particles, no shadow.
7. Sound: none. The title zoom plays over silence or the first spoken words.
8. Brand: the Ep 1&2 version spends 3 s on a logo burn that has nothing to do with water. Ep 4 drops the logo entirely.
9. Template risk: the plate comes from a template with an unknown license, and the look is shared by anyone who has the same pack.

## 3. The new design in 10 lines (PROPOSED, built and rendered free)

1. Concept "Trident Tide": the Winter Wolf's Den shield rises from the deep, a bronze trident thrusts up behind it, the pair becomes the crest that sits over the title, the title surfaces, the host slots slide in. Brand and show fused in one 6 s move.
2. 0.0 to 0.5 s: black fades up into deep icy water, thin caustic lines near the surface, soft light shafts, a few bubbles. Low water bed.
3. 0.3 to 1.5 s: the wolf shield rises from below the frame (wobble from the water decays), cyan rim glow pulses.
4. 1.45 to 1.95 s: a bronze trident head thrusts up from behind the shield with a small overshoot, so the shield and trident read as one crest.
5. 1.95 s IMPACT: soft flash, two shock rings, a bubble burst, 0.4 s of camera shake, a 4 percent camera punch-in that settles.
6. 2.05 to 2.7 s: the crest scales down and travels to the right panel, bubbles trail it.
7. 2.55 to 3.1 s: "PERCY JACKSON" surfaces left to right (blur to sharp, small rise), gold with a navy outline and cyan glow; Greek key rule draws out from the center at 3.0 s; "& THE OLYMPIANS" follows at 3.15 s; "A WINTER WOLF'S DEN REVIEW" at 3.9 s.
8. 4.15 to 4.85 s: two host slots slide in from the left with cyan frames and bronze corner ticks. The live cams go on top of them in Premiere.
9. 5.0 to 5.6 s: one light glint crosses the title. 5.6 to 6.0 s: hold on the lockup, which is the plate for the talking section.
10. Sound (owned, Adobe library): deep underwater bed, a pitched-down whip for the thrust, gong plus orchestral hit plus water-and-ice impact at 1.95 s, bubble pop burst, a soft cymbal wash and horn swell under the title. Built, not heard by me.

Reference thinking, principle only (no look copied): film title design where one object lands and then the type resolves (impact then settle); channel branding that fuses the channel mark with the show mark in a crest. I did not run a web search in this job (time and the primary file was given), so no source URLs are listed. Everything here is my own design: own caustics code, own trident vector, own Greek key, system font Constantia, the show's own WWD logo.

Never used: a studio logo, a studio font, studio art, any Percy Jackson actor image.

## 4. Deliverables (all free)

Built version, viewed by frame pulls (PROVEN):
- `P:\WWD Kit\Percy Jackson Intro\Intro - Percy Jackson Trident Tide (MP4).mp4`: H.264, 1920x1080, 30 fps, 180 frames, 6.000 s, AAC 48 kHz stereo, 4.8 MB.
- `P:\WWD Kit\Percy Jackson Intro\Intro - Percy Jackson Trident Tide.mov`: ProRes 422 HQ, yuv422p10le, 6.000 s. Opaque, no alpha (the water is part of the shot), so "alpha" means opaque here.
- `P:\WWD Kit\Percy Jackson Intro\Intro Lockup Plate (last frame).png`: the held lockup, for the talking section.
- `P:\WWD Kit\Percy Jackson Intro\PJ Trident Head.png`: the trident as a 720x770 transparent PNG (also used in the AE guide).
- `P:\WWD Kit\Percy Jackson Intro\Intro Sound Mix (6 s, owned sounds).wav`: the mixed cue track.
- Build script (rebuilds everything): `D:\WKP\.claude\skills\wwd-review-photo-pull\scripts\make_pj_intro_new.py`. Frames and scratch in `D:\WKP\scratch\pj-intro-new\`.
- Firefly and Veo cards, linted PASS: `D:\WKP\WWD\reports\PJ-Intro-Firefly-Prompts-2026-11-23.md`.

Frame checks on the encoded mp4 (PROVEN, viewed): 0.1 s dark water with bubbles, 0.8 s shield rising, 1.6 s crest with trident, 1.95 to 2.1 s impact and rings, 2.3 s crest traveling, 3.0 s title half revealed, 3.7 s both lines and the key rule, 4.4 s slots sliding in, 5.2 s glint on "R" of PERCY, 5.9 s final lockup. After the first render the impact flash was a blown white disc over the wolf, I lowered it and re-rendered frames 58 to 76, then re-viewed 1.9, 1.97, 2.0 and 2.1 s. No black frames found by blackdetect. Sound: integrated -20.0 LUFS, true peak -1.9 dBFS (ffmpeg), audio stream present 6.000 s. I cannot hear audio.

Known weak spots in my own build (honest):
- The Greek key line is small and low contrast. A hand-built version in AE can be bigger.
- The wolf logo is a flat vector, so it does not get true underwater refraction, only a wobble that decays.
- The caustics are code-made lines, not real water. Shot A (Veo) would be more real if Zac wants to spend.
- The slots are plain placeholders, the hosts' cams cover them.
- Frame rate: the rest of the Final files are 59.94 fps. This is 30 fps as Zac ordered. Drop it on a 59.94 timeline and Premiere will repeat frames, so use a 30 fps sequence or accept it (PROPOSED: check the sequence).

## 5. Sound plan (owned files only, all copies of Adobe library items)

| Time | Cue | File | Level (PROPOSED) |
|---|---|---|---|
| 0.0 to 6.0 | Deep underwater bed (10 to 16 s slice) | `P:\Sounds\Sound FX\Adobe\Underwater\Underwater Water Ambience Deep Cave Abyss Surreal 01.wav` | 0.9 gain, fade in 0.6 s, out from 5.0 s |
| 0.0 to 6.0 | Slow bubbles (5 to 11 s slice) | `...\Underwater\Underwater Water Ambience Slow Bubbles 01.wav` | 0.5 gain |
| 1.35 | Trident thrust whip, slowed to 60 percent speed | `P:\Sounds\Sound FX\Adobe\Weapons\Weapon Staff Whip Thin Fast 01.wav` | 2.2 gain |
| 1.95 | Impact: gong, orchestral hit, water and ice | `P:\Sounds\Music\adobe\Classical&Orchestral\Orchestral_(solo&ensemble)_120BPM\OrchGong10-Dhit.wav`, `...\Orchestra_60BPM\OrchHits01-C.wav`, `P:\Sounds\Sound FX\Adobe\Liquid-Water\Liquid Water And Ice Impact 04.wav` | 0.9, 0.5, 1.0 |
| 2.0 | Bubble burst | `...\Liquid-Water\Liquid Water Bubble Surfacing And Popping Multiple 01.wav` | 0.8 |
| 2.55 | Title shimmer, first 1.6 s | `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Electronic Whoosh Digital Resonant Cymbal Wash 01.wav` | 0.45 |
| 2.6 | Horn swell | `P:\Sounds\Music\adobe\Classical&Orchestral\Horns_E_80BPM\HornsE05.wav` | 0.35, fade out |

License basis: Adobe library items, owned via subscription, free to use per Zac (as recorded in the sound pull README of 2026-11-23). No music beyond these short Adobe one-shots. Review intro sting length rule: 6 s or less (feedback-intro-length), this is exactly 6.0 s. Zac can ask for a 4 s cut: drop the 0.3 to 0.8 s dead time and start the rise at 0.0 (PROPOSED).

Sound-designer and motion-graphics benches: I did not route this through them. Both live under studio-director for non-WWD work and the job is a WWD kit piece, so wwd-vfx (me) owns it. Sound matching is in my charter. Say so if wwd-director wants a second pair of ears from `wwd-sound`.

## 6. Credit plan, lowest-credit way for each element

| Element | How made | Credits |
|---|---|---|
| Water, light shafts, caustics, bubbles | Code (this build), or AE Fractal Noise (guide) | 0 |
| Wolf shield | Existing WWD logo PNG | 0 |
| Trident head | Own vector, PNG supplied | 0 |
| Title, key rule, slots | Code or AE text and shape layers | 0 |
| Sounds | Owned Adobe library | 0 |
| Optional real water plate (Shot A) | Veo 3.1 Fast draft then Veo 3.1 | NOT RETRIEVED |
| Optional real trident (Shot B) | Firefly Image still plus Veo 3.1 | NOT RETRIEVED |

## 7. After Effects BUILD GUIDE for Zac

Everything here is PROPOSED. I did not open After Effects (Adobe apps are off limits to me), so menu names and numbers are from my knowledge of the program and from the working numbers in the build script. Effect names can differ slightly by version. If an effect is missing, use the "If stuck" line. Build in a copy: File > Save As > "PJ Intro Trident Tide v1.aep" in a new folder. Never touch your old project.

Files you need (all on disk):
- Logo: `L:\Winter Wolfs Den review show\Pictures\logo.png` (1920x1080, transparent, the shield is centered).
- Trident: `P:\WWD Kit\Percy Jackson Intro\PJ Trident Head.png` (720x770, transparent).
- Sounds: the seven files in section 5, or `P:\WWD Kit\Percy Jackson Intro\Intro Sound Mix (6 s, owned sounds).wav` for one drop-in track.
- Font: Constantia Bold and Constantia Italic (come with Windows). Check: Character panel font list.

### Step 1. Project and comps
1. File > New > New Project.
2. Composition > New Composition. Name "PJ INTRO MAIN". Width 1920, Height 1080, Pixel Aspect Square, Frame Rate 30, Duration 0:00:06:00, Background Color black. OK.
3. File > Import > File. Pick the logo PNG and the trident PNG. Import the sound files too. Drag all into the Project panel.
4. Composition > New Composition. Name "WATER BG". 1920x1080, 30 fps, 0:00:06:00. This is a pre-comp: all the water goes here so the main comp stays clean.

### Step 2. WATER BG comp (the deep water)
Layer order top to bottom:
1. Bubbles (shape layers, step 2g).
2. LIGHT SHAFTS.
3. CAUSTICS.
4. DEPTH (gradient).

2a. DEPTH. Layer > New > Solid. Name DEPTH, Make Comp Size, color any. Effect > Generate > Gradient Ramp. Start of Ramp 960,0. End of Ramp 960,1080. Start Color #4DA8CC (light teal blue). End Color #010A1A (near black navy). Ramp Shape Linear Ramp. Scrub: top bright, bottom dark.
2b. CAUSTICS. New Solid, name CAUSTICS. Effect > Noise & Grain > Fractal Noise. Fractal Type: Turbulent Smooth. Noise Type: Soft Linear. Check Invert. Contrast 220. Brightness -60. Transform: uncheck Uniform Scaling, Scale Width 180, Scale Height 100. Evolution: Alt-click the stopwatch and type `time*60`. Then Effect > Color Correction > Tint: Map Black To #000000, Map White To #8EE8FF. Effect > Blur & Sharpen > Fast Box Blur, Blur Radius 1. Set the layer Blend Mode to Add (select layer, press F4 to show the modes column). Layer Opacity 55%. Then add a mask to fade it with depth: Rectangle tool, draw a box over the whole comp, press M twice, set Mask Feather 0,600, Mask Expansion 0, then drag the lower mask points up so the mask covers only the top 55 percent of the frame. (The caustics should live in the top half only, the build fades them out by 62 percent of the height.)
   If stuck: if Fractal Noise looks like clouds, not lines, raise Contrast to 300 and set Fractal Type to Turbulent Basic.
2c. LIGHT SHAFTS. New Solid, name LIGHT SHAFTS. Effect > Noise & Grain > Fractal Noise: Fractal Type Basic, Noise Type Soft Linear, Contrast 190, Brightness -40, Transform: uncheck Uniform Scaling, Scale Width 2500, Scale Height 40 (this makes tall soft stripes: swap the two numbers if your stripes come out flat), Evolution `time*8`. Effect > Generate > CC Light Rays (found in some versions as "CC Light Rays" under Generate). Intensity 110, Center 960,-150, Radius 55, Warp Softness 100, Shape Round, Direction 0, Color From Source on. Blend Mode Add. Opacity 40%. Effect > Distort > Transform (the effect, not the panel): Skew 6 so the beams lean.
2d. SURFACE BAND (optional). Duplicate CAUSTICS, rename SURFACE, change Fractal Noise Scale Width to 400, drag its mask to the top 10 percent only, Opacity 70%.
2e. Camera push. Layer > New > Null Object, name "BG PUSH". In WATER BG: select all layers except the null, set each layer's Parent (the spiral in the Parent column) to BG PUSH. On BG PUSH press S for Scale. At 0:00 set Scale 100%. At 6:00 set 107%. Set Anchor Point (A key) to 960,380 so it pushes toward the upper middle.
2f. Fade in. In PJ INTRO MAIN you will fade the whole water: see Step 3.
2g. Bubbles. Select the Ellipse Tool, draw a small circle. In the Fill/Stroke settings click Fill and choose None, Stroke white, width 3. Name the layer BUBBLE 1. Size (Ellipse Path > Size) 24,24. Opacity 60%. Position expression: Alt-click the Position stopwatch and paste:

```
startX = 200 + index*140;
spd = 70 + (index % 5)*22;
[startX + Math.sin(time*1.7 + index)*18, 1160 - (time + index*0.35)*spd]
```
   Duplicate the layer (Ctrl+D) 11 times. Change each copy's Ellipse Path > Size to a mix of 10, 16, 24, 36 so the bubbles differ. Bubbles rise from below the frame.
   If stuck: if all bubbles move in lockstep, check the `index` word is in the expression (index is the layer number).

### Step 3. PJ INTRO MAIN: the crest
1. Drag WATER BG into PJ INTRO MAIN as the bottom layer.
2. Fade in: select WATER BG, press T for Opacity. At 0:00 Opacity 12%. At 0:16 (frame 16, press Ctrl+G, type 16) set 100%. Select both keys, press F9 (Easy Ease).
3. Drag logo.png onto the timeline above WATER BG. Rename "WOLF SHIELD". Position will be animated. Turn on 3D? No, keep it 2D.
   - Press P. At 0:09 (0.3 s) Position 960,1190. At 1:15 (1.5 s) Position 960,560. Select both keys, F9. Then open the Graph Editor (the graph icon on the timeline top), choose Value Graph, drag the end handle of the second key to the right and low so the movement is fast at first and glides at the end (ease out). 
   - Press S. At 0:09 Scale 56%. At 1:15 Scale 62%. Press F9 on both.
   - Press T. At 0:09 Opacity 0%. At 0:24 Opacity 100%.
   - Effect > Distort > Turbulent Displace: Amount 9, Size 40, Complexity 1. Animate Amount: at 0:09 value 9, at 1:21 value 0, F9 both. (This is the water wobble that settles.)
   - Effect > Stylize > Glow: Glow Threshold 75%, Glow Radius 30, Glow Intensity 0.6, Colors A and B Colors, Color A #5AE1FF, Color B #1B6BFF.
4. Trident: drag PJ Trident Head.png above WATER BG and BELOW WOLF SHIELD in the stack (it must sit behind the shield). Rename TRIDENT.
   - Press S. Set Scale 37% from 1:12 to 1:15 on the stage, and animate to 27.5% (the lockup size) between 2:03 and 2:23: at 2:03 Scale 37%, at 2:23 Scale 27.5%. F9 both.
   - Press P. At 1:12 (1.4 s) Position 960,503. At 1:27 (1.9 s) Position 960,289. Add a third key at 1:29 Position 960,280 and a fourth at 1:31 Position 960,289 for the small overshoot. Easy Ease the keys. The head rises behind the shield and ends with the prongs above the shield top.
   - Press T: Opacity 0% at 1:12, 100% at 1:16.
   - Effect > Stylize > Glow: Threshold 70%, Radius 25, Intensity 0.8, Color A #5AE1FF.
5. IMPACT at 1:27 to 1:29 (the trident lands at 1:27, the impact peak is at 1:28 or 1:29; the build used 1.95 s = frame 58/59, use 1:28).
   - New Solid, name FLASH, white. Set Mode Add. Opacity: 0% at 1:27, 45% at 1:28, 0% at 1:34. Scale it to 150% and add a radial mask: Ellipse tool double-click makes a full mask, set Mask Feather 400.
   - Layer > New > Shape Layer, name RING. Ellipse tool, hold Ctrl to draw from center. Fill None, Stroke #CFF6FF width 22. Position 960,560. Ellipse Path Size: 1:28 value 120,120, 2:22 value 2400,2400. Opacity 90% at 1:28, 0% at 2:22. Easy Ease out. Duplicate: RING 2, stroke 10, end size 1500, 2:19.
   - Shake: New Null "SHAKE". Position expression: 
```
t0 = 1.95;
if (time < t0 || time > t0 + 0.4) { value } else {
a = 14*Math.exp(-(time - t0)*11);
value + [a*Math.sin(time*90), 0.7*a*Math.cos(time*77)]
}
```
   Parent WOLF SHIELD, TRIDENT and WATER BG to SHAKE (Parent column spiral).
   - Camera punch: select WATER BG Scale. Add a keyframe at 1:28 Scale 104% above the push value and one at 2:10 back to what the push gives. Simplest: add an Adjustment Layer named PUNCH above WATER BG, add Effect > Distort > Transform, Scale 104 at 1:28 and 100 at 2:10 with Easy Ease. (PROPOSED)
6. Crest travel (2:05 to 2:23). Position WOLF SHIELD: at 2:05 Position 960,560, at 2:23 Position 1227,345. Scale: at 2:05 62%, at 2:23 25%. Easy Ease both. Position TRIDENT: at 2:05 960,289, at 2:23 1227,220. Do the same eases. The crest is now sitting in the right panel.
   Bubble burst: duplicate five BUBBLE layers, change their position expression so they start at 960,560 at 1:28 and drift upward: simplest, remove the expression and keyframe Position from 960,560 at 1:28 to a random point 300 px up and 400 px sideways at 3:10. Opacity 100% to 0% across the same span. (PROPOSED, optional.)

### Step 4. Title
1. Right panel center is x 1227. Use the Text tool (Ctrl+T), click anywhere, type PERCY JACKSON. Set the Character panel: Constantia Bold, size 124 px, tracking 60, all caps, Fill color #FFE8A0. Paragraph panel: Center. Position the text layer so its center is X 1227, Y 560 (set Position 1227,560 and Anchor Point to the text center using Layer > Transform > Center Anchor Point in Group, or the Pan Behind tool).
2. Layer Styles (right-click the layer > Layer Styles):
   - Gradient Overlay: Blend Mode Normal, Opacity 100, Colors left #FFE8A0 right #B07430, Style Linear, Angle 90 (bright on top).
   - Stroke: Size 5, Position Outside, Color #05173A.
   - Outer Glow: Color #5AE1FF, Opacity 55, Size 25.
   - Bevel and Emboss: Depth 80, Size 3, Soften 1.
3. Reveal (text animator). Expand the text layer > Text > Animate > Opacity. Set Opacity 0%. Click Add (the Animator arrow) > Property > Blur, set Blur 40,40. Add > Property > Position, set 0,30. Expand Range Selector 1: Advanced > Based On Characters, Shape Square, Smoothness 100%. Animate Offset: at 2:17 (2.55 s) Offset -100%, at 3:15 (3.5 s) Offset 100%. Easy Ease. The letters surface left to right, blurred, rising.
4. Second line: duplicate the layer, change text to "& THE OLYMPIANS", size 76, tracking 140, Fill gradient #EBFCFF to #78CDEB, Position 1227,722. Retime the animator: Offset -100% at 3:05, 100% at 3:29.
5. Third line: duplicate again, text "A WINTER WOLF'S DEN REVIEW", Constantia Italic, size 42, tracking 70, gradient #BEF0FF to #6EC8EB, remove Bevel, Position 1227,815. Animator Offset -100% at 3:27, 100% at 4:18 (about 3.9 to 4.6 s).
6. Greek key line. Layer > New > Shape Layer, name KEY. Add > Path. Click the path Vertices: easiest is Pen tool: click six points inside the comp, then in Path expand Vertices and type: (0,27) (0,3) (24,3) (24,18) (9,18) (9,13) (20,13) relative to the shape. Fill None, Stroke #D19945 width 4, Line Join Round. Add > Repeater. Copies 25, Transform: Repeater > Position 30,0. Group Position so the strip is centered at X 1227, Y 660 (its width is 750). Animate reveal from the center out: Layer > Mask > New Mask > Rectangle, then Alt-click Mask Path stopwatch is not needed: set two Mask Path keys, key 1 at 3:00 a rectangle only 4 px wide at X 1227, key 2 at 3:24 a rectangle 760 px wide centered at X 1227. Easy Ease out. If the shape looks like random hooks, make the first vertex (0,27) and check the order.
7. Glint. Select the PERCY JACKSON layer. Effect > Generate > CC Light Sweep: Direction 45, Shape Smooth, Width 38, Sweep Intensity 60, Edge Intensity 20, Edge Thickness 4, Light Color white. Animate Center: at 5:00 Center 600,560, at 5:18 Center 1900,560. Easy Ease.

### Step 5. Host slots (guide for the live cams)
1. New Solid 535 x 540 named SLOT TOP, color #050F24. Effect > Generate > Stroke is for masks, so use a shape layer: Rectangle path 535x540 with stroke #59E1FF width 4, fill #050F24 at 85% opacity. Duplicate for the lower slot at Position y 810.
2. Animate Position X from -270 to 267.5 between 4:05 and 4:22 for the top one (Easy Ease out) and 4:10 to 4:27 for the lower. (4.15 and 4.3 s start in the build.)
3. In the real edit, put the two webcam clips over these slots in Premiere. In AE you can skip this step and export the plate with slots empty.

### Step 6. Sound inside AE
1. Drag the sound files into the PJ INTRO MAIN timeline bottom. Set start times as in section 5. Or drag the single mix WAV to 0:00.
2. If you place single files: gain is done in Premiere or Audition; AE's Audio Levels work too (press L under each layer, values in dB: bed -1 dB, bubbles -6 dB, whip +6 dB, impacts -1 dB, bubble burst -2 dB, shimmer -7 dB, horn -9 dB). PROPOSED, taken from the ffmpeg gains used in the build.

### Step 7. Check and render
1. Drag the playhead through 0:00, 0:24, 1:15, 1:28, 2:23, 3:10, 4:18, 5:29. Compare to the PNG frames in `D:\WKP\scratch\pj-intro-new\chk2\` and to the MP4.
2. Composition > Add to Render Queue (Ctrl+M). Render Settings: Best Quality, Resolution Full, Frame Rate Use comp's, Time Span Length of Comp. Output Module: Format QuickTime, Video Codec Apple ProRes 422 HQ, Channels RGB, Audio Output On (48 kHz stereo 16 bit). Your notes say ProRes freezes on your machine, so also add Composition > Add to Adobe Media Encoder Queue, Format H.264, Preset Match Source - High bitrate, 1920x1080, 30 fps, Target Bitrate 16 Mbps VBR 1 pass. Output file name "PJ Intro Trident Tide v1.mp4" into a new folder, never over the old file.
3. In Premiere: use a 30 fps sequence for this clip or let it conform. Put the host webcams over the two slots from 4:15 on. The lockup (last frame) holds behind the show: use `Intro Lockup Plate (last frame).png` as the held background, with the cams stacked on the left as before.

## 8. Firefly shots (not generated, linted)
Doc: `D:\WKP\WWD\reports\PJ-Intro-Firefly-Prompts-2026-11-23.md`. Two optional cards (a real water plate, a real trident). Lint PASS on all three prompt blocks (real command output pasted in that file). Credit cost: NOT RETRIEVED. Nobody can test a prompt without spending Zac's credits (Matt paid for them). Cheap path first: ship the free built version and draft Shot A on Veo 3.1 Fast at 720p only if Zac wants more depth.

## 9. What I could not verify
- Audio: I cannot hear. Levels and spectrograms only. The new mix was never heard by a person.
- Whether the Ep 4 intro in Zac's mind is exactly this one. I took his named file.
- The AE build guide steps: written from knowledge, not run in After Effects (Adobe is off limits). Effect names and some values may need a tweak.
- Whether the Seabed template license is clean: NOT KNOWN.
- Firefly and Veo panel facts and credit cost: NOT RETRIEVED.
- Season 2 and 3 intros: not rescanned by me.
- The 59.94 versus 30 fps question for the edit: Zac's sequence settings are not known to me.
- I did not run web research for this redesign, so no outside references are cited.
