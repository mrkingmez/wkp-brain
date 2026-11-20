# Zac Style Sheet and Improvement List

Built 2026-11-19 overnight into 2026-11-20 by the Studio editing department (studio-director running the job, head-editor notes applied, assistant-editor and media-manager support). Draft for Zac. Zac is the editor; nothing here changes his cut or his files.

## Page 1: the short version

**What this is.** We measured 8 of your finished WWD reviews (Carrie through Vision Quest EP 8) and 4 older pieces from P: and E:, frame by frame and with loudness meters. We read 17 editing lessons from well-known pros (Walter Murch's rules, Every Frame a Painting, StudioBinder, Paddy Galloway, Vox's trailer editor, Premiere Gal and others). Then we compared the two. Nobody listened to the audio; every sound number is a meter reading.

**What you already do well.**
1. You trim the talk. Street Fighter kept 32 percent of the raw recording (measured); the four other reviews we could compare kept 56 to 62 percent.
2. Pauses are rare. Seven of eight reviews have 0 to 3 near-silent gaps over 1.5 s at -45 dB; a stricter -35 dB pass finds one pause of 1 s or more every 1.2 to 5 minutes (Part 1).
3. Every review we checked opens on a hook line before the hosts say hello (11 to 23 s), the way pros open with a "bumper" (7 of 8 transcripts read; Carrie's frames show the same).
4. Cutaways hold about 5 s (median 5.0 to 6.5 s on 7 of 8 reviews), inside your own 7 s rule and at the top of the 2 to 5 s range pros teach.
5. You build a real show kit, and on Street Fighter you carried one theme device (the health bar) through the whole review (seen on frames, not measured).

**The three gaps that matter most.**
1. **Long stretches where the screen never changes.** Every review has 3 to 11 stretches of more than a minute on the two-shot; the longest are 13 minutes (Crystal Lake), almost 10 minutes (Clayface) and 5.5 minutes (Vision Quest EP 7). Pictures, clips and cams fill only 8 to 16 percent of the runtime.
2. **Exports miss your own loudness standard.** WWD's standard (WWD\STANDARDS.md) is -14 LUFS integrated and -1 dB true peak. All 8 reviews miss it: they measure -20.5 to -24.7 LUFS, and 4 of 8 peak above 0 dBTP.
3. **The first 30 seconds.** After a strong hook, all 7 transcripts we read open the two-shot with a "welcome back" restart (Crystal Lake's runs 19 s, 0:23 to 0:42). Pros say the first 30 s is where viewers decide. Keeping it is your call (it is the show's ritual); shortening it is an option in Part 4.

**Your target look, in one sentence.** Same hosts, same kit, same trimmed talk, but no stretch over 60 seconds without something new on screen, and every export at your own -14 LUFS standard.

**A workflow to test (PROPOSED CHANGE, needs your yes).** Your locked rule is "a few solo cams, only when a host makes a good point and has the floor". So the 60-second rule below is carried by pictures and clips, not by more cams. If you want more cam switching, a 3-angle multicam (two-shot, King-Z cam, Winter Wolf cam, switched with the 1, 2, 3 keys) makes it fast. Head-editor's advice: do not switch workflow mid-edit on A Knight's Tale; try a 2-minute throwaway test first. Steps in Part 5, Recipe 2.

**Fix before posting (if not posted yet).** Godzilla Minus Zero shows the same picture twice (25:36 and 26:15) and ends on 10.5 s of black. TASKS.md lists Godzilla as not yet posted, so these are live fixes, not practice.

**What needs your call.** (a) Which Premiere you edit in, 2026 or 2027 (both are installed; color steps differ, and a 2027 project will not open in 2026). (b) PROPOSED CHANGE: more solo cam cuts than your "a few" rule, using multicam, yes or no. (c) Blurred fill behind portrait posters, yes or no. (d) Picture "settle-in" move, yes or no. (e) Keep, shorten or drop the "welcome back" line.

**Three words used below.** LUFS is how loud a video feels on average (closer to zero is louder; -14 is louder than -22). LU is a step on that scale (1 LU is about the smallest change you can hear). dBTP (true peak) is the single loudest instant; above 0 it can crackle after YouTube re-encodes.

---

## Part 1. What we measured (your work)

Full tables and methods: `D:\WKP\Post-Production\research\editing-study\2026-11-19-zac-work-measurements.md`.

| Review | Length | Off the two-shot | Median cutaway hold | Two-shot stretches over 60 s | Longest stretch with no change | Loudness | True peak |
|---|---|---|---|---|---|---|---|
| Vision Quest EP 8 | 27:47 | 13.2 % | 5.0 s | 7 | 4:13 (23:25 to 27:38) | -21.2 LUFS | +0.1 dBTP |
| Vision Quest EP 7 | 23:56 | 8.0 % | 6.5 s | 7 | 5:35 (5:48 to 11:23) | -22.8 | -1.7 |
| Godzilla Minus Zero | 28:54 | 12.6 % | 5.0 s | 7 | 4:04 (18:21 to 22:26) | -24.7 | -2.4 |
| Vision Quest EP 5 and 6 | 28:09 | 9.3 % | 5.0 s | 11 | 3:40 (9:50 to 13:30) | -23.0 | -2.2 |
| Clayface | 22:41 | 10.3 % | 5.0 s | 3 | 9:55 (11:28 to 21:23) | -23.3 | +0.9 |
| Crystal Lake | 35:44 | 9.0 % | 5.5 s | 6 | 13:13 (22:18 to 35:31) | -20.5 | -0.3 |
| Street Fighter | 20:47 | 15.7 % | 5.0 s | 7 | 2:44 (14:19 to 17:03) | -20.6 | +1.6 |
| Carrie | 39:30 | 12.2 % | 8.0 s | 10 | 4:07 (33:31 to 37:38) | -21.5 | +1.0 |

"Off the two-shot" means a picture, clip, solo cam, sticker, spoiler card, opener or end card is on screen. "Median cutaway hold" counts all of those, not pictures alone. A median of exactly 5.0 s on 5 of 8 reviews may simply be Premiere's default still length (head-editor's guess, not checked). Stretches are measured from the end of one cutaway to the start of the next. "Stretches over 60 s" counts the body only (30 s in to 30 s before the end); "Longest stretch" counts the whole video, so a stretch near the end runs into the end card (Carrie has 11 over 60 s if the whole video is counted).

