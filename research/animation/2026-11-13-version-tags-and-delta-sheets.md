# Version tags and delta sheets for the six approved tutorials

Date 2026-11-13. Made by animation-director for Zac. Our versions: Blender 5.2.4 (LTS release candidate build, C:\Blender\5.2.4), Unreal 5.8.4.
Notes are in our own words. The caption files are third-party text kept for private study in `D:\WKP\research\animation\transcripts\<id>\` (gitignored). Nothing here copies their wording.

## 0. What was and was not checked (read first)

- **Blender live link was DOWN.** `get_addon_status` and `get_scene_info` both returned "Could not connect to Blender. Make sure the Blender addon is running." So the blender MCP could not be used and Zac's open Blender was not touched. Per `blender-mcp-ops` rule 6, all Blender checks were run in a SEPARATE headless Blender 5.2.4 (`C:\Blender\5.2.4\blender.exe -b --factory-startup`) on throwaway data. It never opened any of Zac's .blend files and saved nothing.
- **What headless can prove:** that an operator, modifier, node input, property, enum value or bundled asset exists in 5.2.4, and what its default is. **What it cannot prove:** menu paths and keyboard shortcuts (no UI, and the keymap list is empty in background mode). Every row below names the check type. A row marked PASS (API) means the thing exists and works by that name. A UI path taken from release notes or from the tutorial itself is marked UI-UNVERIFIED.
- **Unreal: docs only.** No Unreal Editor was opened. Sources are Epic's release notes for 5.5 to 5.8 and the 5.8 docs pages, fetched from dev.epicgames.com on 2026-11-13. Anything not found there is UNVERIFIED.
- **H1 captions are missing.** YouTube answered HTTP 429 (Too Many Requests) for the H1 caption file on five tries over about 10 minutes while the other five files downloaded fine. I did not rotate clients or use workarounds to get past the rate limit. H1's delta sheet is therefore built from its chapter list, description and the release notes, and is flagged chapter-level only. Retry later with the same command, no change needed.
- **Not processed, on purpose:** S1 (Ryan King Art sculpting) and R1 (Ryan King Art retopology), the TOP picks for those topics, were not on Zac's yes list. Zac can add them. Also not processed: L2, L3, R2, H2, B2, B3, U2 is approved and is processed.

Sources for Blender deltas (all fetched 2026-11-13 from the Blender developer docs repo, raw markdown): `https://projects.blender.org/blender/blender-developer-docs/raw/branch/main/docs/release_notes/<version>/<page>.md` for versions 4.3, 4.4, 4.5, 5.0, 5.1, 5.2, pages index, sculpt, modeling, user_interface, rendering, compositor, core, eevee, assets. Published form: `https://developer.blender.org/docs/release_notes/<version>/`.
Sources for Unreal: `https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-5-8-release-notes?application_version=5.8` (and the same slug for 5-7, 5-6, 5-5), `.../mesh-terrain-in-unreal-engine`, `.../accessing-mesh-terrain-in-unreal-engine`, `.../crafting-mesh-terrain-in-unreal-engine`, `.../mesh-terrain-material-in-unreal-engine`, `.../lumen-global-illumination-and-reflections-in-unreal-engine`, all with `?application_version=5.8`.

Release dates read from the Blender notes: 4.3 on 2024-11-19, 4.4 on 2025-03-18, 4.5 LTS on 2025-07-15, 5.0 on 2025-11-18, 5.1 on 2026-03-17, 5.2 LTS on 2026-07-14.

## 1. Version tag blocks

### S2 Master Blender Sculpting: Every Brush Explained (Grant Abbitt) `5-mNgCpEkCI`
- Software: Blender. Version STATED: 4.3.1. Evidence: the speaker says the video covers the new brushes in 4.3 (caption 00:00:07) and "I'm in Blender 4.3.1" (00:00:18). The description says "latest Blender version" only.
- Uploaded 2024-12-20. Length 43:40. Captions: English auto-generated, saved.
- Ours: Blender 5.2.4. Gap: 5 releases (4.4, 4.5 LTS, 5.0, 5.1, 5.2) and one major boundary (4 to 5). Gap size: LARGE for UI and brush settings, small for brush behavior.

### L1 Mesh Terrain tutorial (Unreal Sensei) `Lhj2LutYNjA`
- Software: Unreal Engine. Version STATED: 5.8 Preview build. Evidence: speaker says the tutorial works only on 5.8 because Mesh Terrain was introduced there, and that he is using the preview build of 5.8 (caption 00:01:31 to 00:01:42), and that he uses a newer plugin build than the preview, so people on the preview will see a different material (about 00:06:17).
- Uploaded 2026-06-10. Length 1:06:18. Captions: English auto-generated, saved.
- Ours: Unreal 5.8.4 (release). Gap: Preview to release to four hotfix levels. The feature is labelled Experimental in Epic's 5.8 notes, so behavior and names are allowed to move. Gap size: UNKNOWN to SMALL, cannot be measured without opening the editor.

### H1 Stylized Low Poly Wooden Cabin (Ryan King Art) `11sC54-pq_0`
- Software: Blender. Version NOT STATED in the title or description (description read from the live page, it lists project-file stores and a forest tutorial link, no version). INFERRED 4.3. Evidence: upload date 2025-01-30, Blender 4.3 was the current stable release then (released 2024-11-19) and 4.4 did not exist until 2025-03-18. A 4.2 LTS user is also possible, so treat it as 4.2 or 4.3.
- Uploaded 2025-01-30. Length 29:12. Chapters: Intro 0:00, Modeling Cabin 0:28, Door 5:27, Roof 10:34, Lantern 16:19, Materials 18:24, Closing 27:57. Captions: auto-generated track exists, NOT saved (HTTP 429, see section 0).
- Ours: Blender 5.2.4. Gap: 4.4, 4.5, 5.0, 5.1, 5.2 (plus 4.3 if it was made in 4.2).

### B1 How to make a private jet in Blender (Blender Guru) `4wxmKLDhsnQ`
- Software: Blender. Version STATED by the speaker as 5.2 or newer. Evidence: at 02:14:51 he says "as of Blender 5.2" the Principled BSDF has a new Thin Wall option, and uses it. Blender's own 5.2 notes confirm Thin Wall is new in 5.2 (rendering.md, "Thin Wall"). The title and description do not give a number. The Blender Guru post (read on 2026-11-05) also gave none.
- Uploaded 2026-10-17. Length 3:23:39. Captions: English auto-generated, saved (about 5,576 lines).
- Ours: 5.2.4. Gap: NONE at minor level. Patch level unknown (5.2.0 to 5.2.x). Gap size: NEGLIGIBLE.

