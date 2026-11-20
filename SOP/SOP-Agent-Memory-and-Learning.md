# SOP: Agent Memory and Learning

Created 2026-11-19 (system reset). Zac: "I thought we built a memory for everyone and these agents are supposed to learn and get better so I can be less in the loop."

What was there before today: one shared memory index (`memory\MEMORY.md`) that only 1 of 62 agent specs told the agent to read, no per-agent lessons files, and a self-improvement loop in AGENT-NETWORK.md pointing at a folder that did not exist (`memory\topics\lessons\`). Agents started every job cold. This SOP replaces that loop.

## Where memory lives

| Layer | File | Holds |
|---|---|---|
| Shared index | `D:\WKP\memory\MEMORY.md` | one line per learning, pointers to detail files |
| Shared detail | `D:\WKP\memory\topics\*.md`, `D:\WKP\memory\feedback-*.md`, `project-*.md` | Zac's standing corrections and project facts |
| Per agent | `D:\WKP\memory\agents\<agent-name>.md` | that agent's own lessons, newest at the bottom |
| Agent working reference | `D:\WKP\.claude\agents\_spec\<agent>-reference.md` (music, graphic-design, wwd-color, wwd-vfx) | craft knowledge the agent keeps current |
| Decisions | CLAUDE.md files | what Zac decided (not learnings) |

Never write memory to `C:\Users\...\.claude\projects\` (junction). Always `D:\WKP\memory\`.

## Before every job (2 minutes, every agent)

1. Read `D:\WKP\memory\MEMORY.md` (the index only). Open the pointers that touch this job.
2. Read your own lessons file `D:\WKP\memory\agents\<your-name>.md` in full (keep it short so this stays cheap).
3. Read `D:\WKP\SOP\SOP-Output-Locations-and-Formats.md` for where your output goes.
4. Set your budget (time, tokens, $0 unless Zac approved).

## After every real job (3 minutes)

1. Row in `D:\WKP\logs\agent-runs.md` (did, verified, not verified, budget).
2. ONE dated lesson appended to your lessons file:
   `- YYYY-MM-DD | <lesson, one imperative sentence> | evidence: <file, log line or QA finding> | NEW`
   No lesson that only repeats a spec rule. Nothing learned? Write `- YYYY-MM-DD | no new lesson | job: <name>`. That line still proves the loop ran.
3. In the hand-back, a four-line after-order note: Order, Worked, Missed, Try next.

## Zac corrections (same turn, no exceptions)

1. Whoever is corrected (or Jarvis, when the correction comes in conversation) writes it as a lesson in the affected agent's file, status `CONFIRMED` (Zac said it, so it needs no review).
2. If it is a standing rule for more than one agent, also write `memory\feedback-<topic>.md` and one pointer line in `memory\MEMORY.md`.
3. If it changes a format or path, update `SOP-Output-Locations-and-Formats.md` and the owning skill or spec the same turn. A rule that lives only in memory is how the 4 s clip limit and the 15 s intro survived after Zac changed them.

## Same mistake twice means a spec edit

- An agent that sees the same lesson (or the same QA FAIL reason) twice in its file marks the second one `REPEAT`.
- Its director (or Jarvis when there is no director) makes a small spec edit the same day: one line in the spec's "Memory and learning" or relevant section, and a line in `logs\jarvis-delegation.md` naming the spec and the reason.
- Agents never edit their own spec or another agent's spec. Directors edit their benches. Jarvis edits directors.
- Zac does not approve these small spec edits (he said 2026-11-19 not to bring this to him). A change that alters a Zac-locked rule is not a small edit and goes to DECISIONS.md.

## Director review

When a director accepts work, it marks each NEW lesson in the bench's file `CONFIRMED`, `EDITED` (rewrite it), or `REJECTED` (one line why). One pass, no loops.

## Weekly (Monday, with the brief)

- Jarvis or chief-of-staff reads every lessons file changed that week.
- REPEAT lessons: confirm the spec edit happened.
- Lessons older than 60 days still `NEW`: retire (`RETIRED`).
- One line in the Monday brief: lessons written, repeats, spec edits made.
- qa-auditor counts send-backs and QA first-pass rate against last week.

## Size rule

Lessons file over 40 lessons: the director folds confirmed lessons into the spec and moves the old lines under `## Archive` at the bottom. The file an agent reads stays short.
