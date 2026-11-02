# ANIMATION STANDARDS: the gate

**STATUS: DRAFT 2026-10-31, written from best practice. Zac marks it up. Once he corrects it, this file is the law.** Every number marked (draft) is a starting point for Zac to change.

animation-director checks every deliverable against this file before the requesting director sees it. A send-back must cite a line number or item from here, or name a concrete problem. "Not good enough" alone is not allowed.

## A. Applies to every asset

1. **Matches the brief and the reference.** A checklist of the reference's defining features is written before building. Every item is marked pass or miss. Any miss on a defining feature fails the asset.
2. **Real-world scale.** 1 Blender unit = 1 meter. Dimensions are read from the scene and reported, not assumed.
3. **Transforms applied.** Scale (1,1,1), rotation (0,0,0) on finished objects. Origin placed where the asset is used (feet on the ground for characters and props that stand, hinge or base point for others).
4. **Clean geometry.** No non-manifold edges, no loose vertices or edges, no overlapping duplicate faces, no zero-area faces. Quads on curved and deforming surfaces. N-gons only on flat surfaces, never on deforming ones. (audit script reports all of these)
5. **Triangle budget (draft):** background prop under 5,000 tris. Hero prop 5,000 to 30,000. Real-time character under 60,000. Hero or offline character up to 150,000. Anything over budget needs a reason in the report.
6. **UVs.** Every textured object has a non-overlapping UV layout (mirrored overlap allowed and noted), with padding (draft: 4 to 8 pixels at 2048), consistent texel density across one asset, UV map named `UVMap`.
7. **Materials.** Principled BSDF with PBR values. No unnamed `Material.001`. Names follow Section B. Texture sizes are powers of two (draft: 2048 default, 4096 for hero, 512 or 1024 for small props). Normal map convention noted for the target (Unreal is DirectX, Blender is OpenGL).
8. **Normals and shading.** No shading artifacts, no inverted normals (checked with face orientation). Smooth shading with correct edge handling, not blanket smoothing.
9. **Clean scene.** No stray objects, no hidden leftovers, no unused material slots, orphan data purged. Objects named, grouped in collections.
10. **Seen from four angles.** At least front, side, back and three-quarter, shown in rendered shading, plus a close-up on the face or the most detailed area. The director looks at the images, not only the numbers.

## B. Naming (Unreal style)

`SM_` static mesh, `SK_` skeletal mesh, `M_` material, `MI_` material instance, `T_` texture (with `_BC` base color, `_N` normal, `_ORM` occlusion roughness metallic), `SKEL_` skeleton, `A_` animation, `UCX_<mesh>_01` collision. Spaces never. Versions in file names as `vN`.

## C. Characters and creatures (adds to A)

1. **Silhouette reads as the character** from the reference's main angle, and also from the side.
2. **Face and head** match the reference: muzzle length, eye shape and placement, brow, ears, jaw. This is checked first.
3. **Proportions** match the reference within a tolerance the director states from measurements (draft: key proportions within 10 percent).
4. **Anatomy holds.** Limbs and hands join correctly, legs are not thinner than the torso supports, the pose is balanced.
5. **Armor and props fit.** Nothing floats or clips through the body. Held items sit in the hand with correct grip.
6. **Rigged characters:** deform correctly through the pose range tested, no collapsing joints, weights checked at shoulders, hips, elbows and knees.
7. **Fur and hair method stated** (cards, hair curves, geometry) and fits the target (real-time or offline).

## D. Sourced assets

1. License is exact, logged in `D:\WKP\data\assets\animation-asset-log.csv`, and allows WKP commercial use. CC-BY needs the attribution line recorded.
2. No franchise or trademarked characters.
3. Passes Section A at the same level as something we built.
4. Nothing was bought and no credit spent without Zac's yes.

## E. Unreal handoff (adds to A)

1. Exported with the settings in skill `ue-import-pipeline` for the chosen format.
2. Imports at the right size, right pivot, with correct normals and materials, and no import errors. (Zac confirms or sends a screenshot; if unchecked the report says "not available".)
3. Collision, LODs and Nanite decided and stated.
4. Texture compression and sRGB flags correct.

## F. Scenes and renders (Unreal)

1. Lighting reads clearly, no blown highlights or crushed blacks on the subject. Exposure is not left on a wrong auto value.
2. Runs inside the machine's limits (RTX 5060, 8 GB class VRAM). Final render settings stated.
3. Camera, lens and composition serve the subject. The subject is in focus and fully in frame unless the shot says otherwise.
4. Render checked by looking at the actual frames, not by the settings alone.

## G. Reports

1. Every report lists the numbers read from the scene (tris, dimensions, texture sizes, UV status), the checklist result line by line, the angles checked, and what is still weak.
2. Nothing is called done that was not looked at.
3. Spend: none. Anything that would cost money is queued for Zac with the exact price.

## Zac's corrections (add dated lines here as he gives them)

- **2026-11-01 (Zac), the bar for characters and creatures:** the Wolf Warrior v1/v2 "looked like crap, like someone who has never used Blender before would draw." Anything that reads as amateur, blobby, cartoonish or primitive-built FAILS, whatever the poly count and checklist say. The test is: would it pass as work from an experienced 3D artist? If the Blender section cannot reach that with the method it has, it says so and queues options for Zac instead of delivering a weak version. Skin-modifier blob characters are not an accepted method.
