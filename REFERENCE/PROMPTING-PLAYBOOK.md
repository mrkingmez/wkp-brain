# PROMPTING PLAYBOOK (general, any venture, any engine)

Written 2026-11-24 by graphic-design on Zac's order: the prompt-book method must help every venture, not one trailer. Owner: graphic-design (keeps it current). Parent of `D:\WKP\data\firefly-prompt-guide\STANDARD.md`, which is the Firefly and video-model child with the engine templates and rules R1 to R17.

Read this when you plan, write or order any generated image, video, audio or 3D asset, for any project: AI film or series, a show intro, a trailer, an ad, product art, a cover support piece, a thumbnail for a non-WWD channel, an animation. Read STANDARD.md next if the engine is Firefly, Veo, Kling, Seedance, Runway, Luma or Flux. Read `LESSONS.md` in the same folder before the first prompt.

## Tags used here
| Tag | Meaning |
|---|---|
| SOURCED-book | The C.N. Scott Keyframe Prompt Library says it (notes: `D:\WKP\data\firefly-prompt-guide\BOOK-NOTES-CN-SCOTT-2026-11-24.md`). A claim to check, not an order. |
| PROVEN | Seen on Zac's own clips or stills, with a count (`LESSONS.md`, `firefly-prompt-log`). |
| PROPOSED | Our rule, written but not yet run. A try, not a law. |
| UNTESTED | Idea or maker claim not yet run on Zac's account. |

Conflict rule: where the book disagrees with a PROVEN rule in STANDARD.md, the proven rule wins. Known conflicts are marked "OURS WINS" below. Nothing in this file is copied from the book. It is our own words.

Hard limits, every project: no credits spent and nothing posted without Zac's yes. Never state a credit number you did not read at the Generate button. Text, logos, plates and numerals are never made by a model (R14), they go on in code, Photoshop or Premiere.

---

## A. The staged pipeline

One shot at a time. Never ask one prompt for a whole film or a whole scene sequence. SOURCED-book, and it matches our R6 (one body, one object, one action).

| Stage | What you make | Why it comes here | Tag |
|---|---|---|---|
| 0. Kickoff | Decisions from section E, bible started | Everything later copies from it | PROPOSED |
| 1. Places | One master still per location, no people | The set must exist before anyone stands in it | SOURCED-book |
| 2. Extra views | Back view, plan (top) view, a 3 by 3 sheet of camera positions of each place | Gives the place a second side and a coverage map | SOURCED-book, UNTESTED on Firefly |
| 3. Characters | One master portrait, then one full-body sheet, per person | Identity is fixed here and copied after | SOURCED-book |
| 4. Group scenes | Two or three people with correct scale and contact | Only after each person and the place are locked | SOURCED-book |
| 5. Sketch or storyboard | Plain black and white layout of the shot | Locks pose and framing before style can wander | SOURCED-book, UNTESTED on Firefly |
| 6. Keyframes | Render the sketch with the masters as references | The picture the video starts from | SOURCED-book |
| 7. Narrow edit passes | One change per pass (section C) | Fixes without rolling the dice on the whole picture | SOURCED-book pattern |
| 8. Continuity check | The nine-point check (section D) on every frame | Catches drift before it costs a video run | SOURCED-book |
| 9. Video or motion | Start frame (and end frame where the engine takes one), motion-only prompt | Per STANDARD.md R7, R8 | PROVEN (start frame), end frame UNTESTED |
| 10. Sound and finish | Audio, music, text overlays, grade | Text and logos never from a model | PROVEN (R14) |

Reading of the book's two orders (it never reconciles them): storyboard the story for beats first, build masters, then storyboard again at shot level. UNTESTED.

Skip stages, do not reorder them. A thumbnail or a product shot may only need stage 1 or 3, then 6 and 7. A film needs all of them. Write down which stages the project uses in the kickoff checklist.

Which department does which stage (all orders go through the normal chain):
| Stage | Owner |
|---|---|
| 0, 1 to 8 stills | graphic-design (writes the prompts, Zac clicks Generate) |
| Sketch and shot list text | script-room writes the beats, graphic-design turns them into frames |
| 9 video | graphic-design writes the prompt and settings, point man for the project (assistant-editor, documentary-editor, wwd-vfx, marketing-director) orders it |
| 10 sound | sound-designer, music |
| 3D equivalents | animation-director (its own standard, `ANIMATION\STANDARDS.md`) |

