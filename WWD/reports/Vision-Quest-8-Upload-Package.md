# Vision Quest (Disney+ series, episode 8 "Forever", the series finale) - Upload Package

**Built 2026-11-17 by wwd-director from Zac's FINAL export and the final transcript.** One doc, in upload order, upload package and shorts together. Posting is one sequence with three time options per post. Nothing here has been posted, scheduled, sent or spent. Zac posts everything.

Voices in all copy: Winter Wolf (sharp, verdict-first) and KingZ (warm, connective). Handles only. No review score stated. No em dashes.

## BEFORE YOU UPLOAD (read this first)

Fix or decide these before you press publish. Full detail is in Section 9.

1. **CC BY-SA photo credit.** The Elizabeth Olsen photo (picture 12) needs the credit line. It is already pasted at the bottom of the description in Section 2. Do not remove it. Open legal question for an attorney, not decided here: whether one CC BY-SA cutaway triggers share-alike on the whole video.
2. **AI disclosure.** The series opener is Firefly-made. Tick YouTube's "altered or synthetic content" box if the opener shows realistic synthetic footage, and the safe choice is to tick it. Your call after you watch it. I did not watch it.
3. **Pictures with no recorded source page:** 14, 20, 21, 23, 24, 27 (and 1 by file name only). If any of them is in the export, record where it came from or swap it. **Picture 28 carries a Disney+ mark** (swap if a clean still exists). I did not check which of the 31 pictures made it into the export.
4. **Sound files with no license file on disk:** the Audioblocks-style files (`audioblocks-fast-start-whoosh`, `audioblocks-frost-low-whoosh`, `deep-fast-whoosh`, `strong-cinematic-hit`, `magic-turning-spells-casting`, `fast-strong-wind-whooshes`, `jg-032316-sfx-sci-fi-sweep-1`). Confirm they came from a paid plan. The Adobe library is covered by your own settled call.
5. **Loudness.** The export measures **-21.2 LUFS** integrated with a true peak of **+0.1 dBFS** (over 0, clipping risk). That is about 7.2 dB under the -14 LUFS target. Fix the master level and limiter in Premiere and re-export, or ask wwd-sound.
6. **No finale end card in the export.** The export ends on the standard "Thanks for watching" card. The `End Card - Vision Quest Finale` with the FrostCast line from the run sheet is not in it. The video works without it (Section 7).
7. **Card 3 and the card list are stale.** `WWD\data\video-inventory.md` was pulled 2026-11-02 and 11-03 and was not refreshed (no vidIQ credit spend without your yes, decision WWD-2026-11-17-01 is open). Swap card 3 for the newest FrostCast you can see in Studio.
8. **"Ultra Vision" spelling.** The transcript spells the hosts' sitcom-back-half name as "Ultra Vision", but the same transcript spells Ultron as "Ultra" and "all Tron" all over. It may be "Ultron Vision". Listen once at 06:05 and fix the description and chapter 5 if needed.

## Header

- **Source video (final):** `L:\Winter Wolfs Den review show\Raw Footage\Vision Quest\Vision Quest ep 8\Vision Quest- Ep8 Is it the best MCU show to-date.mp4`, 3,502,818,596 bytes, last written 23:08. Media Encoder also left the two raw streams beside it: `...43436.43148.m4v` (3,435,800,128 bytes) and `...43436.43148.aac`. Use the .mp4. The raw pair has no container timestamps and is not for the upload.
- **ffprobe of the .mp4:** duration **1666.90 s (27:46.90)**, 1920x1080, 30 fps, H.264 video, AAC 48 kHz stereo. Cross-check: the raw video stream has 50,007 frames, which is 1666.9 s at 30 fps, and the raw audio decodes to 27:46.96. All three agree.
- **Loudness of the export (measured, ffmpeg ebur128):** integrated **-21.2 LUFS**, true peak **+0.1 dBFS**, loudness range 7.8 LU. Same numbers on the .mp4 audio and the raw .aac.
- **Export timing:** the export was still being written when I started (the raw files were growing and locked). I waited until the .mp4 was complete and readable before reading any number above.
- **Transcript:** `Vision Quest ep 8 final .txt` (saved 22:38 on 11-17), 636 lines, Premiere format HH:MM:SS:FF, last block `00:27:32:21 - 00:27:37:22` (ends at 27:37.7). The older `Vision Quest .txt` from 11-15 (ends 27:57, no hook) was not used.
- **Transcript versus export (checked):** the export runs 9.2 s past the last spoken word. That tail is the "Thanks for watching" card (frames show it from about 27:38). To be sure the final transcript's clock is the export's clock, I transcribed the export's own audio with wwd-video-transcriber (`--num-speakers 2`, voiceprints on). It lines up to within about 1 s: "All right, boss" at 00:15, the spoken spoiler countdown at 02:55 to 03:03 in the export pass (03:05 in the Premiere file), "Take care" at 27:37. **No mismatch. Every chapter and short timecode below is the final-cut clock.** The check transcript is in `D:\WKP\scratch\vq8check\` and is a working file, not a deliverable.
- **Speaker audit:** two real speakers. Premiere labels Speaker 1 and Speaker 2, and the export's voiceprint pass names them Winter Wolf and KingZ the same way. One block at 27:03 to 27:09 is labelled Speaker 3 in the Premiere file, it is KingZ (the export pass finds only two voices). Copy says "the hosts" except where a line was checked against the label.
- **What the video opens with (frames viewed):** a cyan code-screen graphic at about 3 s (consistent with the Vision Quest opener, not compared against the kit file) and a Winter Wolf logo sting at about 13 s. The hook line runs over them from 00:00 to 00:15.
- **Audio:** `AUDIO\` mp3 not made in this job (not asked). The raw `.aac` exists.
- **Copy gate:** public copy went through `marketing-director`, which ran `script-room` (two runs on the description, posts and shorts), the `copywriting` desk (title and description parts) and `social-media` (posts and the first shorts set). The shorts were rewritten once more after `devils-advocate` rulings and then run through the `social-media` and `copywriting` desks (details in Section 9). `no-ai-slop` mechanical check (`slop_check.py`) exit code 0 on the draft and on this package. Marketing-director did the judgment pass. Details in Section 9.
- **Short ideas gate:** `devils-advocate` reviewed the five shorts and the titles. Four fixes were taken (Short 1 hard out, Short 2 cut before the verdict, Short 4 and Short 5 start lines), one short was swapped out. See Section 9.
- **QA:** `qa-director` first verdict on this package was FAIL (two blockers: shorts copy skipped the desks, and an unverified cast line). Both were fixed, see Section 9. The recheck verdict is in the report that came with this package.
- **Rights gate:** `wwd-rights`, `WWD\reports\Vision-Quest-8-Rights-Note.md` (2026-11-17), verdict: flags, see the box above.
- **Release date:** not set. The plan below assumes **Wed 2026-11-18**.

## 1. SEO / GEO Title

**Primary:** Vision Quest Episode 8 Review: Did Marvel Stick the Landing? (60 characters)
**Alt 1:** Vision Quest Finale Review: Is "Forever" the Right Ending? (58 characters, drop the quotes if the upload box mangles them)
**Alt 2:** Vision Quest Episode 8 Review: Vision, Ultron and a Coin Toss (61 characters)

Why the primary won: the keyword cluster is the first five words, the question is the one the hosts ask in the first 15 seconds, and the title gives no verdict and no score. Alt 1 uses the "Finale Review" cluster, Alt 2 names a detail from before the spoiler warning. Zac may combine them. All are under the 100 hard cap.

**Not used: the export's working title** "Is it the best MCU show to-date". It promises a ranking the video never gives (the hosts compare it to Wonder Man and WandaVision, never to the rest of the MCU), it leans toward a yes, and the only "best" support is a viewership stat that is not verified. `devils-advocate` and the writing room both ruled against it.

## 2. Full Description (one paste-ready block)

```
Vision Quest Episode 8 review: Winter Wolf and KingZ take on "Forever," the series finale on Disney+, and open with one question. Does Marvel finally stick the landing with one of its legacy shows? Before the spoiler warning at 02:55, they trade callbacks and bookends, a coin toss, and the "you're my something" line that Vision and Ultron share. The answer, and a couple of nitpicks, are in the video.

