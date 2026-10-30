# Vision Quest (Disney+ series, eps 3 and 4) - Rights Note (DRAFT 2026-10-28, FINAL section added 2026-10-29)

Author: wwd-rights. Reports to wwd-director.
**This is a risk flag, not legal advice. Fair use is decided case by case, and a Content ID claim or copyright strike can still happen even on a clean cut. Nothing here promises otherwise.**

# FINAL CUT CHECK (2026-10-29)

Checked: `...\Vision Quest ep 3 and 4\Vision_Quest_EP_3_and_4_review.mp4` (ffprobe: 1157.9 s = 19:17.9, one video and one audio stream). Method: frames pulled with ffmpeg at the stated times, bottom-right corner crops tiled at 6 to 10 fps across each trailer window, scene-cut detection around each window, still checked by eye. Not done: I cannot hear audio, so "muted" is unverified by ear. The two trailer files in the timeline were not re-opened. Upload package for eps 3 and 4: not available (no such file in WWD\reports yet).

## Final results

| # | Item | Result | What it rests on | Action |
|---|---|---|---|---|
| F1 | Trailer count and seconds | PASS on the cap, FLAG on the flash | 3 trailer blocks. (1) Opening flash 0.0 to about 1.8 s, several quick shots. (2) Ultron and Vision, scene cuts at 478.97 and 480.13 s, about 1.2 s. (3) Pool scene, about 606.3 to 607.97 s, about 1.7 s. Total about 4.7 s against the 30 s cap. Each block under 4 s. | None for the cap |
| F2 | Opening flash: Disney+ bug | FLAG, fix before export | Corner crops at 8 fps from 0 to 1.9 s: the Disney+ logo is plainly visible in 15 of 16 samples, no blur. Frame at 0.1 s is Vision in the hall, 0.6 s is the house, both with the full logo. Standards rule 13: no studio logo. | Do one of two things. (a) Cut the flash and start the Firefly opener at 0.0 (cleanest, removes the risk). (b) Keep the flash and put the same corner blur on it as the Ultron and pool clips, frame by frame, for the full 1.8 s. I recommend (a). Either way, it must be shorter than 4 s and not stacked with the other two. |
| F3 | Opening flash: under a host line, not back to back | FLAG | Several different shots cut one after another in 1.8 s, under a hook voice-over. I did not confirm the hook line is about those scenes. Rule 12 says a clip plays only under a line about that exact scene, and no clips back to back. | If the flash stays, wwd-director confirms the hook line describes what is on screen. If it cannot, cut it (this is another reason for option a). |
| F4 | Ultron and Vision clip (about 479 s) | PASS | Corner crops across 478.9 to 480.3 s: no logo visible in any frame (area is dark, nothing legible). Full frame at 479.5 s shows no bug. Single shot, 1.2 s. | None. Zac still scrubs it once at full size. |
| F5 | Pool scene clip (about 606.3 to 607.97 s) | PASS (visible blur) | Corner crops across the window: the logo is not legible in any frame. The blur shows as a soft rectangle with hard vertical edges on a few frames (visible on the bright water), so it looks edited. Single shot, 1.7 s. | None for rights. Optional: soften the blur edge so it is less obvious. |
| F6 | Muted trailer audio | UNVERIFIED | The Premiere Ready MUTED files have no audio stream (draft note, ffprobe). I cannot hear the final. Hosts talk over both windows. | Zac listens to 478.5 to 480.5 s and 606 to 608 s and the first 2 s with the hosts muted in his head, or solos A1 off. Any trailer sound or music under the flash fails rule 11. |
| F7 | Stills | FLAG (record mismatch) | Stills seen by eye: 38 (key art, TMDb, at about 20 s), 19, 27, 17, 11, 16, 21, and the 795 s close-up. The 795 s picture is USE\37.png (pixel match 1.00), a young man in a grey bomber jacket in a station or market. But `pictures-tags.md` row 37 describes 37.png as a chrome female robot beside a woman, source TMDb qmYfpB9O7yUvjri6WGWzHWQH9Nl. The tag file and the file on disk disagree, so the source for what is on screen is not recorded correctly. Others still carry the draft note's open items: IMDb URLs are "order-assumed", not verified. No still repeats in the frames I saw. Not checked: 36 and the rest of the 10. | wwd-pictures fixes the row for 37 (real source and who) or swaps the picture. Record the source for every still shown. Commentary use, brief, each under 7 s. |
| F8 | Music | NOT COVERED | I heard nothing (cannot hear). Opener MP4 and the Next Up MP4 both carry an audio stream (ffprobe: 11.5 s and 6.0 s). Where that audio came from is not recorded in what I read. The Firefly opener's audio could be model-generated. | Zac or wwd-vfx states: (1) the opener's audio source, owned P:\ sounds or generated; (2) the intro and outro tracks, if any, with the owned-library path or YouTube Audio Library attribution line. Suno stays FLAG while the plan is lapsed (STANDARDS, lapsed as of 2026-10-26). |
| F9 | Sounds | PASS on paper | Sound cues are from `P:\Sounds\` per the draft XML. I did not listen to the final. | None |
| F10 | AI-made assets | FLAG, disclosure needed | The Firefly opener is in the final (frame at 8 s is a Firefly cyberspace plate, then the in-house wolf logo burn at about 14 s). Firefly output, so use the YouTube altered or synthetic content box. If the opener audio is model-generated, that counts too. No Suno track known. | Zac ticks the altered or synthetic content box at upload. |
| F11 | In-house cards and logos | PASS | Next Up terminal card (about 1145 s) is in-house text and shows no Disney or Marvel mark. Wolf logo is Winter Wolf's Den. Thanks for watching card is in-house. | None |
| F12 | Upload package and disclaimer | NOT AVAILABLE | No eps 3 and 4 package in WWD\reports. | Disclaimer last, worded as below. |

## QA items I found while scanning (not rights, passing along)
- Thanks for watching card is on screen at 1152.5 s but frames at 1153.5, 1154.2, 1156 and 1157.5 s are plain black. The stated 1153.1 to 1157.9 s card window shows nothing. Check the end of the timeline.
- Stuck "Grandfather is the fun one." caption on the KingZ tile, as you reported (not rewatched by me).

## Paste into the upload package
**Section 12, Production notes (flags):**
1. Rights check: trailer excerpts total about 5 s (Ultron and Vision 1.2 s, pool scene 1.7 s, plus the opening flash if it stays). Each under 4 s, muted, Disney+ corner mark blurred or cut. The opening flash must be cut or blurred before export.
2. Stills: 10 stills from official galleries (IMDb, TMDb) and official key art, used for commentary, each under 7 s, none repeated. Source row for still 37 to be corrected.
3. AI disclosure: the opener is Firefly-generated footage. Tick "altered or synthetic content" at upload.
4. Music: intro and outro only, source to be named (owned P:\ library, or YouTube Audio Library with an attribution line). No Suno unless the paid plan is confirmed.

**Section 13, Fair use disclaimer (last section):**
"This review is commentary and criticism. Short, muted trailer excerpts (about 5 seconds in total) and a small number of promotional stills from Vision Quest are used under fair use, only to illustrate what the hosts are discussing. Vision Quest, its characters and its footage belong to Marvel Studios and Disney. No endorsement by or affiliation with them is implied. The opening animation was generated with Adobe Firefly. If you hold rights to anything shown and want it removed, contact us and we will act promptly." (Edit the seconds figure to match the final cut after F2 is fixed. If the flash is cut, trailer total is about 2.9 s.)

## What Zac must do (final)
1. Cut the opening flash and start the Firefly opener at 0.0, or blur the Disney+ bug for the full 1.8 s (F2, F3).
2. Confirm the first 2 s, and both windows, have no trailer sound (F6).
3. Fix or swap still 37 so its source is recorded correctly (F7).
4. Name the intro and outro music and the opener's audio source (F8).
5. Tick the altered or synthetic content box (F10).
6. Fix the end of the timeline black frames and the stuck caption.
7. Send the finished package back to wwd-rights for the disclaimer check.

DECISION QUEUED: none. Legal question for an attorney, only if Zac wants certainty: does blurring a platform watermark on a trailer excerpt change a fair use analysis.

---

# EARLIER NOTE ON THE DRAFT CUT (2026-10-28, superseded by the FINAL section above where they differ)

Checked: draft video `...\Vision Quest ep 3 and 4\Vision Quest EP 3 and 4 Review - DRAFT for Zac.mp4` (ffprobe: 1145.5 s = 19:05.5, h264 video + aac audio), its Premiere export `...DRAFT for Zac.xml` (clip names listed), `USE\pictures-tags.md`, run sheet `WWD\reports\Vision-Quest-3-4-Edit-Run-Sheet.md`, `WWD\STANDARDS.md`. Not done: I did not watch or frame-scan the rendered draft. Findings on its contents rest on the XML clip list and the run sheet's own frame checks. Upload package for eps 3 and 4: not available (no such file in WWD\reports yet), so disclaimer and disclosure checks are pending.

## Results

| # | Item | Result | What it rests on | Action |
|---|---|---|---|---|
| 1 | Trailer clip count and total | PASS | XML shows 2 trailer clips (A, B) from one file, `VisionQuest - Official Trailer (2-39) MUTED.mp4`. Run sheet: A 00:02:15:06 to 00:02:16:10 (about 1.2 s), B 00:02:12:22 to 00:02:14:18 (about 1.9 s). Zac's handoff says 1.17 s and 1.83 s. Total about 3.0 to 3.1 s vs 30 s cap. Each under 4 s. | None |
| 2 | Under a host line about that scene | PASS (one soft spot) | A sits on "Ultron has moved in as his number one confidant"; B on "scene in the pool". Per the run sheet, the Tommy and father ID for clip B is a visual match plus the hosts' words only. | Zac: confirm B really is the pool scene he means |
| 3 | Not back to back | PASS | A about 07:57, B about 10:05, over 2 min apart (rule: at least one full spoken line) | None |
| 4 | Muted | PASS | ffprobe of the MUTED file: video stream only, no audio stream. The un-muted copy is not in the XML clip list. | Keep the un-muted copies out of the timeline |
| 5 | No title card, release date, studio logo in clip | FLAG (see a) | Run sheet says clips cut inside one shot before any card. Disney+ corner bug is in every trailer frame; Zac says it is blurred on both clips. I did not view the blur in the render. | Zac: scrub both clips once at full size, confirm the blur holds on every frame |
| 6 | Stills | FLAG (see b) | 10 stills used (38, 19, 35, 27, 17, 34, 11, 37, 16, 21), none used twice (XML shows each twice only as video+link track entries). None is in the same scene as clip A or B (pic 4 left out). Source recorded in pictures-tags.md for all 10. | See b |
| 7 | Music | NOT COVERED | Draft has no music; Zac adds intro/outro and logo card himself. | Send the track names to wwd-rights before export. Owned P:\ library, YouTube Audio Library (attribution line) or paid-plan Suno only. Suno plan is lapsed as of 2026-10-26 per STANDARDS, so Suno = FLAG. A soundalike of a film score or named song = fail. |
| 8 | Sounds | PASS (on paper) | XML lists only files from `P:\Sounds\Sound FX\` plus the in-house stickers. Owned per Zac's note (2026-10-17). I did not listen. | None |
| 9 | AI-made assets | FLAG, disclosure needed | Opener `Opener - Firefly (MP4).mp4` is Firefly-generated footage and was reused from eps 1 and 2 (run sheet stop 1). It is not in the draft XML clip list, so confirm whether it is in the final. If it is, check the YouTube "altered or synthetic content" box. Suno: no Suno track known in this draft. | Zac: tick the AI disclosure box at upload if the Firefly opener is in the export. |
| 10 | Upload package and disclaimer | NOT AVAILABLE | No eps 3 and 4 upload package yet. | When built, disclaimer must be the last section and describe exactly: 2 muted trailer clips (about 3 s), 10 stills for commentary, no music clips from the show. |

## The five handoff questions

**(a) Blurring the Disney+ corner bug.** Blurring is removing a mark, not a license. It does not make a clip fair use and it does not stop Content ID, which matches on picture and audio, not on the logo. The run sheet's own rule is no studio logo, so the blur is consistent with house rules and is better than leaving the bug. Risk of the blur itself: low as far as I can tell. Two cautions: (1) a blur that flickers or slips for a few frames defeats the point, so check it frame by frame; (2) do not describe the clips as anything other than trailer excerpts. The credit and the source (official trailer) should be named in the description. Whether blurring a source mark has any legal weight in a fair use fight is a question I cannot answer. It goes to an attorney if Zac wants certainty.

**(b) AI-looking stills 19, 21, 27.** I cannot confirm from the files whether these are official stills or not. pictures-tags.md says the IMDb stills came with no caption or cast tag, and notes the CDN key is "order-assumed, not independently verified". Source URLs in the tag file are m.media-amazon.com (IMDb image CDN) for 19, 21, 27, and image.tmdb.org (TMDb) for 36, 37, 38. So the stated source is IMDb or TMDb for all ten, but IMDb galleries do not prove a still is an official studio still, and I have not verified that. Status of each in the tag file: 19 and 21 SCENE-MATCH, 27 OK-MEDIUM. Only 38 is labeled official promo art (and it is a TMDb backdrop). I did not open the images, so I cannot say whether they are AI-altered. Not verified. Note the scene itself could be a real show scene set inside an AI mindscape, which would explain a synthetic look. Action: Zac or wwd-pictures opens 19, 21, 27 next to the trailer or an official gallery page and confirms they are real frames from the show. If they turn out to be fan or AI-generated art, drop them (a swap spare is 36, or 35); using non-official art with a caption implying it is the show would add a different problem.

**(c) Trailer total vs 30 s.** About 3.1 s used, against under 30 s total and under 4 s per clip. PASS with a wide margin.

**(d) QA note, not rights.** The StreamYard composite has a stuck burned-in caption on the KingZ tile ("Grandfather is the fun one."). I did not see it in the render, reporting per handoff. Fix before publish.

**(e) Studio names and logos.** Kit pieces show the character name and the actor name as text (AI Tag FRIDAY, AI Tag EDITH). Names as text are not a logo, and naming the cast in commentary is routine. Disney+ corner bug: blurred per Zac (see a). The Next Up end card in the draft is named "Next Up - Vision Quest 5 and 6" (XML). I did not check it for a Disney or Marvel logo. The Vision Quest title text in the Firefly opener is in-house made text. Show title and "Disney+" used in speech and in the description are fine as plain names of the work. Do not put Disney, Marvel or Disney+ logos in the thumbnail or cards.

## What Zac must do
1. Scrub clips A and B once, confirm the blur never slips and no card or logo flashes.
2. Open stills 19, 21, 27, confirm they are real show frames, or swap them.
3. Tell me the intro/outro music before export.
4. Tick the YouTube altered/synthetic content box if the Firefly opener ships.
5. Fix the stuck "Grandfather is the fun one." caption.
6. When the upload package is built, send it for the disclaimer check.

DECISION QUEUED: none. Open legal question for an attorney only if Zac wants it: does blurring a platform watermark on a trailer excerpt change a fair use analysis.
