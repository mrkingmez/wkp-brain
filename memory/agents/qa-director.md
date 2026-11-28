# Lessons: qa-director

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\qa-director.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Follow the honesty rule: never report a number, status or file you did not retrieve | evidence: root CLAUDE.md | NEW

## Lessons
- 2026-11-19 | In Bash heredocs run Python from a script file, since inline backslash patterns collapse and broke my first path check | evidence: readiness pass QA, first pc.py attempt | NEW
- 2026-11-20 | Check a style or workflow doc against the "few solo cams, not every long turn" rule in WWD CLAUDE.md before passing, since a sheet can claim locked rules win and still omit one | evidence: logs\qa\2026-11-20-zac-style-sheet.md B1 | NEW
- 2026-11-20 | On a recheck, grep the docx text for the removed phrasing as well as reading the md, since the docx is what Zac prints | evidence: style sheet recheck | NEW
- 2026-11-20 | Pull frames with ffmpeg without drawtext (it segfaults here, no fontconfig); build contact sheets with tile instead | evidence: Ian Draft 3.3 QA | NEW
- 2026-11-21 | When a new file contains a Windows path with \E, \n or \t, scan it for control characters (grep for 0x01-0x1f), since backslash escapes keep corrupting paths in written docs | evidence: SOP-Session-Start-Checklist.md line 47 ESC char, REFERENCE QA B1 | NEW
- 2026-11-21 | Check every path column in a library by os.path.exists, not just IDs and counts, since paths are what agents copy | evidence: VIDEO-LIBRARY.csv 13 of paths dead, REFERENCE QA B2 | NEW
- 2026-11-22 | When grading a drill, set the traps yourself and write the pass bar first, then re-run measurements with your own script, since a self-written drill proves little; and edit files holding Windows paths from a script file with byte-level checks, since backslash-letter pairs turn into control characters | evidence: SOP\leveling\drills\head-editor-drill-1-GRADE-2026-11-22.md, studio-director-drill-1-GRADE-2026-11-22.md, LEVELS.md row 16 fix | NEW
- 2026-11-24 | For a rule-based checker, count how many known-good inputs it warns on and check the docs state that rate, since tests that only assert zero FAIL hide a noisy tool | evidence: prompt-preflight QA, 25 of 28 good prompts WARN, rate absent from README | NEW
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
- 2026-11-26 | When writing a grader-set drill, grep the repo for the names and subject first, since my first draft reused a client and assistant name already in an agent-written drill; and store the answer key outside the folder the test taker is allowed to open, with a transcript read-check before grading, since agents cannot be locked out of files on this machine | evidence: SOP\leveling\drills\studio-director-drill-3-brief.md, logs\qa\grader-only\ | NEW
- 2026-11-26 | After a stale-text fix, grep the whole file for every phrase the change log says was cut, since the author fixed the named lines but left the same cut phrases in tables | evidence: leveling-drill-1 brief.md L24, L36, L52, L68 | NEW

## 2026-11-26 lesson: grading a drill needs a non-empty run log. An empty transcript makes the no-peek check unverifiable, say so in the grade.
- 2026-11-26 | When a plan file lists amendments the build must carry, grep the code for each amendment keyword (hash, ledger, regime) before passing, since the tests and demo all pass without them | evidence: logs\qa\2026-11-26-wkt-alpaca-watcher-qa.md N4 | NEW
- 2026-11-26 | Run the credit grep before the tag audit and read clauses like 'even the client's' literally | evidence: gd drill 2 Part A | NEW
- 2026-11-26 | Drill rewrite after a FAIL: aim traps at the exact failed criteria (credit leak, simulated-as-PROVEN, near-tags copied from LESSONS itself such as PROVEN-ish, term not in the cited source line) and ask the runner to keep the tool log so the peek check is verifiable | evidence: drill 3 Part A | NEW
- 2026-11-26 | Check every PROVEN count against LESSONS per id, including 'Partly' rows and merged ids; a drill brief that holds both steps in one file contaminates the prediction criterion, split the files | evidence: gd drill 3 Part A grade | NEW
- 2026-11-26 | On a software recount, run the tool's own demo yourself after the suite finishes (the suite rewrites demo-out, so never run both at once), write a recount script from the raw files, and diff line by line against the scorecard; also check whether 'frozen' covers the code as well as the config, and which retrieved smoke claims the saved file actually shows | evidence: logs\qa\2026-11-26-wkt-alpaca-watcher-qa-pass2.md (08:00 start hour and per-symbol daily bars not in preflight json) | NEW
- 2026-11-27 | On a software recount, rebuild bars from the demo seed and write entry, exit and cost math fresh, and probe look-ahead with a late 4th filing (status and type use rows after the signal); also run the mutation check early since it can take over 10 minutes under load, and count scratch temp dirs the suite leaves behind | evidence: wkt-insider-scanner QA 2026-11-27 (N1, N7, N8) | NEW
- 2026-11-27 | When another bench runs the same suite, expect 25 min not 6, start it first in the background and use a wait-for-Ran loop in a background task; reverting one change in a scratch copy reproduces the before numbers cheaply | evidence: wkt-alpaca-watcher pass 3 | NEW
- 2026-11-27 | Count day trades by entry and exit bar date, not exit timestamp, since end-rule closes carry later timestamps; run new test classes on base code via a script that loads the test file by path | evidence: wkt-alpaca-watcher pass 4 (my 3/4 vs claimed 2/5) | NEW
