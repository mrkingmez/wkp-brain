# Animation tutorial picks, Blender and Unreal

Date 2026-11-05. Requested by animation-director for Zac. Facts pulled 2026-11-05, view counts move daily.
Team versions are Blender 5.2.4 and Unreal 5.8.4. Nothing was downloaded, no transcripts or captions were saved, no signups, no spend.
Blenderfast paid track is excluded as ordered.

## APPROVE THESE (mark YES or NO)

Top pick per topic comes first. Run time is the video length. Version is what the video was made in, or "not stated" with my best inference.

SCULPTING
- S1 TOP. Ryan King Art, "Sculpting for Complete Beginners! (Blender Tutorial)", 54 min, Blender 4.3, uploaded 2024-10-11. YES / NO
- S2. Grant Abbitt, "Master Blender Sculpting: Every Brush Explained", 44 min, Blender 4.x, uploaded 2024-12-20. YES / NO

RETOPOLOGY
- R1 TOP. Ryan King Art, "Retopology for Beginners (Blender Tutorial)", 22 min, version not stated (June 2024, probably 4.x), includes baking. YES / NO
- R2. CG Boost, "Retopology in Blender (Beginner Tutorial)", 14 min, Blender 3.0, uploaded 2022-03-16, older, uses add-ons. YES / NO

LANDSCAPE AND TERRAIN FOR UNREAL
- L1 TOP. Unreal Sensei, "How to Use Unreal Engine's New Landscape System - Mesh Terrain Tutorial", 66 min, made for the Unreal 5.8 Mesh Terrain feature (experimental), uploaded 2026-06-10. YES / NO
- L2. Unreal Sensei, "Unreal Engine 5 Landscape Material - UE5 Tutorial", 60 min, UE5 (5.3 era, inferred), uploaded 2023-11-08, classic Landscape tool. YES / NO
- L3 optional. Smart Poly, "Make An Open World Map in 20 Minutes", 23 min, UE5 (version not stated), uploaded 2024-08-23. YES / NO

HOUSE AND BUILDING
- H1 TOP. Ryan King Art, "Stylized Low Poly Wooden Cabin (Blender Tutorial)", 29 min, version not stated (Jan 2025, probably 4.x). YES / NO
- H2. Blender Guru, "How to make an abandoned house in Blender - Tutorial", 26 min, version not stated (Oct 2021, likely 2.9x or 3.0). Mostly texturing. YES / NO

BOAT, HULL, VEHICLE (gap, see section 4)
- B1 TOP for hull method. Blender Guru, "How to make a private jet in Blender", 3 hr 24 min, version not stated (Oct 2026, likely 5.x). YES / NO
- B2. Grant Abbitt, "Make a Low Poly Hot Rod in Blender" series, 4 parts, about 57 min total, Blender version not stated, uploaded 2026-08-28 to 09-03. YES / NO
- B3 optional. Grant Abbitt, "Low Poly Boat Animation - Breakdown - Blender 3", 14 min, Blender 3, 2022, only 3 minutes of boat modeling. YES / NO
- Boat DECISION. Look outside the five channels for one real boat or hull video? YES / NO

UNREAL IMPORT AND LIGHTING (5th section)
- U1 TOP. Unreal Sensei, "Unreal Engine 5 Beginner Tutorial 2026 - UE5 Starter Course", 5 hr 50 min, Unreal 5.8, uploaded 2026-10-19. Use the chapters, not the whole thing. YES / NO
- U2 optional. William Faucher, "Lighting in Unreal Engine 5 for Beginners", 45 min, UE5.0 era, uploaded 2022-06-10. YES / NO

If Zac says yes, next step is the transcripts from the approved picks, then the three skills and the graded drills.

---

## How I verified

