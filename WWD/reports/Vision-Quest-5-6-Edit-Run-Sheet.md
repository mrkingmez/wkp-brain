# Vision Quest (Disney+ series, episodes 5 and 6) - Edit Run Sheet v2

`LOGO_SECONDS = 5.0`  (confirmed by Zac 2026-10-31, the logo is 5.0 s)

**Built 2026-10-31 from the Premiere edit transcript (31:05, two speakers: Winter Wolf and KingZ).** Folder: `L:\Winter Wolfs Den review show\Raw Footage\mass recording clayface and vision ep 3&4\Vision Quest ep 5 and 6\`. The USE folder holds 15 pictures, 12 are placed. Also placed: 2 promo clips, 3 solo cams, 3 stickers and tags, 2 sound-only cues, the logo slot and the Next Up Vision Quest 7 card. The series opener is already in Zac's cut and is not on this sheet. Owned sounds only, music at the intro and outro only, no bleeping.

**Two time columns on every stop.** The first time is the transcript time (what the Premiere transcript shows). The "with logo" time is the same spot after the logo slot is inserted (transcript time plus `LOGO_SECONDS`, for everything after 00:18). The logo slot (stop 1) is the push, nothing is placed before it.

**Why 24 stops:** the verified-picture rule limits the count (15 pictures, 12 placed). Lines with no verified picture are spoken only, listed under Gaps. Where a host has a good point the cams and tags carry it.

**Picture rule (LOCKED 2026-10-19):** no picture on screen longer than 7 seconds (every one here is 6), no picture twice. The CAM stops are the solo shots, only where one host has the floor.

**The transcript gives block times, not word times.** Every time below is my best estimate inside the block. Search words are checked to appear once in the transcript. Trust the words, not the clock.

## Trailer clips and fair use

**Two short promo clips are placed (stops 12 and 15). Total about 2.4 seconds in a 31 minute video.**

**Fair use rules, keep every one:**
1. **Commentary only.** A clip plays only while a host is talking about that exact scene.
2. **Short.** No clip over 4 seconds. Total promo footage under 30 seconds. Never two clips back to back (these two are about six minutes apart).
3. **Muted.** Both files below are the MUTED copies, no audio stream (checked with ffprobe).
4. **No title cards, release date or studio logo.** Both promos have "TONIGHT", "TWO NEW EPISODES" and the Disney+ and VISIONQUEST end cards, none are used. Clip A's used frames have no text. Clip B has the Disney+ bug and burned-in captions on every frame, cropped out (stop 16). Flagged for wwd-rights.
5. **No picture twice.** Picture 15 (Ultron at a glowing doorway) is also in promo A's first seconds, but that part of the promo is not used.
6. **The upload package keeps its fair use disclaimer as the last section.** Risk flag, not legal advice.

**Clip files (H.264, 30 fps, vertical 1080x1920, both import into Premiere):**
- A: `L:\Winter Wolfs Den review show\Raw Footage\mass recording clayface and vision ep 3&4\Vision Quest ep 5 and 6\Video Clips\Promo - There's No Hope For You (muted H264).mp4`
- B: `L:\Winter Wolfs Den review show\Raw Footage\mass recording clayface and vision ep 3&4\Vision Quest ep 5 and 6\Video Clips\Promo - Devil on His Shoulder (muted H264).mp4`

I pulled frames every 0.25 s over the first 8 s of each, every 0.5 s to the end, then every 0.1 s and frame by frame at each edge I used. Timecodes below are at the file's own 30 fps.

## Before you start (one time, about 5 minutes)

