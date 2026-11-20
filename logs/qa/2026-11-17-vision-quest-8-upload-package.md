# QA report: Vision Quest 8 Upload Package (2026-11-17)
Verdict: FAIL (2 blockers, both small and fixable). Everything else checked passes.

Deliverable: D:\WKP Reports\WWD Upload Packages\Vision Quest 8 Upload Package\2026-11-18 - Vision Quest 8 Upload Package.docx
Source: D:\WKP\WWD\reports\Vision-Quest-8-Upload-Package.md

## Blockers
1. Review gate 1 (social media) skipped for the final shorts copy. Package Section 9 gate log admits the post-devils-advocate rewrite of all five shorts (titles, descriptions, IG and FB captions, Sections 8.4 Shorts 1 to 5) ran through script-room only. copywriting and social-media were NOT run, and the slop check ran only on the whole file. Disclosed, not silent, but the rule says a skipped gate is a FAIL. Fix: marketing-director routes the five rewritten short copy sets through copywriting and social-media, then reruns slop_check and logs it. If script-room cannot call the desks, the main session runs them.
2. Unverified public claim in the description (Section 2, QUICK ANSWERS line 1): "The hosts also credit Emily Hampshire as Edith." The transcript only has Winter Wolf saying "Emily Hampshire just turns it on" (11:32 to 11:49, a block about a robot character) and names Edith separately at 11:08 and 16:38. No line credits her as Edith. fact-research was not run (gate log says so). Bettany as Vision and Spader as Ultron are likewise inferred from loose mentions (15:10, 04:21, 18:00). Fix: send the three cast claims to fact-research, or cut the cast line from the public description.

## Checks passed
- docx equals md: all content lines present; only differences are list numbering and "->" arrows. No @@, no em or en dashes in docx or md. slop_check on md: clean, exit 0 (mechanical only).
- Tag line: 489 characters (recounted, in docx and md). In 450 to 500.
- Hashtags: exactly 5 in description and Section 4, none channel-branded.
- Chapters: 14 lines, first is 00:00:00 - Start, all gaps over 10 s, every time lands on a block start in the final transcript (00:15, 01:44, 02:55, 05:43, 08:14, 10:03, 12:31, 13:55, 15:17, 16:17, 18:21, 21:12, 22:39). Chapter topics match the lines (hat at 05:43 of hat discussion lines 363 to 371, Edith at 16:38, post-credits at 18:21, second spoiler warning at 18:26).
- CC BY-SA line: byte-identical to Rights Note, appears once in md and once in docx, inside the description block.
- Cards: exactly 3, 01:05, 01:50, 02:35, card 3 FrostCast. All four video IDs (YWRdI5A_cdw, 7B1LJmhfOYM, kYsixGzX3PQ, s9tvpaPKDBA) are in video-inventory.md with matching titles. Card 1 and card 2 times fit the spoken lines (00:54 to 01:16, 01:44 to 02:03).
- ffprobe: 1666.90 s, 1920x1080, 30 fps, H.264, AAC 48 kHz stereo, 3,502,818,596 bytes. Re-measured ebur128: -21.2 LUFS, LRA 7.8, true peak +0.1 dBFS. All match.
- Frames at 27:40 and 27:44 show the Thanks for watching card with Subscribe graphic and two empty boxes, so the end-screen plan in Section 7 fits.
- Short in and out points match the transcript: Short 1 hard out 00:38:04 (verdict starts 38:06), Short 2 out before "because I don't think", Short 3 15:17:25 to about 16:15 ("Get the coordinates on the record" before "But it was at that reunion bit"), Short 4 12:31:27 to 13:14:15, Short 5 about 05:50 to 06:54:07 ending "I loved that part."
- No score in copy (hosts say "nine, nine and a half" at 24:56, copy omits it). No verdict in title, opening, FB, IG or Short 1 and 2 copy. The only verdict before 02:55 is spoken at 00:38 and kept out of the copy.
- Order: Title, Description, Tags, Hashtags, Thumbnail, Cards, End Screen, one Post Sequence (3 time options per item), Flags, Fair Use last. Fair use block is the last section.

