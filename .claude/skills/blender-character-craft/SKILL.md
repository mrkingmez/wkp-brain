---
name: blender-character-craft
description: How to build good characters and creatures in Blender for Zac's Animation department. Use for any request to model, block out, sculpt, retopologize, rig, weight paint, pose, add fur or hair, or fit armor and props on a character, wolf, creature, anthropomorphic or humanoid figure, or to work from a reference image, or to decide between code-driven modeling and an AI image-to-3D service. Includes the Skin modifier plus Subdivision method used on the Wolf Warrior test, its limits, a candid list of what code-driven modeling cannot do, and the free-only rule for AI generators.
---

# Blender character craft

Verified live against Blender 5.2.4 where marked (VERIFIED). Everything else is community practice and marked UNVERIFIED where I could not check it. Sources in references.md. Finish every character with `blender-asset-quality` and drive Blender with `blender-mcp-ops`.

## 0. Honest capability statement (read first)

Code-driven modeling (bpy primitives, Skin modifier, booleans, metaballs, curves) produces blockouts, stylised low-detail figures, props, armor plates and rigid parts well. It does not produce:
- A face that reads as a face. Eyes, brow, muzzle, lips, ears with believable form.
- Hands with correct finger proportions and flesh.
- Muscle definition, fur clumps, skin folds, believable anatomy transitions.
- Clean organic edge flow on its own. Skin modifier output is evenly dense and quad-ish, not deformation-ready around joints.
- Anything a sculptor does by feel.

Rule: if the shot shows the character within about 3 m of the camera, or the face is on screen, a code-built mesh will look amateur. Say so in the report instead of polishing it endlessly. Options in order:
1. Source an existing rigged model (see `blender-asset-sourcing`), free and properly licensed.
2. AI image-to-3D service via the blender MCP `generate_3d` (section 11). FREE ONLY. Ask Zac first before any credit is spent.
3. Hand sculpt (needs Zac or a human sculptor; the agent can only do rough sculpt via bpy sculpt operators, UNVERIFIED quality).
4. Keep the code-built blockout and present it honestly as a stylised or distant-shot asset.

## 1. Start from a reference image

1. Get a front and side (and ideally 3/4) orthographic reference. If only one concept image exists, generate or request a turnaround before modeling. Do not invent proportions.
2. Put references in a `_REF` collection as Empty > Image objects (`bpy.data.objects.new("REF_Front", None)`, `empty_display_type='IMAGE'`, `data` = image), front on the XZ plane facing -Y, side on the YZ plane. Set `empty_display_size` so the figure height in the reference equals the real target height.
3. Lock the ref objects (`hide_select=True`) and put them at 30 to 50 percent opacity (`color` alpha, `show_in_front=False`).
4. Decide the real height in metres before modeling: human 1.75 to 1.85, wolf standing at shoulder 0.75, wolf nose-to-tail 1.5 to 2.0, giant 3+. The head count method for humanoids: 7.5 heads for a realistic adult, 8 for heroic, 6 for stocky or stylised.
5. Silhouette first: block out in plain solid colour, check the black silhouette with `look` (solid, flat lighting, or a black emission material) from front, side and 3/4. If the silhouette is not recognisable at 64 px, the details will not save it.

## 2. Blockout

- Use simple volumes (cubes, cylinders, UV spheres) for head, chest, pelvis, limb segments, hands, feet. One object per mass, named (`BLK_Head`, `BLK_Chest`).
- Big forms first: ribcage and pelvis angle, shoulders, head size relative to the body, limb length ratios. Compare against the reference overlay at every step.
- Proportion check numbers (humanoid, 8 heads): shoulders 2 heads wide, elbows at waist, wrists at crotch, knees halfway between hip and floor, hand length equals face length.
- Fix proportions in the blockout. They cannot be repaired after the sculpt.

## 3. Skin modifier plus Subdivision (what the Wolf Warrior test used)