1. **Shortcuts used below:**
   - `USE\` = `L:\Winter Wolfs Den review show\Raw Footage\mass recording clayface and vision ep 3&4\Vision Quest ep 5 and 6\USE\`
   - Kit = `P:\WWD Kit\Vision Quest\` (AI Tag - JARVIS.mov, AI Tag - DUM-E.mov)
   - Cards = `P:\WWD Kit\Cards\` (Next Up - Vision Quest 7 (MP4).mp4)
   - Stickers = `P:\WWD Kit\Stickers\` (Recommend Watch.mov)
2. **Import:** drag the `USE` folder into the Project panel. Then **Ctrl+I**, pick the kit files, the card, the sticker and both promo clips, **Import**. Import sounds one at a time as you reach them. Use the MP4 card, the .mov versions freeze on this machine.
3. **Tracks:** V1 host cams (the two-shot), V2 pictures, V3 and V4 clips, tags and stickers. A1 voices, A3 and A4 sound effects. No music except your intro and outro.
4. **How to find each spot:** **Window > Text > Transcript**, type the search words from the stop into the search box, click the highlighted word. The playhead jumps there. Do the logo insert (stop 1) first, then everything below follows the "with logo" times.
5. **How to set a transition length:** drag the transition from the Effects panel onto the cut, right-click it, **Set Transition Duration**, type the frames (12f = `00:00:00:12`). Designed transitions are in **Effects > Video Transitions > Modern Transitions**, click path in each stop. If the folder names differ on your build, type the name (example: `Mirror Impacts`) in the Effects panel search box. Classic ones (Cross Dissolve, Film Dissolve) are in **Effects > Video Transitions > Dissolve**.
6. **How to set a sound level:** click the clip, Effect Controls, **Volume > Level**, type the number. Put each transition's paired sound on A3 starting on the first frame of the transition.
7. **Solo shots (CAM):** KingZ webcam `Untitled_recording-King-Z-webcam-00h_00m_00s_494ms-StreamYard.mp4`, Winter Wolf webcam `Untitled_recording-Winter_Wolf-webcam-00h_00m_00s_892ms-StreamYard.mp4`, both in the show folder. "Matt / Winter Wolf" in the transcript is Winter Wolf, "Zac / King-Z" is KingZ. **Zac has already synced both cams to the main recording**, so each CAM stop gives in and out on the main-recording timeline and the same times work on the cam file. No waveform work.
8. **Pictures:** each placement says the picture and where it ends. Drop it on V2 at the search spot, drag its right edge to the end time. The PNGs have see-through edges, so your cams show around them.
9. **Transition rules for this sheet:** designed Modern transitions on half the placements, each with a paired owned sound. Calm and sad beats stay plain (stops 3, 6, 14, 16). Never the same transition twice in a row. Cross Dissolve on 2 stops only.
10. **Check this first:** the garbles to check are in the Garbles section near the end. Nothing in the hook needs a fix.

---

### 1. 00:18 (slot runs 00:18 to 00:23)  |  LOGO SLOT  |  search: "back in the chairs"
Said: "...All right, dude, we're back in the chairs for Vision Quest five and six." (Winter Wolf)
**Zac inserts the logo here, right after the hook (the hook stays the first 18 seconds).** The opener is already in Zac's cut and is not part of this sheet. Slot length is `LOGO_SECONDS = 5.0` (top of this sheet). Park the playhead on the frame right after "chairs" (the transcript block ends 00:18:22), turn Sync Lock on for every track, select the logo in the Project panel and press the **comma** key (Insert) with V1 and A1 targeted. Insert pushes everything after it later by the logo length. The first time on every stop below is the transcript time, the "with logo" time is where it lands after the insert.
Notes: if the logo ever changes length, change `LOGO_SECONDS` and every "with logo" time moves by the difference. Tell me and I reissue the sheet.

### 2. 00:22 (with logo 00:27)  |  PNG 1 (Vision close-up, glowing gem, Ep 5 Firewall)  |  search: "episode six is deadlock"
Said: "There are two episodes for you guys tonight. Episode five, firewall. And I think episode six is deadlock." (Winter Wolf)
Picture `USE\1.png` to 00:28 (with logo 00:33). In: **Light Leak Impacts 12f** (`Effects panel > Video Transitions > Modern Transitions > Lights & Blurs > Light Leak Impacts`), a bright wash out of the logo slot. Out: hard cut.
Sound: `P:\Sounds\Sound FX\audioblocks-fast-start-whoosh_BKITlG8RwU.mp3` on the first frame, -18 dB.
Notes: Tag OK: Paul Bettany as Vision, Ep 5 "Firewall" still. The line names episode five, this is the episode five still.

### 3. 00:50 (with logo 00:55)  |  PNG 5 (Ultron, black and white, long white beard)  |  search: "pivotal conversations"
Said: "There's three kind of pivotal conversations that go on between Tommy Shepherd and Ultron, vision and all, Tron and then and Ultron." (Winter Wolf)
Picture `USE\5.png` to 00:56 (with logo 01:01). In: Film Dissolve 12f (`Effects panel > Video Transitions > Dissolve > Film Dissolve`). Out: hard cut.
Notes: Tag OK: James Spader as Ultron (human form). The line is about the Ultron conversations, so Ultron is on screen. Plain on purpose, a calm set-up beat. Garble in this line: "all, Tron" means Ultron (see Garbles).

### 4. 01:38 (with logo 01:43)  |  PNG 13 (Ultron and Jocasta, robot heads face to face)  |  search: "build their scenes together"
Said: "Seeing how she is working with Ultron and watching them to build their scenes together. It's like watching a painting that moves." (KingZ)
Picture `USE\13.png` to 01:44 (with logo 01:49). In: **Mirror Impacts 12f** (`Effects panel > Video Transitions > Modern Transitions > Transformers > Mirror Impacts`), two faces, two sides. Out: hard cut.
Sound: `P:\Sounds\Sound FX\deep-fast-whoosh_GyZDnHNu.mp3` on the first frame, -20 dB.
Notes: Tag OK: James Spader (Ultron) and T'Nia Miller (Jocasta), robot heads face to face. Fits "working with Ultron". Garble 16 seconds earlier: "Jakarta" means Jocasta (see Garbles), it sits before this stop.

### 5. 02:44 (with logo 02:49)  |  CAM: single out KingZ  |  search: "good thing about Wonder Man"
Said: "And one of the things that was told to me today, she's like, well, the good thing about Wonder Man getting canceled and this not getting the second season is they can't mess it up. They have one season. It is great. We like it and there's no second season to ruin it." (KingZ)
Cut to KingZ's solo camera at "good thing about Wonder Man". **CAM IN 02:44 (02:49 with logo), CAM OUT 03:01 (03:06 with logo), length 17 s**, out on the end of "ruin it". Synced cam, main-recording time. Hard cut in, hard cut back to the two-shot. Cam file (KingZ): `L:\Winter Wolfs Den review show\Raw Footage\mass recording clayface and vision ep 3&4\Vision Quest ep 5 and 6\Untitled_recording-King-Z-webcam-00h_00m_00s_494ms-StreamYard.mp4`.
Notes: His joke and his point, he has the floor for the whole block. The cams are already synced by Zac.

### 6. 03:11 (with logo 03:16)  |  PNG 4 (T'Nia Miller as Jocasta, hood, glowing red eyes)  |  search: "Taniya miller"
Said: "I'm kind of with you on this. I think that, it's Taniya miller that plays it. James Spader is..." (Winter Wolf)
Picture `USE\4.png` to 03:17 (with logo 03:22). In: Cross Dissolve 12f (`Effects panel > Video Transitions > Dissolve > Cross Dissolve`). Out: hard cut.
Notes: Tag OK: T'Nia Miller as Jocasta (source caption). The picture shows the actress he is talking about. Plain, a praise beat. Garble: "Taniya miller" means T'Nia Miller (see Garbles).

### 7. 04:25 (with logo 04:30)  |  PNG 15 (Ultron at a glowing doorway, top hat, back to camera)  |  search: "you'll always be alone"
Said: "Thomas getting the upper hand on him at the end, like you'll always be alone. And like that is what's actually haunting him, is that there is no one else like him." (KingZ)
Picture `USE\15.png` to 04:31 (with logo 04:36). In: **Luma Fade Impacts 12f** (`Effects panel > Video Transitions > Modern Transitions > Essentials > Luma Fade Impacts`), a dark fade for a haunting line. Out: hard cut.
Sound: `P:\Sounds\Sound FX\Adobe\Drones\Drone Production Element Imaging Digital Feedback Loop 01.wav` on the first frame, -26 dB. First 2 seconds only, fade out.
Notes: Tag OK by caption only: IMDb names James Spader (Ultron), the face is not visible. The line is about what haunts Ultron, so the lonely figure at the door fits. Quiet sound on purpose. Garbles: "Thomas" means Tommy, "spade" in the block before means Spader.

### 8. 05:45 (with logo 05:50)  |  SOUND ONLY  |  search: "taken the liberty"
Said: "I've already taken the liberty of calling you a ride." (KingZ, quoting the show)
Sound: `P:\Sounds\Sound FX\Adobe\Transportation\Transportation Auto Avalanche Honk Horn Short 01.wav` on "calling you a ride", -20 dB. A small gag cue on a line that is a joke. No picture, none verified.
Notes: Light tone, no violence on this line. Skip it if it steps on his delivery, I cannot hear the timing.

### 9. 06:22 (with logo 06:27)  |  PNG 6 (Ultron and Jocasta in robot form at a bar)  |  search: "order a drink"
Said: "They realize that in the two seconds it took James Spader as Ultra at the bar to order a drink, the whole conversation played out in that split second." (Winter Wolf)
Picture `USE\6.png` to 06:28 (with logo 06:33). In: **Chroma Leak Impacts 12f** (`Effects panel > Video Transitions > Modern Transitions > Lights & Blurs > Chroma Leak Impacts`), neon bar light. Out: hard cut.
Sound: `P:\Sounds\Sound FX\Adobe\Science Fiction\Science Fiction Sci-Fi Electronic  Energy Swell Fluttering 07.wav` on the first frame, -22 dB.
Notes: Tag OK: James Spader (Ultron) and T'Nia Miller (Jocasta) at a bar, from the IMDb Ep 5 gallery. IMDb files some stills under more than one episode, so the tag proves the bar, not that it is this exact scene (see Gaps). Garble: "Ultra" means Ultron.

### 10. 07:02 (with logo 07:07)  |  PNG 12 (Todd Stashwick as the Paladin)  |  search: "I love this guy"
Said: "Let me just say on the Paladin, I love this guy. This guy should play that role until the day he dies, because he's hilarious in every scene he's in." (Winter Wolf)
Picture `USE\12.png` to 07:08 (with logo 07:13). In: **Zoom Blur Impacts 8f** (`Effects panel > Video Transitions > Modern Transitions > Lights & Blurs > Zoom Blur Impacts`), a punch-in on the name. Out: hard cut.
Sound: `P:\Sounds\Sound FX\audioblocks-frost-low-whoosh_BWSg1QdQKvL.mp3` on the first frame, -20 dB.
Notes: Tag OK: Todd Stashwick (Paladin), source caption.

### 11. 07:39 (with logo 07:44)  |  PNG 7 (Vision close-up, blue eyes, gem lit)  |  search: "not your father"
Said: "This is not your father's vision, dude. No dude is mean and I like it." (Winter Wolf)
Picture `USE\7.png` to 07:45 (with logo 07:50). In: **Radial Blur Impacts 10f** (`Effects panel > Video Transitions > Modern Transitions > Lights & Blurs > Radial Blur Impacts`), Vision powering up. Out: hard cut.
Sound: `P:\Sounds\Sound FX\Adobe\Multimedia\Multimedia Internet CD-Rom Flash Beep Whoosh 01.wav` on the first frame, -20 dB.
Notes: Tag OK: Paul Bettany as Vision, close-up. Not a twin of picture 1 (hash check run over the whole folder, zero pairs flagged).

### 12. 09:28 (with logo 09:33)  |  USE VIDEO (promo clip A)  |  search: "chains him to a chair"
Said: "I love the part where she thinks that he's smooth talking her... and she chains him to a chair because it's her mind. She's the queen. It's her board, it's her pieces." (Winter Wolf)
**USE VIDEO:** `L:\Winter Wolfs Den review show\Raw Footage\mass recording clayface and vision ep 3&4\Vision Quest ep 5 and 6\Video Clips\Promo - There's No Hope For You (muted H264).mp4` from `00:00:14:13` to `00:00:15:06` (0.8 s). Starts on "chains him to a chair". Muted (file has no audio stream). In: hard cut. Out: hard cut.
What is in it: two shots, frame-checked. Shot 1 (14:13 to 14:22) a white pillar, a boot and glowing chains. Shot 2 (14:23 to 15:05) the bearded Ultron figure, low angle, chained at the wrist.
How to set it: the file is VERTICAL 1080x1920, 30 fps. Double-click it, type `00:00:14:13` in the Source Monitor timecode box, press **I**, type `00:00:15:06`, press **O**, drag to **V3**. Then Effect Controls > Motion > Scale **56.25**, so the whole tall frame fits the 1080 high screen with empty sides (your cams or black show there, no stretch).
Notes: Shot edges pulled at 30 fps: the window shot before it ends on frame 432 and the pillar shot starts on frame 433 (that is 14:13), the pillar shot ends on frame 442 and Ultron starts on frame 443 (14:23). Frames 443 to 457 are all Ultron, the dip to black comes later, so the out point (frame 456) is clean. No title card, no text and no Disney+ bug in the used frames. The ID comes from the hosts' words (chains him to a chair) plus the visible chains, the promo has no caption. Under one second is short on purpose.

