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
