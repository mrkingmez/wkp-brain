---
name: wwd-review-photo-pull
description: >
  Pulls the standard 18-picture set (exactly 1 movie poster + 17 real film
  stills, cast photos kept to a minimum) for a WWD review video, drops it
  in a Raw Footage folder named for the movie (creating it if it doesn't
  exist), and resizes it into a sibling USE folder as 1920x1080 PNGs with
  alpha-transparent padding using the same contain/fit rule as
  wwd-broll-prep. If a script, outline, beat sheet, OR a timestamped
  transcript already exists for the episode, also runs a second pass
  pulling additional beat-matched images tied to specific moments/jokes/FX
  discussion (including behind-the-scenes/production photos, not just
  movie stills), then writes a timecoded timeline-placement list saying
  exactly where each beat-matched image belongs, with a Premiere transition
  recommendation for each - see Step 8. Also runs the whole review intake
  (calendar entries, photo pull, resize, delete originals) when Zac says "we
  are doing a review on <title>" - see Review Intake Mode. Trigger on
  "we are doing a review on <title>", "record video on this movie <title>", "picture gather for <title>", "get
  pictures for <title>", "pull pictures from this transcript", "tell me
  where to insert these in the timeline", or when Zac names a movie and
  wants the picture set ready to go, or hands over a transcript and wants
  images placed against it. Requires Claude Code (local filesystem +
  Chrome browser tools + Python/Pillow) - cannot run in plain claude.ai
  chat.
---

# WWD Review Photo Pull

Turns "record video on this movie X" into a ready-to-edit picture set with
no other input needed. Built 2026-08-29 doing this by hand for Good Boy
(2025) and The Whisper Man (2026 Netflix); corrected 2026-08-30 after Zac
reviewed that first pass and flagged three real problems - each fix below
is load-bearing, not a nice-to-have.

## Requires Claude Code (local machine access + Chrome)

Needs the `mcp__claude-in-chrome__*` tools (load them via ToolSearch if
deferred - `browser_batch`, `navigate`, `javascript_tool`, `find`,
`read_page` at minimum), plus Python + Pillow and read/write access to
`L:\`. Cannot run in plain claude.ai chat.

## Review Intake Mode (added 2026-10-11, Zac's call) - the full flow

Zac opens with "we are doing a review on <title>" and gives the recording
date, filming date, and release date (if he leaves one out, ask in one line).
Run all of this without further prompting:

1. **Calendar.** Put the dates on the **Winter Wolf's Den** Google Calendar
   (id `thewinterwolfsden@gmail.com`, not the primary or the WKP one). Follow the
   existing pattern on that calendar: a timed `<Title> - Record Review` event
   (Sunday-night recording convention is 7 to 9 PM ET unless he says a
   different time) and an all-day `<Title> - Review Release` event on the
   release date. Check `list_events` first so you never double-book an entry.
   If the movie's own theatrical-release entry already exists (e.g.
   `Other Mommy - Movie`), leave it alone, it is a different event.
2. **Folder, photos, resize** - Steps 1 to 7 below, unchanged.
3. **Delete the originals (Step 7.5).** Only after Step 7 verification passes.
4. **Report back** with the real count and mix, anything flagged, and the
   calendar entries made. Then wait for the transcript.
5. **When Zac hands over the transcript** (he edits first, cutting the
   banter and life talk, so never transcribe or build from the raw recording
   before he says the cut is ready), run Step 8 and deliver the placement
   report with transitions to `D:\WKP Reports\`.

Resolve the title first (Step 2). A just-released film is the normal case
here, so expect TMDb to be thin. Report the real count, never pad.

## The three corrections from the first run - read before doing anything

1. **One source is not enough.** IMDb's media index alone leans heavily on
   marketing key art and can bleed in off-topic images from its "more like
   this" strip. Check TMDb (themoviedb.org) as well - its "Backdrops" tab
   is genuine film stills, separated cleanly from "Posters." Prefer TMDb
   backdrops for the 17 non-poster images; use IMDb and the studio/
   streamer's official press site to fill gaps or confirm identity.
2. **Exactly ONE poster in the final 18, full stop.** Character-poster key
   art (a campaign's per-actor variant - different face, different quote,
   same design language) is marketing art, NOT a second poster and NOT a
   film still. It does not count as a "different image" just because the
   text changed. Zac's exact words after the first pass: "you have gave me
   like four of each posters, I only need one poster." Any image that is
   poster-style key art and isn't your one chosen poster gets excluded,
   no exceptions.
3. **The 17 non-poster images: mostly real shots from the movie itself,
   cast/press photos limited to a few at most.** Red carpet photos, studio
   portrait sessions, and premiere group shots are easy to find and fill a
   set fast - resist that. A TMDb backdrop or an official film still beats
   a press photo every time. Zac's words: "all still other than the poster
   should be either from the movie itself, or a cast, but limit the cast
   and focus on shots from the movie."

## Step 1 - Find or create the movie's folder

Target is always flat, directly under Raw Footage - matches the existing
convention (e.g. `...\Raw Footage\Spider-Man Brand New Day\USE\`), not
nested under a dated batch folder:

```
L:\Winter Wolfs Den review show\Raw Footage\<Movie Name>\
L:\Winter Wolfs Den review show\Raw Footage\<Movie Name>\USE\
```

Check `Raw Footage\` for an existing folder matching the movie name
(case-insensitive; allow for a trailing year/platform in parens, e.g.
"Good Boy (2025)"). If found, use it. If not, create both the movie folder
and its `USE` subfolder. Never ask which folder to use - this is the whole
point of the skill.

## Step 2 - Confirm the exact title

Movie titles collide (multiple "Good Boy" entries exist, different years
and formats). Search IMDb (`https://www.imdb.com/find/?q=<title>&s=tt`) or
TMDb (`https://www.themoviedb.org/search?query=<title>`), match on
whatever Zac gave you - year, platform (Netflix/theatrical), genre. If more
than one plausible match exists and nothing disambiguates it, flag it and
ask rather than guessing.

