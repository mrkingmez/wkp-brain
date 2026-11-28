# Percy Jackson and the Olympians Season 3, Episodes 1 and 2 (The Titan's Curse) - Edit Run Sheet v1

**Built 2026-11-23 by wwd-run-sheet for wwd-director, from the Premiere transcript of Zac's EDITED cut, 31:58 long, speakers 1 and 2 only.** Transcript: `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\Percy Jackson season 3 ep 1 and 2.txt`. Movie folder (MOVED, spelled Percey): `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\`. USE folder: `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\USE\`. Every time on this sheet is a time in YOUR CUT as the transcript shows it (MM:SS). The .mp4 in the folder (`Percy Jackson season 3 ep 1 and 2.mp4`, 48:25, 2905.39 s) is the RAW recording, NOT the cut, and no time here comes from it.

## Timing check (read this first)

- **Transcript is the newest text file in the folder** (`ls -la`: the .txt is dated Nov 23 20:06, the raw .mp4 Nov 23 19:56, no other transcript or export in the folder). The last stamp in the transcript is **00:31:58:05 = 31:58 (1918.2 s)**, matching the 31:58 the director gave. No edited export or sequence length is on disk to compare against, so a drift against your latest sequence is NOT CHECKED. If you re-cut after this transcript was made, the search words still find every stop, trust them over the clock.
- **Frame rate assumption: 30 fps.** Frame numbers in the stamps reach :29 and never :30 or higher (script), and ffprobe reports 30/1 for the raw recording and all three webcam files.
- **How I checked:** a script parsed all 243 speaker blocks, counted every search phrase over the whole transcript (each of the 38 phrases appears exactly once, 0 problems), checked that each stop's time falls inside the block that holds its phrase, and checked that every "Said:" line is a copy from that block. Block stamps are exact. The second inside a block is word position, about plus or minus 2 s. Lines in quotes keep the transcript's garbles (Caption fixes lists them).
- **Speakers:** Speaker 1 = Winter Wolf, Speaker 2 = KingZ. Speakers 3 and 4 are one-word glitches and are attributed to nobody.

## Tags used on every instruction

PROVEN = checked by me or a script on disk or in the transcript this job. SOURCED = taken from a named report or file (named in the line). PROPOSED = my choice, not tested. I cannot hear audio or open Premiere, so no sound level, transition length or cut was heard or seen in a program.

## Fair use and rights note (short)

