---
name: blender-asset-quality
description: The quality standard every finished Blender asset must meet before it leaves the Blender section of the Animation department. Use when an agent finishes, reviews, audits, cleans up, names, UV unwraps, applies modifiers on, or prepares to export any model, prop, character, creature or environment piece, and when someone says "is this ready", "check this asset", "audit", "clean up the mesh", "export to Unreal", "FBX", "glTF", "poly count", "topology", "normals", "UVs", "naming convention". Includes a tested bpy audit script that reads real numbers from the scene.
---

# Blender asset quality standard

Verified against Blender 5.2.4 (LTS release candidate) headless on Zac's machine. Items tagged UNVERIFIED came from community sources or search snippets, not an official page or a live test. See references.md.

Rule zero: never report an asset as ready from looking at it. Run the audit script, read the numbers, paste them in the report.

## 1. Run the audit first

```python
import runpy
ns = runpy.run_path(r"D:\WKP\.claude\skills\blender-asset-quality\scripts\audit_asset.py")
ns["audit"](["SM_Crate"], kind="prop", expected_prefix="SM_")
```

It is read-only. It prints PASS / WARN / FAIL per object with: dimensions in metres, tris, quads, n-gons, non-manifold edges, loose verts and edges, zero-area faces, duplicate verts, UV layers, UV area used, texel density spread, UV corners outside 0-1, unapplied scale or rotation, negative scale, material slots (empty and unused), power-of-two check on image nodes, inside-out check on closed meshes (signed volume), and orphan data counts. `kind` sets the triangle budget (section 4).

Tested 2026-10-31 on TEST_ objects in a headless Blender: a crate with scale (2,1,1), a loose vertex and no UVs returned FAIL on all three; a clean unit cube with UVs returned a clean result. Ship rule: no FAIL, every WARN either fixed or explained in the report.

Also use the built-in MCP tool for a second opinion: `get_scene_info` with `fields=["topology","materials","modifiers","placement"]` reports quads, tris, ngons, non-manifold and boundary edges, loose verts and poles.

## 2. Units and scale