Live-confirmed in 5.2.4 (VERIFIED): `SKIN` modifier exists with props `branch_smoothing`, `use_smooth_shade`, `use_x_symmetry`, `use_y_symmetry`, `use_z_symmetry`. Per-vertex data lives at `mesh.skin_vertices[0].data[i]` with `radius` (2 floats: x, y), `use_root`, `use_loose`. Operators `object.skin_root_mark` and `object.skin_armature_create` exist. A 3-vertex line with Skin plus Subdivision level 2 evaluated to 416 faces.

How it works: build a wire skeleton of vertices and edges (a stick figure), the modifier inflates it into a quad mesh with a per-vertex radius. Subdivision Surface smooths it. The Blender manual puts an Armature modifier directly below Skin so it only deforms (source via search snippet).

Workflow:
1. Create a mesh of vertices and edges only: `me.from_pydata(verts, edges, [])`. Spine, neck, head, shoulder-arm chains, legs, tail, ears. Real-world metres.
2. Add modifiers in this order: `SKIN`, `SUBSURF` (viewport 1, render 2), optional Mirror above Skin (`use_x_symmetry` on the Skin modifier is the simpler route).
3. Set radius per vertex: `me.skin_vertices[0].data[i].radius = (rx, ry)`. Torso radii larger than limbs, wrists and ankles smallest.
4. Exactly one root per connected piece (`use_root = True` on the pelvis or chest vertex). Mark `use_loose` on branch vertices that make ugly pinching at shoulders and hips.
5. `branch_smoothing` 0.5 to 1.0 smooths the joint junctions.
6. Add details as separate meshes: head shaping, jaw, snout, ears, hands as hand-made meshes, boolean or join them later.
7. Apply Skin (and Subsurf) on a copy only after approving the silhouette; then retopo or sculpt.

When it works: stick-figure to stylised body fast, creature bodies (wolf torso, tail, limbs), rigid armour backing, distant shots, prototypes for blocking animation, and auto armature via `skin_armature_create`.

Limits: round tubular limbs only (no muscle shape), joints pinch, no face, no hands (fingers would need extra tiny chains and are poor), uneven polycount, no UV-friendly layout, and shading artefacts around branches. Treat it as a blockout generator, not a final mesh, unless the style is deliberately blobby.

## 4. Sculpt then retopology

Standard pro pipeline (community practice, UNVERIFIED as a single doc):
1. Sculpt Mode with Multires or Dyntopo (Dyntopo for early forms, Multires once topology is clean). Brushes: Draw, Clay Strips, Grab, Smooth, Inflate, Crease. Work big to small.
2. Retopology: build a clean low-poly mesh over the sculpt with Shrinkwrap (`wrap_method='NEAREST_SURFACEPOINT'`, `use_negative_direction`, offset 0.001) and the Snap-to-face tool, or Quad Remesher-style tools (paid add-on, do not buy without Zac). Free: the voxel remesh plus manual edge loops; or `bpy.ops.object.quadriflow_remesh` (exists in Blender; UNVERIFIED on 5.2.4 quality).
3. Edge flow: concentric loops around eyes and mouth, loops across joints, flow follows muscle direction. 2 to 3 loops at each joint.
4. Bake: high-poly normal, AO, curvature onto the low-poly UV map (Cycles bake, selected to active, cage extrusion 0.02 m, margin matched to padding in `blender-asset-quality`).
5. Final: game body 20k to 60k tris; hero offline 100k+ (budgets in `blender-asset-quality`).

## 5. Anatomy and muscle masses

- Learn the masses before the surface: skull, ribcage, pelvis, then big muscle groups (humanoid: trapezius, deltoids, pectorals, lats, glutes, quads, hamstrings, calves).
- Quadruped (wolf, dog): shoulder blade floats free on the ribcage and sits high; deep narrow chest; the hock (ankle) is the "backward knee" of the rear leg; long forearm and metacarpal in the front; tail from the sacrum.
- Weight: the body should read as having mass sitting over the feet; the centre of gravity must fall within the support polygon of the planted feet.
- Keep a reference sheet of real anatomy (photographs) beside the model. Do not model anatomy from memory.

## 6. Anthropomorphic and creature pitfalls