- WebFetch on YouTube returns only the page title and footer, so it could not confirm anything. The claude-in-chrome tools are not in my toolset this run.
- So I used `yt-dlp` (already installed on this PC, version 2026.10.21) in metadata-only mode, flags `--skip-download` and `-J`. It reads the live watch page data. It downloaded no video, no audio, no caption files. Search results came from `ytsearch` in flat mode.
- Every URL below came back from a live watch-page read today with the title and channel matching. Upload date, length, views, chapter list and caption track list are straight from that read.
- "Captions" here means the caption track list on the watch page. I know a track exists, I have not read the text. I saved none.
- Version rule. Only a version written in the title, the description, or on the channel's own page counts as stated. Anything else is marked "not stated" with an inference from upload date, flagged INFERRED.
- "Virtus Learning Hub" is a channel that now shows on YouTube as Tinkr Academy. The search for Virtus returned only Tinkr Academy videos that mention Virtus Hub. I treated them as the same channel. Not independently confirmed.
- "Unreal Gaimedev" matched a channel called UnrealGaimeDev. It returned one old UE4 inventory video and nothing on these topics.

---

## 1. Sculpting and retopology

### Sculpting

**S1 TOP. Sculpting for Complete Beginners! (Blender Tutorial)**
- Channel Ryan King Art
- URL https://www.youtube.com/watch?v=Lxem4yMs5Dg
- Uploaded 2024-10-11. Length 54:08. Views 834,929.
- Version Blender 4.3 (the description links its own "Blender 4.3 New Brushes" video, so it is the 4.3 era). Not 5.2, brush names and menus may differ slightly.
- Captions English auto-generated track present. No manual track.
- Teaches high poly mesh, sculpt mode, navigation, brushes, strength and radius, pen pressure, symmetry, Remesh and Dyntopo, then sculpts and paints a fish end to end. 22 chapters.
- Why it beats the rest of the channel. It is the one full workflow with a finished result, and it covers Remesh versus Dyntopo, which the team needs before a rock hill drill. His other sculpt videos are heads and busts (hours long, 11k views and under) or the older 2020 version at 1.68 million views, made in a much older Blender.

