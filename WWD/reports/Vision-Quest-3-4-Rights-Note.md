# Vision Quest (Disney+ series, eps 3 and 4) - Rights Note (DRAFT cut)

Date: 2026-10-28. Author: wwd-rights. Reports to wwd-director.
**This is a risk flag, not legal advice. Fair use is decided case by case, and a Content ID claim or copyright strike can still happen even on a clean cut. Nothing here promises otherwise.**

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