---

## B. Master references and the bible

### B1. Masters
One master image per character and one per place. Every later still uses it as a reference with a named role ("image one is the person, image two is the room"). SOURCED-book, fits R15. Keep masters in the project folder under `01-masters\`, never overwritten. A new master gets a new version number.

A master must pass the full-size check before it is called a master: face clean, hands clean, no stray text, no extra objects. A bad master poisons every shot that copies it. PROPOSED.

### B2. Bible template (copy this block into `00-bible.md` for each project)
Fields come from the book, wording is ours. Write each field once, in visible words, and paste the same words into every prompt (R12). Positive wording only.

```
PROJECT BIBLE
Project / working title:
Medium and end use (film, trailer, intro, ad, cover support, product art):
Aspect ratio and delivery size:
Look in one line (what a stranger would see, no brand names of artists):
Color grade (two or three colors, contrast, warm or cool):
Lens habit (one focal length used for the whole sequence):
Time of day and weather per sequence:
Things the project must show (flag, logo, product shape):
Things only Zac or the client decides:

PEOPLE (one block each)
Name or role:
Age and build:
Face (shape, skin tone, eye color, facial hair):
Hair (color, length, style):
Costume (each piece, color, material):
Accessories and props carried:
Posture and walk in a word or two:
Preferred lens and light for this person:
Master file name:
Voice and sound notes (if audio):

PLACES (one block each)
Name:
Architecture and layout (left, right, front, back named from the camera):
Materials and surfaces:
Fixed props and where they sit:
Light sources and their direction:
Time of day, weather:
Lens and grade for this place:
Master file name and extra views made (back, plan, 3 by 3):

PROPS (one block each)
Name:
Shape and color in visible words (the exact words used in every prompt):
Size against a person (hand, forearm, waist):
Where it lives in the shot (which hand, which shelf):
Is a logo or text on it? (composite it in code or Photoshop, never prompt it)
Master file name:

