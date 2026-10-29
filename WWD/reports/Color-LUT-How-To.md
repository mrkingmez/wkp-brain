# How to load a .cube LUT (Premiere and free DaVinci Resolve)

LUTs live in `P:\WWD Kit\Color\`. Always try Safe first. Check faces on your own screen every time.

Rewritten 2026-10-25 (wwd-color sandbox test) after checking the steps against Adobe's and Blackmagic's documentation. See "What was checked" at the bottom. Three of the old steps were wrong and are fixed below.

## Premiere Pro (load one LUT on one clip)
1. Click the clip once on the timeline.
2. Open the Lumetri Color panel: Window > Lumetri Color.
3. Click Basic Correction to open it.
4. Find the Input LUT dropdown (it says None).
5. Click the dropdown, then click Browse.
6. Go to `P:\WWD Kit\Color\`, pick the .cube file, click Open.
7. The Input LUT has NO strength slider (the Intensity slider only works for LUTs loaded in the Creative tab, see next section). If the look is too strong, use the Creative tab method below, or the adjustment layer method and lower its Opacity.
8. Match LUTs (cam to cam) go on the SOURCE clip only (for example the Winter Wolf cam).

## Premiere Pro (strength control: use the Creative tab)
1. Click the clip, open Lumetri Color (Window > Lumetri Color).
2. Click the Creative section.
3. Click the Look dropdown, then click Browse, pick the .cube file, click Open.
4. Drag the Intensity slider left to weaken the look, right to strengthen it.
Note: the Input LUT runs before the Basic tab controls, the Creative Look runs after them, so the result can differ slightly between the two methods.

## Premiere Pro (one look on every clip)
1. Make an adjustment layer: File > New > Adjustment Layer (or in the Project panel click the New Item button, then Adjustment Layer). Click OK in the Video Settings box.
2. Drag it from the Project panel onto a video track ABOVE the clips. Drag its right edge to cover the whole video.
3. Click the adjustment layer on the timeline, then load the LUT in Lumetri Color (Creative > Look > Browse for the Intensity slider).
4. To soften it another way, click the adjustment layer, open Effect Controls (Shift+5), and lower Opacity.
(The old step said Layer > New > Adjustment Layer. That menu is After Effects, Premiere does not have it.)

## DaVinci Resolve (free)
1. Click the Color tab at the bottom.
2. Click the clip in the timeline strip at the bottom.
3. Right-click the node in the Node Editor (the numbered box).
4. Click LUT, then 3D LUT, then pick the .cube file name. (A .cube is a 3D LUT. The LUT menu also has 1D Input LUT, 1D Output LUT, DCTL and CLF, ignore those.)
5. First time only, if the list does not show the file: click the gear icon at the bottom right (Project Settings), click Color Management on the left, find Lookup Tables, click Open LUT Folder. Copy the .cube file into the folder that opens (Windows default: `C:\ProgramData\Blackmagic Design\DaVinci Resolve\Support\LUT`, ProgramData is a hidden folder, the button opens it for you). Back in Project Settings click Update Lists, then Save. Redo steps 3 and 4.
6. Other way: click the LUT Browser button at the top of the Color page, find the LUT, drag it onto the node. If it is not listed, right-click in the browser area and choose Refresh.
7. To weaken it: click the LUT node ITSELF (not a new node), open the Key palette (the key icon in the row of palettes under the viewer), find Key Output, and lower Gain below 1.00. At 0 the node does nothing, at 1.00 it is full strength.

## What was checked, and what was not (2026-10-25)

Confirmed in Blackmagic's official DaVinci Resolve 19 Reference Manual (https://documents.blackmagicdesign.com/UserManuals/DaVinci_Resolve_19_Reference_Manual.pdf, chapter 148 "Using LUTs", chapter 6 Project Settings, Key palette section):
- Right-click a node, then LUT submenu with 1D Input LUT, 1D Output LUT, 3D LUT, DCTL, CLF. Confirmed.
- LUT Browser: drag onto a node, or right-click and Refresh. Confirmed.
- Open LUT Folder and Update Lists buttons exist in the Lookup Tables settings of Project Settings, Windows default LUT folder as written above. Confirmed.
- Project Settings opens with the gear button at the bottom right. Confirmed. (The old step said File > Project Settings, the manual does not say that, so it was removed.)
- Key Output Gain on the node itself sets how strong that node is, 0 none, 1.00 full. Confirmed. The old step said to add a second node after the LUT node, that would not weaken the LUT, it was wrong.
- Add serial node is Option-S in the manual (Alt-S on Windows is the usual mapping). Not used any more.
- Not confirmed by the manual: that the item in the left list is literally named Color Management on every build (the 19 manual says the Lookup Tables controls sit in the Color Management panel, and also calls them "the Lookup Tables panel"). If your list shows Lookup Tables as its own item, click that.
- Not confirmed: that the free version's menu is identical to Studio. The manual has no free-version LUT warning and LUTs are a core Color page feature, but nobody ran the free build here.

Confirmed from Adobe's help pages through search results (Adobe's own pages returned HTTP 403 to direct fetch from this machine, so the wording comes from the search summaries of these pages, not from reading them):
- "Add Look-up Tables in Premiere" (https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/add-look-up-tables.html): Window > Lumetri Color, select a clip on the timeline, Basic Correction tab, Input LUT dropdown, Browse to load a LUT from anywhere on the computer.
- "Apply Lumetri looks in Premiere" (https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/apply-lumetri-looks.html) and the older https://helpx.adobe.com/premiere-pro/using/creative-lumetri-looks.html: Creative tab Look and the Intensity slider ("Drag the slider to the right to increase the effect of the applied look").
- "Install custom Look-up Table files in Premiere" (https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/install-custom-look-up-table-files.html): LUTs in the Creative folder show under Creative > Look, Technical folder under Basic Correction > Input LUT, restart Premiere after adding files. Adobe also notes that in Premiere 24.0 and later the color-management Input LUT sits at Modify > Color > Input LUT.
- "Create adjustment layers in Premiere" (https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/create-adjustment-layers.html): File > New > Adjustment Layer or Project panel New Item, drag above the clips, Effect Controls is Shift+5.
- Community-only, not Adobe documentation: the Input LUT has no working Intensity slider (greyed out), see https://community.adobe.com/bug-reports-728/luts-intensity-slider-greyed-out-1330479. Also community-only: Browse inside the Creative Look dropdown (works in practice per forum posts, the Adobe page text I could see only describes the Creative folder). If Browse is missing in your Look dropdown, copy the .cube into the Creative folder (Windows user folder per Adobe's community FAQ: `C:\Users\<you>\AppData\Roaming\Adobe\Common\LUTs\Creative`, not confirmed on Premiere 2026) and restart Premiere.
- NOT verified on Premiere 2026 (version 26): nobody opened it. Menu labels may have moved. If a label does not match your screen, stop and tell wwd-director.
- Opacity on an adjustment layer in Effect Controls: standard behavior, but not quoted from an Adobe page.
