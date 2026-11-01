---
name: blender-mcp-ops
description: How to drive Zac's live Blender safely and well through the blender MCP tools (get_addon_status, get_scene_info, execute_blender_code, look, search_assets, import_asset, generate_3d). Use before ANY action in Zac's open Blender session, for every Blender agent, whenever the task involves running bpy code, checking the scene, taking viewport or rendered looks, creating a scratch test scene, saving files, parenting or grouping objects, switching render engines, or recovering from errors. Contains the safety rules (never touch Zac's objects, versioned saves, no destructive ops without a copy) and the gotchas found while testing.
---

# Blender MCP operations

Tested on Blender 5.2.4 (LTS release candidate). Honest status of this skill's evidence: the live MCP link to Zac's GUI Blender was DOWN during writing (addon handshake failed with "Connection to Blender lost", `get_scene_info` and `execute_blender_code` returned "Not connected to Blender"; only the `blender-mcp` process was running, Blender itself was not). So all bpy behaviour below was verified in a separate headless Blender 5.2.4 process (`blender -b --factory-startup --python file.py`), which cannot touch Zac's session. The `look` tool and addon status could not be tested live: those parts come from the tool descriptions and are marked (TOOL DOC). Sources in references.md.

## 1. Iron rules

1. **Zac's scene is not yours.** Objects such as `Wolf`, `WolfBody`, `Sword` and anything not created by you in this session are read-only. Do not move, rename, delete, apply modifiers to, re-parent, re-material, or change visibility of them. Do not change scene-level settings (camera, render engine, frame range, units, world) in his scene.
2. **Work in your own scene.** For tests, experiments and builds that are not Zac's request, create a scratch scene (section 6), prefix all objects `TEST_`, and delete everything when done.
3. **Never save over a file.** Versioned saves only: `D:\Blender Projects\<Name> vN.blend`, N one higher than the highest existing. Check the folder first; never `save_mainfile` to the current path unless Zac says so; never `bpy.ops.wm.save_mainfile()` in a test.
4. **No destructive operation on user objects without a copy.** Applying modifiers, joining, deleting vertices, decimating, remeshing, applying scale: duplicate first, work on the copy, keep the original hidden in `_SOURCE`.
5. **One small verified step at a time.** Run a step, print what changed, check it, then continue. Do not paste a 300-line script that builds everything blind.
6. **If the tools say "Not connected to Blender", stop.** Report it. Do not fall back to launching a second Blender against his files. Headless Blender is fine for tests on scratch data only, never on his `.blend`.

## 2. Session start (always, in this order)

1. `get_addon_status`. Read: `up_to_date`, `blender_version`, `libraries` (polyhaven, sketchfab, polypizza on or off), `generators` (tripo, hunyuan3d, hyper3d, meshy on or off). If `up_to_date` is false or `source` is `error`, tell Zac how to update: `uvx mcp-for-blender install-addon`, then in Blender disable and enable "Interface: Blender MCP" (or restart) and press Start MCP Server (text comes from the tool's own output).
2. `get_scene_info` with default fields, then once more with `fields=["settings"]` to read file, engine, frame range, resolution, camera, HDRI, unit scale. Write them down. This is your baseline for diffing at the end.
3. List what exists: top-level objects only (default). Note names that are Zac's. You may list a hierarchy with `root="Name"` or search with `query="wolf"`.
4. Check the active camera name (`scene.camera`). It can be hijacked (section 7).

## 3. Reading the scene (cheap and exact)

`get_scene_info` fields: placement (`location`, `size`, `ground`, `rotation`, `scale`, `parent`), contents (`children`, `hidden`, `details`, `materials`, `modifiers`, `animation`), health (`topology`, `weights`), `settings`. Default limit is 20 objects; raise `limit` for bigger scenes. Prefer it over scripts for counts: it reports quads, tris, ngons, non-manifold and boundary edges, loose verts, poles, and for rigs: vertices no deform bone moves, deform bones with no vertex group.

For anything else, use `execute_blender_code` and `print()` exactly what you need. Output is whatever you print. Keep printed output short: print counts and names, not entire lists.

Always pass `user_prompt` (Zac's words, verbatim) on every call in a task. Do not paraphrase.

## 4. Writing bpy safely

- **Shader nodes by type, never by name** (names are localised): `next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")`. Output node: `n.type == "OUTPUT_MATERIAL"`. Image texture: `"TEX_IMAGE"`.
- **Never hardcode enum values.** Read them:
  `[i.identifier for i in bpy.types.RenderSettings.bl_rna.properties["file_format"].enum_items]`.
  Tested caveat: reading `render.engine` enum items in a background session returned only `['BLENDER_EEVEE']`, yet assigning `'CYCLES'` worked and assigning garbage raised `TypeError: ... enum "BOGUS" not found in ('BLENDER_EEVEE', 'BLENDER_WORKBENCH', 'CYCLES')`. So read the current value, then assign inside `try/except TypeError` and print the message to get the valid list. Same trick applies to any enum.
- **Material colours go on node inputs**, not `material.diffuse_color` (viewport only).
- Principled input names in 5.2.4: Base Color, Metallic, Roughness, IOR, Alpha, Normal, Subsurface Weight, Specular IOR Level, Specular Tint, Anisotropic, Transmission Weight, Coat Weight, Sheen Weight, Emission Color, Emission Strength, Thin Film Thickness. Old names (Specular, Subsurface, Transmission, Coat, Emission) are gone. Look up with `inputs.get(name)` and handle `None`, or loop `inputs` and match `name`.
- **New materials in 5.2.4 already have a node tree** (`bpy.data.materials.new(...).node_tree` was a `ShaderNodeTree` without setting anything). `Material.use_nodes` is deprecated and the interpreter warns it will be removed in Blender 6.0. Do not set it in new code.
- **Auto smooth is gone** (4.1+): no `Mesh.use_auto_smooth`. Use `bpy.ops.object.shade_smooth_by_angle(angle=..., keep_sharp_edges=True)` or `shade_smooth()`.
- Operators need context. Prefer data-API edits (`obj.location = ...`, `obj.modifiers.new(...)`, `bmesh`) over `bpy.ops.*`. When an operator is needed, select and activate explicitly: `bpy.ops.object.select_all(action='DESELECT'); obj.select_set(True); bpy.context.view_layer.objects.active = obj`. Use `with bpy.context.temp_override(...)` if a context is missing.
- Create meshes without ops: `me = bpy.data.meshes.new(name); me.from_pydata(verts, edges, faces); me.update(); ob = bpy.data.objects.new(name, me); coll.objects.link(ob)`; or `bmesh.ops.create_cube(bm, size=1)` then `bm.to_mesh(me); bm.free()`.
- Name everything you create with a clear prefix and keep a list so cleanup is exact.
- Wrap risky code in `try/except Exception as e: print("ERR", e)` so the failure message comes back instead of a bare failure. The tool returns text only.

## 5. The `look` tool (TOOL DOC, not live-tested)

Modes: `viewport` (what Zac sees, default), `camera` (through the scene camera at render aspect), `angles` (auto-framed sides: default front, right, top, three_quarter; `views` takes up to 6 of front, back, left, right, top, three_quarter or `[x, y, z]` directions), `frames` (strip over the animation: `frames` list or `frame_count` 2 to 12, plus `view`).
Shading: `solid`, `material`, `rendered` (EEVEE and Workbench only; not Cycles), `wireframe`, `xray` (bones in front). Default is the viewport's current shading.
Other: `target` (object names to frame, children included; default every visible object), `distance` (metres), `max_size` (longest side in pixels, default 768; images stay in the conversation so every one costs tokens). Settings changed for the shot are restored afterwards (TOOL DOC).

How to use it:
- Quick checks: `max_size=384` to `512`. Detail checks: 1024. Never above 1024 unless reading small text.
- Always set `target` to your own object so Zac's objects are not framed in. If you are in a scratch scene, make sure the viewport is showing that scene (the tool looks at what Zac sees in the current window; switching his window's scene changes his view, see section 6 for the safe approach).
- Judging a model: `mode="angles"`, `shading="solid"` first (forms and silhouette), then `wireframe` (edge flow), then `material` or `rendered` (shading and textures).
- Judging an animation: `mode="frames"`, `frame_count=6`, `shading="solid"`.
- `camera` mode uses `scene.camera`; confirm its name before trusting the image.
- Cycles caveat: `rendered` shading is EEVEE and Workbench only, so for a Cycles look do an actual render to `Render Result` and pass `image="Render Result"`. UNVERIFIED how that behaves through MCP; test in a scratch scene when connected.
- After `look`, state in one sentence what you see and what you will change.

## 6. Clean scratch scene for tests (tested headless 2026-10-31)

```python
import bpy, bmesh
sc = bpy.data.scenes.new("TEST_scene")
# build only into sc.collection; never link into Zac's scene collection
me = bpy.data.meshes.new("TEST_m"); bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1); bm.to_mesh(me); bm.free()
ob = bpy.data.objects.new("TEST_cube", me); sc.collection.objects.link(ob)
cam = bpy.data.cameras.new("TEST_cam"); co = bpy.data.objects.new("TEST_cam", cam)
sc.collection.objects.link(co); sc.camera = co      # camera is per scene
```
Cleanup (run last, then print what remains):
```python
for ob in [o for o in bpy.data.objects if o.name.startswith("TEST_")]: bpy.data.objects.remove(ob)
for coll in (bpy.data.meshes, bpy.data.cameras, bpy.data.materials, bpy.data.worlds, bpy.data.images):
    for d in [x for x in coll if x.name.startswith("TEST_")]: coll.remove(d)
bpy.data.scenes.remove(bpy.data.scenes["TEST_scene"])
print([s.name for s in bpy.data.scenes], [o.name for o in bpy.data.objects if o.name.startswith("TEST_")])
```
Tested result: scenes back to the original, zero TEST_ objects or meshes, `bpy.data.is_dirty` False in the headless run. In Zac's live session the file will show as modified (dirty) after any change; do not save it. Never call `bpy.context.window.scene = sc` in his session: it flips what he sees. Run checks that do not need the viewport (bmesh, audit script, data API) inside the scratch scene without switching his window. When you do need `look` on test objects, tell Zac first, switch, look, and switch back to the original scene in the same step.

`audit_asset.py` from `blender-asset-quality` reads `bpy.context.scene` for units and the evaluated depsgraph, so the object must be in the context scene to evaluate modifiers. In a scratch run in a live session, either audit with `use_evaluated=False`, or tell Zac you are briefly switching scenes. Headless is the cleanest.

## 7. Known gotchas

- **Camera hijack (happened before):** `scene.camera` once pointed at a mesh object. Symptoms: `look` in camera mode shows nonsense or errors. Check: `print(bpy.context.scene.camera, bpy.context.scene.camera.type if bpy.context.scene.camera else None)`; must be `CAMERA`. Do not fix it in Zac's scene without asking; report it. In your own scene, set `sc.camera` explicitly.
- A new scene has no camera and no world (`sc.world` is `None` in the tested run). Add a camera and a World (`bpy.data.worlds.new`) if you need a render.
- Newly created scene objects do not get a default material; they render grey. Create `M_`-style materials with names.
- `bpy.data.scenes.new` produces an empty scene; the objects only appear in `look` when that scene is the window scene.
- Enum reads under-report (engine example above). Use try/except to discover.
- `bpy.ops.object.transform_apply` on multi-user mesh data fails; use `isolate_users=True` (argument confirmed in 5.2.4) or `make_single_user` first.
- The Skin modifier's per-vertex data is `mesh.skin_vertices[0].data[i]` (radius, use_root, use_loose), not an attribute named skin.
- Rigify is bundled (`scripts/addons_core/rigify`) but enabling it in a background run raised a preferences KeyError; enable via the GUI add-ons panel. `pose.rigify_generate` exists once enabled.
- Cycles `compute_device_type` enum read empty in background; read it in the live session before assuming OptiX. Zac's machine has an RTX 5060 and Cycles OptiX was configured earlier (TASKS.md 2026-10-31). Setting it: `prefs = bpy.context.preferences.addons['cycles'].preferences; prefs.compute_device_type = 'OPTIX'; prefs.get_devices()` then enable each device (UNVERIFIED sequence in 5.2.4). This is a user preference, so ask Zac before changing it.
- Importing assets changes the file. Do it in your own scene or collection and name-prefix.
- Huge prints get truncated or cost tokens: print counts and short lists.
- Do not run `bpy.ops.wm.read_factory_settings`, `read_homefile`, `open_mainfile`, `revert_mainfile`, `quit`, or `file_new`: they replace Zac's open session.
- Timeouts: long operations (bake, render, remesh, voxel) can exceed the tool timeout. Prefer small chunks; do not retry blindly.

## 8. Parenting, grouping, naming

- Group with **collections** (`bpy.data.collections.new("ASSET_Wolf")`, `parent_coll.children.link(c)`), not empties, unless the parts must move together at runtime.
- Parent with preserved transform: `child.parent = parent; child.matrix_parent_inverse = parent.matrix_world.inverted()`. Never set `parent` and let the child jump.
- Parent to a bone: `child.parent = armature; child.parent_type = 'BONE'; child.parent_bone = "Hand_R"` (then set `matrix_parent_inverse` accordingly).
- `bpy.ops.object.parent_set(type=...)` valid types in 5.2.4 include `OBJECT`, `ARMATURE`, `ARMATURE_NAME`, `ARMATURE_AUTO`, `ARMATURE_ENVELOPE`, `BONE`, `BONE_RELATIVE`, `CURVE`, `FOLLOW`, `PATH_CONST`, `LATTICE`, `VERTEX`, `VERTEX_TRI`.
- Names per `blender-asset-quality` section 9.

## 9. Saving

- Zac's rule is the file path `D:\Blender Projects\<Name> vN.blend`. Look at what exists:
  `import os, re; d=r"D:\Blender Projects"; print(sorted(f for f in os.listdir(d) if f.endswith(".blend")))`.
- Next name = highest N + 1. Save with `bpy.ops.wm.save_as_mainfile(filepath=path, copy=True)`. `copy=True` writes a copy and does NOT change the open file's path or overwrite it (operator argument; UNVERIFIED on 5.2.4 listing, check `bpy.ops.wm.save_as_mainfile.get_rna_type().properties.keys()` first). Verify the file exists and print its size afterwards.
- Only save when Zac asks or the task is a deliverable. Never in tests. Say the path in the report.
- Scratch/test files: `D:\WKP\scratch\`. Deliverables log line in `D:\WKP\logs\`.

## 10. Performance and render engines

- Viewport work: Solid or Material Preview, `look` with `max_size` 384 to 768. `rendered` shading in the viewport is EEVEE or Workbench only.
- Engines available in 5.2.4 (from the TypeError list): `BLENDER_EEVEE`, `BLENDER_WORKBENCH`, `CYCLES`. The enum name is `BLENDER_EEVEE`, not `BLENDER_EEVEE_NEXT`.
- EEVEE: fast previews and final output for stylised or fast-turnaround animation. Ray tracing option exists (`scene.eevee.ray_tracing_method`, `use_taa_reprojection`, `taa_render_samples`, `gi_*` props confirmed).
- Cycles on the RTX 5060 with OptiX: final stills, hair curves, realistic fur and glass. Denoise on. 64 to 256 samples for previews, 256 to 1024 for finals. Use a small render border or resolution percentage 50 for tests.
- Before a full render: check frame range, resolution, output path, engine; estimate time from one frame; ask Zac before long renders (a 1000-frame Cycles job can take hours).
- Heavy things: Subdivision above level 3, particle or curve hair above 100k strands, volumetrics, many 4K textures. Use viewport levels low.
- Keep viewport tris below about 5 million for smooth interaction (rule of thumb, UNVERIFIED for this machine).
- Do not leave `look` calls inside loops; each image costs tokens.

## 11. Per-task template

1. `get_addon_status`, `get_scene_info` (and settings). Record baseline.
2. State the plan in one line, name your prefix (`TEST_` or `ASSET_`).
3. Create your scratch scene or collection.
4. Build in steps. After each: print numbers, then `look` at 384 to 512.
5. Run `audit_asset.py`. Fix FAILs.
6. Save a versioned copy if it is a deliverable.
7. Clean up (section 6), print remaining names.
8. Re-run `get_scene_info` and diff against the baseline: Zac's object names, count and settings must be identical.
9. Report: what was made, numbers, file path, and the list of Zac's objects still present.

## 12. Things only Zac can do (ask, do not attempt)

- Switch on a library (Poly Haven, Sketchfab, Poly Pizza) or paste an API key in the addon panel.
- Spend credits or money, including `generate_3d` (may cost a credit) and paid assets.
- Change user preferences (GPU compute type), add-on enable states, or overwrite his files.
- Delete or rename anything of his.