STYLE RULES
Words we always use:
Words we never use (and why, from LESSONS.md):
Reference images and their roles:
```

### B3. Same lens, same grade
Keep one focal length and one grade across the shots of a sequence so the cuts match. SOURCED-book. Our still model may not read focal lengths as settings, so treat the lens line as a try. UNTESTED (book test T3, T4).

### B4. Quality stacks
Do not paste long quality lists ("4K, HDR, 10-bit, premium") or camera-body, ISO and shutter lines until a test shows they change a Firefly still. PROPOSED. OURS WINS over the book, which uses them. Resolution is a panel setting.

---

## C. Edit prompts and the repair loop

### C1. The two-line edit prompt
Line 1 names the one change. Line 2 names what stays, written positively. Structure SOURCED-book, wording PROPOSED.

```prompt
ID: PB-edit-pose
KIND: still
ENGINE: firefly
---
Change the man's body pose to standing upright with both feet flat, holding the wrench in both hands at chest height. Keep his face, clothing, the work lamp light, the garage background and the framing as in the source.
```

Template:
1. Change: [one thing, with the end state described as a picture].
2. Keep: [list, each with "as in the source"].

Rules:
- One change per pass (R13, B5). Two changes means two passes.
- Do not write "do not change X". Write "keep X as in the source". OURS WINS over the book (R1, SOURCED from Google, Runway, Kling, Luma and Black Forest Labs pages, PROVEN on 5 video clips). For Firefly stills the negation question is UNTESTED here, so book test T1 settles it before this becomes a still rule.
- Never name the unwanted thing. Describe the wanted picture.
- Order of passes (PROPOSED): layout and pose, identity, costume, light, time of day, grade, depth blur, polish last.

### C2. Repair loop
1. Compare the new image with its master (or with the sketch). Write down the differences as plain statements.
2. Pick the single worst difference.
3. Write the two-line edit for that one thing.
4. Run it. Record the try (section F).
5. Repeat from 1. After three failed tries on one shot, redesign the shot (new camera, new sketch, a cut, another engine), do not write a stronger sentence (R13, PROVEN F18).

Compare-and-correct loop: SOURCED-book. Wording PROPOSED.

### C3. Symptom to fix table
Column "Whose" says where the fix comes from. OURS means our own evidence, BOOK means the book's pattern, BOTH means each agrees.

| Symptom | Fix, one pass | Keep list | Whose | Tag |
|---|---|---|---|---|
| Hands wrong (extra finger, wrong tool, fused) | A hands-only edit: describe the hand shape and what it holds as a picture. Check at full size. If it fails twice, change the pose so the hands are hidden or small, or composite a clean hand | face, pose, clothes, light, framing | OURS (garage clip 1, R17). The book never mentions hands | PROPOSED, hands-only edit UNTESTED (book test T11) |
| Identity drift (face changed from master) | Edit the face and hair using the master as reference with a named role | head angle, expression, body, clothing, light | BOOK pattern | SOURCED-book, UNTESTED on Firefly (T9) |
| Wrong side or wrong hand (left and right swapped) | Fix the still, not the words. Put the geometry in the start frame. Name the side camera-relative ("the hand nearest the camera") | everything else | OURS | PROVEN (R7, F5, F11, 3 clips) |
| Wrong costume or prop | Swap from a reference image with a role | face, hair, pose, background | BOOK | SOURCED-book |
| Scale off (giant hand, tiny door) | Name the size against a person in the bible and in the prompt ("the wrench is as long as his forearm"). Use the plan view to check. Last resort, a proportion pass naming the parts | pose, face, clothing, light | BOTH | PROPOSED, proportion pass UNTESTED (T10) |
| Light from the wrong side or wrong time | A relight or time-of-day pass: say the light direction and hour as a picture | objects, layout, camera view, subject | BOOK | SOURCED-book, UNTESTED |
| Grade or mood off | Match the grade of a reference image, as its own pass | objects, faces, layout | BOOK | SOURCED-book |
| Text, logo, plate or numerals wrong | Do not retry. Remove from the prompt and composite later (R14) | everything | OURS | PROVEN (F3, 2 of 2) |
| Extra object or person appears | Remove the cause from the whole prompt, including every "no" and "without" (R5). Then rerun | n/a | OURS | PROVEN (garage 7, 8) |
| Objects vanish, duplicate or morph in a video | The shot has two bodies or a handoff. Split into two clips and a cut (R6) | n/a | OURS | PROVEN 6 of 6 |
| Camera re-frames or door moves by itself | Add one camera sentence that fits the move, or cut (R9) | n/a | OURS | PROVEN (F11) |
| Leaning verticals, feet not on floor | A perspective pass: straighten verticals, plant boots on the floor plane | composition, light, objects | BOOK | SOURCED-book, UNTESTED |
| Flat, subject lost in background | A depth-blur pass | framing, color, light | BOOK | SOURCED-book, UNTESTED |
| Soft, low detail | Polish pass last | identity, pose, background | BOOK | SOURCED-book |
| Frame drifts in video (look changes mid-clip) | Shorter clip, start frame plus end frame, state what stays constant in one positive sentence | n/a | BOTH | SOURCED (maker pages), end frame UNTESTED |

---

## D. Shot list, storyboard and continuity

### D1. Shot list method
1. Break the story into scenes. A scene is one place and one stretch of time.
2. Break each scene into shots. A shot is one uninterrupted camera view.
3. Give each shot a row (table below). One body, one object, one action per row (R6).
4. Mark the keyframe for each shot, the one image that sets pose, light and camera.
5. Plan coverage: establishing, wide, medium, close-up, over the shoulder, point of view, reaction, insert. A master (wide, whole scene) and a hero (the most striking angle) per scene. SOURCED-book.
6. Choose camera positions from the place's 3 by 3 sheet if one exists.

Shot list table (copy):

| Shot id | Scene | Place master | People masters | Camera (shot size, angle, move) | Lens | Action in one sentence | Start frame file | End frame file (if needed) | Length | Audio | Engine |
|---|---|---|---|---|---|---|---|---|---|---|---|

Hand this to script-room for the beats and to graphic-design for the frames. script-room writes the words, graphic-design writes the generation prompts. Neither rewrites the other's part.

### D2. Storyboard method
1. Make or pick an image you like for the shot (rough is fine).
2. Turn it into a plain black and white sketch: same camera angle, pose and framing, no costume, no texture, no background detail, simple mannequin figures with face guides.
3. Lock the sketch as the layout reference and render it, changing only background, light, material and texture.
4. Fix proportions in the sketch, not after rendering. PROPOSED.
Why it should work: the sketch strips away everything the model can wander off on. SOURCED-book, UNTESTED on Firefly (book test T6).
Free Blender version of the sketch stage (added 2026-11-24): `D:\WKP\ANIMATION\previs\` (how-to `HOWTO.md`, one-page `CHECKLIST.md`). A shot card in, gray stand-in figures with a blue LEFT and red RIGHT hand out, plus a plan view, a 3 by 3 camera sheet and a report of numbers read from the scene (hand visible percent, which side of frame, lens, camera height). Layout only, never look. Ask animation-director to run it; no credits.

Storyboard fields to settle first: camera angle, camera move, who stands where, composition, what happens before and after.

### D3. Continuity checks
Same masters in every shot. Same lens and grade across a sequence. Compare each new frame to its master (section C2).

**The nine-point start-frame check.** Run it, one line each, before any frame becomes a video start frame. SOURCED-book, wording ours.

| # | Check | Pass looks like |
|---|---|---|
| 1 | Identity | Face, age and build match the master |
| 2 | Costume | Every garment and accessory matches the bible |
| 3 | Place | Layout, props and materials match the place master |
| 4 | Camera language | Shot size, angle and lens habit match the shot list and neighbors |
| 5 | Light direction | Shadows fall the same way as the shot before and after |
| 6 | Grade | Color and contrast match the sequence |
| 7 | Scale | People and objects have believable size against each other |
| 8 | Perspective | Verticals straight, horizon level, feet on the floor |
| 9 | Time of day | Sky, light color and shadows fit the hour |

Add three of our own (PROPOSED, from our failures): 10. hands and face clean at full size (R17), 11. no text, logo or plate in the picture unless it will be replaced (R14), 12. the geometry the video needs (which hand, which side) is visible in the frame (R7).

Record pass or fail for each point in the project log. A fail goes back through section C before video. A frame that fails points 1 to 3 never becomes a start frame.

---

## E. Project kickoff checklist (any director can run it)

Run before the first generation of any project. Answer every line in writing. Unknown answers are written NOT DECIDED with who decides.

| # | Question | Where the answer goes |
|---|---|---|
| 1 | What is the end use, where does it appear, and in what size and ratio? (platform spec with its source) | bible |
| 2 | Who orders it, who approves it, who is the point man agent? | project log |
| 3 | Locks and house rules that apply: flag and people on patriotic work, tone, no actor tags, AI disclosure on shop images, `REFERENCE\LOCKS.md` | bible |
| 4 | Which stages from section A does this project use? | project log |
| 5 | Which engines, and what does each take (start frame, end frame, references, seed, audio)? Mark every panel fact "Zac checks at the panel" until he has seen it | project log |
| 6 | Look, grade, lens habit in one line each | bible |
| 7 | People, places, props: how many, each with a bible block | bible |
| 8 | Is anything text, a logo, a plate or a number? Plan the code or Photoshop route now (R14) | bible |
| 9 | Licensing: can every generated or reference asset be used commercially? Real people, real brands, real units are excluded. License note per asset | project log |
| 10 | Credits: which tier, which resolution for drafts and for finals? Zac reads the credit number at the button. No number is ever estimated by an agent. Money needs Zac's yes | project log |
| 11 | Shot count and plan: one pass of the shot list, with the cheapest route first (draft low resolution, final once) | shot list |
| 12 | Where do the files live (section F), who updates the log, who runs the nine-point check? | project log |
| 13 | Review chain: department boss approves, the ordering director accepts, qa-director checks, Zac decides | project log |
| 14 | What is the redesign trigger? Default: three failed tries on one shot | project log |
| 15 | Public copy or posting involved? Writing room, marketing, no-ai-slop gates. Nothing posts without Zac | project log |
| 16 | Disclosure: label AI-made art where required (Etsy shops, YouTube AI box, listing notes) | project log |

---

## F. Project folder layout and the generation log

### F1. Folder layout
Raw outputs live where `SOP\SOP-Output-Locations-and-Formats.md` says. Prompt logs live in `D:\WKP\data\firefly-prompt-log\<project>\`. Use this shape for each project (PROPOSED):

```
<project>\
  00-bible.md              bible and kickoff answers
  01-masters\              locked references, versioned names (char-<name>-v1.png, place-<name>-v1.png)
  02-sketches\             storyboards and layout sketches
  03-keyframes\            rendered stills, one folder per shot id
  04-edits\                narrow-pass results, named <shot>-<pass>-<try>.png
  05-video\                clips, one folder per shot id
  06-sound\                cue sheet, music notes
  shotlist.md              the table from D1
  log.md                   one row per try (below)
  settings\                settings.txt per try, from SETTINGS-TEMPLATE.txt