### 13. 13:11 (with logo 13:16)  |  PNG 8 (Vision, F.R.I.D.A.Y. and E.D.I.T.H. in the TV room)  |  search: "firewall came down Friday"
Said: "When the firewall came down Friday, it was like, you can't do this. It's like if Ultron's out there, that's the same problem we had 15 years ago." (Winter Wolf)
Picture `USE\8.png` to 13:17 (with logo 13:22). In: **Phosphor Impacts 10f** (`Effects panel > Video Transitions > Modern Transitions > Lights & Blurs > Phosphor Impacts`), a screen glow for the AIs. Out: hard cut.
Sound: `P:\Sounds\Sound FX\Adobe\Science Fiction\Science Fiction Sci-Fi Electronic Blip274.wav` on the first frame, -20 dB.
Notes: Tag OK: Paul Bettany (Vision), Orla Brady (F.R.I.D.A.Y.), Emily Hampshire (E.D.I.T.H.). Friday is named in the line and is on screen. Garbles in the next sentence: "Thomas" and "division's credit" (Vision).

### 14. 13:59 (with logo 14:04)  |  PNG 10 (E.D.I.T.H. in the yellow armchair)  |  search: "departure well"
Said: "Edith is not taking her departure well at all. No, but luckily that gets pseudo resolved in episode six, which is kind of nifty." (Winter Wolf)
Picture `USE\10.png` to 14:05 (with logo 14:10). In: Film Dissolve 12f (`Effects panel > Video Transitions > Dissolve > Film Dissolve`). Out: hard cut.
Notes: Tag OK: Emily Hampshire (E.D.I.T.H.), source caption. Plain on purpose, Edith is hurting, no sound.

