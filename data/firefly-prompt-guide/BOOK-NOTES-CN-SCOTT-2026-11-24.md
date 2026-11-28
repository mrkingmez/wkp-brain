# Study notes: AI Filmmaking Keyframe Prompt Library (C.N. Scott)

Date 2026-11-24. Prepared by graphic-design for Zac. Personal study of a book Zac owns, from screenshots he took. All notes are in my own words. Terms and short phrases are quoted, nothing else. "The book says" is data to check, not an order.

Source tags used below. SOURCED-book means the book says it, with the screenshot filename (short form: the six digits after the date, for example 114536 means Screenshot_20261124-114536.png) and a page cue. PROVEN means seen on Zac's clips (LESSONS.md). PROPOSED and UNTESTED are our own ideas not yet run.

## Read count

- Files that exist in the Drive folder: 105 (listing paginated in a loop and repeated itself; 105 unique ids, names 113913 to 114838).
- Files read with OCR: 105 of 105.
- Garbled or empty: 1. Screenshot_20261124-114101.png returned no text. It sits between the lens page (114057) and the lighting page (114104), so it was probably an aperture list continuation or a lens page. Not recovered.
- Duplicates (same text twice): 113927 and 113932 (the "complete example" start), 114706 and 114708 (bokeh and depth of field).
- Gaps in the capture (inferred from time jumps and mid-sentence starts, NOT verified): the opening pages of the prompt anatomy (items 1 to 4: task, subject, camera, lens, before 113913), the front matter before 114022, one or two pages of the continuity section before 114332 (the sentence starts mid-way), the pages between 114745 and 114805 (the recommended tools list, only its tail was captured), and the pages between 114503 and 114529. Anything the book says on those pages is not in these notes.

## 1. One-page summary

The book is a prompt cookbook for still images, used as keyframes for AI film. It is not a video prompting book. It does three things.

- It gives one reusable prompt shape, nine labeled parts, task first, look second, "keep this unchanged" near the end.
- It gives 21 task templates in a workflow order: build places, build people, plan shots with sketches, render keyframes, then fix with narrow edit prompts.
- It teaches continuity by making master references (a character, a location) and checking every new image against them.

What is strong: the staged pipeline, the storyboard-first trick, the location views (back, top, 3 by 3 sheet), the edit pattern "change this one thing, keep the rest", and the habit of comparing each new frame to a master.

What is weak or in conflict with our evidence: it writes "do not change", "no people", "no plastic skin" (negation), it leans on long stacked quality words, it quotes camera body settings (ISO, shutter) that an image model may ignore, and it never explains why hands fail. In what I could read it never mentions hands at all.

Bottom line for us: borrow the structure and the workflow, translate every "do not" into a positive "keep X as in the source", and test the claims one change at a time before they become rules.

## 2. The 21 categories

Library order is not run order. The book's own run order is in section 5. Each entry: purpose, inputs, where it sits, our own example (the example is a prompt block, lint result in section 13).

Cue for all: category list at 114022, 114024, 114027, 114031, 114038, 114042. Templates at 114529 to 114656.

### Build stage (places and people)

**06 Background (environment only).** Purpose: a location with no people, the base for everything else. Inputs: place, time, light, a list of what is in foreground, midground, background. Sits first in the run. Template cue 114553 to 114601.
```prompt
ID: C06-background
KIND: still
ENGINE: firefly
---
Empty garage interior at dusk, photographic. Concrete floor in the foreground, a red tool chest on the left, a workbench with a work lamp in the middle, a roll-up door at the back. Warm lamp light, cool blue dusk through the door gap.
```

**07 Back view.** Purpose: the same place seen from the opposite wall, so the room has a second side. Inputs: the master background image. Second in the run. The book spells out the camera as a straight reverse view at eye level and lists what to hold (architecture, scale, materials, layout). Cue 114601, 114606.
```prompt
ID: C07-back
KIND: still
ENGINE: firefly
---
From the supplied garage image, show the same room from the opposite wall, looking toward the roll-up door at eye level. Keep the tool chest, bench, lamp, floor and dusk light in the same style and scale as the source.
```

