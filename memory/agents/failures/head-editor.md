# Failure ledger: head-editor

Format per `SOP\SOP-Agent-Leveling.md` part 5. Opened 2026-11-22 in the leveling job, from evidence already on disk, not the turn the failure was known. Stays OPEN until the Re-drill line is filled by a grader-signed pass.

## 2026-11-20 | Zac Style Sheet draft, loudness target called missing | cost: a QA note and a rewrite of the loudness text, time NOT KNOWN
- What happened: the draft said loudness had no set target while `D:\WKP\WWD\STANDARDS.md` line 48 already locks -14 LUFS and -1 dBTP. Caught on the notes pass (my lessons file 2026-11-20). Final sheet states the standard on Page 1.
- What the maker's guidance said: no source says what a channel's standard must be. Searched 2026-11-22: EBU page (-23 LUFS, +/- 0.5 LU, broadcast), Frame.io guide ("YouTube doesn’t release exact values, but YouTube tends to shoot for -12 to -14 LUFS."). Neither replaces looking at the house standard file first.
- What we did instead: wrote "no set target" from memory of the earlier notes without opening STANDARDS.md.
- Root cause: skipped checklist item, no step to read the house standard file before calling a number a gap.
- Fix: pre-flight item 3 in `SOP\leveling\preflight\head-editor-pre-post-qa-report.md` and item 3 of `head-editor-final-export-check.md`.
- Re-drill: OPEN. Drill 1 criterion 3 covers it; result `head-editor-drill-1-result-2026-11-22.md` is UNGRADED.