Other measured facts:
- **Godzilla uses the same picture twice** (25:36 and 26:15) and ends on 10.5 s of black and 8.8 s of silence after the end card.
- **Black at the end of the others:** 1.1 to 2.5 s on four reviews, none on three. Under about 3 s is fine; only Godzilla needs a fix.
- **Intro level jumps.** Vision Quest EP 8's first 15 s measures about 7 LU louder than its talk; Vision Quest EP 7's is about 1 LU quieter.
- **Crystal Lake** has a StreamYard caption tag ("Well.... That was weird.") under King-Z's name in every two-shot frame we sampled from 0:53 to 34:50. The solo cam files were not checked for it.
- **Pictures are contain-fit** (never cropped, correct), which leaves wide black bars on portrait posters (Street Fighter character posters, Ultron in Vision Quest EP 8).
- **Pauses at -35 dB (second pass):** pauses of 1 s or more under -35 dB (a stricter meter that also catches quiet room tone): Street Fighter 4, Vision Quest EP 7 9, Clayface 12, Godzilla 18, Vision Quest EP 8 19, Crystal Lake 20, Vision Quest EP 5 and 6 21, Carrie 32. That is about one pause every 1.2 minutes (Carrie) to one every 5 minutes (Street Fighter). Still lean; Carrie has the most to trim.
- **Older work (P: and E:).** The 2022 Ladies Night promo cuts about every 1.4 s with split screens and kinetic text, loud at -7.9 LUFS with +0.6 dBTP. The 2022 Father's Day video cuts about every 5.6 s, -12.1 LUFS, +3.0 dBTP. The 2025 FrostCast horror picks short measures -30.9 LUFS. You can cut fast when a job calls for it; finished loudness has varied by more than 20 LU across jobs.

