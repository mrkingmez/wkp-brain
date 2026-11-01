---
name: ue-import-pipeline
description: How to move assets from Blender 5.x into Unreal Engine 5.8 correctly. Use for any request to import, export, bring in, convert or validate a model, prop, character, creature, skeleton, animation, texture or material in Unreal; FBX vs glTF vs USD vs Interchange; axis, scale and pivot problems; naming prefixes; collision (UCX_), LODs, Nanite eligibility, lightmap UVs, ORM and normal-map settings, IK Retargeter, folder structure, Data Validation, editor Python import scripts, headless commandlets; and troubleshooting wrong scale, flipped normals, black materials, missing textures or bad pivots. Written for the ue-asset-integrator agent.
---

# ue-import-pipeline

Owner: ue-asset-integrator. Engine: Unreal Engine 5.8.4 at `D:\Epic\UE_5.8`. Asset source: Blender 5.2.4. Projects live in `D:\Unreal Projects`. Free tools only; ask Zac before any spend.

Evidence tags used below:
- VERIFIED-5.8 = read from the installed engine files or 5.8 release notes.
- DOC-5.x = Epic documentation page written for an earlier 5.x; assumed to still hold, not re-tested in 5.8.
- COMMUNITY = widely repeated practice, not from Epic.
- UNVERIFIED = could not confirm for 5.8. Test on a throwaway asset before trusting it.

