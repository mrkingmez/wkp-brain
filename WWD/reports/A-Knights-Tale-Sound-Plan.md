# A Knight's Tale (2001) first-watch: sound cue plan (wwd-sound, 2026-11-19)

For wwd-run-sheet. Built from the 36:37 transcript, `USE\timeline-placements.md` and `clips\clip-list.md`. I cannot hear audio. Every pick is by file name and by ffmpeg meter reading (ebur128, integrated loudness and true or sample peak, measured today). Nothing was auditioned. Zac checks by ear.

All paths are owned (`P:\Sounds\`). Levels are Premiere Volume > Level on the effect clip. Effective peak = file peak + level.

## 0. Tone map (what gets no cue)

Tone of the film: comedy-adventure, medieval jousting, rock soundtrack, "violence is WWF comedy". Fun cues fit. These beats get NO comedy sound and NO designed move:
- 02:25 to 02:32, "after their knight, their knight, passes away" (the mentor's death, same block as the director line). Picture 03 stays a plain cut.
- 17:51 to 20:33, the dark night: pillory, arrest, jail cell and the straw, the crew taking tomatoes. No cue.
- 20:33 to 21:05, the father and son reunion ("a call back to his dad", "reunion was moving"). No cue. Clip 3 sits here, silent.
- 27:24 to 28:10, Heath Ledger's death and the cause talk (pictures 26 and 27). No cue, quiet cut. The last cue before it ends by 27:21.
- 28:31 to 29:10, injuries and fight-violence talk. No cue.

## 1. Gag cues (7, each on a line the hosts earned)

Search words were each grep-checked: exactly 1 hit in `A knights Tale.txt`. Times are Premiere cut timecodes, MM:SS:FF, estimated inside the block by word position (plus or minus 2 s). Anchor on the search words, not the time. If Zac cuts the 06:32 and 29:54 to 30:24 patches, every time after those shifts.

| # | Search words | Cut TC | File | Trim | Level | Peak after level | Why |
|---|---|---|---|---|---|---|---|
| G1 | `discount on accountability` | 00:01:10:20 (block 00:00:55:15 to 00:01:12:06) | `P:\Sounds\Music\adobe\Drum One Shots\Drum_One-Shots_Brushes\Rimshot03.wav` | whole file, 0.66 s | -6 dB | -8.9 dBFS | Winter Wolf's pay-off to his own bit. Same rimshot used in Vision Quest 8. |
| G2 | `Much, much pain` | 00:03:04:00 (block 00:03:01:05 to 00:03:04:16) | `P:\Sounds\Sound FX\Adobe\Weapons\Weapon Armor Hit 03.wav` | whole file, 0.5 s | -8 dB | -8.8 dBFS | Tudyk gag line, slapstick pain. Lands on "pain". Picture 07 sits here, keep 07 a plain cut so the hit is the only sound. |
| G3 | `Pope may be French` | 00:05:02:10, on "English" (block 00:04:54:12 to 00:05:03:09) | `P:\Sounds\Sound FX\church-bell-multiple_zymjaZ4_.mp3` | first 1.5 s, fade out 0.5 s | -10 dB | -13.2 dBFS | KingZ quotes the film's own joke line. Must be out by 00:05:03:10, Winter Wolf says "Yeah." at 00:05:03:11. |
| G4 | `knocked off the boat` | 00:21:20:00 (block 00:21:11:22 to 00:21:33:21) | `P:\Sounds\Sound FX\jump-into-water-splashes_MyjdEHNd.mp3` | first 1.5 s, fade 0.3 s | -14 dB | -14.1 dBFS | The boat-training gag he calls "in and out, funny". It is a drowning bit played for laughs in the film and in his telling. Splash only, no bubbles, no comic horn. If Zac thinks a near-drowning is too close to a heavy beat, drop this one first. |
| G5 | `flattened him` | 00:27:19:00 (block 00:27:09:03 to 00:27:22:16) | `P:\Sounds\Sound FX\Adobe\Weapons\Weapon Armor Hit 02.wav` | whole file, 0.43 s | -8 dB | -9.1 dBFS | Battering-ram test of the new armor, he calls it "hilarious". Ends 2.5 s before "R.I.P. Heath" at 27:24, so there is a clear silence going into the tribute. |
| G6 | `Crowd was doing it` | 00:33:32:04 (KingZ block 00:33:32:04 to 00:33:41:07) | `P:\Sounds\Sound FX\Adobe\Human Elements\Human Crowd Stomping Feet 02.wav` | first 2.5 s, fade 0.5 s | -8 dB | -15.1 dBFS | The "We Will Rock You" crowd line, the film's rock-music joke. File is quiet (-32.4 LUFS, peak -7.1), so the level is lighter than other cues on purpose. Picture 31 sits here, keep 31 a plain cut. Pace of the stomp in the file not heard, Zac checks it reads as stomp-stomp. |
| G7 | `I will make you naked for eternity` | 00:23:45:12, on "You die" (block 00:23:42:17 to 00:23:48:22) | `P:\Sounds\Sound FX\sword-pull-from-sheathe_zyjdbqEu.mp3` | whole file, 0.34 s | -10 dB | -10.8 dBFS | Chaucer's mock sword threat, the quoted line Winter Wolf calls "the funniest way". Optional: if it feels like too much with transition 19 seven seconds earlier, drop G7. |

Count: 7 gag cues in 36:37, one about every 5 minutes. Optional to drop in order: G4, G7.

Not given a cue on purpose: the Prince Edward argument (08:30 to 09:29, hosts correcting each other), the Debo Treatment line (10:15, clip 1 plays muted under it and the joke is about heads), "Humperdinck" and the Game of Thrones asides, the movie quotes at 10:11 and 22:08. Silence counts as a cue.

## 2. Pool for designed (Modern) transitions

About half of the 32 stops: 16 designed, 16 plain. Plain Cross Dissolve on 3 stops at most.

Suggested split (wwd-run-sheet may change the transition names, keep the tone rules):
- **Designed (16):** 04, 06, 08, 09, 11, 13, 14, 16, 18, 19, 21, 23, 25, 29, 30, 32.
- **Plain (16):** 01 (poster, slow Cross Dissolve 20 to 30 frames, no sound), 02 (Cross Dissolve), 03 (hard cut, "passes away" in the same block), 05, 07 (hard cut, G2 owns this moment), 10, 12, 15, 17, 20, 22, 24, 26 (Cross Dissolve, slow, quiet, death tribute), 27 (hard cut, Joker line sits on the death talk), 28, 31 (hard cut, G6 owns this moment).
- Cross Dissolve count: 01, 02, 26 = 3 (the limit).
- Heavy-beat stops that stay plain, say why in the sheet: 03, 26, 27.

Paired sounds (one per designed stop, none repeated on neighbors, none doubled with a gag cue). Level is Volume on the first frame of the transition. Peak column is file peak plus level.

| Stop | Picture | Suggested transition family (meaning map) | Sound file (all under `P:\Sounds\Sound FX\` unless noted) | Trim | Level | Peak after level |
|---|---|---|---|---|---|---|
| 04 | the cast | Pop Motion or Spring Motion (ensemble pops in) | `Adobe\Multimedia\Multimedia Internet CD-Rom Flash Pop Up 05.wav` | whole, 0.28 s | -10 dB | -11.7 |
| 06 | jocelyn portrait | Glow or Light Sweep (love interest) | `Adobe\Foley\Foley Bell Metal Handbell Short Ring 01.wav` | first 2 s, fade | -14 dB | -19.0 |
| 08 | chaucer announces | Light Sweep or Flare (the herald) | `audioblocks-frost-low-whoosh_BWSg1QdQKvL.mp3` | first 1.5 s | -20 dB | -20.7 |
| 09 | the gang at the rail | Push or Slide | `deep-fast-whoosh_GyZDnHNu.mp3` | whole, 1.6 s | -20 dB | -19.8 |
| 11 | ten things i hate about you | Mosaic or Chaos (other title, teen movie) | `Adobe\Multimedia\Multimedia Internet CD-Rom Flash Beep Whoosh 02.wav` | whole, 1.5 s | -20 dB | -21.5 |
| 13 | peasants and buddies | Slide | `fast-strong-wind-whooshes_fyhBVHEu.mp3` | first 1.5 s | -22 dB | -22.0 |
| 14 | the first joust | Pull Motion or Travel Motion (rider pass-by) | `Adobe\Animals\Animal Horse Canters By 01.wav` | first 2.5 s, fade | -10 dB | -11.6 (file is quiet, -33.6 LUFS) |
| 16 | the splinter lance | Slice or Linear Wipe | `Adobe\Weapons\Weapon Axe Whip 01.wav` | whole, 0.23 s | -14 dB | -14.5 |
| 18 | treated his men | Frame or Louver | `Adobe\Foley\Foley Chains Rattle Short 01.wav` | whole, 1.4 s | -16 dB | -17.1 |
| 19 | chaucer naked | Spring Motion or Flip Motion (comic) | `Adobe\Weapons\Weapon Broad Sword Hit Metal Tink 01.wav` | whole, 0.79 s | -12 dB | -12.6 |
| 21 | kate at the forge | Plateau Wipe or Stretch Wipe | `Adobe\Weapons\Weapon Armor Hit 01.wav` | whole, 0.58 s | -10 dB | -10.9 |
| 23 | the ballroom | Luma Fade or Blur Dissolve | `Adobe\Imaging Elements\Module Production Element Title Imaging Slow Swell Dramatic 01.wav` | first 2.5 s, fade 1 s | -22 dB | -24.2 |
| 25 | harden steel | Split or Block Motion | `Adobe\Weapons\Weapon Broad Sword Hit Metal Short 01.wav` | whole, 0.17 s | -12 dB | -12.2 |
| 29 | stunt armour | Mirror or Split | `Adobe\Weapons\Weapon Broad Sword Hit Metal Deflect 01.wav` | whole, 0.23 s | -12 dB | -12.4 |
| 30 | the heartthrob | Glow or Flare | `Adobe\Imaging Elements\Module Production Element Title Imaging Electronic Whoosh Calm 01.wav` | first 1.5 s, fade | -22 dB | -25.6 |
| 32 | the romantic scene | Blur Dissolve or Soft Wipe | `Adobe\Imaging Elements\Module Production Element Title Imaging Empty Electronic Whoosh 01.wav` | first 2 s, fade 1 s | -24 dB | -27.6 |

Spare medieval or flavored sounds if the sheet swaps a transition: `sword-whoosh-in-hall_GyaJhr4_.mp3` (3.7 s, loud, peak +0.2, use -18 dB, trim to first 1.5 s) for a Slice or Wipe, `Adobe\Animals\Animal Horse Snort 01.wav` (0.9 s, -14 dB) for a joust stop, `Adobe\Human Elements\Human Crowd Cheer 04.wav` (13.6 s, trim 2 s, -18 dB) for a crowd or ensemble stop, `audioblocks-fast-start-whoosh_BKITlG8RwU.mp3` (-18 dB) for a hard Whip.

Do not use: `Sword Shring - Sound Effects - Download.mp3` (45 s, peak +5.4 dBFS, clips on its own), `hit-metal-hard_M1WQr3Eu.mp3` and `strong-cinematic-hit` as transition sounds (too big, peaks +0.5 and -0.3, they were VQ gag hits). No cartoon sounds on a transition over a heavy beat.

## 3. Intro and outro

- **Music:** intro and outro only, no bed. The cut opens on speech (00:00:03, first host word) and the transcript says no logo sting is in this export.
- **Standard WWD intro or outro music:** NOT FOUND. `L:\Winter Wolfs Den review show\Muisc\` is empty. `P:\WWD Kit\` has no intro or outro music file. The Godzilla run sheet calls it "your outro music", which points at Zac's own file kept outside what I can see. Not available: its path.
- **The logo sting that exists:** `L:\Winter Wolfs Den review show\VFX\burning logo.mp4` (5.0 s) and `Master Logo 2.mp4` (8.2 s). Both have an audio stream, and both measure silent (-70 LUFS, peak -inf). So they carry no sound. If Zac adds a logo sting at the open, it needs a paired sound. Candidate from owned kit, not auditioned: `P:\WWD Kit\Godzilla\Sounds\ST2 stomp layer 2 blast impact - Production Element Title Transition Blast Impact 01.wav` (Godzilla sound for a different sting, Zac to decide if it fits).
- **If Zac wants owned music for this video (rock, to match the film), options for the `music` agent to confirm, not auditioned, license files not on disk:** `P:\Sounds\Music\rock-the-crowd.mp3` (175.8 s, measured -7.4 LUFS, peak +1.1 dBFS, so it needs at least -10 dB of clip gain), `P:\Sounds\Music\rock-guitar_f1HxpNS_.mp3` (not measured). Adobe library rock loops under `P:\Sounds\Music\adobe\Funk&Rock1\` are license-clear (Adobe SFX library is OK per Zac) but are loops, so the music agent should pick one. I did not pick for him. Suno is lapsed, not used.
- **Placement and level:**
  - Intro: if used, start full on a silent open only. If it plays under speech, -18 dB under the voice, duck under the first host word (00:00:03) and out within 3 s.
  - Outro: start about 00:36:20 at -18 dB under KingZ's thank-you, rise to full only after Winter Wolf's last "By people" ends (00:36:37:28), if the cut runs past it for an end card. Duck under the last host word.
- The end card: no Knight's Tale card exists. Not checked further.

## 4. Clip silence check

ffprobe `-show_entries stream=codec_type` on all 11 files: each prints `video` only, no `audio` line.
- `clips\Premiere Ready\`: `PVEIr4MGaT8-muted.mp4`, `95N85bGdzw4-muted.mp4`, `1WwlHv69kik-muted.mp4`, `yygNdTxoHus-muted.mp4`, `_KzsTKqTq1M-muted.mp4`, `eAC2kNiKuEg-muted.mp4`
- Cut files: `AKT-clip-1-debo-heads.mp4`, `AKT-clip-2-stocks.mp4`, `AKT-clip-3-father.mp4`, `AKT-clip-4-dance.mp4`, `AKT-clip-5-joust.mp4`

**Clips silent: yes** (no audio stream in any of the five clip files or the six Premiere Ready copies). The in-export check (silence below -60 dB in the clip windows) is still to run on Zac's finished export, with `ebur128` or `silencedetect` over the five windows below.

Clip windows in the cut (start times from clip-list, length 3.8 to 4.0 s):
1. 00:10:15:01, 2. 00:14:55:11, 3. 00:20:33:25, 4. 00:26:11:00, 5. 00:31:10:25.

## 5. Flags for wwd-director and wwd-run-sheet (collisions found while mapping sounds)

- **Clip 4 overlaps pictures 23 and 24.** Clip 4 is 3.8 s at 26:11:00. Picture 23 runs 26:06 to 26:11 and picture 24 runs 26:12 to 26:19. The clip and picture 24 cover the same line.
- **Clip 5 overlaps picture 28.** Clip 5 is 3.8 s at 31:10:25. Picture 28 starts 31:11.
- The sheet must pick one of clip or picture at those two spots, or move the picture after the clip. Not my call. If the sheet keeps both on separate tracks, no sound conflict, because the clips are silent.
- Picture 02 (02:19 to 02:26) ends right before "passes away". Kept plain in my split. Picture 03 sits on "passes away", kept a hard cut.
- Cue times shift if Zac cuts "Cut that part, cut that part two" (06:32) or the 29:54 to 30:24 inflation-math patch.

## 6. Default levels and export target for the sheet

Written from STANDARDS.md addendum (2026-10-26), until Zac sets different:
- Voices carry the show. Voice target about -14 LUFS integrated for the whole export.
- Music (intro, outro only): about -18 dB under the voice when voice is present, full only on a silent open or close, ducked under the first and last host word. Source file `rock-the-crowd.mp3` needs -10 dB or more of clip gain first.
- Effects and transition sounds: peak no higher than -12 dB against voice peaks. The numbers in section 2 are Volume levels for that (whooshes -20 to -22, quiet ambience -24).
- Gag stings (G1, G2, G5, G7): may sit at -6 dB against voice peaks. Table above: effective peak -8.8 to -10.8 dBFS, which is under the -6 limit if voice peaks near -3 dBFS. Voice peak level not measured, no export or raw audio to read yet.
- Trailer audio: muted. Silence below -60 dB in every clip window.
- **Export target: -14 LUFS integrated, true peak under -1 dBTP.**
- Level of the voice to anchor "12 to 20 dB under": not available, no export. Rerun the meters on the finished export (`ebur128=peak=true`) and check the gag cues stay under voice peaks.

## 7. What was measured (today, ffmpeg ebur128)

Integrated loudness and peak of each chosen file are in the tables above (peaks) and here for the big ones: Rimshot03 -20.5 LUFS peak -2.9 dBFS; Weapon Armor Hit 01 to 03 peak -0.9, -1.1, -0.8; church-bell-multiple -17.6 LUFS peak -3.2; jump-into-water-splashes -18.2 LUFS peak -0.1; Human Crowd Stomping Feet 02 -32.4 LUFS peak -7.1; Horse Canters By -33.6 LUFS peak -1.6; sword-whoosh-in-hall -11.5 LUFS peak +0.2; deep-fast-whoosh -12.4 LUFS peak +0.2. Files with a clip under 0.4 s read -70 LUFS (too short for the gate), their sample peaks are in the tables.

## 8. What Zac needs to adjust by ear

- G6 stomp: the file is quiet and I did not hear its rhythm.
- G3 church bell: it must read as a comic sting, not a funeral bell. Trim or swap if it reads solemn.
- G4 splash (near-drowning gag): his call whether it sits too close to a heavy beat.
- Whether the horse canter (stop 14) and swell (stop 23) are audible at -10 and -22 against the hosts.
- The quiet ones at -22 to -24 (stops 13, 23, 30, 32) may need +2 to +4 dB, or may be fine.
- Outro and intro music choice (not found, see section 3).
