# Photo Restore in Photoshop: Beginner Guide

Written 2026-11-10 for Zac. Read-only research and writing. Nothing was downloaded, signed up for, posted, or spent.

## READ THIS FIRST: how well the menu names are backed up

Adobe's help pages (helpx.adobe.com) returned "403 Forbidden" every time they were opened directly, from the page fetcher and from curl. So nothing below was read off the live Adobe page by Claude. What was done instead: Adobe help pages were found by search, and the search tool returned summaries and short quotes of those pages. Each fact below carries one of these labels:

- **ADOBE-SUMMARY**: stated in a search summary or quote of the Adobe page named next to it. The page itself was not opened.
- **NOT VERIFIED**: standard Photoshop knowledge, not confirmed against an Adobe page this session. Check it on your screen. If your menu looks different, trust your screen.

Adobe pages that were found (open them yourself if you want to double check):
- Retouch and repair: https://helpx.adobe.com/photoshop/using/retouching-repairing-images.html
- Spot Healing Brush: https://helpx.adobe.com/photoshop/desktop/repair-retouch/clean-restore-images/remove-small-spots-with-the-spot-healing-brush.html
- Remove tool: https://helpx.adobe.com/photoshop/using/tool-techniques/remove-tool.html
- Dust & Scratches: https://helpx.adobe.com/photoshop/desktop/effects-filters/artistic-stylize-filters/apply-the-dust-and-scratches-filter.html
- Levels: https://helpx.adobe.com/photoshop/desktop/adjust-color/color-corrections/adjust-levels-in-an-image.html
- Curves: https://helpx.adobe.com/photoshop/desktop/adjust-color/color-corrections/adjust-color-and-tone-with-curves.html
- Levels and Curves eyedroppers: https://helpx.adobe.com/photoshop/using/adjust-color-tone-levels-curves.html
- Crop and straighten: https://helpx.adobe.com/photoshop/desktop/crop-resize-transform/resize-adjust-resolution/crop-and-straighten-images.html
- Crop tool options: https://helpx.adobe.com/photoshop/desktop/crop-resize-transform/crop-straighten/crop-tool-options.html
- Neural Filters list and FAQ: https://helpx.adobe.com/photoshop/using/neural-filters-list-and-faq.html
- Generative credits FAQ: https://helpx.adobe.com/creative-cloud/apps/generative-ai/generative-credits-faq.html
- Generative credits access and use: https://helpx.adobe.com/photoshop/using/generative-credits-access-and-use.html
- Non-destructive editing: https://helpx.adobe.com/photoshop/using/nondestructive-editing.html

## The rules that run the whole guide

1. **Never touch the original file.** You only ever work on a copy.
2. **Every fix goes on its own layer.** A layer is a see-through sheet stacked on top of the photo. If you mess up, you delete the sheet and the photo underneath is fine.
3. **Faces get cleanup only.** Dust, scratches, and brightness. Nothing gets redrawn.
4. **No generative credit tools in the main path.** Standard tools only.
5. **Stop and compare often.** Click the eye icon next to a layer to hide it and see the before.

Quality bar (from the launch prep file, section 2). A photo is done only if every line is true:
- The face looks like the same person to someone who knew them. No plastic smoothing, no new teeth, no changed expression.
- No visible clone-stamp repeats, smears, or halo edges at 100 percent.
- Damage that was fixed is gone. Damage that was left is named in the note.
- Grain and age are kept enough that it still looks like an old photo.
- The file opens on a phone, resolution at least as large as the original.
- If it fails, redo once. If it still fails, tell the customer, no charge.

Total time for one photo once you know the steps: about 60 to 90 minutes. Your first one will take longer. That is normal.

---

## STAGE 1: Setup (10 minutes)

**Words you need:**
- **Layer**: a see-through sheet on top of the photo.
- **Pixel**: one tiny dot of color. A photo is millions of them.
- **Zoom 100 percent**: each photo dot takes one screen dot. This is the honest view. Use it to judge faces.