### U1 Unreal Engine 5 Beginner Tutorial 2026 (Unreal Sensei) `e83pKSlfGR0`
- Software: Unreal Engine. Version STATED: 5.8 in the description, and "Unreal Engine 5.8.3" in the captions at 02:41:57.
- Uploaded 2026-10-19. Length 5:50:18. Chapters used: Lighting with Lumen 35:58, Archviz Lighting 50:36, Import/Create a Static Mesh 1:36:52, Landscape Sculpting 1:56:50, Landscape Material 2:08:16, Foliage Paint 2:38:18, Nanite 2:49:32. Captions: English auto-generated, saved (about 8,990 lines, whole course; study only the chapters).
- Ours: 5.8.4. Gap: one patch release (5.8.3 to 5.8.4). Hotfix contents NOT checked, UNVERIFIED. Gap size: NEGLIGIBLE.

### U2 Lighting in Unreal Engine 5 for Beginners (William Faucher) `fSbBsXbjxPo`
- Software: Unreal Engine. Version NOT STATED as a number. INFERRED UE 5.0 era. Evidence: says "Lumen and UE5" (00:00:27), project settings screen shows Virtual Shadow Maps labelled Beta (00:02:28), upload 2022-06-10. Epic's UE 5.0 release date is from my memory (April 2022), UNVERIFIED here.
- Uploaded 2022-06-10. Length 44:43. Captions: English auto-generated, saved.
- Ours: 5.8.4. Gap: eight minor releases (5.1 through 5.8). Gap size: LARGE. Use for light principles only.

## 2. Delta sheets

Status key: PASS = works as shown. CHANGED = differs, new path or behavior given. NEW = feature that did not exist when the video was made. DOCS = verified in docs only. API = verified headless in Blender 5.2.4. UI-UNVERIFIED = a menu path or shortcut we could not click.

### 2.1 S2 delta sheet, Blender 4.3.1 to 5.2.4

| # | Tutorial step | Status | What is true in 5.2.4 | Evidence |
|---|---|---|---|---|
| 1 | Delete cube, Add > Mesh > Ico Sphere, raise Subdivisions to 6 in the Adjust Last Operation panel | PASS (API) | `mesh.primitive_ico_sphere_add` has `subdivisions` (default 2) and `radius` (default 1 m) | headless |
| 2 | Open the Sculpting workspace tab | PASS (API) | Workspace named "Sculpting" exists | headless |
| 3 | Brush picker along the bottom, set rows, icon size, show names | CHANGED, UI-UNVERIFIED | It is the Asset Shelf. 5.0 gave the shelf one global style and 5.1 added thumbnail size options. Brushes are assets from the bundled Essentials library | 5.0 and 5.1 UI notes, 64 brush assets (including paint and texture brushes shipped in that file) found in `essentials_brushes-mesh_sculpt.blend` |
| 4 | Brush radius with F, strength with Shift+F, radius and strength fields | CHANGED (value meaning), keys UI-UNVERIFIED | Brush Size is now a DIAMETER, not a radius (5.0). The same number gives a brush twice as wide as the old Radius field. Properties `size`, `unprojected_size`, `strength` exist | 5.0 sculpt notes, headless |
| 5 | Negative direction with the +/- toggle and Ctrl to invert | PASS (API), keys UI-UNVERIFIED | `Brush.direction` exists | headless |
| 6 | Add detail with Remesh: Voxel Size field and Remesh button, Ctrl+R to remesh, R to resize the voxel | PASS (API), keys UI-UNVERIFIED | `object.voxel_remesh`, `object.voxel_size_edit` and `Mesh.remesh_voxel_size` exist. NOTE the operator lives under `object`, not `sculpt`. 5.2 now interpolates vertex colors across remesh instead of scrambling them | headless, 5.2 sculpt notes |
| 7 | Dyntopo toggle | PASS (API) | `sculpt.dynamic_topology_toggle` exists. 5.2 removed the confirmation prompt when re-entering sculpt mode with Dyntopo on | headless, 5.2 sculpt notes |
| 8 | Chapter list of brushes (draw, clay, crease, inflate, layer, fill, flatten, plateau, scrape, trim, grab, snake hook, elastic, nudge, pinch, pull, relax, thumb, twist, pose, boundary, density, mask, cloth) | PASS for most (API) | Every chapter brush has a same-named asset except the renamed ones in row 9 | headless asset list |
| 9 | "Crease", "Flatten Contour", "Scrape Fill", "Fill/Deepen" | CHANGED | Assets are now "Crease Polish" and "Crease Sharp", "Flatten/Contrast", "Scrape/Fill", "Fill/Deepen". Brush TYPE list has a single PLANE type (added 4.4) that covers flatten, fill and scrape, with no separate FLATTEN, FILL or SCRAPE types left. One asset name has a trailing space, "Grab Planar Cloth " | headless enum and asset list, 4.4 sculpt notes |
| 10 | Brushes the video predates | NEW | Plane brush type (4.4), Blur brush (5.1), Scene Project brush (5.2), Airbrush, Sharpen and Smear assets are in the bundle. Mask by Color operator (4.5, `sculpt.mask_by_color`) | release notes, headless |
| 11 | Cloth brushes: Persistent and simulation area | CHANGED | Cloth brushes default to Persistent OFF, and Grab Cloth and Grab Random Cloth default to Local simulation area (both 4.4). Re-test the tutorial's cloth pitfalls, they may not reproduce | 4.4 sculpt notes |
| 12 | Mask brush, face sets, mask tools | PASS (API) with changes | `paint.mask_flood_fill`, `sculpt.mask_filter`, `sculpt.face_sets_create`, `sculpt.expand` exist. 5.1 adds Alt+LMB to toggle the Mask asset temporarily and Ctrl+Alt+LMB to erase mask. Face set and mask overlays now warn when hidden | 5.1 sculpt notes, headless |
| 13 | Multires: erase and smear displacement, subdivide | PASS (API) | Modifier `MULTIRES` with `levels`, `sculpt_levels`, `render_levels`, `total_levels`. 5.0 adds Conform Base next to Apply Base | headless, 5.0 sculpt notes |
| 14 | Trim tools and Boolean solvers | CHANGED | Boolean solver enum is now FLOAT, EXACT, MANIFOLD. "Fast" was renamed "Float" in 5.0, Manifold arrived in 4.5 and works in sculpt trim, but needs a manifold mesh | headless, 4.5 and 5.0 notes |
| 15 | Pen pressure toggles on Grab, Snake Hook, Pose, Boundary, Thumb, Rotate | CHANGED | Those toggles were removed (5.0). Size, strength and jitter now take a pressure curve with presets. 4.5 adds Tilt Factor on Draw, Draw Sharp, Plane, Clay Strips | 4.5 and 5.0 notes |
| 16 | Unified size and strength shared across the scene | CHANGED | Unified brush settings are now per mode, held on the paint settings (`Sculpt.unified_paint_settings` exists). Radial symmetry is stored on the mesh (`Mesh.radial_symmetry`), not the scene | 5.0 notes, headless |
| 17 | Frame the view on the last stroke | CHANGED | "Frame Selected" was renamed "Frame Last Stroke" in sculpt, vertex paint, weight paint and texture paint (4.4) | 4.4 sculpt notes |
| 18 | Retopology overlay offset | CHANGED | Default offset is now 0.01 m (was 0.2 m, 4.5). Read as 0.00999 in 5.2.4 | 4.5 modeling notes, headless |