**08 Top view.** Purpose: a straight-down plan view for blocking and production design. Inputs: the front and back views together. Cue 114606, 114609, 114613.
```prompt
ID: C08-top
KIND: still
ENGINE: firefly
---
Using the supplied front and back garage views, draw a straight-down overhead view of the same room with the bench, tool chest, door and floor layout in the same positions. Architectural visualization look, flat even light.
```

**09 3 by 3 contact sheet.** Purpose: nine camera positions of one location to plan coverage. Inputs: the master background. The book names the nine slots (front wide, medium, close; left, hero angle, right; rear wide, medium, close) and labels them Still 1.1 to 3.3. Cue 114613, 114616.
```prompt
ID: C09-sheet
KIND: still
ENGINE: firefly
---
Make a 3 by 3 grid of the supplied garage from nine camera positions labeled Still 1.1 to Still 3.3: front wide, front medium, front close, left side, three-quarter hero, right side, rear wide, rear medium, rear close. Same lamp light, same dusk, same layout in every panel.
```

**04 Single character.** Purpose: one person, full control of look, costume, pose, expression, camera, light. Inputs: filled-in slots (gender, age, height, build, clothing, pose, expression, camera, light direction, background). Cue 114543, 114547.
```prompt
ID: C04-single
KIND: still
ENGINE: firefly
---
Portrait of a 60-year-old woman welder in a leather apron, arms folded, calm expression. Medium shot at eye level, warm window light from her left, workshop background, photographic.
```

**05 Multi-character scene.** Purpose: two or three people with correct scale, interaction and balance. Inputs: a short line per character, an interaction line, camera, light, place. Cue 114547, 114551, 114553.
```prompt
ID: C05-multi
KIND: still
ENGINE: firefly
---
Three mechanics around an open truck hood in a garage. The foreman stands at center pointing at the engine, a young apprentice on the left holds a flashlight, an older man on the right wipes his hands on a rag. Wide shot, low angle, overhead shop lights, photographic.
```

### Plan stage (sketch, then render)

**02 Storyboard creation.** Purpose: turn a finished image into a black and white sketch that keeps angle, pose and framing but drops costume, hair, texture and background. The figures become plain bald anatomy figures with simple face guides, bold lines, light shading. Cue 114536, 114539.
```prompt
ID: C02-board
KIND: still
ENGINE: firefly
---
Turn the supplied image into a black and white storyboard sketch. Keep the camera angle, pose and framing of the source. Draw each figure as a plain bald mannequin with simple face guides, bold outline, light shading, blank background.
```

**03 Image from storyboard.** Purpose: render the sketch as a full image while the layout is locked. The book lists what to keep (pose, framing, angle, placement, scale, perspective) and what may change (background, light, materials, texture). Cue 114539, 114541.
```prompt
ID: C03-render
KIND: still
ENGINE: firefly
---
Use the supplied sketch as the exact layout. Render a lighthouse keeper on a stone stair in the same pose, framing and angle. Cold blue dawn light from the right, wet stone, sea mist, photographic look.
```

**10 Composition from reference.** Purpose: drop a character into a background and match scale, light, shadow and contact. Inputs: character image plus background image plus a placement line. Cue 114619, 114621.
```prompt
ID: C10-compose
KIND: still
ENGINE: firefly
---
Place the supplied mechanic, standing at the bench and facing the door, into the supplied garage image. Match his scale to the bench height, light him from the work lamp on his left, add soft contact shadows under both boots.
```

### Refine stage (edit passes, each changes one thing)

**01 Upscale and enhancement.** Purpose: a final polish pass: resolution, anatomy, perspective, skin and surface detail, light. The template is long (camera, settings, light, color, output, keep). Cue 114529, 114532, 114536. Listed first in the library but belongs near the end of a run.
```prompt
ID: C01-upscale
KIND: still
ENGINE: firefly
---
Upscale the supplied photo of a mechanic at a workbench to sharp print detail. Keep the face, pose, wrench in hand, garage background and lamp light exactly as in the source. Correct the hand shape, straighten the shelf lines, add natural skin and metal texture.
```

