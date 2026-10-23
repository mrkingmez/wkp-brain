---
name: wwd-skill-formats
description: Output-format preferences Zac has given for WWD production skills (audio cut, and future skills as they come up)
metadata:
  type: feedback
---

## wwd-audio-cut: one chronological list, not separate KEEP/DROP blocks [2026-09-02]

Zac rejected the original audio-cut format — a `##KEEP` section followed by a
separate `##DROP` section, each with its own ascending timestamp list. His
words: "it just flows wrong." He wants ONE continuous chronological list that
alternates Start/Cut in actual play order, so the document reads exactly like
the edit will play out rather than requiring him to cross-reference two lists.

**Why:** matches how he'll actually work the edit — play, hit a cut point,
skip forward, resume playing — not how a spreadsheet-style ledger separates
kept vs. dropped material.

**How to apply:** any future audio-cut (or similar edit-list) output should
use:
```
Start [in] and go until [out] | [description]. Ends on: "[exact last line
spoken, quoted verbatim]"

Cut [in] up to [out] | [reason]
```
alternating straight through the episode. Boundary timestamps must be shared
edit points — a Start's "until" equals the following Cut's first number, and
vice versa — no gaps, no overlaps. Merge adjacent same-type decisions into one
entry instead of splitting one continuous keep/cut into multiple consecutive
lines with no real edit point between them. The "Ends on" quote matters to
him specifically — he wants the literal last word/line so there's zero
ambiguity about where to stop when he's actually cutting the audio.

This is now baked into `wwd-audio-cut/SKILL.md`'s Output format section
directly (updated 2026-09-02), so this memory is a pointer/rationale, not the
only place the rule lives — check the skill file is still correct before
assuming this memory is up to date.

See also [[transcription]] for the rest of the post-FrostCast pipeline this
feeds into.

## Weekly output goes in ONE per-week folder, not split into topic folders [2026-09-16]

