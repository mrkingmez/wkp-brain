# Previs method: how to use it (agents and Zac)

Created 2026-11-24. Free, runs on this PC in headless Blender, no credits, no network, no Adobe. It is the Blender version of the playbook's plain bald-figure sketch stage (`REFERENCE\PROMPTING-PLAYBOOK.md` D2 and the book notes).

**What it fixes:** layout. Who stands where, which way they face, which hand holds which prop, how big things are against each other, where the camera is, which lens, what the camera can and cannot see.
**What it does NOT fix:** look. No costume, face, skin, light mood, color, texture, lens character or style. The render is gray on purpose. Do not judge look from it and do not expect an image engine to copy it exactly.

## Folder layout (`D:\WKP\ANIMATION\previs\`)

| Item | What it is |
|---|---|
| `previs.py` | The one command you run. Builds the scene, renders, checks the card, writes the report. |
| `previs_lib.py` | The reusable parts: gray figure (head, nose wedge, torso, limbs, hands, feet), props with grip points, location blocks, 1 m ground grid, light marker, camera rig. |
| `build_shot.py` | Runs inside Blender. Reads the card, measures the scene, renders. Do not run it by hand. |
| `gen_lens_sheet.py` and `lens_cheatsheet.md` | Lens table computed from the sensor maths. The same text is stored in every saved .blend as the text block `PV_LensCheatSheet`. |
| `cards\` | Shot cards (JSON). `_card-template.json` is the blank to copy. Proof cards for the Ian garage hand-off and a WWD cold open frame are here too. |
| `renders\<card id>\` | Output per card: `shot_captioned.png`, `plan_captioned.png`, `sheet_3x3.png`, `REPORT.md`, `report.json`, and the built `.blend`. |
| `D:\Blender Projects\Previs Template v1.blend` | The template scene (two stand-ins, prop, room blocks, ground, light marker, camera rig with lens, plan camera, nine sheet cameras, cheat sheet text). Versioned: never overwrite, a new one is v2. |
| `CHECKLIST.md` | One page. What to confirm before a previs is used as a structure reference. |

## The conventions (they are printed on every render)

- 1 Blender unit is 1 metre. Ground grid lines are 1 m apart.
- +Y is away from the front camera, +X is to the right of it. Compass facing: 0 faces +Y, 90 faces +X, 180 faces -Y, 270 faces -X.
- **BLUE hand = the character's own LEFT. RED hand = the character's own RIGHT.** These are the character's hands, not the screen's. The report also says which side of the screen each hand lands on.
- The dark wedge on the head is the nose. It shows where the face points.
- Yellow arrow is the light: it sits on the side the light comes from and points the way it travels. Shadows in the render follow it.

## Run it

1. Copy `cards\_card-template.json` to `cards\<project>-<shot>-v1.json`.
2. Fill it in (fields below). One body, one object, one action (playbook R6).
3. Run (normal Python, not Blender):
   `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe D:\WKP\ANIMATION\previs\previs.py D:\WKP\ANIMATION\previs\cards\<card>.json --plan --sheet`
   Options: `--plan` adds the top-down view, `--sheet` adds the 3 by 3 camera sheet (low, eye, high by three azimuths, the shot camera is the middle tile), `--guides` draws thirds lines, `--out DIR` changes the output folder.
4. Open `REPORT.md`. Read the PASS and FAIL lines and the warnings, then open the images.
5. Fix the card (never the render) and rerun. Keep the failed run: rename its report and shot with `first-pass` so the lesson stays visible.
6. A run takes about 20 to 40 seconds with all three outputs.

## Card fields

- `ratio` `16:9`, `9:16`, `1:1`, `4:5`, `4:3`, `2.39:1`; `res_long` pixels on the long side.
- `location`: `size` [w,d,h], `center`, `walls` (any of back, front, left, right, ceiling), `blocks` (name, loc, size, rot_z_deg, on_ground).
- `props`: name, type (box, cylinder, sphere), size, loc (centre), optional `tilt_deg` [rx,ry,rz], `grips` (named points in the prop's own space, e.g. `top`, `shaft`), optional `end_marker`.
- `characters`: name, `height` (m), `build` (lean, average, stocky), `pos` [x,y], `facing_deg` or `facing_to` (another character or a point), `pose` stand or sit (`seat_height`), `look_at`, `left_hand` and `right_hand`. A hand is one of `{"holds": {"prop": "wrench", "at": "top"}}`, `{"reach": [x,y,z]}`, `{"on": [x,y,z]}`, or empty for relaxed. A hand that cannot reach is drawn straight and reported with the shortfall in metres.
- `light`: `azimuth_deg` (compass the light comes FROM) and `elevation_deg`.
- `camera`: `azimuth_deg` (0 = stand on the -Y side, +90 = on the +X side), `distance`, `height`, `target` ([x,y,z], a character name, or `centroid`), `lens_mm`; or give `loc` directly.
- `expect`: the claims you want checked, each with a `note` in plain words. Keys: `char` plus `hand` (`holds`, `visible_min`, `visible_max`, `screen_side`, `over_face`, `in_frame`) or `char` alone (`head_in_frame`, `feet_in_frame`, `facing_dot_min`, `body_pct_min`).

## What the report reads from the scene

Camera height, lens, field of view; per character the distance, the side we see (front, back, side), whether head and feet are in frame; per hand the screen side, the percent visible, what hides it, what it holds, any reach shortfall, and whether it is drawn over the face; the closest hand to hand distances. Visibility is by ray casting from the camera to nine points on each hand, so it is a number, not a guess.

## How it feeds the generation work

1. Run the previs before the first credit is spent, at the sketch stage in playbook section A and D2.
2. Use `shot_captioned.png` as the layout reference (the sketch image in `02-sketches\`), and `REPORT.md` for the words: write the camera side and the hand in plain words in the prompt ("his right hand, the hand nearest the camera") using the report, not memory.
3. Use `plan_captioned.png` to settle who is left and right of whom across a sequence (continuity point 3, 4 and 7 in the nine-point check).
4. Log the previs files in the project log, and after the engine run compare the frame against the previs with the checklist.

UNTESTED: whether Firefly, Veo or any engine holds a gray previs as a structure reference. The playbook marks the sketch method UNTESTED on Firefly (book test T6). Run T6 with a previs as the sketch when Zac has a sitting.

## Limits to know

- Stand-in figures are blocks and tubes. They show layout, not anatomy. Do not read fingers, faces or clothing from them.
- Hands are one block each. A grip is a point, not a finger pose.
- No physics or collision between bodies and props. Two arms can pass through a torso. The visibility check will show it as an occluder, so read the "hidden by" names.
- Legs and arms are solved with simple two-bone maths, so poses are approximate. A seated pose is one fixed shape.
- Editing the saved .blend in the GUI moves parts but does not re-solve the arms. The method is: change the card, rerun.
- Blender MCP and `look` were not available on 2026-11-24 (connection refused, addon outdated). Everything ran headless on scratch data. When the MCP is up, `look` can be used on the saved .blend, but never save over Zac's open scene.