## Notes (none block)
1. Order of the locked upload format: "BEFORE YOU UPLOAD" box and a "Header" section sit ahead of Title. The lock says the package runs in upload order starting at Title. Check whether earlier shipped packages carried the same header. If Zac wants Title first, move them below Fair Use or into Flags.
2. Spoiler timing: package says the countdown ends at 03:03. Transcript shows "You've been warned" in the block ending 03:05:03, with the lead-in at 02:43 to 02:55. Chapter 4 at 02:55 is the countdown, not the first spoiler. Harmless, but "spoilers start at 02:55" in copy is about 10 s early, which errs safe.
3. Teaser rule, description chapters: titles after 02:55 (Tommy and Billy brothers hug, hat ending, Ultron Learns Loss, Multiverse of Madness footage) are not SPOILER-labelled in the chapter list. WHAT WE COVER bullets are labelled. Consider prefixing or softening. Chapter 4 title "Who Dies And Who Was The Client?" hints at a death.
4. Short 4 audio (12:51 to 13:12) says the balcony scene "convinced Vision Ultron could be reached", which is the same plot point the package flags as the heaviest spoiler in Short 5. Short 4 is labelled "moderate" and posts a day earlier. Consider relabelling or moving the out-point.
5. Short 3 audio has Winter Wolf saying "That was my only nitpick" while a second nitpick appears at 21:12. Package already forbids "the only nitpick" in captions; the audio itself is the conflict.
6. "Ultra Vision" and "Terry" credit spellings: package flags both for a listen at 06:05. Still must be resolved before upload (description and chapter 5 use "Ultra Vision").
7. Fix-list line "find Jennifer (12:20)" is about 12:01 to 12:20 in the transcript; at 12:20 the name is "Lisa". Cosmetic.
8. Video not upload-ready on loudness: -21.2 LUFS and +0.1 dBFS true peak. Package says so (Before You Upload item 5). Hold the upload until re-export or Zac accepts it.
9. Card 3 points to EP 118 while EPs 119 and 120 exist; inventory is stale since 11-03. Disclosed in package, needs Zac's Studio check.
10. Open rights flags (pictures 14, 20, 21, 23, 24, 27, 28, sound licenses, AI box) are Zac's and are disclosed honestly. Not re-audited here.
11. Layout (print-readiness): docx is US Letter with 1.25 inch side margins, tables present, Consolas for code blocks. Could not render pages: no LibreOffice or Word converter here (NOT AVAILABLE: soffice). Page count and visual wrap not seen.
12. qa-media was not routed separately; media checks above were run directly (ffprobe, ebur128, two frames).

---

# RECHECK (second pass), 2026-11-18
Verdict: PASS WITH NOTES. Both 2026-11-17 blockers are cleared. No new blockers. Notes below, none block shipping to Jarvis, several should be fixed before Zac posts.

Scope: upload package docx and md, shorts titles and captions docx and md, five built shorts, cover PNGs, AUDIO mp3. Documents, claims and media checks were run directly by qa-director (no separate bench agents were spawned).

## Blocker recheck
1. Gate skipped on shorts copy: CLEARED with a caveat. Package Section 9 gate log says marketing-director called both the social-media and copywriting desks on all five sets. Their outputs exist on disk (D:\WKP\scratch\vq8-shorts-socialmedia.md, vq8-shorts-copywriting.md). slop_check on both md files: clean, exit 0, mechanical only. Caveat: marketing-director hit a rate limit before its final pass, so wwd-director picked the copywriting set and made the last edits. The marketing judgment pass is therefore missing, and the package says so honestly. Recommend a marketing-director read of the five sets before Zac posts.
2. Unverified cast claim: CLEARED. The line now reads "The hosts single out Paul Bettany and James Spader by name, and they praise Emily Hampshire's Edith scene." Checked against the final transcript: "Paul Bettany is a gene" (15:10), James Spader named at transcript lines 83, 87, 131, 391, 423, and at 11:08 to 11:49 Winter Wolf talks about Edith and the Paladin and says "Emily Hampshire just turns it on in that moment". Supported.

## Document checks
- Docx equals md for both documents: every md line is found in its docx (list markers aside). Zero em or en dashes in docx and md. No placeholders. Delivery copies in D:\WKP Reports\WWD Upload Packages\Vision Quest 8 Upload Package\ and the episode-folder copies are byte-identical (md5 match, md and docx).
- Section order: BEFORE YOU UPLOAD box and Header, then 1 Title, 2 Description, 3 Tags, 4 Hashtags, 5 Thumbnail, 6 Cards, 7 End Screen, 8 Post Sequence, 9 Flags, 10 Fair Use last. Locked order holds after the preface (same note as pass one).
- Hashtags: exactly 5 in the description and in Section 4, none channel-branded. Tags: 489 characters (recounted). Chapters: 14 lines, first is 00:00:00 - Start. Cards: exactly 3, all before 3:00, card 3 FrostCast. Titles 60, 58, 61 characters.
- No score in any copy (hosts say "nine, nine and a half" at 24:56, copy omits it). The only verdict before the spoiler warning is spoken at 00:38 and is kept out of every copy block. Teaser rule holds.
- Spoiler labels: shorts 3, 4, 5 titles, descriptions and captions open with SPOILER. The pass-one note on unlabelled chapter titles is addressed by the added line "Chapter titles from 02:55 on contain spoilers." Spoiler start is described as 02:55 with the countdown end at about 03:05 (matches the Premiere file). Handles only, no real names.
- Layout and print-readiness: US Letter, 1.25 inch side margins (read from the file). NOT AVAILABLE: a docx renderer (no LibreOffice or Word converter), so page count and visual wrap were not seen.