2026-09-15 pulled the weekly social calendar out of its week folder into a
new standalone `WWD Social\` top-level folder (reasoning at the time: "one
flat folder for one recurring document type," same pattern as the Monday
brief). Zac reversed this the next day — he doesn't like it. He explicitly
pointed to `L:\Winter Wolfs Den review show\2026-08-10 Week of Aug 10\` as
the model to keep matching: one folder per week, with `01 Images`,
`02 Thumbnails`, `03 Transcripts`, `04 Upload Packages`, `05 Social Copy`
inside it. Everything for that week's production lives together.

**Why:** he said flat-out "I still want this each and every time just all
save in one overall folder" — the split-by-document-type structure (however
tidy it looks organizationally) breaks the thing he actually wants, which is
one place to look for everything tied to a given week.

**How to apply:** don't extract a recurring document type into its own
top-level folder just because it repeats weekly — the per-week folder IS the
organizing unit for WWD production output. If a new recurring output type
shows up, default to a new numbered subfolder inside the week folder (like
`05 Social Copy`), not a new top-level folder, unless Zac says otherwise.
Full rule now lives in `WWD/CLAUDE.md` Working Notes (locked 2026-09-16,
reverses the 2026-09-15 lock). Fixed going forward only — the 2026-09-14
files already sitting in `WWD Social\` and `Sponsors\Surfshark\` were left in
place, Zac's call.

## wwd-frostcast-chapters: always re-read the SKILL.md before writing chapters, never go from memory [2026-09-16]

Generated EP112's chapter list from memory of "what chapters generally look
like" instead of opening `wwd-frostcast-chapters/SKILL.md` first, and got the
format wrong in four ways at once: missing the mandatory first line
(`00:00:00 - Start`), wrong timecode format (`0:31` instead of `00:00:31` —
the spec requires HH:MM:SS even under an hour), wrong separator (en dash
instead of a plain hyphen), and added a paragraph of commentary when the spec
says "Return ONLY the chapter list. No preamble, no notes, no summary."
Zac caught it immediately: "You did the chapters wrong, I know you know the
format and you didn't do it this time."

**Why:** YouTube silently discards the ENTIRE chapter list if the format is
off (wrong first line, wrong timecode format, etc.) — this isn't cosmetic,
a small format slip means zero chapters ship, not degraded ones.

**How to apply:** every time chapters are requested for any WWD video
(FrostCast, reviews, Den Files, Retro Watch), read
`wwd-frostcast-chapters/SKILL.md` fresh before writing the list, even if the
format feels well-known from having done it before. Content (where subject
changes happen) can come from actually reading the transcript, but the
OUTPUT FORMAT itself must be re-verified against the skill file every time,
not reproduced from memory. This generalizes beyond chapters — any skill with
a locked exact-format spec (audio-cut's Start/Cut list, show-prep's per-topic
structure) deserves the same re-check-before-writing discipline, not just a
one-time "I know this" assumption.

## wwd-show-prep: full read-up material AND quick bullets, every time [2026-09-16]

The `wwd-show-prep` skill's format drifted thinner on 2026-09-15 (flat
What happened/Why it matters/Numbers/History/Colour list, no run-order table,
no before-you-go-live checklist, no direct critic quotes) compared to the
richer EP109/110 "RUN SHEET" style Zac was used to. He caught this live,
36 minutes before EP112's taping, and it forced a scramble to re-research and
patch the doc while Word already had the old version open and locked.

His exact standard, given directly: "I want all the information so I can
read up on it and then some bullet points to get my memory going." Both
halves are required on every topic — the full sections for reading ahead of
air, PLUS a short "Quick hits" bullet list (3-5 compressed facts) at the end
of each topic for glancing at live without re-reading paragraphs. Neither
one alone satisfies this; a prep sheet with only bullets has no depth to
read up on, and one with only paragraphs is too slow to scan live.

**Why:** the whole point of show prep is dual-purpose — study material
beforehand, quick-reference during the live show. Optimizing for only one of
those isn't fixing the format, it's swapping one incomplete version for
another.

**How to apply:** `wwd-show-prep/SKILL.md` now requires a "Quick hits"
section per topic (locked in the skill file directly, 2026-09-16). Also
still owed: restoring the RUN SHEET structural elements (run-order table
with timing/leads, "before you go live" checklist, block-by-block framing)
that the 2026-09-15 rewrite dropped — promised to Zac same night, not yet
built back into the skill file itself as of this entry. Check the skill file
before assuming this got done.


## Shorts factory (Part 2), installed 2026-10-14

Review shorts are now BUILT, not just cut. Source of truth is `.claude/skills/wwd-review-pipeline/shorts-factory.md` plus `scripts/build_short.py`. Zac's trigger: the old shorts "looked like they were just cut up, no other build to it."

- Five clips max, all finished, ship floor 7. No HOLD FOR RE-TRIM. The old reason (block-level timecodes can't resolve mid-block in-points) was wrong, silencedetect (-32dB, 0.28s) solves it.
- Length: YouTube Shorts and Instagram Reels are 3 min now (Oct 2024, Jan 2025). Working target 30 to 75s, floor 20s. Facebook Reels unverified, assume 90s. The old 59s Instagram cap is retired.
- Every clip: blurred-fill 1080x1920 (never center crop), burned-in Poppins captions, timed hook text, film tag strip, cover PNG plus one-frame prepend. Output doc is `[Title] - Shorts Captions.md/.docx`, replaces shorts_manifest.txt.
- Gotcha found in testing: the one-frame cover clip carries about 1s of silent audio unless capped with `-t 0.0334`, which breaks head-silence QC and adds a second of length.
- Gotcha: PowerShell 5.1 `Set-Content -Encoding utf8` writes a BOM, so JSON specs are read with utf-8-sig.
- Additions beyond Zac's spec (flagged for veto): film tag strip, hook fade, background darken, -14 LUFS loudness normalize.

## Review placement reports need a fun layer with sound (2026-10-14)
Zac on the Carrie report: "where is the fun... where is the cool thing that happens with the poster... sound effects... music prompts for Suno... a Firefly prompt for the nomination sticker." The first Carrie report was dissolves only. **Why:** reviews are entertainment, and Other Mommy's melt and blood close set the bar. **How to apply:** every placement report gets the fun layer described in `premiere-transitions.md` (5 built moments, timecoded SFX cue map, Den Kit, Suno prompts, Firefly sticker prompts). Wolfie Awards sticker is the recurring graphic. Research limit: web searches gave general SFX principles plus Dead Meat's awards bit and CinemaSins' breaking counter, no frame-level channel teardowns.

**Tone rule on top of the fun layer (2026-10-14):** Match the tone of the movie, not just the joke. The fun comes from the hosts' lines, but the sound underneath must fit what is on screen. No comedy music or cartoon sounds over death, abuse, bullying violence or school-shooting talk. Dry and dark beats funny there: a silence, a heartbeat, a low hit, or no cue at all. Zac's example: no Benny Hill chase music while counting dead bodies. **How to apply:** before listing any sound cue, ask what is on screen and what is being said; if it is a death, abuse or violence beat, use horror sound or silence only.

**Transition variety, 2026-10-14:** Zac said 90% of the Carrie report was Cross Dissolve, hard cut and Film Dissolve and Premiere has more. My old skill note wrongly said he was on Adobe defaults only. **How to apply:** use Adobe's Modern transitions (Impacts set, names in `premiere-transitions.md`), about half of placements, matched to the picture, each paired with a sound, no back-to-back repeats. He also wants verdict stickers (Recommend Watch, Do Not Watch, Dumpster Fire) with timestamps, used only where a host says it. Open: the exact name of his own glitch transition (third-party, not on Adobe's list).

## Posting Checklist is part of every review's shorts package (2026-10-15)
Zac: the checklist should be part of the posting package for all review videos. shorts-factory.md Section 11 footer now requires a dated table (day, clip path, cover, YT/IG/FB times, tick boxes) plus click-by-click YouTube Studio and Meta Business Suite steps. Why it was missing: the footer was only a 3-line schedule. Posting is manual: Composio is cloud-side and cannot read L:\, YouTube API quota was exhausted 2026-10-15, Meta composer can't take automation uploads. Use asset_id=104052046075172 for the Winter Wolf's Den page.


## Stay on the movie in shorts and packages (LOCKED 2026-10-19)
Zac, on the Street Fighter package: the short about animating the DCU was a tangent, swap it for something about the movie, and when we do a review keep it about the movie. Rule 14 in wwd-review-pipeline SKILL.md, plus WWD/CLAUDE.md. Replaced with Not For Me Until It Was (WWE cast worry turned respect for the games), Game Details (bonus stage car, announcer voice), kept Momoa as Blanka, Bison Raul Julia line, and Watch Again. Dropped Mortal Kombat 2 from tags, the DCU from the description and a chapter title.

## Upload package hard rules (locked 2026-10-19, Zac)
- Cards: ALL inside the first 3 minutes. Average viewers only watch that far. Outro mentions go on the end screen.
- Hashtags: exactly 5 on YouTube, never more (YouTube penalizes channels over 5). High-volume discovery tags only (franchise, movie, MovieReview, star name). Never channel-branded tags like #FrostCast. Both were missed in the first Street Fighter package, fixed same day. Rules live in wwd-review-pipeline SKILL.md Sections 5 and 10.
- Teasers, not verdicts (2026-10-19, Zac): FB/IG posts and the description opening never state the hosts' verdict. Hook only, so people still need to watch. Copy must go through copywriting + social-media (via marketing-director) and no-ai-slop BEFORE it goes in the report; I had been hand-writing it. Rules 15 and 16 in wwd-review-pipeline SKILL.md. Open: the description's QUICK ANSWERS block gives verdicts for GEO, conflicts with this, Zac to decide.
- Instagram images (2026-10-19, Zac): ratio must be 4:5 to 1.91:1 and all images in a post share one ratio. He posts the thumbnail (16:9) with the Firefly picture, so Firefly prompts are 16:9 horizontal. Never vertical/square. In wwd-review-pipeline Section 9.

## Mass record of two shows (2026-10-20, Zac)
- Layout: one folder `Raw Footage\mass record <titles>\` holds the raw `Untitled recording.mp4`, the King-Z and Winter Wolf StreamYard webcam mp4s, and one subfolder per show with its transcript. Each show subfolder gets its own `USE\`. Assets built for a show go in their own folder under `P:\WWD Kit\<Show>\`, never mixed.
- Transcripts from Premiere label hosts Speaker 1 = Winter Wolf, Speaker 2 = KingZ (confirmed by Zac). Zac cuts the big banter first, the transcript timecodes match the assembly cut, small cuts remain, so anchor every stop on search words.
- Tone per show: Zac picks it when he hands over the folder (Crystal Lake straight-forward for the Friday the 13th franchise, Vision Quest tech-y for the AIs). Build kit pieces to match (spoiler card, boot opener, AI tags), all original looks.
- Built with `scripts\make_wk_kit_cl_vq.py` (kit) and `D:\WKP\scratch\mass_cl_vq\rs_*.py` (run sheets, finds each stop by transcript words and checks no repeated picture, 7 s holds).
- Host requests spoken on camera become kit pieces: Winter Wolf asked for a counter every time KingZ says a wrong name for Spader, so there are Wrong Name Counter clips 1 to 3 (Kevin, David, Dave).


## Run sheet standing items (Zac, 2026-10-20)
- Zac already has a Spoiler Alert clip he uses every time. Do NOT build a new one in kits. In run sheets just say where it goes. **Why:** I built new Spoiler Alerts for Crystal Lake and Vision Quest that he did not need. **How to apply:** skip it in make_wk_kit scripts, mark the stop as 'your Spoiler Alert'.
- Zac has a Like and Subscribe video. Every run sheet must say what time or which line to drop it in. **How to apply:** add one LIKE AND SUBSCRIBE stop per run sheet, in timeline order. Do not build the clip.
- No new documents or rework of the two current run sheets right now (Zac, 2026-10-20). Applies going forward. See [[visual-media]].

## Crystal Lake opening scare (Zac, 2026-10-20)
19.0 s opener starting at 0:01: canoe girl, show poster leaps from the lake and drags her under, she just vanishes (no blood). Homage to the canoe scare in Friday the 13th (1980), not Part 3 (that one is Pamela's body). Option 1 built in code (make_cl_opening.py, P:\WWD Kit\Crystal Lake\). Option 2: Zac generates Firefly plates, Claude composites the real poster, sound and cuts (the Adobe connector here has no Firefly generation). **Why:** AI video garbles poster text, so the poster is always composited from the real PNG. **How to apply:** for any "make a shot" ask, build the free fallback first, give Firefly prompts for the realistic version, and flag run sheet re-timing. See [[visual-media]].
