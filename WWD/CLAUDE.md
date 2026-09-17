@../ME.md
@../projects.md

# The Winter Wolf's Den (WWD) / FrostCast

## What This Is
The one collaborative venture. Run with co-host Matt (Winter Wolf), a close friend since 1992. Zac goes by KingZ. Covers the "nerd-verse" — MCU, DCU, sci-fi, fantasy, horror.

## Host Voices — keep these distinct in every script
- MATT (Winter Wolf) — sharp, verdict-first. Delivers the call, then defends it.
- ZAC (KingZ) — warm and connective. Frames topics, carries community callbacks, brings the audience in.

Do not blend these. The contrast is the show.

## Content Lines

REVIEW VIDEOS
Movies and shows in the nerd-verse. Tone benchmark is the Spider-Noir review: gritty, noir-influenced, direct, authentic. Not corporate, not sanitized.

**No bleeping — locked 2026-09-12.** On-air profanity ships as recorded, never bleeped or cut. Applies to every WWD content line (reviews, FrostCast, Den Files, Retro Watch, shorts). Do not flag profanity as something needing a bleep in upload packages going forward.

FROSTCAST
Weekly podcast, Wednesdays 9pm. News, trailers, books, games in the same space.

Currently at **episode 106** (recorded Wednesday, August 5, 2026). Episode 100 was recorded live in Worcester, MA — the first time Zac and Matt saw each other in person in over 20 years. Worth referencing in show framing/promo where relevant.

Recording is every Wednesday 9-11pm, scheduled on the Winter Wolf's Den calendar through episode 114 (Sep 30, 2026). This line should be bumped by 1 automatically the Thursday after each scheduled Wednesday slot, assuming the recording happened as planned — flag it here and to Zac if a week's recording didn't happen on schedule instead of silently bumping the count.

**Source video location convention:** every episode's raw download lives at `L:\Winter Wolfs Den review show\Frost-Cast\EP <number>\`, confirmed consistent back through EP 1. When Zac says an episode is downloaded, look in that episode's folder for the video file — no need to ask for the full path.

**Cold open:** a new cold open replaces the current one starting around **episode 112** (roughly mid-to-late September 2026) — pushed 2 weeks from the prior ~episode 110 / early-September target, Zac's call 2026-09-01. This is the FrostCast cold open — distinct from the Den Files cold open template, do not confuse the two.

FrostCast Intel briefing docs in this folder are the prep format.

RETRO WATCH
Rewatching childhood movies to see if they hold up.

THEMED MONTHS
For example, November military month in honor of veterans.

DEN FILES
Internal name for the series pitched externally as "Story Behind the Story." Deep dive into the true events that inspired a movie versus what the movie actually showed.

Episode 1 — Fire in the Sky (Travis Walton case), script already drafted in this folder. Key angle: Travis Walton has said publicly his actual abduction experience was more like a healing encounter — beings noticed he was hurt and were trying to help him — but the 1993 movie reframed it as straight horror, which reportedly upset him. The hook: contrast what Walton actually described versus the horror treatment Hollywood gave it. Structure: lead with the real account, then show how/where the film diverged. Targeted for release 1 October 2026 (locked 26 Aug 26).

The cold open template from the Episode 1 script is reused every Den Files episode; keep it consistent. (Again — this is the Den Files cold open, not the FrostCast one.)

Series pipeline beyond Episode 1 (not yet scripted): The Conjuring franchise, other "based on true events" found-footage horror, Texas Chain Saw Massacre. Selection criterion: films that market themselves as "based on a true story" where the true story is meaningfully different from the film.

Cadence: releases roughly every 6 weeks once launched. Separate video series from FrostCast, not woven into the Wednesday podcast slot. Explicit secondary purpose: testing audience appetite for this longer-form deep-dive format before committing further.

Workflow: Zac leads research/writing since it's his concept; Matt reviews everything Zac sends over before it's finalized. Not an even split on this series specifically (contrast with the general show, which is run as a joint decision-making venture).

No dedicated TV/streaming series review format planned right now — considered, but channel analytics don't support it currently. Standard movie reviews continue (e.g. Spider-Man: Brand New Day and others in the pipeline).

## Shorts and Reels — Opus Clip Prompt System v2.1
The clip extraction spec lives in this folder and is authoritative. Core rules:
- First-three-words hook test — the opening must hook in the first three words or the clip is rejected
- On-screen hook text required per clip
- Mid-clip retention beat required
- Ending plus loop rule — the clip must end in a way that loops back
- Every candidate clip scored 1 to 10; only elite clips ship
- 5 to 7 clips per source video

