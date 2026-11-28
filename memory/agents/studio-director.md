# Lessons: studio-director

Read this whole file plus `D:\WKP\memory\MEMORY.md` before every job. Append one lesson after every real job.
Rules: `D:\WKP\SOP\SOP-Agent-Memory-and-Learning.md`. Spec: `D:\WKP\.claude\agents\studio-director.md`.

Format: `- YYYY-MM-DD | lesson, one imperative sentence | evidence: file, log line or QA finding | NEW, CONFIRMED, EDITED, REJECTED, REPEAT or RETIRED`

## Seeded 2026-11-19 (system reset, from memory files and locked rules)

- 2026-11-19 | Spend no credits: Veo and Firefly credits are at zero, work from what is on disk | evidence: memory\project-ian-trailer-settled.md | NEW
- 2026-11-19 | Nobody can hear audio: say 'not heard' for every sound claim | evidence: agent-runs.md rows 2026-11-17 and 2026-11-18 | NEW
- 2026-11-19 | Ian trailer is a free favor for a friend; never list it as a cash source | evidence: memory\project-ian-trailer-free.md | CONFIRMED
- 2026-11-19 | Ian trailer: no credits, V4 cut, cover is its own story piece, Adobe SFX free, ElevenLabs only with Zac's yes | evidence: memory\project-ian-trailer-settled.md | CONFIRMED

## Lessons
- 2026-11-19 | Re-signoff found studio-director.md still said "Not yours" for WWD; reworded to "Not your gate": wwd-director owns WWD, the editing department does the prep job, studio-director neither gates nor logs it | evidence: readiness pass re-signoff 2026-11-19 | NEW
- 2026-11-20 | Space YouTube caption pulls at 40 s or more; 429s began after about 8 pulls and two retries 3 minutes apart still failed, so pick 2 or 3 spare sources up front and log blocked ones honestly | evidence: Post-Production\research\editing-study\sources.md (17 of 19 pulled) | NEW
- 2026-11-20 | Grep the venture's STANDARDS.md and the owning bench's spec before calling something a missing target; send every draft through head-editor before QA (its notes caught the loudness standard, a recipe that would ghost the hosts through a poster, and two rule clashes) | evidence: head-editor notes 2026-11-20 on Post-Production\reports\Zac-Style-Sheet-2026-11-19.md | NEW
- 2026-11-20 | Read the full locked-rule list (WWD\STANDARDS.md items 1 to 12) before proposing any pacing rule; 'cut to solo cam on every long turn' broke the locked 'a few solo cams, only on a good point' rule and failed QA | evidence: logs\qa\2026-11-20-zac-style-sheet.md B1 | NEW
- 2026-11-20 | Write python helpers with the Write tool and run them by path, not through Bash heredocs: a heredoc turned a double backslash into "\r" and corrupted a memory file path, and an earlier one-line regex commit wiped three TASKS.md tables; diff TASKS.md before every commit | evidence: memory\project-ian-trailer-settled.md fix and commit 6711cc5 restore, Ian Draft 3.3 | NEW
- 2026-11-20 | Run the cheap devils-advocate gate before ordering prompts or builds: it cut three of six NEED shots and caught a fence leak in the memory beat before any desk spent time on them | evidence: Post-Production\projects\ian-trailer\2026-11-20-devils-advocate.md | NEW
- 2026-11-22 | Leveling job: read and quote the story or brief source file before writing any fence, and never overrule a clearance STOP myself, queue it for Zac; keep every credit cost NOT RETRIEVED until read at the tool | evidence: memory\agents\briefs\studio-director-craft-brief.md, gap-audit.md, failures\studio-director.md (2 OPEN), drill 1 submitted UNGRADED | NEW
- 2026-11-22 | Source fetching: support.google.com, copyright.gov and tech.ebu.ch PDFs fetch fine with curl, Adobe helpx and Pixabay return 403 and Netflix partner help is a JavaScript shell; write NOT RETRIEVED, do not recall | evidence: scratch\sd-level\ raw pages | NEW
- 2026-11-22 | A line that leans toward the secret, even a public blurb, is a queued question to the client via Zac, never my ruling | evidence: drill grade FAIL criterion 1, failures\studio-director.md | NEW
- 2026-11-22 | Compare the client deadline to the gates (two script passes, one send-back per desk) and name any conflict with a queued decision | evidence: drill grade criterion 7 | NEW
- 2026-11-22 | Tag every table row, decision and client request PROVEN, SOURCED or PROPOSED; third slip on tags | evidence: drill grade criterion 8 | REPEAT
- 2026-11-26 | STANDING RULE: when a tool or source fails, try the other connected route (other browser, other connection, other source) before escalating; only Zac's money and public posting are hard stops; never spoof headers or user agents to get past a block (say it plainly in the report if no other route exists) | evidence: Zac 2026-11-26, wwd-pictures PJ S3 follow-up (no browser step ran, agent-runs.md 2026-11-26) | NEW