### 15. 15:42 (with logo 15:47)  |  USE VIDEO (promo clip B)  |  search: "devil on your shoulder"
Said: "You know, you always have that little, as they used to say, the devil on your shoulder. That's what Ultron was. He's the one whispering." (KingZ)
**USE VIDEO:** `L:\Winter Wolfs Den review show\Raw Footage\mass recording clayface and vision ep 3&4\Vision Quest ep 5 and 6\Video Clips\Promo - Devil on His Shoulder (muted H264).mp4` from `00:00:03:02` to `00:00:04:20` (1.6 s). Starts on "devil on your shoulder". Muted (file has no audio stream). In: hard cut. Out: hard cut.
What is in it: a top-hat silhouette in the back seat of the van, dark red, then black and white, then a red glitch with glowing glasses. Frame 140 (`00:00:04:20`) is Vision's face, the out point stops one frame before it.
**This clip has a Disney+ bug and burned-in captions on every frame. Crop it, do not use it as is.** The file is VERTICAL 1080x1920. Effect Controls > Motion > Scale **177.8**, Position **960, 1138**. That shows the band from 320 to 927 pixels down the tall frame, which sits between the bug (top right, about 200 to 300 px down) and the captions (about 1330 px down). I rendered that exact crop on frames 88 to 93, 109 to 114 and 136 to 142 and checked by eye that neither shows. Scrub it once in Premiere to confirm, I cannot open Premiere. The upscale is about 1.8x on a 1.6 s clip.
Notes: The scene ID is by the hosts' words (Ultron whispering in Vision's head) and the promo's own caption text ("the devil on his shoulder", cropped out of frame). No face is shown, only silhouettes. Flag for wwd-rights: Disney+ bug on every source frame, cropped out. Frame 110 is a hard cut inside the clip (red hat to black and white), that is the promo's own edit.