1. Open Photoshop.
2. Check your version. On the top menu bar click **Help**, then click **About Photoshop**. (NOT VERIFIED for exact wording. On some versions on Windows it is under Help.) A window shows a year or a version number. Write it down: ________.
3. Close that window.
4. Make a work folder on your drive, for example `D:\WKP\scratch\photo-restore\practice\`. Make three sub folders inside it: `01-original`, `02-work`, `04-final`.
5. Put the photo file in `01-original`. Then copy it into `02-work` (right click, Copy, go to `02-work`, right click, Paste).
6. In Photoshop click **File**, then **Open**. Browse to the copy in `02-work`. Click it, click **Open**.
7. Make a duplicate layer. Click **Layer** on the top menu, then **New**, then **Layer Via Copy**. (ADOBE-SUMMARY: Adobe's retouch page says "choose Layer > New > Layer Via Copy to make a copy of the Background layer.") Shortcut: Ctrl+J (NOT VERIFIED).
8. If the Layers panel is not on screen, click **Window**, then **Layers**. You should see two layers: the bottom one called Background, the top one called Layer 1.
9. Double click the name "Layer 1", type `work`, press Enter.
10. Click the lock icon on Background (NOT VERIFIED) so it cannot be changed. If the lock icon is missing, skip this. The copy rule already protects you.
11. Save the working file right now: **File**, **Save As**, pick the format **Photoshop (*.PSD)**, name it `practice1-restore-v1.psd`, save it in `02-work`. (Saving as PSD is NOT VERIFIED for exact wording, but PSD keeps layers.)

**CHECKPOINT 1:** Is the original still sitting untouched in `01-original`? Do you see Background and `work` in the Layers panel? If yes, go on.

### Where menus can differ by version
- Adobe's own pages are written in two styles. Older pages say "Filter > Noise > Dust & Scratches". Newer pages are labeled "Photoshop on desktop". (ADOBE-SUMMARY, Dust & Scratches pages.)
- The Neural Filters menu: one Adobe page says File > Neural Filters, another route is Filter > Neural Filters. (ADOBE-SUMMARY, mixed.) Look in both places.
- Adobe says wording "may differ slightly by version". If a menu is not where this guide says, use **Help**, then **Search** or the search icon at the top right (NOT VERIFIED).

---

## STAGE 2: Scan or phone-photo prep, crop, straighten (10 minutes)

If the photo is a flat scan, skip to step 4.

1. For a phone photo of a print: use daylight from a window, no flash, phone held directly over the print, flat surface. Do this before you open Photoshop (NOT VERIFIED, common practice).
2. In the Layers panel click the `work` layer so it is highlighted.
3. In the left toolbar click the **Crop tool** (looks like two overlapping corners). Shortcut C (NOT VERIFIED).
4. Look at the options bar at the top of the screen. Find the checkbox **Delete Cropped Pixels**. Make it **unchecked**. (ADOBE-SUMMARY: Adobe says to uncheck Delete Cropped Pixels so "you can recover any areas you crop away".)
5. Find **Content-Aware** in the same bar and make it **unchecked** for now. (ADOBE-SUMMARY: Adobe says Content-Aware fills empty edges with matching content. That is a computer guess at what is missing. Keep it off.)
6. To straighten: put the cursor just outside a corner of the crop box. It turns into a curved arrow. Drag a little to rotate until the edge of the photo is level. (ADOBE-SUMMARY: "click outside a corner of the crop boundary and drag to rotate".)
7. Drag the box edges so the white border and desk are cut off. Keep all of the picture.
8. Press Enter to apply.

**CHECKPOINT 2:** The photo edges look level and no desk shows. Press **Ctrl+0** (zero) to fit it on screen (NOT VERIFIED). Good? Save with **Ctrl+S**.

---

## STAGE 3: Fix brightness and contrast with Levels (10 minutes)

Old photos look gray and flat. Levels fixes that without changing what is in the picture.

**Word you need:** **Histogram**: a hill-shaped graph of how many dark, middle, and light dots the photo has.

1. Click the `work` layer.
2. Click **Layer**, then **New Adjustment Layer**, then **Levels**. Click **OK** in the New Layer box. (ADOBE-SUMMARY: "Layer > New Adjustment Layer > Levels, then click OK in the New Layer dialog".) An adjustment layer is a correction sheet that sits on top, so the photo itself is not changed.
3. The **Properties** panel opens with a histogram and three small triangles under it: black on the left, gray in the middle, white on the right.
4. Drag the **black** triangle right until it touches the left edge of the hill. (ADOBE-SUMMARY: "dragging them to the edge of the first group of pixels in the histogram maps those tones to 0 and 255".)
5. Drag the **white** triangle left until it touches the right edge of the hill.
6. Hold Alt (Windows) while you drag a triangle to see clipping, which is where detail is being lost. (ADOBE-SUMMARY: holding Alt while dragging previews clipping.) If large areas go pure black or pure white, back off a little.
7. Drag the **gray** triangle left or right until the middle tones look natural. Check the face. The face should not be a bright white blob or a dark mask.
8. Do not use the eyedroppers on a first try. Adobe warns eyedropper use overrides earlier Levels changes, so use them first if you use them at all. (ADOBE-SUMMARY.) Do not pick a shiny highlight as the white point. (ADOBE-SUMMARY.)

**When to use Curves instead:** Curves does the same job with more control across many tones. Adobe says Levels suits simpler corrections, Curves gives more precision. (ADOBE-SUMMARY.) For a beginner, use Levels. Add Curves later: **Layer, New Adjustment Layer, Curves**, then drag one small point at a time, a little.

9. Click the eye icon next to the adjustment layer to hide it, then show it again. This is your before and after for brightness.

**CHECKPOINT 3:** Photo looks clearer, not harsh. Face still has soft shading. Save (Ctrl+S).

---

## STAGE 4: Dust and scratches (15 to 25 minutes)

**Which tool for which job:**

| Problem | Use this | Why |
|---|---|---|
| Lots of tiny white specks across a smooth area (sky, wall, clothing) | Dust & Scratches filter, on a masked copy | Fast, but it blurs, so you limit where it works |
| A few individual spots | **Spot Healing Brush** on an empty layer | One click per spot, picks its own source |
| A scratch line, or a spot near an edge | **Healing Brush** | You choose the clean source area |
| A spot where texture or a hard edge must match exactly | **Clone Stamp** | Copies pixels exactly, no blending, most control |
| Larger object, big blotch | **Remove tool** with Generative AI OFF | See the AI section. Not for faces |

### 4A. Dust & Scratches filter on a masked copy (small specks only)

A **mask** is a paint-on switch. White shows an effect, black hides it.

1. Click the `work` layer. Press Ctrl+J to duplicate it (or Layer, New, Layer Via Copy). Rename the copy `dust`.
2. Click **Filter**, then **Noise**, then **Dust & Scratches**. (ADOBE-SUMMARY, older Adobe page: "Filter > Noise > Dust & Scratches".) A small box opens with Radius and Threshold sliders.
3. Set **Threshold** to its top value, and **Radius** to 1 pixel. (ADOBE-SUMMARY: "Start with a low value (1 or 2 pixels), and increase it only as needed. Higher values blur more of the image." Radius slider range 1 to 16.)
4. Slowly drag **Threshold** down until the specks vanish, and stop as soon as they do. (ADOBE-SUMMARY: Threshold decides how different pixels must be to be touched. "Higher values preserve more detail but may leave some defects." 0 examines all pixels.) Do not go to 0 unless you must.
5. Click **OK**.
6. Add a mask that hides everything: hold **Alt** and click the **Add Layer Mask** button at the bottom of the Layers panel (the rectangle with a circle). (NOT VERIFIED for Alt behavior. If your mask comes out white, press Ctrl+I to flip it to black.)
7. Click the **Brush tool** (B). Set the color to white (press D then X if needed). Pick a soft brush at about 30 percent opacity.
8. Paint on the mask over smooth areas only. Do NOT paint on eyes, mouth, hair strands, or text.
9. Adobe offers two safer ways to apply this filter. For editing without damage convert the layer to a Smart Object first. Or apply it to a duplicate layer and lower its opacity or use a layer mask. (ADOBE-SUMMARY.) This guide uses the duplicate plus mask method.

### 4B. Spot Healing Brush on an empty layer (individual specks)

1. Click the **New Layer** button at the bottom of the Layers panel (the paper with a folded corner). Rename it `spots`.
2. Click the **Spot Healing Brush** in the toolbar. (It looks like a bandage with dots. It may be grouped under the Healing Brush. Right click the group icon to see the others. NOT VERIFIED for icon.)
3. In the options bar tick **Sample All Layers**. (ADOBE-SUMMARY: Adobe says "Create a new layer, select Sample All Layers in the Options bar, and apply your spot healing edits to the empty layer while preserving your original image.")
4. Pick a **Type** in the options bar. Choose the content-aware style or proximity match (NOT VERIFIED for exact names). Do not pick any option that says "generative" unless you want credits used.
5. Set the brush size a little bigger than the speck. Use the [ and ] keys (NOT VERIFIED).
6. Zoom to 100 percent: press Ctrl+1 (NOT VERIFIED).
7. Click once on each speck. Do not drag a long stroke across detail.
8. Work in small sections. Move across the whole photo in a grid so you do not miss any.

### 4C. Healing Brush (scratch lines, edges)

1. On the same `spots` layer, click the **Healing Brush** tool.
2. In the options bar find the **Sample** menu and choose **Current & Below** so it can read the photo but writes on your empty layer. (ADOBE-SUMMARY: "Its Sample menu offers Current & Below for working on a separate layer.") Choose **Ignore Adjustment Layers** if offered, so your Levels layer does not get applied twice. (ADOBE-SUMMARY.)
3. Hold **Alt** and click a clean spot beside the scratch. This is the source.
4. Release Alt. Paint over the scratch with short strokes.
5. Pick a new source often. Never reuse one source over and over, that causes repeating patterns.

### 4D. Clone Stamp (exact copy)

1. Make a new empty layer called `clone`.
2. Click the **Clone Stamp** tool. In the options bar set **Sample** to **Current & Below** or **All Layers** so it can see the photo while painting on your empty layer. (ADOBE-SUMMARY: Sample has Current Layer, Current & Below, and All Layers.) Note: Adobe says the Clone Stamp does not work on adjustment layers. (ADOBE-SUMMARY.)
3. Set **Opacity** to about 40 to 60 percent so changes build up gently.
4. Alt click a clean source, then paint in small dabs.
5. Re-pick the source every few dabs. Mix the direction you sample from.

### 4E. Remove tool (only if needed, and read the AI section first)

1. Click the **Remove tool** (NOT VERIFIED for icon, may be grouped with the Healing tools).
2. Look at the **Mode** dropdown in the options bar. Adobe lists Generative AI on, Generative AI off, and Auto (may use generative AI). (ADOBE-SUMMARY, Remove tool page.) Choose **Generative AI off**.
3. Paint over the thing, then release. Keep it off faces entirely.

**CHECKPOINT 4:** Hide the `spots`, `clone`, `dust` layers with their eyes, then show them again. Do the specks come back when hidden? Good, that means the work is on separate layers. Are there new smears or repeating tile patterns when you look at 100 percent? If yes, undo that stroke (Ctrl+Z) and use a different source. Save.

---

## STAGE 5: Creases and stains, away from faces (20 to 30 minutes)

A crease is a white or dark line where paper folded. A stain is a blotch.

1. Make a new empty layer. Name it `creases`.
2. Use the **Healing Brush** (best for creases, because it matches the tone of what is around it) with **Sample: Current & Below**, as in 4C.
3. Zoom in to 100 percent. Work along the crease in short pieces, about as long as your thumbnail on screen.
4. Pick the source area right beside the crease, same tone, same texture.
5. For a stain over cloth, sky, or wall use the **Clone Stamp** at 40 to 60 percent opacity.
6. For a big stain that has color but the texture underneath is fine, make a new layer, set its blend mode to **Color** (blend mode menu at the top of the Layers panel, it says Normal) (NOT VERIFIED), and paint over the stain with a sample of nearby color. This changes color only, not texture.
7. Stop at faces. If a crease crosses a face, see Stage 6.

**CHECKPOINT 5:** Zoom out to fit (Ctrl+0). Squint. Can you still see the crease or stain from arm's length? If yes, go back. Can you see where you worked (blur patches, mirrored shapes)? If yes, undo that part. Save.

---

## STAGE 6: The face rule (10 to 15 minutes, never skip)

**Faces get cleanup only.** That means dust, a thin scratch, an even brightness fix. It does not mean smoothing skin, fixing teeth, opening eyes, shaping lips, or drawing a missing eye.

Why: if the face stops looking like the real person, the customer will not want the photo. This is the one mistake that cannot be fixed afterward.

1. Press **Ctrl+1** to go to 100 percent zoom (NOT VERIFIED). Move around so the whole face is on screen.
2. Click the eye icons to hide all your repair layers. Look at the face. Now show them. Does anything about the eyes, nose, mouth, hairline, or skin age look different? If it looks younger, smoother, or like a different person, that is a fail.
3. Zoom out to fit and look again from a distance. Do the same compare.
4. Allowed on a face: Spot Healing Brush on a single speck, Healing Brush on a thin scratch on skin, Levels or Curves for brightness.
5. Not allowed on a face: Remove tool, Neural Filters, Generative Fill, any blur or skin smoothing.
6. A scratch that crosses an eye, mouth, or the edge of the face: try one careful clone, one pass, at 30 percent opacity. If the eye or mouth shape looks even slightly different from what the photo shows, delete that layer.

**When to back out (any one of these means undo and leave it alone):**
- You cannot tell where the original shape of a feature was.
- The fix takes more than three tries on the same spot.
- Someone who knew the person would say "that does not look like them".
- You are tempted to draw something. Do not.

Backing out is easy because every fix is on its own layer: click the layer, press Delete, or just hide its eye.

When the face cannot be fixed honestly, tell the customer plainly: "the face is too damaged to restore without guessing. I cleaned the rest and left the face as it is." That is the honest limit named in the launch prep.

**CHECKPOINT 6:** Face passes the same-person test at 100 percent and at fit-to-screen.

---

## STAGE 7: Optional color (last, 10 to 20 minutes)

Only if the face passed. Only if the customer wants it.

**Caution: this invents information.** A black and white photo has no color in it. Any color you add is a guess about skin, clothes, and sky. Customers can be unhappy if the guess looks wrong. Offer color as an extra, and always deliver the black and white version too.

1. Make a new empty layer above all the others. Set its blend mode to **Color** (NOT VERIFIED).
2. Use the **Brush tool** with a soft brush, about 20 to 30 percent opacity.
3. Skin: pick a gentle skin color from the Color Picker (click the foreground color square, choose). Paint lightly. Keep it varied, not one flat tone.
4. If you are not sure what color something was (a uniform, a dress), ask the customer, or leave it gray.
5. Do not use Neural Filters Colorize on the main path. It is part of the AI section.
6. Lower the layer opacity to 40 to 60 percent so it looks natural, not painted.

**CHECKPOINT 7:** Does the color look like a painted-on mask? Lower the layer opacity until it looks like a tinted old photo.

---

## STAGE 8: Gentle sharpen and noise (10 minutes)

**Words you need:**
- **Noise** here means film grain, the little speckle in old photos. It is part of the look.
- **Over-smoothing** means rubbing out grain until skin looks like plastic.

1. Make a merged copy at the top without losing your layers: press **Ctrl+Alt+Shift+E** (stamp visible, NOT VERIFIED). A new layer appears on top. Rename it `sharpen`.
2. Click **Filter**, then **Sharpen**, then **Unsharp Mask** (NOT VERIFIED for exact wording, Adobe has a page "Sharpen images with unsharp mask in Photoshop").
3. Start small: Amount 50 percent, Radius 1.0 pixel, Threshold 2 levels. Tick Preview and look at the face at 100 percent.
4. If you see white edges around faces or shoulders, that is a halo. Lower Amount.
5. Lower the layer opacity to 50 to 70 percent.
6. **Leave grain alone.** Do not run Reduce Noise on skin. If the scan has color speckle (red and blue dots), you may use **Filter**, **Noise**, **Reduce Noise** at a low strength on a duplicate layer, with a mask that keeps faces off (NOT VERIFIED). Never aim for smooth.
7. Check the compare: eye icon off, on.

**CHECKPOINT 8:** Face still has grain and texture at 100 percent. No halos. Save.

---

## STAGE 9: Export and file naming (10 minutes)

Keep two files: a layered PSD (your work file) and a JPG (what you deliver).

**Naming rule:** `YYYY-MM-DD-name-short-title-restored.jpg`, example `2026-11-10-practice1-soldier-restored.jpg`. PSD: `2026-11-10-practice1-soldier-restored.psd`. Never overwrite the original. Keep original named `...-original.jpg`.

1. Save the layered PSD: **File**, **Save As**, format **Photoshop (*.PSD)**, folder `04-final`. (NOT VERIFIED for wording.)
2. Make a JPG: **File**, **Export**, **Export As** (NOT VERIFIED for exact path), format **JPG**, quality high, leave the size as it is. Do not upscale. Or use **File**, **Save a Copy** (NOT VERIFIED), choose JPEG.
3. Save to `04-final`.
4. Open the JPG on your phone and look at it. Does it open, and does it look right?

**CHECKPOINT 9:** Two files exist in `04-final`, plus the untouched original in `01-original`.

---

## STAGE 10: Before and after checklist (10 minutes)

Tick every one. This matches the quality bar in the launch prep, section 2.

- [ ] Original file untouched in `01-original`.
- [ ] The face looks like the same person, at 100 percent and at fit-to-screen.
- [ ] No plastic smoothing, no new teeth, no changed expression, no redrawn eyes or mouth.
- [ ] No clone repeats, smears, or halo edges at 100 percent.
- [ ] Damage I fixed is gone.
- [ ] Damage I left alone is written down for the note.
- [ ] Grain and age are kept. It still looks like an old photo.
- [ ] JPG opens on my phone.
- [ ] JPG is at least as large as the original. I did not upscale.
- [ ] No generative or Neural Filter tool was used on any face.
- [ ] Side by side with the original, someone who knew the person would say "that is them".
- [ ] A 3 line note is written: what was repaired, what was left alone, what was too damaged.

If any line is not ticked: redo once. If it still fails, tell the customer and charge nothing.

---

## SECTION: Photoshop AI features (what they cost, and the face rule)

This section is separate on purpose. The main path above uses none of it.

**What Adobe's pages say (ADOBE-SUMMARY, search summaries of the pages listed at the top):**

| Feature | Costs generative credits? | Confidence |
|---|---|---|
| **Remove tool** | Currently NO. Adobe's Generative credits FAQ lists it among features that do not currently consume credits. The Remove tool page says credits are not deducted. Adobe notes the policy could change. Mode options on the tool: Generative AI on, off, or Auto. | ADOBE-SUMMARY. Both pages not opened directly. |
| **Generative Fill** (Adobe Firefly model) | YES. A "standard" generative feature, generally 1 credit per generation. Plans with unlimited standard generations exist. | ADOBE-SUMMARY, plan details not confirmed for Zac's plan. |
| **Generative Fill** (partner models) | YES, more. One Adobe page lists 10 to 40 credits depending on output size. | ADOBE-SUMMARY. |
| **Generative Upscale** | YES, by output size. 10 credits up to 25 MP, 20 credits for 25 to 67 MP. | ADOBE-SUMMARY. |
| **Neural Filters: Photo Restoration** | **NOT CONFIRMED either way.** The search did not find a credit cost for it. Adobe lists it as a Beta filter. | NOT VERIFIED. Check the Generative Credit Usage panel in Photoshop before using it. |
| **Harmonize** | YES, 5 credits per generation. | ADOBE-SUMMARY. |

Credit counts and plan allowances differ by plan and date (Adobe says single-app plans changed in June 2025). Zac's real balance and plan are NOT VERIFIED. Matt's paid Firefly credits are shared and limited, so treat every "maybe" as a "yes it costs" until you see the credit meter stay the same after one test.

**Where each AI tool is:**
- Neural Filters Photo Restoration: Adobe's page says to open Neural Filters, then **All filters**, then download Photo Restoration from the **Beta** section. The menu path differs between pages (File > Neural Filters vs Filter > Neural Filters). Look in both. Adobe's page describes Photo Enhancement and Scratch Reduction, and Colorize as a separate step. Exact slider names were NOT confirmed.
- Generative Fill: appears in the Contextual Task Bar after a selection. (NOT VERIFIED for location.)
- Remove tool: toolbar, with the Mode dropdown above.

**THE RULE: no AI feature on a face. Ever.** Not Photo Restoration, not Generative Fill, not Remove with AI on, not Colorize on skin. These tools guess. A guessed face is a different person. The standard tools in this guide are the only ones allowed near eyes, nose, mouth, hairline, or skin.

**If you ever want to try an AI tool on a non-face area** (a big torn corner of a wall or sky): get Zac's yes first, look at the credit meter before and after one use, run it on a copy, and keep it on its own layer so it can be deleted.

---

## PRACTICE PLAN: three public-domain photos

Rule: **do not download these yet.** Zac says yes first, then Zac downloads them himself, or says "go" and the download is done on his say-so.

All three were chosen by reading catalog and category metadata. **The actual damage on each photo was NOT looked at by Claude**, because that would mean downloading or loading the image. Zac should open each page first and look at the preview. If the damage does not match the label, swap it using the swap tips under each one.

Rights quoted from each item's own page or catalog record, as returned by the site's data (Library of Congress JSON record, Wikimedia Commons file page text). Keep a screenshot of each rights line in the practice folder.

### Practice 1: light damage

- **Item:** [Unidentified soldier in Confederate uniform], Liljenquist Family Collection of Civil War Photographs, Library of Congress, between 1861 and 1865. Carte de visite (a small photo on card). Call number LOT 14043-2, no. 981.
- **URL:** https://www.loc.gov/item/2019630437/
- **Rights statement quoted from its record, Rights Advisory field:** "No known restrictions on publication."
- **What that means:** the Library says it found no known restrictions. The Library's records also say it generally does not own the rights to items and that using it is the researcher's responsibility to assess. (From the Library's standard wording in the search results.) For a practice file this is fine. For a customer job it does not apply.
- **Why it is a good practice case:** the record notes a visible mark: "Number scratched into negative: '448.'" That is a real, documented, small defect. The rest of the photo is likely light wear. Condition NOT VERIFIED by sight.
- **What to fix:** dust specks, small marks, flat tones (Levels). The scratched number mark if it sits in a plain area, with Healing Brush on an empty layer.
- **What to leave:** the soldier's face and uniform detail except for dust, the card edges, the age tone.
- **Skills it practices:** Stages 1 to 4, 6, 8, 9.
- **Swap tip:** if it looks too clean, pick another item in the Liljenquist collection (same rights line), for example 2010650258 or 2014645461. Both show "No known restrictions on publication."

### Practice 2: creases and stains

- **Item:** 80-G-27208, "Using exercise wheel at Pre-Flight School, Chapel Hill, North Carolina, November 1942," official U.S. Navy photograph from the National Archives, on Wikimedia Commons. Commons files it in **Category:Ripped photographs**.
- **URL:** https://commons.wikimedia.org/wiki/File:80-G-27208_(31323126572).jpg
- **Rights statement quoted from its Commons file page:** "This file is a work of a sailor or employee of the U.S. Navy, taken or made as part of that person's official duties. As a work of the U.S. federal government, it is in the public domain in the United States. This file has been identified as being free of known restrictions under copyright law, including all related and neighboring rights."
- **Why it is a good practice case:** Commons' own classification says ripped, which usually means tears and fold lines. Resolution is about 2179 by 2296, big enough for 100 percent work. Condition NOT VERIFIED by sight. The subject is a shirtless man in an exercise scene (the file's own categories say so). If you want something else, use the swap tip.
- **What to fix:** tear lines and creases in non-face areas, stains on the background and floor, tone with Levels.
- **What to leave:** the face except dust, the camera grain, the age.
- **Skills it practices:** Stage 5 (Healing Brush on its own layer, Clone Stamp at low opacity), Stage 4.
- **Swap tip:** browse Wikimedia Commons "Category:Ripped photographs" or "Category:Scratched photographs" and read the license box on the page of any file before saying yes. Only pick files whose box says public domain.

### Practice 3: face damage (honest-limits practice)

- **Item:** "Sofia Jansdotter Wallin family," Wikimedia Commons, family portrait from about 1877 with an inset from about 1907, Sweden. Commons files it in **Category:Scratched photographs**.
- **URL:** https://commons.wikimedia.org/wiki/File:Sofia_Jansdotter_Wallin_family.jpg
- **Rights statement quoted from its Commons file page:** "I, the copyright holder of this work, release this work into the public domain. This applies worldwide. In some countries this may not be legally possible; if so: I grant anyone the right to use this work for any purpose, without any conditions, unless such conditions are required by law." The page's source line says the image comes from the Southerly Clubs of Stockholm, which "donated this picture to the Public Domain," and the page notes Wikimedia VRTS permission ticket 2010092510008875.
- **Caution on the rights:** this is a donation by the image owner, not a government release. It is fine for practice. Do not treat it as a model for customer work.
- **Why it is a good practice case:** a multi-person old portrait, 2413 by 3341, with scratches per Commons' category. People means faces, so you practice the face rule. Whether a scratch actually touches a face is NOT VERIFIED.
- **What to fix:** thin scratches and dust on faces (Spot Healing Brush, one speck at a time, at 100 percent), flat tone (Levels).
- **What to leave:** any damaged face feature you cannot tell the original shape of. Write that in the note instead of drawing it. If a scratch crosses an eye or mouth, try one careful pass, compare to the original, and back out if the shape changes.
- **Skills it practices:** Stage 6 (the face rule), Stage 4, Stage 8, Stage 10.
- **Swap tip:** if no scratch touches a face, use another file from Commons "Scratched photographs" with a clear public domain license box. Note: the Norwegian National Library group photo in that category (title says "sterkt skadet", heavily damaged) is public domain only under Norwegian law per its own license box, and it is heavily damaged, so skip it as a beginner case.

### What is not in the plan
- No National Archives (catalog.archives.gov) item was used. Its pages did not load for the page fetcher, so no rights statement could be quoted from one.
- The two Library of Congress Rosa Parks Papers photos that were checked ("Mount partially torn at the bottom", "Postcard torn on upper left side") say "Publication may be restricted." Do not use them.

---

## TROUBLESHOOTING

**It looks plastic.**
Cause: too much blur, too much sharpen on skin, or noise reduction on a face. Fix: delete the layer that smoothed it. Lower the layer opacity to 30 percent. Keep the grain. Redo only the part that needed it with a small Spot Healing Brush.

**There are halos (light or dark outlines around heads and shoulders).**
Cause: Unsharp Mask Amount too high, or too large a Radius. Fix: undo, run it again with Amount 30 to 50 and Radius 0.5 to 1. Lower the sharpen layer opacity.

**I see repeating patterns (little tiles, mirror shapes).**
Cause: cloning from the same source over and over. Fix: undo the strokes. Re-pick sources often, use smaller dabs, lower opacity to 40 percent. Use the Healing Brush instead, which blends tone.

**The color looks fake.**
Cause: painted color too strong or too flat. Fix: lower the color layer opacity to 30 to 50 percent. Use several shades, not one. If unsure, leave that part gray. Offer the black and white copy.

**The healed spot looks like a smudge.**
Cause: brush too big or sample area wrong tone. Fix: undo. Shrink the brush so it is just bigger than the spot. Source from beside it, same tone.

**The Dust & Scratches filter ate the detail.**
Cause: Radius too large, Threshold too low. Fix: undo. Radius 1, raise Threshold. Use the mask so it only touches smooth areas. (ADOBE-SUMMARY on Radius and Threshold.)

**The edges of the crop look strange or filled with odd content.**
Cause: Content-Aware crop is on. Fix: turn Content-Aware off in the Crop tool options bar, redo the crop.

**I cannot find a menu.**
Photoshop's menus vary by version. Look at the version you wrote down in Stage 1. Search for the tool name in the Help menu or the search icon (NOT VERIFIED). Adobe's own help pages say wording may differ.

**I used an AI tool by accident.**
Delete that layer. Check the credit meter. Tell Zac. Redo with the standard tools.

---

## Open items for Zac

1. Say yes or no to the three practice downloads (name them, or give a go-ahead). Open each URL first and look at the preview to see if the damage matches.
2. Write your Photoshop version at Stage 1 step 2 and tell Claude, so the guide can be adjusted.
3. Check the Photoshop credit meter before using any AI feature, and decide what Matt's shared credits are allowed to be spent on.
4. Check Adobe's current terms for commercial restoration work (from the launch prep, still unverified).
5. Adobe help pages returned 403 to every automated fetch, so every "ADOBE-SUMMARY" label means "reported by a search summary of the page", not "read directly". Spot check the three that matter most: the Remove tool page, the Generative credits FAQ, and the Neural Filters FAQ (Photo Restoration credit cost is unconfirmed).
