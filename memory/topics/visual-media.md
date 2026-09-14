# Visual Media / Framing Preferences

## Edge-to-edge over letterbox, except for vertical content [2026-08-24]
When fitting a still image into a fixed video frame (e.g. 1920x1080 B-roll),
Zac wants landscape/square source images cover-cropped to fill the frame
completely, edge to edge, no black bars — even though this trims some
content off the sides/top/bottom. Only portrait/vertical sources (movie
posters, key art, anything taller than wide) get pillarboxed with black
bars on the sides, because cropping those into a landscape frame would cut
off way too much.

**Why:** Went through two iterations on the Den Files EP1 B-Roll pass before
landing here. First pass cover-cropped everything and zoomed in too tight on
some images ("too zoomed in to make out what they are"). Second pass padded
everything with black bars to avoid any cropping — Zac called it "close
enough" but wanted less black space. Final rule: edge-to-edge is the
priority; only exempt vertical content where cropping would be destructive,
not just imperfect.

**How to apply:** Default to this rule for any future image-to-fixed-frame
resize task — Etsy listing prep, thumbnails, other WWD B-Roll — not just
[[wwd-broll-prep]]. If a specific landscape/square source is losing
something important to the crop (small/low-res source, tight composite),
flag it and ask rather than silently accepting or silently switching to
pillarbox. Full mechanics and the reference implementation live in the
wwd-broll-prep skill (`D:\WKP\.claude\skills\wwd-broll-prep\`).

## SUPERSEDED 2026-08-29 — contain/fit only, never crop
Overridden for the Good Boy (2025) / The Whisper Man picture-gather job and
going forward as the new default: **nothing gets cropped, ever.** Every
source (landscape, square, or portrait) is scaled to fit entirely inside
the 1920x1080 frame, uniform scale, with letterbox (top/bottom) or
pillarbox (left/right) black bars added wherever the source's aspect ratio
doesn't already fill the frame. Zac pointed to
`L:\Winter Wolfs Den review show\Raw Footage\Spider-Man Brand New Day\USE`
as the reference look — those images read edge-to-edge only because the
source stills already happened to be close to 16:9, not because anything
was cropped to force that.

**Why:** Zac's exact words: "Trim nothing, make it fit." Direct override of
the 2026-08-24 cover-crop default above.

**How to apply:** Use this rule for any future image-to-fixed-frame resize
task, including [[wwd-broll-prep]] — the cover-crop/pillarbox-split logic
above is no longer the default. If a resize job seems to call for
cover-crop instead (e.g. Zac asks for the old edge-to-edge look
specifically), confirm rather than assuming which rule applies.

## New skill: wwd-review-photo-pull [2026-08-29, corrected 2026-08-30]
Built the same day as the rule above — pulls the standard 18-picture set
(1 poster + 17 stills) for a WWD review, creates the Raw Footage\<Movie
Name>\ folder if it doesn't exist, and resizes into USE using the same
contain/fit script as [[wwd-broll-prep]]. Trigger: "record video on this
movie <title>".

First run (Good Boy 2025, The Whisper Man 2026) used IMDb's media index
only and got it wrong two ways, corrected 2026-08-30:
- **IMDb-only sourcing is not enough.** Its media index leans heavily on
  marketing key art (character posters, one per lead actor) rather than
  genuine film stills, and can bleed in off-topic images from the "more
  like this" recommendation strip. Pull from multiple sources — TMDb's
  backdrops tab in particular separates real film stills from posters
  cleanly and is the better primary source; supplement with the studio/
  streamer's official press site when needed. Don't rely on one site.
- **Exactly one poster, period.** Character-poster key art variants
  (different actor, different quote, same campaign) are NOT distinct
  B-roll — Zac counted 4 "posters" in one delivered set and only wanted 1.
  Treat any marketing key-art/character-poster image as excluded unless
  it's the single chosen poster.
- **Content mix for the 17 non-poster images: mostly real film stills
  (backdrops/screengrabs from the movie itself), cast/press photos limited
  to a few at most.** Don't fill the set with red-carpet and studio
  portrait photos just because they're easy to find — prioritize actual
  shots from the film.

Also corrected 2026-08-30: padding on the resize is **alpha transparency,
not black bars** (Zac caught black bars on a poster and wants the editor
able to composite it, not a black box baked in) — see [[wwd-broll-prep]]'s
script, now RGBA output.

## wwd-review-photo-pull Step 8 added: beat-matched images, not just the generic 18 [2026-09-13]
Zac pointed to `Raw Footage\T-2\USE\` (Terminator 2 review, already
produced) as the standard to hit going forward — 27 images, not 18. The
extra 9 were hand-picked and hand-named to match specific moments in the
actual commentary (`a new man.png` — T-1000's CGI fire-walk reveal;
`frozen.png` — the climax; `pratical effects.png` — a **behind-the-scenes
production photo** of Robert Patrick in practical squib rigging, not a
movie still at all, pulled to illustrate a practical-vs-CGI talking
point). That set is what actually carried the episode.

**Why:** Zac's framing: "take a look at T-2 in Use... that is what I
needed to tell the story." The generic poster+17-stills pull is the
floor, not the ceiling — it has no connection to what's actually said in
the review.

**How to apply:** `wwd-review-photo-pull` now runs a second pass (Step 8)
whenever a script/outline/beat sheet exists for the episode: read it,
pull an image for every actual talking point (a named scene, a specific
joke or line, an FX/production discussion), name each file after the
moment (not `still-19.jpg`), and allow BTS/production photos when the
discussion point is genuinely about the making of the movie. If no
script exists yet at pull time, the pass is flagged as pending in the
report, not silently skipped. Additive to the numbered 18, same USE
folder, same resize pipeline. Full detail in the skill file itself.

## wwd-review-photo-pull Step 3.5 added: know the story, cover major characters [2026-09-14]
On the Heat (1995) pull, the first 25-image set (TMDb backdrops/posters,
Steps 1-7 process) was strong on De Niro/Pacino and action beats but had
**zero images** of Natalie Portman (Lauren, the stepdaughter whose suicide
attempt is a real plot beat), Ashley Judd (Charlene Shiherlis, whose
ending rooftop signal to Chris is a major plot turn), Diane Venora
(Justine, Hanna's disintegrating marriage), or Dennis Haysbert (Breedan,
the ex-con cook forced into being the crew's driver). Zac's exact words:
"these are all people major to the story... when you are pulling this
pictures you need to understand the story of the film, and all the major
players in it as well, and be sure to pull ones that are not just cool
but hit major beats."

**Why:** A picture pull built from "whatever looks coolest in the TMDb
backdrop gallery" naturally skews to the two leads and the flashiest
action shots. That's a real gap, not a style choice — it under-serves any
episode that actually discusses the film's subplots and supporting cast.

**How to apply:** Before finalizing any picture set, pull the film's full
cast list (IMDb `/title/<id>/fullcredits/`) and identify which credited
characters carry a real subplot or beat, not just who has the most screen
time. Get at least one real still per major character. The reliable way
to find character-specific stills: from the full-cast link, follow to the
character page (`/title/<id>/characters/<nm id>/`), then its "Photos"
link, which lands on a still-frame gallery filtered to just that person
(`/title/<id>/mediaindex/?relatedNames=<nm id>&contentTypes=still_frame`).
This filtered view works even when IMDb's general mediaindex won't
paginate past 50 results (gated behind sign-in) — the per-name filtered
URL is a separate, un-gated view. Full detail now in the skill file
itself as Step 3.5.
