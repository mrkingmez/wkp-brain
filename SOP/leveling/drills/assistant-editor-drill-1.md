# Drill 1: assistant-editor (replay: Vision Quest EP 8 run sheet)

Written 2026-11-22 BEFORE the run, by assistant-editor. Standard: `D:\WKP\SOP\SOP-Agent-Leveling.md` part 3. Launch file: `D:\WKP\SOP\leveling\assistant-editor.md`.
Cost: $0, no credits, nothing posted, no source media modified. Output goes to `D:\WKP\scratch\leveling-drill1\` only. The shipped sheet (`D:\WKP Reports\Asset Placement Run Sheets\2026-11-17 - Vision Quest EP 8 Edit Run Sheet.docx`, md `D:\WKP\WWD\reports\Vision-Quest-8-Edit-Run-Sheet.md`) is the comparison, not the input.

## Disclosure (contamination, stated before the run)
Before this file was written the agent read the first 60 lines of the shipped .md (its preamble, rules and stops 1 to 3). Format and rules (7 s picture cap, no picture twice, -14 LUFS, Cross Dissolve limit) are therefore known. Stop placements beyond stop 3 were NOT read. Grader: treat stops 1 to 3 comparison as not independent.

## Inputs
- Transcript: `L:\Winter Wolfs Den review show\Raw Footage\Vision Quest\Vision Quest ep 8\Vision Quest ep 8 final .txt` (the FINAL transcript, 2026-11-17 22:38). The shipped sheet was built from the earlier `Vision Quest .txt`. Differences are expected and are reported, not penalised.
- Pictures: the numbered PNGs actually present in `...\Vision Quest ep 8\USE\` on 2026-11-22 (24 numbered files, not the 31 the tag file and launch file name; 7 are absent from disk). Tags from `USE\pictures-tags.md`. Not read: `USE\timeline-placements.md`.
- Owned sounds: P:\ (Adobe SFX library and loose mp3s) via `D:\WKP\data\assets\p-drive-index.csv` and media-map.

## Task
Build an Edit Run Sheet (.md, same stop format as the lint script expects) for the final cut: every picture placed on the spoken line it is about, with a search phrase copied from the transcript, plus a Sound line per stop where a sound is used, a gap list, loudness and black-tail checks, and a sound pull into a scratch Sounds folder (copy, never move).

## Pass bar (numbered, each PASS or FAIL). Pass = 6 of 7, with 1 and 2 CRITICAL.
1. CRITICAL. Every picture stop has a timecode that lands on the spoken line in the transcript: the stop's quoted "Said:" text must appear verbatim in the transcript and the stop time must fall inside that block's start to end (script `D:\WKP\scratch\leveling-drill1\check1.py`, written before the run and not changed after). 100 percent of stops, no exceptions. A stop whose picture does not match its line by the tag file is also a FAIL.
2. CRITICAL. No picture file used twice, and every picture used exists in USE on disk (script check).
3. Sound pull folder matches the run sheet: every file named in a Sound line exists at its source path, a copy sits in the scratch Sounds folder, and file count in the folder equals unique files named. Any unlicensed loose mp3 is flagged by name.
4. Lint passes: `python D:\WKP\.claude\skills\wwd-review-photo-pull\scripts\lint_run_sheet.py <sheet>` exit 0 (warnings allowed, listed).
5. Gaps listed with durations: every stretch of the cut longer than 25 s with no picture on screen is listed with start, end and seconds, and the total is stated. Arithmetic checked by script.
6. Loudness and black tail checks listed WITH numbers retrieved: ffmpeg ebur128 integrated LUFS and true peak, and blackdetect on the last 15 s, read from the final export that exists on disk (read-only), against the lock (-14 LUFS, -1 dBTP, black tail 1 s or less). If the file cannot be read, write "not available" and the reason, which counts as PASS only if the check steps are written.
7. Every instruction handed to Zac carries PROVEN, SOURCED or PROPOSED, and no sound claim says it was heard (say "not heard").

## Informational (not scored)
Compare to the shipped sheet: stop count, pictures used, mean time difference on shared pictures, pictures the shipped sheet used that this one did not and the reverse. Compare to the style sheet `D:\WKP\Post-Production\reports\Zac-Style-Sheet-2026-11-19.md`.

## Graders (never the agent)
head-editor for craft (criteria 1 placement fit, 5 gaps, 7), qa-director for file checks (2, 3, 4, 6). Result file beside this one: `assistant-editor-drill-1-result.md`.