```
Never overwrite a master or a kept result. New try, new filename.

### F2. Log format (one row per try, in `log.md`)

| Date | Shot id | Stage | Engine and tier | Prompt (file name or text) | Settings (ratio, resolution, fps, length, audio, seed) | Inputs (start frame, end frame, references and roles) | Credit readout (copied by Zac, else NOT SHOWN) | Result (kept, failed) | Failure code | Nine-point result | One change from the last try | Lesson |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Rules:
- Record failures. A failure row costs nothing and saves the next project.
- After Zac reports any result, add a row to `D:\WKP\data\firefly-prompt-guide\LESSONS.md` the same turn.
- A lesson seen three times is promoted into STANDARD.md or this playbook. A lesson that contradicts an UNTESTED tip strikes that tip.
- Seed: write it when the panel shows it. Same seed across tiers is UNTESTED.

---

## G. Testing a book idea on our account before it becomes a rule

A book idea, a YouTube tip, a maker blog line or a community post is a claim. It starts as UNTESTED and moves like this.

1. State the claim and the question in one sentence (book tests T1 to T12 already exist in the notes file).
2. Write run A and run B. They are identical except for one change. Same engine, tier, ratio, start image, references.
3. Zac runs both and copies the settings line and credit readout. The agent never states a credit number it did not retrieve. A draft tier and a low resolution come first (R16).
4. Zac hands back the results. The agent logs both runs the same turn (section F).
5. Judge on a short stated list (what must survive, what must not appear). Name the winner or call it a tie.
6. Tag the idea:
   - One clear win, once: PROVEN 1. Use it, still marked as seen once.
   - Same result three times: PROVEN, promote to STANDARD.md or this playbook.
   - It loses or ties: strike it and record why.
7. Stop after three failed tries on one test and redesign the test.

Never change two things in one run. Never promote an idea on a single lucky result. A rule that conflicts with a PROVEN rule needs a test where the PROVEN rule is run B.

Free test before any credit test (added 2026-11-24): run the shot through the Blender previs (`ANIMATION\previs\HOWTO.md`) and clear its checklist first, so a failed generation is never a layout mistake you could have caught for free. Using a previs as the T6 sketch reference is UNTESTED on our account.

Free pre-flight before any run (added 2026-11-24): `python D:\WKP\software\prompt-preflight\preflight.py <file or --text "..."> --kind still|video|edit --engine <name>` flags known failure words from our own logs (rule table `D:\WKP\software\prompt-preflight\RULE-TABLE.md`, how-to `README.md`). It reads words only and cannot predict what an engine draws, so a clean result is not a test result. The A/B runs above are still how an idea is proven.

Priority tests for any new project (from the book notes): T1 keep-line versus do-not-change, T3 and T4 camera and quality stacks, T6 sketch first, T9 pose edit holds the face, T11 hands-only edit. Cheapest first.

---

## Where this plugs in

| Who | Use |
|---|---|
| graphic-design | Owns this file. Sections A to G for every still and video prompt |
| wwd-vfx, assistant-editor, documentary-editor, studio-director | Section E before ordering generation, D for shot lists, F for logs |
| script-room | Hand beats and shot lists in the D1 table. Never rewrites generation prompts |
| marketing-director, video-ugc, etsy-director, kdp-director, fiction-director (covers only), wkp-channel-director | Section E kickoff for any art order, tag results per G |
| vfx-compositor, motion-graphics, sound-designer, music | Section D3 and F for inputs to their work. Text, logos and numerals are theirs (R14) |
| animation-director | Same stages for 3D (masters become reference sheets). Its own standard still governs |
| Everyone | Zac clicks Generate. No credits, no posting, no spending without his yes |

Firefly and video engine details: `D:\WKP\data\firefly-prompt-guide\STANDARD.md`. Book notes: `D:\WKP\data\firefly-prompt-guide\BOOK-NOTES-CN-SCOTT-2026-11-24.md`. Lessons: `D:\WKP\data\firefly-prompt-guide\LESSONS.md`.
