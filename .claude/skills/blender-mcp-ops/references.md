# References: blender-mcp-ops

Evidence base 2026-10-31:
- The blender MCP tool descriptions and server instructions in the Claude session (get_addon_status, get_scene_info, execute_blender_code, look, search_assets, import_asset). Marked TOOL DOC in the skill.
- Headless runs of C:\Blender\5.2.4\blender.exe (`-b --factory-startup --python`), a separate process that never touched Zac's open session or files. Probe scripts were in D:\WKP\scratch\bl\.
- The live MCP connection to Zac's GUI Blender was unreachable during this work (addon handshake: "Connection to Blender lost [WinError 10053]"; later calls: "Not connected to Blender"; only the blender-mcp process was alive). So `look`, `get_addon_status` fields, and the live scene could NOT be tested. Zac's scene was therefore not touched.

Verified headless in 5.2.4
- Scene creation and removal pattern, per-scene camera, new scene has no world.
- Render engine assign TypeError lists ('BLENDER_EEVEE', 'BLENDER_WORKBENCH', 'CYCLES'); enum_items read returned only BLENDER_EEVEE.
- New materials have a node_tree; Material.use_nodes deprecated, removal in 6.0.
- Operator argument names: transform_apply (isolate_users), shade_smooth_by_angle, orphans_purge, parent_set type enum, export_scene.fbx, pack_islands, smart_project.

UNVERIFIED
- `look` behaviour (Render Result image, camera mode on a hijacked camera).
- save_as_mainfile `copy=True` argument in 5.2.4 (standard in Blender, argument list not printed).
- Cycles OptiX enabling sequence, viewport triangle comfort limit.
- Which library needs an API key (Sketchfab token suspected).

Docs
- https://docs.blender.org/api/current/ (Python API reference; the fetch tool received HTTP 403 so it was not read directly)
- https://docs.blender.org/manual/en/dev/modeling/modifiers/generate/skin.html (seen via search snippet)
