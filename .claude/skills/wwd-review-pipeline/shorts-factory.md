# WWD Review Pipeline, Part 2: Shorts and Reels Factory

Second half of the review pipeline. Part 1 (SKILL.md) produces `[Title] - Upload Package.md`.
This file takes over for: audio extraction, clip selection, cut points, vertical reframe,
burned-in captions, on-screen hook text, cover frame, finished .mp4 files, and the
per-platform captions document.

Supersedes the Shorts sections of the old wwd-review-pipeline and wwd-shorts-clip-factory.
Where they disagree, this file wins. Source: Zac's Part 2 spec, revision 2026-10-14,
adapted 2026-10-14 for local Windows (original targeted a cloud Linux VM). Every rule and
number below is the original's. Commands changed, VM-only limits dropped.

The build is automated by `scripts\build_short.py` (stdlib Python, local ffmpeg). Use it.
Do not hand-assemble ffmpeg chains.

---

## 0. The three rules that changed

**Rule 1: Five clips maximum, and every one ships finished.**
Hard cap of five per review video. Four excellent clips beat five with a weak one.
Every clip that ships is done: framed, captioned, hook text burned in, cover frame
attached, verified. No "HOLD FOR RE-TRIM." No "needs an editor pass." If a clip cannot be
made good, drop it and pick another moment. Shipping four is fine. Shipping a held clip is
not. (Good Boy held three of six and Other Mommy held five of six for the same retired
reason: block-level timecodes cannot resolve a mid-block in-point. Section 3 solves it.)

**Rule 2: Length limits were lifted and the old numbers were wrong.**
The old spec (45 to 90 YouTube, hard 59 Instagram, 45 to 90 Facebook) is out of date. On
Other Mommy two clips at 21 and 24 seconds were tagged "YouTube and Facebook only" citing
the 59-second Reel cap, which is a ceiling, not a floor. They were too short for every
platform. Section 1 has the current limits. Quality is the binding constraint now.

**Rule 3: This is the AI's call.**
Pick the moments, frames, and hooks. Do not queue editorial decisions back to Zac. Two
things this does not authorize:
- A hook the clip does not pay off. Every hook is cashed by what follows it in the next
  ten seconds, or retention dies.
- Publishing an unconfirmed transcription garble, an unreconciled number, or a host
  attribution resting on inferred diarization. Those stay flagged. Use a safe rewrite in
  public copy and note it.

Everything else: decide and move.

---

## 1. Platform specs, current as of October 2026

| Platform | Max length | Resolution | Notes |
|---|---|---|---|
| YouTube Shorts | 3 minutes | 1080x1920, 30 or 60fps | Raised from 60s in Oct 2024. Vertical or square only. The 60s cap now applies only to the in-app camera, not uploads. |
| Instagram Reels | 3 minutes | 1080x1920, 30fps | Raised from 90s on 2025-01-20. Reels over 3 min rarely reach non-followers; under 90s is still the reach advice. Over 90 is not penalized. |
| Facebook Reels | verify before relying | 1080x1920, 30fps | Sources conflict: 90s native, 2 min per upload, "cross-posted Reels honor Instagram length." Assume 90s and check Meta's help page before shipping longer. |

**Working target for WWD review clips: 30 to 75 seconds.** Absolute floor: **20 seconds**
(below that there is no room for a hook, a beat, and a button). The three-minute ceiling is
headroom, not a goal. A review clip needing two minutes is usually two clips or a weak idea.
If a clip must run past 90 seconds, ship it to YouTube and Instagram only and say so in the
captions document.

---

## 2. Selecting the five

Re-derive candidates against the transcript. Score each 1 to 10. **Take the top five that
clear 7.** Fewer clear it, ship fewer. (Floor raised from 6 to 7, a five-clip cap leaves no
room to carry a 6.)

What makes a clip: a verdict stated plainly; genuine host disagreement; a "wait, what"
reveal; sharp specific criticism of writing, casting, effects, or a studio decision; a real
surprise fact; a personal story that lands; fast humor with a payoff.