- Faces: wolf-human hybrids slide into uncanny when the eyes sit on the front of a long muzzle and the brow is human. Choose a side: predator eyes at the front-side with a heavy brow ridge, or a human face with animal features added. The eye line sits about halfway down the skull.
- Eyes: spheres with a separate cornea; add eyelid thickness and a wet rim. Dead eyes are the number one tell of an amateur character. Add a specular catchlight source in the lighting.
- Hands: palm width equals four finger widths; fingers have 3 segments (thumb 2) with lengths roughly in ratio 1 : 0.6 : 0.5; knuckles stagger in an arc; model fingers slightly curled, never ruler-straight.
- Digitigrade legs: the animal stands on its toes; the heel (hock) is the high joint halfway up the visible leg. For a humanoid wolf warrior build the leg as three segments: thigh, calf, a long metatarsal to the toe pad, with a bone chain to match for IK. Plan the rig first.
- Neck and shoulders: animal neck is thick and goes into the shoulders low; do not paste a human trapezius onto a wolf head.
- Ears and tail are the silhouette; check them from the back.
- Proportion drift: a 1.9 m figure with a 0.35 m long head and 0.1 m long hands looks wrong. Check dimensions numerically with `get_scene_info` fields `size`.

## 7. Armor and props fitting

- Model armour on a copy of the body shrunk by the thickness: Shrinkwrap modifier on a plane/shell then Solidify (thickness 0.005 to 0.02 m).
- Leave a visible gap and clearance at joints (elbow, knee) so the rig can bend; split plates into overlapping segments.
- Weight armour pieces to the bone they ride on, 100 percent to that bone, or parent with `parent_type='BONE'` (VERIFIED enum includes `BONE`, `BONE_RELATIVE` on `parent_set`).
- Props in hand: origin at the grip, parent to the hand bone (or use a Child Of constraint on the bone), set a rest pose so the weapon sits correctly.
- Sword: blade 0.8 to 1.0 m, grip 0.12 to 0.15 m, crossguard 0.2 m wide. Check against the character's hand size.
- Scale check: a prop must match the hand. Measure, do not eyeball.

## 8. Fur and hair

| Option | Realtime | Offline | Notes |
|---|---|---|---|
| Hair curves (new hair system, `bpy.ops.object.curves_empty_hair_add` exists, VERIFIED) with geometry nodes | no | yes | Best offline look; editable with the Curves sculpt brushes. Cycles renders them fastest; EEVEE supports curves but heavy counts are slow. |
| Particle hair (legacy) | no | yes | Still present; convert with `bpy.ops.curves.convert_from_particle_system` (VERIFIED exists). Avoid for new work. |
| Hair/fur cards (flat strips with an alpha texture) | yes | ok | The game standard: 100 to 200 cards for a head; fur shells for body. Card textures need a packed alpha. |
| Shells (stacked layers) | yes | no | Cheap fur for short coat; needs a shader. |
| Geometry Nodes fur (Distribute Points on Faces, Curve Primitives, Set Curve Radius, Interpolate Hair Curves) | no | yes | Procedural and tweakable; heavy at millions. |