### 16. 17:15 (with logo 17:20)  |  PNG 3 (Vision, E.D.I.T.H., U and DUM-E in the TV room)  |  search: "other than a dummy"
Said: "Edith figuring out who she is without Friday and being the only AI other than a dummy and U in the head." (KingZ)
Picture `USE\3.png` to 17:21 (with logo 17:26). In: Cross Dissolve 12f (`Effects panel > Video Transitions > Dissolve > Cross Dissolve`). Out: hard cut.
Notes: Tag OK: Paul Bettany (Vision), Emily Hampshire (E.D.I.T.H.), Jonathan Sayer (U), Henry Lewis (DUM-E). Edith, DUM-E and U are all named in the line and all on screen. Plain on purpose, a thoughtful beat. Not a twin of picture 8 (different shot, hash check clean).

### 17. 17:56 (with logo 18:01)  |  PNG 11 (Lisa and Tommy, foreheads together)  |  search: "get to Lisa"
Said: "Let's get to Lisa real quick here. Her when she gets the nanobots in the..." (KingZ)
Picture `USE\11.png` to 18:02 (with logo 18:07). In: hard cut. Out: hard cut.
Notes: Tag OK: Lauren Morais (Lisa) and Ruaridh Mollica (Tommy), IMDb Ep 6 gallery. Lisa is named and on screen. This is a quiet moment between them, not the nanobot scene, so the picture is only about Lisa. Hard cut on purpose, the next stop is the creepy beat.