What never makes a clip: intros, outros, sponsor reads, plot summary with no opinion, dead
air, generic agreement, anything needing the full video to parse, anything where the speaker
is off camera for the hook.

- **Self-contained test.** A viewer with zero context understands the movie, the take, and
  why it matters. If it needs the chapter before it, extend the in-point or drop it.
- **Uniqueness.** No two clips repeat a verdict, an emotional register back to back, or the
  same scene from another angle. Aim for five registers: a verdict, a disagreement, a
  reveal, a story, a laugh.
- **The IP has to appear.** The film's name is spoken in the clip or burned into the hook
  text, ideally both. A clip that never names the movie is unsearchable.
- **First-3-words test.** The first three spoken words carry the hook. Never open on So,
  Yeah, I think, Alright, Well, I'm just, Welcome back.
- **Mid-clip retention.** No pause over 2 seconds, no restated sentences, energy holds or
  climbs.
- **Ending.** Last line is a verdict, punchline, reaction, or debate trigger. Never
  mid-sentence. When two end points work, pick the one that loops to the hook.

---

## 3. Frame-accurate cut points (no Whisper, no human listening)

Premiere exports block-level timing and the strong line is almost always mid-block. Speech
blocks are separated by measurable silences, and the gaps are where a clean cut lives.
Verified detection values for these recordings: **-32dB, 0.28s.** Do not retune without
a reason. (Whisper is not used: Hugging Face model downloads are blocked from the cloud
container the original ran in. Not relevant to local transcription, which is a separate
skill, but do not use Whisper for cut points.)

1. Analyze once per review (maps every silence gap in the finished edit):
   ```
   python scripts\build_short.py analyze --src "<finished edit .mp4>" --out "<scratch>\silence.json"
   ```
2. Snap each clip from the transcript's approximate window:
   ```
   python scripts\build_short.py snap --silence "<scratch>\silence.json" --start <sec> --end <sec>
   ```
   In-point = `silence_end - 0.06`. Out-point = `silence_start + 0.35`. The script prints
   both, or says NO GAP within 3 seconds, in which case widen the window.
3. **Verify the head.** The render QC measures head silence on the finished clip. Clean is
   0.10 to 0.35 seconds. More than 0.5 means the in-point is late and the hook is buried.
   Less than 0.05 means the first word is clipped. Fix and re-render.
4. **Verify the first spoken words** against the transcript block the cut came from. If they
   are So, Yeah, I think, Alright, or Well, the in-point snapped to the wrong gap. Move it
   forward one gap and re-check.

Premiere timecode: the transcript may be `HH:MM:SS:FF` (four fields) or `MM:SS:FF`. Test
the last transcript timecode against the ffprobe duration. If they do not line up the
format assumption is wrong. Stop and say so rather than cutting from bad math.

---

## 4. Audio deliverable

Separate from the analysis file. Create `AUDIO\` in the movie folder:

```
ffmpeg -i "<finished edit>" -vn -c:a libmp3lame -b:a 192k "AUDIO\[Movie Title].mp3"
```

Verify with ffprobe that duration matches the source within 0.5 seconds. Report the path
and duration in the captions document header.

---

## 5. Vertical framing (never center crop)

The multicam edit alternates a full-screen single camera and a two-box side-by-side layout.
A center crop slices both hosts in half whenever the split is up. Not a preference.

Blurred fill, fixed geometry, built into the script: canvas 1080x1920; full 16:9 frame
scaled to 1080x608; overlaid at y=656 (656px above and below); background is a darkened,
blurred, scaled-up copy of the same frame. Hook text lives in the band above the video,
captions in the band below. Nothing covers a host's face.

---

## 6. Burned-in captions (every clip, non-negotiable)

Most feed views are muted. The script builds a per-clip `.ass` and burns it with the
subtitles filter (local ffmpeg has libass). Timing method: take the silence-split speech
spans inside the clip, distribute the clip's words across them proportionally by character
count, group into lines. That lands phrase-level timing, which is what you want. Word-by-
word karaoke is not achievable without word-level ASR and is not worth faking.

Style: 2 to 5 words per line, Poppins Bold 74px, white fill, black outline, no box, all
caps, in the band below the video.

The clip text you pass in is the transcript words actually spoken inside the window.
Mark every uncertain word and use the safe rewrite from the flags, never a garble.

---

## 7. Hook text

Separate layer from captions and from the spoken hook. The spoken open has to be strong on
its own, the hook text reinforces it and is never a patch for a weak open.

- 4 to 8 words, all caps, names the film or the specific claim
- Poppins Bold 86px, white, heavy outline, above the video band
- Visible for the first 3.6 seconds with a short fade, then gone

Good: `ZERO SCRIPT. 400 DAYS OF SHOOTING.` / `THE TRAILER WAS THE BEST PART`
Bad: `GREAT DISCUSSION` / `YOU WON'T BELIEVE THIS`