- Scene: Unit System Metric, Unit Scale 1.0 (`scene.unit_settings.system == 'METRIC'`, `scale_length == 1.0`). The audit warns if not.
- 1 Blender unit = 1 metre. Model at real size. Reference sizes: door 2.0 x 0.9, chair seat height 0.45, adult human 1.7 to 1.9, sword 1.0 to 1.2, wolf shoulder height 0.7 to 0.9 (a real grey wolf), coffee cup 0.1.
- Unreal uses 1 unit = 1 centimetre (Epic's FBX docs: "1 Unreal Unit equals 1 centimeter"). A correctly sized 1 m cube in Blender should import as 100 uu. Confirm by importing a test cube the first time on any new export setup. FBX exporter options that matter: `global_scale`, `apply_scale_options`, `apply_unit_scale`.
- Imported or generated models arrive at arbitrary scale. Measure `obj.dimensions` and fix before anything else.

## 3. Transforms, origin, pivot

- Apply scale and rotation on every mesh before export: `bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)`. Never apply scale on a mesh with shared data users without `isolate_users=True` (the operator has that argument in 5.2.4).
- Final state: scale (1,1,1), rotation (0,0,0), no negative scale. Negative scale flips normals and breaks exports.
- Origin by asset type:
  - Prop on the ground: origin at the centre of the base, on the floor (Z = 0 at the bottom).
  - Hand-held (sword, tool): origin at the grip point, axes aligned to the hand.
  - Door or hinged piece: origin on the hinge axis.
  - Character: origin at world centre between the feet, feet on Z = 0, facing -Y in Blender (front view looks along +Y). UE root bone sits at the same place.
  - Modular kit pieces: origin on a grid corner, dimensions in multiples of the grid (e.g. 1 m, 2 m, 4 m).
- Set origin without moving geometry: 3D cursor to target, then `bpy.ops.object.origin_set(type='ORIGIN_CURSOR')`.
- Do not parent unrelated objects just to group them. Use collections for grouping; parent only for real mechanical relationships (sword to hand bone, wheel to car).

## 4. Topology and budgets

- Quads by default. Triangles are fine in flat, non-deforming areas and are what the game engine ends up with anyway. N-gons: zero on anything that deforms, subdivides, or is sculpted. Allowed on flat hard-surface faces that never deform (e.g. a flat cap on a cylinder) if they will be triangulated cleanly. Epic's skeletal mesh import wants triangulated meshes (Epic doc: "Meshes must be triangulated").
- Edge flow follows form: loops around eyes, mouth, elbows, knees, shoulders, fingers. Put 3 loops at a deforming joint, 2 minimum.
- Poles: 5-edge poles are fine, put them on flat low-curvature areas, not on the cheek or the knee crease. Avoid poles of 6 or more edges.
- Non-manifold edges: zero on anything solid. Allowed only on intentional open shells (cloth planes, hair cards, leaves).
- No loose verts or edges, no zero-area faces, no doubled verts (Merge by Distance 0.0001 m).
- Do not leave interior faces or hidden geometry under armour or clothes unless needed.
- Budgets (WKP working targets, tris, community-derived, not an official standard):

| Asset type | Real-time (UE) tris | Hero / offline render tris |
|---|---|---|
| Small prop (cup, tool) | 500 to 3,000 | up to 30,000 |
| Hero prop (sword, key weapon) | 5,000 to 20,000 | 50,000 to 200,000 |
| Character (game) | 20,000 to 60,000 | 100,000 to 500,000 |
| Creature (game, with fur cards) | 40,000 to 80,000 | 200,000 to 1,000,000 |
| Environment piece (wall, rock) | 1,000 to 20,000 | 20,000 to 100,000 |
| Background filler | under 1,500 | under 5,000 |

  Pick `kind` in the audit accordingly (`prop`, `hero_prop`, `character_game`, `character_hero`, `environment_piece`, `background`). Offline renders have no hard cap, but keep the viewport at 30 fps or better.
- LODs for real-time: LOD0 100 percent, LOD1 about 50, LOD2 about 25, LOD3 about 10. Name `SM_Name_LOD0` ... (UE FBX import recognises the `_LOD#` suffix, UNVERIFIED in English docs). Decimate modifier for quick LODs, hand-fix silhouettes.
- Collision for UE: separate simple convex meshes named `UCX_SM_Name_01` (Epic's FBX static mesh pipeline uses the `UCX_` prefix, confirmed in search excerpts; exact English wording UNVERIFIED). Keep them convex, under 32 verts each.

## 5. Normals and shading (Blender 4.1 and later)

Live-checked in 5.2.4: `Mesh.use_auto_smooth` and `Mesh.calc_normals_split` no longer exist. Any old snippet that sets them throws AttributeError.

- Smooth/flat is stored as the boolean face attribute `sharp_face` (seen in `mesh.attributes` on a new mesh). `Mesh.corner_normals`, `normals_domain`, `has_custom_normals`, `vertex_normals`, `polygon_normals` all exist.
- Default for organic and most props: `bpy.ops.object.shade_smooth()` then Smooth by Angle. One-call version: `bpy.ops.object.shade_smooth_by_angle(angle=math.radians(30), keep_sharp_edges=True)` (args confirmed: `angle`, `keep_sharp_edges`). Angle 30 degrees is the common default. UE caveat: the shading is exported as per-edge smoothing; check in UE after import.
- Smooth by Angle runs before the modifier stack in 4.1+, the old auto smooth ran after it (community and Blender bug tracker threads). Practical effect: put it at the top of the stack, and do not expect it to re-smooth after a Subdivision modifier.
- Hard-surface props: flat shading plus Bevel modifier (segments 2 or 3, width 0.002 to 0.01 m, `harden_normals=True`, angle limit 30 degrees) plus Weighted Normal modifier (`mode='FACE_AREA'`, `keep_sharp=True`, weight 50 to 100). Props confirmed on the 5.2.4 modifier: `weight`, `mode`, `thresh`, `keep_sharp`, `use_face_influence`.
- Character and creature: smooth with Smooth by Angle 45 to 60 degrees, no custom normals unless there is a seam problem.
- Always check normals visually with `look` in `wireframe` and `solid` shading from two or more angles. Dark patches or inverted lighting means flipped faces: Edit Mode, select all, Mesh > Normals > Recalculate Outside (`bpy.ops.mesh.normals_make_consistent(inside=False)`).
- The audit flags a closed mesh with negative signed volume as inside-out.

## 6. UV unwrap

- Every renderable mesh has a UV map. Zero UV maps = FAIL.
- First UV channel (`UVMap`, index 0) is the texture UV: non-overlapping, inside 0-1, one island per material zone, seams hidden in natural creases and under armour edges.
- Overlap is allowed only for mirrored halves (symmetric props and characters) or deliberate tiling. Check: the audit prints `uv_area_used`; above 1.05 without a mirror reason is a WARN.
- Second UV channel for baked lightmaps in UE (name it `UVLightmap`, index 1): no overlap at all, even for mirrored parts. Only needed for static meshes using baked lighting. UE can also generate it on import (UNVERIFIED which default applies in 5.x).
- Texel density: the same real-world size gets the same pixel count. WKP targets (community practice, UNVERIFIED as a standard): 10.24 px/cm (a 1K map across 1 m) for props, 20.48 px/cm (a 2K map across 1 m) for hero close-ups, 5.12 px/cm for background. The audit measures consistency only, not absolute density: `texel_density_spread` should be below 2.0 (WARN above 2.5). Work out absolute density yourself: texture pixels across the UV area divided by the real size in cm.
- Padding between islands: 8 px at 1K, 16 px at 2K, 32 px at 4K for baked maps (community rule, UNVERIFIED as a standard). In bpy: `bpy.ops.uv.pack_islands(margin=0.01, rotate=True, merge_overlap=False)` (args confirmed in 5.2.4: `margin`, `rotate`, `merge_overlap`, `scale`, `shape_method`, `margin_method`). Quick unwrap for rough props: `bpy.ops.uv.smart_project(angle_limit=math.radians(66), island_margin=0.01)`.
- Straighten and equalise islands by hand on anything the camera will see up close; Smart UV Project is acceptable only for rough or background props.
- Name UV channels `UVMap` (colour/PBR) and `UVLightmap`. Delete unused extra channels (they increase FBX size and confuse exporters).

## 7. PBR materials

- One Principled BSDF per material. Look the node up by type, never by name: `next(n for n in mat.node_tree.nodes if n.type == "BSDF_PRINCIPLED")`. Note `material.use_nodes` is deprecated and slated for removal in Blender 6.0 (live warning in 5.2.4); avoid setting it in new code, new materials already carry a node tree in recent versions, so check `mat.node_tree` first.
- Principled input names in 5.2.4 (live): Base Color, Metallic, Roughness, IOR, Alpha, Normal, Diffuse Roughness, Subsurface Weight, Specular IOR Level, Specular Tint, Anisotropic, Transmission Weight, Coat Weight, Sheen Weight, Emission Color, Emission Strength, Thin Film Thickness. Older names (Specular, Subsurface, Transmission, Coat, Emission) were renamed; do not use them.
- Texture colour spaces: Base Color = sRGB; Roughness, Metallic, AO, Normal, Height, ORM = Non-Color. Wrong colour space is the most common cause of washed-out or dark materials.
- Metallic is nearly binary: 0 or 1. Intermediate values only on dirt/transition pixels.
- Normal maps: Blender and OpenGL convention is green up (+Y). Unreal expects DirectX convention (green down, -Y). Fix before export: either invert the green channel in the texture, or use the green-flip option in UE's texture settings (UNVERIFIED exact label). Test with a single bump lit from one side.
- Packing for real-time: ORM = Occlusion (R), Roughness (G), Metallic (B), Non-Color, one 8-bit texture. Suffixes: `_BC` base colour, `_N` normal, `_ORM` packed (Epic/community convention, UNVERIFIED as official).
- Sizes: powers of two only (512, 1024, 2048, 4096). Props 1K to 2K, hero props and character body 2K to 4K, background 512. Non-square OK if both sides are powers of two. Audit warns on non-power-of-two image nodes.
- Max material slots on a game asset: 1 to 3 (each slot is a draw call). Merge slots, use texture atlases.
- Image textures must be packed or saved beside the file; the audit warns on `no_pixels_or_missing_file`.

## 8. Modifiers: what to apply, in what order

Order in the stack (top to bottom): Mirror, Array, Boolean, Smooth by Angle (if used as a modifier), Bevel, Weighted Normal, Subdivision Surface, Armature last or near-last. (Skin modifier docs: put the Armature directly below Skin so it deforms without changing topology.)

- Before export to a game engine: apply Mirror, Array, Boolean, Bevel, Solidify, Triangulate. Do not apply Armature. Exporting with modifiers evaluated: FBX `use_mesh_modifiers=True` (default) does this at export time without altering the scene, which is the safer route.
- Subdivision: keep the viewport level at 1 or 2 during work, render level 2 or 3. For real-time delivery either apply once at level 1 and clean up, or keep the low poly and bake normals from the high poly.
- Mirror: keep `use_clip` on and merge on the centre line. Apply Mirror only when asymmetry details start (scars, different armour).
- Never apply modifiers on an object that has shape keys (Blender refuses or loses keys). Make a copy first.
- Never apply on the user's original object. Duplicate, apply on the copy, keep the original in a hidden collection `_SOURCE`.
- After applying Mirror, check the UVs: mirrored halves are fine but overlapping parts must be intentional.

## 9. Naming (Unreal style)

| Type | Pattern | Example |
|---|---|---|
| Static mesh | `SM_Name` | `SM_Crate_01` |
| Skeletal mesh | `SK_Name` | `SK_Wolf` |
| Skeleton asset | `SKEL_Name` | `SKEL_Wolf` |
| Material | `M_Name` | `M_Fur` |
| Material instance | `MI_Name_Variant` | `MI_Fur_Dark` |
| Texture | `T_Name_BC`, `_N`, `_ORM`, `_E` (emissive) | `T_Crate_BC` |
| Animation | `A_Name_Action` (UE convention is `A_`/`AS_`) | `A_Wolf_Run` |
| LOD | `SM_Name_LOD0` | |
| Collision | `UCX_SM_Name_01` | |

- PascalCase, no spaces, no `.001` suffixes (audit warns on them), no non-ASCII characters.
- Name the object, the mesh data, the materials and the images consistently: object `SM_Crate`, mesh data `SM_Crate`, material `M_Crate`.
- Armature `Armature` is not a name. Use `SK_Wolf_Rig`; bones `spine_01`, `Hand_L` style with L/R suffix (`.L`/`.R` is Blender's mirror convention; keep it if using symmetry tools, rename on export only if the target engine needs it).
- Source of the SM_/SK_/T_/M_/MI_ prefixes: community Unreal style guides and Epic's recommended naming, UNVERIFIED against a single official page.

## 10. Collections and clean-up

- Collections: `ASSET_Name` containing the final meshes, `_SOURCE` (hidden, excluded) for originals and sculpts, `_REF` for reference images, `_RIG` for armature and controls. Exports use the collection (`export_scene.fbx(collection=...)`) so only intended objects go out.
- Remove unused material slots: Material Properties > the minus button, or script `bpy.ops.object.material_slot_remove_unused()`.
- Purge orphans after all edits, repeat until zero: `bpy.ops.outliner.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)` (args confirmed).
- Delete unused vertex groups, extra UV maps, extra colour attributes, leftover empties, cameras and lights that are not part of the asset.
- Do not leave hidden objects in the final file unless in `_SOURCE`.

## 11. Before-export checklist

Copy this into the report and mark each.

- [ ] Audit run, no FAIL, WARNs explained. Numbers pasted.
- [ ] Unit Scale 1.0, Metric. Real-world dimensions correct (list them).
- [ ] Scale and rotation applied, origin placed per section 3.
- [ ] Tris within budget for the asset kind.
- [ ] Zero loose geometry, zero non-manifold on solids, zero n-gons on deforming parts.
- [ ] Normals face outward, smooth/flat intentional, checked with `look` from 3 angles.
- [ ] UVs: no unplanned overlap, inside 0-1, density spread under 2, padding set.
- [ ] Materials: Principled, correct colour spaces, power-of-two textures, normal map convention matches the target (OpenGL for Blender, DirectX for UE).
- [ ] Modifiers applied or exported as evaluated, Armature kept.
- [ ] Names follow section 9, no `.001`.
- [ ] Orphans purged, unused slots removed.
- [ ] Rig (if any): every vertex weighted, max 4 influences per vertex for game, root bone at origin.
- [ ] Saved as versioned `.blend`: `D:\Blender Projects\<Name> vN.blend`, never overwrite.
- [ ] Export test: FBX or glTF re-imported into a scratch scene and measured.

## 12. Export notes (parameters confirmed in 5.2.4)

- FBX for Unreal: `bpy.ops.export_scene.fbx(filepath=..., use_selection=True, object_types={'MESH','ARMATURE'}, use_mesh_modifiers=True, mesh_smooth_type='FACE', add_leaf_bones=False, use_tspace=True, apply_scale_options='FBX_SCALE_ALL', bake_anim=False)`. Enum values must be read, not assumed: `bpy.ops.export_scene.fbx.get_rna_type().properties['apply_scale_options'].enum_items`. UE uses FBX 2020.2 (Epic).
- Armatures: `add_leaf_bones=False`, `use_armature_deform_only=True`.
- glTF (`export_scene.gltf`) is the better route for web and for transferring PBR materials; it exposes `export_tangents`, `export_normals`, `export_texcoords`, `export_draco_mesh_compression_enable`, `export_format`.
- Export, then import into a TEST_ scratch scene and re-run the audit on the result.

## 13. Report format

```
ASSET: SM_Crate  KIND: prop
dims 1.00 x 0.60 x 0.60 m | tris 1,240 | quads 620 | ngons 0 | nonmanifold 0 | loose 0
UV: UVMap, density spread 1.3, overlap none | materials 1 (M_Crate) | textures 2K, ORM
audit verdict: PASS | WARN items: none
file: D:\Blender Projects\Crate v3.blend
```