## Step 3 - Pull from TMDb backdrops first

TMDb separates real film stills from marketing art far more cleanly than
IMDb. On the title's TMDb page, open the Images/Media section and go to
**Backdrops** - these are actual film stills. Grab image URLs (TMDb serves
large originals directly, no hash-decoding needed like IMDb's CDN).
Backdrops alone should cover most or all of the 17 non-poster slots.

Only pull from **Posters** for your single poster image - pick the primary
US/wide-release one-sheet, not a character variant.

If TMDb's backdrop count is thin, supplement from IMDb's media index (same
hash-extraction approach as before - see git history of this file for the
`javascript_tool` snippet) or the studio/streamer's official press site.
Whatever the source, every non-poster image still has to be a real film
still or a limited cast photo per the rule above - the source doesn't
change the content bar.

## Step 4 - Download

Save any working hash/URL lists to `D:\WKP\scratch\<movie>_urls.txt` (temp
working file only - never system temp, see LOCAL-PATHS.md). Download
straight into the movie's Raw Footage folder (this is a deliverable, not
scratch) with PowerShell:

```powershell
Invoke-WebRequest -Uri $url -OutFile $out -UseBasicParsing -Headers @{ "User-Agent" = "Mozilla/5.0" }
```

Name the chosen poster `poster.jpg`. Name the rest `still-01.jpg`,
`still-02.jpg`, etc.

## Step 5 - Look at every image before finalizing. Do not trust gallery order.

Read (view) every downloaded image and sort each one into: poster (exactly
one allowed), real film still, or cast/press photo (a few at most). Filter
out:

- **Any poster-style key art beyond your one chosen poster** - character
  variants, foreign-market variants, alternate crops of the same design.
  These do not count toward the 17.
- **Off-topic images from other titles** - a broad DOM/gallery scan can
  pull in "more like this" recommendation content that shares the same
  CDN URL pattern but belongs to unrelated movies.