### 18. 18:04 (with logo 18:09)  |  SOUND ONLY  |  search: "creepiest thing"
Said: "I wasn't her getting back up. The creepiest thing we've seen this month, including every scary movie that's coming out in theaters." (KingZ)
Sound: `P:\Sounds\Sound FX\Adobe\Drones\Drone Production Element Imaging Pounding Deep Low Tremor 01.wav` at -20 dB, starting on "creepiest thing", fade out under Winter Wolf's reply ("Dude, it might be"). A low tension swell on his own line, not a bed. No picture, none verified for the nanobot scene.
Notes: Horror tone matches what the hosts say, nothing comic.

> **PLACEHOLDER, transcript 20:53 (with logo 20:58), search: "send you the clip".** Winter Wolf says "I'll send you the clip. We can put it here." The van gunman clip has not been received. No clip placed, no stop number used. Leave the two-shot running here until it arrives.

### 19. 21:35 (with logo 21:40)  |  STICKER  |  AI TAG JARVIS  |  search: "built Jarvis"
Said: "I liked the last 20 years of the MCU, thinking Tony Stark put all this together, like his ingenuity built Jarvis, built the A's, built the suits..." (Winter Wolf)
Drop `P:\WWD Kit\Vision Quest\AI Tag - JARVIS.mov` on the top video track, lower left, starting on "Jarvis". Runs 3.6 seconds, 1920x1080, the beep is built in.
Notes: The hosts name Jarvis here, so the tag is honest. No Jarvis picture exists in the set, so the tag stands alone. This whole 21:25 to 23:29 stretch is the long canon talk with no verified pictures, the cams and tags carry it.

### 20. 22:00 (with logo 22:05)  |  CAM: single out Winter Wolf  |  search: "don't need to underwrite"
Said: "Doctor Who's done that? Like we don't need to underwrite the cool shit we already had that. It did kind of annoy me that they wrote that in. That's just a me thing." (Winter Wolf)
Cut to Winter Wolf's solo camera at "Like we don't need to underwrite". **CAM IN 22:00 (22:05 with logo), CAM OUT 22:13 (22:18 with logo), length 13 s.** Synced cam, main-recording time. Hard cut in, hard cut back to the two-shot. Cam file (Winter Wolf): `L:\Winter Wolfs Den review show\Raw Footage\mass recording clayface and vision ep 3&4\Vision Quest ep 5 and 6\Untitled_recording-Winter_Wolf-webcam-00h_00m_00s_892ms-StreamYard.mp4`.
Notes: His point of the nitpick segment, he has the floor. Cam already synced by Zac.

### 21. 22:56 (with logo 23:01)  |  STICKER  |  AI TAG DUM-E  |  search: "wrote the AI for dummy"
Said: "Well, I know he wrote the AI for dummy and U because that was his college project, right?" (KingZ)
Drop `P:\WWD Kit\Vision Quest\AI Tag - DUM-E.mov` on the top video track, lower left, starting on "dummy". Runs 3.6 seconds, beep built in.
Notes: Honest tag, he names DUM-E. Picture 3 already showed DUM-E at stop 16, so no picture here.

### 22. 24:07 (with logo 24:12)  |  CAM: single out KingZ  |  search: "changes canon all that much"
Said: "He could have took that base and then improved it... I don't think it changes canon all that much." (KingZ)
Cut to KingZ's solo camera at "I don't think it changes canon all that much". **CAM IN 24:07 (24:12 with logo), CAM OUT 24:20 (24:25 with logo), length 13 s.** Synced cam, main-recording time. Hard cut in, hard cut back to the two-shot. Cam file (KingZ): `L:\Winter Wolfs Den review show\Raw Footage\mass recording clayface and vision ep 3&4\Vision Quest ep 5 and 6\Untitled_recording-King-Z-webcam-00h_00m_00s_494ms-StreamYard.mp4`.
Notes: His counter to the stop 20 point, the payoff of the debate. Third and last solo cam.

### 23. 25:31 (with logo 25:36)  |  STICKER  |  RECOMMEND WATCH  |  search: "gives it a big recommend"
Said: "Still recommend. How about you?" (KingZ) "Wolf gives it a big recommend because again, I think there's a lot to take away from the pacing..." (Winter Wolf)
Drop `P:\WWD Kit\Stickers\Recommend Watch.mov` on the top video track so it starts on "gives it a big recommend". 4.0 seconds, thud built in.
Notes: Placed because both hosts say recommend out loud. A sticker, not a score or a verdict card.

