---
name: missing-skills
description: wwd-video-upload-package and wwd-shorts-clip-factory are named in WWD/CLAUDE.md and director routing but do not exist as installed skills on this machine
metadata:
  type: project
---

WWD/CLAUDE.md's Related Skills section and the wwd-director routing steps
both name `wwd-video-upload-package` and `wwd-shorts-clip-factory` as the
tools for a "full work up." Neither has ever existed as an installed skill
folder under `D:\WKP\.claude\skills\` (confirmed by directory listing
2026-08-31 — only `wwd-video-transcriber`, `wwd-frostcast-chapters`,
`wwd-broll-prep`, `wwd-review-photo-pull`, `wwd-audio-cut`, and others
unrelated to this pair actually exist).

Hit 3 times now: The Last House package (~2026-08-10), FrostCast EP103
(2026-08-20), and Good Boy (2025) (2026-08-31). Each time worked around by
hand-building the package from the relevant `formats\<TYPE>.md` spec plus
the skill's own description text in CLAUDE.md's Related Skills section —
this produces materially the same output shape (SEO title, GEO description
with chapters, tags, hashtags, thumbnail concept, shorts candidates, FB/IG
posts, end screens/cards, posting schedule) each time, so the hand-build
process itself is now a reliable stand-in even without the real skill.

Queued formally as decision WWD-2026-08-31-01 in `logs/DECISIONS.md` after
3 uncaught recurrences — prior 2 runs flagged it in the session log but
never escalated it as a queued decision the way the devils-advocate gap got
queued (see WWD-2026-08-20-01, which got resolved by actually building the
agent).

**Why this matters:** per the MISSING SKILLS rule in CLAUDE.md ("flag, do
not fake... queue a decision"), this should have been queued the first
time. Not escalating it let the same gap get rediscovered from scratch
twice.

**How to apply:** don't rediscover this — on any WWD full work up, assume
these two skills are still missing unless a fresh `Glob` of
`D:\WKP\.claude\skills\` shows otherwise, go straight to the hand-build
workaround, and point to WWD-2026-08-31-01 rather than re-flagging or
re-queuing. For `wwd-shorts-clip-factory` specifically: actual clip cutting
with ffmpeg against a real source video is very doable by hand in a
director session (see [[raw-capture-files]] for the Good Boy run's
end-to-end proof) — don't assume "no skill" means "can't produce real cut
files," only that the packaging/scoring/captioning steps have to be done by
reading formats\SHORTS.md directly instead of invoking a tool.
