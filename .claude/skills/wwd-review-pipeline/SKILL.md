---
name: wwd-review-pipeline
description: >-
  End-to-end Winter Wolf's Den review video pipeline. Triggered when Zac/KingZ says he
  finished a review video for a named film or show. Locates the movie folder under
  L:\Winter Wolfs Den review show\Raw Footage, reads the Adobe Premiere Pro transcript,
  and produces the complete upload package (SEO/GEO title, description, chapter list,
  backend tags under 500 characters, hashtags, thumbnail concept, cards, end screen,
  Facebook and Instagram posts, posting schedule), extracts an audio-only version to
  \AUDIO, cuts vertical Shorts/Reels to \shorts, and writes a per-clip title and caption
  document for YouTube, Instagram, and Facebook. Trigger phrases include "I just
  finished [title]", "run the review pipeline on [title]", "work up [title]",
  "review pipeline", "cut shorts for [title]".
---

# WWD Review Video Pipeline

Full pipeline for a Winter Wolf's Den review video, from finished Premiere export to
ready-to-paste upload package plus cut Shorts.

**This skill needs real local filesystem access, ffmpeg, ffprobe, and Python.** It runs
in Claude Code or Cowork. It cannot run in plain claude.ai chat.

---

## 0. Trigger and Inputs

**Trigger:** Zac names a film or show and says he finished the review video for it.
Examples: "I just finished Weapons", "run the review pipeline on Predator Badlands",
"work up The Long Walk for a review."

**Only required input:** the movie title.

**Optional input:** an explicit folder path. If Zac gives a path, use it and skip the
search in Section 1.

**Do not ask clarifying questions before starting.** Locate, verify, and run. Surface
anything ambiguous in the Flags section of the finished package, not as a blocking
question up front. The only reason to stop is a missing transcript or a missing video
file, both covered in Section 1.

---

## 1. Locate the Project Folder

Default root:

```
L:\Winter Wolfs Den review show\Raw Footage
```

