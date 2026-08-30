---
name: wwd-review-photo-pull
description: >
  Pulls the standard 18-picture set (exactly 1 movie poster + 17 real film
  stills, cast photos kept to a minimum) for a WWD review video, drops it
  in a Raw Footage folder named for the movie (creating it if it doesn't
  exist), and resizes it into a sibling USE folder as 1920x1080 PNGs with
  alpha-transparent padding using the same contain/fit rule as
  wwd-broll-prep. Trigger on "record video on this movie <title>", "picture
  gather for <title>", "get pictures for <title>", or when Zac names a movie
  and wants the picture set ready to go. Requires Claude Code (local
  filesystem + Chrome browser tools + Python/Pillow) - cannot run in plain
  claude.ai chat.
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