Hard rules:
1. Never launch the editor to "see what happens" without a task from the caller. Never edit anything under `D:\Epic\UE_5.8`.
2. Never overwrite a source `.blend`. Export to `D:\Unreal Projects\<Project>\_Incoming\` first, import from there.
3. Import one test asset before a batch. Batches inherit mistakes.
4. Report numbers (triangle count, bounds in cm, texture sizes), not adjectives.

---

## 1. Format choice

| Format | Use for | Avoid for | Notes |
|---|---|---|---|
| FBX | Static meshes, skeletal meshes, animation, LODs, collision, sockets. The default production path. | Anything needing full PBR round trip | Epic FBX pipeline is built on FBX 2020.2 (DOC-5.x). Blender writes FBX 7.4 binary; works in practice (COMMUNITY). |
| glTF / GLB | Single textured props, quick previews, Sketchfab-style assets | Rigged characters with many LODs, collision meshes, sockets | Imported through Interchange. 5.8 ships glTF material parents under `/InterchangeAssets/gltf/` (VERIFIED-5.8). Release notes list only glTF reader vulnerability fixes and exporter fixes (VERIFIED-5.8). |
| USD | Whole scenes, layered assets, pipelines with other DCCs | Casual single props | 5.8 notes: USD import through Interchange is production ready for assets, experimental for levels (VERIFIED-5.8). |
| Alembic | Baked vertex animation, cloth sim caches | Anything that can be skinned | Separate importer plugin. |

Decision for Zac's pipeline:
- Props, environment pieces, hero meshes: FBX first. Use GLB only when the asset arrives from outside with embedded textures and no collision/LOD needs.
- Characters and creatures: FBX with armature. Animation: FBX per clip or one FBX with multiple actions.
- Scenes with many layout objects: USD, treat as experimental until a test passes.

### What Interchange is
Interchange is Epic's file-format-agnostic, asynchronous import/export framework; its pipeline stack is customizable with Blueprint or Python (DOC-5.x). Plugin `Interchange` has `EnabledByDefault: true` in 5.8 (VERIFIED-5.8). Import dialog option names were regrouped and renamed in 5.8 (VERIFIED-5.8 release notes).

The legacy FBX importer still exists in 5.8 (release notes mention fixes to the "legacy FBX importer", VERIFIED-5.8). Which importer opens by default for `.fbx` dragged into the Content Browser in a fresh 5.8 project: UNVERIFIED. Check the dialog title on the first import. Interchange shows the "Interchange Import Content" dialog with a Pipeline Stack selector; the legacy path shows "FBX Import Options". Record which one appeared in the log. A new experimental uFBX library speeds up large FBX imports (VERIFIED-5.8 release notes, Experimental, off by default; do not enable without a task).

---

## 2. Blender to Unreal coordinate and scale

| | Blender | Unreal |
|---|---|---|
| Up axis | +Z | +Z |
| Forward | -Y is "front" view; objects face -Y | +X is forward for characters |
| Handedness | Right-handed | Left-handed |
| Unit | 1 unit = 1 m (Unit Scale 1.0) | 1 unit = 1 cm |

Consequences: a 2 m tall Blender object must arrive as 200 UU tall. Characters must face +X in Unreal.

### Blender 5.2 FBX export settings (File > Export > FBX)
Property names are the Python `bpy.ops.export_scene.fbx` names. Defaults changed little across 4.x to 5.x but confirm in the UI (UNVERIFIED for 5.2.4 exact labels; Blender was not reachable during research).

| Setting | Value | Why |
|---|---|---|
| Limit to: Selected Objects | on (when exporting one asset) | `use_selection=True` |
| Object Types | Mesh, Armature (add Empty only for sockets) | `object_types={'MESH','ARMATURE'}` |
| Scale | 1.0 | `global_scale=1.0` |
| Apply Scalings | FBX Units Scale | `apply_scale_options='FBX_SCALE_UNITS'`. With scene Unit Scale 1.0 the file says meters; Unreal then reads cm correctly when Convert Scene Unit is on. COMMUNITY. |
| Forward | -Y Forward | `axis_forward='-Y'` |
| Up | Z Up | `axis_up='Z'` |
| Apply Unit | on | `apply_unit_scale=True` |
| Use Space Transform | on | `use_space_transform=True` |
| Apply Transform | off (experimental) | `bake_space_transform=False`. Turning it on bakes rotation but breaks armatures and animation. COMMUNITY. |
| Apply Modifiers | on for static meshes, off for skinned meshes with shape keys | `use_mesh_modifiers` |
| Smoothing | Face (or Normals Only) | `mesh_smooth_type='FACE'`. Exports smoothing so Unreal does not recompute normals badly. |
| Triangulate Faces | on | `use_triangles=True`. Epic prefers manual triangulation in the DCC (DOC-5.x). Triangulate with a Triangulate modifier using "Keep Normals" if normals are custom. |
| Tangent Space | on only if the mesh has custom normals and is triangulated | `use_tspace=True` |
| Add Leaf Bones | off | `add_leaf_bones=False`. Leaf bones add junk end joints to the skeleton. |
| Only Deform Bones | on | `use_armature_deform_only=True` |
| Primary/Secondary Bone Axis | Y / X (defaults) | Fine for retargeting through the IK Retargeter. |
| Bake Animation | on for animation exports | `bake_anim=True`, `bake_anim_simplify_factor=0` to keep curves exact, `bake_anim_use_all_actions=False` unless exporting every action. |
| Path Mode | Copy + Embed Textures off | Do not embed. Export textures separately as PNG/TGA/EXR. |

If the mesh arrives rotated 90 degrees or 100x too small/large, see Troubleshooting.

Unreal side (either importer): enable Convert Scene and Convert Scene Unit; leave Force Front X Axis off for props, test it on for characters whose forward axis ends up wrong (DOC-5.x FBX Import Options Reference lists Convert Scene, Force Front XAxis, Convert Scene Unit, Import Uniform Scale).

### glTF export (File > Export > glTF 2.0)
- Format: glTF Binary (.glb) for single props.
- Transform: +Y Up (this is glTF's convention; Blender converts from Z-up). Do not change.
- Include: Selected Objects on; Mesh: Apply Modifiers on, UVs on, Normals on, Tangents on only if needed, Vertex Colors per need.
- Material: Export on. Images: Automatic or PNG. 
- Animation: only if skinned.
- Unreal imports glTF via Interchange and converts to cm and its axes itself. Check bounds after import; glTF is defined in meters (COMMUNITY, verify with the check below).

### USD export (File > Export > USD)
- Up axis: Z (convert_orientation on; set to match). Meters per unit: 0.01 if available so Unreal reads cm; otherwise rely on Interchange Convert Scene Unit. UNVERIFIED for Blender 5.2.4 exact option names.
- Use for scenes only after a one-asset test.

---

## 3. Naming (Epic style, DOC-5.x)

Pattern: `[AssetTypePrefix]_[AssetName]_[Descriptor]_[OptionalVariant]` e.g. `SM_Crate_Wooden_01`, `T_Crate_Wooden_BC`.

| Asset | Prefix | Asset | Prefix |
|---|---|---|---|
| Static Mesh | SM_ | Skeletal Mesh | SK_ |
| Skeleton | SKEL_ | Physics Asset | PHYS_ |
| Material | M_ | Material Instance | MI_ |
| Texture | T_ | Animation Sequence | AS_ |
| Montage | AM_ | Blend Space | BS_ |
| Animation Blueprint | ABP_ | Blueprint | BP_ |
| Level Sequence | LS_ | Rig | Rig_ |
| Niagara System | FXS_ | Niagara Emitter | FXE_ |
| HDRI | HDR_ | Post Process Material | PPM_ |
| Data Table | DT_ | Remote Control Preset | RCP_ |

Texture suffixes: Epic's naming page does not list them (checked). Use this project standard, COMMUNITY: `_BC` base color, `_N` normal, `_ORM` occlusion/roughness/metallic packed, `_E` emissive, `_O` opacity, `_H` height. Do not mix `_D` and `_BC` inside one project.

Collision meshes (DOC-5.x FBX Static Mesh Pipeline), names must contain the render mesh name exactly:
`UBX_<Mesh>_##` box, `UCP_<Mesh>_##` capsule, `USP_<Mesh>_##` sphere, `UCX_<Mesh>_##` convex hull. Spheres and boxes fail under non-uniform scale. Sockets: `SOCKET_<Mesh>_##` on empties; one render mesh with sockets per FBX.
LODs: Epic's page defers to the FBX Import Options Reference for LOD names. Blender-side convention that Unreal reads: `<Mesh>_LOD0`, `_LOD1`, ... (COMMUNITY; UNVERIFIED for Interchange 5.8). Tick Import Mesh LODs.