Vision Quest Episode 8 review, Vision Quest finale review, Vision Quest Forever, Vision Quest series finale, Vision Quest 2026 Disney+, Vision Quest Ultron, Vision Quest post-credit scenes

SPOILER WARNING: spoilers for Vision Quest Episode 8 start at 02:55, after a spoken warning. Watch the episode first if you want the finale clean.

CONTENT NOTE: Strong language, not bleeped.

QUICK ANSWERS
Who stars in Vision Quest? The hosts single out Paul Bettany and James Spader by name, and they praise Emily Hampshire's Edith scene.
Is Episode 8 the last episode, and is there a season 2? The hosts call "Forever" the series finale of an eight-episode run and say the show is not getting another season. That comes from the hosts, and we have not independently verified it.
Do you need to watch WandaVision first? The hosts split on it. One says to watch at least one episode, the other says Vision Quest keeps reminding you what happened. They get into it at 25:18, past the spoiler warning.
Are there post-credit scenes? Yes, two. The hosts go through them at 18:21 under a second spoiler warning, so nothing is given away here.
What do the hosts nitpick? Two things, both past the spoiler warning, so we are keeping them out of this description.
Does Vision Quest stick the landing? That is the question the video is built to answer, so the answer is not in this description. Both hosts say where they land, on camera.

WHAT WE COVER
- The opening question: does Marvel stick the landing with a legacy show
- Vision Quest and Wonder Man, and the 2026 bingo card
- Terry Matalas and his crew: callbacks, bookends, the "you're my something" line and a coin toss
- SPOILER: the sitcom-style back half the hosts call "Ultra Vision," with a Full House comparison
- SPOILER: Ultron learning loss, "I'm the Vision," and a line back to Age of Ultron
- SPOILER: Jocasta, Tommy Maximoff and Billy
- SPOILER: Friday, Jarvis, Edith and the Paladin
- SPOILER: the balcony setup and payoff, and a Luke and Vader comparison
- SPOILER: the nitpick about coordinates
- SPOILER: the hat ending and the two end-credit scenes, one of which brings back Multiverse of Madness footage
- SPOILER: five characters, one identity arc, and the runtime

YOUR TURN: Did Vision Quest stick the landing for you, or did it go off the rails? Be specific about what did not work.

Subscribe and the next one, whatever it ends up being, shows up in your feed.

Chapter titles from 02:55 on contain spoilers.

CHAPTERS
00:00:00 - Start
00:00:15 - Vision Quest Episode 8 Forever: First Reactions
00:01:44 - Terry Matalas, Callbacks And The Bookends
00:02:55 - Spoiler Warning: Who Dies And Who Was The Client?
00:05:43 - Ultra Vision: The WandaVision Sitcom Homage
00:08:14 - Ultron Learns Loss: I Am The Vision
00:10:03 - Jocasta, Edith And The Paladin In The Finale
00:12:31 - The Balcony Setup, Friday And The Luke Vader Line
00:13:55 - Tommy, Billy And The Brothers Hug
00:15:17 - The Pool Scene And The Coordinates Nitpick
00:16:17 - Drone Pilots, Edith's New Job And The Hat Ending
00:18:21 - Two Post-Credit Scenes And A Double Spoiler Warning
00:21:12 - The Multiverse Of Madness Recap Nitpick
00:22:39 - Final Thoughts: Season 2, Identity Arcs And Runtime

