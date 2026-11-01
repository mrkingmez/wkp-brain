# References: blender-asset-quality

Fetched or searched 2026-10-31. docs.blender.org returned HTTP 403 to the fetch tool, so Blender facts were verified against the live Blender 5.2.4 Python API (headless run of C:\Blender\5.2.4\blender.exe, separate process, Zac's scene untouched) rather than manual text.

Verified by live API (5.2.4): Mesh.use_auto_smooth and calc_normals_split removed; shade_smooth_by_angle args; sharp_face attribute; Principled BSDF input names; modifier property names (Bevel, WeightedNormal, Skin); operator argument lists for transform_apply, pack_islands, smart_project, orphans_purge, export_scene.fbx, export_scene.gltf; Material.use_nodes deprecation warning (removal in 6.0).

Sources
- https://dev.epicgames.com/documentation/en-us/unreal-engine/importing-static-meshes-in-unreal-engine (1 UU = 1 cm, FBX recommended)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-skeletal-mesh-pipeline-in-unreal-engine (root bone pivot, triangulated meshes, FBX 2020.2)
- https://dev.epicgames.com/documentation/unreal-engine/fbx-static-mesh-pipeline-in-unreal-engine (UCX_ collision, LODs, smoothing groups; only a French copy read, English wording UNVERIFIED)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/python-api/class/FbxStaticMeshImportData?application_version=5.2 (collision, MikkTSpace, LOD import flags)
- https://projects.blender.org/blender/blender/issues/119633 (Auto Smooth vs Smooth by Angle)
- https://projects.blender.org/blender/blender/issues/116922 (autosmooth 4.1 workflow regression)
- https://blenderartists.org/t/blender-4-1-auto-smooth-is-now-a-modifier-only/1488922 (4.1 change, runs before stack)
- https://docs.blender.org/manual/en/dev/modeling/modifiers/generate/skin.html (Armature below Skin; seen via search snippet)
- https://polyhaven.com/license (CC0)

UNVERIFIED (community practice, not read on an official page)
- Triangle budget table, LOD ratios, padding pixels per resolution, texel density targets.
- SM_/SK_/T_/M_/MI_ naming and _BC/_N/_ORM suffixes (widely used Unreal community style, not one official page).
- Normal map green channel convention for UE (DirectX, green down) and the exact name of UE's flip option.
- Lightmap UV auto-generation default on UE 5 import.
- `_LOD0` suffix and `UCX_` rules in Epic's English docs.