Rule: Blender object name = Unreal asset name minus prefix. Blender mesh data and material names must match too; no `.001` suffixes.

---

## 4. Static vs skeletal requirements

Static mesh:
- Origin at the intended pivot. Epic: pivot is at (0,0,0) on export, so model at origin (DOC-5.x). Props sit with origin at base center; modular pieces at a snap corner.
- Apply rotation and scale in Blender (Ctrl+A > All Transforms) before export; scale must read 1,1,1.
- Triangulated, no n-gons, no loose verts, no zero-area faces, no non-manifold geometry unless intentional.
- One UV map for textures (UV0). Second UV map for lightmaps only if baked lighting is used.
- Material slots in intentional order, one per material.

Skeletal mesh:
- One armature, root bone named `root` at origin, bone count under 256 per section for GPU skinning limits (COMMUNITY: keep under 75 for game characters).
- Max 4 bone influences per vertex unless the Unreal project enables 8 (COMMUNITY; UNVERIFIED for 5.8 default). Normalize weights.
- Armature at scale 1, rotation 0, mesh parented with Armature modifier. Apply scale on both before skinning.
- Rest pose = T-pose or A-pose, consistent across characters that will share animations.
- Shape keys export as morph targets. Nanite does not support morph targets (DOC-5.x).
- Import with Skeleton field set to an existing skeleton to share animation, or empty to create one named `<Mesh>_Skeleton`. Rename to `SKEL_...`.
- Check Create Physics Asset on first import (DOC-5.x); edit capsules after.

---

## 5. Collision

Priority order:
1. Primitive/convex custom collision (UBX/UCP/USP/UCX) in the FBX. Cheapest at runtime, most predictable.
2. Auto Generate Collision at import (DOC-5.x: skipped when the FBX already has custom collision).
3. Static Mesh Editor > Collision menu: add Simplified Box/Sphere/Capsule, or Auto Convex Collision with hull count 4 to 8 for props.
4. Complex-as-simple only for walkable floors and level geometry that must trace per-triangle. Costs memory and CPU.

Nanite meshes: collision is not generated from Nanite clusters. A Nanite mesh still needs UCX or auto collision (COMMUNITY). Nanite also keeps a fallback mesh for ray tracing; Fallback Relative Error controls its fidelity (DOC-5.x).

---

## 6. LODs and Nanite

Decision table:

| Asset | Use Nanite? | Use classic LODs? |
|---|---|---|
| Static opaque or masked mesh over about 2,000 triangles | Yes | No (Nanite handles it) |
| Tiny prop under 500 triangles | Optional, usually no | Single LOD is fine |
| Skeletal mesh (character, creature) | Possible: skeletal Nanite exists in 5.8 (the Nanite doc shows a Nanite Settings section on skeletal meshes, DOC-5.x; 5.8 notes fix outlines for Nanite skeletal meshes, VERIFIED-5.8). Default to classic LODs unless a test shows a win. | Yes, 3 to 4 LODs |
| Translucent / glass / water surface | No: Nanite supports only Opaque and Masked blend modes (DOC-5.x) | Yes |
| Mesh with morph targets | No (DOC-5.x) | Yes |
| Mesh using Custom expression nodes or heavy World Position Offset | Avoid (DOC-5.x) | Yes |
| Decals mesh | No | Yes |

