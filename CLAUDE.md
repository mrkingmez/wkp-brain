# WKP — Warrior King Productions
## Root context file. Read this first, always.

@./ME.md
@./projects.md
@./TASKS.md
@./LOCAL-PATHS.md

---

## What this is
Top-level routing intelligence for all WKP ventures. Any session that starts here should read ME.md, projects.md, and TASKS.md, then route to the relevant venture folder.

## Ventures and where they live
| Venture | Folder | Priority |
|---|---|---|
| Etsy — WarriorKingDesigns (puzzles + wall art) | ./ETSY/ | 1 |
| Etsy — Kingdom Planners (digital planners) | ./Kingdom-Planners/ | 2 |
| Shattered Empire novels (Books 1 and 2) | ./Shattered-Empire/ | 3 |
| Winter Wolf's Den / FrostCast / Den Files | ./WWD/ | 4 |
| Watershed / Hidden Hinge (What If) | ./WhatIF/ | 5 |
| Post Production house | ./Post-Production/ | 6 |
| Military SciFi novel | ./SciFi-Novel/ | 7 |
| RUBY TWO (WWII short film) | ./RUBY-TWO/ | 8 |
| Cyber Security (day job practice) | ./Cyber-Security/ | 9 |
| Investing challenge | ./Investing/ | 10 |

## Standing rules

**Files and source of truth**
- GitHub (`wkp-brain`, cloned to C:\WKP) is source of truth for all operational brain files: ME.md, projects.md, TASKS.md, LOCAL-PATHS.md, and every CLAUDE.md.
- Google Drive holds reference material only — manuscripts, images, spreadsheets, production bibles, PDFs. Not operational files.
- Local drives hold raw media and large files, mapped in LOCAL-PATHS.md. LOCAL-PATHS.md is per-machine and must be rebuilt on each new computer, never copied.
- NEVER create operational files through the Google Drive API. It silently converts markdown to Google Docs and breaks every @-import. Create locally in C:\WKP, commit, push.
- One folder per venture, one CLAUDE.md per folder. A piece of a venture (a cold open, a single book, a template, an episode) is a section inside that venture's CLAUDE.md, not its own folder. New folders only for genuinely separate operations.

**Task tracking**
- TASKS.md is the single task list across all ventures. New work goes in it the same turn it comes up.
- When something in a conversation should update a file, flag it in the moment — which file, what changed. Do not let updates accumulate silently. Unmerged patch files are how the Drive version of this system rotted.

**How to work with Zac**
- Fire-and-forget: take initiative, propose next steps, execute reversible actions without asking. Zac pulls the trigger on anything irreversible.
- Real opinions and pushback with evidence. Buddy-cop / writer-editor engagement, not hedged responses.
- Zac uses voice-to-text, often while driving. Interpret phonetically, not literally. "roger" and "copy" mean yes. Don't flag typos. Pauses and self-talk during voice sessions are not directed at Claude — wait rather than treating silence as a complete answer.
- Step-by-step with every click spelled out. Plain language, no jargon. Word (.docx) format for guides so they can be printed and worked from physically; save the .md too.
- Zac has ADHD. Structure helps. Keep responses tight so it's easy to snap back to task.

## Daily rhythm
- **Morning** — calendar + TASKS.md: what's on today, what's overdue, what comes first
- **Midday** — accountability: what was committed to, what's done, update TASKS.md
- **Evening** — review: what got done, what rolls to tomorrow, update TASKS.md

## Recurring commitments
- FrostCast records **Wednesdays 9pm**, weekly, does not stop for other projects
- Etsy posts new designs Monday and Wednesday: 3 physical (puzzle/canvas) on Monday, 2 digital printables on Wednesday

## Current state — August 2026
- Second Brain rebuilt on GitHub after the Drive/Google Docs conversion failure. Phase 1 in progress.
- FrostCast at episode 106. New cold open targeted for ~episode 110.
- Kingdom Planners: seven finished products, zero listings, shop not yet created. The pipeline is far ahead of the storefront.
- Den Files episode 1 (Fire in the Sky) targeted for release ~August 2026.
- CySA+ exam targeted end of August 2026.

## Memory

There is a memory system in this repo at `memory/`.

- **Session start:** read `memory/MEMORY.md`, then follow pointers relevant to
  the work at hand. Do not recite it back unless asked.
- **During the session:** when something worth keeping is learned, append it to
  `memory/topics/<topic>.md` and add a pointer line to `memory/MEMORY.md`.
