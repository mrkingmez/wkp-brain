# WWD Standards (one page, every WWD agent reads this first)

Single checklist of Zac's locked rules for review videos. Source of truth for the rules stays in `WWD\CLAUDE.md`. This page is the checklist version, so nothing gets missed. Created 2026-10-26 after a Clayface run sheet shipped with weak transitions and unchecked pictures.

## Pictures (wwd-pictures owns this)
1. **Every picture is verified against the transcript line it sits on.** The picture must show the thing being said: that character, that scene, that object. If the line is about the best friend, the picture is the best friend, identified from a cast tag or a caption, never "picked by look."
2. **Nothing untagged goes in.** If a face or scene cannot be identified for sure, it is left out and listed under flags. Do not place a guess and ask Zac to check it.
3. **No picture twice, and no near-twin.** Same scene from the same shot counts as the same picture. The lint runs a perceptual-hash check over the whole `USE\` folder, and a visual check by eye on anything flagged.
4. **7 seconds max on screen.** A few solo cams only, when a host makes a good point.
5. **Cover every subplot character** (Step 3.5), not just the leads.
6. **Contain/fit resize, never crop.** 1920x1080 PNG.

## Transitions (wwd-run-sheet and wwd-vfx)
7. About half of the placements get a designed Modern transition with a paired owned sound. Plain Cross Dissolve on 3 stops at most. Never the same transition twice in a row.
8. Match the movie. No comedy or cartoon sound over death, abuse or violence. Heavy beats stay plain and the sheet says why.

## Music and sound (music and wwd-sound)
9. Music is intro and outro only. No bed under the conversation. Sound effects and short stings on a gag are fine.
10. Owned sounds only, from `P:\Sounds\`. Suno tracks only on a paid plan.
11. Trailer audio is always muted.

## Trailer clips and fair use (wwd-clip-scout and wwd-rights)
12. A clip plays only under a host line about that exact scene. 4 seconds max, under 30 seconds total, never back to back.
13. No title cards, release date or studio logo from the trailer. Cut on verified shot edges.
14. The upload package keeps its fair use disclaimer as the last section.

## Documents
15. Run sheet: one timeline-order list, each stop opens with timecode, PNG or USE VIDEO or STICKER or CAM, search words, then the spoken line. Revise in place, never a second dated copy.
16. Deliverables are .docx in `D:\WKP Reports\<Name>\`, .md source in the repo.
17. No em dashes. Handles only (Winter Wolf, KingZ, Oracle). No verdicts on cards, no scores.
18. No bleeping.

## The gate
A bench hands back only after it has run its own check and written the result line in the hand-back. wwd-director proofreads second against this page, and Zac sees it last. "Done" without a check line is not done.

## Addendum 2026-10-26 (boarding check fixes)

**Who owns what (ends the overlaps)**
- wwd-vfx BUILDS sound-bearing kit pieces and drops candidate sounds in the show's `P:\WWD Kit\<show>\Sounds\`. wwd-sound CHOOSES the cue match, sets levels, and checks loudness. music owns music only (intro, outro, Suno).
- Transitions: wwd-run-sheet picks them and pairs the sound; wwd-vfx builds any custom one.
- Trailer clips are MUTED by wwd-clip-scout at conversion (Premiere Ready copy has no audio stream). wwd-sound verifies. Zac does nothing.
- "Never back to back" for clips = at least one full spoken line (about 10 s) with no clip between them. wwd-clip-scout reports times at the file's own frame rate.
- Making a Premiere Ready copy is a write step, wwd-clip-scout does it without asking but never overwrites a source file.

**Default levels (wwd-sound, until Zac sets different)**
- Music at intro/outro: about -18 dB under voice when voice is present, full only on a silent open or close.
- Effects: peak no higher than -12 dB against voice peaks. Stings on a gag may sit at -6 dB.
- Export loudness: -14 LUFS integrated, true peak -1 dB. Trailer audio "muted" = silence below -60 dB.
- Suno: tracks count as commercially clear only if made on a paid plan. Plan status is Zac's to confirm, music queues the question in DECISIONS.md, wwd-rights flags every Suno track while the plan is lapsed (lapsed as of 2026-10-26).

**Shared rules**
- Read this file first on every job, every bench. A hand-back without a check line goes back.
- Bench log format: copy the newest entry style in `D:\WKP\logs\wwd-director.md` (Status, Trigger, Actions, Deliverables, Flags).
- DECISIONS ID format: copy the newest line in `D:\WKP\logs\DECISIONS.md`.
- `USE\pictures-tags.md` columns: number, filename, who (actor and character), scene, source URL, status. Duplicate flag: dHash distance under 14 or correlation over 0.85, then look by eye. wwd-pictures may write its hash script into the photo-pull skill's `scripts\`.
- wwd-pictures has no browser. wwd-director or Jarvis gives it pull URLs, or it reports IMDb "not available". Thin releases (TMDb stills with no tags): unverified stills go to `_unverified\`, flagged to wwd-director, not guessed.
- Lint: `--max-cross` default is 3.
- Music in the owned library and sound effects come from `P:\` (Sounds\Sound FX, Sounds\Music). YouTube Audio Library music needs attribution and wwd-rights sign-off.
- Fixed ffmpeg path is in LOCAL-PATHS.md. Color scratch for real jobs: `D:\WKP\scratch\color\` (`color-test` is for sandbox only).
- Siblings: vfx, color, run-sheet, music, pictures, clip-scout, sound, rights. All report to wwd-director only.