Settings when enabling Nanite: on the Static Mesh, tick Enable Nanite Support (Build Nanite at import is not documented on the checked page, UNVERIFIED label). Keep Fallback Relative Error at default; lower it only if hardware ray tracing is in use. Source meshes can be dense (hundreds of thousands of triangles) but Zac's 8 GB VRAM budget makes memory the limit: check Nanite disk size in the Static Mesh Editor stats.

Classic LOD targets (COMMUNITY): LOD0 100%, LOD1 50%, LOD2 25%, LOD3 10%; screen sizes 1.0, 0.5, 0.25, 0.1. Generate in Unreal (Static Mesh Editor > LOD Settings > Number of LODs) or supply from Blender.

---

## 7. UVs and lighting

- Zac's projects use Lumen (dynamic GI). Lumen needs no lightmap UVs; `r.AllowStaticLighting=False` is the 5.8 Blank template default (VERIFIED-5.8). Leave Generate Lightmap UVs off for Lumen-only projects.
- Lumen does need clean, closed, reasonably thick geometry and valid Mesh Distance Fields. Thin walls under about 10 cm and open meshes leak light (COMMUNITY). Keep Generate Mesh Distance Fields on in Project Settings.
- If a project switches to baked lighting later: UV1 non-overlapping, 0 to 1 space, 2 to 4 pixel padding, or tick Generate Lightmap UVs at import.
- UV0 texel density: pick one target (for example 10.24 px/cm = 1024 px per 100 cm for hero props, 5.12 for background) and keep it across the project.
- Keep UV islands inside 0 to 1 unless tiling is intentional; mirrored islands break normal maps.

---

## 8. Materials and textures

Texture import rules (COMMUNITY unless noted):

| Map | sRGB | Compression | Notes |
|---|---|---|---|
| Base color (`_BC`) | on | Default (BC1/DXT1; BC3 with alpha) | |
| Normal (`_N`) | off | Normalmap (TC_Normalmap) | Blender exports OpenGL (Y+); Unreal wants DirectX (Y-). Flip the green channel: in the texture editor tick Flip Green Channel, or invert G in Blender before saving. |
| ORM (`_ORM`) | off | Masks (no sRGB) | R = ambient occlusion, G = roughness, B = metallic. Pack in Blender compositor or an image tool; pack linear data as non-color. |
| Roughness, metallic, AO alone | off | Grayscale or Masks | |
| Emissive | on | Default | |
| Height | off | Grayscale / Displacement | |

- Power-of-two sizes where possible (512, 1024, 2048, 4096). Non-power-of-two does not stream or mip. Hero prop 2048, background 1024, character body 4096 max on 8 GB VRAM. Use Texture Group `World` or `Character` as appropriate.
- Use PNG or TGA 8-bit for color, 16-bit PNG/EXR only for height.
- Put textures beside the mesh in `/Textures`; do not rely on FBX embedded media.
- Make one master material (`M_Master_Opaque`) with texture parameters and static switches; every asset gets a `MI_` instance. Do not import a unique full material per asset.
- Interchange glTF import builds instances from `/InterchangeAssets/gltf/MaterialInstances/` (VERIFIED-5.8 config, e.g. `MI_Default_Opaque`, `MI_Default_Mask`, `MI_Default_Blend`).
- Material import choice in the dialog: Import as Materials, Import as Material Instances, or Do Not Import. The enum `EInterchangeMaterialImportOption` has a "DoNotImport"/"ImportAsMaterials" rename in 5.x (VERIFIED-5.8 DefaultInterchange.ini). Prefer Do Not Import for FBX and assign `MI_` instances by hand or script.

---

## 9. Skeleton and animation retargeting (IK Rig, IK Retargeter)

Plugin `IKRig` is enabled by default in 5.8 (VERIFIED-5.8). Workflow (DOC-5.x):
1. Create an IK Rig asset for the source skeletal mesh (`Rig_<Name>`, Epic prefix `Rig_`). Set the Retarget Root (pelvis), add a Retarget Chain for spine, head, each arm, each leg, fingers, tail.
2. Same for the target mesh. Chain names must match between rigs where the chains correspond.
3. Create an IK Retargeter asset (right-click > Animation > IK Retargeter), pick source and target rigs.
4. In the retargeter, match poses: T-pose vs A-pose differences are fixed by editing the retarget pose on the target, not by editing the mesh.
5. Export animations from the retargeter into `AS_` assets in `/Animations`.
Checks: feet planted (no ice skating), no arm penetration, scale compensation on pelvis for different proportions. Creatures with non-human skeletons need custom chains; test with a walk cycle and an idle.