- **When stuck:** grep `memory/MEMORY.md` and follow pointers to past learnings
  before troubleshooting from scratch.

**Routing rule.** Decisions go in a CLAUDE.md. Machine-specific paths go in
LOCAL-PATHS.md. Learnings go in memory. Anything Zac decided on purpose must be
written to the right file and flagged out loud the same turn it comes up.

**Never write memory to `C:\Users\...\.claude\projects\`.** That path is a
junction pointing here. Always write to `memory/`.

Full protocol: `.claude/commands/mem.md`, also `/mem show` and `/mem forget`.

Memory lives in git. Prompt Zac to commit and push before a work session ends.

## FrostCast Transcription Workflow

When Zac says an episode is downloaded, run the whole chain without asking for
details:

1. Find the episode file under the FrostCast path in LOCAL-PATHS.md
2. Launch `skills\wwd-video-transcriber\scripts\transcribe.py` against it,
   detached, on the GPU
3. Save the transcript as `.txt` in the same folder as the video
4. Return chapter timecodes when it finishes

Do not ask which file or where to put the output. The episode number comes from
the WWD calendar, so check there rather than asking.

**Status:** EP106 has no transcript yet. Every blocker is cleared (script bugs
fixed, Hugging Face licenses accepted, CUDA verified on the RTX 5060) — the
original session went bad before it could run. It needs one clean launch.

**Voiceprints are not enrolled.** `voiceprints/` is empty, so speakers come back
as Guest/Unknown and need mapping by hand. Enrolling Matt, Zac, and Gabby
requires a clean solo audio clip of each.
## Venture status — set 15 AUG 26, review 15 NOV 26
 
MAIN EFFORT: Kingdom Planners
ACTIVE: WWD/FrostCast, Shattered Empire, Cyber Security,
        WarriorKingDesigns (triage complete, hold)
ACTIVE-UNSCHEDULED: Watershed, Post-Production, RUBY TWO
  - Keep files current. Capture ideas. No agent, no schedule.
  - Do not surface these in daily or weekly planning.
  - Do not let Zac feel behind on them. They are parked on purpose.
DORMANT: Investing, SciFi Novel, Shadows
  - Capture only. Do not surface at all unless Zac asks directly.
 
No agent may promote a venture between categories. That is a
Zac decision. Queue it in DECISIONS.md if the case is strong.

## Escalation rule — applies to every agent
You cannot ask Zac a question directly. The tool does not exist
inside a subagent. When you hit a decision you are not authorised
to make: do NOT guess. Append to D:\WKP\logs\DECISIONS.md, then
return DECISION QUEUED plus the ID. Keep working on anything not
blocked by it.
 
## Honesty rule — applies to every agent
Never report a number, status, or result you did not actually
retrieve. If a source is unreachable, a key is missing, or a tool
failed, say "not available" and name what is missing.
 
## Scratch and output routing
- Scratch: D:\WKP\scratch\ (gitignored). Never system Temp.
- Reusable scripts: the owning skill's scripts\ folder.
- Deliverables: L:\ per LOCAL-PATHS.md, with a log line in logs\.
- Paths and interpreters: read LOCAL-PATHS.md. Never hardcode.
 
## Etsy listing cap — LOCKED 15 AUG 26, expires 15 NOV 26
Maximum 3 new listings per day, maximum 8 per week, across both
shops combined. Anti-suspension rule, not a preference.
 
## Venture status — set 15 AUG 26, review 15 NOV 26
MAIN EFFORT: Kingdom Planners
ACTIVE: WWD/FrostCast, Shattered Empire, Cyber Security,
        WarriorKingDesigns (triage complete, hold)
ACTIVE-UNSCHEDULED: Watershed, Post-Production, RUBY TWO
  - No agent, no schedule. Do not surface in daily planning.
DORMANT: Investing, SciFi Novel, Shadows, Survival-SciFi, KDP,
         Website
  - Capture only. Do not surface unless Zac asks directly.
 
## Closed loop — applies to every director
Before planning any week's work, check D:\WKP\data\ for a recent
file for your venture. If none exists in the last 10 days, say the
plan is unguided rather than inventing a number.

## Etsy data — manual, not exported
Etsy provides NO traffic CSV export. Views, favorites, and visits
live only in D:\WKP\data\etsy-manual-YYYY-MM-DD.md, typed by hand
each Friday. Do not look for an Etsy traffic CSV. Do not report a
view or favorite count that is not in that file.