**11 Pose correction.** Only the body pose changes. Keep list: face, clothing, hair, background, light, composition. Cue 114621, 114625.
```prompt
ID: C11-pose
KIND: still
ENGINE: firefly
---
Change the mechanic's body pose: standing upright, both feet flat, holding the wrench in both hands at chest height. Keep face, clothing, light, background and framing as in the source.
```

**12 Clothing or prop swap.** Outfit from a second image onto the person in the first. Keep face, hair, pose, expression, background. Ask for folds and shadows to adapt. Cue 114625, 114629.
```prompt
ID: C12-clothes
KIND: still
ENGINE: firefly
---
Dress the mechanic from image one in the grey coverall from image two. Keep his face, hair, pose, expression and the garage as in image one, with natural fabric folds under the lamp.
```

**13 Face and hairstyle swap.** Face and hair from image two onto image one. Keep head angle, expression, pose, light, background. Cue 114629, 114631.
```prompt
ID: C13-face
KIND: still
ENGINE: firefly
---
Give the figure in image one the face and hairstyle from image two. Keep the head angle, expression, eye line, body, clothing and lighting from image one, with a matching skin tone.
```

**14 Head direction and eye gaze.** Only head turn and eye line. The book gives the head turn as an angle and the gaze as a target. Cue 114631, 114635.
```prompt
ID: C14-gaze
KIND: still
ENGINE: firefly
---
Turn the head about 30 degrees to the left and send the eye line to the roll-up door. Keep body, clothing, expression, background and framing as in the source.
```

**15 Facial expression change.** Only the expression. Keep pose, light, background, camera, identity. Cue 114635, 114638.
```prompt
ID: C15-expression
KIND: still
ENGINE: firefly
---
Change the expression to a quiet half smile with relaxed eyes. Keep pose, clothing, light, background, framing and identity as in the source.
```

**16 Body proportion correction.** A list of named parts to nudge (head, neck, shoulders, torso, arms, legs) with the pose, face, clothing, light, background kept. Cue 114638, 114641.
```prompt
ID: C16-proportion
KIND: still
ENGINE: firefly
---
Adjust the figure to natural adult proportions: slightly smaller head, longer torso, level shoulders, arms ending mid-thigh, knees aligned. Keep pose, face, clothing, light and background as in the source.
```

**17 Lighting and color grade transfer.** Light and grade from image two onto image one. Matched items: color temperature, shadow density, contrast, highlights, mood. Composition and objects stay. Cue 114641, 114645.
```prompt
ID: C17-transfer
KIND: still
ENGINE: firefly
---
Apply the light and color grade of image two, a warm low sun with deep shadows, onto image one. Keep every object, face and the layout of image one as it is.
```

**18 Lighting direction.** Relight: style, direction, shadow quality. Everything else stays. Cue 114645, 114648.
```prompt
ID: C18-relight
KIND: still
ENGINE: firefly
---
Relight the scene with soft window light from the upper left, long shadows falling to the right, gentle falloff. Keep subject, pose, background and framing as in the source.
```

**19 Time of day transformation.** Same place, other hour. Keep architecture, objects, perspective, composition. Cue 114648, 114651.
```prompt
ID: C19-time
KIND: still
ENGINE: firefly
---
Turn the garage from dusk to bright morning: pale sunlight through the door gap, cool air, short shadows. Keep every object, the layout and the camera view as in the source.
```

**20 Depth blur.** Subject stays sharp, midground and background fall off, like a fast 85mm lens. Cue 114651, 114653.
```prompt
ID: C20-blur
KIND: still
ENGINE: firefly
---
Add shallow depth of field: the mechanic sharp, the bench and door softly blurred, round soft highlights in the lamp. Keep framing, color and light as in the source.
```

**21 Perspective correction.** Straighten verticals, level the horizon, fix depth and scale, plant feet on the ground plane. Cue 114653, 114656.
```prompt
ID: C21-perspective
KIND: still
ENGINE: firefly
---
Straighten the vertical lines of the shelves and door frame, level the horizon, and seat both boots on the floor plane. Keep composition, light and objects as in the source.
```