**S2. Master Blender Sculpting: Every Brush Explained**
- Channel Grant Abbitt (Gabbitt)
- URL https://www.youtube.com/watch?v=5-mNgCpEkCI
- Uploaded 2024-12-20. Length 43:40. Views 140,821.
- Version Blender 4.x (the description says "the latest Blender version" and links Blender 4 videos). Exact number not stated.
- Captions English auto-generated present.
- Teaches every sculpt brush with tips and pitfalls, 51 chapters (draw, clay, crease, grab, pose, face sets, boundary, mask, cloth brushes, and more). Best for a skill the team can look things up in.
- Why it beats the rest of the channel. It is the reference one. His 2023 beginner guide (9N87-yRR5aE, 33 min, 809k views) is broader but older (Blender 3 era, with a 4.5 course link in the text). His 2026 "Sculpt Better Faces in Blender 5" (https://www.youtube.com/watch?v=Lgg39sZF0kI, 2026-02-08, 28:17, 129,231 views, Blender 5, 12 chapters, auto captions) is the only Blender 5 sculpt video found. It is heads only, so keep it as the follow-on for the Wolf Warrior character work, not the first pick.

Also looked at. CG Boost "Sculpting in Blender for Beginners (Full Course)" https://www.youtube.com/watch?v=KURuPAVJ6hM, 2024-07-18, 3:39:54, 748,023 views, version not stated (INFERRED 4.x), English manual and auto captions, 24 chapters, builds a Moai sculpture then lights and renders it. Strong, but 3.6 hours for one statue. CG Boost "Full Advanced Creature Creation Workflow" https://www.youtube.com/watch?v=tQfFlzHJJ88 is 2021, 53 min, version not stated, so older. Blender Guru's sculpt videos are Blender 4.0 (2023, 19:45, 2.26 million views, https://www.youtube.com/watch?v=--GVNZnSROc) and a 2017 detail-sculpt video, old. Ducky3D has no sculpting video in the search results.

### Retopology

**R1 TOP. Retopology for Beginners (Blender Tutorial)**
- Channel Ryan King Art
- URL https://www.youtube.com/watch?v=1myOZaxtHes
- Uploaded 2024-06-19. Length 21:51. Views 162,382.
- Version not stated. INFERRED Blender 4.x from the date.
- Captions English auto-generated present.
- Teaches object setup, snapping, shrinkwrap, the retopology workflow itself (5:28 to 18:39), applying modifiers, and baking high poly detail onto the low poly (19:58). The bake step is what the Unreal import needs.
- The chapter list shows no add-ons. I did not watch it, so whether it needs any is unverified.
- Why it beats the rest of the channel. His other retopo content is inside long character sculpt videos.

**R2. Retopology in Blender (Beginner Tutorial)**
- Channel CG Boost
- URL https://www.youtube.com/watch?v=X2GNyEUvpD4
- Uploaded 2022-03-16. Length 14:14. Views 1,317,214.
- Version Blender 3.0 and up (stated in the description). OLD, over 2 years.
- Captions English manual AND auto-generated present. Manual is the cleanest transcript source in this whole list.
- Teaches a full retopo using free add-ons shipped with Blender (Bsurfaces, F2, LoopTools), snapping and Shrinkwrap, auto merge, relax brush. 14 chapters.
- Risk. Those add-ons ship in a different way in newer Blender (extensions platform). I believe that is true from the Blender 4.2 change but did not verify it for 5.2. UNVERIFIED. The skill must check before teaching it.
- Why it beats the rest of the channel. Shortest and most watched retopo video on the whole list.

Also looked at. Grant Abbitt's three-part "Retopology a Detailed Guide" (Part 1 https://www.youtube.com/watch?v=6sE-p8PcHDo, Part 2 https://www.youtube.com/watch?v=cHQSr3EMCq4, Part 3 https://www.youtube.com/watch?v=R9tdLV6LWrw) is Blender 2.8, uploaded October 2020, 8:44 plus 14:56 plus 43:49. Thorough but old. His 2024 "Blender Made Retopology 10x Easier" https://www.youtube.com/watch?v=RwbG-HAd6Qc is 2:06 long, a news tip only.

Top recommendation for this topic. S1 for sculpting, R1 for retopology.

---

## 2. Landscape and terrain for Unreal (big worlds)

**L1 TOP. How to Use Unreal Engine's New Landscape System - Mesh Terrain Tutorial**
- Channel Unreal Sensei
- URL https://www.youtube.com/watch?v=Lhj2LutYNjA
- Uploaded 2026-06-10. Length 1:06:18. Views 246,964.
- Version. The video does not state a number. Mesh Terrain is the experimental new terrain system that arrived with Unreal 5.8, per Epic's 5.8 launch coverage (PC Gamer, Inven Global, DigitalProduction; see Sources). The video was uploaded the month after the 5.8 Preview, so INFERRED made on 5.8 Preview or 5.8.
- Captions English auto-generated present.
- Teaches Mesh Terrain basics, Sculpt, Remesh, Spline and Boolean mesh modifiers, a Nanite displacement master material with auto texturing and virtual texture blending, paint layers, foliage, and Convert to Terrain (the last chapter, 1:03:17). 10 chapters.
- Why it is the pick. It is the only landscape video in the list made for the version the team runs. Epic says Mesh Terrain is true 3D mesh (overhangs, tunnels, floating islands) and ties into World Partition, which is the big-world part.
- Risks. Epic labels Mesh Terrain experimental. The creator sells the Sensei Terrain material in the description, so the free path may differ. Check what works without buying it. Also the team has a rule that experimental Unreal features need Zac's yes, nothing here turns anything on.

**L2. Unreal Engine 5 Landscape Material - UE5 Tutorial**
- Channel Unreal Sensei
- URL https://www.youtube.com/watch?v=5ju7wyvZGBI
- Uploaded 2023-11-08. Length 59:49. Views 435,794.
- Version UE5, number not stated. The description says the downloadable material is "updated for 5.5 and 5.6", which tells us the video itself is older. INFERRED 5.3 era. OLD, over 2 years.
- Captions English auto-generated present.
- Teaches the classic Landscape tool basics, Megascans, Nanite, height patches, virtual texture blending, procedural foliage. 7 chapters.
- Why it is second. It is the proven heightmap Landscape route, the fallback if Mesh Terrain is too unstable.

**L3 optional. Make An Open World Map in 20 Minutes | Unreal Engine 5 Tutorial**
- Channel Smart Poly
- URL https://www.youtube.com/watch?v=6_5_GiYgCis
- Uploaded 2024-08-23. Length 22:36. Views 593,379.
- Version UE5, number not stated. INFERRED 5.4 era.
- Captions English auto-generated present.
- Teaches landscape shape, mountains and hills, a free landscape material, ocean, trees. 7 chapters. Quick overview, shallow. It points to free marketplace assets, and whether those links still work is unverified.
- Same channel has an older UE5 World Partition video https://www.youtube.com/watch?v=efN4bGbzr78 from 2021-06-03, made on early UE5, skip it.

Channels with nothing good for this topic.
- William Faucher. Strong on look (Lofoten https://www.youtube.com/watch?v=ifryjffUJT8, 2022, Arctic https://www.youtube.com/watch?v=dVwFrmOvXG4, 2023), but both are photogrammetry and finishing, not terrain building. His 5.7 Megaplants crash course https://www.youtube.com/watch?v=3f7miRB9_Eo (2025-11-12, 12:19, UE 5.7, 131,142 views, English auto captions, 13 chapters) is worth a later look for vegetation on a big world, not for terrain.
- Virtus Learning Hub (shows as Tinkr Academy). Landscape videos are all UE4 (2016 to 2020). Example https://www.youtube.com/watch?v=OWOlYoI-3tY, 2017, UE4. Skip.
- Beardgames. One UE4 landscape video, 8:41, 4,088 views. Skip.
- Unreal Gaimedev. Nothing on this topic.

Top recommendation for this topic. L1, with L2 as the fallback. Note the Unreal Sensei 5.8 starter course (U1 below) also has a Landscape Sculpting chapter at 1:56:50 and Landscape Material at 2:08:16 on 5.8.

---

## 3. House, building, architecture

**H1 TOP. Stylized Low Poly Wooden Cabin (Blender Tutorial)**
- Channel Ryan King Art
- URL https://www.youtube.com/watch?v=11sC54-pq_0
- Uploaded 2025-01-30. Length 29:12. Views 16,404.
- Version not stated. INFERRED Blender 4.x from the date.
- Captions English auto-generated present.
- Teaches modeling the cabin, door, roof, lantern, then materials. 7 chapters. A whole small building with a door and roof in one sitting, game-ready low poly.
- Why it beats the rest of the channel. Newest of his building videos and a complete asset. His "Low Poly Building" https://www.youtube.com/watch?v=QHWAbVSkYic (2022-01-31, 22:34, 146,996 views, 14 chapters) is a clip of a larger 2022 course and focuses on foundation, door, window, so older. His 3.5-hour "Low Poly City Assets" is long.
- Weakness. Only 16k views, so it is less proven. Low views do not mean it is bad.

**H2. How to make an abandoned house in Blender - Tutorial**
- Channel Blender Guru
- URL https://www.youtube.com/watch?v=1aNnERnHRZg
- Uploaded 2021-10-27. Length 25:38. Views 3,680,453.
- Version not stated. INFERRED Blender 2.9x or 3.0. OLD, over 2 years.
- Captions English auto-generated present.
- Teaches house modeling (only 0:25 to 4:08), then reference, textures, polygon material converter, hand painted texture, color burn, painting. 9 chapters. Mostly texturing and weathering, not construction.
- Flag. It uses Poliigon textures and a Poliigon add-on, some of which are paid. Free-only rule applies, the skill should teach the method, not the assets.
- Why it beats the rest of the channel. The other Blender Guru building videos are interiors. "How to Make an Interior in Blender (in 9 mins)" https://www.youtube.com/watch?v=DJRBv917CI0 (2022-09-15, 8:46, 1,150,547 views, auto captions) is short and clean. "How to Make Interiors in Blender" https://www.youtube.com/watch?v=wrzSrjAY69c (2020, 29:12) has NO English caption track, so I would not use it.

Also looked at. Grant Abbitt "Lowpoly Stylized Cottage" https://www.youtube.com/watch?v=izjz2Hya2QM, Blender 2.8, 2020, 9:17 for part 1, part 2 https://www.youtube.com/watch?v=q8t3lOC5mTE. OLD. CG Boost "How to texture REALISTIC buildings in Blender" https://www.youtube.com/watch?v=ilaD-V8R1gI (2024-05-23, 22:28, 459,099 views, manual and auto English captions, 9 chapters) is texturing only, good as a companion. Its urban environments course is a paid course, excluded. Ducky3D has two architecture videos, "Modern Home Design in Blender 2.8" https://www.youtube.com/watch?v=N8C_bzsOt5w (2019) and "Architecture Modeling For the First Time (Blender 2.9)" https://www.youtube.com/watch?v=xsL0fxlR0oU (2020). Both OLD, skip.

Top recommendation for this topic. H1 for building the house, H2 only for weathering.

---

## 4. Boat, hull, vehicle

**None of the five Blender channels has a real boat or hull modeling tutorial.** I searched each channel by name with boat, ship, hull, rowboat, canoe, and viking. The nearest boat result is a 2022 animation breakdown. I am not padding. The picks below are the closest transferable material.

**B1 TOP for hull method. How to make a private jet in Blender**
- Channel Blender Guru
- URL https://www.youtube.com/watch?v=4wxmKLDhsnQ
- Uploaded 2026-10-17. Length 3:23:39. Views 254,187.
- Version not stated in the video description or on the channel's own tutorial post. INFERRED Blender 5.x from the date, three weeks old. UNVERIFIED.
- Captions English auto-generated present. 33 chapters.
- Teaches blueprint setup, blocking the fuselage by silhouette (6:33 to 13:41), base mesh plus a details mesh with subdivision, bevel weights, panels, UVs, painting, materials, lighting, rivets, a short animation, render.
- Why it transfers. A fuselage is a long curved hull built from blueprints, the same method a boat hull needs. The channel's own post notes the base mesh and details mesh trick and the edge bevel weight fix.
- Weaknesses. It is 3 hours 24 minutes. It uses Photoshop for painting (113:47) and links a paid third-party car course in the description. Jet panels and rivets do not apply to a rowboat.

**B2. Make a Low Poly Hot Rod in Blender, 4-part series**
- Channel Grant Abbitt (Gabbitt)
- Part 1 https://www.youtube.com/watch?v=XaaP2qXuQJg (2026-08-28, 13:33, 23,463 views). Part 2 https://www.youtube.com/watch?v=FaAcvzyRG3w (2026-08-30, 15:50, 14,999 views). Part 3 https://www.youtube.com/watch?v=j0WzeKJG3_I (2026-09-01, 12:57, 10,685 views). Part 4 https://www.youtube.com/watch?v=tIAZ1o3GFH4 (2026-09-03, 15:20, 11,646 views).
- Version not stated in the title. The description mentions Blender 3D and links "basics of Blender 5". INFERRED Blender 5 era from 2026 dates. UNVERIFIED.
- Captions English auto-generated present on all four. No chapters.
- Teaches importing reference images, blocking a body with loop cuts and extrusions, engine, wheels and details, materials and render.
- Why it is here. Short steps, a good graded practice between the house and the rowboat, since blocking a rowboat hull from side and top reference uses the same moves. Not a boat.

**B3 optional. Low Poly Boat Animation - Breakdown - Blender 3**
- Channel Grant Abbitt (Gabbitt)
- URL https://www.youtube.com/watch?v=8MX9e7bRFyU
- Uploaded 2022-03-02. Length 13:55. Views 42,092. Blender 3 (title). OLD.
- Captions English auto-generated present.
- It is a talk-through of one finished animation. Modeling is a timelapse with commentary (1:13 to 4:15). Then a low poly person, rig, textures, lighting, shape key waves (8:43) and particles. Useful for water motion, not for building a hull.

Also looked at and passed. Ryan King Art "Low Poly Stylized Car" https://www.youtube.com/watch?v=yiwp37tevhU (2022-01-28, 33:58, 23,751 views, version not stated, a clip of his city course). CG Boost "Hard-Surface Modeling in Blender for Beginners (Full Course)" https://www.youtube.com/watch?v=zxhaCD-Zlfw (2026-05-13, 2:18:23, 66,007 views, English auto captions, 17 chapters) builds a robot, so no vehicle. Grant Abbitt "Space Ship" exercise, Blender 2.8, 2020, OLD.

Top recommendation for this topic. B1 for the hull method, B2 for the simpler practice step. Real boat coverage needs a decision, see the Open questions.

---

## 5. Unreal import and lighting (one standout exists)

**U1 TOP. Unreal Engine 5 Beginner Tutorial 2026 - UE5 Starter Course**
- Channel Unreal Sensei
- URL https://www.youtube.com/watch?v=e83pKSlfGR0
- Uploaded 2026-10-19. Length 5:50:18. Views 75,259.
- Version Unreal 5.8 (the description says "Unreal Engine 5.8").
- Captions English auto-generated present. 31 chapters.
- Useful chapters for the team. Lighting with Lumen 35:58, Archviz lighting example 50:36, Import/Create a Static Mesh 96:52, Move Assets Between Projects 107:26, Landscape Sculpting 116:50, Landscape Material 128:16, Foliage Paint 158:18, Nanite 169:32, Connect AI to Unreal with MCP 223:42, Castle environment build 276:43.
- Why it stands out. It is the only item on the list that is both made for 5.8 and covers import plus lighting plus landscape in one place. It is a beginner course, so import covers a plain static mesh, not the Blender to Unreal pipeline the department picked (xavier150 add-on). The MCP chapter talks to Epic's experimental MCP plugin. The department's rule is that the Epic MCP stays off until Zac says yes, so the MCP chapter is for reading, not for acting on.
- Take chapters only. Nobody needs the full 5 hours 50 minutes as a transcript.

**U2 optional. Lighting in Unreal Engine 5 for Beginners**
- Channel William Faucher
- URL https://www.youtube.com/watch?v=fSbBsXbjxPo
- Uploaded 2022-06-10. Length 44:43. Views 1,370,394.
- Version Unreal Engine 5 (early, UE5.0 era, INFERRED). OLD, over 2 years.
- Captions English auto-generated present. 13 chapters (light types, VSM versus raytraced shadows, indirect lighting, emissive, daylight, god rays, overcast).
- Use for lighting principles only. Menus and defaults in 5.8 will differ. His newer 5.7 Megaplants video is under topic 2.

Checked and not chosen. Unreal Sensei "Learn Unreal Engine 5 for Blender Users" https://www.youtube.com/watch?v=IQCNJ9Lpx-s (2021-09-15, 4:40:45, 438,495 views, English manual and auto captions, 27 chapters, Blender 3 and early UE5). It has Blender material and Blender object import chapters, but it is early UE5 and four years old, OLD. Tinkr Academy (Virtus) "Realistic Lighting in 15 Minutes - Unreal Engine 5 Lumen Tutorial" https://www.youtube.com/watch?v=sfMG746hk3k (2022-05-19, 16:08, 101,498 views, auto captions), short and OLD. Smart Poly "Unreal Engine 5.8 Beginner Tutorial" https://www.youtube.com/watch?v=57yLCKqC9m8 (2026-06-27, 1:37:09, 148,963 views, 5.8, manual and auto captions, 37 chapters) is UI, assets and a Lumen and Nanite intro only, no import or lighting depth. William Faucher "Path Tracer Explained" https://www.youtube.com/watch?v=X5zVhc5ahl0 is UE 4.27, 2021, OLD.

---

## Channel scorecard

- Blender Guru. Best for house realism (abandoned house) and the new jet. Sculpting is old or from the 4.0 donut series. Donut for Blender 5.0 exists as one 4:19:10 video (https://www.youtube.com/watch?v=z-Xl9tGqH14, 2026) for basics, not asked for here.
- Grant Abbitt. Best for brush reference, Blender 5 face sculpt, vehicle practice. Boat only as an animation breakdown.
- CG Boost. Best captions (manual on several). Retopo is older. Courses beyond the free videos are paid and excluded.
- Ducky3D. Nothing recent on any topic here. The architecture videos are Blender 2.8 and 2.9.
- Ryan King Art. Strongest overall fit, three top picks (S1, R1, H1). Version numbers are mostly not stated.
- William Faucher. Look, lighting and vegetation, not terrain building. Only the lighting video is a pick.
- Virtus Learning Hub (Tinkr Academy). UE4 era on every topic that matters. Nothing picked.
- Beardgames. Nothing picked.
- Smart Poly. One optional landscape pick (L3).
- Unreal Sensei. Best Unreal fit, three picks (L1, L2, U1). Sells his own materials, check for free paths.
- Unreal Gaimedev. Nothing found on any of the topics.

---

## Sources

All watch pages read with yt-dlp on 2026-11-05, metadata only, each link below confirmed to resolve to a matching title and channel.
- Lxem4yMs5Dg, 5-mNgCpEkCI, Lgg39sZF0kI, 1myOZaxtHes, X2GNyEUvpD4, Lhj2LutYNjA, 5ju7wyvZGBI, 6_5_GiYgCis, 11sC54-pq_0, 1aNnERnHRZg, 4wxmKLDhsnQ, XaaP2qXuQJg, FaAcvzyRG3w, j0WzeKJG3_I, tIAZ1o3GFH4, 8MX9e7bRFyU, e83pKSlfGR0, fSbBsXbjxPo, and the others named inline, all at https://www.youtube.com/watch?v=<id>.
- Blender Guru jet post, no version stated, fetched 2026-11-05. https://www.blenderguru.com/posts/2026/10/14/how-to-make-a-private-jet
- Blender Guru Donut for Blender 5.0, version stated in text. https://www.blenderguru.com/posts/blender-donut-v5-tutorial
- Mesh Terrain is an experimental Unreal 5.8 feature. https://pcgamer.com/software/unreal-engine-5-8-launches-with-improved-terrain-and-vegetation-tools-a-lumen-lite-option-for-faster-global-illumination-and-for-the-times-we-now-live-in-an-open-standard-plugin-for-llm-systems/ and https://www.invenglobal.com/articles/23006/unreal-engine-58-released-enhanced-large-scale-open-world-and-ai-workflows and https://digitalproduction.com/2026/05/14/unreal-engine-5-8-preview-rolls-in/ (from a search summary, I did not open Epic's own release notes, so the Mesh Terrain and World Partition detail is UNVERIFIED against Epic's primary page).

## Open questions for Zac

1. Approve the picks above, mark yes or no. Then the department pulls transcripts for the yes items only.
2. Boat gap. None of the five channels has a boat or hull tutorial. Options are A. use the jet plus the hot rod series and learn the hull method from them, B. let the department search outside the five channels for one boat video and bring it back for your OK, C. use your Blenderfast track for the boat. Recommendation B, one video, comes back for approval before any transcript is pulled.
3. Mesh Terrain is experimental in 5.8. OK to teach it as the main landscape route, with the classic Landscape video as the fallback, or classic only? Recommendation, teach both, classic first for anything that must ship.
4. Several pre-2024 videos are included only where no newer one exists. Flagged OLD above. Skills built from them need a version check against 5.2.4 and 5.8.4 before anything is trusted.
