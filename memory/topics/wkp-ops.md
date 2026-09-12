# WKP Operating Rules

## Fire-and-forget partnership model [2026-07-24]
Take initiative, propose next steps, execute reversible actions without being
asked. Zac pulls the trigger on anything irreversible. Give real opinions and
push back with evidence rather than hedging. Buddy-cop, writer-and-editor.

## Voice-to-text is interpreted phonetically [2026-07-24]
Zac dictates constantly, often while driving. Read for intent, not literal
transcription. "roger" and "copy" both mean yes. He talks to himself during
pauses — silence is not a finished answer, so wait rather than fill it.

## Flag file updates in the moment [2026-08-03]
Standing rule, established after unmerged `CLAUDE-update` patch files were
identified as the root cause of the first Second Brain's decay. When something
in a CLAUDE.md, ME.md, projects.md, TASKS.md, or LOCAL-PATHS.md needs to change,
say so on the spot and name the file. Never let changes pile up to merge later.

## The repo is on D:, not C: [2026-08-03]
`wkp-brain` is cloned to `D:\WKP`. The printed Phase 1 guide says `C:\WKP`
throughout and is wrong on that point. Ten venture folders, one CLAUDE.md each,
no sub-folders for sub-projects. Skills live in `D:\WKP\skills\`.

## Do not hammer a rejected tool call [2026-08-06]
When the same command is rejected before execution more than twice, stop and
diagnose the approval path instead of re-issuing it. After 24+ hours and dozens
of tool calls, a session itself can go bad — a fresh session is the fix, not
another retry. Say so plainly rather than reassuring.

## Output format preferences — repeated correction, now LOCKED [2026-07-24, re-corrected 2026-09-12]
Step-by-step with every click spelled out. Plain language, no jargon.

**The .docx rule is broader than "guides."** Test: is the file needed as
an operational repo file (CLAUDE.md, TASKS.md, skill/agent defs, code)?
If yes, stays `.md`/code. If no — it's a deliverable a human reads,
prints, or ships (upload packages, reports, worksheets, tracker docs,
guides, anything "finished") — it goes out as `.docx`, `.md` kept
alongside per the file-retention rule. This got narrowed to "just guides"
in practice and WWD upload packages kept shipping as `.md`/`.txt` (Last
House, EP103, T-2) until Zac called it out again 2026-09-12 ("how many
times do I have to tell you"). Root CLAUDE.md now has this spelled out
explicitly under "Output document format" — check there, don't re-narrow
it to guides-only again.

## Secrets never go on the command line [2026-08-06]
A Hugging Face token was pasted directly into a Claude Code prompt and is now
recorded in that session's `.jsonl` log in plaintext. Tokens and keys go in an
environment variable or a gitignored file, and get passed by reference. If one
is ever pasted, say so immediately and tell Zac to rotate it.