ABOUT
Winter Wolf's Den is a pop culture and entertainment commentary channel
hosted by Winter Wolf, KingZ, and Oracle. We cover superhero, sci-fi,
fantasy, horror, gaming, and comics with honest reviews and no studio hype.
FrostCast airs live every Wednesday at 9 PM ET.

Photo of Elizabeth Olsen by Gage Skidmore, CC BY-SA 2.0 (https://creativecommons.org/licenses/by-sa/2.0/), via Wikimedia Commons (https://commons.wikimedia.org/wiki/File:Elizabeth_Olsen_by_Gage_Skidmore_01.jpg). Resized to fit the frame.

#VisionQuest #Marvel #MCU #DisneyPlus #TVReview

FAIR USE DISCLAIMER

Copyright Disclaimer under Section 107 of the Copyright Act of 1976:
Allowance is made for fair use for purposes such as criticism, comment,
news reporting, teaching, scholarship, education and research. Fair use
is a use permitted by copyright statute that might otherwise be infringing.

All footage, images, audio and other material appearing in this video are
the property of their respective owners and are used here for the purpose
of critical review and commentary. No copyright infringement is intended.
Winter Wolf's Den does not claim ownership of any third party material.

This video is transformative in nature. It contains original commentary,
criticism and analysis, and is not intended to substitute for the original
work in any way.

If you are a copyright owner and believe material in this video has been
used improperly, please contact us directly and we will address it promptly.
```

Chapter check: 14 lines including Start, the first line is `00:00:00 - Start`, every chapter is over 10 s, every time is a block start in the final transcript (00:15, 01:44, 02:55, 05:43, 08:14, 10:03, 12:31, 13:55, 15:17, 16:17, 18:21, 21:12, 22:39) and was cross-checked against the export transcript. The hook line fills 00:00 to 00:15 inside Start. The chapter titles after 02:55 name spoilers, which is why the warning chapter comes first.

Spoiler timing note: the host's spoken lead-in starts at about 02:43 ("we are going to give you a spoiler warning right now"), the countdown ends at about 03:05 ("You've been warned"), and spoilers start in the first block after that. Whether the cut has an on-screen spoiler sticker was not checked.

Teaser check: the opening, the QUICK ANSWERS and the bullets give no verdict and no score. The hosts do give both on air.

## 3. Backend Tags

```
Vision Quest Episode 8 review, Vision Quest review, Vision Quest episode 8, Vision Quest finale review, Vision Quest finale, Vision Quest Forever, Vision Quest series finale, Vision Quest 2026, Vision Quest Disney+, Vision Quest episode 8 breakdown, Vision Quest episode 8 recap, Vision Quest post credit scenes, Vision Quest Ultron, Vision Quest Paul Bettany, Vision Quest James Spader, Paul Bettany, James Spader, Ultron, Jocasta, Terry Matalas, Marvel TV review, MCU review, WandaVision
```

(Verified with Python `len()`: 489 characters, inside the 450 to 500 window.) No "vs" tags, no ending-explained tag (the hosts recount the ending, they do not explain one), no real-name tags for private people.

## 4. Hashtags (exactly 5)

`#VisionQuest #Marvel #MCU #DisneyPlus #TVReview`

All high-volume discovery tags, none channel-branded.

## 5. Thumbnail

Thumbnails are Matt's (Winter Wolf makes them). Not ordered. Concept note only: the video's own question is "Did Marvel stick the landing?", so a question on the thumbnail matches the title and keeps the verdict off it. Pictures in `USE\` that suit it and are verified with captions: `02 vision and ultron on the sofa.png`, `06 vision and ultron sofa 108.png`, `04 ultron and jocasta in the church.png`. No score on the thumbnail. Keep the Doctor Doom, Wanda and client pictures off it, they are spoilers.

## 6. Cards (exactly 3, all inside the first 3 minutes)

| Card | Time | Tied to what is said | Destination (checked in `WWD\data\video-inventory.md`) |
|---|---|---|---|
| 1 | 00:01:05 | The hosts say their predictions about how the characters evolved over the eight-episode run came true (00:54 to 01:16) | "Vision Quest Review Eps 5 and 6: Who Is the Client? Did It Rewrite Tony Stark's Genius?" (ID YWRdI5A_cdw) |
| 2 | 00:01:50 | Wonder Man comes up at 01:44 to 02:03 | "Wonder Man Review: Marvel's Most Human Show Yet or Another Miss?" (ID 7B1LJmhfOYM) |
| 3 | 00:02:35 | FrostCast, the standing flagship card. Nothing in the first 3:00 names FrostCast, so this card is tied to the show, not to a spoken line. It sits just after the host asks viewers to comment (02:34) | "James Gunn fires back after Clayface 'Flop' / FrostCast Episode 118" (ID kYsixGzX3PQ) |

Flags: the inventory is 15 days old and was not refreshed. FrostCast Episodes 119 and 120 and the Vision Quest Episode 7 review are not in it (no video ID on file for the Episode 7 review, so I did not suggest it). Swap card 3 for the newest FrostCast in Studio, and put the Episode 7 review in place of card 1 if you prefer a link to the previous episode. No card points at a playlist: no Vision Quest playlist exists in the inventory.

## 7. End Screen

The export ends on the standard "Thanks for watching" card, about 27:38 to 27:46.9 (about 8.9 s), a Subscribe button graphic and two empty boxes. Place the end-screen elements across 27:38 to 27:46:
- Subscribe element on the logo and the Subscribe graphic.
- Left box: video tile, "Is the MCU Back? Vision Quest Review: Who Steals Episodes 1 and 2, Spader or Bettany?" (ID s9tvpaPKDBA), so a new viewer can start the series.
- Right box: "Best for viewer" (YouTube picks), or the newest FrostCast.

The finale `End Card - Vision Quest Finale (MP4)` and its "NEXT: FROSTCAST, LIVE WEDNESDAYS 9 PM ET" line are not in the export. If you want them, they go in the edit and the export has to be redone. The hosts name no next review, so no Next Up card applies.

## 8. POST SEQUENCE

Timing basis: `WWD\data\post-times.md` (researched 2026-11-02, 15 days old, under the 30-day refresh line) and Zac's locked shorts cadence (2026-11-11: YouTube Shorts one a day including Thursday at 6 to 7 PM, Facebook and Instagram one post Thursday at 6 PM). Confidence is LOW to MED, the sources disagree and the channel data cannot separate hour from topic. Audience assumed US Eastern. All times Eastern. The review is late (the finale aired before the hosts recorded), so take the earliest option you can make.

### 8.1 Full video on YouTube

Assumed release **Wed 2026-11-18**, before the FrostCast live show at 9 PM.
1. **Best:** Wed 11/18 2:00 PM. Weekday 2 to 4 PM is the best-supported long-form slot.
2. **Good:** Wed 11/18 12:00 PM. Late morning, same studies, earlier.
3. **Late but fine:** Wed 11/18 6:00 PM. Still before the live show.

Before upload: the box at the top of this doc. Tick: [ ] uploaded  [ ] description pasted  [ ] tags pasted  [ ] cards 1 to 3 set  [ ] end screen set  [ ] "altered or synthetic content" decided  [ ] scheduled or live

### 8.2 Facebook post (same day, tied to the video time)

Copy:

> Does Marvel finally stick the landing?
>
> Vision Quest Episode 8, titled Forever, is the series finale, and the hosts say there is no more season after it. They open on how the run ended, then work through the callbacks and bookends, a shared line and a coin toss. Spoilers start around 2:55, with a warning first.
>
> Sad it is over, or happy with how it ended?
>
> [VIDEO LINK]
>
> #VisionQuest #Marvel #DisneyPlus #MCU #VisionQuestEpisode8

Firefly prompt: A single silver coin frozen mid-flip above a dark table lit by drifting embers, a white android silhouette on the left and a shadowed metallic silhouette on the right facing each other across the table, deep violet and ember-gold rim light, wide empty space across the top, cinematic sci-fi comic-book painting style, no human likeness, no logos, no text

Times:
1. **Best:** Wed 11/18 3:30 PM (+90 min after a 2:00 PM video, and a table slot for Wednesday).
2. **Good:** Wed 11/18 1:30 PM (+90 min after a 12:00 PM video).
3. **Late but fine:** Thu 11/19 9:00 AM (Facebook's best-supported Thursday slot).
Tick: [ ] image made  [ ] posted

### 8.3 Instagram post (same day)

Copy:

> Vision Quest Episode 8 review is up, and the cards are all on the table.
> It is the series finale, titled Forever, and the hosts say the show gets no more seasons.
> They trace the callbacks and bookends, from the "you're my something" line to a coin toss.
> Spoilers start around 2:55, with a warning first.
> Which callback did you catch first?
> Full video at the link in bio.
>
> #VisionQuest #VisionQuestEpisode8 #MarvelTV #DisneyPlus #MCU #Marvel #Ultron #TVReview

Firefly prompt (16:9 horizontal, to match the video thumbnail; Instagram only takes 4:5 to 1.91:1 and every image in one post must share the ratio): A long dark table seen from a low angle, a fan of face-down playing cards in the foreground and a single glowing silver coin standing on its edge in the center, soft violet and ember-gold light, a faint white android silhouette far in the background, large empty dark space across the top third, moody cinematic key art, painterly style, no faces, no likenesses, no logos, no text

Times:
1. **Best:** Wed 11/18 2:45 PM (+45 min after a 2:00 PM video).
2. **Good:** Wed 11/18 12:45 PM (after a 12:00 PM video).
3. **Late but fine:** Thu 11/19 9:00 AM (Instagram's best-supported Thursday slot).
Tick: [ ] image made  [ ] posted

### 8.4 Shorts (post only after the full video is live; non-spoiler first, spoilers from mildest to heaviest)

The five shorts are BUILT (2026-11-18, `shorts-factory.md`, CPU x264, from the final .mp4) in the episode folder's `shorts` subfolder. Each block gives the real file, length, loudness, final-cut in and out, and the cover. Nothing is scheduled or posted. Burned-in captions read Terry Matalas, never the transcript's garbles (McAuliffe, Metallic, Metalist, Alice).

Cadence note: five shorts fill the YouTube slot for Thu to Mon (one a day) and one Facebook and one Instagram post a day. Zac's cadence of 4 to 5 Facebook and Instagram posts a day Friday to Tuesday cannot be met by one review's five shorts. The other posts that week come from the FrostCast Episode 121 shorts. I did not shrink the cadence, I am saying plainly this pool is five.

### Short 1: THE QUESTION (post 1st, non-spoiler)
Source (as built): 00:14.8 to 00:38.0 on the final cut, 23.25 s. Starts on the hosts' greeting, after the 14 s opener. Ends before the verdict (which starts at 00:38.4).
On-screen hook: DID MARVEL STICK THE LANDING?
Opens on: "All right boss, we are here"   Ends on: the question, sad it is over or happy with how it ended, and "this would be a good wrap-up".

YouTube title:Vision Quest Finale: Did Marvel Stick the Landing?

YouTube description: Vision Quest Episode 8 is called "Forever," and the hosts say the show gets no season after it. Before the review gets going, KingZ puts one question to Winter Wolf: sad it is over, or happy with how it ended? His answer is in the full review.
#VisionQuest #Marvel #DisneyPlus #Shorts

Instagram caption: A show with no more seasons, ending on an episode called "Forever." KingZ asks Winter Wolf to pick a side: sad it is over, or happy with how it ended? Tell us yours before you hear his. Full review on the channel.
#VisionQuest #MarvelTV #MCU #DisneyPlus #TVReview

Facebook caption: Winter Wolf opens the Vision Quest finale review by asking if Marvel finally sticks the landing with a legacy show. KingZ's follow-up is simpler: are you sad it is over, or happy with how it ended? Pick one in the comments.
#VisionQuest #Marvel #DisneyPlus
File (BUILT 2026-11-18, 1080x1920, 30 fps, burned-in captions and hook text): `L:\Winter Wolfs Den review show\Raw Footage\Vision Quest\Vision Quest ep 8\shorts\clip1_the-question.mp4`. Length 23.25 s, loudness -16.8 LUFS, source in/out on the final cut 00:14.8 to 00:38.0. Cover frame (first frame, also saved as a PNG beside the clip): `USE\25 vision on the yellow phone.png` (Vision on the yellow phone (cover frame only; the clip itself is the two hosts)).
Times (basis: Zac's shorts cadence, locked 2026-11-11, plus `WWD\data\post-times.md` for FB and IG):
YouTube Shorts: Thu 11/19 6:00 PM (best) / 6:30 PM (good) / 6:55 PM (late). Zac's locked window is 6 to 7 PM.
Facebook: Thu 11/19 6:00 PM (best, Zac's Thursday slot) / 6:30 PM (good) / 7:30 PM (late).
Instagram: Thu 11/19 6:00 PM (best) / 6:30 PM (good) / 7:30 PM (late).
Tick: [ ] YT  [ ] IG  [ ] FB

### Short 2: CALLBACKS EVERYWHERE (post 2nd, non-spoiler)
Source (as built): 02:00.8 to 02:34.9 on the final cut, 34.15 s. Ends on "let us know in the comments below", before "what stood out to you guys is the best part of this finale" and the verdict talk.
On-screen hook: CALLBACKS EVERYWHERE
Opens on: "...it didn't sacrifice any of the actual writing, and full credit to Terry..."   Ends on: "...let us know in the comments below"
Build notes: burned captions must read Matalas, the transcript garble is McAuliffe. No Wonder Man, no bingo in copy or hook (the clip starts after both).

YouTube title:Vision Quest Episode 8: Callbacks, Bookends and a Coin Toss

YouTube description: Winter Wolf says Terry Matalas and his crew packed the Vision Quest finale with "at least two or three, maybe even four" callbacks and bookends. He names two: the "you're my something" line that Vision and Ultron share, and a coin toss. The rest he leaves for you to find. Clip from the full review.
#VisionQuest #Marvel #MCU #Shorts

Instagram caption: Count the callbacks. Winter Wolf puts the number at two or three, maybe four, and only names a couple: the "you're my something" line and a coin toss. Credit to Terry Matalas and his crew for the bookends. How many did you catch? Full review on the channel.
#VisionQuest #MarvelTV #MCU #DisneyPlus #TVReview

Facebook caption: Vision Quest Episode 8 loops back on itself, and Winter Wolf gives Terry Matalas and his crew the credit. A line two characters share, a coin toss, and a few more he will not spoil. Which callback was your favorite? Tell us below.
#VisionQuest #Marvel #DisneyPlus #MCU
File (BUILT 2026-11-18, 1080x1920, 30 fps, burned-in captions and hook text): `L:\Winter Wolfs Den review show\Raw Footage\Vision Quest\Vision Quest ep 8\shorts\clip2_callbacks-everywhere.mp4`. Length 34.15 s, loudness -14.4 LUFS, source in/out on the final cut 02:00.8 to 02:34.9. Cover frame (first frame, also saved as a PNG beside the clip): `USE\11 age of ultron vision and ultron.png` (Age of Ultron frame of Vision and Ultron, fits the shared line).
Times (basis: Zac's shorts cadence, locked 2026-11-11, plus `WWD\data\post-times.md` for FB and IG):
YouTube Shorts: Fri 11/20 6:00 PM (best) / 6:30 PM (good) / 6:55 PM (late).
Facebook: Fri 11/20 9:30 AM (best) / 12:00 PM (good) / 3:30 PM (late).
Instagram: Fri 11/20 12:00 PM (best) / 6:00 PM (good) / 3:00 PM (late).
Tick: [ ] YT  [ ] IG  [ ] FB

### Short 3: GIVE ME THE COORDINATES (post 3rd, SPOILER, mild)
Source (as built): 15:17.5 to 16:13.8 on the final cut, 56.45 s
Out-point choice: cut just BEFORE "But it was at that reunion bit at the end that was solid", so no verdict word. The clip ends on "Get the coordinates on the record." (about 00:16:15). HARD OUT backward.
On-screen hook: GIVE ME THE COORDINATES
Opens on: KingZ, "I like the part when they meet the first time"   Ends on: "Get the coordinates on the record."
Checks: mild profanity in the audio, ships as recorded, not repeated in copy. The review has two nitpicks, so captions say "a nitpick", never "the only nitpick".

YouTube title:SPOILER: Vision Quest Episode 8, 15 Seconds of Air and a Nitpick

YouTube description: SPOILER for Vision Quest Episode 8. Two brothers meet for the first time and one asks, "Does everybody in this family have imaginary friends?" Then Winter Wolf has a nitpick: with 15 seconds of air left, hand over the address before the hugging starts. KingZ pushes back. Clip from the full review. Strong language in the audio.
#VisionQuest #Spoilers #Marvel #Shorts

Instagram caption: SPOILER for Vision Quest Episode 8. Only 15 seconds of air left, and the first move is a hug? Winter Wolf would rather get the address on the record first. KingZ says you cannot know how you would act. Who wins this one? Full video on the channel.
#VisionQuest #Spoilers #MarvelTV #MCU #DisneyPlus

Facebook caption: SPOILER for Vision Quest Episode 8. A portal scene gets a laugh from the hosts, then a nitpick from Winter Wolf: if you are low on air, you say where you are before anything else. KingZ's answer is that nobody knows how they would react meeting a version of family for the first time. Would you have asked for the coordinates first?
#VisionQuest #Spoilers #Marvel
File (BUILT 2026-11-18, 1080x1920, 30 fps, burned-in captions and hook text): `L:\Winter Wolfs Den review show\Raw Footage\Vision Quest\Vision Quest ep 8\shorts\clip3_give-me-the-coordinates.mp4`. Length 56.45 s, loudness -15.0 LUFS, source in/out on the final cut 15:17.5 to 16:13.8. Cover frame (first frame, also saved as a PNG beside the clip): `USE\30 edith hugging vision.png` (Edith hugging Vision).
Times (basis: Zac's shorts cadence, locked 2026-11-11, plus `WWD\data\post-times.md` for FB and IG):
YouTube Shorts: Sat 11/21 6:00 PM (best) / 6:30 PM (good) / 6:55 PM (late). Spoiler short, so not before about 72 hours after the full video (Wed 2:00 PM plus 72 h is Sat 2:00 PM).
Facebook: Sat 11/21 2:00 PM (best) / 5:00 PM (good) / Sun 11/22 10:00 AM (late).
Instagram: Sat 11/21 6:00 PM (best) / 2:00 PM (good) / Sun 11/22 10:00 AM (late).
Tick: [ ] YT  [ ] IG  [ ] FB

### Short 4: I SENSE THE GOOD IN YOU (post 5th, SPOILER, heaviest of the five after the Short 5 trim)
Source (as built): 12:31.7 to 13:14.1 on the final cut, 42.55 s
On-screen hook: I SENSE THE GOOD IN YOU
Opens on: "You called it and you called the Friday thing"   Ends on: "It is Luke Vader, it is the same thing."
Build notes: burned captions must read Matalas (transcript garbles it as "Metallic" and "mittal"). The Luke and Vader line is spoken audio only, kept out of the YouTube title. Copy does not say who survives or what the balcony moment decides.

YouTube title:SPOILER: Vision Quest Episode 8, Ultron, Friday and a Balcony

YouTube description: SPOILER, moderate to heavy for Vision Quest Episode 8. Winter Wolf says Terry Matalas and his crew set up a balcony moment between Ultron and Friday, credits KingZ for calling it, then reaches for a Luke and Vader comparison. Clip from the full review. Strong language in the audio.
#VisionQuest #Spoilers #Marvel #Shorts

Instagram caption: SPOILER, moderate to heavy for Vision Quest Episode 8. Ultron, Friday, a balcony, and a setup that stopped Winter Wolf cold. KingZ saw part of it coming. Credit to Terry Matalas and his crew, and then a Star Wars father and son comparison. Did you call it? Full video on the channel.
#VisionQuest #Spoilers #MarvelTV #MCU #DisneyPlus

Facebook caption: SPOILER, moderate to heavy for Vision Quest Episode 8. Winter Wolf walks through one setup and payoff from Terry Matalas and his crew, and his first reaction to the setup was shock. KingZ gets credit for calling part of it. Then Luke and Vader come up. Did you see this one coming?
#VisionQuest #Spoilers #Marvel
File (BUILT 2026-11-18, 1080x1920, 30 fps, burned-in captions and hook text): `L:\Winter Wolfs Den review show\Raw Footage\Vision Quest\Vision Quest ep 8\shorts\clip4_i-sense-the-good-in-you.mp4`. Length 42.55 s, loudness -14.7 LUFS, source in/out on the final cut 12:31.7 to 13:14.1. Cover frame (first frame, also saved as a PNG beside the clip): `USE\16 friday jarvis u and dum-e.png` (Friday, Jarvis, U and Dum-E).
Times (basis: Zac's shorts cadence, locked 2026-11-11, plus `WWD\data\post-times.md` for FB and IG):
YouTube Shorts: Mon 11/23 6:00 PM (best) / 6:30 PM (good) / 6:55 PM (late).
Facebook: Mon 11/23 9:30 AM (best) / 12:00 PM (good) / 3:30 PM (late).
Instagram: Mon 11/23 9:00 AM (best) / 6:00 PM (good) / 3:00 PM (late).
Tick: [ ] YT  [ ] IG  [ ] FB

### Short 5: THE SITCOM TWIST (post 4th, SPOILER, moderate)
Source (as built): 05:48.2 to 06:13.0 on the final cut, 24.85 s. Trimmed at the build so the how-Vision-reaches-Ultron lines (about 06:32 to 06:52) are not in the clip
On-screen hook: THE SITCOM TWIST
Opens on: "I thought the best part of this show was their clever reinterpretation of WandaVision" (start on that phrase, not "Without with us on the line")   Ends on: "...very much old 80s sitcom, and I love that."
Build notes: on-screen text garbles Matalas as "Terry Alice", fix it. Copy says nothing about how Vision wins. See the flag in the report: the audio at about 06:32 to 06:52 does say it.

YouTube title:SPOILER: Vision Quest Episode 8 and the Sitcom Twist

YouTube description: SPOILER for Vision Quest Episode 8. The back half of the finale turns into an 80s sitcom, saxophone theme included, and even the on-screen credit gets in on the joke. Winter Wolf reaches for Full House. Clip from the full review.
#VisionQuest #Spoilers #Marvel #Shorts

Instagram caption: SPOILER for Vision Quest Episode 8. A saxophone theme, an 80s sitcom look, and an on-screen credit that plays like a punchline. Winter Wolf reaches for Full House. Which sitcom did it remind you of? Full review on the channel.
#VisionQuest #Spoilers #MarvelTV #MCU #DisneyPlus

Facebook caption: SPOILER for Vision Quest Episode 8. Out of nowhere, the finale starts playing like Full House, saxophone theme and all. Winter Wolf says it is a clever reinterpretation of WandaVision. Did you catch the WandaVision link right away?
#VisionQuest #Spoilers #Marvel
File (BUILT 2026-11-18, 1080x1920, 30 fps, burned-in captions and hook text): `L:\Winter Wolfs Den review show\Raw Footage\Vision Quest\Vision Quest ep 8\shorts\clip5_the-sitcom-twist.mp4`. Length 24.85 s, loudness -14.8 LUFS, source in/out on the final cut 05:48.2 to 06:13.0. Cover frame (first frame, also saved as a PNG beside the clip): `USE\10 wall of tvs.png` (wall of TV screens, fits the sitcom beat).
Times (basis: Zac's shorts cadence, locked 2026-11-11, plus `WWD\data\post-times.md` for FB and IG):
YouTube Shorts: Sun 11/22 6:00 PM (best) / 6:30 PM (good) / 6:55 PM (late).
Facebook: Sun 11/22 10:00 AM (best) / 1:00 PM (good) / 5:00 PM (late).
Instagram: Sun 11/22 10:00 AM (best) / 6:00 PM (good) / 2:00 PM (late).
Tick: [ ] YT  [ ] IG  [ ] FB

Cover note: Cover pictures are chosen from the verified or captioned pictures only. The rights note says each short cover needs its own check, this one is not done. Do not use pictures 8, 9, 15 or 19 (other titles) on a cover.

### How to post, click by click
YouTube Studio: studio.youtube.com, Create (top right), Upload videos, pick the clip, paste the title and description from its block, "No, it's not made for kids", Next to Visibility, Schedule, pick the date and time, Schedule.
Meta Business Suite: business.facebook.com, Create reel. Select both the Winter Wolf's Den page and the winterwolfsden Instagram, upload the clip, pick the cover, use Customize post to paste the Instagram caption for Instagram and the Facebook caption for Facebook, then Schedule. The composer defaults to the wrong page unless `asset_id=104052046075172` is in the address.
Before posting any short: confirm the full video is live, and listen to the first word of each clip.

## 9. Flags and Production Notes

**Rights flags still open (from wwd-rights, 2026-11-17):**
1. Pictures 14, 20, 21, 23, 24, 27 (and 1, 6 by file name) have no recorded source page. 14 is a three-frame fan-style screen-grab collage with a burned-in subtitle. 21 is low resolution.
2. Picture 28 carries a Disney+ watermark, swap preferred. If kept, 5 to 6 s, never enlarged.
3. Picture 12 is CC BY-SA 2.0 (Gage Skidmore). The credit line is in the description. The share-alike question is for an attorney.
4. Audioblocks-style sound files: no license file on disk (box above).
5. Opener and end-card audio origin not verified. The sax hit is a one-shot, not a song.
6. AI disclosure for the Firefly opener (box above).
7. Other-title pictures (8 WandaVision, 9 Full House, 15 Johnny 5, 19 Luke and Vader) sit only on the line where a host names that title. Keep them off shorts covers.

**Stale-line check:** no spoken line names a date, a next episode or a next review. The hosts say the show has no more seasons, which is their statement and is not independently verified (the description says "the hosts say"). The 3.7 million viewership stat (23:34 to 23:49) is left out of all copy because it is unverified.

**Run sheet open questions, answered by the final transcript and export** (`WWD\reports\Vision-Quest-8-Edit-Run-Sheet.md`, Still open list):
| # | Question | Answer |
|---|---|---|
| 1 | Is the Firefly opener already in the cut? | Yes. A cyan code-screen graphic is on screen at about 3 s and a Winter Wolf logo sting at about 13 s, with the hook line spoken over them. Not compared against the kit file. |
| 2 | Cam sync | Not answerable from the export. The two-shot layout shows both cams with the right speaker talking at the frames I viewed (27:30 to 27:37), nothing more. |
| 3 | Is there a tail after "Take care"? | Only the "Thanks for watching" card, about 27:38 to 27:46.9. |
| 4 | Is the end card's FrostCast line still right? | Moot. The finale end card is not in the export. |
| 5 | Speaker 3 at 27:03 | KingZ. The export's voice pass finds two voices only. |
| 6 | Picture 5 versus EP 7's near twin | Not answerable here. |
| 7 | Second spoiler alert copy | The hosts do say a second ("double") spoiler warning at about 18:27. Whether the on-screen alert plays twice was not checked. |
| 8 | Do the two .mov stickers play cleanly | Not checked. |
| 9 | Optional rune-room teaser clip | Not answerable here. |
**Also:** the run sheet was built on the older 27:57 transcript. Its clock is about 15 s off the final cut at the start (the final has a hook the older file lacks) and about 20 s long at the end. Treat its times as stale. Nothing in this package uses them.

**Judgment calls and notes:**
- Profanity ships as recorded (WWD rule). Nothing in public copy repeats it. The description carries a content note.
- "Jocasta" is the show's spelling. The transcript has "Jakarta" twice. The description names Emily Hampshire, which the host says at 11:49 in the Edith scene talk. Role-to-actor pairings are not claimed in the description, the cast list in the picture tags comes from the series Wikipedia page, not fact-research. The hosts credit Terry Matalas "and his crew", copy gives him no job title because the transcript does not say who directed.
- Short 5 was trimmed at the build to end on "very much old 80s sitcom and I love that" (05:48 to 06:13), so the "how Vision gets through to Ultron" lines are NOT in the clip. Its burned-in caption does say "Ultra Vision" because that is how the final transcript spells the spoken phrase; the post copy still avoids the spelling. Short 1 starts at 00:14.8, after the opener, instead of 00:00 (the opener is 14 s of kit pieces and would waste the hook).
- Short 3 audio says "my only nitpick" although a second nitpick comes at 21:12. Captions say "a nitpick". Short 3 ends on "Get the coordinates on the record." and drops the "solid" line that follows. Short 4 audio has mild profanity.
- Short 4 names Winter Wolf in its captions because the transcript label confirms the speaker.
- The old "Why recap it" short was dropped: its audio opens on the post-credit reveal.
- Picture 5 is a near twin of EP 7's `in shadow client.png` (a different frame of the same park scene), flagged in the run sheet.
- No vidIQ pull was run (credits need Zac's yes, decision WWD-2026-11-17-01 open). The only recent data file is `data\weekly-2026-11-13.md`, which has no per-video timing data. Timing therefore rests on `post-times.md`.

**Gate log (who touched what):**
- `marketing-director` ran the copy: `script-room` drafted titles and description parts and reviewed the posts and shorts, `copywriting` reworked the titles and description parts, `social-media` drafted the Facebook and Instagram posts and the first shorts set. Marketing-director edited three lines of the Quick Answers.
- Second pass (shorts rewrite after devils-advocate): `script-room` rewrote the five sets, then, after `qa-director` failed the package for skipping the desks, `marketing-director` called BOTH the `social-media` desk and the `copywriting` desk on all five sets (both ran, outputs `D:\WKP\scratchq8-shorts-socialmedia.md` and `vq8-shorts-copywriting.md`). The marketing-director agent then hit a rate limit before its final edit pass, so wwd-director chose the copywriting set (more specific, quotes the hosts accurately) and made three small edits: removed the "Ultra Vision" spelling from the Short 5 title, YouTube description and Instagram caption because the spelling is unverified. The judgment pass on the shorts is therefore wwd-director's, not marketing-director's. Flagged so a marketing-director read can be asked for.
- `devils-advocate` ruled on all five shorts and the three titles (verdicts: Short 1 fix first, Short 2 fix first, Short 3 fix first, Short 4 (coordinates) fix first, Short 5 (recap) rethink and swap, Primary title keep, working title rethink). Its list is in `D:\WKP\scratch\vq8-devils-advocate.md`.
- `no-ai-slop`: mechanical check `slop_check.py` exit 0 (draft file and this package). Em dash check: none.
- Not run: `originality` and `clearance` (not scripts), `fact-research`, any vidIQ pull.

### Caption fix list (find and replace in the auto-caption file)
find "Jakarta" -> replace "Jocasta"
find "all Tron" -> replace "Ultron"
find "Altra" -> replace "Ultron"
find "Ultra" (when it means the character) -> replace "Ultron"
find "Terry McAuliffe" -> replace "Terry Matalas"
find "Terry Metallic" -> replace "Terry Matalas"
find "Tara Metalist" -> replace "Terry Matalas"
find "Tara mittal" -> replace "Terry Matalas"
find "Terry Alice" -> replace "Terry Matalas" (the on-screen credit the hosts read out at 06:05)
find "division" (23:55 and 25:38) -> replace "WandaVision"
find "Wanderers" -> replace "WandaVision" (check by ear)
find "Jennifer" (12:01 to 12:20 block) -> replace "Lisa"
find "King Z" -> replace "KingZ"
find "Acosta" (26:50) -> replace "Jocasta"
find "Costa" (04:41) -> check by ear, probably "Costa" is a garble of the actor's name, fix after listening
find "Ultra Vision" -> check by ear, may be "Ultron Vision" (box above)
No real first or last names of the hosts or private people are in the final transcript. Real names of the show's cast and crew said on air (Paul Bettany, James Spader, Elizabeth Olsen, Emily Hampshire, Terry Matalas) are fine.

## 10. Fair Use (always last)

Same block as pasted at the end of the description in Section 2, never reworded:

```
FAIR USE DISCLAIMER

Copyright Disclaimer under Section 107 of the Copyright Act of 1976:
Allowance is made for fair use for purposes such as criticism, comment,
news reporting, teaching, scholarship, education and research. Fair use
is a use permitted by copyright statute that might otherwise be infringing.

All footage, images, audio and other material appearing in this video are
the property of their respective owners and are used here for the purpose
of critical review and commentary. No copyright infringement is intended.
Winter Wolf's Den does not claim ownership of any third party material.

This video is transformative in nature. It contains original commentary,
criticism and analysis, and is not intended to substitute for the original
work in any way.

If you are a copyright owner and believe material in this video has been
used improperly, please contact us directly and we will address it promptly.
```

Rights Production Notes line (from wwd-rights, worded to match this video): "Rights check: no trailer or promo clips used. Stills are series press and gallery images used for commentary, each on the line it is about, each under 7 s, none repeated, plus one CC BY-SA cast photo credited in the description. The series opening animation was made with Adobe Firefly (altered or synthetic content box decided at upload). Intro and outro audio source: to be named."
- Shorts build notes (2026-11-18, after the QA recheck fixes): POST ORDER CHANGED. After the Short 5 trim, Short 4 (Ultron, Friday, balcony) is the heavier spoiler, so the order is 1, 2, 3, then Short 5 on Sun 11/22, then Short 4 last on Mon 11/23. The block numbers did not change, so the file names still match. Short 2 captions were repaired: the two garbled phrases were re-listened with the speech model and prompted (large-v3), result "what was the other good one, at the very end, the 50/50 with the coin toss, Ultron be good, 50/50, a coin toss"; a second small model agreed on "Ultron, be good". Listen once at about 02:23 to 02:30 to confirm. Short 1 no longer shows the word "dude" and Short 4 no longer ends on a caption with no audio. Short 5's burned caption says "ULTRA VISION", the final transcript's spelling; listen at about 05:55 of the full video (clip 7 to 9 s) and if it is "Ultron Vision", tell me and the clip rerenders in a minute. Short 5 copy now names Winter Wolf only, since he is the only speaker in that clip. Short 1 shows the series poster (October 14, Disney+ logo) for a few seconds inside the final cut itself, about 17 to 24 s of the full video; this is the cut's own picture, not an added one, flagged for wwd-rights (not rerun here). Short 3 and Short 4 burn in mild profanity as spoken. Short 1 loudness -16.8 LUFS is under the other four because the clip is short and starts on a quiet room.
- Audio-only file: `AUDIO\Vision Quest Ep 8.mp3`, 192 kbps, 1666.90 s (matches the video).