Coverage check: all 21 are above (01 to 21, grouped by stage).

## 3. Prompt anatomy the book uses

Order, labeled sections (113913, 113921, 113927, 113937, 114142). Items 1 to 4 were on pages I did not get, so the first four come from the later "best practice" list (114142).

1. Task: what to create or edit (start with a verb: create, enhance, convert, transform, replace, 114656).
2. Subject: who or what.
3. Camera: framing, angle (the lens settings may sit here or on their own line).
4. Lens: focal length, aperture, and in the book's full example also a camera body, ISO and shutter speed (113937).
5. Lighting: direction, quality, time, color temperature, contrast (113913).
6. Background or environment: place, time of day, weather.
7. Style: realistic, cinematic, editorial, illustrative (113921).
8. Preserve: what must stay the same, strongest for edits (113921).
9. Output quality: resolution, color depth, sharpness, grain, "production-ready" (113921, 113927).

Rule of thumb from the author: say what to create before saying how it looks. Task and subject first, technical detail second (113937).

General practice list (114656): start with a verb, separate what changes from what stays, prefer plain sentences over comma-heavy keyword lists, put camera, light and quality after the main task, finish with a short render line. The stated reason: a multimodal model tells the required edit apart from the untouched parts better when they are separated.

Two ways the book builds a prompt: a labeled form (Task, Subject, Camera, and so on), and a plain-sentence form where the same parts are folded into two or three sentences. Both appear in the examples.

## 4. Vocabulary (terms only, from 114050 to 114356 and the glossary)

- Camera angle: eye level, low angle, high angle, bird's-eye, worm's-eye, Dutch angle, over-the-shoulder, point of view, top-down 90 degrees, front, back, side, three-quarter.
- Framing: extreme close-up, close-up, medium close-up, medium shot, medium long shot, full body, long shot, wide shot, extreme wide shot, group shot. Also establishing, master, hero, insert, reaction, coverage.
- Composition: rule of thirds, center, symmetrical, leading lines, diagonal, layered, negative space, balanced, dynamic, framing, blocking.
- Lens: 16mm ultra wide, 24mm wide, 35mm environmental portrait, 50mm natural, 85mm portrait, 135mm telephoto portrait, 200mm long telephoto; apertures f/1.2 to f/8; lens compression; bokeh; shallow, deep and selective focus; rack focus.
- Light direction: front, side, back, rim, top, bottom, upper left and right, left, right.
- Light quality: soft, hard, diffused, directional, volumetric, ambient, natural, studio.
- Light style: golden hour, blue hour, overcast, high key, low key, moody, Rembrandt, split, butterfly.
- Grading: neutral editorial, warm cinematic, cool cinematic, teal and orange, filmic, Kodak look, Fuji look, desaturated, high or low contrast, 10-bit color, HDR, dynamic range.
- Mood and character: determined, confident, suspicious, focused, calm determination; eye lines (left, right, up, down, into camera, at another character, at an object); head turns (three-quarter, profile, back).
- Place and weather: castle, village, city street, desert, beach, mountain, snow, interior room, palace, marketplace, battlefield; sunrise to midnight; sunny, cloudy, rain, fog, mist, storm, windy.
- Materials and quality words: photorealistic, ultra detailed, sharp focus, 4K, 8K, film grain, editorial photography, film still, premium render, production quality.
- Edit verbs: upscale, enhance, restore, face swap, clothing swap, prop swap, pose correction, expression change, relight, color grade transfer, depth blur, background replacement, object removal or addition, anatomy correction, texture enhancement.
- Preserve phrases (list of 17 kinds at 114138): facial identity, body proportions, composition, camera angle, lighting, background, environment, hairstyle, clothing, perspective, shadows, color palette, architecture, scale, materials, spatial relationships.

## 5. Pipelines and workflows, in the book's own order