The movie folder is often nested one level deep inside a recording-session folder
(example: `Raw Footage\Mass recording 30 Aug\Good Boy (2025)\`). Search recursively,
do not assume it sits at the root.

**Matching rules:**
- Match case-insensitively on the movie title.
- Tolerate a trailing year in parentheses: `Good Boy (2025)` matches "Good Boy".
- Tolerate punctuation differences (colons, apostrophes, ampersands vs "and").
- If the `L:` drive is unreachable, say so once and stop. Do not silently fall back to
  a local path for this pipeline, the source video has to be real.
- If two or more folders match, list them with their last-modified dates and let Zac
  pick. Do not guess.

**Inventory the folder before doing anything else.** Log to the package:
- The transcript file (Premiere export, usually `.txt`, sometimes `.srt` or `.csv`).
- The finished video export (usually a single `.mp4`).
- Any `USE\` folder from a prior `wwd-review-photo-pull` run.
- Any raw dual-stream files (`.m4v` + `.aac`).

**Hard rules on source selection:**
- **Always cut Shorts from the finished single-file `.mp4` export.** Never from raw
  `.m4v` / `.aac` pairs. Those are bare elementary streams with no container timestamps
  and no audio track, and they have broken this pipeline before.
- **Check whether Premiere or Media Encoder is still writing.** If a `._00_` or similar
  temp file exists alongside the `.mp4`, or if `ffprobe` duration changes between two
  reads 30 seconds apart, the export is still running. Poll until the file size is
  stable for two consecutive checks, then proceed.
- Run `ffprobe` on the final `.mp4` and record exact duration, resolution, fps, and
  audio codec in the package header.

**Stop conditions:**
- No transcript found: stop, say which folder was searched, ask Zac to drop the
  Premiere transcript in.
- No finished `.mp4` found: produce the upload package from the transcript anyway, skip
  Sections 4 through 6 (audio and shorts), and flag it clearly at the top.

---

## 2. Read the Transcript (Whole Thing, No Skimming)

Read the entire transcript before generating a single line of output. Use only the
transcript. No memory of the film, no prior conversations, no invented moments.

### 2a. Timecode format trap, read this every run

Adobe Premiere transcripts export timecode as **MM:SS:FF** (minutes, seconds, frames),
not HH:MM:SS. A 16 minute video will show a line at `12:51:25`, which is 12 minutes
51 seconds and 25 frames, not 12 hours.

Convert to seconds before any ffmpeg call:

```
seconds = MM*60 + SS + (FF / fps)
```

Pull `fps` from ffprobe on the actual export (WWD reviews are 30fps). Verify the
conversion by checking that the last transcript timecode lands within a few seconds of
the ffprobe duration. If it does not, the assumption is wrong, stop and say so.

Chapter markers in the description use **HH:MM:SS**, converted from the above.

### 2b. Speaker audit, do this before writing any host-specific line

Multicam review transcript mapping when diarization is present:
- Speaker 1 = Matt / Winter Wolf
- Speaker 2 = Zac / KingZ
- Speaker 3 = Gabby / Oracle
- Speaker 4 and up = guest or other crew

**If every line reads the same speaker label, there is zero diarization.** In that case:
- Attribute nothing to a specific host anywhere in the package.
- Never write "the two hosts" for a back-and-forth, it may be one host self-correcting.
- Put an ATTRIBUTION FLAG block at the top of the package saying so.

### 2c. Extraction pass

Pull and hold before writing:
- Total runtime.
- Primary franchise / IP / film keywords.
- The 5 to 10 most repeated phrases.
- Every major topic shift in chronological order with its timecode.
- The strongest verdicts, hot takes, disagreements, and surprising facts.
- Which segments got the most runtime.
- Any hard numbers spoken on air (budget, box office, scores, runtimes, dates).
- Any name or term that reads like a transcription garble. Flag it, never publish it.
  Precedent: "grease creature" and a name garbled as "Carrie Fisher" both had to be
  held on the Good Boy run.

---

## 3. Build the Upload Package

Write to the movie folder as `[Movie Title] - Upload Package.md`.

### Package header

Source transcript filename and line count, ffprobe readout of the export, speaker-audit
result, and this line:

```
Voices in all copy: Winter Wolf (sharp, verdict-first) and KingZ (warm, connective).
Handles only. No review score stated. No em dashes.
```

### Section 1. SEO Title

Deliver a **Primary** and one **Alt**, plus two lines on why the primary won.

- Hard cap 100 characters. 60 is display truncation, not a cap. Aim under 70.
- **Primary keyword verbatim in the first 5 words.** Non-negotiable, this is the
  TubeBuddy 80%+ requirement.
- Front-load the film or franchise name. Include the year when the title collides with
  other releases.
- Emotionally charged, never a promise the video does not pay off.
- Include one high-intent phrase: Review, Breakdown, Ending Explained, Honest Take.
- **GEO layer:** the title should read as an answer to a question a person would type
  or ask out loud. "Good Boy (2025) Review: The $70K Horror Movie Filmed From a Dog's
  POV" answers "what is Good Boy about and why does it matter" in one line.

Good: `Good Boy (2025) Review: The $70K Horror Movie Filmed From a Dog's POV`
Bad: `Our Thoughts on the Movie`

### Section 2. Description

Structure, in this order:

1. **Answer-first opening paragraph.** Two to four sentences. Lead with the single
   strongest concrete fact from the transcript. The primary keyword appears verbatim in
   the first sentence. Written so an AI answer engine could lift it as a standalone
   answer to "what is [film] about" or "is [film] worth watching."
2. **Spoiler note**, if the review goes deep on a reveal. Say roughly where it starts
   and give the reader an exit chapter.
3. **QUICK ANSWERS block.** Three to five short Q and A lines pulled from the
   transcript. This is the GEO workhorse, it is what Google AI Overviews, Ask YouTube,
   ChatGPT Search, and Perplexity actually pull from. Format:
   ```
   QUICK ANSWERS
   Is Good Boy actually scary? ...
   How long is Good Boy? ...
   Where can I watch Good Boy? ...
   ```
   Every answer must be a fact stated in the transcript. Never fill a gap from outside
   knowledge without flagging it.
4. **Entity-loaded bullets.** The major discussion topics, using transcript language.
   Named entities carry weight here: film title, director, cast, studio, streamer,
   franchise, year.
5. **One comment-driving question.**
6. **CHAPTERS block.** See Section 3 below.
7. **Hashtags.** See Section 5 below.

Never state a final review score in the description. Tease only.

### Section 3. Chapter List

**The first line is always this literal line, no exceptions:**

```
00:00:00 - Start
```

Then the first real theme-based chapter at the first actual topic shift, and onward.

- Format `HH:MM:SS - Title`, converted from the Premiere MM:SS:FF timecodes.
- Minimum 8, maximum 14 total including the Start line.
- Group by theme, not every small transition. Heavy discussion blocks get more runtime
  before the next marker.
- Chapter titles are answer-phrased and searchable, each one reads like a mini clickable
  episode. `What The Movie Is Really About` beats `More Discussion`.
- Include the IP name in at least the first two or three chapter titles.
- Never invent a timestamp. Every marker traces to a real transcript line.

### Section 4. Backend Tags

Comma-separated, hidden tags. **Target 450 to 500 characters total, hard cap 500.**

Composition:
- Exact-match short phrases only. No descriptive sentences as tags.
- Standalone tags for: film title, film title + year, actor name, character name,
  director name, franchise, studio or streamer, year.
- IP + review / recap / breakdown / ending explained combinations.
- Long-tail variations a real person would type.

**Verify the character count with Python before writing it into the package.** Do not
eyeball it. Do not estimate.

```python
tags = "tag one, tag two, tag three"
print(len(tags))
```

Print the verified count into the package: `(Verified: 487 characters.)` If it lands
outside 450 to 500, cut the lowest-intent tags and re-count until it fits. Log what was
cut and why.

### Section 5. Hashtags

Eight to ten hashtags for the description, on-video use, and socials.

- 2 franchise / IP anchors
- 2 to 3 search-intent drivers (Review, Breakdown, HonestTake, EndingExplained)
- 2 to 3 broad community magnets (HorrorCommunity, MovieReview, IndieHorror, SciFi)
- Year or genre tag where it fits

**Never use #WinterWolfsDen.** The channel is too small for a branded tag to carry any
weight, it wastes a slot. (The Good Boy package used it. That was wrong, do not copy it
forward.) `#FrostCast` is fine on FrostCast content only, not on review videos.

### Section 6. Thumbnail Concept

- If a `USE\` folder exists from `wwd-review-photo-pull`, reference the actual filenames
  and say which image goes where. One poster only, never two poster-style key arts.
- Give a concrete composition: base image, secondary image, text stack with the actual
  words baked in, color grade.
- **Text must be real text, never a blank placeholder banner.**
- Pull the text stack from the strongest number or verdict in the transcript.
- Never state a review score on the thumbnail.

### Section 7. Shorts Candidates

Full scoring detail per clip. See Section 5 of this skill for the selection criteria and
Section 6 for what gets written. This section of the package holds the reasoning: source
timecode, first three spoken words, hook assessment, on-screen text, mid-clip retention
beat, ending and loop assessment, 1 to 10 score, and ship or hold verdict.

### Section 8. Facebook Post

- Opening line is a hook built on the strongest concrete fact.
- 3 to 5 sentences. Facebook gets more crew storytelling and breathing room.
- One direct question.
- `[VIDEO LINK]` placeholder.
- 3 to 5 hashtags.
- One Adobe Firefly image prompt in brackets. **Firefly prompt format: subject first,
  descriptors second, style keywords last.** No cinematic instruction language. No actor
  likenesses, no logos, no readable text in the generated image.

### Section 9. Instagram Post

- Hook in line one, Instagram truncates after it.
- 4 to 6 lines max, exits quickly.
- Primary keyword and IP name in the first sentence.
- 5 to 8 hashtags, more than Facebook.
- One Firefly prompt, square or vertical, bold and high contrast, negative space at the
  top for a text overlay.

**Never post identical copy across platforms.** Always split.

### Section 10. Cards and End Screen

**Cards:** 2 to 3, placed at natural pause points, with the exact HH:MM:SS timestamp and
a stated destination type (another review on a related film, a playlist, a FrostCast
episode covering the same IP). If the actual destination video cannot be verified, say
so and mark it for Zac or Matt to fill in rather than inventing a title.

**End screen:** last 15 to 20 seconds, starting from the final chapter marker.
- Subscribe element, standard placement
- "Watch Next" tile, most recent review or best-performing related review
- Second tile, relevant playlist if one exists

Flag clearly that channel analytics and current playlist structure are not visible from
this pipeline, so destinations are structural recommendations, not verified links.

### Section 11. Posting Schedule

- **YouTube full review:** 11:00 AM ET on the publish date.
- **Instagram promo post:** +45 minutes.
- **Facebook promo post:** +90 minutes.
- **Shorts:** one per day, YouTube first, Instagram +45 min, Facebook +90 min, starting
  the day after the full review publishes so they do not compete with the main upload.
- V2 follow-up posts on both platforms target the following weekend, using a secondary
  angle from the transcript, never the same angle as V1.

### Section 12. Flags and Production Notes

Everything that needed a judgment call, everything unverified, everything that broke.
Transcription garbles held back. Speaker attribution gaps. Runtime discrepancies between
source files. Numbers spoken on air that do not reconcile with each other. Missing files.
Anything Zac or Matt has to decide.

Be direct here. An unflagged assumption that reaches publish is worse than a long flags
section.

---

## 4. Extract the Audio

Create `[movie folder]\AUDIO\` and extract from the finished `.mp4`:

```bash
ffmpeg -i "Movie Title.mp4" -vn -c:a libmp3lame -b:a 192k "AUDIO/Movie Title.mp3"
```

Verify with ffprobe that the output duration matches the source within 0.5 seconds.
Report the file path and duration in the package.

---

## 5. Select the Shorts

Selection criteria are the **Opus Clip Prompt System v2, Prompt 2 (Review Videos)**
standard, applied by hand here. Every candidate is scored 1 to 10. **Ship at 6 and
above, hold below 6.** Target 5 to 7 keepers. Never fill a quota, five elite clips beat
twelve average ones.

**First-3-words test.** The first three spoken words must contain an IP name, a verdict
word, or an emotional spike. If they do not, the clip is cut or the in-point moves.
Never start on: So / Yeah / I think / Alright / Well, I'm just / Welcome back. On-screen
text is a separate hook layer, it is never a substitute for a weak spoken open.

**Mid-clip retention.** No pause over 2 seconds. No restated sentences. Energy holds or
climbs. A great hook with a dead middle still dies.

**Ending and loop.** Last line is a verdict, punchline, reaction, or debate trigger.
Never mid-sentence, never a trailing thought. When two end points work, pick the one
that loops back to the hook.

**Uniqueness filter.** No two clips repeat the same verdict, the same emotional tone
back to back, or the same scene from a slightly different angle.

**Never include:** intros, outros, sponsor mentions, pure plot summary with no opinion,
dead air, generic agreement, anything needing full-video context, anything where the
active speaker is off camera for the hook or most of the clip.

**Clip types to look for:** strong verdicts, genuine host disagreement, emotional
reactions, "wait, what" moments, sharp criticism of writing or casting or studio
decisions, connections to a bigger industry pattern, predictions, fast humor with a
payoff.

**Block-level timecode limitation.** Premiere transcripts give block-level, not
word-level, timing. If a candidate's in-point needs to land mid-block to fix a soft
open, the pipeline cannot do it accurately. Cut it anyway, then mark it
**HOLD FOR RE-TRIM** with a note on where the in-point should move. Do not estimate a
frame-accurate in-point and call it shipped.

---

## 6. Cut the Shorts

Create `[movie folder]\shorts\`.

**Filename convention:** `clipN_short_slug.mp4`, lowercase, underscores, no spaces.
Example: `clip4_unscripted_good_boy.mp4`

**Padding:** in-point exactly at the hook block start minus 0.3 seconds, out-point plus
1.0 second. Do not pad the in-point wide, it kills the hook.

**Vertical reframe.** Reviews are 1920x1080 multicam. Shorts and Reels need 1080x1920.
Default is a blurred-fill vertical frame that keeps the full 16:9 frame intact and
leaves clean space top and bottom for the on-screen hook text:

```bash
ffmpeg -i "Movie Title.mp4" -ss START -to END \
  -filter_complex "[0:v]split=2[bg][fg]; \
   [bg]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20:5[bgb]; \
   [fg]scale=1080:-2[fgs]; \
   [bgb][fgs]overlay=(W-w)/2:(H-h)/2,setsar=1[v]" \
  -map "[v]" -map 0:a \
  -c:v libx264 -crf 20 -preset veryfast -pix_fmt yuv420p -r 30 \
  -c:a aac -b:a 192k \
  "shorts/clipN_slug.mp4"
```

`-ss` and `-to` go **after** `-i` so they are absolute input timestamps and frame
accurate on a re-encode.

Alternative if a single host fills the frame cleanly and the blur bars look weak, a
center crop:
`crop=ih*9/16:ih,scale=1080:1920`
Only use this when it is confirmed the speaker stays inside the crop. If it is not
confirmed, use the blur-fill default.

**Length caps by platform:**
- YouTube Shorts: 45 to 90 seconds
- Instagram Reels: 30 to 59 seconds, **hard cap 59**, under-60 Reels get pushed to
  wider non-follower audiences
- Facebook Reels: 45 to 90 seconds

If a clip runs over 59 seconds, either tighten it under 59 or tag it YouTube and
Facebook only. State which in the manifest.

**Verify every cut file with ffprobe.** Confirm duration, 1080x1920, and that an audio
stream is present. ffprobe confirms ffmpeg cut the requested length, not that the
content inside is good, so every clip still needs an eyeball pass.

---

## 7. Write the Shorts Manifest

Write `shorts\shorts_manifest.txt`.

Header block:
- Source file full path, its duration, resolution, fps, audio codec
- Cutting parameters used
- Which package section holds the scoring detail
- **Ready to post as-is:** list of clip numbers
- **Held for a manual Premiere re-trim:** list of clip numbers, with why
- Attribution warning if the transcript had no speaker diarization

Then one block per clip:

```
N. clipN_slug.mp4 (durations) - READY TO POST | HOLD FOR RE-TRIM
   On-screen hook text: "4 TO 8 WORDS, NAMES THE IP, TEASES THE TAKE"
   YouTube caption: ...
   Instagram caption: ...
   Facebook caption: ...
   Score: N/10.
```

**Caption rules per platform:**
- **YouTube Shorts:** one or two punchy lines, front-loads the film name, 3 to 4
  hashtags. Treat the first line as a title, it shows in the feed.
- **Instagram Reels:** hook line, exits fast, 4 to 5 hashtags including one broad
  community tag. No #WinterWolfsDen.
- **Facebook Reels:** slightly longer, more conversational, more crew voice, hashtags
  optional and no more than 2.

Never identical copy across the three.

**On-screen hook text rules:** 4 to 8 words, names the IP, teases the take, all caps.
Good: `ZERO SCRIPT. 400 DAYS OF SHOOTING.` Bad: `GREAT DISCUSSION`. No clickbait the
clip does not pay off. Never put a review score in it. Never publish a term that is an
unconfirmed transcription garble, use a safe rewrite and flag it.

Footer:
- Posting schedule, one clip per day, YouTube first, Instagram +45 min, Facebook
  +90 min, starting the day after the full review publishes
- Ready clips post first, held clips post only after re-trim and eyeball check

---

## 8. Output Summary

At the end, report to Zac in chat, short:
- Folder used
- Files written, with full paths
- Clip count, split into ready and held
- The top 3 flags, nothing else

Do not restate the package contents in chat. He reads the file.

---

## HARD RULES, APPLY TO EVERY OUTPUT

1. **No em dashes anywhere.** Regular hyphens only.
2. **Handles only in anything public facing.** Winter Wolf, KingZ, Oracle, ReelDon.
   Never a real first or last name in a title, description, caption, post, thumbnail, or
   on-screen graphic. Matt requires this for employment reasons.
3. **Never describe WWD as veteran-owned.** Inaccurate, do not use it.
4. **Never use #WinterWolfsDen.**
5. **Never state a final review score** in a description, caption, thumbnail, or promo
   copy. Tease only.
6. **Chapter output always starts with `00:00:00 - Start`.**
7. **Backend tags Python-verified**, 450 to 500 characters, hard cap 500.
8. **Never invent a timestamp, a quote, a number, or a name.** Everything traces to the
   transcript or to the ffprobe readout.
9. **Flag every transcription garble, publish none of them.**
10. **No scripted host lines.** This pipeline writes copy for the channel, not words for
    the hosts to read on camera.
11. **Markdown output is fine, this is internal.** If Zac asks to send any of it to a
    sponsor, partner, or collaborator, convert to PDF or Word first.
12. **Do not ask permission mid-run.** Execute, then flag.

---

## Reference: Good Boy (2025)

The Good Boy run is the working reference for output shape. Two known deviations to
correct going forward: it used `#WinterWolfsDen` (banned, see rule 4) and its chapter
list opened on `00:00:00 - Good Boy Cold Open` instead of the required
`00:00:00 - Start` line (see rule 6).