Never a review score. Never an unconfirmed garble. Never a number the hosts did not settle
on air.

---

## 8. Cover frame

All three composers let you choose a cover, so the reliable play is both:
1. A standalone `clipN_slug_cover.png` (1080x1920) saved beside the clip.
2. The same image prepended as exactly one frame (0.033s at 30fps), so a platform that
   defaults to frame one picks it up. Never prepend a held still of half a second or more,
   that burns the only moment of a Short that reliably gets watched.

The script builds the cover from a real frame inside the clip (`cover_at` seconds into the
clip, default 6) in the same blurred-fill layout, with the hook held large in the top
third and the film tag above the video band. **Look at it.** A frame mid-blink is worse than
no cover. Re-render with a different `cover_at` if it is a bad frame.

---

## 9. Render

One spec file per clip, then render. The script handles all three stages (body, one-frame
cover, concat), loudness-normalizes the audio, writes the cover PNG, and runs QC.

```
{
  "src": "<finished edit .mp4>",
  "outdir": "<movie folder>\\shorts",
  "n": 1,
  "slug": "trailer_was_the_best_part",
  "film": "Other Mommy (2026)",
  "start": 17.16,
  "end": 41.55,
  "hook": "THE TRAILER WAS THE BEST PART",
  "text": "words actually spoken in this window",
  "silence": "<scratch>\\silence.json",
  "cover_at": 6
}
```

```
python scripts\build_short.py render --spec "<scratch>\clip1.json"
```

**Word-level captions and edge checks (added 2026-10-14, proven on Other Mommy).** Local
faster-whisper large-v3 is installed and runs on the GPU, so caption timing no longer has to
be guessed from character counts:

1. `python scripts\word_times.py --audio "<scratch>\silence_analysis.mp3" --out "<scratch>\words.json"`
   once per review (about a minute and a half for a 19-minute edit). Add `"words": "<path>"`
   to each clip spec and captions are built from real word times.
2. Whisper word times run loose, often 0.2 to 0.4s early. Use them for captions only. Cut
   points still come from the silence map. Check the fine gaps near an in-point
   (`silencedetect` at -33dB, d=0.04) when a word is missing or extra at the head.
3. Spec keys for caption cleanup: `head_pad` (accept words this many seconds before the
   start, default 0.05), `drop_tail` (discard N ASR words past the real out-point),
   `drop_phrases` (unclear audio, left out of captions, never guessed), `fixes` (single-word
   garble fixes), `prepend_text` (a spoken word the ASR missed, confirmed by listening to the
   isolated slice). Fillers (um, uh, ah) and function-word stutters are removed automatically.
4. After every render run `python scripts\check_clip.py --clip "<clip.mp4>"`. It transcribes
   the first and last 3.5 seconds of the finished clip so the first and last audible words can
   be checked against the plan. The first word is always stamped 0.00 by Whisper, so treat a
   leading "So" or "Dude" as a prompt to check the fine silence map, not as proof.