**A. The recommended use order of the 21 categories (114042).** Environment first; alternate background views if needed; individual characters; multi-character scenes; storyboard sketches; final keyframes from storyboards; then edit passes (pose, light, face, costume, expression, perspective, enhancement). Reason given: visual continuity and consistent space across shots (114045).

**B. Eight-stage "idea to video" flow (114204 to 114227).**
1. Idea development: story, characters, setting, tone, visual style. Output: concept, mood board, genre, references.
2. Character design: appearance, age, body, clothing, hair, face, personality, expressions. Output: front, side, back, three-quarter views, character sheets, portraits, expression references.
3. Environment design: architecture, landscape, interiors, props, weather, time, light. Output: several views (front, back, top), a background library.
4. Storyboard creation: camera angle and movement, placement, blocking, composition, scene progression. Output: storyboards, shot plans, camera layouts.
5. Keyframe generation: combine character, place, light, camera, lens, composition, mood.
6. Image editing and refinement: the targeted edit prompts.
7. Shot continuity: check identity, costume, place, camera language, light direction, grade, scale, perspective, time of day.
8. AI video generation: use final keyframes as references; camera moves, character motion, environment motion, effects, transitions. Then edit, sound, music, dialogue, grade.
Principle: do not try to make a whole film with one prompt, build it one shot at a time (114227).

**C. The film-language chain (114425 to 114503).** Story idea, screenplay, storyboard, scene, shot, frame, keyframe, animation, editing, sound design, color grading, final film. Terms: scene = one place and time, several shots (114428 to 114432). Shot = one uninterrupted camera view (114432). Frame = one still, so 5 seconds at 24 fps is 120 frames (114437). Keyframe = the most important frame of a shot, defines composition, pose, light and camera, and the video tool uses it as guide (114437). Animation = generated motion between keyframes (114440, 114445).

**D. Pipeline lists (114456, 114459, 114822, 114824).** Same chain drawn as boxes, with a "pipeline" version adding: shot list, scene planning, visual effects, sound design, music. The closing chain: idea, script, storyboard, character design, environment design, keyframes, image editing, animation, editing, final film.

Note: pipeline B puts character and environment before storyboard. Pipeline C and D put screenplay and storyboard first. The book never reconciles them. Reading: storyboard the story first for beats, build the master characters and places, then storyboard again at shot level. UNTESTED reading.

## 6. Shot list method and storyboard method

Shot list (114425 to 114453, 114733):
- Start from a scene that lives in one place and time. Break it into shots, one camera view each.
- The worked example is a five-shot temple entrance: establishing shot of the building, wide shot of the hero arriving, medium shot on the stairs, close-up on the face, POV of the door opening. Each important moment gets its own keyframe (114453, 114456).
- Standard coverage kit (114733): establishing, wide, medium, close-up, over-the-shoulder, POV, reaction, insert. More coverage gives the editor more choice.
- Also generate a master shot (wide, whole scene, spatial anchor) and a hero shot (the most striking image, low angle and strong light as the example) (114727, 114730).
- Plan the shots on the 3 by 3 location sheet first, then pick (114613, 114724).
- A keyframe list for action: the beats that matter, for example prepare, strike, fall, victory (114440).

Storyboard method (114536, 114539, 114541, 114211):
1. Make the image you like (or a rough one).
2. Convert it into a black and white sketch (category 02): same angle, pose, framing; strip clothing, hair, accessories, texture, background; plain bald figures with face guides.
3. Lock that sketch as the layout reference, render it (category 03), changing only background, light, material, texture.
4. Storyboard fields to settle first: camera angle, camera movement, placement, blocking, composition, scene progression.
Why it works (my reading): the sketch removes everything the model can wander off on, so only layout is carried over. UNTESTED on Firefly.

## 7. Continuity method