- **One muted clip, 7.00 s, 7.00 s in all (stop 10).** From Disney Plus's own "Watch a Sneak Peek" upload (YouTube ID ofo6JgXlNfA), 2.9 percent of its 243 s. Inside one shot, only under a host line about that scene, no title card, release date or studio logo in the frames I pulled. **Disney+ corner marks are on every frame** (show mark top left, "Disney+ hulu" top right), not removable. wwd-rights flag. The clip has no audio stream.
- **Pictures are Disney press-kit images and one poster, used for commentary**, each placed on the line that is about it. 27 stills and the poster: 9 of them are SEASON 1 press stills of the same actors in the same roles (Clarisse, Chiron, Hermes, Zeus, Hades, Poseidon, Ares, Mr. D, Luke in armor), tagged S1 in `USE\pictures-tags.md`. The press page gives no license text beyond its footer. A rights note for this review: not available, I did not find one in `D:\WKP\WWD\reports\` (Still open 23).
- **Film material line for the description, above the disclaimer** (PROPOSED): `Film stills and a short clip from Percy Jackson and the Olympians (Disney+) are used for commentary and criticism. All rights belong to their owners.`
- No on-screen name tags on anyone. No card carries a score or a verdict. No bleeping, the language stays as recorded.

## Picture rules in force (LOCKED)

No picture longer than 7 s (the longest here is 6 s, most are 3 to 5), no picture twice (28 placements, 28 different files), contain/fit already done by wwd-pictures, no name tags. Pictures are cutaways: no picture sits on the same seconds as a cam or the clip (checked by script, 0 overlaps). USE holds 29 pictures, 28 are placed, ONE is a spare (`annabeth-percy-winter-dance.png`, the clip owns its line, Still open 16). Nothing from outside `USE\` is used. Lines with no verified picture are spoken only (Gaps and flags).

**Where this sheet differs from `USE\timeline-placements.md`:** (1) the placements list had the dance-floor still at 06:18 on the same line as the clip, I kept the clip and spared the picture; (2) holds are trimmed to end inside the line they illustrate: picture 6 ends at 04:00 and picture 18 at 20:51 so neither runs into a claim the facts file flags, picture 15 at 13:54; (3) picture 18 starts at 20:48 (was 20:49) for the same reason; (4) the Hades "no demigod" timecode in the facts file is 22:24, but KingZ's own sentence is the block before it (22:20 to 22:24), see Still open 1.

## Before you start (one time, about 10 minutes)

1. **Shortcuts used below:**
   - Movie folder = `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\`
   - `USE\` = `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\USE\`
   - Clips = `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\clips\Premiere Ready\` (cut file `PJ3-C01 ... 7.00s MUTED.mp4`, source `PJ-S3 Sneak-Peek (2026-11-18) MUTED.mp4`). Never use the .mkv files in `clips\`.
   - Cards = `P:\WWD Kit\Cards\`
   - Sound FX = `P:\Sounds\Sound FX\Adobe\` (every cue below is from this Adobe library except the rimshot, which is `P:\Sounds\Music\adobe\Drum One Shots\`). No loose mp3 is used, so no unlicensed file is on this sheet. Adobe folders carry a LICENSE.pdf (I saw one in Imaging Elements and in Multimedia, did not check the other folders, did not open any).
2. **Import:** drag `USE` into the Project panel, then **Ctrl+I** and pick the clip cut file, the Next Up card and the end card. Import each sound as you reach it. [SOURCED: A Knight's Tale sheet, the same build you cut that one in. NOT VERIFIED in your current Premiere.]
3. **Tracks:** V1 host two-shot (your cut), V2 pictures, V3 your Spoiler Alert and Like and Subscribe clips, V4 the clip and the cards. A1 voices, A3 and A4 sound effects. No music except the intro sting (if you add one) and the outro. Sequence is 30 fps, the clip is 24 fps, let Premiere conform it (it is already 1920x1080). [PROPOSED]
4. **Find each spot:** **Window > Text > Transcript**, type the search words from the stop, click the highlighted word, the playhead jumps there. [SOURCED: A Knight's Tale sheet. NOT VERIFIED in your current build.]
5. **Set a transition length:** drag it from the Effects panel onto the cut, right-click it, **Set Transition Duration**, type the frames (12f = `00:00:00:12`). Designed ones are in **Effects > Video Transitions > Modern Transitions**, the click path is in each stop. If a folder name differs on your build, type the name (example `Mirror Impacts`) in the Effects search box. Classic ones are in **Effects > Video Transitions > Dissolve**. [SOURCED: premiere-transitions.md, Adobe Help Center list read 2026-10-14. NOT VERIFIED in your build.]
6. **Set a sound level:** click the clip, Effect Controls, **Volume > Level**, type the number. Each transition's paired sound goes on A3 starting on the first frame of the transition. Every level is PROPOSED, set by ear against the voices.
7. **Solo shots (CAM):** the cams are in the movie folder. Winter Wolf webcam `Percy_Jackson_season_3_ep_1_and_2-Winter_Wolf-webcam-00h_00m_00s_870ms-StreamYard.mp4` (2897.6 s, 1920x1080, 30 fps, starts 0.87 s after the recording start). KingZ has TWO files: `...King-Z-webcam-00h_00m_00s_457ms-StreamYard.mp4` (339.4 s) and `...King-Z-webcam-00h_13m_33s_082ms-StreamYard.mp4` (2085.1 s, starts 13:33.1 into the recording, so it covers about 13:33 to 48:18 of the raw). **Between about 05:40 and 13:33 of the raw recording KingZ has no cam file.** Both KingZ cam stops on this sheet (stops 26 and 30) use the SECOND file: your cut only removes material, so a time in your cut is never later than the same moment in the raw, and the earliest of them (21:42 in the cut) is therefore at 21:42 or later in the raw, past 13:33 (inference, PROVEN only if the cut keeps the original order). The cams are NOT confirmed synced: sync each to the raw recording (`Percy Jackson season 3 ep 1 and 2.mp4`) by waveform first, then to your cut. The CAM times below are CUT times, the ones on your sequence.
8. **Pictures:** each stop names the file and where it ends. Drop it on V2 at the search spot and drag its right edge to the end time. The PNGs have see-through edges so the hosts show around them.
9. **Clip:** one clip, stop 10. Put the cut file on V4 at the search spot, audio track off (it has no audio).
10. **Transition rules for this sheet:** 13 of 28 picture stops get a designed Modern transition, each with a paired owned sound (picture stops with a sound-bearing designed move). Plain Cross Dissolve on 2 stops only (stops 2 and 13), Film Dissolve on 2, the rest are hard cuts. Never the same transition twice in a row. Luma Fade is used twice (stops 12 and 36), every other designed one once. The hosts' talk is a kids' fantasy series, so nothing heavy sits under a gag sound: where the line is a guess about who dies the move is quiet (stops 22 and 23).
11. **Loudness:** export target -14 LUFS integrated, true peak -1 dBTP (Zac's lock; EBU R 128 itself states -23.0 LUFS and -1 dBTP, source S2 in the preflight; the YouTube loudness page is NOT RETRIEVED). No export exists yet, so nothing was measured. After you export, run: `ffmpeg -hide_banner -nostats -i "<export>.mp4" -af ebur128=peak=true -f null -` for loudness and true peak, and `ffmpeg -hide_banner -i "<export>.mp4" -vf blackdetect=d=0.5:pix_th=0.10 -an -f null -` for a black tail (limit 1 s). The ffmpeg path is in LOCAL-PATHS.md.
12. **The Spoiler Alert and the Like and Subscribe clips are yours.** Stops 14 and 38 only mark where they go.

---

### 1. 00:00  |  INTRO STING (optional, a sting before the first word)  |  search: "Olympians is back on Disney+"
Said: "Percy Jackson and the Olympians is back on Disney+ with season three, and it looks like the kids are all grown up..." (Winter Wolf, block 00:00:00 to 00:00:13)
Optional. The first speech block starts at 00:00:00:00, so nothing is in front of it in the sequence this transcript came from. A sting does not show in a transcript, so I cannot see whether your cut already has one. If you add one in front of the first word, every time on this sheet moves later by its length. Length cap 6 s (Zac 2026-11-19).
Sound (owned, Adobe library, nothing auditioned): layer `P:\Sounds\Music\adobe\Classical&Orchestral\Horns_E_80BPM\HornsE05.wav` (1.5 s) with `P:\Sounds\Music\adobe\Classical&Orchestral\Orchestra_60BPM\OrchHits01-C.wav` (2.0 s), about 3 s in all, full level on a silent open (no dB level set on purpose: it opens a silent timeline, set by ear). [PROPOSED, files PROVEN on disk, durations PROVEN by ffprobe]
Notes: The pick belongs to the music agent (Still open 15). The A Knight's Tale stomp-and-clap cut in `D:\WKP\scratch\akt-music\intro-6s.wav` is rock and joust themed and its recipe includes loose crowd mp3s with no license on file, so it is not proposed here. No logo sting is proposed for this show (the only logo files, `L:\Winter Wolfs Den review show\VFX\burning logo.mp4` and `Master Logo 2.mp4`, measured silent per wwd-sound and were not made for it). Skip this stop and nothing moves.
Tags: durations PROVEN. Everything else PROPOSED.

### 2. 00:00 - 00:07  |  PNG 1 (the show poster, season three key art with the title, a Nov 20 date and the Disney+ and Hulu marks)  |  search: "back on Disney+ with season three"
Said: "Percy Jackson and the Olympians is back on Disney+ with season three, and it looks like the kids are all grown up and facing even darker challenges than they had before." (Winter Wolf, block 00:00:00 to 00:13:28)
Picture `USE\poster.png` to 00:07 (7 s). In: hard cut. Out: Cross Dissolve 24f (`Effects panel > Video Transitions > Dissolve > Cross Dissolve`). Why: slow, gives the poster weight on the way out. Cross Dissolve 1 of 2.
Notes: The one poster, on the intro line only. The intro line runs to 00:14 (block 00:00:00:00 to 00:00:13:28), so the host cam carries the last 7 s (7 s rule). The poster is the studio's own season three art, it carries the date and streaming marks as made, no title card from a trailer. No sound on the poster.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 3. 00:43 - 00:47  |  PNG 2 (Percy in an orange camp tee, close portrait, bead necklace)  |  search: "Percy Jackson is now like six three"
Said: "Feels like it's been like five years in between, though, because Percy Jackson is now like six three. His voice is a little different." (Winter Wolf, block 00:35:12 to 00:46:24)
Picture `USE\percy-closeup-camp-tee.png` to 00:47 (4 s). In: hard cut. Out: hard cut.
Notes: Pictures Percy, it cannot show height. The "six three" is UNVERIFIED (Still open 9), a rough joke by Winter Wolf. If you trim it, drop this picture with it. Plain.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 4. 01:22 - 01:26  |  PNG 3 (Thalia in an orange hoodie with a chain belt beside a big tree, outdoors)  |  search: "before she became a tree"
Said: "It shows progression of both Percy and it shows Thora where she was before she became a tree." (KingZ, block 01:16:11 to 01:30:27)
Picture `USE\thalia-orange-hoodie-hill.png` to 01:26 (4 s). In: Film Dissolve 12f (`Effects panel > Video Transitions > Dissolve > Film Dissolve`). Out: hard cut.
Notes: The line is about Thalia before she became a tree, the picture is Thalia beside a tree. It does not claim this is her tree. Transcript garble "Thora" (Caption fixes). Soft, gentle beat.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 5. 01:27 - 01:31  |  PNG 4 (Annabeth, long hair, denim jacket, forest)  |  search: "hasn't grown or changed that much"
Said: "And I think the only one who really hasn't grown or changed that much is Annabel." (KingZ, block 01:16:11 to 01:30:27)
Picture `USE\annabeth-forest-portrait.png` to 01:31 (4 s). In: hard cut. Out: hard cut.
Notes: Names Annabeth (transcript garble "Annabel"). Plain, it follows picture 3 by a second.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 6. 03:35 - 03:39  |  PNG 5 (Clarisse in an orange Camp Half-Blood tee (a SEASON 1 press still))  |  search: "shows up briefly in episode two"
Said: "Like, it could literally, Aries daughter Clarice, who shows up briefly in episode two." (Winter Wolf, block 03:17:11 to 03:37:07)
Picture `USE\clarisse-camp-tee-s1.png` to 03:39 (4 s). In: hard cut. Out: hard cut.
Notes: Same character, but a season 1 press still (caption Episode 102), not a season 3 frame. Placed on the line that names her, a gap fill from the same show. Garbles "Aries" and "Clarice" (Caption fixes). Plain.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 7. 03:57 - 04:00  |  PNG 6 (Percy and Thalia face to face and tense at the forest camp (episode 302))  |  search: "forbidden forbidden children"
Said: "They have narrowed it down that it's either going to be Thalia or Percy, because both of them are the forbidden forbidden children." (KingZ, block 03:52:03 to 04:06:15)
Picture `USE\percy-thalia-faceoff-camp.png` to 04:00 (3 s). In: hard cut. Out: hard cut.
Notes: Names Thalia and Percy as the two forbidden children. Held only 3 s so it ends BEFORE the Hades clause that follows ("the child of Hades, which I don't think they have one", about 04:02 to 04:06, WRONG per the facts, Still open 1). Plain.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 8. 04:28 - 04:32  |  PNG 7 (Annabeth and Percy in winter coats inside a stone building (episode 301))  |  search: "burn down all of her work"
Said: "He told her I would burn down all of her work for you." (KingZ, block 04:26:03 to 04:30:25)
Picture `USE\annabeth-percy-winter-coats.png` to 04:32 (4 s). In: Burn Alpha Impacts 10f (`Effects panel > Video Transitions > Modern Transitions > Essentials > Burn Alpha Impacts`). Out: hard cut. Why: a flare on his own word "burn".
Sound: `P:\Sounds\Sound FX\Adobe\Fire and Explosions\Fire Flare Start Up Ignite 01.wav` on the first frame of the transition, first 1.5 s with a 0.5 s fade, -20 dB. [PROPOSED level, file PROVEN on disk]
Notes: Matches on who (Annabeth and Percy) and the topic of the line. The exact scene is not proven. Burn Alpha because the host says "burn" himself, light tone.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 9. 04:51 - 05:27  |  CAM: single out Winter Wolf  |  search: "tells me they'll figure it out"
Said: "this isn't Game of Thrones. You know. It's not The Expanse, it's not jaded, it's not cynical." ... "this still feels pretty light hearted to me through what we've seen in two episodes." (Winter Wolf, block 04:51:23 to 05:20:15)
Cut to Winter Wolf's solo camera. **CAM IN 04:51, CAM OUT 05:27, length 36 s.** Hard cut in, hard cut back to the two-shot. Cam file (Winter Wolf webcam): `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\Percy_Jackson_season_3_ep_1_and_2-Winter_Wolf-webcam-00h_00m_00s_870ms-StreamYard.mp4`. Sync first (Before you start, 7).
Notes: His point on why the show can grow up and get darker, one speaker, he has the floor the whole turn. The cam goes in at the block start (04:51), the search words are about 1 s in. 36 s is long for a cam: if you want it shorter, go back to the two-shot at 05:20 after "backstabbers and stuff like that" (29 s). No picture sits on these seconds. First solo cam.
Tags: cam file PROVEN on disk (30 fps, 1920x1080 by ffprobe). Cut times PROPOSED (block stamps are exact, the second inside a block is word position). Sync NOT CONFIRMED.

### 10. 06:16 - 06:23  |  USE VIDEO (clip C01, a dim parking garage, a girl in a denim jacket, a curly-haired boy walks up)  |  search: "Percy and Annabeth are on a mission"
Said: "Percy and Annabeth are on a mission to a military academy in Maine to scoop up a couple of kids they have identified as being half bloods." (Winter Wolf, block 06:11:05 to 06:30:11)
**USE VIDEO:** `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\clips\Premiere Ready\PJ-S3 Sneak-Peek (2026-11-18) MUTED.mp4` from `00:03:09:06` to `00:03:16:06` (168 frames, 7.00 s at 24 fps). Cut file with the same range, ready to drop: `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\clips\Premiere Ready\PJ3-C01 Sneak-Peek Annabeth-Percy-mission in 00h03m09s06f out 00h03m16s06f 7.00s MUTED.mp4`. Put it on V4 starting on "Percy and Annabeth" (about 06:16), muted. Hard cut in, hard cut back. [SOURCED: Clip-Placements report C01. File and 168 frames PROVEN by ffprobe, no audio stream PROVEN.]
Notes: One shot, the same wide garage frame throughout (I pulled frames 0, 2, 84, 165 and 167 of the cut file and looked at them, no title card, release date or studio logo, same shot start to end). The clip scout checked the shot edges in the source (shot runs source frames 4541 to 4711, clip uses 4542 to 4709, next shot starts 4712). It is a talking beat, the clip is silent. **Disney+ corner marks are on every frame, not removable:** the show mark top left, "Disney+ hulu" top right (wwd-rights flag, Still open 18). The footage is very dark and low contrast, wwd-color should check it against the host cams. The clip ends about 06:23 inside Winter Wolf's block (ends 06:30). It sits on the line about the military academy in Maine, which this garage scene is not (the scene is the two heroes laying out the rescue plan, per the official captions, auto captions not checked against audio), so the notes claim only "the mission". **One per beat:** the dance-floor still of Annabeth and Percy (`annabeth-percy-winter-dance.png`) also fits this line and is NOT placed, it is the spare (Still open 16). 7.00 s of the 243 s Sneak Peek (2.9 percent). Never back to back with another clip, it is the only one.
Tags: file and length PROVEN. Match SOURCED (Clip-Placements). Start time PROPOSED (word position, about 06:16), place by ear on "Percy and Annabeth".

### 11. 06:28 - 06:33  |  PNG 9 (Percy in a blazer and Nico, a small boy in uniform, on a crowded dance floor (episode 301))  |  search: "we meet a couple of kids"
Said: "We get there, we meet a couple of kids." (Winter Wolf, block 06:11:05 to 06:30:11)
Picture `USE\percy-nico-dance-floor.png` to 06:33 (5 s). In: hard cut. Out: hard cut.
Notes: The kids they meet at the academy, same dance set as the episode 301 stills. Not frame-proven to be the academy. Plain. The clip before it (stop 10) ends at 06:23.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 12. 07:12 - 07:17  |  PNG 10 (Luke standing alone in a dim stone space (episode not confirmed by caption))  |  search: "Brought where Luke is"
Said: "Or she gets captured. Brought where Luke is. That's how they reintroduce him back to the story." (Winter Wolf, block 06:56:00 to 07:16:25)
Picture `USE\luke-stone-hall-ep-unconfirmed.png` to 07:17 (5 s). In: Luma Fade Impacts 12f (`Effects panel > Video Transitions > Modern Transitions > Essentials > Luma Fade Impacts`). Out: hard cut. Why: slow, dark-leaning, a quiet reveal.
Sound: `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Slow Swell Dramatic 01.wav` on the first frame of the transition, first 2.5 s with a 1 s fade, -22 dB. [PROPOSED level, file PROVEN on disk]
Notes: Matches on the character only (Luke, from the press caption). The episode is NOT confirmed, so these notes do not describe the room. Luma Fade because the beat is Luke's introduction and the next lines say he is being punished.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 13. 07:54 - 07:58  |  PNG 11 (Chiron, an older man with a gray beard, glasses, tweed jacket and tie, seated (a SEASON 1 press still))  |  search: "seeing Kiran back"
Said: "I like seeing Kiran back and kind of running things same." (KingZ, block 07:50:27 to 08:12:19)
Picture `USE\chiron-tweed-jacket-s1.png` to 07:58 (4 s). In: Cross Dissolve 12f (`Effects panel > Video Transitions > Dissolve > Cross Dissolve`). Out: hard cut.
Notes: Season 1 press still (caption Episode 101) of the same character, placed because no season 3 frame of him exists in the press set. "Kiran" is the transcript spelling of Chiron (Caption fixes). Plain, calm talk. Cross Dissolve 2 of 2.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 14. 08:20  |  SPOILER ALERT (your own clip, marker only)  |  search: "drop a spoiler warning"
Said: "Come back to this point right here, because I'm about to drop a spoiler warning and three, two, one go." (KingZ, block 08:12:19 to 08:22:27)
Mark where your Spoiler Alert clip goes: on V3, starting on "three, two, one go" (about 08:20). Length is whatever your file is. I did not build or pick one (SOP rule, no new Spoiler Alert graphic). No transition.
Notes: The warning window the hosts give runs 08:12 to 08:30: KingZ's setup (08:12), Winter Wolf's "Nobody died." (08:22) and KingZ's "And well, you have been warned." (08:25 to 08:30). Plot talk already happened before this point (06:11 to 08:12, the setup of the two episodes), that is where the hosts put the warning. Kit files that exist for other shows, your choice and not picked for you: `P:\WWD Kit\Vision Quest\Spoiler Alert.mov`, `P:\WWD Kit\Crystal Lake\Spoiler Alert.mov` (both PROVEN on disk).
Tags: time PROPOSED. Placement SOURCED (memory wwd-skill-formats, 2026-10-20).

### 15. 08:22  |  SOUND ONLY (G1)  |  search: "Nobody died"
Said: "Nobody died." (Winter Wolf, block 08:22:29 to 08:25:25)
Sound: `P:\Sounds\Music\adobe\Drum One Shots\Drum_One-Shots_Brushes\Rimshot03.wav` on the word "died", whole file (0.66 s), -6 dB. A one-shot rimshot on Winter Wolf's own joke, not music. [PROPOSED level, file PROVEN on disk, 0.66 s from wwd-sound's A Knight's Tale plan, not re-measured]
Notes: His own gag on the countdown. If your Spoiler Alert clip still has sound playing at 08:22, skip this cue. No picture on this line. The only gag cue on the sheet: the other jokes are about electrocution ("toaster baths", 09:02 to 09:17) or a death guess, so they get no cue (see Gaps and flags).
Tags: time PROPOSED. File PROVEN.

### 16. 09:37 - 09:42  |  PNG 12 (Thalia peeking over a silver shield with a Medusa face, snow and a stone wall (episode 301))  |  search: "Zeus's only child on the planet"
Said: "Well, as, each one of them, it's been established she's the most powerful demigod alive because she's Zeus's only child on the planet." (Winter Wolf, block 09:23:18 to 09:45:00)
Picture `USE\thalia-aegis-shield-snow.png` to 09:42 (5 s). In: Flash Impacts 10f (`Effects panel > Video Transitions > Modern Transitions > Essentials > Flash Impacts`). Out: hard cut. Why: a flash for the power line.
Sound: `P:\Sounds\Sound FX\Adobe\Multimedia\Multimedia Internet CD-Rom Flash Beep Whoosh 02.wav` on the first frame of the transition, whole file (1.5 s), -20 dB. [PROPOSED level, file PROVEN on disk]
Notes: Line is about Thalia being the most powerful demigod, picture is Thalia. The hosts say the show said it, the facts file has it UNVERIFIED (Still open 11), leave. Flash on the power line, a short bright pop.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 17. 12:44 - 12:46  |  PNG 13 (three Huntresses with bows at a snowy ivy gate, Artemis in the middle (episode 301))  |  search: "Hunter faction of Lady Artemis"
Said: "Let's see what he does. And then we got introduced to the Hunter faction of Lady Artemis." (KingZ, block 12:39:22 to 12:46:11)
Picture `USE\artemis-huntresses-arrive-snow.png` to 12:46 (2 s). In: hard cut. Out: hard cut.
Notes: Introduces the Hunters of Artemis, picture is the Hunters. The middle figure is Artemis by matching a captioned portrait, the other two are not named here. Short, the next line is about Apollo.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 18. 12:57 - 13:00  |  PNG 14 (Apollo in a gray shirt with a sun logo, reclining in a car seat (episode 302))  |  search: "He's got a nice little entrance"
Said: "I didn't think so. That's right. He's got a nice little entrance. That was kind of dope." (Winter Wolf, block 12:56:10 to 13:00:00)
Picture `USE\apollo-sun-car.png` to 13:00 (3 s). In: Light Leak Impacts 12f (`Effects panel > Video Transitions > Modern Transitions > Lights & Blurs > Light Leak Impacts`). Out: hard cut. Why: warm light for the sun god.
Sound: `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Electronic Whoosh Calm 01.wav` on the first frame of the transition, first 1.5 s with a fade, -22 dB. [PROPOSED level, file PROVEN on disk]
Notes: The line is about Apollo's entrance, the sun car is his ride. The "god of fate" and "travel and poetry" list that follows (13:00 to 13:12) is UNVERIFIED as the show's own gag (Still open 8). Light Leak for the sun god.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 19. 13:48 - 13:54  |  PNG 15 (Artemis full length, hood up, bow and quiver, dark studio backdrop (a Disney season 3 character portrait, not a scene frame))  |  search: "Playing Artemis is Daphne Keene"
Said: "Yeah. Yes. Technically. So technically. So, worth pointing out. Playing Artemis is Daphne Keene, who looks lovely as ever. That's formally, X-23." (Winter Wolf, block 13:44:25 to 14:06:22)
Picture `USE\artemis-bow-portrait.png` to 13:54 (6 s). In: hard cut. Out: hard cut.
Notes: Line names the actor who plays Artemis, the picture is the Artemis portrait. It is a portrait, not a scene. Ends at 13:54 so it is gone before the "not much since Logan" and "Doomsday" jokes (14:06 to 14:14, UNVERIFIED, Still open 8). "Daphne Keene" and "formally" are garbles (Caption fixes). Plain.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 20. 14:32 - 14:37  |  PNG 16 (Artemis hooded with a bow beside Percy in a school blazer, snowy dusk (episode 301))  |  search: "invitation to join the eternal hunt"
Said: "The faction shows up after, Annabeth drops on Percy the whole invitation to join the eternal hunt, which is posted by Artemis that would remove her piece from the table and give her something to do elsewhere." (Winter Wolf, block 14:23:21 to 14:45:21)
Picture `USE\artemis-percy-snow.png` to 14:37 (5 s). In: Soft Wipe Impacts 12f (`Effects panel > Video Transitions > Modern Transitions > Lights & Blurs > Soft Wipe Impacts`). Out: hard cut. Why: a soft wipe for the snowy hunt scene.
Sound: `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Electronic Whoosh Digital Reverse Delay 01.wav` on the first frame of the transition, first 1.5 s with a 0.5 s fade, -22 dB. [PROPOSED level, file PROVEN on disk]
Notes: Matches on Artemis and the hunt invitation topic. It is NOT the moment Annabeth tells Percy.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 21. 16:59 - 17:03  |  PNG 17 (Huntresses with bows in a forest with two kids in camp tees, Nico and Bianca (episode 301))  |  search: "protectors as they were lined up"
Said: "They're not theirs protectors as they were lined up to be." (KingZ, block 16:49:16 to 17:15:29)
Picture `USE\huntresses-bring-nico-bianca.png` to 17:03 (4 s). In: hard cut. Out: hard cut.
Notes: The line is about the Hunters not being the protectors they were lined up to be. The Huntresses are unnamed in the caption, used only as a group. Plain.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 22. 20:48 - 20:51  |  PNG 18 (Grover in a camp tee facing the camera, blurred forest (episode 301))  |  search: "It could be Grover"
Said: "It could be Annabelle. It could be Grover. I mean, Pan should come back because he's technically a child of Pan." (KingZ, block 20:43:04 to 20:55:12)
Picture `USE\grover-camp-tee-forest.png` to 20:51 (3 s). In: Ray Impacts 12f (`Effects panel > Video Transitions > Modern Transitions > Lights & Blurs > Ray Impacts`). Out: hard cut. Why: the discovery look for the prophecy talk, no joke.
Sound: `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Electronic Whoosh Electrical 01.wav` on the first frame of the transition, first 1.5 s with a 0.5 s fade, -22 dB. [PROPOSED level, file PROVEN on disk]
Notes: Names Grover. Held 3 s because the "technically a child of Pan" sentence follows at about 20:51 and is UNVERIFIED, probably wrong (Still open 4, trim recommended). The picture ends before it. No comic cue: the talk is a guess about who the prophecy kills, so a quiet move only (Ray, the discovery look).
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 23. 21:00 - 21:05  |  PNG 19 (Hermes laughing in a beige hoodie, leaning at a casino table with chips (a SEASON 1 press still))  |  search: "Luke's going to be killed by Hermes"
Said: "I think it's Luke. Luke's going to be killed by Hermes. Hermes gonna have to make that hard. That hard choice." (KingZ, block 20:59:17 to 21:06:10)
Picture `USE\hermes-casino-hoodie-s1.png` to 21:05 (5 s). In: Zoom Blur Impacts 10f (`Effects panel > Video Transitions > Modern Transitions > Lights & Blurs > Zoom Blur Impacts`). Out: hard cut. Why: a fast move for the messenger god.
Sound: `P:\Sounds\Sound FX\Adobe\Weapons\Weapon Staff Whip Thin Fast 01.wav` on the first frame of the transition, whole file (0.41 s), -16 dB. [PROPOSED level, file PROVEN on disk]
Notes: Names Hermes, season 1 press still (caption Episode 106). It is a guess about the prophecy, so the sound is a quiet whip, not a gag.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 24. 21:16 - 21:19  |  PNG 20 (Zeus, bald, navy suit and tie, looking aside (a SEASON 1 press still))  |  search: "Zeus is kind of a piece of shit"
Said: "But I think that because we know Zeus is kind of a piece of shit in this show." (Winter Wolf, block 21:06:12 to 21:19:11)
Picture `USE\zeus-suit-s1.png` to 21:19 (3 s). In: hard cut. Out: hard cut.
Notes: Names Zeus, season 1 press still (caption Episode 108). Plain, the line is blunt and the picture is a straight portrait. Ends with the block.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 25. 21:30 - 21:33  |  PNG 21 (Hades in profile, green patterned jacket over a dark turtleneck (a SEASON 1 press still))  |  search: "Hades good one"
Said: "Of the three of them. Hades good one, Dresden Files handles that in spades." (Winter Wolf, block 21:29:16 to 21:33:28)
Picture `USE\hades-green-jacket-s1.png` to 21:33 (3 s). In: Blur Dissolve Impacts 14f (`Effects panel > Video Transitions > Modern Transitions > Essentials > Blur Dissolve Impacts`). Out: hard cut. Why: soft focus for the underworld.
Sound: `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Empty Electronic Whoosh 01.wav` on the first frame of the transition, first 2 s with a 1 s fade, -24 dB. [PROPOSED level, file PROVEN on disk]
Notes: Names Hades, season 1 press still (caption Episode 107). Blur Dissolve for the underworld god, dark-leaning meaning. The Hades talk at 22:20 and 04:02 is WRONG per the facts file (Still open 1).
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 26. 21:42 - 22:07  |  CAM: single out KingZ  |  search: "think of underworld in Greek mythology"
Said: "When you think of underworld in Greek mythology, it's different than what they." ... "they gave him the underworld." (KingZ, block 21:42:12 to 22:07:04)
Cut to KingZ's solo camera. **CAM IN 21:42, CAM OUT 22:07, length 25 s.** Hard cut in, hard cut back to the two-shot. Cam file (KingZ webcam, second file): `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\Percy_Jackson_season_3_ep_1_and_2-King-Z-webcam-00h_13m_33s_082ms-StreamYard.mp4`. Sync first (Before you start, 7).
Notes: KingZ's point that the underworld in Greek myth is not hell, and that Hades got the short end. He has the floor the whole block. The "he wanted the sky" part is his opinion about myth, UNVERIFIED in detail and low risk, leave (facts row 45). The Hades "no demigod" claim comes later at 22:20, outside this cam (Still open 1). Second solo cam.
Tags: cam file PROVEN on disk (30 fps, 1920x1080 by ffprobe). Cut times PROPOSED (block stamps are exact, the second inside a block is word position). Sync NOT CONFIRMED.

### 27. 24:18 - 24:21  |  PNG 22 (Poseidon, bearded, light linen shirt, pendant (a SEASON 1 press still))  |  search: "handsome, older looking like, fit dude"
Said: "It's a handsome, older looking like, fit dude." (Winter Wolf, block 24:18:01 to 24:21:25)
Picture `USE\poseidon-linen-shirt-s1.png` to 24:21 (3 s). In: hard cut. Out: hard cut.
Notes: The hosts describe Percy's dad as a handsome, older, fit man of the sea, this is that character (season 1 press still, caption Episode 108). 3 s, the line is 4 s long. Plain.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 28. 24:30 - 24:33  |  PNG 23 (Ares, bearded, gray helmet, leather jacket, beside motorcycle handlebars (a SEASON 1 press still))  |  search: "He shows up on a motorcycle"
Said: "He shows up on a motorcycle. His first. This is." (KingZ, block 24:30:27 to 24:33:09)
Picture `USE\ares-motorcycle-s1.png` to 24:33 (3 s). In: Directional Blur Impacts 10f (`Effects panel > Video Transitions > Modern Transitions > Lights & Blurs > Directional Blur Impacts`). Out: hard cut. Why: a fast blur for the motorcycle.
Sound: `P:\Sounds\Sound FX\Adobe\Transportation\Transportation Auto Motorcycle Drive By Fast 01.wav` on the first frame of the transition, whole file (5.1 s), fade out the last 1.5 s, -18 dB. [PROPOSED level, file PROVEN on disk]
Notes: Shows exactly the line: Ares by a motorcycle (season 1 press still, caption Episode 105). "Ed shows up as Aries" just before it is a garble, listen first (Caption fixes). Directional Blur is the speed look.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 29. 25:03 - 25:08  |  PNG 24 (Dionysus, Mr. D, curly hair and beard, patterned short-sleeve shirt, arms crossed, forest path (a SEASON 1 press still))  |  search: "Mr. D shows up"
Said: "So she hasn't shown up. But like everybody else has a vibe. Even when Mr. D shows up. Dionysus, when he shows up. Oh, fuck. More kids." (Winter Wolf, block 24:56:28 to 25:12:29)
Picture `USE\mr-d-dionysus-hawaiian-shirt-s1.png` to 25:08 (5 s). In: Spring Motion Impacts 10f (`Effects panel > Video Transitions > Modern Transitions > Animation > Spring Motion Impacts`). Out: hard cut. Why: a bouncy move on the host's own gag.
Sound: `P:\Sounds\Sound FX\Adobe\Cartoon\Cartoon Spring Twang 10.wav` on the first frame of the transition, whole file (1.9 s), -14 dB. [PROPOSED level, file PROVEN on disk]
Notes: Names Mr. D, season 1 press still (caption Episode 108). Winter Wolf does the character's grumpy line right after, a light joke on his own bit, so the cartoon spring cue fits. The "Raffi" and "Mr. Nice" garbles at 25:13 to 25:19 are listen-first (Caption fixes).
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 30. 26:41 - 26:56  |  CAM (CONDITIONAL, see notes)  |  search: "special operations unit"
Said: "Well, I mean, if you really want to break it down," ... "they mostly have girls as their offspring." (KingZ, block 26:41:12 to 26:56:01)
Cut to KingZ's solo camera. **CAM IN 26:41, CAM OUT 26:56, length 15 s.** Hard cut in, hard cut back to the two-shot. Cam file (KingZ webcam, second file): `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\Percy_Jackson_season_3_ep_1_and_2-King-Z-webcam-00h_13m_33s_082ms-StreamYard.mp4`. Sync first (Before you start, 7).
Notes: **CONDITIONAL, SKIP THIS STOP if you trim the daughters claim.** This block IS the claim that special forces fathers mostly have daughters. The facts file found no support and recommends a trim (Still open 2), so a solo cam would put a spotlight on a line that should go. The picture-fit report listed it as a cam because he has the floor, that is the only reason it is here. If you do trim 26:41 to 27:01, everything after it moves about 20 s earlier, the search words do not move.
Tags: cam file PROVEN on disk (30 fps, 1920x1080 by ffprobe). Cut times PROPOSED (block stamps are exact, the second inside a block is word position). Sync NOT CONFIRMED.

### 31. 27:06 - 27:10  |  PNG 25 (Grover in a camp tee, looking off left, rock wall behind (episode 302))  |  search: "Like Grover's there"
Said: "Interesting. I still think I need. I need, I need this kid to have more bro time. Like Grover's there, but he ain't throwing hands." (Winter Wolf, block 27:01:23 to 27:09:19)
Picture `USE\grover-camp-tee-ep2.png` to 27:10 (4 s). In: hard cut. Out: hard cut.
Notes: Names Grover. Plain. A second Grover still, a different shot from picture 18 (checked by wwd-pictures, far apart in the video). If the daughters claim is trimmed (stop 30) this stop moves about 20 s earlier, the words do not move.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 32. 28:33 - 28:38  |  PNG 26 (Nico resting his head on a table of small toy soldier figures (episode 302))  |  search: "Magic The Gathering"
Said: "They're kind of interesting, too, because we get the one little nerdy kid who's, like, into, like, Magic The Gathering." (Winter Wolf, block 28:25:11 to 28:43:07)
Picture `USE\nico-mythomagic-figures.png` to 28:38 (5 s). In: Flip Motion Impacts 10f (`Effects panel > Video Transitions > Modern Transitions > Animation > Flip Motion Impacts`). Out: hard cut. Why: a flip for the nerdy kid.
Sound: `P:\Sounds\Sound FX\Adobe\Multimedia\Multimedia Internet CD-Rom Flash Animation 12.wav` on the first frame of the transition, whole file (1.8 s), -18 dB. [PROPOSED level, file PROVEN on disk]
Notes: Matches on the kid and the game hobby. The hosts say Magic The Gathering cards, the picture shows toy figures, a detail that differs, and the game is UNVERIFIED (Still open 10, rewatch). If you trim that sentence, drop this picture. Flip Motion, quick and light.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 33. 28:39 - 28:44  |  PNG 27 (Bianca and Nico in camp tees at a weathered door (episode 302))  |  search: "Big Sis"
Said: "And Big Sis, who also didn't know they they didn't know they were half bloods until now." (Winter Wolf, block 28:25:11 to 28:43:07)
Picture `USE\bianca-nico-camp-doorway.png` to 28:44 (5 s). In: Mirror Impacts 12f (`Effects panel > Video Transitions > Modern Transitions > Transformers > Mirror Impacts`). Out: hard cut. Why: two sides, brother and sister.
Sound: `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Electronic Whoosh Digital Resonant Cymbal Wash 01.wav` on the first frame of the transition, first 1.5 s with a 0.5 s fade, -24 dB. [PROPOSED level, file PROVEN on disk]
Notes: The big sister and her brother, the two siblings the line is about. Mirror for two sides of one pair. It follows picture 26 by one second, both designed, the sounds differ.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 34. 29:25 - 29:29  |  PNG 28 (Luke in armor and a plumed helmet pointing a sword, forest (a SEASON 1 press still, face hidden, identity from the caption only))  |  search: "my dark horse"
Said: "So there's new stuff mixed with, oh, I also need to know what happens with Luke because that's like my dark horse." (Winter Wolf, block 29:07:21 to 29:26:02)
Picture `USE\luke-armor-sword-s1.png` to 29:29 (4 s). In: Film Dissolve 12f (`Effects panel > Video Transitions > Dissolve > Film Dissolve`). Out: hard cut.
Notes: WEAK fit, character only: Luke in season 1 armor (caption Episode 102) on a line about Luke's arc. The face is under the helmet, so it is the caption alone. It is the first picture to drop. 4 s, the line is 4 s long.
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 35. 29:33 - 29:56  |  CAM: single out Winter Wolf  |  search: "got into his head"
Said: "They showed us, dude." ... "He's not chaotic evil at all. He's just." (Winter Wolf, block 29:33:07 to 29:49:27)
Cut to Winter Wolf's solo camera. **CAM IN 29:33, CAM OUT 29:56, length 23 s.** Hard cut in, hard cut back to the two-shot. Cam file (Winter Wolf webcam): `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\Percy_Jackson_season_3_ep_1_and_2-Winter_Wolf-webcam-00h_00m_00s_870ms-StreamYard.mp4`. Sync first (Before you start, 7).
Notes: Winter Wolf's read on Luke: he cares, so he is not chaotic evil. He has the floor for both blocks (29:33 to 29:56), KingZ answers at 29:56. The cam goes in at the block start, "got into his head" is about 3 s in. "Holding the world up" is Winter Wolf's wording, the show has Atlas hold up the sky (facts row 28, leave). No picture on these seconds, picture 28 ends at 29:29. Fourth solo cam.
Tags: cam file PROVEN on disk (30 fps, 1920x1080 by ffprobe). Cut times PROPOSED (block stamps are exact, the second inside a block is word position). Sync NOT CONFIRMED.

### 36. 30:30 - 30:35  |  PNG 29 (Dr. Thorn, an older man in a dark military dress uniform with medals, snow and red light (episode 301))  |  search: "played thorn"
Said: "You didn't see the show, but that's the guy that played thorn, the manager." (Winter Wolf, block 30:14:23 to 30:32:05)
Picture `USE\dr-thorn-uniform-snow.png` to 30:35 (5 s). In: Luma Fade Impacts 12f (`Effects panel > Video Transitions > Modern Transitions > Essentials > Luma Fade Impacts`). Out: hard cut. Why: quiet, the manticore teacher.
Sound: `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Ambient Smooth Tension 01.wav` on the first frame of the transition, first 2 s with a 1 s fade, -24 dB. [PROPOSED level, file PROVEN on disk]
Notes: Line is about the actor who played Thorn, the picture is Thorn. "Gail" is a garble of "Gale" (Caption fixes). The hosts' talk of the actor's other roles (30:47 to 31:10) is UNVERIFIED in part (Still open 13), leave. Luma Fade, second use, far from the first (stop 12).
Tags: file PROVEN (on disk, checked by script). Match SOURCED (Picture-Fit report, tags file). In and out times PROPOSED (word position inside the block, plus or minus 2 s). Transition PROPOSED (name and click path SOURCED from premiere-transitions.md, not checked in your build).

### 37. 31:35 - 31:58  |  CAM: single out Winter Wolf  |  search: "That's weird for this show"
Said: "That's weird for this show." ... "Thanks, everybody." (Winter Wolf, block 31:35:05 to 31:48:29)
Cut to Winter Wolf's solo camera. **CAM IN 31:35, CAM OUT 31:58, length 23 s.** Hard cut in, hard cut back to the two-shot. Cam file (Winter Wolf webcam): `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\Percy_Jackson_season_3_ep_1_and_2-Winter_Wolf-webcam-00h_00m_00s_870ms-StreamYard.mp4`. Sync first (Before you start, 7).
Notes: The sign-off. Winter Wolf has the floor to the end of the video: the Friday release talk, "check it out", the comments call and "Thanks, everybody". CAM OUT is the end of your sequence (31:58). The Friday release is VERIFIED (facts rows 66 to 68). "These dropped early in the day" is UNVERIFIED but he hedges with "I think", leave. The Like and Subscribe clip (next stop) sits on top of this cam. Fifth solo cam.
Tags: cam file PROVEN on disk (30 fps, 1920x1080 by ffprobe). Cut times PROPOSED (block stamps are exact, the second inside a block is word position). Sync NOT CONFIRMED.

### 38. 31:49  |  STICKER: LIKE AND SUBSCRIBE (your own video, marker only)  |  search: "Let us know in the comments below"
Said: "Let us know in the comments below if you're watching." (Winter Wolf, block 31:48:29 to 31:58:05)
Drop your Like and Subscribe video on V3, starting on "Let us know in the comments below" (about 31:49), over the sign-off cam. I did not build it and I do not have its file path or length (Still open 25). If it runs longer than about 8 s, slide the start earlier, never past the last word (31:58). No transition.
Notes: The hosts do not say the words "like" or "subscribe", so this is the standing every-review stop (SOP), placed on their closing call to action. It sits before "we'll see you guys in the next one" so the last line is clear. No sticker is placed anywhere else: no host says "recommend", "dumpster fire" or "wolfie", "this is an endorsement for me" (28:04) is the closest and it is not a sticker word.
Tags: time PROPOSED. Stop SOURCED (SOP-WWD-Review-Workflow, memory wwd-skill-formats 2026-10-20).

### 39. 31:58  |  NEXT UP CARD (generic)  |  search: "Thanks, everybody"
Said: "...and we'll see you guys in the next one. Thanks, everybody." (Winter Wolf, block 31:48:29 to 31:58:05, the last block, the transcript ends 00:31:58:05)
Drop `P:\WWD Kit\Cards\Next Up - Next Review (MP4).mp4` on V4 right after "Thanks, everybody". 6.0 s, 1920x1080, carries its own audio (PROVEN by ffprobe: one video and one audio stream, 6.000 s). Use the MP4.
Notes: The hosts do not name the next review, so this is the GENERIC card. Do NOT use `Next Up - Percy Jackson Season 3 (MP4).mp4`, that card was made for the previous show's slot and points at this very review. The card's content was not viewed by me this job and not heard. Order is PROPOSED: Next Up first, then the end card (next stop).
Tags: file and length PROVEN. Choice SOURCED (wwd-director handoff 2026-11-23). Order PROPOSED.

### 40. 31:58  |  END CARD and OUTRO MUSIC  |  search: "see you guys in the next one"
Said: "Thanks, everybody." (Winter Wolf, last word of the cut)
End card BUILT 2026-11-23 by wwd-vfx, free, 0 credits: `P:\WWD Kit\Cards\End Card - Percy Jackson S3 (MP4).mp4` (12.000 s, 1920x1080, 30 fps, PROVEN by ffprobe; .mov and .png beside it). Look: star-chart night sky, says LOOK TO THE STARS, THANKS FOR WATCHING, NEXT: FROSTCAST EVERY WEDNESDAY 9 PM ET. Subscribe ring and two video tiles are drawn from frame 20 to the end. Audio was NOT heard by anyone. Drop it on the last word, then the generic Next Up card `P:\WWD Kit\Cards\Next Up - Next Review (MP4).mp4` (6.000 s, generic wording, the next review is not named). [PROVEN files, PROPOSED placement]
Outro music: owned pick proposed by the sound pull: `L:\Winter Wolfs Den review show\Audio\Main Channel Theme.mp3` (117.2 s, the channel's own theme, cut or fade it to the end card; owned but no receipt on disk) [PROPOSED, nothing heard]. Fallback below. (Still open 15) Adobe stand-in for a short close: `P:\Sounds\Music\adobe\Wedding&Event\Pachelbel_Canon_80BPM\Endings-Cadences\HornsFrenchEnding01.wav` (9.0 s, PROVEN by ffprobe, not auditioned), about -18 dB if it starts under the last words, full only after the last word. If the new end card carries its own audio (the existing ones do), add no music on top.
Notes: Music is the outro only, no bed anywhere else in the video.
Tags: card files PROVEN. Stand-in choice PROPOSED. Music PROPOSED, nothing heard.

---

## Transition map

| Stop | Picture | In | Out | Paired sound file |
|---|---|---|---|---|
| 2 | PNG 1 poster.png | hard cut  | Cross Dissolve 24f | none |
| 3 | PNG 2 percy-closeup-camp-tee.png | hard cut  | hard cut  | none |
| 4 | PNG 3 thalia-orange-hoodie-hill.png | Film Dissolve 12f | hard cut  | none |
| 5 | PNG 4 annabeth-forest-portrait.png | hard cut  | hard cut  | none |
| 6 | PNG 5 clarisse-camp-tee-s1.png | hard cut  | hard cut  | none |
| 7 | PNG 6 percy-thalia-faceoff-camp.png | hard cut  | hard cut  | none |
| 8 | PNG 7 annabeth-percy-winter-coats.png | Burn Alpha Impacts 10f | hard cut  | Fire Flare Start Up Ignite 01.wav |
| 11 | PNG 9 percy-nico-dance-floor.png | hard cut  | hard cut  | none |
| 12 | PNG 10 luke-stone-hall-ep-unconfirmed.png | Luma Fade Impacts 12f | hard cut  | Module Production Element Title Imaging Slow Swell Dramatic 01.wav |
| 13 | PNG 11 chiron-tweed-jacket-s1.png | Cross Dissolve 12f | hard cut  | none |
| 16 | PNG 12 thalia-aegis-shield-snow.png | Flash Impacts 10f | hard cut  | Multimedia Internet CD-Rom Flash Beep Whoosh 02.wav |
| 17 | PNG 13 artemis-huntresses-arrive-snow.png | hard cut  | hard cut  | none |
| 18 | PNG 14 apollo-sun-car.png | Light Leak Impacts 12f | hard cut  | Module Production Element Title Imaging Electronic Whoosh Calm 01.wav |
| 19 | PNG 15 artemis-bow-portrait.png | hard cut  | hard cut  | none |
| 20 | PNG 16 artemis-percy-snow.png | Soft Wipe Impacts 12f | hard cut  | Module Production Element Title Imaging Electronic Whoosh Digital Reverse Delay 01.wav |
| 21 | PNG 17 huntresses-bring-nico-bianca.png | hard cut  | hard cut  | none |
| 22 | PNG 18 grover-camp-tee-forest.png | Ray Impacts 12f | hard cut  | Module Production Element Title Imaging Electronic Whoosh Electrical 01.wav |
| 23 | PNG 19 hermes-casino-hoodie-s1.png | Zoom Blur Impacts 10f | hard cut  | Weapon Staff Whip Thin Fast 01.wav |
| 24 | PNG 20 zeus-suit-s1.png | hard cut  | hard cut  | none |
| 25 | PNG 21 hades-green-jacket-s1.png | Blur Dissolve Impacts 14f | hard cut  | Module Production Element Title Imaging Empty Electronic Whoosh 01.wav |
| 27 | PNG 22 poseidon-linen-shirt-s1.png | hard cut  | hard cut  | none |
| 28 | PNG 23 ares-motorcycle-s1.png | Directional Blur Impacts 10f | hard cut  | Transportation Auto Motorcycle Drive By Fast 01.wav |
| 29 | PNG 24 mr-d-dionysus-hawaiian-shirt-s1.png | Spring Motion Impacts 10f | hard cut  | Cartoon Spring Twang 10.wav |
| 31 | PNG 25 grover-camp-tee-ep2.png | hard cut  | hard cut  | none |
| 32 | PNG 26 nico-mythomagic-figures.png | Flip Motion Impacts 10f | hard cut  | Multimedia Internet CD-Rom Flash Animation 12.wav |
| 33 | PNG 27 bianca-nico-camp-doorway.png | Mirror Impacts 12f | hard cut  | Module Production Element Title Imaging Electronic Whoosh Digital Resonant Cymbal Wash 01.wav |
| 34 | PNG 28 luke-armor-sword-s1.png | Film Dissolve 12f | hard cut  | none |
| 36 | PNG 29 dr-thorn-uniform-snow.png | Luma Fade Impacts 12f | hard cut  | Module Production Element Title Imaging Ambient Smooth Tension 01.wav |

Counts: 28 picture stops. Designed Modern transitions: 13 (46 percent). Film Dissolve: 2. Cross Dissolve: 2 stops (poster out, Chiron in). Other stops with a hard cut in: 11 (the poster's in is the video open, its out is the Cross Dissolve). Never the same transition twice in a row. Longest run of designed stops in a row: 2. The clip, the cams, the markers and the cards are hard cuts and are not counted here. Cross Dissolve is within the limit of 3.

## Sound list (every cue on the sheet, ready to drag in)

All files exist (PROVEN by script). All Adobe library, owned. Levels PROPOSED. Nothing was heard.

| Stop | File | Part | Level |
|---|---|---|---|
| 8 | `P:\Sounds\Sound FX\Adobe\Fire and Explosions\Fire Flare Start Up Ignite 01.wav` | first 1.5 s with a 0.5 s fade | -20 dB |
| 12 | `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Slow Swell Dramatic 01.wav` | first 2.5 s with a 1 s fade | -22 dB |
| 16 | `P:\Sounds\Sound FX\Adobe\Multimedia\Multimedia Internet CD-Rom Flash Beep Whoosh 02.wav` | whole file (1.5 s) | -20 dB |
| 18 | `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Electronic Whoosh Calm 01.wav` | first 1.5 s with a fade | -22 dB |
| 20 | `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Electronic Whoosh Digital Reverse Delay 01.wav` | first 1.5 s with a 0.5 s fade | -22 dB |
| 22 | `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Electronic Whoosh Electrical 01.wav` | first 1.5 s with a 0.5 s fade | -22 dB |
| 23 | `P:\Sounds\Sound FX\Adobe\Weapons\Weapon Staff Whip Thin Fast 01.wav` | whole file (0.41 s) | -16 dB |
| 25 | `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Empty Electronic Whoosh 01.wav` | first 2 s with a 1 s fade | -24 dB |
| 28 | `P:\Sounds\Sound FX\Adobe\Transportation\Transportation Auto Motorcycle Drive By Fast 01.wav` | whole file (5.1 s), fade out the last 1.5 s | -18 dB |
| 29 | `P:\Sounds\Sound FX\Adobe\Cartoon\Cartoon Spring Twang 10.wav` | whole file (1.9 s) | -14 dB |
| 32 | `P:\Sounds\Sound FX\Adobe\Multimedia\Multimedia Internet CD-Rom Flash Animation 12.wav` | whole file (1.8 s) | -18 dB |
| 33 | `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Electronic Whoosh Digital Resonant Cymbal Wash 01.wav` | first 1.5 s with a 0.5 s fade | -24 dB |
| 36 | `P:\Sounds\Sound FX\Adobe\Imaging Elements\Module Production Element Title Imaging Ambient Smooth Tension 01.wav` | first 2 s with a 1 s fade | -24 dB |
| 15 | `P:\Sounds\Music\adobe\Drum One Shots\Drum_One-Shots_Brushes\Rimshot03.wav` | whole file (0.66 s) | -6 dB |

Optional intro and outro stand-ins are in stops 1 and 40.

## Caption fixes (short list, from the facts file, transcript garbles and not spoken errors)

Fix these in the captions or the burned-in text if you use auto captions. Full list with the listen-first items: `D:\WKP\WWD\reports\Percy-Jackson-S3-E1-2-Facts.md`, section "Caption fix list".

| Timecode | Find | Replace |
|---|---|---|
| 00:46 | "first season" (the clips) | "third season" |
| 01:16, 03:20, 16:03, 18:10, 20:41, 28:17 | "Thora", "Fabia", "thalli", "Thor you", "Thala", "Phala" | "Thalia" |
| 02:01, 20:10 | "value" | "Thalia" |
| 01:30, 16:11 | "Annabel", "Annabelle" | "Annabeth" |
| 01:42 | "Bronze" | "Ron" |
| 02:46 | "Titans cars" | "Titan's Curse" |
| 03:20, 07:34, 11:20 | "Clarice" | "Clarisse" |
| 03:20, 10:51, 11:08, 24:22 | "Aries" | "Ares" |
| 05:20 | "Middle Potter" | "Harry Potter" |
| 06:49, 06:55 | "mana core", "Manafort", "man core", "Thorne" | "manticore", "Thorn" (and "a manticore has a scorpion tail") |
| 07:50, 10:23 | "Kiran", "Kieran" | "Chiron" |
| 14:00 | "Daphne Keene", "formally X-23" | "Dafne Keen", "formerly X-23" |
| 23:37 | "giving earth to fire to the humans" | "giving fire to the humans" |
| 24:33 | "Haiti" | "Hades" |
| 30:12 | "Gail" | "Gale" |

Listen first (text alone cannot fix): 04:51 "bobbing", 09:17 "hits though your staff", 10:23 "from torch", 16:40 "free to see Cal", 24:22 "Ed" (maybe "Edge"), 25:13 to 25:19 "Raffi", "he's a Demeter", "Mr. Nice", 25:58 "He was a fireball", 30:26 "thorn, the manager".

## Gaps and flags

**Stretches over 25 s with no picture, cam or clip (the hosts' faces carry them).** 20 stretches, 1554 s in all of the 1918 s. Every stretch over 60 s has a concrete PROPOSED fill. Most fills need a picture or clip that is NOT on disk, they wait on Jarvis's browser pull (list in `D:\WKP\WWD\reports\Percy-Jackson-S3-E1-2-Picture-Fit.md`, "JARVIS BROWSER PULL LIST") or on Zac relaxing the 6 s clip floor. A solo cam fill is PROPOSED only, "a few cams" is the rule and this sheet already has 5.

| From | To | Seconds | Fill |
|---|---|---|---|
| 00:07 | 00:43 | 36 | talk-led, none needed (36 s, the hosts open the review and the host cam carries it) |
| 00:47 | 01:22 | 35 | talk-led, none needed (35 s) |
| 01:31 | 03:35 | 124 | PROPOSED fill, none on disk: Ron and Hermione aside at 01:39 stays spoken only (other-title pictures only on a joke that matches exactly, none does). Book cover for "The Titan's Curse" at about 02:33 (line 02:28 to 02:46) from the publisher page, and the two earlier film posters at about 02:40 ("they never made a third movie of this, those died like they did two"). All three are on the browser pull list for Jarvis, wwd-pictures resizes and tags them. Also a PROPOSED solo cam is NOT needed here. |
| 04:00 | 04:28 | 28 | talk-led, none needed (28 s) |
| 05:27 | 06:16 | 49 | talk-led, none needed (49 s). The Chapstick quip at 05:27 is spoken only. |
| 06:33 | 07:12 | 39 | talk-led, none needed (39 s). The manticore and the monster effect (06:30 to 06:49) have no still in the press set, trailer-only (Still open 17). |
| 07:17 | 07:54 | 37 | talk-led, none needed (37 s) |
| 07:58 | 09:37 | 99 | PROPOSED fill: the two short trailer shots U1 (garage pipes burst, about 1.9 s, line 08:50) and U2 (the boy behind a wall of falling water, about 3.7 s, line 09:02, "toaster baths"). Both are under the 6 s floor, so they only go in if Zac relaxes the floor, edges are NOT frame-verified (Clip-Placements section 3). The Spoiler Alert clip also covers about 08:20. |
| 09:42 | 12:44 | 182 | PROPOSED fill, 182 s: (1) short clip U4, the dome of water around a statue (about 1.2 s, line 10:24 "Dome Shield"), same floor problem; (2) an Atlas first-look still at about 12:07 ("they introduced of course, Atlas"), on the pull list (TV Insider page, save as atlas-first-look.jpg); (3) no picture exists for Chiron stopping the fight. Needs Jarvis's browser pull, then wwd-pictures. |
| 13:00 | 13:48 | 48 | talk-led, none needed (48 s, the Apollo title-list gag) |
| 13:54 | 14:32 | 38 | talk-led, none needed (38 s) |
| 14:37 | 16:59 | 142 | PROPOSED fill, 142 s: an Oracle still (green mist, S3) at about 15:19 and a sea cow still at about 16:35, both on the browser pull list (IMDb S3 photos or a trailer screenshot, caption must name the subject). The Oracle green-haze trailer shot (about 3 s, very dark) is unproven as this scene, no clip. If nothing arrives, a PROPOSED solo cam for KingZ at 15:19 to 15:43 (he tells the Oracle scene, one speaker). |
| 17:03 | 20:48 | 225 | PROPOSED fill, 225 s: the Oracle still (at 19:04, "the mother of Norman Bates", Oracle appears) from the same pull; Atlas and Artemis vision (19:17) has no still. Nothing for the water charge (18:11) exists, the four official videos do not contain it. A trailer screenshot is the only route. If nothing arrives, a PROPOSED solo cam for KingZ at 18:56 to 19:17 (Oracle entrance, one speaker). This is the longest bare stretch. |
| 22:07 | 24:18 | 131 | PROPOSED fill, 131 s: the Atlas first-look still again is NOT allowed (one use per video), so use a second pull: an Atlas still at about 24:00 ("not physically imposing") only if the pull returns two different Atlas images. Otherwise a PROPOSED solo cam for Winter Wolf at 23:57 to 24:17 (his point on the casting, one speaker). |
| 24:33 | 25:03 | 30 | talk-led, none needed (30 s) |
| 25:08 | 26:41 | 93 | PROPOSED fill, 93 s: a season 2 still of Tantalus (the camp head who ate and could not be full) at about 25:58, from the Disney press kit season 2 gallery, not retrieved. Otherwise talk-led. |
| 27:10 | 28:33 | 83 | PROPOSED fill, 83 s: a solo cam for Winter Wolf at 27:47 to 28:04 ("this is an endorsement for me", one speaker). A season 2 Tyson still at 27:11 ("threw a cyclops out of a cave") is on no pull list yet. |
| 28:44 | 29:25 | 41 | talk-led, none needed (41 s) |
| 29:56 | 30:30 | 34 | talk-led, none needed (34 s) |
| 30:35 | 31:35 | 60 | talk-led, none needed (60 s, the Thorn actor talk, a few UNVERIFIED lines, Still open 13) |

**Other flags**
- **Spoken-only beats (no honest picture, nothing placed by look):** Atlas (12:00 to 12:19 and 23:22 to 24:17), Kronos (12:27), the Oracle and the green mist (15:19 to 15:43, 19:04 to 19:17), the sea cow (16:35 to 16:49), the water-sphere dome fight (10:24 to 10:51), the water-main spin cut (08:50 to 09:17), Percy's sliding dash (07:00) and the charge across the water (18:11), the Apollo car crash (16:14), the manticore effect (06:30 to 06:49), Young Annabeth, Hera, Demeter, Athena, Persephone, Prometheus, Sisyphus.
- **Gags with no cue on purpose:** "toaster baths" (09:16, a joke about electrocution), "Doom got him" and the Doomsday aside (14:14 to 14:23), the Chapstick weapons quip (05:27), "Ron and Hermione" (01:39). Funny cues only on the hosts' own jokes, and not on death or electrocution talk.
- **No sticker is placed.** No host says "recommend", "wolfie" or "dumpster fire". No new Spoiler Alert was built (SOP).
- **Weakest picture fits, first to drop if you want fewer:** picture 28 (Luke in S1 armor on "my dark horse", character only, face hidden), picture 10 (Luke in a stone space, episode unconfirmed), picture 26 (toy figures on a Magic The Gathering line).
- **A `.claude` folder** dated Nov 23 20:10 already sits in the movie folder (it holds only `agent-memory`). I did not create it and did not touch it.
- **Not done by this job (done by other benches 2026-11-23, see Still open):** the sound pull folder, the rights note, the intro and outro pick, the end card. See Still open.
- The Luke world-holding shot from the Curse Teaser (YouTube `7D8y_W4YmoI`, about 15 s, one shot) is ON HOLD. If Zac supplies who the holder is and says it is Luke, it becomes an optional clip stop at 29:33 (the cam stop's words "got into his head"), 7 to 8 s cut by wwd-clip-scout. It is NOT on the sheet.

## Still open

**Spoken claims to decide (from the facts file, 69 rows, `D:\WKP\WWD\reports\Percy-Jackson-S3-E1-2-Facts.md`). Action is TRIM, CAPTION or LEAVE. No cut or caption has been made.**

- **Open 1.** **WRONG, the Hades "no demigod" claim.** KingZ at 04:00 to 04:06 ("the child of Hades, which I don't think they have one", block 03:52 to 04:06, and Winter Wolf's "Oh, that's right" reply at 04:06:21 to 04:08:12 reacts to it), then KingZ at **22:20:16 to 22:24:11** ("I don't think Hades ever has a demigod") and Winter Wolf at 22:24:13 to 22:31:01 ("No, I don't"). The show's cast lists Nico and Bianca as Hades's children. NOTE: the facts file gives the second timecode as 22:24, which is Winter Wolf's answer, KingZ's own sentence is the block before it. Action: TRIM 22:20:16 to 22:31:01 and 04:02 to 04:08 (recommended by fact-research), OR leave both and pin a correction. Zac's call. Confirm on a rewatch whether the episodes name them before putting a correction on screen (spoiler rule).
- **Open 2.** **UNVERIFIED, no support: special forces fathers "mostly have girls".** KingZ, **26:41:12 to 26:56:01** (the claim, in the cam stop 30) and again 26:57:10 to 27:01:21. NOTE: the facts file says 26:56 to 27:01, which misses the first sentence, the claim starts at 26:41. Action: TRIM 26:41:12 to 27:01:21 (about 20 s), then skip stop 30. Winter Wolf's next block (27:01:23, "Interesting. I still think I need...") starts with one "Interesting" that goes with the cut, then picture 25 stays.
- **Open 3.** **WRONG, "Prometheus was a god".** KingZ, 23:34:25 to 23:36:07 (Winter Wolf echoes "Was a god" at 23:36:11 to 23:37:15). Prometheus is a Titan. Action: TRIM 23:34 to 23:37, or CAPTION "Prometheus is also a Titan". Recommend trim.
- **Open 4.** **UNVERIFIED, probably wrong, Grover "a child of Pan".** KingZ, about 20:51 to 20:55 (last sentence of block 20:43:04 to 20:55:12). Action: TRIM that sentence, or CAPTION "Grover is a satyr, a follower of Pan". Recommend trim. Picture 18 (stop 22) ends at 20:51 just before it.
- **Open 5.** **UNVERIFIED, probably wrong, the "Maze Runner kid".** KingZ, about 02:49 to 02:52 (block 02:46:06 to 02:52:06). Also "they all aged out of their roles" (02:46 to 02:49) is UNVERIFIED, low risk. Action: TRIM the one Maze Runner sentence. Winter Wolf's next block (02:52:11) does not depend on it.
- **Open 6.** **WRONG but corrected on air, "Atlas is not technically a Titan".** Winter Wolf, 23:22:15 to 23:24:03, fixed by KingZ at 23:24 and Winter Wolf at 23:26. Action: LEAVE.
- **Open 7.** **WRONG as stated, Percy "the only one to Poseidon".** Winter Wolf, 09:49:18 to 09:59:03. KingZ half corrects at 10:07 ("not the only one ever"). Action: LEAVE (or trim 09:49 to 10:07).
- **Open 8.** **UNVERIFIED, Apollo and Dafne Keen.** KingZ and Winter Wolf, 13:00 to 13:12, the "god of fate and the sun god ... travel and poetry" list: LEAVE if it is the show's gag, CAPTION "oracles, music, archery, healing" if it is KingZ's own. Winter Wolf, 14:06 to 14:14, Dafne Keen "not done much as an adult" (WRONG, hedged) and "reappearing in Doomsday" (UNVERIFIED, a joke): LEAVE, or TRIM 14:06 to 14:14.
- **Open 9.** **UNVERIFIED, Percy "like six three".** Winter Wolf, 00:35:12 to 00:46:24 (picture 2 sits on it). Last height found is 5 ft 7 in from Dec 2023. Action: LEAVE as a rough joke, or TRIM the words (and drop picture 2). Low risk.
- **Open 10.** **UNVERIFIED, "Magic The Gathering".** Winter Wolf, 28:25:11 to 28:43:07 (picture 26 sits on it). In the books Nico plays Mythomagic. Action: rewatch, then LEAVE, CAPTION, or TRIM 28:25 to 28:32 and drop picture 26.
- **Open 11.** **UNVERIFIED, "she's Zeus's only child on the planet", the show said so.** Winter Wolf, 09:23:18 to 09:45:00 (picture 12 sits on it). Action: LEAVE, confirm on a rewatch.
- **Open 12.** **Listen first (garbles that text cannot settle):** "Ed" at 24:22 (maybe Edge), "Raffi" and "Mr. Nice" at 25:13 to 25:19, "hits though your staff" at 09:17. Also NOT CHECKED, leave: the dagger and sea cow talk at 16:11 to 16:49.
- **Open 13.** **UNVERIFIED in part, the Thorn actor's other roles.** Winter Wolf and KingZ, 30:47 to 31:10 ("got shot in the face", "thrown out of his own law firm"). Actor is VERIFIED, details not retrieved. Action: LEAVE.

**Production items**

- **Open 14. CLOSED 2026-11-23.** End card built by wwd-vfx: `P:\WWD Kit\Cards\End Card - Percy Jackson S3 (MP4).mp4` (stop 40). Not heard, no qa-director pass. Do not use the A Knight's Tale card.
- **Open 15.** **Intro and outro music: not chosen.** The `music` agent owns the pick (owned only, intro 6 s or less). Stand-ins named in stops 1 and 40, nothing auditioned. Route through wwd-director.
- **Open 16.** **Spare picture:** `annabeth-percy-winter-dance.png` is not placed (the clip owns its line). If Zac prefers the picture over the clip on that line, swap and the clip drops.
- **Open 17.** **Browser pull list** (Atlas, the Oracle, the sea cow, S3 frames of Chiron, Clarisse and Mr. D, a Tantalus still, the Titan's Curse book cover, the two earlier film posters) is Jarvis's, in the Picture-Fit report. The trailer-only action beats are clip-scout jobs only if Zac relaxes the 6 s clip floor (U1 to U4 in the Clip-Placements report, edges NOT frame-verified).
- **Open 18.** **wwd-rights:** log the Disney+ marks on the clip and the Disney press-kit images (page gives no license text beyond its footer). The clip came from Disney Plus's own YouTube upload.
- **Open 19.** **Hades statements are on both ends of the cut** (04:02 and 22:20). If Zac keeps them and pins a correction, the correction text belongs to fact-research and marketing, not this sheet.
- **Open 20.** **Cam sync NOT confirmed.** KingZ has no cam file between about 05:40 and 13:33 of the raw recording (Before you start, 7).
- **Open 21.** **Sound pull folder BUILT 2026-11-23 (assistant-editor, 17 files, all open in ffprobe).** Import from `P:\WWD Kit\Percy Jackson S3 (The Titan's Curse)\Sounds\` (README.md inside; files named by stop number). Report `WWD\reports\Percy-Jackson-S3-E1-2-Sound-Pull.md`. Stops 1, 15 and 40 and the music candidates come from the Adobe MUSIC tree, whose license file was not checked (subscription only, unproven by file). Every cue's path is in the Sound list above, parseable by the sound pull script.
- **Open 22.** **Latest sequence not compared.** No export or sequence length is on disk (Timing check).
- **Open 23. CLOSED 2026-11-23.** Rights note written: `WWD\reports\Percy-Jackson-S3-E1-2-Rights-Note.md` (HIGH 0, MEDIUM 3). Zac: keep or drop the clip, spot-check picture bottom edges for baked-in copyright lines, rule on the fact trims, send the export for a recheck.
- **Open 24.** **Stray folder** `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\.claude\` (created 20:10 on 2026-11-23, before this job). Not mine, untouched. Delete it when convenient.
- **Open 25.** **Like and Subscribe file path and length not on file.** Zac's own clip, I do not know where it lives.
- **Open 26.** **Premiere menu paths NOT VERIFIED in Zac's build** (Window > Text > Transcript, Modern Transitions folders, Set Transition Duration). Copied from the A Knight's Tale sheet and premiere-transitions.md.

40 stops: 28 picture, 5 CAM (1 conditional), 1 USE VIDEO clip, 1 SPOILER marker, 1 SOUND ONLY, 1 LIKE AND SUBSCRIBE, 1 INTRO (optional), 1 NEXT UP card, 1 END CARD.
