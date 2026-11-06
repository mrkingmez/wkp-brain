---
name: blender-planar-head-modeling
description: Planar (block-plane) head modeling in Blender from a plaster-style planar reference, the viewport settings that make flat planes readable (Cavity, Auto Smooth, Studio lighting, Outline), the final front/side/ear views as a quality bar, and a graded practice drill. Use before any character or creature head, face, bust or horned or eared head, and whenever a bench must show it can build a head that passes as an experienced artist's work. Source kit is copyrighted internal training material.
---

# Blender planar head modeling

Written 2026-11-05 by animation-director from Zac's starterKit (images only). Nothing here was run in Blender. Scope of evidence: what is visible in 8 files. Every inference is tagged INFERENCE. Every Blender 5.2.4 behavior not tested is tagged UNVERIFIED.

Why a new skill and not an extension of `blender-character-craft`: that file is already long and covers the whole character path (reference, rig, fur, AI options). This one is a narrow head method that can be drilled. `blender-character-craft` section 0 says code-built Skin-modifier blobs fail; this skill is the hand-built-from-planes alternative for the head. Cross-link both ways when either is touched.

## 0. Rights (read first)

The planar reference images (planarModeling_ref.jpg, planarModeling_ref_profile.jpg) are credited in CREDITS.txt to 3D Total, Marisa Lewis, "Anatomy Head: the Human" (https://3dtotal.com/news/general/approaching-planar-references-by-marisa-lewis-anatomy-head-the-human). Copyrighted, license not stated. Rules:
- Internal training reference only. Never republish, never put in a deliverable, video, post or Unreal project, never use in a shipped asset's textures.
- Studying the planes and modeling our own practice head is fine. A shipped character must be built from its own concept art, not from this head.
- The other kit images (_front_final, _side_final, _ear_final, planarModeling_settings, dustBokeh) have no credit line. Author and license are UNKNOWN. Same treatment: internal only.
- Files: `D:\WKP\ANIMATION\training\starterKit-2026-11-05\starterKit\`. Logged in the asset log as internal reference only, not usable.

## 1. What the kit contains (read from the images)

1. **Planar reference, front and 3/4** (two panels). A bald neutral head and bust made only of flat facets. Left is a grey digital version front-on, right is a white plaster cast photographed at 3/4 on a dark backdrop. Facets show at the brow ridge, nose bridge, nose sides and tip, cheekbone, under-lip and chin, jaw, temple, skull top, neck and bust.
2. **Planar macro close-up** (planarModeling_ref_profile.jpg). Near-profile close-up. The brow-to-nose transition is a small stack of angular planes, the cheek is a large plane turning at the jaw line, the lips are the only softly rounded forms, the ear is a simple rounded form with a hook-shaped inner fold.
3. **Settings screenshot**, Blender 2.92.0 per the status bar, shown twice side by side. The model is a horned, pointed-ear female bust made of flat planes. Left: Object Data tab with Normals > Auto Smooth ticked at 30 degrees. Right: the viewport shading popover with Cavity on. Red marks circle those controls.
4. **Final front, side and ear views** (2048 px, grey, black outline). The smooth sculpted end state of the same character type (section 4).
5. **dustBokeh.jpg.** Dark navy and teal backdrop with out-of-focus dust specks. Purpose not stated. INFERENCE: a background or overlay for a presentation render. Not a modeling aid.

## 2. Exact viewport values (transcribed from planarModeling_settings.jpg)

Blender 2.92.0 UI. Only what is visible.

Object Data properties (green triangle tab), Normals panel:
- Auto Smooth: ticked, 30 degrees.

Viewport Shading popover (dropdown beside the shading buttons), Solid mode:
- Lighting: Studio selected (others shown: MatCap, Flat).
- Color: Material selected (others: Object, Vertex, Single, Random, Texture).
- Background: Theme selected (others: World, Viewport).
- Backface Culling: off. X-Ray field 0.500 and Shadow field 0.500 shown, both appear not enabled.
- Cavity: ticked. Type: Screen.
- Screen Space: Ridge 0.000, Valley 1.136.
- Depth of Field: off.
- Outline: ticked, color black.
- Specular Lighting: ticked.

Other context: Local View ("User Perspective (Local)"), Object Mode. The outliner lists Head.001 to Head.009 and more with modifier (wrench) icons, active object Head.015. INFERENCE: numbered copies of the head at different stages. A good habit (versioned copies), not shown to be deliberate.

### What the settings do (INFERENCE from the two screenshots, not tested)
- Left screenshot has Cavity off, right has it on. With Cavity on, Ridge 0.000 and Valley 1.136, the creases between planes (eye-brow junction, nostril edge, lip line, under-chin, collar planes) darken and ridges are not brightened. Planes separate by tone, which is the point: reading plane breaks without material work.
- Studio lighting plus Specular gives orientation-dependent grey values, so each plane reads on its own.
- Auto Smooth at 30 degrees: planes stay flat and breaks over 30 degrees stay crisp, gentle turns (lips, eyelids, ear) shade smooth. INFERENCE from how the head looks.
- Black Outline gives a silhouette edge to judge the profile against the reference.

### Blender 5.2.4 translation (all UNVERIFIED)
- To my knowledge Auto Smooth as an Object Data checkbox was removed in Blender 4.1 and replaced by Shade Auto Smooth and the Smooth by Angle modifier (default 30 degrees). I have not opened 5.2.4 to confirm the name or place.
- Viewport Shading popover with Cavity (Screen or World type, Ridge, Valley), Outline and Specular Lighting is believed still present in 5.x. Set the same values.
- Keep Solid (Workbench), not Rendered, for plane reading.
- When a drill is authorized, read and set via blender MCP on `bpy.context.space_data.shading` (properties such as `show_cavity`, `cavity_type`, `cavity_ridge_factor`, `cavity_valley_factor`, `show_object_outline`, `show_specular_highlight`, `light`). Names are from memory, UNVERIFIED. Read enum values first, never hardcode (see `blender-mcp-ops`).

## 3. Method (what is and is not shown)

The kit gives results and settings, NOT a step-by-step video. The images do not show edit-mode work, the modifiers on Head.001 to Head.015, or sculpt tools. The steps below are standard planar-head practice written by me. The whole list is INFERENCE / community practice, UNVERIFIED in 5.2.4.

1. Set up front and side reference images (`blender-character-craft` section 1).
2. Block the head as a simple large form with a Mirror modifier on X. Keep face count low (a few hundred). Work big to small: skull, jaw, cheek, brow ridge, nose block, mouth block, ear block, neck.
3. Keep every surface flat on purpose while structure is decided. Judge only with the Section 2 settings, in front, side and 3/4 views, rotating the light.
4. Check against the reference: plane breaks land at the same places (brow ridge, nose bridge and wings, cheekbone, jaw line, chin, temple). Match the planes, not only the outline.
5. After the planes are right, smooth or sculpt for form (subdivision or multires), then retopologize if the head will deform or go to Unreal. The kit's final views show the smooth end state but not how it was reached. Do not claim a specific tool chain.

## 4. The final views as a quality bar (what they show)

Observed in _front_final, _side_final, _ear_final:
- Smooth head with believable proportions: eye line near mid head height, nose and mouth in sensible thirds, neck column placed right, clear jaw-to-neck transition. Symmetrical, calm face.
- Defined eyelids with a lid line, nostrils, lips with a lip line, an ear with helix and inner fold, pointed ear tips. Side view: forehead, nose, lips and chin profile read cleanly and the neck-to-skull angle is natural.
- Horns are large, curled and roughly textured. They are the most detailed element.
- Bust and plinth are simple, clean and hard-edged. Black outline everywhere.
- Visible weaknesses, so the bar is "credible", not "perfect": empty eyes (no eyeballs), black speckle noise along the horns, hairline and skull rim (INFERENCE: outline or cavity artifacts from the viewport), coarse grainy horn texture, and in _ear_final a rectangular patch of mismatched noise at the horn base that is clearly a render or compositing artifact. These are grey viewport renders with no materials, not a finished shipped character.
- What it demands of us for any head: correct facial proportions, planes readable before smoothing, an ear with inner structure, lips with form, a clean profile, a surface with no artifacts. A bench that cannot do this on a neutral head must not attempt a stylised creature head.
- Not knowable from images alone: poly count, topology and edge flow, whether the horns are sculpted or textured, UVs, the modifiers used, the render engine, time taken, whether the head was built from or traced over the reference.

## 5. Where this fits

- STANDARDS.md section C item 2 (face and head matched first) and the 2026-11-01 correction (Wolf Warrior rejected, skin-modifier blobs not accepted, test is "would it pass as work from an experienced 3D artist"). A planar head is the foundation test: it shows structure can be built from reference before fur, armor or a rig.
- Order on the sculpt and retopo path (mandate, skill still to write `blender-sculpting-and-retopo`): planar blockout (this skill), smooth or sculpt, retopology and bake, UV, rig. This skill covers the first step and plane-reading discipline only.
- Run `blender-asset-quality` checks. Gate views per STANDARDS A10: front, side, back, 3/4, plus a face close-up.
- Wolf, canine or creature heads: planar thinking applies (muzzle, brow, cheek, skull planes) but the kit has no creature reference. Do not invent one. Ask for a real reference.

## 6. Graded practice drill: "Plaster head"

Status: PROPOSED, NOT RUN. Zac's 2026-11-01 decision: no scratch tests until he asks. No Blender or Unreal work for this until then.

Task: from the planar front and 3/4 references (internal only), build a neutral planar head and bust in Blender 5.2.4, then a smooth version. Save as `D:\Blender Projects\Plaster Head v1.blend` (versioned, never overwrite). Never put the file or renders of the 3D Total references in any deliverable folder.

Tiers, each needs the one before:
- **Tier 1, planes only.** Mirror-symmetric faceted head and bust, 300 to 2,000 faces (my estimate, UNVERIFIED), flat shading with the Section 2 settings.
- **Tier 2, smooth form.** Same head smoothed (subdivision or multires), proportions kept, eye sockets, nose, lips, ear form and neck.
- **Tier 3, one change.** Add one feature not in the reference (pointed ears or a horn pair) without breaking the face.

Pass or fail, from STANDARDS.md. Mark each pass or miss with image evidence:
1. A1: a written checklist of the reference's defining plane breaks (brow ridge, nose bridge, wings and tip, cheekbone, jaw line, chin, lips, temple, ear, neck) before building. Any miss on a defining plane fails.
2. A2: head height read from the scene and reported in metres, with the reference stated. Target about 0.22 to 0.25 m chin to crown for a realistic adult (my number, UNVERIFIED).
3. A3: transforms applied, origin at a stated point (base of the bust).
4. A4: Tier 2 is quads, no non-manifold, no loose geometry, no zero-area faces, audit output attached. Tier 1 may have n-gons on flat planes only.
5. A8: no shading artifacts, no inverted normals (face orientation view). The black speckle seen in the kit's final images counts as an artifact and fails.
6. A9: clean scene, named objects, no leftover copies other than versioned saves.
7. A10: front, side, back, 3/4 and a face close-up in the Section 2 style, looked at by the director.
8. C1 and C2: silhouette and face match the reference from front and side. Measured proportions (eye line, nose, mouth, chin thirds) within 10 percent (draft).
9. 2026-11-01 correction: honest read by the director, "would it pass as an experienced 3D artist's work". If not, name what fails and stop polishing.
10. G: report lists measured numbers and what is still weak. No "looks good" without viewed images.

Pass = every item passes at Tier 2. Tier 1 alone is not a pass. Same line failed twice goes to Zac with both versions (AGENT-NETWORK.md).

When Zac says go: first test and record the 5.2.4 equivalents of the Section 2 settings here and drop the UNVERIFIED tags that were confirmed.

## 7. Change log

- 2026-11-05: created from starterKit. Images read directly. Untested.
