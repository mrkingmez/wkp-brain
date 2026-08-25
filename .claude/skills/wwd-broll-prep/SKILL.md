---
name: wwd-broll-prep
description: >
  Takes a folder of mixed-source still images (screenshots, movie posters,
  newspaper clippings, Google Images grabs, archive photos) gathered for a
  Den Files episode or a WWD review video, and turns them into numbered,
  frame-ready 1920x1080 PNGs dropped into a USE folder next to the source
  B-Roll, sequenced to match the episode/review script. Trigger on "resize
  the B-Roll", "get these images ready for the edit", "turn the B-Roll into
  PNGs", "prep the stills for EP [n]", or when Zac hands over a B-Roll
  folder and a script/outline and wants it edit-ready. Works for both Den
  Files episodes and standard WWD review videos - the folder layout differs
  slightly (see Step 1) but the prep logic is identical. Requires Claude
  Code or Cowork (local filesystem + Python/Pillow access) - cannot run in
  plain claude.ai chat.
---

# WWD B-Roll Prep

Turns a messy folder of grabbed images into a clean, numbered set of
1920x1080 PNGs an editor can drop straight into a timeline in script order.
Built after the EP1 (Fire in the Sky) B-Roll pass — the steps below encode
what that pass actually needed, including the mistakes worth not repeating.

## Requires Claude Code or Cowork (local machine access)

Needs Python + Pillow and read/write access to the actual folders on disk
(typically on `L:\`). Cannot run in plain claude.ai chat.

## Step 1 — Find the inputs

Ask for (if not already given, don't guess):
- The B-Roll source folder. Den Files: `...\Den Files\EP [n]\B-Roll\`.
  Review videos: confirm the folder name with Zac, layout isn't
  standardized yet the way Den Files is.
- The output folder. Den Files uses a sibling `USE\` folder
  (`...\Den Files\EP [n]\USE\`) next to B-Roll. For review videos, ask
  where Zac wants the numbered output if there's no existing convention.
- The script or outline to sequence against — a `.docx` editing script
  (Den Files) or whatever outline/script exists for a review video. If
  there's no written script, ask Zac for the beat order instead of
  guessing at sequence.

If the script is a `.docx`, extract it with:
`python scripts/extract_docx_text.py "<path>.docx"`
(no python-docx dependency needed — reads the zip's document.xml directly).
Look for a production-reference / source list section first (Den Files
scripts have one); it's usually a faster map to filenames than reading the
whole script beat by beat.

## Step 2 — Look at every image. Do not sequence from filenames alone.

This is the step that matters most. Filenames lie: a file called
`UFO_listing.png` turned out to be a newspaper clipping, not a poster.
`Logging_Crew_1970s_NARA.jpg` didn't show a logging crew. Generic names
(`images.jpg`, `images (1).jpg`, `unnamed.webp`) tell you nothing.

Read (view) every image in the source folder before building the manifest.
For each one, note:
- What it actually shows (not what the filename claims)
- Whether it looks mislabeled, low-value, or off-topic relative to the
  script

## Step 3 — Flag findings and ambiguity before building the manifest

Don't silently decide on the user's behalf, and don't silently follow a
filename-based assumption once you know it's wrong. Ask (AskUserQuestion)
about things like:
- **Scope** — process everything in the folder, or skip generic/likely-reject
  files?
- **Sensitive/duplicate content** — e.g. multiple film stills of the same
  graphic scene when the script says "single still only, fair use." Ask
  whether to include all candidates (editor picks one at cut time) or have
  Claude pick the single best match
- **Mislabeled/off-topic files** — confirm whether to include or skip them

Don't re-ask things already settled earlier in the same session — only
surface genuinely new findings from Step 2.

## Step 4 — Build the manifest

Order images to match the script/outline's flow (cold open through outro,
or the review's segment order) — not alphabetical, unless Zac explicitly
asks for alphabetical. Group same-topic images together within their beat
even if the script doesn't cite every file individually.

Write a JSON manifest — just an ordered list of filenames:

```json
["example-poster.webp", "example-photo.jpg"]
```

Save the manifest to the scratch folder (`D:\WKP\scratch\`), not inside the
venture folder — it's a working file for this run, not a deliverable.

## Step 5 — Run the resize

```
python scripts/resize_broll.py --src "<B-Roll folder>" --dst "<USE folder>" --manifest "<manifest.json>"
```

Defaults to 1920x1080. Pass `--width`/`--height` for a different target
(e.g. a vertical short) if Zac asks for one.

**Orientation decides the treatment** (locked in with Zac 2026-08-24, EP1
pass — went through two iterations before landing here):
- **Landscape or square source** (width ≥ height) → cover-fit, center-crop
  to fill the frame completely, edge to edge, no black bars.
- **Portrait source** (height > width — movie posters, key art, anything
  taller than wide) → scale to touch top and bottom, keep the full width
  visible with nothing cropped off the sides, pillarbox with black bars
  left/right. Cropping into a vertical poster/title would cut off way too
  much to be worth avoiding the bars.

Scaling is always uniform — aspect ratio locked, never stretched or
distorted — in both cases. If a landscape source's crop is trimming
something important (e.g. a busy multi-person composite), that's a Step 2/3
judgment call: flag it and ask whether to swap in a tighter-cropped source
image or accept the trim, rather than silently defaulting to pillarbox for
a landscape image just to dodge cropping.

Output is `1.png`, `2.png`, ... in manifest order, written to the
destination folder.

## Step 6 — Verify before reporting done

View at least a couple of outputs — check the full source image is visible
with nothing cropped off, the aspect ratio looks right (no stretching), and
the black bars land where expected. Check output dimensions match the
target. Don't just trust the script ran without errors — actually look.

## Why not the Adobe connection

Tried this first on EP1 and hit two hard limits: Adobe's tools cap batch
jobs around ~20 files, and there's no programmatic upload path for local
(non-Adobe-hosted) files — only an interactive file picker, one file at a
time. For a folder of 20+ images that's impractical. Default to the local
Pillow script; only route through Adobe if Zac specifically wants each
image touched by Photoshop's cloud tools and is willing to click through
the picker per file.

## Do not

- Sequence images from filenames without viewing them first
- Silently keep or silently override a stale assumption (e.g. a filename,
  or a note in another file) once visual inspection contradicts it — flag
  it and ask
- Crop a portrait/vertical source (posters, key art) — pillarbox those,
  never crop
- Pillarbox a landscape/square source by default — those cover-fill edge to
  edge; only fall back to padding one if cropping it would genuinely lose
  something important, and flag that case rather than deciding silently
- Save the manifest or intermediate files into the venture folder — scratch
  only
- Attempt to batch more than ~20 files through the Adobe connection
- Skip the Step 6 visual verification
