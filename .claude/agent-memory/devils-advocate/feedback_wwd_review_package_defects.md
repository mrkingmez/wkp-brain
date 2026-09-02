---
name: wwd-review-package-defects
description: Recurring defect classes in hand-built WWD upload packages, and the specific checks that catch them, learned reviewing the Good Boy (2025) review package
metadata:
  type: feedback
---

WWD upload packages are built by hand because `wwd-video-upload-package` and
`wwd-shorts-clip-factory` are not installed as skills on the Main Desktop
(open decision WWD-2026-08-31-01 in `D:\WKP\logs\DECISIONS.md`). Hand-building
produces the same defect classes every time. Check these before anything else.

**Why:** three packages in a row (FrostCast EP103, The Last House, Good Boy)
came out of the same manual workaround, so the failure modes are systemic, not
one-off writing misses.

**How to apply:** run these checks on every WWD package review.

1. **Status inflation on cut clips.** "CONFIRMED DONE" plus "verified durations
   via ffprobe" only proves ffmpeg cut the requested length. It never proves the
   right words are inside the clip. If the transcript timeline was never
   reconciled to the exported video's t=0, every clip boundary is unverified.
   Demand a watched-it confirmation, not a duration match.
2. **Backend tag overflow.** YouTube caps the tags field at 500 characters
   total. Hand-built tag blocks routinely run 550 to 600 and silently truncate.
   Count the characters.
3. **Claims not in the transcript.** Social copy drifts into hype ("everyone's
   been talking about", "the sadder metaphors the guys have seen in a while").
   The transcript is the only permitted source for stats and host opinions.
4. **Speaker-count claims when diarization is absent.** Packages correctly avoid
   naming Winter Wolf or KingZ, then break the same discipline by asserting
   two-speaker dynamics ("the guys could not agree", "back-and-forth between the
   two hosts"). A transcript where every line reads "Speaker 1" cannot support a
   claim about how many people spoke, only about what was said.
5. **Transcription garbles promoted into public copy.** Voice-to-text noise
   ("Carrie Fisher" as a dog trainer, "grease creature") gets withheld
   inconsistently. Apply one standard to all uncertain proper nouns and coined
   terms from the same transcript.
6. **Three-word hook test treated as a score input.** `D:\WKP\WWD\formats\SHORTS.md`
   makes it a hard reject, not a weighting. A clip with a weak spoken opener is
   dead even at 6/10, and on-screen text is not allowed to rescue it.

Related: [[wwd-shudder-talks]].