Net for S2: every brush name in the video still resolves in 5.2.4 (row 9 maps the renamed ones), so the skill can use it as a reference. Do not teach numbers (brush sizes, remesh voxel values, strengths) from the video: size is now diameter and defaults moved.
Not verified: keyboard shortcuts and the visual look of the shelf (no UI in headless). The live check list is in section 4.

### 2.2 L1 delta sheet, Unreal 5.8 Preview to 5.8.4 (docs only)

| # | Tutorial step | Status | What the 5.8 docs say | Evidence |
|---|---|---|---|---|
| 1 | Use a blank Open World level, Mesh Terrain only works in World Partition levels | PASS (DOCS) | Epic: "You must use Mesh Partition in a World Partition level. When creating a new level make sure to select an Open World level." | crafting-mesh-terrain page |
| 2 | Enable two plugins, Mesh Partition and Mesh Terrain Mode, restart | CHANGED (DOCS) | Docs list FOUR: MeshPartition, MeshPartitionWater, PCG MeshPartition Interop and Mesh Terrain Mode. Only MeshPartition and Mesh Terrain Mode are needed for the video | accessing-mesh-terrain page |
| 3 | Mesh Terrain mode toolbar | CHANGED (DOCS) | Six tabs: Create, Edit, Modifiers, Sculpt, Paint, Shapes | accessing page |
| 4 | Create the base terrain | PASS (DOCS) | Create tab has Create Rectangle, Import Heightmap, Convert Mesh. Settings: size in cm, resolution in quads per axis, sections auto by max triangles or explicit layout | crafting page |
| 5 | Sculpt modifier and sculpt tools | PASS (DOCS) | A modifier must be selected first, then the Sculpt tab brushes work | crafting page |
| 6 | Remesh modifier | PASS (DOCS) | Remesh mode makes new uniform triangles, Tessellate mode subdivides existing ones and is usually faster. Main setting is Target Edge Length | crafting page |
| 7 | Texture modifier with adaptive tessellation | PASS (DOCS) | Texture modifiers have an Adaptive Tessellation option | crafting page |
| 8 | Spline and Boolean mesh modifiers | PASS (DOCS) | Spline remesh modifier and a Boolean section with Boolean Op are documented | crafting page |
| 9 | Sensei Terrain master material (from 23:36) | CHANGED, FREE-ONLY FLAG | It is SOLD by the creator (description link). Do not buy. Epic documents the free path: Mesh Partition Resource, Mesh Partition Channel Sample and related nodes in the Material graph, reading weight channels set in the Mesh Partition Definition. The first 23 minutes (basics, sculpt, remesh) need no purchased material | mesh-terrain-material page, video description |
| 10 | Paint material layers | CHANGED (DOCS) | Painting writes Weight Channels held on the mesh partition vertices and baked to a texture 2D array. Channels come from the Mesh Partition Definition asset | mesh-terrain-in-unreal-engine page |
| 11 | Convert any mesh into terrain (last chapter, 1:03:17) | PASS (DOCS) | Edit tab has a Convert tool, and Create tab has Convert Mesh. Settings include sections per side and which axes to split | crafting page |
| 12 | Preview vs release | UNVERIFIED | Speaker says his plugin build is newer than the 5.8 Preview and differs. We cannot tell what moved between his build and 5.8.4 without opening the editor | transcript 00:06:17 |

Flags: Mesh Terrain is Experimental per Epic's 5.8 notes ("Mesh Terrain (Experimental)"). Teaching it means enabling experimental plugins, which needs Zac's yes at the time of use. Nothing was enabled.

### 2.3 H1 delta sheet, Blender 4.2 or 4.3 to 5.2.4 (CHAPTER LEVEL ONLY, no captions)

| # | Chapter or step | Status | What is true in 5.2.4 | Evidence |
|---|---|---|---|---|
| 1 | Modeling cabin, door, roof: loop cut, extrude, inset, bevel, knife | PASS (API) | `mesh.loopcut_slide`, `extrude_region_move`, `inset`, `bevel`, `knife_tool`, `bridge_edge_loops` exist. 5.1 adds Ctrl snapping and Shift precision while beveling | headless, 5.1 modeling notes |
| 2 | Mirror modifier and Bevel modifier | PASS (API) | Mirror has `use_clip`, `use_mirror_merge`, `use_axis`. Bevel has `width`, `segments`, `limit_method` (NONE, ANGLE, WEIGHT, VGROUP), `harden_normals` | headless |
| 3 | Shading | PASS (API) | Mesh Auto Smooth is gone (since 4.1, before this video). `object.shade_auto_smooth` and `object.shade_smooth_by_angle` exist, `Mesh.use_auto_smooth` is absent | headless |
| 4 | Boolean cuts for windows or details, if used | CHANGED | Solver "Fast" is now "Float" (5.0). Manifold added in 4.5 | headless, 4.5 and 5.0 notes |
| 5 | Array for planks or roof tiles, if used | CHANGED | A new geometry-nodes Array modifier arrived in 5.0 and the old one remains for now. Which one the Add Modifier menu shows first is UI-UNVERIFIED | 5.0 modeling notes |
| 6 | Lantern: round shapes, loop tools | CHANGED, UNVERIFIED | 5.2 builds Circle ("To Circle"), Space ("Space Edge Loops Evenly") and Flatten in from the Loop Tools add-on. Whether the video uses Loop Tools is UNVERIFIED | 5.2 modeling notes |
| 7 | Materials | PASS (API) | Principled BSDF inputs in 5.2.4 include Base Color, Metallic, Roughness, Emission Color, Coat Weight, Thin Wall (new in 5.2). New materials already have a node tree | headless, `blender-mcp-ops` |
| 8 | UV unwrap, if shown | CHANGED | UV sync selection is on by default since 5.0, so selecting in the 3D view no longer pulls whole vertex UV sets. No UV chapter appears in the chapter list, so this may not apply | 5.0 modeling notes |
| 9 | Sold project files, store links | FLAG | Description sells the files on seven stores. Free-only: build it by following the video, do not buy | description |

Open until captions are pulled: exact tool order, any add-ons used, texture approach. The skill author must not rely on this table for step order.

### 2.4 B1 delta sheet, Blender 5.2 (stated) to 5.2.4

Version gap is negligible, so most steps PASS. The useful part is the list of items that depend on the maker's setup, not on version.