## Related Skills
- wwd-video-transcriber (`skills/wwd-video-transcriber/` in this repo) — turns a downloaded episode video into a diarized, speaker-labeled transcript. Requires one-time setup (Python/ffmpeg/torch — done on the Main Desktop machine as of Aug 2026) and voiceprint enrollment for Matt/Zac/Gabby (not yet done — currently runs with everyone labeled Guest/Unknown until enrolled). Standing rule: the output transcript always saves into the same EP folder as the source video, never a separate outputs/transcripts location — overrides the skill's own doc default.
- wwd-review-pipeline — replaces the old wwd-video-upload-package / wwd-shorts-clip-factory names (2026-09-04, those never existed as real skills — see decision WWD-2026-08-31-01). Real installed skill now: reads the Premiere transcript for a finished review, produces the full upload package (SEO/GEO title, description, chapters, backend tags under 500 characters, hashtags, thumbnail concept, cards, end screen, FB/IG posts, posting schedule), extracts audio-only to `\AUDIO`, cuts vertical Shorts/Reels to `\shorts`, and writes per-clip titles/captions. Trigger on "I just finished [title]," "run the review pipeline on [title]," "work up [title]."
- wwd-broll-prep (`skills/wwd-broll-prep/` in this repo) — turns a mixed-source B-Roll folder (screenshots, posters, clippings, Google Images grabs) into numbered, frame-ready 1920x1080 PNGs in a `USE\` folder, sequenced to match the episode/review script. Works for Den Files and standard review videos. Local Pillow script, not the Adobe connection — Adobe's batch tools cap around 20 files and can't auto-upload local files. Trigger on "resize the B-Roll" / "get these images ready for the edit."

## Working Notes
- **Shorts posting task + reminder — LOCKED 2026-09-15.** Any time `wwd-review-pipeline` (or any other WWD workflow) cuts shorts/Reels for a review or episode, two things happen the same session, automatically:
  1. Add a row to TASKS.md: "Post [title] shorts" under WWD, deadline 3 days out from the cut date, status Not Started, noting where the clips live (`\shorts\` folder path) and the manifest file. If the shorts are on hold for re-trim or another block, note that instead of a deadline and skip step 2 until they're actually postable.
  2. Set a one-time reminder (via the `schedule` skill/CronCreate) for that same deadline to check whether the task got marked Done. If it did not, flag it back to Zac rather than silently rescheduling or dropping it.
  This closes the loop that shorts get cut but posting itself is a manual, easy-to-forget step — see the still-open Whisper Man and EP103 shorts in TASKS.md as the pattern this is meant to stop.
- **Show prep picture location — LOCKED 2026-09-15.** The Tuesday planning meeting topic-list photo (input to `wwd-show-prep`) now lives at `L:\Winter Wolfs Den review show\Frost-Cast\FrostCast Show docs\Pictures\`, named `Frostcast EP <n>.<ext>`, one per week, incrementing by episode number — starts at EP 112 (2026-09-15). Replaces the skill's old default input path `D:\WKP\WWD\prep\`.
- **Weekly output save location — LOCKED 2026-09-16, REVERSES the 2026-09-15 "WWD Social" rule.** Zac does not want a separate top-level social folder — everything for a given week saves inside that week's own folder (`L:\Winter Wolfs Den review show\<YYYY-MM-DD> Week of <Mon DD>\`), matching the structure of `2026-08-10 Week of Aug 10\` (`01 Images`, `02 Thumbnails`, `03 Transcripts`, `04 Upload Packages`, `05 Social Copy`, `_TODO.md`), which he explicitly holds up as the output he likes. This applies to every weekly social calendar package (`WWD_Weekly_Social_Calendar_YYYY-MM-DD` .md/.docx, whether built by `wwd-weekly-planner` or by marketing-director/social-media) — it saves into that week's `05 Social Copy` folder, never into a standalone `WWD Social\` folder. The `WWD Social\` top-level folder is retired; do not create new files there. The 2026-09-14 week's files already sitting in `WWD Social\` and `Sponsors\Surfshark\` stay put (Zac's call 2026-09-16 — fix going forward, not retroactively) — only new weekly builds follow this rule. The full weekly build package (`WWD_Weekly_Package_YYYY-MM-DD.docx`, bundling social copy with polls/shorts/growth notes/cold-open check-in) already followed this correctly and is unaffected — it stays in its week folder's `04 Upload Packages`.
- **Outstanding shorts reminder in the Sunday build — LOCKED 2026-09-16.** Every Sunday-night `wwd-weekly-planner` run checks TASKS.md for any "Post [title] shorts" rows (created per the Shorts posting task + reminder rule above) still marked Not Started or Blocked, and adds a short checklist section to that week's `WWD_Weekly_Package_YYYY-MM-DD.docx`/`.md` listing each one — title, where the clips live, and the deadline. Reminder only; do not copy or move the actual clip files.
- **"The episode is downloaded" trigger:** when Zac says this, locate the video in `L:\Winter Wolfs Den review show\Frost-Cast\EP <next episode number>\` (using the tracked episode count above), run wwd-video-transcriber's extract + transcribe steps automatically, then read the finished transcript and hand back chapter-break timecodes. There is no separate automated chapters tool yet — chapter breaks are identified by reading the transcript directly and judging topic shifts, not a deterministic script. If a dedicated wwd-frostcast-chapters skill shows up later, prefer it over manual reading.
- This is a two-person show. Anything affecting format, schedule, or branding is a joint decision with Matt, not a solo call.
- FrostCast is weekly and recurring. It does not stop for other projects.
- Den Files episodes require real historical research, not summary. Sourcing matters the same way it does for Watershed.
- FrostCast has been inactive on the audio/podcast side for ~18 months even while the show continued — relaunch strategy is a "We're Back" episode cross-posted to YouTube and audio simultaneously.

## Open
[EP 106 transcript blocked mid-run — see TASKS.md for full status and the exact resume command. Everything is debugged and working (script, HF licenses, GPU/CUDA); it just needs the actual run repeated after Zac's computer restart.]
[FILL IN — new FrostCast cold open: written? recorded? needs building before ep 110]
[FILL IN — Den Files topic queue beyond episode 1, once selected from the pipeline candidates above]
[DECIDED 2026-09-04 — podcast host staying on Spotify for Creators (free) for now]
[FILL IN — Spotify metadata fix, flagged as open in TASKS.md — brand name typo "Winters" vs "Winter," inconsistent episode title formatting]

## Writing room

Script craft belongs to the writing room, not to this venture. For any
scripted segment - Den Files cold open, character expose, FrostCast bit -
call script-room rather than drafting here. Pass the format spec path so
the room writes to spec.

devils-advocate still owns format compliance. originality owns whether the
idea is derivative. They are different checks and both run.
