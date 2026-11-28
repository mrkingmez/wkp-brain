# Percy Jackson and the Olympians Season 3, Eps 1 and 2: Assembly v1 cut list and Premiere pickup sheet

Built 2026-11-25 by assistant-editor for Zac (Zac could not edit today). Winter Wolf (Matt) and KingZ (Zac). This is a ROUGH ASSEMBLY, not the final cut. Zac may finish it in Premiere from the pickup sheet below or ignore it.

## 1. The file

- Render: `L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\export\Percy-Jackson-S3-E1-2-Assembly-v1.mp4`
- Measured by ffprobe and ffmpeg on the finished file: 1920x1080, 30/1 fps, h264, 56504 frames, audio aac 48000 Hz 2 ch, duration 1883.467 s (31:23.47), integrated loudness -14.0 LUFS, true peak -1.3 dBTP, loudness range 5.9 LU.
- Black frames (blackdetect d 0.3 s): none. Freeze check (8 s still): none.
- Length breakdown: conversation 31:05.47 (55964 frames), then Next Up card 6.0 s, then End card 12.0 s (18 s, the outro music plays across both).
- The earlier edited-cut transcript was 31:58. This assembly's conversation is 31:05.47, so 0:52.70 was cut (content cuts 47.5 s, pause tightening 5.1 s, plus the quantizing of the intro take).
- I did not play the video and did not hear any audio. I viewed stills (contact sheets) and read back every spec with ffprobe, ffmpeg or a script. See section 10 for exactly what was and was not checked.

## 2. What the recording and the transcript really are (PROVEN by script)

- The recording `Percy Jackson season 3 ep 1 and 2.mp4` is 48:25 (2905.39 s), the StreamYard two-shot with the Winter Wolf's Den frame. I re-transcribed it on the GPU (whisperx large-v3, word timestamps) and matched it word for word against the Premiere transcript (`Percy Jackson season 3 ep 1 and 2.txt`, 31:58).
- Result: the 31:58 transcript is NOT a cut with gaps. It is two raw pieces: the intro take (raw 04:38.1 to 04:51.9, the "Percy Jackson and the Olympians is back on Disney+" paragraph, placed first) and then one unbroken stretch of the raw recording from 15:22 to 47:05.8. Every run-sheet time (E) maps to the raw recording by R = E + 908.0 s (to within word jitter). Everything before 15:22 (11 minutes of mic and stream troubleshooting, pre-show talk, a clip playing) and after 47:05.8 (shoulder and physical therapy talk, fan, ending the stream) is outside it.
- The Winter Wolf cam is 0.70 s behind the recording clock and the KingZ cam (second file) is 813.10 s, set by waveform match at four points (correlation 0.65 to 0.79 for Winter Wolf, 0.37 to 0.60 for KingZ, offsets steady within 0.02 s across the whole show). Cam sync is therefore checked, not assumed.

## 3. Cuts I made (every one, with why)

All are word-anchored on pauses. Times are raw-recording TC (HH:MM:SS:FF at 30 fps) and the spot in the new cut where the join sits. To restore one, put the raw range back in.