| # | Chapter or step | Status | What is true in 5.2.4 | Evidence |
|---|---|---|---|---|
| 1 | Snap to side view (Numpad 3), Shift+A, Image, Reference, import the blueprint (01:00 to 01:40) | PASS (API) | `object.empty_image_add` exists. Empty image options moved into an Image category in the Add menu in 5.0, which matches the video | headless, 5.0 UI notes |
| 2 | Show reference only in orthographic views | PASS (API) | `show_empty_image_perspective` and `show_empty_image_orthographic` exist | headless |
| 3 | Delete half, add Mirror from Generate (17:43 to 18:18), subdivision before mirror warning | PASS (API) | Modifier types MIRROR, SUBSURF exist, Subsurf has `levels`, `render_levels`, `quality`, `use_creases`, `use_limit_surface` | headless |
| 4 | Matcaps for seeing form (chapter "Improving visibility with Matcaps" at 26:20, and again at 2:54:32) | CHANGED | Bundled matcaps were updated and expanded in 5.0. 5.2.4 ships 27 including clay_studio, clay_warm, ceramic_dark, hard_surface_grey, resin. Matcap names on screen may differ from the video's | 5.0 UI notes, headless |
| 5 | Mean Bevel Weight on edges (1:32:40 to 1:33:00) | PASS (API) for the data, UI-UNVERIFIED for the panel | Edge bevel weight is a generic attribute `bevel_weight_edge` (the old edge property is gone). Bevel modifier Limit Method Weight exists | headless |
| 6 | Crease to 1 on edges for subdivision (2:54) | PASS (API) | Attribute `crease_edge` exists, Subsurf `use_creases` exists | headless |
| 7 | Solidify for panels, glass and seals | PASS (API) | Modifier type SOLIDIFY exists | headless |
| 8 | "The Solution to Panels" base mesh plus details mesh | PASS | Method, not UI. Depends only on modifiers listed above | transcript chapter 50:35 |
| 9 | Glass with Thin Wall (2:14:51) | PASS (API) | Principled BSDF has the boolean input "Thin Wall" in 5.2.4. Confirmed new in 5.2 | headless, 5.2 rendering notes |
| 10 | UV unwrapping (1:41:05 chapter) | CHANGED | UV sync selection default ON since 5.0 and a shared selection across UV maps. The video, made in 5.2, already shows the new behavior, so no gap for this video | 5.0 modeling notes |
| 11 | Painting in Photoshop (1:53:47) | FLAG | Photoshop is paid software and the department cannot drive it. Teach the method with Blender Texture Paint instead, or Zac does that step | description, `STANDARDS.md` rule on free tools |
| 12 | Downloads (aerial HDRIs, finished jet.blend, blueprints, PureRef board) | FLAG | HDRIs and the finished file are on poliigon.com, blueprints on Google Drive. Licenses not read. Must be read and logged in `animation-asset-log.csv` before use | description |
| 13 | Rivets by duplicating a detail piece with Shift+D (2:59:23) | NEW option | 5.0 added Array, Scatter on Surface and Instance on Elements modifiers that can place rivets. The tutorial's manual method still works | 5.0 modeling notes |
| 14 | Glare in the compositor (3:19:09) | CHANGED | Compositor trees now live on `scene.compositing_node_group`, and `Scene.use_nodes` no longer applies (5.0 rewrite). The Glare node got a Sun Beams mode, a Kernel option and higher Low and Medium quality in 5.0. The video is 5.2-era so it already shows this | 5.0 compositor notes, headless |
| 15 | Length and scope | FLAG | 3 h 24 min, 33 chapters. Use chapters 0:42 to 0:53:00 (blueprint, silhouette block, mirror and subdivision logic), 50:35 (panels solution), 1:32 (bevel weight) and 2:54 (crease). Skip the jet-only chapters | chapter list |

### 2.5 U1 delta sheet, Unreal 5.8.3 to 5.8.4, used for the classic route (docs only)

Gap is one patch. Hotfix notes were not read, UNVERIFIED. The useful deltas are the items later than the tutorial's own era and the Zac-rule flags.

| # | Chapter | Status | Notes | Evidence |
|---|---|---|---|---|
| 1 | Lighting with Lumen (35:58), Archviz lighting (50:36) | PASS (DOCS) | New projects have Lumen GI and Reflections, Generate Mesh Distance Fields and Support Hardware Ray Tracing ON by default. Lumen is set under Project Settings, Engine, Rendering, Global Illumination and Reflections. 5.8 adds Lumen Lite (Beta), a cheaper medium-quality GI setting, and MegaLights is production ready | Lumen docs page, 5.8 notes |
| 2 | Import/Create a Static Mesh (1:36:52): drag FBX into Content Drawer, uncheck material and texture import | PASS (DOCS) for the same version | Plain FBX beginner path. It is NOT the Blender to Unreal pipeline the department picked, so treat it as the baseline only | transcript, `ue-import-pipeline` skill |
| 3 | Landscape Sculpting (1:56:50): empty level, directional light, Sky and Atmosphere, Exponential Height Fog, Landscape mode | PASS (DOCS) | Same classic Landscape tool in 5.8.4 | transcript |
| 4 | Landscape Material (2:08:16): layer info set to Advanced Weight Blending, paint layers | CHANGED (DOCS) | 5.6 removed the auto-fill of an empty landscape target layer. 5.8 adds an Exclusive Paint Mode for weight-blended layers (default triggered by NOT holding Ctrl) and erasing no longer rebalances the other layers. Expect painting to feel different from older videos | 5.6 and 5.8 release notes |
| 5 | Sensei Landscape Material and downloads | FLAG | The tutorial files come from the creator's own site. License NOT read. No signups allowed. Must be logged before any use, otherwise build the layered material by hand | description |
| 6 | MCP chapter (3:43:42) | FLAG | Reading only. Epic MCP stays OFF until Zac says yes (`ANIMATION\CLAUDE.md` pipeline decision 4) | CLAUDE.md |
| 7 | Whole-course size | NOTE | 5 h 50 min. Use only the chapters above. Caption file for the course is about 3 MB, only study the needed timestamps | |

### 2.6 U2 delta sheet, Unreal 5.0 era to 5.8.4 (docs only)

| # | Step | Status | Notes | Evidence |
|---|---|---|---|---|
| 1 | Project settings first: Dynamic GI = Lumen, Virtual Shadow Maps, Hardware RT (1:37 to 3:07) | CHANGED (DOCS) | New 5.8 projects already have Lumen GI and Reflections and Hardware Ray Tracing on. Existing projects converted from UE4 do NOT. The "Beta" label on Virtual Shadow Maps in the video is out of date, exact version it went away is UNVERIFIED | Lumen docs page, transcript 00:02:28 |
| 2 | Light types and mobility (static, stationary, movable) | PASS in concept, UNVERIFIED in UI | Concept holds. Whether the default for a new light is still Stationary in 5.8.4 is UNVERIFIED. The video says to switch to Movable for Lumen | transcript 00:06:11 |
| 3 | Shadows: virtual shadow maps vs ray traced | CHANGED | MegaLights (production ready in 5.8, Beta in 5.7, Experimental in 5.5) and Lumen Lite did not exist. The tradeoffs in this chapter need a refresh | 5.5, 5.7, 5.8 notes |
| 4 | Emissive materials, indirect lighting | PASS in concept | Substrate materials are production ready and enabled by default since 5.7, so the material graph and slab nodes look different from the video's Default Lit | 5.7 notes |
| 5 | Daylight with Sky Light, Directional light, Sky Atmosphere, god rays | PASS in concept | Same actor set as U1's chapters, which are 5.8. Prefer U1 for clicks, U2 for why | U1 transcript |
| 6 | Overcast look | PASS in concept | Principle only | |