From 114332, 114342, 114350, 114408, 114416, 114221, 114045.
- Character bible: name, age, height, body type, skin tone, eye color, hair color and style, facial hair, clothing, armor, accessories, preferred lens, light style, grade, reference images. The book's picture for it: an actor's continuity file.
- Character checklist: face, hair, body, costume, light direction and mood, lens focal length, seed (reuse where supported), same master reference images for every shot.
- Character loop: create, master portrait, full character sheet, save references, new scene, compare with master, correct differences, next scene. "Consistency is built through discipline" (114350).
- Environment checklist: architecture, layout, materials, vegetation, props, light and weather and time of day, lens, grade, master environment references.
- Environment loop: master environment, multiple views, environment bible, new scene, compare, correct. Treat each location as a permanent set (114416).
- Shot continuity pass before video: identity, costume, environment, camera language, light direction, grade, scale, perspective, time of day (114221).
- Same focal length across shots for matching perspective (114342, 114408).
- Same master references used for every shot (114342).

## 8. Anatomy and hands: what the book does, and why it says it fails

What I found in the 105 pages:
- The book never explains why anatomy or hands fail. No failure theory is on the pages I read.
- Hands are not mentioned anywhere in what I read.
- What it does about anatomy: asks for "realistic anatomy", "natural anatomy" and "accurate anatomy" in the style line; adds an anatomy fix line to the enhance template (114529); gives a whole category to proportion correction that names parts (head, neck, shoulders, torso, arms, legs) while keeping pose, face, clothing, light (114638); asks for natural neck anatomy on gaze edits (114631); asks for natural anatomy and balance on pose edits (114625); and uses the bald-mannequin storyboard so proportions are fixed in a sketch where nothing else can go wrong (114536).
- It lists "anatomy correction" in the edit keywords (114134).

What our evidence says: wrong tool in hand on garage clip 1, R17 in STANDARD.md (faces and hands in a start frame must be clean, fix the still). Our rule is stronger on hands than the book. PROPOSED reading of why hands fail (not from the book): hands are small, high-detail and change shape in every pose, so a model gets them wrong more often than a face; the repair is to fix the still with a narrow edit and check at full size. UNTESTED.

## 9. The tweak, do not change repair loop

The book does not have an explicit repair table. It has the pattern behind one: every edit category states one change, then a keep list, and the closing pages say to review, improve, experiment, repeat (114830). The table below is my synthesis from categories 11 to 21 and 16. Everything marked PROPOSED is mine.

| Symptom | Adjust only | Leave alone |
|---|---|---|
| Body pose wrong | the body pose (cat 11) | face, clothes, light, background, framing |
| Wrong costume or prop | outfit from a reference (cat 12) | face, hair, pose, expression, background |
| Face drifted from master | face and hair from master (cat 13) | head angle, expression, body, light |
| Looks at wrong thing | head turn and eye line (cat 14) | body, expression, clothes, framing |
| Wrong feeling on face | expression (cat 15) | pose, light, framing, identity |
| Odd proportions | named body parts (cat 16) | pose, face, clothes, light |
| Mood or grade off | light and grade from a reference (cat 17) | objects, faces, layout |
| Shadows from wrong side | light direction (cat 18) | subject, background, framing |
| Wrong hour | time of day (cat 19) | architecture, objects, view |
| Flat, subject lost | depth blur (cat 20) | framing, color, light |
| Leaning verticals, floating feet | perspective (cat 21) | composition, light, objects |
| Low detail, soft | upscale pass (cat 01), last | identity, pose, background |
| Hands wrong | PROPOSED: the hands only, keep pose and everything else | face, clothes, light, framing |
| Frame drifts from the master | PROPOSED: compare with the master, write the differences as the next prompt | everything that already matches |

Rules behind the table: one change per pass (SOURCED-book pattern in every template; the strict "one only" is also our R13). Order of passes: layout first, identity next, light, then enhance last (PROPOSED order, the book lists upscale first but its flow ends with polish).

## 10. Book versus STANDARD.md (R1 to R17)

Verdict labels: AGREES, ADDS, CONFLICTS. SILENT means the book says nothing, so no verdict is fair.

