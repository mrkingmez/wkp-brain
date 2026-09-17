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