Use U2 for the reasoning (why a sun is a point, why sky light fills shadows, exposure and a gray card). Use U1 for current menus.

## 3. Items not verified, one place

1. All keyboard shortcuts and menu paths in Blender (headless has no UI or keymap).
2. Visual look of the 5.x Asset Shelf and Sculpting workspace.
3. H1 step order (no captions).
4. Every Unreal step (editor not opened). Epic hotfix notes 5.8.0 to 5.8.4.
5. Mesh Terrain differences between the Preview build in the video and 5.8.4.
6. Virtual Shadow Maps Beta label removal version, default light mobility.
7. Licenses of Poliigon files, Sensei downloads, Blender Guru blueprints.
8. Whether 5.2.4 (which the folder reports as a Release Candidate LTS build) differs from final 5.2.x on any item above.

## 4. Live Blender check list for when the MCP link is up (run in a scratch scene, never Zac's objects)

Open `blender-mcp-ops` first. Then: confirm `get_addon_status`, make `TEST_scene`, build a 6-subdivision ico sphere, enter sculpt mode on it, confirm brush picker is the bottom Asset Shelf, read `brush.size` with the Draw asset, press F and Shift+F, run Ctrl+R voxel remesh, toggle Dyntopo, check the Brush type list in the tool settings shows Plane and no separate Flatten, Fill, Scrape. Then Shift+A, Image, Reference in a side view. Then clean up per `blender-mcp-ops` section 6.

---

# 5. Second pass: boat and sci-fi ship picks (added 2026-11-13, after Zac's answer on ANIM-2026-11-05-02)