| Rule | Verdict | Note |
|---|---|---|
| R1 positive only | CONFLICTS | Book writes "do not change", "no people", "no plastic skin" (114532, 114553, 114601, 114606). Its "preserve X" lines are fine. Evidence side below. |
| R2 no shouting | SILENT | no capitals in the book |
| R3 engine template, 100 words | CONFLICTS | the book has one generic 9-part form and its examples run about 120 to 190 words (113937, 114532). Template idea ADDS labeled parts |
| R4 observable words | CONFLICTS | stacked quality words: "ultra-realistic, premium, production-ready" (113927). The verb-first plain sentence advice AGREES (114656) |
| R5 no contradictions | AGREES | separating change from keep lowers contradictions (114656) |
| R6 one body, one object, one action | AGREES | one shot at a time, no whole film in one prompt (114227). Category 5 allows three people in one still, a still is not a clip |
| R7 start frame holds geometry | AGREES | storyboard as layout, back and top views, composition from a reference (114539, 114601, 114619). ADDS the sketch as the layout carrier |
| R8 end frame | AGREES | interpolating between keyframes (114440, 114445). Book names no engine |
| R9 one camera sentence | AGREES | a full camera vocabulary and a camera line in every template |
| R10 audio | SILENT | image book |
| R11 timing | SILENT | only frame math, 5 s at 24 fps is 120 frames (114437) |
| R12 name each object, same wording | ADDS | character and environment bible with fixed fields (114332, 114416) |
| R13 one change per retry, redesign after three | CONFLICTS (mild) | the book says improve dozens of times (114813). Its edit passes still change one thing, which agrees. Redesign rule is ours |
| R14 no logos or text from the model | SILENT | |
| R15 give each reference a role | AGREES | image one is the base, image two is the outfit, face, light (114625, 114629, 114641). ADDS the numbered-image pattern |
| R16 draft cheap, final once | SILENT | |
| R17 clean faces and hands in start frame | AGREES for faces, SILENT on hands | ADDS fixing anatomy at the sketch stage and in a dedicated proportion pass |

Which side the evidence supports:
- Negation. Our evidence (R1: SOURCED from Google, Runway, Kling, Luma, Black Forest Labs pages; PROVEN on 5 video clips, F1) supports positive wording for video. For stills the picture is thinner: an Adobe Community reply (lesson 2026-11-22) says negatives get added to the image. Both point to our side. The book's negations are UNTESTED here, and book authors rarely test across engines. Side: ours, tagged SOURCED and PROVEN for video, UNTESTED for Firefly stills.
- Length. Garage 5 was 189 words and the best clip, so long is not proven bad (STANDARD R3 says so). Luma caps at 100 (SOURCED). Side: neither proven for stills, test.
- Camera body, ISO, shutter (113937). No maker page I have read says an image model reads these as settings. UNTESTED. Side: unproven, test cheaply.
- Quality stack (4K, HDR, 10-bit). In Firefly resolution is a panel setting. UNTESTED whether words change the picture.
- "Describe what you do not want": the book does the opposite of what Google's own page says (G1). Side: the makers.

## 11. Proposed additions to our standard (numbered)

Do not edit STANDARD.md. These are candidates. Tag is on each line.