5. Premiere's transcript can drop words (Other Mommy clip 1 lost its first "Dude"). When
   Premiere and Whisper disagree, run Whisper on the isolated slice at two beam sizes, and
   believe it only if both agree.

Work files go to `D:\WKP\scratch\shorts_clipN_slug\` (override with env `WKP_SCRATCH`).
Filename convention: `clipN_slug.mp4`, lowercase, underscores, no spaces. Render one clip
per call. Typical cost is well under a minute per clip on this machine.

**Additions beyond the original spec (Zac to veto):** a persistent small gold film tag
("FILM TITLE | REVIEW") above the video band so every clip reads as one channel's product;
a 120ms hook fade-in; a slight darken on the blurred background so the footage pops; and
loudness normalization to -14 LUFS so clips are not quieter than the feed around them.

---

## 10. QC every clip

Mechanical (the script prints these): 1080x1920; duration inside 20 to 75 seconds, or
flagged if longer; audio stream present; head silence 0.10 to 0.35 seconds.

Actual viewing, not skippable. The script writes three frames (1s, midpoint, 2s before the
end) to the work folder. Open them with Read and confirm captions are legible, not
overlapping the footage, not running off frame, and that the hook text is clear of the video
band. Confirm the cover is a frame you would choose. Confirm the first spoken words match
what the hook promises. **A clip that fails a visual check gets fixed, not flagged.**
ffprobe is not a visual check.

---

## 11. Shorts copy and posting (now inside the Upload Package)

**Merged 2026-10-18 (Zac): no separate `Shorts Captions` file.** Everything below goes into
the Upload Package, Section 7 (one complete block per short, format in SKILL.md) and
Section 11 (flexible posting windows plus checklist). The fixed-date, fixed-clock table
described in the footer below is replaced by windows timed from when the full video goes
live; keep the click-by-click steps and pre-post checks. Older reviews (Other Mommy, Carrie)
keep their separate captions files as they are.

**Header:** source file full path, duration, resolution, fps, audio codec; audio deliverable
path and duration; clip count; any attribution warning (diarization absent or inferred);
any garble held out of public copy and the safe rewrite used.

**One block per clip:**
```
N. clipN_slug.mp4 | 00:00 to 00:00 source | 47.2s | YT / IG / FB

   Cover: clipN_slug_cover.png
   On-screen hook: "FOUR TO EIGHT WORDS, ALL CAPS"
   Opens on: "first five spoken words"

   YouTube title: ...
   YouTube description: ...
   #tag #tag #tag

   Instagram caption: ...
   #tag #tag #tag #tag

   Facebook caption: ...