---

## 10. Folder structure

```
/Game
  /Art
    /Characters/<Name>/{Meshes,Materials,Textures,Animations,Rigs}
    /Props/<Category>/<Name>/{Meshes,Materials,Textures}
    /Environments/<Biome>/{Meshes,Materials,Textures}
    /Materials/Master   (M_Master_*)
    /Materials/Instances (shared MI_)
    /FX
  /Cinematics/{Sequences,Renders}   (LS_*, movie render presets)
  /Maps               (L_*, test and final)
  /Developers/<name>  (scratch; excluded from audits)
  /Collections        (virtual: Review, Approved)
```
Epic's naming page gives no folder rules (checked); this layout is COMMUNITY. Keep names Pascal_Case, no spaces, no special characters. Never rename or move assets with the editor closed; use editor Rename or "Fix Up Redirectors".

---

## 11. Step-by-step import checklist

Blender side (also see the `blender-asset-quality` skill):
- [ ] Object origin at intended pivot, rotation applied, scale 1,1,1.
- [ ] Dimensions in meters sensible (print `obj.dimensions`).
- [ ] Triangulated or exporter set to triangulate. No n-gons, no loose geometry.
- [ ] Normals checked (Face Orientation overlay all blue). Custom normals only if intended.
- [ ] UV0 inside 0 to 1, no overlap unless mirrored on purpose.
- [ ] Names follow section 3; no `.001`.
- [ ] Collision hulls named `UCX_<Mesh>_##`, parented or in the same export selection.
- [ ] Exported with the section 2 settings to `_Incoming`.
- [ ] Textures exported linear/sRGB correctly, ORM packed, normal map OpenGL noted.

Unreal side:
- [ ] Project has Interchange plugin enabled and DataValidation enabled (both default-on in 5.8, VERIFIED-5.8).
- [ ] Import into `/Game/Art/.../Meshes` via Content Browser > Import, or Python (section 12).
- [ ] Dialog: Convert Scene on, Convert Scene Unit on, Import Uniform Scale 1.0, materials per section 8, Import Mesh LODs as needed, skeleton chosen for skeletal.
- [ ] Open the asset. Check bounds in the mesh details: size in cm matches Blender size x 100.
- [ ] Check collision (Show > Collision), pivot gizmo, normals, UV channel 0.
- [ ] Assign `MI_` instance, fix texture sRGB/compression flags.
- [ ] Nanite decision per section 6.
- [ ] Rename to prefixes, move to final folder, Fix Up Redirectors.
- [ ] Right-click folder > Asset Actions > Validate Assets (Data Validation), zero errors.
- [ ] Drop into a test map under a neutral light, screenshot at 3 angles.
- [ ] Save all. Log: source file, importer used, triangles, bounds, texture list, warnings.

---

## 12. Validation and audit

- Data Validation plugin (`DataValidation`, default-on, VERIFIED-5.8): Content Browser folder right-click > Asset Actions > Validate Assets, or menu Tools > Validate Data. Add project rules in Project Settings > Editor > Data Validation. Release notes mention a data validation fixer fix in 5.8 (VERIFIED-5.8).
- Asset Audit: Window > Developer Tools > Asset Audit (Asset Manager Editor plugin, present in 5.8, VERIFIED-5.8) for size and reference checks. Window labels UNVERIFIED for 5.8; use Size Map (right-click asset > Size Map) as fallback.
- Reference Viewer (right-click > Reference Viewer) finds orphan and duplicate textures.
- Stats to record per asset: triangles at LOD0, Nanite on/off, material slots, texture memory (MB), collision type.

---

## 13. Python automation (high level)

Enable Python Editor Script Plugin (Edit > Plugins > Scripting) and Editor Scripting Utilities, restart; the plugin must be enabled per project (DOC-5.x). Plugin `PythonScriptPlugin` is `EnabledByDefault: false` in 5.8 (VERIFIED-5.8).

Import example (Interchange or legacy; `unreal.AssetImportTask` is the long-standing API, DOC-5.x):