### 24. 27:54 (with logo 27:59)  |  END CARD  |  Next Up Vision Quest 7  |  search: "Wednesday at nine"
Said: "...we'll see you guys next time for Wednesday at nine. See you guys!" (Winter Wolf)
Drop `P:\WWD Kit\Cards\Next Up - Vision Quest 7 (MP4).mp4` on the top video track **right after "See you guys!"** (the goodbye block ends 27:54). 6.0 seconds, 1920x1080, 30 fps. The card says only Vision Quest episode 7. **Use the MP4, the ProRes version freezes on Zac's machine.** Put your outro music under it if you use any.
Notes: **The tail is Zac's.** The transcript runs on to 31:05 after the goodbye, Zac cuts that himself and cuts in the spoiler warning himself (shot later), so nothing from 27:54 on is on this sheet. The card has no score or verdict. Schedule is now episode 7 next week, episode 8 the week after, so the goodbye line "episode seven ... next week" is correct.

---

## Gaps and flags

- **Beat gaps that need more pictures** (spoken only today, nothing verified in the 15). Tell me and I add stops once tagged pictures are in `USE\`:
  - Tommy on his own (Ruaridh Mollica), the Tommy and Ultron talk and the "squash match" (04:16 to 05:49, 13:09 to 13:30). Only picture 11 has him, and it is Lisa's moment.
  - The Madripoor alleyway shootout and the adamantium bullets (08:10 to 09:03).
  - Vision at the exchange with the Paladin, the coin and body-language scene (07:19 to 07:42, 16:07 to 16:45). Only one Paladin picture exists, used at 07:02.
  - Ultron and Jocasta's mind meld and the memories (11:43 to 12:17), and Ultron in the attic or elevator with Vision (11:09).
  - Lisa getting up with the nanobots (18:08), the Sam Raimi comparison and the first Ultron suit in Avengers Tower (18:39 to 19:11, archive stills).
  - The gunman and the Paladin's van (20:13 to 21:05). **Winter Wolf says "I'll send you the clip. We can put it here" at 20:53.** There is no such clip in the folder, ask Zac if Matt sent it.
  - The Stark, Jarvis and prototype AI canon talk, Iron Man 3 and AIM (21:25 to 24:20), a long stretch, two tags and two cams carry it.
  - The client reveal, Raza and the Ten Rings (25:54 to 26:39, archive stills from the first Iron Man).
  - Wonder Man and Ben Kingsley (02:44 to 03:01, 03:50).
- **Unused pictures:** 2 (man in vest and tie, person not named, scene only), 9 (T'Nia Miller close-up, a near twin of picture 4 and the rule is no near-twins), 14 (the two bots in white, no line in the transcript is about them). 12 of 15 pictures used.
- **IMDb heads-up from the tags file:** IMDb files some stills under more than one episode, so a gallery tag is not proof of which episode a still is from. Pictures 5, 6, 8 and 15 are used on general character lines. Picture 6 sits on the one scene-specific line (the bar), flagged at stop 9.
- **Disney+ bug:** promo B has it on every frame, cropped out at stop 15. Promo A has none in the used frames.
- **The tail is Zac's.** Everything after the goodbye (27:54 on) is outside this sheet. Zac cuts it himself and cuts in the spoiler warning himself (shot later).
- **Van gunman clip (20:53) not received yet.** Placeholder note sits between stops 18 and 19, no clip placed.
- **The transcript gives block times, not word times.** Every time above is my best estimate inside the block. Trust the search words, not the clock. Your cut may have drifted from the transcript.
- I cannot hear audio or open Premiere. Sound picks and levels come from file names, not listening. The clip crop and pillarbox settings were checked on ffmpeg-rendered frames, not in Premiere.

## Garbles to check (listed, not fixed)

Times are Premiere block starts from the transcript. Add LOGO_SECONDS for the with-logo time. The word is somewhere inside the block.

| Transcript word | Likely meant | Blocks (transcript time) |
|---|---|---|
| "Taniya miller" | T'Nia Miller (Jocasta) | 03:01 |
| "Jakarta" | Jocasta | 01:22 |
| "all, Tron", "old Tron", "all Tron", "the ultra in" | Ultron | 00:38, 01:56, 05:20, 09:24, 10:03, 10:19, 10:20, 15:33, 27:17 |
| "Ultra at the bar" | Ultron | 06:16 |
| "spade" | Spader | 04:16 |
| "Thomas" | Tommy | 04:16, 05:20, 06:59, 13:09 |
| "Division", "division's credit" | Vision | 13:09, 25:16 ("Division quest") |
| "Tommy Shepherd" | unclear, check the name | 00:38 |
| "Daredevil season three aboard again", "Daredevils dot three", "No jet two seasons" | Daredevil: Born Again, unclear | 02:21 |
| "Iranian" | vibranium | 19:54 |
| "hot it up" | shot it up | 08:48 |
| "cocked" | cooked | 10:03 |
| "side by hands", "MP." | sides of the van, unclear | 20:13 |
| "Costa", "now more than Eric. Ever." | unclear | 26:14 |
| "assassin of message board" | unclear | 26:39 |
| "Joe Horton" | unclear, check the name | 17:28 |
| "That's Deadlock and Firewall. I think I reversed those." | Winter Wolf says it himself: episode 5 is Firewall, 6 is Deadlock | 27:34 |

**"Kingsley" is NOT a KingZ garble in this episode.** The hit (03:50 "Sir Ben Kingsley") is Ben Kingsley, the actor from Wonder Man, so leave them. No "Kingsley and I" appears. "Cynthia Zoid" from the eps 3-4 sheet does not appear either.

## Still open

- Zac: the van gunman clip Matt mentioned at 20:53 ("I'll send you the clip. We can put it here") has not arrived. When it does, tell me and I add a stop with in and out points.
- Zac: want stops added once more pictures are pulled (see Gaps)?
- wwd-rights: promo B Disney+ bug (cropped out), both promos are Marvel promo cuts used under the fair use block above, the source page for each promo was not recorded in the folder. The opener is in Zac's cut, so its AI disclosure is Zac's to carry at upload.
- Not on this sheet: the post-goodbye tail and the spoiler warning (Zac's).
- After you lock the edit, tell me and the review pipeline runs (upload package, audio, shorts).

---

## Transition map

Only stops with a picture or promo clip are listed. D = designed Modern transition. Plain = hard cut, Cross Dissolve or Film Dissolve. Cams, stickers, tags, sound-only cues, the logo slot and the end card carry their own motion or none and are not counted.

| Stop | In | Out | Paired sound (level) |
|---|---|---|---|
| 2 | D: Light Leak Impacts 12f | hard cut | audioblocks-fast-start-whoosh (-18 dB) |
| 3 | Film Dissolve 12f | hard cut | none (calm set-up) |
| 4 | D: Mirror Impacts 12f | hard cut | deep-fast-whoosh (-20 dB) |
| 6 | Cross Dissolve 12f | hard cut | none (praise beat) |
| 7 | D: Luma Fade Impacts 12f | hard cut | Digital Feedback Loop 01 (-26 dB, quiet, haunting line) |
| 9 | D: Chroma Leak Impacts 12f | hard cut | Energy Swell Fluttering 07 (-22 dB) |
| 10 | D: Zoom Blur Impacts 8f | hard cut | audioblocks-frost-low-whoosh (-20 dB) |
| 11 | D: Radial Blur Impacts 10f | hard cut | CD-Rom Flash Beep Whoosh 01 (-20 dB) |
| 12 | hard cut (clip A) | hard cut | none |
| 13 | D: Phosphor Impacts 10f | hard cut | Sci-Fi Electronic Blip274 (-20 dB) |
| 14 | Film Dissolve 12f | hard cut | none (Edith hurting) |
| 15 | hard cut (clip B) | hard cut | none |
| 16 | Cross Dissolve 12f | hard cut | none (thoughtful beat) |
| 17 | hard cut | hard cut | none (next beat is the creepy cue) |

**Counts:** 14 placement stops (12 pictures, 2 promo clips). 7 have a designed transition (stops 2, 4, 7, 9, 10, 11, 13). 7 are plain (3, 6, 12, 14, 15, 16, 17). Cross Dissolve is on 2 stops (6, 16), Film Dissolve on 2 (3, 14). Each designed transition is used once. No two identical transitions in a row.

Sound files, all checked on disk 2026-10-31 under `P:\Sounds\Sound FX\`: audioblocks-fast-start-whoosh_BKITlG8RwU.mp3, deep-fast-whoosh_GyZDnHNu.mp3, audioblocks-frost-low-whoosh_BWSg1QdQKvL.mp3, Adobe\Science Fiction\Science Fiction Sci-Fi Electronic Blip274.wav, Adobe\Science Fiction\Science Fiction Sci-Fi Electronic  Energy Swell Fluttering 07.wav (two spaces after Electronic), Adobe\Multimedia\Multimedia Internet CD-Rom Flash Beep Whoosh 01.wav, Adobe\Drones\Drone Production Element Imaging Digital Feedback Loop 01.wav, Adobe\Drones\Drone Production Element Imaging Pounding Deep Low Tremor 01.wav, Adobe\Transportation\Transportation Auto Avalanche Honk Horn Short 01.wav.