Zac REJECTED BH3, SF4, SF5. APPROVED BH1, BH2, SF1, SF2, SF3. Nothing for the rejected three was pulled or written.
Notes are in our own words. Captions are private study text in `D:\WKP\research\animation\transcripts\<id>\` (gitignored): `.en.vtt` as downloaded, `.en.txt` as timestamped lines (HH:MM:SS). No video, audio or other file was downloaded. Nothing installed, no plugin enabled, $0.

## 5.0 What was and was not checked

- **Captions.** Pulled for BH1 `FHw-MakUNu0`, BH2 `3cMXjX9bAD0`, SF1 `_zNOpeOno9A`, SF2 `mC1fPZbuKw0`, SF3 `tiL3wRk0uQ4`. All five are English auto-generated. One yt-dlp call each, 8 s apart.
- **H1 retry `11sC54-pq_0`: STILL FAILS, HTTP 429.** One try, same command. Not worked around (no client rotation, no cookies, no proxy). H1 stays chapter-level only (section 2.3). Retry on another day, same command.
- **Blender live link was not used.** Only headless Blender 5.2.4 (`C:\Blender\5.2.4\blender.exe -b --factory-startup`) on throwaway data, as in section 0. It opened none of Zac's .blend files and saved nothing.
- **Headless proves** an operator, modifier property, enum, node input or bundled asset exists in 5.2.4, and its default. **It cannot prove** menu paths, shortcut keys or how anything looks. Every shortcut named in a video (Ctrl+B, Alt+E, Shift+G, Shift+E, Shift+R, Ctrl+M, J, K, Y, I and so on) is UI-UNVERIFIED as a key, even where the operator behind it exists.
- **Release notes read** (same source as section 0) for 4.4, 4.5, 5.0, 5.1, 5.2: index, modeling, user_interface, rendering, compositor, core, eevee, sculpt, python_api. Not read: the color management page, so the release that added ACES is UNVERIFIED (only that ACES exists in 5.2.4 is proven).
- **Videos were not watched.** Everything is from caption text plus API checks. No visual claims are made.
- **Extensions on Zac's profile (read-only look, nothing changed).** Headless listing of `C:\Users\kingz\AppData\Roaming\Blender Foundation\Blender\5.2\extensions\blender_org\` shows four extensions on disk: F2 1.8.5, LoopTools 4.7.7 (GPL-2.0-or-later), Sapling Tree Gen 0.3.7, Ucupaint 3.0.0 (GPL-3.0-or-later). Licenses read from each `blender_manifest.toml`. Whether each is ENABLED in Zac's own Blender is not known. Node Wrangler is bundled in `scripts\addons_core`. UV Squares, Hard Ops, Mesh Machine and Dream UV are not on this machine.

## 5.1 Version tag blocks

### BH1 Making Boats! (WillUrquhart3D) `FHw-MakUNu0`
- Software: Blender. Version NOT STATED (no version number in the captions or title). INFERRED 4.1 to 4.3. Evidence: upload 2025-02-02, Blender 4.3 was current stable then and 4.4 did not exist until 2025-03-18. He uses "shade auto smooth" at 00:14:29, a menu item that exists since 4.1, so 4.0 or older is out. At 00:00:18 to 00:00:21 he says to open Preferences, Add-ons tab, and enable Loop Tools, UV Squares and Node Wrangler.
- Uploaded 2025-02-02. Length 14:37. Captions: auto-generated English, saved (433 lines).
- Ours: 5.2.4. Gap: 4.4, 4.5 LTS, 5.0, 5.1, 5.2 (plus 4.2 and 4.3 if he was on 4.1 or 4.2). Gap size: MEDIUM. The tools are basic mesh tools, so most steps survive.
- Paid or third-party: none paid. Needs three add-ons by name, see rows 1 to 3.

### BH2 How To 3D Model An Oceanliner, Part I (Maritime History Buff) `3cMXjX9bAD0`
- Software: Blender. Version NOT STATED (no number in 801 caption lines). INFERRED 4.4 or 4.5. Evidence: upload 2025-10-05. **Correction to the picks report**, which guessed "4.5 or 5.0": Blender 5.0 was released 2025-11-18, six weeks AFTER this upload, so 5.0 is not possible unless it was a pre-release build. 4.5 LTS (2025-07-15) is most likely. "Shade auto smooth" at 00:46:59 confirms 4.1 or newer.
- Uploaded 2025-10-05. Length 49:21. Captions: auto-generated English, saved (801 lines). No chapters. Speaker says he is "by no means a professional" (00:01:01) and this is part 1, hull only.
- Ours: 5.2.4. Gap: 5.0, 5.1, 5.2 (and 4.5 if he was on 4.4). Gap size: SMALL.
- Paid or third-party: none named. Needs a ship profile view, top-down view and ideally hull lines as images, which he sources himself. Image licenses not checked.

### SF1 Creating a Spaceship Animation in Blender 5.0 (Polygon Runway) `_zNOpeOno9A`
- Software: Blender. Version STATED: 5.0 in the title. Caption evidence: "with the new Blender 5, we got these awesome compositor presets" and the asset shelf (00:17:58 to 00:18:03), which matches the 5.0 release notes (Asset Shelf and built-in assets added to the compositor).
- Uploaded 2025-11-28. Length 20:25. Captions: auto-generated English, saved (515 lines). A project walkthrough, not a step by step build. He says so at the start.
- Ours: 5.2.4. Gap: 5.1, 5.2. Gap size: SMALL.
- Third-party: "Yuk Paint" (caption spelling, almost certainly Ucupaint, INFERRED from the name and from "available in the extensions", 00:08:52) for layered texturing. Textures come from free sites per the pick report, licenses not read.

### SF2 The SECRET to Sci-Fi DESIGN in Blender (Bevels and Booleans) `mC1fPZbuKw0`
- Software: Blender. Version NOT STATED (none in the captions). INFERRED 4.4 or 4.5. Evidence: upload 2025-09-29, same logic as BH2.
- Uploaded 2025-09-29. Length 13:52. Captions: auto-generated English, saved (374 lines). Mostly a talk about the blockout mindset. The demo is a time lapse at 5x, the voice only lists the tools.
- Ours: 5.2.4. Gap: 5.0, 5.1, 5.2. Gap size: SMALL, and the content is method not menus.
- Third-party: he names Hard Ops (his "Hard Ops mirror") and Mesh Machine (its radial array) as tools used on screen (00:06:57, 00:07:23). The captions do not state their prices, so "paid" is UNVERIFIED here. FLAG. His free Gumroad lesson with PDF references (00:07:31, 00:13:03) was not read.

### SF3 Blender 5.0 Making a Scifi Spaceship LIVE (Markom3D) `tiL3wRk0uQ4`
- Software: Blender. Version STATED: 5.0 in the title, and in the captions "So, Blender 5.0" (00:05:08) and "Blender 5.0, baby" (00:29:57). He says he planned to wipe and reinstall his add-ons for 5.0 but did not (00:18:06).
- Uploaded 2025-11-21 (three days after 5.0 shipped). Length 2:02:29. Captions: auto-generated English, saved (2,028 lines), a live stream with chat talk. The "4.4 is out" remark at 01:20:15 is about a game, not Blender.
- Ours: 5.2.4. Gap: 5.1, 5.2. Gap size: SMALL.
- Third-party: Dream UV with its "hotspot" feature (00:08:11, 00:55:07), which he says is "not working 100%" in Blender 5 (00:08:14). He mentions buying add-ons on Superhive (00:08:50). Price not stated, treat as paid, FLAG. Free route is native UV, see row 7.

## 5.2 Delta sheets

Status key as in section 2. API means proven headless in 5.2.4. UI-UNVERIFIED means no UI click.

### 5.2.1 BH1 delta sheet, Blender 4.1 to 4.3 (inferred) to 5.2.4

| # | Tutorial step | Status | What is true in 5.2.4 | Evidence |
|---|---|---|---|---|
| 1 | Preferences, Add-ons tab, enable Loop Tools | CHANGED | Loop Tools is now an Extension (4.2 onward), 4.7.7 is on this machine's profile, enabled state unknown. 5.2 builds three of its tools in: "To Circle", "Space Edge Loops Evenly" (`mesh.space_edge_loops_evenly`) and "Flatten" (`mesh.flatten`). Teach the built-ins first | 5.2 modeling notes, headless op check, manifest. Menu path UI-UNVERIFIED |
| 2 | Enable UV Squares | FLAG | Not bundled, not on this machine, third-party, license not read. Not needed for the hull. Teach native UV (`uv.unwrap`, `uv.smart_project` exist) | headless add-on list |
| 3 | Enable Node Wrangler | PASS (API) | Bundled in `scripts\addons_core\node_wrangler` | headless |
| 4 | Screencast Keys on at the start (00:00:12) | UNVERIFIED | Not in the bundled list. Not needed for the work | headless add-on list |
| 5 | Cube, scale on Y, loop cut, one loop in the middle, move edges to shape the boat | PASS (API) | `mesh.loopcut_slide` exists. Keys G, S, Y, Z UI-UNVERIFIED | headless |
| 6 | Bevel edge loop with Ctrl+B, add segments with the scroll wheel | PASS (API) | `mesh.bevel` exists with `segments`. 5.1 adds Ctrl snapping and Shift precision while beveling | headless, 5.1 modeling notes |
| 7 | Bevel with Clamp Overlap, then width type to percentage | PASS (API) | `mesh.bevel` has `clamp_overlap` and `offset_type` with OFFSET, WIDTH, DEPTH, PERCENT, ABSOLUTE. The Bevel MODIFIER has no property named `width_type` (read: ABSENT), so read the property list before scripting it | headless |
| 8 | Select one face, Shift+G, Coplanar, delete the faces | PASS (API) | `mesh.select_similar` has `FACE_COPLANAR` | headless |
| 9 | Alt+E, extrude faces along normals, thicken the hull | PASS (API) | `view3d.edit_mesh_extrude_move_normal` exists. Keys UI-UNVERIFIED | headless |
| 10 | Mark seam, L with delimit Seam, split with Y | PASS (API) | `mesh.mark_seam`, `mesh.select_linked_pick` (delimit includes SEAM), `mesh.split` exist | headless |
| 11 | Merge by distance to clean the hull bottom, he reads "removed 16 vertices" | CHANGED | 5.0 changed Merge by Distance. A new Centroid option, ON by default (read: `use_centroid` default True), moves merged vertices to their average position. The merged shape and the vertex count on screen can differ from the video | 5.0 modeling notes, headless |
| 12 | Duplicate, scale, inset a ring to make beams, Shift+R repeat last | PASS (API) | `mesh.duplicate_move`, `mesh.inset`, `screen.repeat_last` exist | headless |
| 13 | Ctrl+M mirror a selection across X | PASS (API) | `transform.mirror` exists. Key UI-UNVERIFIED | headless |
| 14 | Bridge Edge Loops | PASS (API) | `mesh.bridge_edge_loops` exists | headless |
| 15 | Face Orientation overlay, flip and recalculate normals | PASS (API) | Overlay `show_face_orientation`, `mesh.normals_make_consistent`, `mesh.flip_normals` exist. Keys UI-UNVERIFIED | headless |
| 16 | Fill (F), Inset (I), J connect, K knife | PASS (API) | `mesh.edge_face_add`, `mesh.inset`, `mesh.vert_connect_path`, `mesh.knife_tool` exist | headless |
| 17 | Bevel modifier: segments 2, miter outer Arc, intersection Cut Off | PASS (API) | `miter_outer` has MITER_SHARP, MITER_PATCH, MITER_ARC. `vmesh_method` has ADJ and CUTOFF. Same names | headless |
| 18 | "Shade Auto Smooth" at 00:14:29 | CHANGED | `object.shade_auto_smooth` exists and adds a Smooth by Angle geometry nodes modifier (`angle`). `object.shade_smooth_by_angle` exists (`angle`, `keep_sharp_edges`). The old mesh checkbox is gone since 4.1, which the video already reflects. Menu position in 5.2.4 UI-UNVERIFIED | headless |
| 19 | Reference image (00:00:43) | FLAG | The boat image is the maker's own, not provided. Use our own or a free-licensed image, log it | caption |
| 20 | UV unwrap and texturing | NOT IN THIS VIDEO | Ends with "the next video is going to cover unwrapping this object and texturing it" (00:14:33). That part was not picked | caption end |

Net for BH1: a sound hull method that survives almost whole. Changed items to teach: Loop Tools (row 1), Merge by Distance Centroid (row 11), auto smooth path (row 18).

### 5.2.2 BH2 delta sheet, Blender 4.4 or 4.5 (inferred) to 5.2.4

| # | Tutorial step | Status | What is true in 5.2.4 | Evidence |
|---|---|---|---|---|
| 1 | Import profile and top view blueprint images as references, line them up with a rectangle (00:01:24 to 00:02:50) | PASS (API) | `object.empty_image_add` exists. `show_empty_image_orthographic` and `show_empty_image_perspective` exist | headless |
| 2 | Delete half, add Mirror modifier (00:06:03, Generate, Mirror) | PASS (API) | Mirror has `use_clip`, `use_mirror_merge`, `merge_threshold`, `use_bisect_axis`, `mirror_object` | headless |
| 3 | Move vertices to match the blueprint outline, one by one | PASS | Plain vertex edit, no version dependency | caption |
| 4 | Subdivision Surface modifier to soften the hull (00:41:01) | PASS (API) | Modifier SUBSURF with `levels`, `render_levels`, `use_creases` | headless |
| 5 | Shift+E crease so the top edge stays sharp | PASS (API) | `transform.edge_crease` exists. Key UI-UNVERIFIED | headless |
| 6 | Sharpen the bulbous bow | PASS | Method only | caption |
| 7 | Bevel, extrude, Shade Auto Smooth at the end (00:46:59) | CHANGED | Same as BH1 row 18. Modifier order with Subdivision is UNVERIFIED (not clicked) | headless |
| 8 | Scope | FLAG | Hull only. Decks, superstructure, funnels are later parts we do not have. Self-described non-professional and "not an advanced tutorial". Teach the blueprint to hull method, not his accuracy | caption 00:01:01 |
| 9 | Blueprint sources | FLAG | He pulls plans from the web. We need our own public-domain or free-licensed plans and a log row for each | caption |

Net for BH2: thin on tools, useful for method (blueprint, silhouette, half model, mirror, subdivision with creases). Treat as a second hull example beside B1's method (section 2.4).

### 5.2.3 SF1 delta sheet, Blender 5.0 to 5.2.4

| # | Tutorial step | Status | What is true in 5.2.4 | Evidence |
|---|---|---|---|---|
| 1 | Block out with simple shapes, bevels, booleans to cut shapes, subdivision only on the cabin | PASS (API) | Boolean solvers are FLOAT, EXACT, MANIFOLD (FAST became FLOAT in 5.0, his version). Operations INTERSECT, UNION, DIFFERENCE | headless, 5.0 notes |
| 2 | Layered texturing with "Yuk Paint" from Extensions | FLAG | Almost certainly Ucupaint (INFERRED). Ucupaint 3.0.0 is on this machine's profile, GPL-3.0-or-later, min Blender 4.2. NOT in `animation-asset-log.csv` (searched, no row). Log before use. Whether it runs in 5.2.4 is UNVERIFIED (not enabled, not run) | manifest read, log search |
| 3 | Bloom in the viewport early | CHANGED | Legacy EEVEE bloom is gone (`scene.eevee.use_bloom` absent). The bloom is a compositor Glare shown in the viewport. Glare Type is now a MENU INPUT socket on the node (read: `glare_type` property absent, 'Type' input of MENU type present) | headless, 5.0 compositor notes |
| 4 | Planet, atmosphere, clouds: noise texture driving a volume shader, color ramp on density | PASS (API) | `ShaderNodeTexNoise`, `ShaderNodeVolumePrincipled`, `ShaderNodeVolumeScatter`, `ShaderNodeValToRGB` exist. EEVEE volumetric settings exist | headless |
| 5 | Asteroids by geometry nodes scatter | PASS (API) | `GeometryNodeDistributePointsOnFaces` and `GeometryNodeInstanceOnPoints` exist. Bundled assets "Scatter on Surface", "Instance on Elements" and "Array" are in `geometry_nodes_essentials.blend` | headless |
| 6 | Glare for bloom and stretched lens flare, then Split Toning and Chromatic Aberration from the compositor asset shelf | PASS (API) | Bundled compositor assets in 5.2.4: Vignette, Unsharp Mask, Tune Image, Transform and Project, Split Toning, Sepia, Separate Spherical, Separate Cylindrical, Sensor Noise, Screen to 3D Space, Retime, Project with Depth, Film Grain, Combine Spherical, Combine Cylindrical, Chromatic Aberration, 3D to Screen Space. Compositor tree is on `scene.compositing_node_group` | headless asset list, 5.0 compositor notes |
| 7 | "ASUS" view transform instead of AgX | PASS (API), name fixed | "ASUS" is a caption error. View transforms in 5.2.4: Standard, ACES 1.3, ACES 2.0, Khronos PBR Neutral, AgX, Filmic, Filmic Log, False Color, Raw. Default is AgX. Which ACES he meant is UNVERIFIED. Release that added ACES UNVERIFIED | headless enum read |
| 8 | Scene file and textures | FLAG | Scene file is on his Patreon, skip. Texture licenses not read, log before use | pick report |
| 9 | Animation and composite chapters (15:23, 16:57) | NOT CHECKED | Not read line by line | |

Net for SF1: nothing broken for 5.2.4. Teach it as a whole-ship overview and a render recipe (glare bloom, compositor shelf, volume haze). It is not a hard-surface step by step lesson.

### 5.2.4 SF2 delta sheet, Blender 4.4 or 4.5 (inferred) to 5.2.4

| # | Tutorial step | Status | What is true in 5.2.4 | Evidence |
|---|---|---|---|---|
| 1 | Blockout mindset: rough, unmerged, 15 to 20 minute sketches | PASS | Method only | caption |
| 2 | Bevel modifier, large bevels on boolean cutters or on a loop cut, no small bevels | PASS (API) | Bevel modifier properties unchanged (5.2.1 row 17) | headless |
| 3 | Difference booleans only, no union, no intersect, to protect topology | CHANGED (names only) | Operations: INTERSECT, UNION, DIFFERENCE. Solver FAST is now FLOAT (5.0), MANIFOLD is new (4.5). The preference is a method choice. Which solver he used is not stated, UNVERIFIED | headless, 4.5 and 5.0 notes |
| 4 | Solidify modifier on chopped pieces | PASS (API) | `SOLIDIFY` with `thickness`, `offset`, `solidify_mode` (EXTRUDE, NON_MANIFOLD), `use_even_offset`, `use_rim` | headless |
| 5 | "Hard Ops mirror" | FLAG | Third-party, price not stated (treat as paid). Native replacement: Mirror modifier with a Mirror Object | headless |
| 6 | "Mesh Machine radial array" | FLAG | Third-party, price not stated (treat as paid). Native replacement: Array modifier with Object Offset (`use_object_offset`, `offset_object` exist), or the 5.0 Array asset in `geometry_nodes_essentials.blend` | headless |
| 7 | Edge loops, insets, extrudes, duplicate and separate, convert to curve | PASS (API) | `mesh.loopcut_slide`, `mesh.inset`, `mesh.extrude_region_move`, `mesh.duplicate_move`, `mesh.separate`, `object.convert` exist | headless |
| 8 | No proportional editing, no SubD modeling | PASS | Method | caption |
| 9 | Free Gumroad lesson with PDF references | FLAG | Free per the speaker. License and content not read, not downloaded | caption |

Net for SF2: the value is the method, "indicate detail with bevels, booleans and insets, keep it rough, under 20 minutes". The skill must state that his two named add-ons are third-party and teach the native route.

### 5.2.5 SF3 delta sheet, Blender 5.0 to 5.2.4

| # | Tutorial step | Status | What is true in 5.2.4 | Evidence |
|---|---|---|---|---|
| 1 | Paneling method A: delete the faces you want as panels, Shrinkwrap modifier (Project, positive and negative direction) onto the hull, then Solidify | PASS (API) | `SHRINKWRAP` has `wrap_method` (NEAREST_SURFACEPOINT, PROJECT, NEAREST_VERTEX, TARGET_PROJECT), `wrap_mode`, `offset`, `use_positive_direction`, `use_negative_direction`, `cull_face`, `project_limit`, `target`. He first says Generate for Shrinkwrap then corrects to Deform. He says it suits larger ships | headless, caption 00:09:30 |
| 2 | Method B: edge loops, Ctrl+B bevel, delete faces, inset, favor larger panels | PASS (API) | `mesh.bevel`, `mesh.inset`, `mesh.loopcut_slide` exist | headless |
| 3 | Right click, Auto Smooth | CHANGED | Same as BH1 row 18. Position in the right-click menu UI-UNVERIFIED | headless |
| 4 | Merge by Distance, at Center, at Last, used many times | CHANGED | `mesh.merge` exists. Merge by Distance changed in 5.0 (Centroid default ON). He is already on 5.0 so he shows the new behavior, no gap for the video | headless, 5.0 notes |
| 5 | One named mirror point object (the glass) set as Mirror Object | PASS (API) | `mirror_object` exists on the Mirror modifier | headless |
| 6 | Boolean, snap and the long build | UNVERIFIED | Only the paneling and add-on parts were read, not all 2,028 lines. Use the chapters, not the stream | |
| 7 | Dream UV hotspot unwrapping | FLAG | Third-party, treat as paid. He says it is "not working 100%" in Blender 5. Teach native UV: `uv.unwrap`, `uv.smart_project`, and 5.0 UV sync selection default ON (section 2.3 row 8) | caption 00:08:14, headless |
| 8 | Kitbash pack, decals, edge-wear materials | FLAG | His own pack, free on Gumroad per the description, also sold. License not read, not downloaded. Teach making our own panel and decal pieces | pick report |
| 9 | Landing gear, engine pod, mechanism chapters (66:19 onward) | NOT CHECKED | Modeling content, not read line by line | |
| 10 | Whole stream | NOTE | 2 h 02 min with chat talk. Use paneling, topology and landing gear chapters only | pick report |

Net for SF3: no version problem. Two flags (Dream UV, kitbash pack) and one scope note.

## 5.3 Cross-cutting findings (these change how the three skills are written)

1. **Loop Tools:** three tools are now built in (5.2) and the extension is already on this machine. Old videos say "enable the add-on". Our skill says "use To Circle, Space Edge Loops Evenly and Flatten", plus one line "old videos call this Loop Tools".
2. **Merge by Distance:** 5.0 added Centroid, default ON. Old videos show a different merged shape.
3. **Auto Smooth:** the menu action is now a Smooth by Angle modifier, never the old mesh checkbox.
4. **Boolean solver names:** FAST is FLOAT, MANIFOLD is new. SF2 teaches Difference booleans only, which fits any solver.
5. **Third-party tools the videos lean on that we will NOT use or buy:** Hard Ops, Mesh Machine (SF2), Dream UV (SF3), UV Squares (BH1), kitbash packs. Native routes are in each table. Ucupaint (SF1) is free, GPL, already on the profile, so it is a candidate once logged and tested.
6. **Pick report correction:** BH2's inferred version "4.5 or 5.0" was wrong, 5.0 did not exist yet. Now 4.4 or 4.5. No effect on the pick.

## 5.4 New items not verified (adds to section 3)

1. All shortcut keys and menu paths named in BH1, BH2, SF1, SF2, SF3.
2. Whether the four extensions on Zac's profile are enabled in his Blender, and whether Ucupaint 3.0.0 works in 5.2.4.
3. Which release added the ACES view transforms.
4. SF3 chapters not read line by line. SF1 animation and composite chapters not read.
5. BH1, BH2 and SF2 versions are INFERRED only.
6. H1 captions (HTTP 429 on retry).
7. Licenses of SF1 textures, SF2 and SF3 Gumroad files, SF3 kitbash pack, blueprint images. Ucupaint has no asset log row.

## 5.5 Live Blender check list additions (when the MCP link is up, scratch scene only)

In `TEST_scene`: box, Ctrl+B, confirm Clamp Overlap and Percent in the redo panel; Shift+G Coplanar; Alt+E on faces; merge by distance and read the Centroid checkbox; Shrinkwrap then Solidify on a plane over a sphere (Project, both directions); Mirror with a Mirror Object; Bevel modifier with miter outer Arc and intersection Cut Off; Shift+E crease; right-click shade menu entry for Smooth by Angle; Face Orientation overlay path; compositor asset shelf shows Chromatic Aberration and Split Toning; Add menu, Image, Reference. Then clean up per `blender-mcp-ops` section 6.