```

Per platform: **YouTube Shorts**, first line functions as the title, front-load the film
name, one or two lines, 3 to 4 hashtags. **Instagram Reels**, hook line first (it truncates
fast), exit quickly, 4 to 5 hashtags including one broad community tag. **Facebook Reels**,
longer, more conversational, more crew voice, hashtags optional and never more than two.
Never identical copy across the three.

**Footer: the Posting Checklist (REQUIRED, added 2026-10-15, Zac's call).** The posting
package for every review must end with a checklist he can work from without asking anything.
Zac asked why Other Mommy did not have one: the old footer was only a three-line schedule, no
dates, no clock times, no file paths, no tick boxes, so nobody could post from it. Build:

1. **Dated table**, one row per clip, strongest first, one clip per day starting the day
   after the full review publishes (check the live publish date, do not assume). Columns:
   day and date, clip file (full path), cover PNG, YouTube time, Instagram time, Facebook
   time, and three tick boxes (YT / IG / FB). Times default to 11:00 AM ET, +45 min, +90 min.
2. **Click-by-click steps** for each tool: YouTube Studio (Create, Upload, Shorts title and
   description, Schedule), and Meta Business Suite Create reel with the Winter Wolf's Den
   and winterwolfsden pair selected (Facebook and Instagram in one pass, Customize post to
   use the separate captions). Name the right page: the composer defaults to the wrong
   page unless `asset_id=104052046075172` is used.
3. **Pre-post checks** pulled from the header (attribution listen, garbles, language).
4. Every clip's copy stays in the per-clip blocks above, the checklist points to it.

Reason it is manual: the Composio connectors run in the cloud and cannot read `L:\`, the
YouTube API quota is shared and was exhausted 2026-10-15, and Meta's composer cannot take
a file from automation. If a posting route that can read local files is ever set up, update
this section.

---

## 12. Environment (local Windows)

- Tools and interpreters: read `LOCAL-PATHS.md`. ffmpeg 9.0 (gyan full build) is on PATH
  with libass, drawtext, and boxblur confirmed 2026-10-14.
- Font: `assets\fonts\Poppins-Bold.ttf` and `Poppins-SemiBold.ttf` ship with this skill
  (SIL Open Font License, from the Google Fonts repository). The script copies them into the
  work folder and points libass at them. Nothing depends on a system-installed font.
- Cut audio and clips only from the **finished edit**. Folders often hold both the raw
  StreamYard recording and the finished edit (Other Mommy held a 37:48 raw and a 19:06
  edit). Confirm by comparing duration to the transcript's last timecode.
- Watch for a still-running export: a `._00_` temp file beside the `.mp4`, or a duration
  that changes between two ffprobe reads 30 seconds apart, means Premiere or Media Encoder
  is still writing. Poll until the size is stable across two checks.
- Original VM limits (180-second call cap, staging size limit, nohup failures) do not apply
  locally and are dropped.

---

## 13. Hard rules

1. Five clips maximum. Every one finished. No held clips, no re-trim queue.
2. No em dashes anywhere. Regular hyphens only.
3. Handles only in public-facing copy: Winter Wolf, KingZ, Oracle, ReelDon. Never a real
   first or last name in a caption, hook, title, or on-screen graphic. Matt requires this
   for employment reasons.
4. Never use #WinterWolfsDen.
5. Never state a review score in a caption, hook, cover, or post. Tease only. A critic score
   quoted from the film's reviews is fine, label it as theirs.
6. Never describe WWD as veteran-owned.
7. Captions burned in on every clip.
8. Never center crop. Blurred fill only.
9. Flag every transcription garble, publish none. Use a safe rewrite.
10. Never publish a number the hosts did not settle on air.
11. Never attribute a line to a specific host on inferred diarization alone in public copy.
    Flag it for a ten-second audio check.
12. Look at the frames before shipping.

---

## Changelog

**2026-10-14.** Triggered by an audit of the Other Mommy (2026) package. Five-clip cap
replaces "target 5 to 7, ship 6 plus." Ship floor raised 6 to 7. "HOLD FOR RE-TRIM" removed
as an outcome. Length limits corrected (YouTube Shorts 3 min as of Oct 2024, Instagram
Reels 3 min as of 2025-01-20, Facebook flagged unverified, working target 30 to 75s with a
20s floor). Burned-in captions added. Cover frame added as a PNG and a one-frame prepend.
Render split into stages. Captions document promoted to its own required section. Source
file selection rule added.

**2026-10-14, local adaptation.** Installed into the repo skill. Cloud VM commands replaced
by `scripts\build_short.py`. Poppins bundled in `assets\fonts`. Added film tag strip, hook
fade, background darken, and -14 LUFS loudness normalization (flagged above as additions).
Fixed a bug found in testing: the one-frame cover clip carried about a second of silent
audio unless its audio was capped at one frame length.

**2026-10-18.** Captions doc merged into the Upload Package (Zac). Each short's copy,
files, checks and posting window sit in one block. Posting moved from fixed dates and
times to windows timed from the full video going live.


**Stay on the movie (LOCKED 2026-10-19, Zac).** Pick clips about the movie under review. Skip clips whose topic is a tangent (another franchise, the DCU, a different movie). If a clip would mention another title in the first sentence or the hook, cut it later or pick another. Street Fighter (2026): the animated-DCU short was replaced by a game-details short.