Decision: final render in Blender (offline) means hair curves plus geometry nodes. Export to Unreal means cards (or UE's groom system via Alembic, UNVERIFIED workflow). Fur density: 5,000 to 20,000 guide curves for a wolf body, children 5 to 20 each. Always check at the camera's actual distance.

## 9. Rigging basics

- Rigify: VERIFIED present in 5.2.4 at `scripts/addons_core/rigify`, bundled. Enabling it in a background run threw a preferences KeyError (a headless quirk; enable in the GUI via Preferences > Add-ons, UNVERIFIED in GUI). Once enabled the operators `object.armature_human_metarig_add` and `pose.rigify_generate` exist (VERIFIED). Rigify provides human and basic animal metarigs (Rigify 'Basic Quadruped' is the nearest for wolf; UNVERIFIED which metarigs ship in 5.2).
- Manual armature: bones along the real joint centres (knee/elbow bent slightly in rest pose so IK knows the bend direction), root bone at the world origin, a clean parent chain: root > pelvis > spine > chest > neck > head, root > pelvis > thigh > shin > foot > toe.
- FK for arms and tails (natural overlap); IK for legs and planted feet; pole targets in front of the knee. Add IK constraint chain length 2 on the shin, with a pole target.
- Naming: `Name_L` / `Name_R` or `.L` / `.R` (Blender mirrors with `.L`/`.R`).
- Skinning:
  - `parent_set(type='ARMATURE_AUTO')` for first-pass automatic weights. Pitfalls: mesh must be a single manifold-ish, closed, applied-scale object; loose pieces get zero weights; overlapping geometry (hair, ears, armour) bleeds; heat map fails with non-manifold or doubles. Fix: Merge by Distance first, separate unconnected pieces, parent rigid pieces by `BONE`.
  - `ARMATURE_NAME` creates empty groups (no weights); `ARMATURE_ENVELOPE` uses envelopes.
  - Normalise and limit: `bpy.ops.object.vertex_group_normalize_all` and `vertex_group_limit_total(limit=4)` (both VERIFIED present) for game engines.
  - Weight paint in Weight Paint mode; check by rotating bones: shoulders, hips, elbows, knees, wrists. Pinching at the elbow = need an extra loop and a corrective bone or shape key.
- Game rigs: max 4 influences per vertex (limit op above), 60 to 120 bones for a character, root bone at origin.
- Always test the rig: pose the extreme range (arms up, legs lunged) and take `look` from 3 angles.

## 10. Posing and checking

1. Pose with FK/IK controls; use mirrored poses (`bpy.ops.pose.copy` / `paste` flipped) for symmetry then break it for life.
2. Pose principles: weight on one leg, opposing hip/shoulder tilt, strong line of action, readable silhouette, avoid twins (both arms same).
3. Check with `look` mode `angles` (front, right, top, three_quarter), shading `solid` for forms and `wireframe` for edge flow; `max_size=512` for quick passes, 1024 for detail. Then `rendered` for materials. For a rig, `mode='frames'` over the animation range shows pose changes cheaply.
4. Numerical checks: `get_scene_info(fields=["size","ground","topology","weights"])` reports ground contact, topology health and weights (vertices that no deform bone moves; deform bones with no vertex group). Aim for both weights counts at zero.
5. Compare to the reference overlay again before declaring done.

## 11. AI image-to-3D services: when and how

Use when: a hero character or creature needs organic detail (face, hands, fur) that code cannot deliver, and a reference image exists.

Rules:
- Zac's rule: FREE ONLY. Ask first before any paid credit. State the exact price and which provider before spending anything.
- `mcp__blender__get_addon_status` lists `generators` (tripo, hunyuan3d, hyper3d, meshy) as on or off. If a provider is off, do not try to turn it on; tell Zac which click or API key is needed. `generate_3d` "may cost the user a credit" per its own tool description, so treat every call as spending until the price is confirmed free.
- A generation is one textured object, not a rigged character, not a whole scene. Expect 1 to 3 minutes, arbitrary scale, messy triangulated topology, baked-in lighting in textures, and a mesh that needs retopo and a rig before production use.
- After import: measure, scale to real height, run the full `blender-asset-quality` audit, then decide: keep as static pose model, or retopo. Never ship a raw generator output as final without checks. Record the licence terms of the provider in the asset log (`blender-asset-sourcing`).
- Each provider has its own commercial-use terms; read them before use and log them. UNVERIFIED for every provider; I did not read any.

## 12. Character delivery checklist

- [ ] Real height and key measurements printed (head, hand, leg, tail).
- [ ] Silhouette passes at 64 px from three angles.
- [ ] Reference overlay comparison done.
- [ ] Topology: loops at joints, no n-gons on deforming areas, within budget.
- [ ] UVs and materials per `blender-asset-quality`.
- [ ] Rig: weights report zero unweighted vertices, max 4 influences, mirrored poses test passed.
- [ ] Armour and props parented to bones, clearance at joints tested in extreme poses.
- [ ] Fur/hair appropriate to the target (offline curves vs real-time cards).
- [ ] Honest note on limits: what code-built could not achieve and what is recommended next.
- [ ] Saved as `D:\Blender Projects\<Name> vN.blend`.