1. B1. Run work in stages: place, extra views of the place, characters, group scenes, sketch, keyframes from the sketch, narrow edits, then video. SOURCED-book (114042, 114204 to 114227).
2. B2. Make one master reference per character and per location and reuse it as the reference for every later still. SOURCED-book (114342, 114350, 114408, 114416). Fits our R15.
3. B3. Write a bible per character and per location with fixed fields (face, hair, build, costume, lens, light, grade for people; architecture, layout, materials, props, light, lens, grade for places). SOURCED-book (114332, 114408). Fields are the book's, wording ours.
4. B4. Edit prompts have two lines: the one change, then a keep list written as "Keep X as in the source". Structure SOURCED-book (114621 and the other edit templates). Positive wording PROPOSED (our R1).
5. B5. One edit per pass. Pattern SOURCED-book (categories 11 to 21), strict rule PROPOSED (matches R13).
6. B6. For a shot where pose and framing matter, make the black and white sketch first and render from it. SOURCED-book (114536, 114539). UNTESTED on Firefly.
7. B7. Make the back view and the top view of a location from the master, and a 3 by 3 labeled sheet, before placing people. SOURCED-book (114601 to 114616). UNTESTED on Firefly.
8. B8. Keep the same focal length across the shots of one sequence. SOURCED-book (114342, 114408).
9. B9. Change time of day or light as a separate pass with architecture and objects kept. SOURCED-book (114645 to 114651).
10. B10. Run a nine-point continuity check before any frame becomes a video start frame: identity, costume, place, camera language, light direction, grade, scale, perspective, time of day. SOURCED-book (114221).
11. B11. Compare each new image against the master and write the differences as the next prompt, then change only those. SOURCED-book (114350 loop). Wording PROPOSED.
12. B12. Start every prompt with a verb and the task, then subject, then camera and light, then render. SOURCED-book (114656, 113937). Agrees with R3.
13. B13. Keep a personal prompt library sorted by category. SOURCED-book (114816). We already have LESSONS.md and the prompt log.
14. B14. Fix hands in a dedicated pass with the pose and face kept, and check at full size before the still becomes a start frame. PROPOSED (extends R17, the book is silent on hands).
15. B15. Fix proportions in the sketch stage before rendering. PROPOSED (book's bald figures give the idea, 114536, the rule is ours).
16. B16. Order of edit passes: layout, identity, light, grade, depth blur, polish last. PROPOSED (the book lists polish first in its library but ends its flow with refinement).
17. B17. Never paste long quality stacks or camera-body specs until a test shows they change a Firefly still. PROPOSED (tests in section 12).

## 12. Conflicts for Zac to test, one change per run

Rules for every run: same start image or same prompt except the one named change, record the settings line in `settings.txt` (model, tier, ratio, seed if shown, credit readout copied from the Generate button, Zac types it, no credit number from me). Three misses on a test means redesign the test.

| Id | Question | Run A | Run B (one change) | What to look at |
|---|---|---|---|---|
| T1 | Does "Keep X as in the source" beat "Do not change X" on a still edit? | edit prompt with positive keep line | same prompt, keep line replaced by a "Do not change" line | does the kept item survive, any new unwanted item |
| T2 | Do negation words get painted into a still? | positive prompt | same plus one "no people" phrase | people or text appearing |
| T3 | Do ISO and shutter lines do anything? | prompt with a lens and light line | same plus camera body, ISO, shutter line | look, blur, grain, any change |
| T4 | Does a quality stack change a Firefly still? | plain prompt | same plus "4K, HDR, 10-bit, premium" | sharpness, grain, nothing |
| T5 | Does a 9-part labeled form beat a two-sentence form? | labeled form | same content as sentences | which holds identity and layout |
| T6 | Does the storyboard-first step hold a pose better than a text prompt? | text prompt only | sketch reference then render | pose and framing match |
| T7 | Does a 3 by 3 sheet hold one location? | one sheet | nine separate prompts | does the room stay the same |
| T8 | Does the "reverse view" prompt give a true opposite wall? | back view from master | same with the camera position written differently | architecture kept |
| T9 | Does "change only the pose" hold the face and clothes on Firefly? | pose edit | same with the keep list removed | face and clothes drift |
| T10 | Does a proportion pass fix a bad figure without moving the pose? | proportion edit | n/a (compare before and after) | pose, face kept |
| T11 | Does a hands-only edit work? | hands-only edit | same with a second reference of a clean hand | hand shape |
| T12 | Improve dozens of times versus redesign after three | follow our R13 on one shot | n/a, count tries | which shot gets a keeper in fewer tries (long test, low priority) |

Which engines the book assumes: a generic multimodal image model that takes several input images. Whether the Firefly Image menu on Zac's account has a model that takes numbered input images and edit instructions: panel check, UNTESTED.

## 13. Lint and slop results

- prompt_lint.py on this file, 21 example blocks: first run 20 PASS, 1 FAIL (C17, the word "mood" breaks R4). Fixed to "color grade", rerun: 21 of 21 PASS, no WARN, no FAIL.
- slop_check.py: clean, exit 0 (mechanical pass only). No em dashes.
