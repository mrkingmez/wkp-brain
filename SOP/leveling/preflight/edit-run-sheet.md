# Pre-flight: Edit run sheet (assistant-editor, and any agent building one)

Created 2026-11-22 from the Craft Brief and the gap audit (`memory\agents\briefs\assistant-editor-*.md`) and drill 1. Paste into the hand-back with each item ticked and a one-line proof. One unticked item and it does not go to Zac. Every instruction carries PROVEN, SOURCED or PROPOSED.

1. [ ] Transcript is the LATEST file in the movie folder (ls with dates) and its end time is within 15 s of the newest export or sequence length. Proof: both numbers written in the header. (Gap 1)
2. [ ] Every stop quotes a "Said:" line copied from the transcript and the stop time falls inside that block (`scratch\leveling-drill1\check1.py`, 0 fails).
3. [ ] No picture used twice and every picture file exists in USE on disk (check1.py). Pictures named in the tag file but absent from disk are listed by number.
4. [ ] Each picture matches the line by the tag file (who or what it shows). A picture of a specific thing sits on the line that names it. A second person reads 3 stops.
5. [ ] No picture over 7 s, no CONTEXT or OTHER-TITLE picture claims more than its tag says, no name tags on screen.
6. [ ] Lint exit 0 (`.claude\skills\wwd-review-photo-pull\scripts\lint_run_sheet.py`), warnings listed.
7. [ ] Gap list: every stretch over 25 s with no picture has start, end, seconds, total, and a PROPOSED fill or "talk-led, none needed" (check1.py).
8. [ ] Sound lines: each file exists at its source path; copies are in the sound pull folder; loose mp3s with no license on file are named and flagged.
9. [ ] Loudness and black tail: if an export exists, measured integrated LUFS, LRA, true peak and the black tail with the commands (ffmpeg ebur128 and blackdetect). Compared to the lock (-14 LUFS, -1 dBTP, 1 s) and labeled "Zac's lock" for -14 (EBU R 128 states -23.0 LUFS and -1 dBTP, source S2; the YouTube loudness page is NOT RETRIEVED). If no export, the commands are written.
10. [ ] Every Premiere menu path or shortcut is from fact-research for Zac's version or marked NOT VERIFIED. Nothing says a sound or a cut was heard or viewed unless it was.
11. [ ] Zero em dashes (grep count) and slop_check exit 0 on any public-facing line.
12. [ ] Pacing against the style sheet: no stretch over 60 s without a picture, cam break or card. Any gap over 60 s gets a concrete fill (never 'none needed'). Designed transitions at or under about half of the stops, sound files varied, Adobe SFX preferred over loose mp3s. (head-editor grade note, drill 1)
13. [ ] Hold ends on or before the end of the line it illustrates. Picture starts on the distinguishing word (a picture of a detail goes on the line that names the detail).
14. [ ] Ledger row and lesson written.