- **Excess cast/press photos** - red carpet, premiere group shots, studio
  portraits. Keep at most a handful; the rest of the 17 must be real film
  stills.
- **Very low-value frames** - a plain text title card with nothing else in
  frame, a blurry/tiny source.

Replace anything filtered out with the next unused candidate. If a
brand-new release genuinely doesn't have 17 real stills available yet
(marketing dropped days ago, backdrops thin), stop at however many
genuinely qualify, report the real count and the real mix (X stills, Y
cast photos), and flag it - do not pad with excluded categories just to
hit 18.

## Step 6 - Build the manifest and resize

Manifest is `poster.jpg` first, then the rest in whatever order you kept
them (no script to sequence against for a review's picture set - order
doesn't matter beyond poster-first). Save to
`D:\WKP\scratch\<movie>_manifest.json`, then:

```
python D:\WKP\.claude\skills\wwd-broll-prep\scripts\resize_broll.py --src "<Raw Footage>\<Movie Name>" --dst "<Raw Footage>\<Movie Name>\USE" --manifest "<manifest.json>"
```

Same script and contain/fit rule as [[wwd-broll-prep]] (see
`memory/topics/visual-media.md`): every image, any orientation, scales to
fit entirely inside 1920x1080 with **alpha-transparent** padding - not
black bars (corrected 2026-08-30) - so the editor can composite it without
a black box baked in. Output is RGBA PNG. Nothing ever cropped. The poster
(portrait) always ends up pillarboxed by the same logic - no separate
handling needed.

## Step 7 - Verify before reporting done

View the poster output and at least one landscape still from the USE
folder. Confirm: nothing is cropped, the padding is genuinely transparent
(not black), dimensions are 1920x1080. Report the actual count and mix
delivered (poster count, real-still count, cast-photo count) - flag it
plainly if it came in under 18 or the mix leans more cast-heavy than
intended.

## Step 7.5 - Clean up: delete the originals (added 2026-10-11, Zac's call)

Once Step 7 passes, the movie folder should hold ONLY `USE\`. Delete the
downloaded `.jpg` originals sitting directly in `Raw Footage\<Movie Name>\`
(poster candidates, rejected stills, duplicates, everything). Rules:

- Delete only loose files directly in the movie folder. Never touch `USE\`.
- Never delete before Step 7 verification passes (15+ files, 1920x1080
  RGBA, nothing cropped, transparent padding).
- First write the source list to `D:\WKP\scratch\<movie>_urls.txt` (poster
  and every backdrop/still URL, with which were excluded and why). The
  originals are re-downloadable from it if Zac ever wants them back.
- Step 8's second pass pulls fresh images later. Those get downloaded,
  resized into `USE\` the same way, and their originals deleted the same way.

## Step 3.5 - Know the story, cover the major characters (added 2026-09-14)

A picture set built by just grabbing whatever TMDb backdrops look coolest
skews toward the two leads and the action beats, and misses characters who
carry major subplots. On the Heat (1995) pull, the first 25-image set was
strong on De Niro/Pacino and the heist/action sequences but had zero images
of Natalie Portman (Lauren, the stepdaughter whose suicide attempt is a real
plot beat), Ashley Judd (Charlene Shiherlis, whose ending rooftop signal to
Chris is a major plot turn), Diane Venora (Justine, Hanna's disintegrating
marriage), or Dennis Haysbert (Breedan, the ex-con cook forced into being
the crew's driver for the final heist). Zac's correction: "these are all
people major to the story... when you are pulling this pictures you need to
understand the story of the film, and all the major players in it as well,
and be sure to pull ones that are not just cool but hit major beats."

**Before finalizing the set:** pull the film's full cast list (IMDb
`/title/<id>/fullcredits/`) and identify which credited characters actually
carry a subplot or a major beat, not just who has the most screen time or
the flashiest action scene. For each one, get at least one real still.
IMDb's per-character photo galleries are the reliable way to do this -
from a name's full-cast link, follow through to the character page
(`/title/<id>/characters/<nm id>/`), then its "Photos" link, which lands
on `/title/<id>/mediaindex/?relatedNames=<nm id>&contentTypes=still_frame`
- a still-frame gallery filtered to just that person. This works even when
the general IMDb mediaindex won't paginate past its first 50 (which gates
behind sign-in) - the per-name filtered URL is a separate, un-gated view.

**How to apply:** this is not "add more pictures" for its own sake - it's
matching the pull to the actual story. A generic pretty-picture pull is not
a substitute for understanding who matters in the film and why. Treat this
the same as Step 8's beat-matching: know the story first, then go find the
images that tell it.

## Step 8 - Second pass: beat-matched images (added 2026-09-13, extended 2026-09-24 to work from a transcript)

The 18-image set from Steps 1-7 is the floor, not the ceiling. Reviewed
`Raw Footage\T-2\USE\` (Terminator 2 review, already produced) and found
27 images, not 18 - the extra 9 were hand-picked and hand-named to match
specific moments in the actual commentary: `a new man.png` (the T-1000's
full-CGI walk-through-fire reveal), `frozen.png` (the liquid-nitrogen
shatter climax), `pratical effects.png` (a **behind-the-scenes production
photo** of Robert Patrick rigged with practical squib gear on set - not a
movie still at all, pulled specifically to illustrate a practical-vs-CGI
talking point), plus five more each tied to a specific line, joke, or
plot beat. That set is what actually carried the episode - the generic
18 alone would not have.

**Precondition: a script, outline, beat sheet, OR a timestamped
transcript has to already exist** for this pass to mean anything - it is
matching images to specific things the hosts actually say, not generic
content. Check the movie's Raw Footage folder and the script-room/
wwd-director pipeline for a script/outline first; if there isn't one but
a diarized transcript exists (the standard `wwd-video-transcriber`
output, or one Zac hands over directly), use that instead - a transcript
is often the stronger source since it's what actually got said on camera,
not what was planned. Most FrostCast episodes and unscripted reviews will
only ever have a transcript, never a script - do not treat that as
"precondition not met."

- **If a script/outline exists:** read it. Pull out every moment that's
  actually a talking point - a named scene, a specific joke or line, an
  FX or production discussion, a plot beat the hosts call out by name.
  For each one, find an image that matches THAT specific moment, not a
  generic still of the same general scene. Behind-the-scenes and
  production photos are in scope here (unlike Steps 1-7's stills-only
  rule) whenever the discussion point is actually about the making of
  the movie - practical effects, stunt work, a specific visual gag - the
  T-2 BTS photo is the model case, not an exception to avoid.
- **Sanity-check the transcript first (added 2026-10-12).** If the Premiere .txt is much shorter than the video, shows one speaker for a two-host show, or has big empty timecode blocks, do not build on it. Transcribe the mp4 with wwd-video-transcriber using `--num-speakers 2`, then convert to edit timecodes by matching shared lines (see memory/topics/transcription.md). Place each image on the exact line it fits, not at the start of a block.
- **If a transcript exists instead (no script/outline):** read the full
  diarized, timestamped transcript. Walk it the same way as a script -
  pull out every real talking point (a named scene, a specific joke or
  line, an FX/production discussion, a topic the hosts spend real time
  on), but anchor each one to the transcript's actual timecode range
  instead of a script line. A FrostCast episode covering several unrelated
  topics works the same way as a single-movie review - segment by topic
  first (reuse `wwd-frostcast-chapters`' chapter boundaries if that skill
  already ran on this transcript), then beat-match within each segment.
  If a topic discussed has no existing Raw Footage/USE folder yet, either
  pull a fresh image for it (reuse Steps 3-5's sourcing approach - TMDb/
  IMDb for a movie, a plain web image search for a real-world news topic)
  or flag it as needing one rather than skipping it.
- **If neither a script/outline nor a transcript exists yet:** this pass
  can't run yet. Say so plainly in the report ("beat-matched pass pending
  - no script or transcript yet") - do not skip it silently, and do not
  fabricate beats from the movie's general reputation or the episode's
  general topic instead of the actual script/transcript.

**One picture, one place (LOCKED 2026-10-19, Zac: "I do not like using the same picture twice").** Within one video, every placement uses a different image. Never reuse a PNG for a second beat, a second stop in a run sheet, a short, a card or a callback. If there are more beats than pictures, pull more (Steps 3-5 sourcing, new stills) instead of repeating. Before delivering a placement report or run sheet, check that no filename appears twice and say so in the report ("N placements, N different pictures"). The poster is the one allowed exception only if Zac asks for an open and close on it.

**Solo shots, only a few (LOCKED 2026-10-19, Zac, corrected same day).** Add a CAM stop (cut to that host's solo camera, the King-Z or Winter Wolf webcam clip) only when a host is making a good point and clearly has the floor. A few per video, not every long turn. Pick the strongest points from the speaker-labeled transcript and leave the rest as the two-shot. Zac is still teaching his edit taste, so save each new correction to memory the same turn.

**Seven seconds max (LOCKED 2026-10-19, Zac: "we are not a faceless channel").** No picture stays on screen longer than 7 seconds in any run sheet or placement report. A picture is a quick cutaway on the word, then the hosts' faces return. If a talking point runs long, give the picture its first 7 seconds only, or use a different picture for the next beat (never the same one twice). Check every hold before delivering and say so in the report.

**Fill the picture gaps automatically (added 2026-10-18, Zac's call).** On
the FIRST transcript for a video, read it for every talking point with no
picture in `USE\` yet: another movie or show named, an actor's other role,
the game or book it came from, a real event, a callback, a prop or scene
the hosts describe. Also add anything else that would clearly help a
beat. Go get each one without asking (TMDb/IMDb for titles and people, a
plain web image search for everything else, same quality rules as Steps
4 to 5), resize per Step 6, and save it in that video's `USE\` folder with
the next free number. Use them in the run sheet, then tell Zac in the
report what was added and for which line. Anything with no usable image
is listed as a gap, never skipped quietly.

**Naming:** short, specific, tied to the moment - not `still-19.jpg`.
Match the T-2 pattern: `a new man.png`, `frozen.png`, `practical
effects.png`. A name that only makes sense to whoever picked it (T-2 had
one - `henery.png` - that didn't match any character's real name) is
fine; it just needs to mean something to the person cutting the episode,
not to a stranger.

**Where they go:** same `USE` folder as the numbered 18, same resize
pipeline (Step 6), additive - never replace a numbered still with a
beat-matched one, they serve different purposes.

**Timeline-placement output (required whenever the source is a
transcript, optional but welcome for a script/outline pass):** write a
plain timecoded list alongside the images -
`<Raw Footage>\<Title>\USE\timeline-placements.md` - one line per
beat-matched image: transcript timecode range, a short quote/paraphrase
of what's being said, the image filename, and one line on why that image
fits. This is the actual deliverable an editor drops into the timeline
against, not just a folder of extra pictures. Example line:

```
[14:32-14:58] "the liquid nitrogen scene where he just shatters" -> frozen.png (matches the exact FX beat being described)
```

**Transition recommendations (added 2026-10-11).** Every placement line also
gets a transition suggestion and a duration in frames, picked ONLY from the
Premiere built-ins in [premiere-transitions.md](premiere-transitions.md)
(Zac is on the Adobe defaults). Follow that file's table, lean on hard cuts and
Cross Dissolve, and never recommend anything from its avoid list. Extended
example line:

```
[14:32-14:58] "the liquid nitrogen scene where he just shatters" -> frozen.png | in: Cross Dissolve 12f, out: hard cut | matches the exact FX beat being described
```

**Deliverable: the placement report (.docx).** Per the root CLAUDE.md output
rule this goes to `D:\WKP Reports\Asset Placement Run Sheets\<YYYY-MM-DD> - <Title>
Image Placement.docx` (the one delivery folder). Keep the matching `.md` in
`WWD\reports\`. Also keep the `timeline-placements.md` next to the images in
`USE\`.

**Format: one Edit Run Sheet in video order (LOCKED 2026-10-18, Zac).** The
whole report is one list of numbered stops, top to bottom in the order of
the video. No separate sound map, sticker, music or "no image" sections.
Every stop starts with the three things Zac liked from the old placement
doc, then everything else for that moment sits right under it:

```
### 7. 02:54 | PNG 19 | search: "captivated"
Said: "I was captivated from the first episode" (Winter Wolf)
In: Cross Dissolve 12f. Hold to 03:07. Out: hard cut.
Sound: <full path> at -10 dB, on the word "captivated".
Notes: zoom, sticker, anything else for this moment.
```

- Stops with no picture still get their own stop in order, with the type
  in the header where the PNG would go: `SOUND ONLY`, `STICKER`,
  `CAM: single out Winter Wolf` (or KingZ), `CARD`.
- Everything for a PNG lives under that PNG's stop. If one picture is used
  twice, it gets two stops.
- Keep the one-time "Before you start" block at the top (paths, import,
  tracks, how to find a spot) and a short list of gaps at the end. That
  is the only content outside the stops.
- Model: `WWD\reports\Carrie-Edit-Run-Sheet.md`, plus a "Said:" quote line
  and the PNG number in each header. The `no-ai-slop` pass is
not required, since this is an internal editing doc. Build the .docx with `D:\WKP\.claude\skills\no-ai-slop\scripts\md_to_docx.py`.

**Report:** state how many beat-matched images were found and added, name
any talking point from the script/transcript that a real image couldn't
be found for (flag it, don't quietly drop it), and confirm the
timeline-placements file was written when the source was a transcript.

## Do not

- Ask which folder to use - find or create it per Step 1, always flat under
  Raw Footage.
- Save downloaded images to scratch - they are deliverables, they go in the
  Raw Footage movie folder.
- Rely on IMDb alone - check TMDb backdrops first per Step 3.
- Count more than one poster-style image toward the 18, ever - see the
  corrections section.
- Fill the 17 with cast/press photos because they're easy to find - real
  film stills are the priority.
- Skip Step 5. A raw gallery pull is not a curated set.
- Pad a thin result with excluded categories to force the count to 18.
- Crop anything during resize, or pad with black instead of alpha - see
  Step 6.
- Treat Step 8 as optional when a script already exists - it's a
  standard part of the pull, not a nice-to-have. If no script exists
  yet, say the pass is pending; don't silently skip it and don't
  fabricate beats from general reputation instead of the real script.
- Limit Step 8 to movie stills only - a behind-the-scenes/production
  photo is the right answer whenever the discussion point is actually
  about the making of the movie.
- Build the set from only the top-billed leads and the coolest action
  shots - check the full cast per Step 3.5 and cover every character who
  carries a real subplot, not just who has the most screen time.
- Treat "no script exists" as a reason to skip Step 8 - check for a
  transcript before calling the pass pending. A transcript-only source is
  the normal case, not a fallback.
- Deliver beat-matched images from a transcript without the
  timeline-placements file - the timecode list is the point of running
  from a transcript at all.
- Put the same picture on two beats, stops or shorts in one video. Pull
  another still instead (see "One picture, one place" in Step 8).

- **Fun builds are click-by-click with real files (LOCKED 2026-10-17, Zac):** "I need to know how, step by step." Every fun build (poster open, blood drop, stickers, sound cues) must be written as numbered Premiere steps a person can follow without guessing: which track, which panel, which effect, what number to type, which keyframe. Every sound, overlay, template or music bed must name the **exact file path** of an asset Zac owns. Assets live on `P:\` (Sounds, Stock Footage, Tools, AE Templets) and `L:\Winter Wolfs Den review show\`; search the index `D:\WKP\data\assets\p-drive-index.csv` first (rebuild it if P:\ changed). Never write "a creak sound" or "a splat if you have one." Only when nothing owned fits: give a Firefly prompt (images/stickers), a Suno prompt (music), or a specific search (sound), plus the P:\ folder to save it into. Model case: Carrie report, Part B4.
- **The deliverable is ONE run sheet in timeline order (LOCKED 2026-10-17, Zac):** no separate parts for sounds, builds, stickers or transitions. One numbered list of stops from start to finish; each stop holds everything for that moment (search words, picture, in/out transition with frames, sound file path and dB, sticker clip, build steps inline). A short "before you start" block at the top and a "still open" list at the bottom, nothing else. Model: `WWD\reports\Carrie-Edit-Run-Sheet.md`. Name the docx `<date> - <Title> Edit Run Sheet.docx` in `D:\WKP Reports\Asset Placement Run Sheets\`.
- **Every created asset carries its recipe in the run sheet (LOCKED 2026-10-17, Zac):** anything made for a video (Suno music, Firefly art, a rendered sticker or card) gets its exact prompt (Suno Style and Lyrics lines, Firefly prompt) or, if built by script, its source files and how to remake it, written into the stop where it is used. Never in a separate doc.
- **Sticker kit is finished drop-in clips (LOCKED 2026-10-17):** `P:\WWD Kit\Stickers\` holds `Recommend Watch`, `Save Yourself the Time`, `Dumpster Fire` (rubber stamps, upper right, thud baked in, stamp lands 6 frames in) and `Wolfie Award Nominee` (premium, not a stamp: crystal wolf trophy, gold type, the show's own Wolfie fanfare baked in, 6 s). Each is a .mov with alpha plus a .png. "Do Not Watch" is retired. Transitions kit: `P:\WWD Kit\Transitions\Blood Pour.mov` (wet dripping blood sheet with sound, 54 frames, full cover frames 14 to 19, cut on frame 16; `scripts\make_blood_pour.py`). Never hand Zac a flat Color Matte wipe for blood; he called it a big red block. The run sheet just says which clip to drop and on which word. Only use a sticker where a host actually says it; Zac picks how many per video (Carrie: two). Rebuild with `scripts\make_stickers.py`. End cards: `scripts\make_next_up.py --title "<next movie>"` (add `--style fighter` for the slanted brush, fire-gradient arcade look; match the style to the movie, never paste the studio logo) writes `P:\WWD Kit\Cards\Next Up - <Title>.mov`; make it during the photo pull once the hosts name the next review.
- **Sounds: owned or skip (LOCKED 2026-10-17):** only list a sound with a file path Zac owns. If a cue is worth it and nothing owned fits, download it yourself during the photo pull from Mixkit (free, no account, license covers YouTube) into `P:\Sounds\Sound FX\Mixkit\`, then add it to the index. Otherwise drop the cue. Zac is a one-man show: fewer cues, each one ready to drag in. No music except intro and outro.
- **Know who is in every picture (LOCKED 2026-10-17, Zac: the "new bully" line got a picture of a teacher):** before any character-specific placement, build a "who's in it" list for the set: for each picture, the character, the actor, and what is happening. Source character stills from IMDb's per-actor galleries (Step 3.5), which tag who is in the photo, and keep that tag; TMDb backdrops carry no tags. When the hosts name a character ("Tina, the new bully"), look up which actor plays that character and only place a picture tagged with that actor. If none exists, say so in the run sheet and put a general still there instead. Never guess a character from costume or setting.
- **Find spots by words, not just the clock (LOCKED 2026-10-17, Zac: "your timestamps are off"):** every placement and cue gives the exact words to search in Premiere's **Window > Text > Transcript** search box, plus the timecode. Zac's timeline drifts from the transcript once he adds stings and cuts, so the words are the reliable anchor. Use words that appear once in the transcript; check with a grep before writing them.
- **Intro/outro stings (added 2026-10-13):** shows open with a burning-logo sting after the host intro line (Other Mommy: about 00:14 to 01:31). A Premiere transcript block that spans 70+ seconds for one sentence is that sting, not speech. Never put a poster or still across it. Poster covers the intro line only, and a fun transition can hand off into the logo. Ask Zac for sting start/end if the transcript does not make it obvious.
