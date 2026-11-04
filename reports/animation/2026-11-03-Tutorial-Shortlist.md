# Animation Tutorial Shortlist (research, 2026-11-03)

Read-only web research for Zac's Animation department. Free sources only, no logins, no VidIQ, nothing installed.

## How this was verified (read first)
- YouTube channel pages and watch pages do NOT return usable data to the fetch tool (only footer text). Durations and chapter lists were NOT obtainable for any video. Every length below is "not available".
- What WAS verified: the official YouTube RSS feeds (`youtube.com/feeds/videos.xml?channel_id=...`) return the latest 15 uploads with exact title, URL and publish date. All dates below come from those feeds.
- Captions: YouTube pages did not confirm caption tracks. "Likely" means English-language, spoken-tutorial channel, so auto-captions are normally present. UNVERIFIED for every video. Pull with yt-dlp `--write-auto-subs` at transcript time and report any failure.
- Feeds only show the newest 15 uploads per channel, so older evergreen videos (e.g. Ryan King's Oct 2024 sculpting video) were found via search and have no feed-confirmed URL.

## Channel coverage
| Channel | Channel ID (from feed) | Feed checked | Result |
|---|---|---|---|
| Blender Guru | UCOKHwx1VCdgnxwbjyb9Iu1g | yes | Active, 2026 uploads incl. a private jet and Backrooms build |
| Grant Abbitt | UCZFUrFoqvqlN8seaAeEwjlw | yes | Active, 10+ part character series Oct 2026, car video |
| CG Boost | UCWWybvw9jnpOdJq_6wTHryA | yes | Latest 15 are shorts and trailer making-of. Nothing on topic. Landscape/environment content is their PAID course (Master 3D Environments), skip |
| Ducky 3D | UCuNhGhbemBkdflZ1FGJ0lUQ | yes | Motion graphics / geometry nodes / materials. Nothing on topic. Weak fit for all three skills |
| Ryan King Art | UCIXjev1_mJ1plJhF9lGarQg | yes | Active, sculpting and texture content in Oct to Nov 2026 |
| William Faucher | UCGKjGGjdl-GzEcFPf1EQwqw | yes | Sparse uploads, a few strong UE rendering and landscape-adjacent videos |
| Smart Poly | UCp1e34nrTQqVXkNU5ekH9CQ | yes | Almost entirely AI-tool and news videos (UE 5.8 mentioned). Nothing on topic |
| Beardgames | UCaBjhTykCgcQQP5Ecqq9_CQ | yes | Gameplay-framework channel (combat, climbing), last upload Sep 2025. Nothing on topic. Possibly not the channel Zac meant, ask him |
| Unreal Sensei | UCue7TFlrt9FxXarpsl872Dg | yes | Active, UE news and a landscape video (Jun 2026) |
| Virtus Learning Hub | not available (handle @VirtusEdu) | no | Could not resolve a feed. Search says mostly UE4-era courses plus a Blender modelling course. Unverified, nothing recommended |
| Unreal Gaimedev | not available | no | Could not find a channel with this name. Ask Zac for the exact name or link |

## 1. Sculpting and retopology
Honest gap: no 2025/2026 video on retopology specifically was found in the feeds of these channels. Retopology is the weak spot.

1. **Sculpting a Girl Marble Bust Statue in Blender (Full Tutorial)** - Ryan King Art
   - https://www.youtube.com/watch?v=-CUyPta7-IU
   - Published 2026-10-27 (feed). Length: not available.
   - Fit: most recent full-length sculpt tutorial from the channel on the list that teaches sculpting a head and bust. Good for the sculpt half of the skill. Blender version not stated, so check it opens cleanly in 5.x before relying on tool names.
   - Captions: likely (UNVERIFIED).
2. **Use this Tool for Sculpting Ears in Blender** - Ryan King Art
   - https://www.youtube.com/watch?v=Tjv322yodNw
   - Published 2026-10-17 (feed). Length: not available (likely short).
   - Fit: a focused anatomy-detail tip, useful for character sculpt checklists. Supplement only.
   - Captions: likely (UNVERIFIED).
3. **How to Model Characters in Blender (Step-by-Step for Beginners), Parts 1 to 10** - Grant Abbitt
   - Part 1: https://www.youtube.com/watch?v=TwkcUYXK3yA (2026-10-08). Parts 2 to 10 published 2026-10-10 through 2026-10-28, URLs in the feed list: Part 2 U07KQdn4vtY, 3 hQ5wvO5ktFw, 4 CAuyGkfuymY, 5 gHnFExpcWek, 6 -LK-8Qmi_H0, 7 df87mDo7eow, 8 jasoAsjYqoA, 9 DnoFQ4K1AoU, 10 rs7LOOx2m_I (all `youtube.com/watch?v=`).
   - Length: not available. Whether the series covers sculpt or retopo: NOT verified (titles say modeling only). Needs a transcript skim before it is assigned to this skill. It is poly-modeling oriented, so it fits `blender-character-craft` more than sculpt.
   - Captions: likely (UNVERIFIED).
4. **Retopology for Beginners (Blender Tutorial)** - Ryan King Art. OLDER, flag.
   - Published June 2024 per BlenderNation (https://www.blendernation.com/2024/06/21/retopology-for-beginners/). Exact YouTube URL not available (BlenderNation page does not link it). Predates Blender 5 by over a year. Basic retopo ideas (shrinkwrap, snapping, poly build) hold, UI details may differ.
   - Also from Ryan King: "Sculpting for Complete Beginners! (Blender Tutorial)" Oct 11, 2024 (vidiq stats page, 828K views). Older than 2025, flag as possibly dated; URL not available.

Recommendation: use Ryan King's 2026 sculpt videos as the primary, add his 2024 retopo as a flagged older reference, and ask Zac for one retopo video if he has a favorite.

## 2. Environment and landscapes (rock hill, terrain)
Honest gap: none of the listed channels has a 2025/2026 free rock-hill or terrain video in its newest-15 feed. Findings:

- **Grant Abbitt, Blender Environment Artist: Create 3D Worlds in Blender 5.1** is a PAID GameDev.tv / Udemy course (rock and tree section, landscape section). Not free, so out of scope unless Zac supplies it like Blenderfast.
- **CG Boost, Master 3D Environments in Blender**: PAID course. Skip.
- **Ryan King Art, Creating Realistic Rocky Mountains in Blender, Parts 1 to 3**: free on YouTube, January 2023 (per BlenderNation: https://www.blendernation.com/2023/01/05/creating-realistic-rocky-mountains-in-blender/). Part 1 https://www.youtube.com/watch?v=n-c2MMLmNBw, Part 3 https://www.youtube.com/watch?v=rlS9FfmXuYg. Older than 2024, FLAG LIKELY OUTDATED for Blender 5. Best free rock-and-mountain match on the channel list, usable for the method with version-translation. Length: not available. Captions: likely (UNVERIFIED).
- **Ryan King Art, This Material is Broken in Blender 5.0** (3:32). Blender 5.0 material fix, relevant to terrain materials. Transcript confirmed available on sozai.app (https://sozai.app/transcript/material-broken-blender-5-0/, English with timestamps). YouTube video ID per thumbnail: Wn3YdC1RSPU. Date not available. Use as a Blender 5 gotcha note, not as a terrain tutorial.
- **William Faucher (Unreal side) Unreal Engine 5.7 MEGAPLANTS Crash Course** - https://www.youtube.com/watch?v=3f7miRB9_Eo, 2025-11-12 (feed). Length: not available. Relevant for dressing a terrain in UE after the Blender sculpt. Captions likely (UNVERIFIED).
- **Unreal Sensei, How to Use Unreal Engine's New Landscape System - Mesh Terrain Tutorial** - https://www.youtube.com/watch?v=Lhj2LutYNjA, 2026-06-10 (feed). Length: not available. Best recent UE-side terrain video found. Captions likely (UNVERIFIED).

Recommendation: Ryan King rocky mountains Parts 1 to 3 (older, flagged) for the Blender method, plus Unreal Sensei's mesh terrain video for the UE landscape step. Ask Zac if he wants Claude to search outside the list for a 2025+ Blender 5 terrain video.

## 3. Architecture and vehicles (house, rowboat)
No rowboat tutorial and no house tutorial from the listed channels in the feeds. Closest matches:

1. **How to make a private jet in Blender** - Blender Guru
   - https://www.youtube.com/watch?v=4wxmKLDhsnQ
   - Published 2026-10-17 (feed; blenderguru.com post dated Oct 16). Length: not available.
   - Fit: freshest hard-surface vehicle build from the biggest channel, teaches shape breakdown, panel lines, curved fuselage. Transfers to a rowboat hull. Captions likely (UNVERIFIED).
2. **Car Modeling Traps Most Beginners Fall Into (And How to Fix Them)** - Grant Abbitt
   - https://www.youtube.com/watch?v=zyT4soYpR1I
   - Published 2026-10-15 (feed). Length: not available.
   - Fit: vehicle topology and common mistakes, good for checklist content in the architecture and vehicles skill. Captions likely (UNVERIFIED).
3. **How To Make the Backrooms In Blender** - Blender Guru
   - https://www.youtube.com/watch?v=kBsVJSETydU
   - Published 2026-08-30 (feed). Length: not available.
   - Fit: interior architecture construction (repeating rooms, lighting). Nearest to house structure from the list. Not exterior house building. Captions likely (UNVERIFIED).

Not on the list but seen: "Modeling a simple low-poly House in Blender 5.0" (creator and URL not confirmed) and a BlenderNation medieval textured house tutorial by polygonrunway (2025-09-24, URL not available). Mentioned only as leads.

Recommendation: Blender Guru private jet (vehicle) and Backrooms (interior structure), plus Grant Abbitt's car traps video for topology cautions.

## 4. Blender to Unreal import and UE lighting/render
1. **The 2025 Guide to Rendering in Unreal Engine 5** - William Faucher
   - https://www.youtube.com/watch?v=fVg5ihB8Wdc
   - Published 2025-02-20 (feed). Length and UE version: not available. Predates 5.7/5.8, so settings screens may differ. Still the best rendering walkthrough from the list.
   - Captions likely (UNVERIFIED).
2. **The 2026 Unreal Engine to Davinci Resolve Guide - ACES & sRGB** - William Faucher
   - https://www.youtube.com/watch?v=2Q3CybANHKE
   - Published 2025-04-22 (feed) despite the 2026 in the title. Length not available. Useful for color-managed render output.
3. **Lighting in Unreal Engine 5 for Beginners** - William Faucher
   - 2022-06-10 per vidiq, URL not verified. OLDER than 2024, flag as likely outdated. Only mentioned because it is the channel's most-watched lighting video.
4. **Fundamentals of Lighting in Blender** - Blender Guru, https://www.youtube.com/watch?v=ENnEYoUpFfU, 2026-05-09 (feed). Length not available. Blender-side lighting, matches the render/look check before export.

Blender-to-Unreal import: NO video from the listed channels was found. Unreal Sensei and Smart Poly feeds have none. Virtus Learning Hub could not be checked. The Epic-approved path Animation already picked is the xavier150 add-on (docs live on its GitHub). Gap, ask Zac for a link.

## Not recommended, with reason
- Ducky 3D: motion graphics and geometry nodes content, not modeling or environments.
- CG Boost: newest 15 are shorts and trailer making-of, landscape lessons are paid.
- Smart Poly: AI-tool news and tests, no fundamentals.
- Beardgames: Unreal gameplay frameworks, nothing on assets, environments or lighting.

## Open questions for Zac
1. Virtus Learning Hub: please send a link or two. Could not resolve its channel feed.
2. "Unreal Gaimedev": no such channel found. Did he mean Gamedev.tv or another name?
3. Beardgames content does not match the skills. Confirm the name.
4. Want Claude to search outside the list for a 2025+ Blender 5 terrain video and a retopology video, since the list has gaps there?
5. Grant Abbitt's Blender 5.1 Environment Artist course covers rocks and landscape but is paid. If Zac supplies it himself (like Blenderfast), it would solve topic 2.

## Next step (not done)
Transcript pull via yt-dlp for the chosen videos, to be done by the owner of the skill-writing job. No transcripts were fetched in this pass.

## Gap fill (outside Zac's list)
Researched 2026-11-03, WebSearch/WebFetch only, free videos only, nothing installed or spent.

How verified: YouTube search results (domain filter youtube.com) gave the video IDs; the YouTube oEmbed endpoint confirmed exact title and channel for each URL below unless noted. Upload DATES, durations and caption tracks were NOT obtainable (watch pages and channel pages return only footer text, third-party mirrors blocked or unreachable, and channel IDs needed for RSS were not resolvable). So every date below is "not available" unless a version number in the title implies a window. Captions are "likely" (spoken English tutorials) and UNVERIFIED. Pull with yt-dlp at transcript time and report failures. The "older than 2024" flag is applied only where a version number or the search tool's relative age shows it.

### Gap 1: Retopology (characters/creatures)
1. **EASY and COMPLETE Character RETOPOLOGY Tutorial | Blender 5.1** - Proj Prod Blender (@ProjProdBlender)
   - https://www.youtube.com/watch?v=RneUcVxeqRg
   - Date: not available (title says Blender 5.1, so a 2026 video). Length: not available.
   - Fit: full-character retopo on the current Blender version. Best version match. Search blurb says it covers a full stylized character; exact body scope unverified.
   - Captions: likely (UNVERIFIED).
2. **How I Retopologize Stylized Characters in Blender** - Vertex Arcade (@VertexArcade)
   - https://www.youtube.com/watch?v=0aPr51sDkxE
   - Date: not available. The search tool described a "full stylized character" video as about 210 days old (roughly April 2026) but did not tie that age to this ID, so unconfirmed. Length: not available.
   - Fit: stylized character workflow, focus on the head. Good second opinion on face edge flow.
   - Captions: likely (UNVERIFIED).
3. **Nitro Retopo 1.5.0: Step-by-Step Character Retopology in Blender** - Adrien Rouquie
   - https://www.youtube.com/watch?v=wPj5dYqoxXQ
   - Date: not available (search said about 21 days old, unconfirmed). Length: not available.
   - Caution: demonstrates a third-party add-on (Nitro Retopo). Price and license NOT checked. Free-only rule: do not install it. Use only for retopo principles, or skip.
   - Captions: likely (UNVERIFIED).
- Not chosen: "Retopology in Blender (Beginner Tutorial)" X2GNyEUvpD4 (search says about 4 years old, Blender 3.0+, FLAG OLDER than 2024).

### Gap 2: Terrain / rock hill / landscape
1. **Blender 5.0 Geometry Nodes: Easy Procedural Landscapes & Instances** - Patterns and Nodes
   - https://www.youtube.com/watch?v=FJKaycLH13Y
   - Date: not available (Blender 5.0 in title, so late 2025 or later). Length: not available.
   - Fit: only result explicitly labeled Blender 5. Noise-driven landscape deformation plus instancing (Distribute Points). Good for hills and scattering rocks. Not a sculpted rock-face tutorial.
   - Captions: likely (UNVERIFIED).
2. **Create Procedural Landscapes with Geometry Nodes!** - Ryan King Art
   - https://www.youtube.com/watch?v=5avrqTMYOCs
   - Date: not available. It is NOT in his newest-15 feed as of 2026-11-03, so it is older than 2026-10-15. His related landscape-presets product is listed for Blender 5.1, which hints at 2026 but is not confirmed. Length: not available.
   - Fit: same channel Zac already trusts. The modern counterpart to his flagged-old 2023 rocky mountains series. The video is free; the preset file is a paid product, ignore it.
   - Captions: likely (UNVERIFIED).
3. **How I Create Rocky Landscapes in Blender Procedurally** - Jared Brashier (@jbr4sh)
   - https://www.youtube.com/watch?v=UksaACgPSeU
   - Date and Blender version: not available. Fit: rocky focus, closer to the rock-hill drill. Version unknown, verify nodes work in 5.x before assigning.
   - Captions: likely (UNVERIFIED).
- Also seen, not verified: BlenderNation post dated 2026-09-24 (from the URL) "Create This Simple Realistic Landscape in Blender" (Yeho Studios), https://www.blendernation.com/2026/09/24/create-this-simple-realistic-landscape-in-blender/. YouTube link not retrieved. Worth a look as a fourth option.

### Gap 3: Blender to Unreal import pipeline
Honest result: only one candidate names a UE 5.6+ version.
1. **How to Export Blender 3D Models to Unreal Engine 5.8 (Collision Setup Tutorial)** - Freedom Arts 3D Workflow (@FreedomArts3D)
   - https://www.youtube.com/watch?v=Po7Wb-wE-8k
   - Date: not available (UE 5.8 in title, so 2026; search put it at roughly 83 to 98 days, unconfirmed). Length: not available.
   - Fit: only candidate that names the installed engine (Zac has 5.8.4). Covers collision setup. Scale and materials coverage unverified.
   - Captions: likely (UNVERIFIED).
2. **Complete Guide: Exporting Blender Models and Animations to Unreal Engine 5 | Seamless Workflow** - Ben Shukrallah
   - https://www.youtube.com/watch?v=BwUgj_K4y-c
   - Date and UE version: not available. Fit: models plus animations, general pipeline. Verify against the 5.8 import dialog.
   - Captions: likely (UNVERIFIED).
3. **[Blender to Unreal Engine 5] Correct FBX Export Settings for Characters** - Daniel Kreuter
   - https://www.youtube.com/watch?v=YbWfoyf4MqI
   - Date and UE version: not available. Fit: character FBX settings, root scale and bone axes, where imports usually break.
   - Captions: likely (UNVERIFIED).
- Written cross-check seen in search, NOT verified against Epic docs: keep Blender unit scale 1.0 and export with Apply Scalings = FBX All; Blender's FBX exporter reads only the Principled BSDF; one guide says the UE 5.6+ import dialog differs from the legacy FBX importer. One video (wyn6EpC85yg) argues glTF over FBX for materials, which conflicts with the FBX advice and is one creator's opinion. Epic's FBX import docs and the xavier150 add-on docs remain the authority.
- Caution: UE 5.8 and the Blender 5.x FBX exporter are new, so any video older than 2026 may show different menus.

### Bonus: House
1. **Design a Medieval House From Scratch | Blender Beginner Tutorial** - Basic 3rd Dimension
   - https://www.youtube.com/watch?v=LqyFRxu1gOk
   - Date: not available (search said about 62 days old, unconfirmed, roughly early Sept 2026). Blender version not stated. Fit: full house with structure and timber detail, best recent whole-house result.
2. **How to Model the Roof & Floor - Pt 5: Building a House in Blender** - My 3D POV
   - https://www.youtube.com/watch?v=BZet2HL0Yzs
   - Date: not available (search said about 211 days). Part 5 of a series, parts 1 to 4 URLs not retrieved. Boolean-based modeling.
- Flag: the "modern house" and "simple house" timelapse results were about 2,890 days old (about 8 years). OLDER than 2024, skip.

### Bonus: Rowboat
1. **How to create a row boat in Blender** - BlenderBrit
   - https://www.youtube.com/watch?v=jkXo3fHL67Q
   - Date and Blender version: not available. Search says it models from top and side reference images with mirror, solidify and bevel modifiers. Best rowboat-specific match. Likely several years old (UNVERIFIED): method valid, UI possibly dated.
2. **Blender for Beginners: How to create a rowboat on a lake** - channel not checked
   - https://www.youtube.com/watch?v=J4F-wJHdWUU
   - Date not available. Scene-oriented, less about hull shape.
- Flag: "Blender Simple Boat Hull" (aWoB5x6VPkc) reportedly uses Blender 2.49b, far older than 2024, skip. "Animated Boat Tutorial in Blender 3.2" is also pre-2024.

### Still missing
- Exact upload dates and lengths for every item above (blocked by YouTube pages). A yt-dlp metadata pass (`--skip-download --print upload_date,duration`) should confirm before any transcript job.
- A UE 5.6+ import video whose content (scale, materials) is verified.
- A confirmed Blender 5.x rock-face sculpt tutorial; Gap 2 items 1 and 2 are terrain-scale, not rock-detail.