```python
import unreal

def import_fbx(src, dest_path):
    task = unreal.AssetImportTask()
    task.filename = src
    task.destination_path = dest_path      # e.g. "/Game/Art/Props/Crate/Meshes"
    task.automated = True                  # no dialog
    task.save = True
    task.replace_existing = True
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks([task])
    return task.imported_object_paths

print(import_fbx(r"D:\Unreal Projects\_Incoming\SM_Crate.fbx", "/Game/Art/Props/Crate/Meshes"))
```
For FBX specifics set `task.options = unreal.FbxImportUI()` and fields such as `import_mesh`, `import_as_skeletal`, `static_mesh_import_data.combine_meshes`. Interchange scripting classes are `unreal.InterchangeManager` and pipeline assets; exact 5.8 call shapes: UNVERIFIED, check with `dir(unreal)` in a throwaway session.

Validation in Python: `unreal.EditorValidatorSubsystem` exists in 5.x (UNVERIFIED for method names in 5.8).

Headless runs (DOC-5.x, flags confirmed in 5.8 source for `-ExecutePythonScript=`):
```
"D:\Epic\UE_5.8\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" "D:\Unreal Projects\<P>\<P>.uproject" -ExecutePythonScript="D:\WKP\scratch\import_job.py" -unattended -nosplash
"D:\Epic\UE_5.8\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" "D:\Unreal Projects\<P>\<P>.uproject" -run=pythonscript -script="D:\WKP\scratch\import_job.py" -unattended
```
`-run=pythonscript` is the commandlet form: fast, no levels loaded automatically. Both shut the editor down when the script ends. Do not run either until the caller approves launching the editor. Epic warns not to run `py` through `-ExecCmds` because it can run before the editor is ready. Batch from script: `BatchProcessLibrary::RunBatch` (VERIFIED-5.8 release notes). See the `ue-mcp-and-automation` skill for ports and risk.

---

## 14. Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Mesh 100x too small or large | Unit mismatch (Blender meters vs Unreal cm) | Re-import with Convert Scene Unit on; or Apply Scalings = FBX Units Scale in Blender; or set Import Uniform Scale 100 as a last resort and note it. |
| Mesh rotated 90 degrees, lying on its side | Wrong Forward/Up on export | Forward -Y, Up Z; apply rotations in Blender; for characters toggle Force Front X Axis. |
| Character faces sideways | Blender front is -Y, Unreal forward is +X | Rotate armature+mesh 90 degrees around Z in Blender, apply, re-export. Do not rotate in Unreal. |
| Flipped or inside-out faces | Negative scale (mirrored), or flipped normals | Blender: Mesh > Normals > Recalculate Outside; apply scale; avoid negative scale. |
| Faceted or wrong shading | Normals not exported or recomputed | Export Smoothing = Face; set Normal Import Method = Import Normals or Import Normals and Tangents. |
| Black material | Missing texture, wrong Blend Mode, texture compressed wrong, or Lumen/Distance Field issue | Check texture slot, sRGB flags, assign a `MI_`; for glTF use correct parent instance. |
| Missing textures | Textures not exported or Path Mode not Copy | Export textures to disk, import manually into `/Textures`, reassign. |
| Normal map looks inverted | Green channel convention | Flip Green Channel on the texture. |
| Wrong pivot | Origin not at base; Transform Vertex to Absolute on | Set origin in Blender before export; keep Transform Vertex to Absolute off; Bake Pivot in Vertex only when needed (DOC-5.x). |
| Light leaking indoors with Lumen | Thin or open walls, no distance field | Thicken walls, close meshes, enable Generate Mesh Distance Fields. |
| Collision missing | UCX name did not match render mesh | Name must be `UCX_<RenderMeshName>_##` exactly. |
| Nanite mesh renders wrong or fallback visible | Translucent material or morph targets | Turn Nanite off for that mesh. |
| Animation twisted or arms collapse | Bone roll/pose mismatch, Add Leaf Bones on | Re-export with Add Leaf Bones off, same rest pose, use IK Retargeter pose editing. |
| Import dialog never appears | Automated task or Interchange setting | Expected for `task.automated = True`; otherwise check Interchange plugin enabled. |

---

## 15. Output report format (return to caller)

```
ASSET: SM_Crate_Wooden_01
Importer: Interchange | legacy (as observed)
Bounds (cm): X Y Z   Tris LOD0: N   Nanite: yes/no
Collision: UCX (n hulls) | auto | complex
Textures: list with sizes and flags
Validation: pass/fail with messages
Files: source .blend, FBX path, Unreal path
UNVERIFIED items hit this run: ...
```