| # | What was said (raw words) | Raw out of the cut | Length | Joins at (new cut) | Why |
|---|---|---|---|---|---|
| C1 | KingZ: "So this is like the Maze Runner kid in it, right?" (raw 17:56.9 to 18:00.2) | 00:17:56:28 to 00:18:00:07 | 3.3 s | 00:02:47:13 | fact-research Open 5: unverified claim, one sentence |
| C2 | KingZ: "The only one we're missing is the child of Hades, which I don't think they have one." plus Winter Wolf: "Oh, that's right." | 00:19:10:01 to 00:19:15:28 | 5.9 s | 00:03:57:07 | fact-research Open 1: wrong claim (show lists Nico and Bianca as Hades's kids) plus the reaction to it |
| C3 | KingZ: "I mean, Pan could come back because he's technically a child of Pan." plus "Yep." | 00:35:59:08 to 00:36:03:20 | 4.4 s | 00:20:38:21 | fact-research Open 4: unverified, probably wrong |
| C4 | KingZ: "And the thing is, I don't think Hades ever has a demigod." plus Winter Wolf: "No, I don't... modern era, there's that. But" | 00:37:28:12 to 00:37:39:02 | 10.7 s | 00:22:02:20 | fact-research Open 1: wrong claim, repeated |
| C5 | KingZ: "Prometheus was a god." | 00:38:42:21 to 00:38:44:12 | 1.7 s | 00:23:06:09 | fact-research Open 3: wrong (Prometheus is a Titan) |
| C6 | KingZ: the special forces fathers "mostly have girls" talk (about 21 s) plus the two "Interesting." replies | 00:41:49:11 to 00:42:10:28 | 21.6 s | 00:26:10:15 | fact-research Open 2: no support found, 20 s; also drops the lone Interesting that answered it |

Content cuts are the fact-research trims from the run sheet's Still open list (Opens 1, 2, 3, 4, 5: the wrong or unsupported claims). Zac's order was to cut what does not add; a wrong claim does not add, and each cut is one short sentence. If you would rather keep any of them and pin a correction, restore that range. Left in on purpose (hedged or low risk per the facts file): Open 6 (Atlas Titan mistake, corrected on air), 7, 8, 9, 10, 11, 13.

Pause tightening (silence only, measured under -43 dB in the recording, 0.5 s left each side):

| Raw range | Length | Joins at (new cut) |
|---|---|---|
| 00:17:20:25 to 00:17:22:15 | 1.7 s | 00:02:13:00 |
| 00:23:28:06 to 00:23:30:02 | 1.9 s | 00:08:09:15 |
| 00:36:08:29 to 00:36:09:22 | 0.8 s | 00:20:44:00 |
| 00:39:25:11 to 00:39:26:04 | 0.8 s | 00:23:47:08 |

Only 4 dead-air gaps passed that test. The hosts' natural pauses, laughs and cross-talk were left alone so the room tone and the jokes stay.

## 4. Tangents and funny bits (so Zac can restore or drop one)

FUNNY, KEPT (Zac's rule: keep jokes):
- the Chapstick weapons quip, in the new cut at about 5:23.07 (run sheet clock 05:27).
- the condom-joke aside ('maybe season four'), in the new cut at about 5:29.09 (run sheet clock 05:37).
- 'Nobody died.' (gets the rimshot), in the new cut at about 8:10.17 (run sheet clock 08:22).
- 'toaster baths' and the bathing toasters riff, in the new cut at about 8:49.13 (run sheet clock 09:02).
- 'that girl was hilarious updating that list of his titles' (Apollo), in the new cut at about 13:03.25 (run sheet clock 13:15).
- the Doomsday riff, 'Doom got him', in the new cut at about 13:57.27 (run sheet clock 14:06).
- 'think of the mother of Norman Bates', in the new cut at about 18:49.29 (run sheet clock 19:00).
- 'move your desk again out of subbasement storage' (Hades and the basement), in the new cut at about 21:54.26 (run sheet clock 22:10).
- 'waiting in line at the DMV', in the new cut at about 23:29.05 (run sheet clock 23:57).
- Mr. D, 'Oh, fuck. More kids.', in the new cut at about 24:36.05 (run sheet clock 25:03).
- 'He's surrounded by a lot of girls. God bless him.', in the new cut at about 26:03.12 (run sheet clock 26:24).
- 'threw a cyclops out of a cave... ready to toss knuckles', in the new cut at about 26:18.18 (run sheet clock 27:11).
- Gale from Breaking Bad, 'he got shot in the face though', in the new cut at about 29:35.07 (run sheet clock 30:14).

TANGENTS I WEIGHED AND KEPT (about the show, or hedged jokes, or too short to matter):
- Books and audiobooks aside (run sheet clock 02:18 to 02:28), 10 s, sets up why they have not read this one.
- 'Clips for the first season' exchange (00:46 to 00:58, garbled but it is about this show).
- Pan to the fireplace point (05:54 to 06:10): KingZ's argument about keeping the show kid-level, that is the review.
- Dionysus and 'that character in a kids series' (25:23 to 25:35), a joke.
- Tantalus, the camp head who ate and could not be full (25:58 to 26:07), about the show.
- Skeleton Crew comparison (27:47 to 28:04): the argument for why this show builds hype, so it stays.
- Dafne Keen and Doomsday (14:06 to 14:23): hedged joke, run sheet Open 8 says LEAVE.
- Thorn actor's other roles (30:47 to 31:15): jokes, details partly unverified (Open 13, LEAVE).
- Friday release talk (31:15 to 31:35): VERIFIED facts (rows 66 to 68), and it is the sign-off.

NOT CUT BY ME BECAUSE ZAC ALREADY CUT IT: the recording before 15:22 (troubleshooting and pre-show) and after 47:05.8 (ending chatter). The first line spoken in the cut is the clean intro take from 04:38.

## 5. Music and the outro

- INTRO STING: `D:\WKP\scratch\pj-music\intro-6s.wav` (6.000 s, 48 kHz stereo, -13.8 LUFS, peak -1.4 dBFS as delivered) starts on the first frame, on the first words of the intro take. Level: first 2 s at 3 dB under the voice, then a 0.6 s glide to 22 dB under the voice, fade out over the last 0.35 s, ends at 6.0 s. Zac's rule is 6 s or less, so it ends clean at 6.0. The levels are set by measurement against the voice (voice about -17.7 dB RMS in the first 6 s), not by ear. Not heard.
- OUTRO MUSIC: `D:\WKP\scratch\pj-music\outro.wav` (18.000 s, -11.8 LUFS, peak -0.7 dBFS as delivered) starts on the first frame after the last word, plays across the 6 s Next Up card and the 12 s End card, level 1 dB under the speech average, 2 s fade at the end. Not heard.
- ORIGINAL OUTRO MUSIC: I looked for it and did not find any. The recording after the last word ('Thanks, everybody.' at raw 47:05.6) has no music: the mix goes to near silence for 6 s and then the hosts start talking about a shoulder injury and ending the stream (raw 47:12 on), measured per second on the main mix and on both cams. Nothing of the original outro is in this cut because the cut stops on the last word. If Zac's Premiere version has a music bed there, it was not in this recording.
- VOCALS CHECK: whisper (large-v3) found no speech in intro-6s.wav, intro-A.mp3, intro-B.mp3, outro.wav, outro-A.mp3 or outro-B.mp3. That is a speech-detector result, NOT a listen. Treat as probably instrumental, not confirmed.
- RE-RUN WITH NEW MUSIC: `python D:\WKP\scratch\pj-edit\remix.py <intro.wav> <outro.wav>` rebuilds the mix and re-muxes the mp4 as Assembly-v2 (v1 is kept). With no arguments it uses the two paths above.
- Music is the only music in the video, no bed under the talk (locked rule). Music licence: generated by Jarvis in ElevenLabs, terms and the Individual Use question are the open item on the ElevenLabs month plan, not settled here.

## 6. Premiere pickup sheet: the picture track and audio of the conversation, segment by segment

If Zac prefers to finish this himself: import `Percy Jackson season 3 ep 1 and 2.mp4`, make a 1920x1080 30 fps sequence, and lay these 12 segments end to end on V1 and A1 (set the Source In and Out in the Source Monitor, type the timecode, press **I** and **O**, then **,** to Insert; Premiere menu names and shortcuts here are NOT VERIFIED in Zac's build). Segment 1 is the intro take, segment 2 onward is the main conversation. The picture track is already done in the render and the run sheet times below match it.

| Seg | Source IN (raw TC) | Source OUT (raw TC) | Length | Sequence IN | Sequence OUT |
|---|---|---|---|---|---|
| 1 | 00:04:38:03 | 00:04:51:28 | 0:13.83 | 00:00:00:00 | 00:00:13:25 |
| 2 | 00:15:21:20 | 00:17:20:25 | 1:59.17 | 00:00:13:25 | 00:02:13:00 |
| 3 | 00:17:22:15 | 00:17:56:28 | 0:34.43 | 00:02:13:00 | 00:02:47:13 |
| 4 | 00:18:00:07 | 00:19:10:01 | 1:09.80 | 00:02:47:13 | 00:03:57:07 |
| 5 | 00:19:15:28 | 00:23:28:06 | 4:12.27 | 00:03:57:07 | 00:08:09:15 |
| 6 | 00:23:30:02 | 00:35:59:08 | 12:29.20 | 00:08:09:15 | 00:20:38:21 |
| 7 | 00:36:03:20 | 00:36:08:29 | 0:05.30 | 00:20:38:21 | 00:20:44:00 |
| 8 | 00:36:09:22 | 00:37:28:12 | 1:18.67 | 00:20:44:00 | 00:22:02:20 |
| 9 | 00:37:39:02 | 00:38:42:21 | 1:03.63 | 00:22:02:20 | 00:23:06:09 |
| 10 | 00:38:44:12 | 00:39:25:11 | 0:40.97 | 00:23:06:09 | 00:23:47:08 |
| 11 | 00:39:26:04 | 00:41:49:12 | 2:23.27 | 00:23:47:08 | 00:26:10:16 |
| 12 | 00:42:10:28 | 00:47:05:26 | 4:54.93 | 00:26:10:16 | 00:31:05:14 |

## 7. Every overlay on the finished timeline (sequence TC at 30 fps)

Pictures: the file is in the USE folder (`...\EP 1 and 2\USE\`), shown full frame, contain-fit, never cropped, none used twice (28 placed, 28 different files, 1 spare not used). The render uses a simple alpha fade for every transition; the run sheet's named Premiere transition is in the last column if Zac finishes it in Premiere (the designed Modern transitions cannot be made in ffmpeg, I approximated them with a fade plus a small zoom-settle, NOT a copy of the Adobe effect).

| Stop | Picture | In | Out | Len | Run sheet transition in / out | Paired sound (level) |
|---|---|---|---|---|---|---|
| 2 | poster.png | 00:00:00:00 | 00:00:07:00 | 7.0 s | hard cut  / Cross Dissolve 24f | none |
| 3 | percy-closeup-camp-tee.png | 00:00:41:12 | 00:00:45:12 | 4.0 s | hard cut  / hard cut  | none |
| 4 | thalia-orange-hoodie-hill.png | 00:01:21:20 | 00:01:25:20 | 4.0 s | Film Dissolve 12f / hard cut  | none |
| 5 | annabeth-forest-portrait.png | 00:01:26:00 | 00:01:30:00 | 4.0 s | hard cut  / hard cut  | none |
| 6 | clarisse-camp-tee-s1.png | 00:03:30:29 | 00:03:34:29 | 4.0 s | hard cut  / hard cut  | none |
| 7 | percy-thalia-faceoff-camp.png | 00:03:52:26 | 00:03:55:26 | 3.0 s | hard cut  / hard cut  | none |
| 8 | annabeth-percy-winter-coats.png | 00:04:17:25 | 00:04:21:25 | 4.0 s | Burn Alpha Impacts 10f / hard cut  | Fire Flare Start Up Ignite 01.wav (-20 dB) |
| 11 | percy-nico-dance-floor.png | 00:06:18:14 | 00:06:23:14 | 5.0 s | hard cut  / hard cut  | none |
| 12 | luke-stone-hall-ep-unconfirmed.png | 00:07:02:11 | 00:07:07:11 | 5.0 s | Luma Fade Impacts 12f / hard cut  | Module Production Element Title Imaging Slow Swell Dramatic 01.wav (-22 dB) |
| 13 | chiron-tweed-jacket-s1.png | 00:07:43:00 | 00:07:47:00 | 4.0 s | Cross Dissolve 12f / hard cut  | none |
| 16 | thalia-aegis-shield-snow.png | 00:09:25:05 | 00:09:30:05 | 5.0 s | Flash Impacts 10f / hard cut  | Multimedia Internet CD-Rom Flash Beep Whoosh 02.wav (-20 dB) |
| 17 | artemis-huntresses-arrive-snow.png | 00:12:30:02 | 00:12:32:02 | 2.0 s | hard cut  / hard cut  | none |
| 18 | apollo-sun-car.png | 00:12:45:13 | 00:12:48:13 | 3.0 s | Light Leak Impacts 12f / hard cut  | Module Production Element Title Imaging Electronic Whoosh Calm 01.wav (-22 dB) |
| 19 | artemis-bow-portrait.png | 00:13:37:24 | 00:13:43:24 | 6.0 s | hard cut  / hard cut  | none |
| 20 | artemis-percy-snow.png | 00:14:20:20 | 00:14:25:20 | 5.0 s | Soft Wipe Impacts 12f / hard cut  | Module Production Element Title Imaging Electronic Whoosh Digital Reverse Delay 01.wav (-22 dB) |
| 21 | huntresses-bring-nico-bianca.png | 00:16:44:05 | 00:16:48:05 | 4.0 s | hard cut  / hard cut  | none |
| 22 | grover-camp-tee-forest.png | 00:20:38:01 | 00:20:41:01 | 3.0 s | Ray Impacts 12f / hard cut  | Module Production Element Title Imaging Electronic Whoosh Electrical 01.wav (-22 dB) |
| 23 | hermes-casino-hoodie-s1.png | 00:20:44:24 | 00:20:49:24 | 5.0 s | Zoom Blur Impacts 10f / hard cut  | Weapon Staff Whip Thin Fast 01.wav (-16 dB) |
| 24 | zeus-suit-s1.png | 00:20:58:15 | 00:21:01:15 | 3.0 s | hard cut  / hard cut  | none |
| 25 | hades-green-jacket-s1.png | 00:21:12:29 | 00:21:15:29 | 3.0 s | Blur Dissolve Impacts 14f / hard cut  | Module Production Element Title Imaging Empty Electronic Whoosh 01.wav (-24 dB) |
| 27 | poseidon-linen-shirt-s1.png | 00:23:47:26 | 00:23:50:26 | 3.0 s | hard cut  / hard cut  | none |
| 28 | ares-motorcycle-s1.png | 00:23:59:29 | 00:24:02:29 | 3.0 s | Directional Blur Impacts 10f / hard cut  | Transportation Auto Motorcycle Drive By Fast 01.wav (-18 dB) |
| 29 | mr-d-dionysus-hawaiian-shirt-s1.png | 00:24:32:05 | 00:24:37:05 | 5.0 s | Spring Motion Impacts 10f / hard cut  | Cartoon Spring Twang 10.wav (-14 dB) |
| 31 | grover-camp-tee-ep2.png | 00:26:14:08 | 00:26:18:08 | 4.0 s | hard cut  / hard cut  | none |
| 32 | nico-mythomagic-figures.png | 00:27:40:20 | 00:27:45:20 | 5.0 s | Flip Motion Impacts 10f / hard cut  | Multimedia Internet CD-Rom Flash Animation 12.wav (-18 dB) |
| 33 | bianca-nico-camp-doorway.png | 00:27:46:16 | 00:27:51:16 | 5.0 s | Mirror Impacts 12f / hard cut  | Module Production Element Title Imaging Electronic Whoosh Digital Resonant Cymbal Wash 01.wav (-24 dB) |
| 34 | luke-armor-sword-s1.png | 00:28:32:24 | 00:28:36:24 | 4.0 s | Film Dissolve 12f / hard cut  | none |
| 36 | dr-thorn-uniform-snow.png | 00:29:38:02 | 00:29:43:02 | 5.0 s | Luma Fade Impacts 12f / hard cut  | Module Production Element Title Imaging Ambient Smooth Tension 01.wav (-24 dB) |

Solo cams (hard cut in and out, the room two-shot audio runs through):

| Stop | Cam | In | Out | Len | Cam file time at the cut |
|---|---|---|---|---|---|
| 9 | Winter Wolf | 00:04:40:09 | 00:05:16:09 | 36.0 s | 00:19:58:09 |
| 26 | KingZ (second file) | 00:21:24:08 | 00:21:49:08 | 25.0 s | 00:23:16:27 |
| 35 | Winter Wolf | 00:28:40:18 | 00:29:03:18 | 23.0 s | 00:44:40:09 |
| 37 | Winter Wolf | 00:30:42:18 | 00:31:05:14 | 22.9 s | 00:46:42:09 |

Stop 30 (KingZ cam on the special forces daughters claim) was SKIPPED because that claim is cut (C6), as the run sheet says to do.

- USE VIDEO, stop 10: `PJ3-C01 Sneak-Peek ... 7.00s MUTED.mp4` on V4, 00:06:07:22 to 00:06:14:22 (210 frames, 24 fps conformed to 30, no audio, Disney+ corner marks are on the frames, wwd-rights flag in the Rights Note).
- SPOILER ALERT, stop 14 (marker on the run sheet): STAND-IN placed at 00:08:06:29 for 3.2 s = `P:\WWD Kit\Vision Quest\Spoiler Alert.mov` (the red SPOILER WARNING banner from the kit, with its own sound). Zac's own Spoiler Alert clip was not on disk; swap it in (same spot, on 'three, two, one go').
- Rimshot on 'Nobody died', stop 15: 00:08:10:17, `Rimshot03.wav` at -6 dB, on the word 'died'. The main-mix transcript missed this line, so I timed 'died' (raw 23:31.13) from the Winter Wolf cam audio (whisperx on the cam: "It's Disney+. Nobody died." at 23:30.25 to 23:31.5). Not heard.
- LIKE AND SUBSCRIBE, stop 38: STAND-IN at 00:30:56:17 for 8.0 s = the alpha Subscribe Button + Notification Bell (`L:\Winter Wolfs Den review show\VFX\Subscribe Button + Notification Bell (Alpha Channel)\...CT.mov`), over the sign-off cam. Zac's own Like and Subscribe clip path was never on file (run sheet Open 25). Swap it in at 'Let us know in the comments below'.
- NEXT UP card (generic, stop 39): `P:\WWD Kit\Cards\Next Up - Next Review (MP4).mp4`, 6.0 s, at 00:31:05:14. END CARD (stop 40): `P:\WWD Kit\Cards\End Card - Percy Jackson S3 (MP4).mp4`, 12.0 s, at 00:31:11:14. Both cards' own audio is muted so the new outro music is the only music (the cards' sound measured about -26 LUFS and was not heard).
- No intro VIDEO is used. The kit has `P:\WWD Kit\Percy Jackson Intro\Intro - Percy Jackson Trident Tide (MP4).mp4`, which is NOT in the run sheet and was not ordered, so I did not place it. Zac's order was a music sting over the opening words.

## 8. Gaps and flags

- No web browsing was done (order). The run sheet's browser-pull items (Atlas, the Oracle, the sea cow, Season 3 stills of Chiron, Clarisse and Mr. D, Tantalus, Tyson, the Titan's Curse book cover, the two earlier film posters) do NOT exist on disk. I placed nothing for them and used no stand-in picture from another show. Those lines stay on the hosts' faces (two-shot or a host cam). The run sheet's own list of those stretches is in its 'Gaps and flags' section.
- The two-shot carries 19 stretches over 25 s with no picture, cam or clip, 1513 s in all of 1865 s. Longest: 16:48.05 to 20:38.01 (230 s), 9:30.05 to 12:30.02 (180 s), 14:25.20 to 16:44.05 (138 s), 1:30.00 to 3:30.29 (121 s).
- Shots I could have cut to a solo cam to cover the longest bare stretches (a creative call, so NOT done, the rule is a few cams): run sheet 'Gaps' table PROPOSEDs, KingZ 15:19 to 15:43 (Oracle scene) and 18:56 to 19:17, Winter Wolf 23:57 to 24:17 and 27:47 to 28:04 (run sheet clock).
- Spare picture not used: `annabeth-percy-winter-dance.png` (the clip owns that line, Still open 16).
- Stand-ins used and clearly named: Spoiler Alert (Vision Quest kit banner), Like and Subscribe (alpha Subscribe button and bell), because Zac's own two clips were not on disk (Open 25). Swap them at the same frames.
- Picture 22 (Grover) is held 3.0 s but the line it sits on now ends 0.4 s after it starts because the 'child of Pan' sentence was cut (C3), so the picture runs over the start of Winter Wolf's next line ('Or I think, sadly, it's going to be Thalia'). Shorten it to 1.5 s if that bothers you.
- Pictures with a known weak fit stay as the run sheet has them (28 Luke in armor, 10 Luke in a stone space, 26 toy figures on the Magic The Gathering line). Drop first if you want fewer.
- Rights flags unchanged from the Rights Note (`WWD\reports\Percy-Jackson-S3-E1-2-Rights-Note.md`): Disney+ corner marks on the clip, Disney press-kit stills, nine Season 1 press stills used on Season 3 lines, Adobe MUSIC-tree files not used here. No clearance pass was run on this render.

## 9. Picture-count and rule check against the run sheet (PROVEN by script on plan.json)

- Pictures placed: 28 of the run sheet's 28 picture stops, 28 different files (no picture twice: PASS).
- Longest picture on screen: 7.00 s (limit 7 s: PASS).
- Pictures, cams and the clip never overlap each other: PASS.
- Solo cams used: 4 (rule: a few). Clips: 1, muted, 7.00 s (rule 6 to 8 s, up to 12).
- Spoiler warning kept: yes ('I'm about to drop a spoiler warning' through 'And well, you have been warned' are in the cut, with the stand-in banner). Like and Subscribe clip: placed. No cut touches either.
- Poster on the intro line for 7.0 s (stop 2), the run sheet's longest picture.
- Run sheet items NOT done: none of the 40 stops was skipped except stop 30 (conditional, cut with its claim) and stop 1 which became the music sting.

## 10. What I verified and what I did not

- PROVEN by tool on the finished file (ffprobe, ffmpeg ebur128, blackdetect, freezedetect, silencedetect): 1920x1080, 30 fps, H.264 High, yuv420p, 56,504 frames, AAC LC 48 kHz stereo, duration 1883.467 s (31:23.47), size 1.98 GB, integrated loudness -14.0 LUFS (loudness range 5.9 LU), true peak -1.3 dBTP (target -14 LUFS and -1 dBTP, Zac's lock), no black frames of 0.3 s or more, no frozen picture of 8 s or more, no silence of 1.5 s or more.
- PROVEN by script: the picture track length equals plan (55,964 conversation frames + 180 Next Up + 360 End card = 56,504), 28 pictures all different files, longest picture 7.00 s, no overlap between pictures, cams and the clip, every piece was rendered with an exact frame count.
- VIEWED by me as stills: a contact sheet every 30 s (65 frames, whole video including both cards) and a sheet of 37 frames at every picture, cam, the clip, both stand-in banners and two transition starts. They show pictures fitted full frame with the hosts' frame visible around the see-through edges (nothing cropped), the poster on the opening, solo cams for Winter Wolf and KingZ, the dark Disney+ clip frame with the corner marks, the red SPOILER WARNING stand-in, the Subscribe stand-in over the closing cam, the Next Up card and the End card. Sheets: contact_sheet_every30s.png and contact_sheet_overlays.png in the export folder.
- NOT HEARD, NOT PLAYED: I cannot listen. Unverified by ear: voice-to-music balance in the first 6 s, the intro and outro music themselves, every sound effect and its level, the rimshot placement, the join points of all 12 segments (set at silences by measurement, 6 ms dip, not heard), room tone at the joins, lip sync of the cams (matched by waveform correlation only), and whether any joined sentence still sounds natural.
- NOT VERIFIED: that the transcript-matched raw timing equals what the run sheet intended at every stop (every picture start was snapped to its search phrase in the raw recording, 28 of 28 found after a few phrase fixes for raw wording, but the exact word was not checked by eye); the music license; the intro and outro are not confirmed instrumental (a speech detector found no speech, nothing more); no clearance or rights pass was run on this render; no qa-director pass yet at the time of writing (see the report back).
- NOT DONE ON PURPOSE: no web browsing, no downloads, no credits, no posting, nothing sent, no Adobe setting touched, no source file changed (all work in D:\WKP\scratch\pj-edit and the new export folder).
- QA: qa-director (qa-media) PASS WITH NOTES 2026-11-25 on the finished file: specs, 56,504 frames, -14.0 LUFS, -1.3 dBTP, no black, no silence over 1.5 s, all 28 pictures viewed mid-hold and correct and uncropped, 4 cams and the clip on screen, tail is the outro music by level. Notes: generic Next Up card, stand-ins and music licence still open, nothing heard. A 2 s freezedetect hit at 27:49 is the held Bianca and Nico picture, not a stall.
