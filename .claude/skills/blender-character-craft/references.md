# References: blender-character-craft

Searched/fetched 2026-10-31. docs.blender.org blocked the fetch tool (HTTP 403), so Blender behaviour was checked against live Blender 5.2.4 (headless, separate process).

Verified live (5.2.4): SKIN modifier props; `mesh.skin_vertices[i].data[j]` fields radius/use_root/use_loose; ops skin_root_mark, skin_armature_create; Rigify module present in scripts/addons_core and ops armature_human_metarig_add, pose.rigify_generate after enable; hair curve ops curves_empty_hair_add, curves.convert_from_particle_system; parent_set enum values; vertex_group_limit_total and normalize ops.

Sources
- https://docs.blender.org/manual/en/dev/modeling/modifiers/generate/skin.html (Skin modifier: root, loose, Armature below Skin; via search snippet)
- https://docs.blender.org/manual/en/latest/addons/rigging/rigify (Rigify bundled, enable under Add-ons; via search snippet)
- https://docs.blender.org/manual/de/5.0/addons/rigging/rigify/introduction.html (5.0 enable steps)
- https://dev.epicgames.com/documentation/en-us/unreal-engine/fbx-skeletal-mesh-pipeline-in-unreal-engine (root bone, triangulation)

UNVERIFIED
- Proportion numbers, head-count rules, finger ratios, digitigrade guidance (general anatomy and character-art practice).
- Fur strand counts, card counts, Unreal groom via Alembic workflow.
- Which Rigify metarigs ship in 5.2.
- Quadriflow quality; Quad Remesher is a paid third-party tool and was not evaluated.
- Every AI image-to-3D provider's licence and pricing: not read.
- Rigify enabling in the GUI (background enable failed with a preferences KeyError).