## Media checks (ffprobe, ffmpeg ebur128, frames pulled and viewed, own transcription of each finished clip's audio with faster-whisper small)
| Clip | Res / fps / audio | Duration | LUFS | True peak | Source in/out |
|---|---|---|---|---|---|
| 1 | 1080x1920, 30, AAC 48k stereo | 23.25 | -16.8 | -1.5 | matches |
| 2 | same | 34.15 | -14.4 | -1.3 | matches |
| 3 | same | 56.45 | -15.0 | -1.4 | matches |
| 4 | same | 42.55 | -14.7 | -1.4 | matches |
| 5 | same | 24.85 | -14.8 | -1.5 | matches |

All five match the expected specs. Each clip opens on its cover image (frame 0) with the hook text, then burned captions on a blurred background over the two-host layout. Cover PNGs exist for all five. AUDIO\Vision Quest Ep 8.mp3: 192 kbps, decodes to 1666.90 s, matches the video.
- Short 1: audio ends on "...this would be a good wrap up?" then near silence. The verdict ("Dude, this is a solid wrap up", source 38.2 s) is NOT in the clip. Pass.
- Short 5: audio runs from "I thought the best part of this show was their clever reinterpretation of WandaVision" to "very much old 80s sitcom and I loved it." The how-Vision-reaches-Ultron lines (source about 06:32 to 06:52) are gone. Pass.
- Short 3 ends on "get the coordinates on the record", before the "solid" line. Short 2 ends on "let us know in the comments". Pass on both.
- Short 2 caption gaps (disclosed): about 20.5 to 21.3, 22.4 to 23.5 and 26.5 to 28.7 s of the clip have no caption. The last gap is 2.2 s of speech with no words on screen. My independent hearing of that stretch was "...the very end of the 50/50 with the coin toss. Ultron, be good. 50/50, a coin." (small model, not certain), offered only as a starting point for Zac's listen.
- Short 3 and 4 profanity is in audio and in burned captions as disclosed (Short 4: "Luke Vader shit"). Matches the WWD no-bleep rule.

## Notes (none block)
1. Short 4 caption and ending: the last caption "IT WAS" is held from 40.43 to 42.46 s, but the audio there is "Same thing." and the clip stops right where "It was great" would start. The package says it ends on "Same thing. It was great." The file does not. Fix: drop the caption "IT WAS" (or extend the out point to the end of "great", source about 794.5 s) and correct the package text.
2. Short 1 caption: the last caption "GOOD WRAP-UP DUDE" (22.22 to 23.19 s) shows "DUDE", the first word of the hosts' verdict line, with no matching sound (audio is silent there). Not a verdict leak, but remove "DUDE" so the burned text matches the audio, and drop it from the package's "Ends on" line.
3. Spoiler ordering is now inverted. Short 5 is labelled "heaviest" and posts last, but after the trim it no longer says how Vision reaches Ultron. Short 4 audio still carries "that scene convinced Vision Ultron could be reached" and the Luke and Vader line, so Short 4 is now the heavier. Fix the labels or swap the post order (Short 5 before Short 4).
4. Short 5 burned caption reads "ULTRA VISION" (7.4 to 9.2 s). The spelling is still unverified (item 8 of the BEFORE YOU UPLOAD box). If Zac's listen at 06:05 says "Ultron Vision", the clip needs a re-render. Do this before posting.
5. Short 5 copy says "the hosts reach for Full House" and the Facebook caption says "KingZ is along for the ride". Only Winter Wolf speaks in that clip. Change to Winter Wolf and drop the KingZ clause.
6. Short 3 audio opens with "But" before "I like the part" (package says it opens on "I like the part"). About 0.2 s, harmless.
7. Short 1 has a brief dissolve at about 3 s of the clip (source about 17.8 s) showing the series poster with "October 14" and the Disney+ logo over the host cams. It comes from the final cut itself. The rights note flags a Disney+ mark on picture 28 only. Ask wwd-rights whether this poster is a tracked picture.
8. Still open from pass one, all disclosed: short covers need their own rights check, open rights flags (pictures, sounds, AI box), full-export loudness -21.2 LUFS and +0.1 dBFS peak (not re-measured this pass), stale card 3, the Ultra Vision listen. These are Zac's items.
9. The Header and BEFORE YOU UPLOAD box still sit ahead of Title (pass-one note 1, unchanged).

## Not verified
- Rendered look of the docx pages (no converter).
- Full-export loudness and picture-by-picture rights (taken from pass one and the package, not re-run).
- Clip audio tails were checked by an independent small-model transcription, RMS levels and caption timing files, not by a human listen. A word at a cut edge could differ.
- Whether anything is posted or scheduled: not checked, the package says nothing is.
- Marketing-director judgment pass on the shorts copy: it did not happen (rate limit), per the package.
