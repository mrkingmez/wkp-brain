# Drill 1: head-editor, pre-post QA of three finished reviews

Written 2026-11-22 BEFORE the run (pass bar fixed first). Agent: head-editor. Grader: qa-director (qa-media bench), Jarvis spot-check. The agent never signs.

## Task
Three finished reviews on disk, no spend, nothing posted:
1. Godzilla Minus Zero: `L:\Winter Wolfs Den review show\Raw Footage\Godzilla Minus Zero\Godzilla Minus Zero -  Review - All Hail the King! ed.mp4` (1733.6 s)
2. Vision Quest EP 7: `L:\Winter Wolfs Den review show\Raw Footage\Vision Quest\EP 7\Vision Quest Review EP 7 FINAL export.mp4` (1435.5 s)
3. Vision Quest EP 8: `L:\Winter Wolfs Den review show\Raw Footage\Vision Quest\Vision Quest ep 8\Vision Quest- Ep8 Is it the best MCU show to-date.mp4` (1666.9 s)

Run a pre-post QA with ffprobe, an ffmpeg loudness measurement, a black-frame check and a repeated-picture check. List defects.

## Contamination note (honest)
The agent had read the Zac Style Sheet (2026-11-19) before the run, which names the Godzilla repeated picture and black tail. The grader's blind list cannot be fully blind for the agent. To compensate: the repeat and black checks are run by method (scripts in `D:\WKP\scratch\hed-level\`), results are compared to the Style Sheet and any NEW finding or any disagreement is reported, and the grader holds extra defects not in the Style Sheet. Treat a pass as weaker than a blind pass.

## Pass bar (6 criteria, pass = 5 of 6, criteria 1 and 2 CRITICAL)
1. CRITICAL. Finds both known Godzilla defects (repeated picture, black tail) by measurement, with timestamps within 2 s of the grader's list.
2. CRITICAL. Measures loudness for all 3 videos with the ffmpeg command printed in the result, giving integrated LUFS and true peak per file.
3. Cites the loudness standard with a verbatim quote, URL and retrieved date, and states what the quote does NOT prove (YouTube figure is third party, Google publishes none).
4. No claim about frames, sound or timestamps that was not measured or viewed; each unviewed part says "not viewed" or "not heard".
5. Fix list ordered by Zac time (smallest fix first or biggest harm first, stated), each fix one action Zac can do.
6. Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED (SOP Part 7).

Result file: `D:\WKP\SOP\leveling\drills\head-editor-drill-1-result-2026-11-22.md`.
