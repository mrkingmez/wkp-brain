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

FROSTCAST
Weekly podcast, Wednesdays 9pm. News, trailers, books, games in the same space.

Currently at **episode 106** (recorded Wednesday, August 5, 2026). Episode 100 was recorded live in Worcester, MA — the first time Zac and Matt saw each other in person in over 20 years. Worth referencing in show framing/promo where relevant.

Recording is every Wednesday 9-11pm, scheduled on the Winter Wolf's Den calendar through episode 114 (Sep 30, 2026). This line should be bumped by 1 automatically the Thursday after each scheduled Wednesday slot, assuming the recording happened as planned — flag it here and to Zac if a week's recording didn't happen on schedule instead of silently bumping the count.

**Source video location convention:** every episode's raw download lives at `L:\Winter Wolfs Den review show\Frost-Cast\EP <number>\`, confirmed consistent back through EP 1. When Zac says an episode is downloaded, look in that episode's folder for the video file — no need to ask for the full path.

**Cold open:** a new cold open replaces the current one starting around **episode 110** (roughly early September 2026). This is the FrostCast cold open — distinct from the Den Files cold open template, do not confuse the two.

FrostCast Intel briefing docs in this folder are the prep format.

RETRO WATCH
Rewatching childhood movies to see if they hold up.

THEMED MONTHS
For example, November military month in honor of veterans.

DEN FILES
Internal name for the series pitched externally as "Story Behind the Story." Deep dive into the true events that inspired a movie versus what the movie actually showed.

Episode 1 — Fire in the Sky (Travis Walton case), script already drafted in this folder. Key angle: Travis Walton has said publicly his actual abduction experience was more like a healing encounter — beings noticed he was hurt and were trying to help him — but the 1993 movie reframed it as straight horror, which reportedly upset him. The hook: contrast what Walton actually described versus the horror treatment Hollywood gave it. Structure: lead with the real account, then show how/where the film diverged. Targeted for release ~August 2026.

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
- wwd-video-upload-package — full upload package from a transcript: SEO title, description, chapters, backend tags, hashtags, Facebook and Instagram posts with Adobe Firefly image prompts, end screens and cards, posting schedule. Bakes in TubeBuddy SEO compliance targeting 75-85%+. Trigger on "full run" or "full upload package."
- wwd-shorts-clip-factory — cuts actual clip files with ffmpeg plus per-clip captions and staggered posting schedule: YouTube first, Instagram +45 minutes, Facebook +90 minutes, one clip per day. Requires local file and ffmpeg access, so Cowork rather than chat.

## Working Notes
- **"The episode is downloaded" trigger:** when Zac says this, locate the video in `L:\Winter Wolfs Den review show\Frost-Cast\EP <next episode number>\` (using the tracked episode count above), run wwd-video-transcriber's extract + transcribe steps automatically, then read the finished transcript and hand back chapter-break timecodes. There is no separate automated chapters tool yet — chapter breaks are identified by reading the transcript directly and judging topic shifts, not a deterministic script. If a dedicated wwd-frostcast-chapters skill shows up later, prefer it over manual reading.
- This is a two-person show. Anything affecting format, schedule, or branding is a joint decision with Matt, not a solo call.
- FrostCast is weekly and recurring. It does not stop for other projects.
- Den Files episodes require real historical research, not summary. Sourcing matters the same way it does for Watershed.
- FrostCast has been inactive on the audio/podcast side for ~18 months even while the show continued — relaunch strategy is a "We're Back" episode cross-posted to YouTube and audio simultaneously.

## Open
[FILL IN — new FrostCast cold open: written? recorded? needs building before ep 110]
[FILL IN — Den Files topic queue beyond episode 1, once selected from the pipeline candidates above]
[FILL IN — podcast host platform decision, flagged as open in TASKS.md]
[FILL IN — Spotify metadata fix, flagged as open in TASKS.md — brand name typo "Winters" vs "Winter," inconsistent episode title formatting]