## Part 2. The pro standard (what the sources teach)

Notes and source list with dates and software versions: `D:\WKP\Post-Production\research\editing-study\` (`2026-11-19-pro-editing-study-notes.md`, `sources.md`).

| Area | What pros teach | Source |
|---|---|---|
| Where to cut | Emotion first, then story, then rhythm (Murch's Rule of Six). Cut when a thought finishes. | StudioBinder on Murch (2024) |
| Holding a moment | Emotions take time. Hold a reaction a beat after the line before cutting away. | Every Frame a Painting (2016) |
| Talking heads with one camera | A trim inside the same framing is a jump cut. Hide it with a cutaway, a different angle, or a punch-in. | StudioBinder jump cut (2021) |
| Smooth cuts | J-cut (sound arrives before picture) and L-cut (sound carries over the next picture). | tutvid (2017), Johansson (2025) |
| Cut on action | Cut during a movement or gesture so the motion hides the cut. | StudioBinder 6 ways (2022), Steckly (2025) |
| B-roll and pictures | 2 to 5 s per insert, land it on the word that names the thing, start clips mid-motion. | Katie Steckly (2025) |
| Retention | Front-load the first 30 s; keep pacing steady so there is no cliff; give the viewer time on the point that matters ("slow down"); hand the viewer the next storyline fast when one ends. | Nate Curtiss (2024), Paddy Galloway (2022) |
| Do not over-edit | Edit density follows the audience. Older audiences want fewer gimmicks. Save big transitions for big moments. | Curtiss, Galloway |
| Sound design | Ambience, Foley, then creative accents (whoosh, suck-back, hit). Not every moment gets an accent. | Film Editing Pro (2023) |
| Loudness | Measure integrated LUFS and true peak, use a limiter, hit a set target. | Creative Video Tips (2021, Resolve 17) |
| Multicam | Sync cameras by audio once, then switch angles with number keys while playing. | Premiere Gal (2025) |
| Trailers and stings | Open with a bumper; silence before a hit; show four pieces of the puzzle, never the whole box. | Vox with Bill Neil (2023) |
| Still photos | A short eased "settle-in" with blur and a tick sound gives a still an entrance. | Motion Array on Johnny Harris (2022) |

## Part 3. The gap

| Area | You now (measured) | Pro standard | Gap |
|---|---|---|---|
| Visual change | 8 to 16 % of runtime off the two-shot; 3 to 11 stretches over 60 s per review | steady change for a commentary video without over-editing; your median stretch (24 to 47 s on most reviews) is already fine | the long tail: stretches of 1 to 13 minutes |
| Cutaway holds | median about 5 s | 2 to 5 s | none, keep it |
| Cam cuts | solo cams used, sometimes for long single runs (61 s at 21:06 in VQ EP 8) | your locked rule: a few, only on a good point; pros cut on a gesture | keep it to a few; break long solo runs |
| First 30 s | hook 11 to 23 s, then a "welcome back" restart (19 s on Crystal Lake) | hook, then straight into the first opinion | your call |
| Loudness | -20.5 to -24.7 LUFS, 4 of 8 over 0 dBTP | your own WWD standard: -14 LUFS, -1 dB true peak | 6.5 to 10.7 LU short, and clipping risk |
| Intro level | 1 LU quieter to 7 LU louder than the talk | consistent; the sting should hit, not blast | inconsistent |
| Endings | under 3 s of black on most; 10.5 s on Godzilla | end card in the last 5 to 20 s (YouTube's end screen window; video at least 25 s, confirmed on Google's page) | Godzilla only |
| Repeats | one repeated picture (Godzilla) | none (your own rule) | small |

Note: Google does not publish a YouTube loudness number; -14 LUFS comes from third-party testers (fact-research, 2026-11-20). Your WWD standard already uses it.

## Part 4. The Zac Style Sheet (the target look)

House rules for a WWD review cut "like Zac, but better". Your locked rules stay as they are and win any conflict: no music under talk, a few solo cams only when a host makes a good point and has the floor, clips only under a host line about that exact scene (6 to 8 s, 12 s max, never back to back), pictures 7 s max and never twice, intro sting 6 s max, contain-fit never crop, cards in the first 3 minutes, secondary pictures only from the title reviewed, kit pieces only where a host says the line, have fun and match the movie's tone.

**Keep (this is your style):**
1. Trim the talk to the best of it; keep the conversation moving.
2. Cut out long silences.
3. Hook before hello: Winter Wolf's question-style hook over the opener or poster.
4. Cutaway holds of 4 to 6 s, contain-fit, no repeats.
5. A theme device carried through a review when the movie suits one (Street Fighter health bar).

**Add (the "better"):**
6. **The 60-second rule (hard).** No two-shot stretch over 60 s. **Target:** something changes about every 40 s, carried by pictures (and clips where a host talks about that exact scene), not by extra cams. Test 20 to 25 percent of runtime off the two-shot on the next two reviews and check YouTube Studio retention before making it standard.
7. **Cams stay few and earned.** Cut to a solo cam only when a host makes a good point and has the floor (your locked rule), on a gesture or head turn. Break any solo cam run over 30 s with a picture or the two-shot (VQ EP 8 has a 61 s solo run at 21:06).
8. **Hide trims on solo cams with a punch-in.** On a solo cam only, scale the piece after a trim to about 115 percent so the jump reads as a push. Never scale the two-shot (it would crop the StreamYard layout and name tags).
9. **Land pictures on the word.** The picture appears on the word that names it and leaves when the thought ends, 7 s at the latest.
10. **Topic blocks are scenes.** Each topic (a character, a scene, the score) is a 2 to 4 minute block that opens with a picture of the topic (or a clip if a host is talking about that exact scene), so the viewer knows a new storyline started. A sticker only if a host says the line.
11. **Hit your loudness standard on every export:** -14 LUFS integrated, -1 dB true peak, checked by measurement after export. Intro sting no more than about 3 LU louder than the talk. Mix level calls go through wwd-sound.
12. **Clean endings.** End card in the last 5 to 20 s; trim black tails over about 3 s.
13. **Check StreamYard banners** before recording so no caption tag rides through the whole show.

**Creative calls for Zac (offered, not applied; head-editor's pick in brackets):**
- A: Picture "settle-in" move: an 8-frame ease-in with a slight blur and a tick sound (Johnny Harris style). Conflicts with the "no push-ins" line in the A Knight's Tale run sheet. [Pick: no.]
- B: Blurred fill behind portrait posters (a blurred, darkened copy of the same poster behind it, still contain-fit). [Pick: yes, portrait posters only, built once and saved.]
- C: The "welcome back" line: keep, shorten to about 3 s, or drop. [No pick; it is the show's ritual.]
- D: PROPOSED CHANGE to your "a few solo cams" rule: more cam switching with a multicam. [Pick: only if you want it; test on a 2-minute throwaway first, never mid-edit on A Knight's Tale.]

## Part 5. Premiere recipes (every click)

**Version note.** You have Premiere Pro 2026 and Premiere Pro 2027 installed. Premiere 2027 (version 27) retired the Lumetri Color panel and added a Color mode tab (confirmed by fact-research from Adobe community staff replies; Adobe Help pages blocked the checker). **A project saved in 2027 will not open in 2026. Finish every project in the version it started in; do not open A Knight's Tale or Vision Quest EP 8 projects in 2027.** Steps marked NOT VERIFIED were not confirmed for your version; if a menu looks different, look for the same word nearby and tell the studio so the sheet gets fixed.

### Recipe 1. Export at your loudness standard
Steps 1, 2 and 8 (In and Out points, Sequence In/Out range) are standard basics, not checked on 2026 or 2027.
1. Make a 1-minute test first: in the timeline press **I** at a minute that has both talk and the intro sting, and **O** one minute later.
2. Go to **Export** (the Export tab at the top left, or File > Export > Media). Set the range to **Sequence In/Out**.
3. Open the **Effects** section of the export settings.
4. Tick **Loudness Normalization**.
5. Set the loudness standard to an ITU BS.1770 option (Media Encoder lists BS.1770-3; the list in Premiere's export screen is NOT VERIFIED).
6. Set **Target Loudness** to **-14** LUFS and **True Peak Limit** to **-1** dBTP (or the nearest offered).
7. Export the test. Send it to the studio to measure with ffmpeg; do not trust the dialog alone. Fact-research found a reported bug where exports failed with Loudness Normalization on in a beta, so the test also proves it works on your machine.
8. If the test measures right, set the range back to the full sequence and export.
Warning: going from about -22 to -14 LUFS adds about 8 dB of gain. Whether Adobe's normalization reaches -14 without pushing the mix hard into the limiter is NOT VERIFIED. If the test sounds squashed or measures short of -14, wwd-sound sets a mix-level plan instead.

### Recipe 2. Only if you say yes to creative call D: build a 3-camera multicam from StreamYard files
StreamYard gives you three files per recording: the main two-shot recording, the King-Z webcam file and the Winter Wolf webcam file. Try this first on a 2-minute throwaway sequence.
1. In the **Project** panel, select all three files (click the first, hold **Ctrl**, click the other two).
2. **Right-click** one of them and pick **Create Multi-Camera Source Sequence**.
3. In the box: **Name** it. **Synchronize Point**: **Audio**. For the audio, keep only the main two-shot recording's sound (it has both hosts mixed). The exact audio option wording is NOT VERIFIED. **Camera Names**: **Use Clip Names** (not checked on 2026 or 2027). Click **OK**.
4. A multicam source item appears in the Project panel. **Right-click** it and make a new sequence from it (Premiere Gal calls it **New Sequence From Clip**; NOT VERIFIED on your version), or drag it onto the **New Item** button at the bottom of the Project panel.
5. In the **Program** monitor, click the **+** (Button Editor) at the bottom right. Drag two buttons onto the button bar: **Toggle Multi-Camera View** and **Multi-Camera Record On/Off**. Click **OK**. Click **Toggle Multi-Camera View** (all three angles show on the left) and turn **Multi-Camera Record** on. Without Record on, the number keys do not leave cuts.
6. Press **Space** to play. Tap **1** for the two-shot, **2** and **3** for the solo cams as the talk goes. Press Space to stop. The switches are now cuts on your timeline.
7. To move a switch, press **N** (Rolling Edit tool), drag the cut line left or right, then press **V** to go back to the Selection tool.
8. Do your talk trims on this sequence the way you trim now.
Color on multicam angles: NOT VERIFIED for 2026 or 2027; leave color to wwd-color for now.

### Recipe 3. Punch-in to hide a trim on a solo cam (solo cams only; values are standard basics, not checked on 2026 or 2027)
1. Click the solo cam clip right after your trim.
2. Open **Effect Controls** (Window > Effect Controls).
3. Open **Motion**, set **Scale** to **115**. Check the head is not cut off at the top; if it is, nudge **Position** (the second number moves it up and down).
4. On the next trim, set it back to **100**. Alternating 100 and 115 makes each trim look like a camera move.
5. Never do this on the two-shot.

### Recipe 4. Replace a repeated picture (Godzilla 26:15)
1. Pick a new picture from Godzilla's own `USE` folder that has not been used in the video.
2. In the **Project** panel, find it.
3. Hold **Alt** and drag it from the Project panel onto the old clip in the timeline. It swaps in at the same spot and length (long-standing Premiere move; NOT VERIFIED on 2027).
4. Check the fit: click the new clip, open **Effect Controls** > **Motion**. The replacement keeps the old clip's Scale and Position, so a picture with a different shape can end up cropped. Set **Scale** so the whole picture shows with bars if needed. Nothing may be cropped.
5. Check the hold is 7 s or less.
6. If Alt-drag does not work: click the old clip, press **Delete**, drag the new picture into the same spot, trim it to the same length, then do steps 4 and 5.

### Recipe 5. Remove a long black tail (Godzilla)
1. Move the playhead to the last frame of the end card (Godzilla: about 28:43).
2. Press **O** to set the Out point there.
3. In **Export**, set the range to **Sequence In/Out** and export. The black tail is left out without touching the timeline.
4. Only do this for tails longer than about 3 s.

### Recipe 6. Blurred fill behind a portrait poster (only if you say yes to creative call B; effect names and values not checked on 2026 or 2027)
1. Click the poster clip in the timeline. Hold **Alt** and drag it up one track to make a copy above it.
2. Click the **lower** copy. In **Effect Controls** > **Motion**, raise **Scale** until the copy fills the whole frame edge to edge (the number depends on the clip, so watch the Program monitor, not the number).
3. In the **Effects** panel, search **Gaussian Blur**, drag it onto the lower copy. In Effect Controls set **Blurriness** to about **80** and tick **Repeat Edge Pixels**.
4. Darken it: in the Effects panel search **Brightness & Contrast**, drag it onto the lower copy, set **Brightness** to about **-40**. Leave **Opacity** at **100** so the hosts do not show through.
5. The top copy stays at its contain-fit size. Nothing is cropped.

### Recipe 7. Check intro loudness while you edit
1. Open the loudness meter (look under the **Window** menu for "Loudness"; the name on 2026 and 2027 is NOT VERIFIED).
2. Play the intro, then the first minute of talk. Read the **Short-Term** value. The intro should read at most about 3 LU louder than the talk.
3. To lower the intro: click the intro audio clip, right-click, **Audio Gain**, **Adjust Gain by**, type **-4** (or what is needed), **OK** (long-standing option; NOT VERIFIED by fact-research).

### Recipe 8. Picture lands on the word
1. Play the line. Press **M** on the word that names the picture to drop a marker (shortcut NOT VERIFIED by fact-research, long-standing default).
2. Drag the picture so its left edge lines up with the marker. If it does not snap, turn on snapping (the magnet icon at the top left of the timeline, or **S**, NOT VERIFIED).
3. For a whoosh or hit sound, put it a few frames before the marker so it peaks as the picture lands.

### Recipe 9. Color
WWD color looks and LUTs belong to wwd-color, and the kit LUTs are untested. Safe technical pass only:
- **Premiere 2026 (Lumetri Color panel):** click the **Color** workspace at the top, click the cam clip, open **Basic Correction**, click the **White Balance** eyedropper on something white or grey (a wall, a shirt), adjust **Exposure** until faces look right, pull **Highlights** down if the light behind is blown out. Open **Window > Lumetri Scopes**, check the **Waveform**: nothing piled flat at the very top or bottom. (Tab names on 2026 are NOT VERIFIED; Color mode is also in 2026 as a beta.)
- **Premiere 2027 (Color mode):** the Lumetri panel is gone; Color mode has zone controls for shadows, midtones and highlights and sliders in the Properties panel. Exact names NOT VERIFIED. Head-editor writes the 2027 clicks once there is a screenshot of your real Color tab. Do not mix the old Lumetri effect and Color mode on the same clip (Adobe staff warning).

## Part 6. Improvement list (3 changes per video)

Times are from your final exports. "Before" is what the file shows now (measured, or viewed frames); "after" is the target. Godzilla's first two items are pre-post fixes if it is not posted; everything else is practice for the next review, not homework.

### 1. Vision Quest EP 8 (27:47)
1. **Static stretch 23:25 to 27:38 (4:13, the longest).** Before: two-shot only while you give the rating ("I don't hand out a lot of nines", about 24:06) and talk identity ("And a dad", about 26:14). After: the rating is a good point with the floor, so one solo cam there fits your rule; a picture of the moment you mean at 26:14; a picture or the score sticker if a host says the line. Recipe 8.
2. **Intro about 7 LU louder than the talk.** Before: first 15 s at about -15.5 LUFS short-term, talk at -22.7. After: intro within about 3 LU of the talk. Recipe 7.
3. **Export at -21.2 LUFS with a +0.1 dBTP peak.** After: -14 LUFS and -1 dBTP, your WWD standard. Recipe 1.

### 2. Vision Quest EP 7 (23:56)
1. **5:48 to 11:23 with no change (5:35).** Before: two-shot through Winter Wolf's run on "I am the vision, there is only one vision" (about 6:38) and "Holy crap, it was you, she names him" (about 10:26). After: a picture at 6:38; at 10:26 a clip of the reveal scene (a host is talking about that exact scene, 6 to 8 s) or a picture; pictures on the other named moments so no stretch passes 60 s. One solo cam on Winter Wolf's strongest point at most. Recipe 8.
2. **12 cutaways in 24 minutes (8 percent).** After: no stretch over 60 s, filled with pictures.
3. **The restart at 0:18 (your call C).** Before: "Welcome back everybody, we're going to talk Vision Quest episode seven" after the hook. After, if you choose to shorten it: hook, sting, then "this show is 100 percent heating up". Trim with the Razor (**C**) at both ends, select the piece, right-click **Ripple Delete** (standard, not checked on 2026 or 2027).

### 3. Godzilla Minus Zero (28:54)
1. **Repeated picture at 25:36 and 26:15 (pre-post fix).** After: swap the second for a new Godzilla picture. Recipe 4.
2. **10.5 s of black and 8.8 s of silence at the end, 28:43 to 28:53 (pre-post fix).** After: video ends on the end card. Recipe 5.
3. **Quietest of the 8 at -24.7 LUFS, plus the 18:21 to 22:26 stretch (4:04).** Before: two-shot through the "Super Saiyan moment" talk (about 18:59) and "if you were there for creature combat" (about 21:44). After: a picture of the power-up at 18:59, a picture (or a clip if the hosts are on that exact fight scene) at 21:44, export with Recipe 1.

### 4. Clayface (22:41)
1. **11:28 to 21:23 with no change (9:55).** Before: two-shot through the apartment-building talk (about 11:30), the comparisons (about 14:52), performances and the mob character (about 17:55) and "she was going to walk out the front door" (about 19:46). After: a change at least every 60 s, about 10 to 15 in that block, mostly pictures: the apartment, the mob character, the front-door scene, each performance named. Pictures only from Clayface itself, even when the talk names other movies. One solo cam on the best point at most.
2. **True peak +0.9 dBTP, -23.3 LUFS.** After: Recipe 1.
3. **Last 20 s at -32.2 LUFS short-term, about 8 LU under the talk.** After: keep the sign-off at talk level, then the end card. Check with Recipe 7.

### 5. Crystal Lake (35:44)
1. **22:18 to 35:31 with no change (13:13, the longest of all 8).** Before: two-shot through Pamela's backstory (about 24:25), Trip "the village idiot" (about 26:40) and the period-language talk (about 31:09 and 33:16). After: a picture of Pamela at 24:25 and of Trip at 26:40, and pictures of each scene named so nothing runs past 60 s. A solo cam only on a strong point. Recipe 8.
2. **StreamYard caption tag on screen from at least 0:53 to 34:50.** After: next recording, clear banners in StreamYard before hitting record. Whether the solo cam files carry the tag was not checked.
3. **Hook split across both hosts (0:00 to 0:23)** works. The "welcome back" right after it (0:23 to 0:42, 19 s) is a 19 s restart (your call C).

### 6. Street Fighter (20:47), the model to copy
1. **Keep:** the health-bar overlay and "2 HITS COMBO" card. The strongest theme device of the 8.
2. **True peak +1.6 dBTP, the highest of the 8.** After: Recipe 1.
3. **Portrait posters with black bars** (Akuma, Dan, Guile). After, only if you say yes to creative call B: blurred fill. Recipe 6.

### 7. Carrie (39:30)
1. **Cutaway holds about 8 s (26 over 7 s).** Made before the 7 s rule of 2026-10-19; the rule now covers it.
2. **9 silent gaps (20.5 s total), the most of the 8.** After: trim each by the waveform with the Razor (**C**) and Ripple Delete (standard, not checked on 2026 or 2027).
3. **24:00 to 28:02 and 33:31 to 37:38 with no change (about 4 minutes each).** After: the 60-second rule.

### 8. Vision Quest EP 5 and 6 (28:09)
1. **11 two-shot stretches over 60 s, the most of the 8.** After: the 60-second rule, filled with pictures of what is being discussed.
2. **9:50 to 13:30 (3:40) and 24:30 to 27:43 (3:13).** After: something new about every 40 s.
3. **Keep:** the terminal "next review" card and the spoiler card. Both are grammar your audience now knows.

## Part 7. AI video tools (PLAN ONLY, credits are zero)

Nothing here gets run. Veo, Firefly and ElevenLabs credits are at zero, and any spend is your call with the exact price.

| Tool | What it can do | Where it would help WWD | Status of facts |
|---|---|---|---|
| Premiere Generative Extend (Firefly) | Adds up to 2 s of video or up to 10 s of room tone to a clip | Hold a reaction a beat longer; fill a sound gap under a cut | Limits and credit use confirmed by fact-research; the per-second credit table is secondhand, confirm before use |
| Premiere 2027 Generative Media tool | Generates video and sound effects that land on the timeline as clips | A whoosh or hit you do not own | Credit use NOT VERIFIED (one creator said 30 credits for a sound effect; not checked) |
| Premiere 2027 AI Assistant (beta) | Assistant inside Premiere | Unknown for WWD | NOT VERIFIED |
| Firefly Quick Cut (beta, web) | Builds a first cut from a prompt: removes pauses, lays B-roll over talk | Practice: compare its cut with yours on a raw recording | From an Adobe Live video dated 2026-03-17; NOT VERIFIED by fact-research |
| Firefly video models (Veo 3.1, Kling 3.0, Runway Gen-4.5, Luma Ray, Firefly Video) | Text or start-frame to video | Intro stings, theme cards, transitions | Menu from your screenshot 2026-10-25 |

Prompts to try when credits return (one generation each; one generation can be cut into intro and outro):
1. **6 s intro sting, start frame = the WWD logo.** Model: Kling 3.0 (memory notes it for start-frame work; NOT VERIFIED as best). Settings: 16:9, 1080p, 6 s, audio off (music comes from the music department). Prompt: "The Winter Wolf's Den logo sits in a frozen cave, frost cracks across the emblem, a cold blue light flares behind it on the final beat, camera holds still, the last second is a clean hold on the logo."
2. **Theme overlay plate (like the Street Fighter health bar).** Model: Firefly Video. Settings: 16:9, 1080p, 5 s, audio off. Prompt: "A clean animated arcade-style frame border in neon blue and red on a plain black background, centered empty space, subtle flicker, no text." Use with blend mode Screen.
3. **Generative Extend on a reaction.** Tool name and location on your version NOT VERIFIED. Max 2 s.
Disclosure: YouTube asks for its altered or synthetic content label on realistic AI content; the exact rule for stylized logo stings is NOT VERIFIED, so check the label box whenever unsure.

## Part 8. What we could not do or check
- Nobody listened to any audio; all sound findings are meter readings.
- Two sources were blocked by YouTube rate limits (Zac Watson's Premiere color tutorial, Lila's Premiere 2027 Color mode video).
- Adobe Help pages returned 403 to the fact checker. Premiere 2027 Color mode labels, the loudness meter menu, "New Sequence From Clip", the multicam audio option, Alt-drag replace on 2027, and the M and S shortcuts are NOT VERIFIED.
- YouTube's -14 LUFS reference is third-party, not Google documentation.
- No retention data was pulled (VidIQ off). The 60-second rule and the 40 s target are to be tested, not a proven cause of retention.
- Transition counts were not measured (the cut detector misses dissolves). Speech pace was not measured.
- Carrie's transcript was not read; the solo cam files were not checked for the Crystal Lake banner.
- Topic lines in Part 6 come from your own final transcripts on L:, matched to the nearest timestamp (plus or minus a few seconds).
