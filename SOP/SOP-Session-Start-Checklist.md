# SOP Session Start Checklist

Created 2026-11-19 (readiness pass). What Jarvis reads and checks at the start of every session, in order, before taking Zac's first task. Target: under 5 minutes. Say nothing back to Zac unless something is RED or a staged job needs him.

## 1. Read (in this order)

| Step | File | Check |
|---|---|---|
| 1 | Root `CLAUDE.md` (loads automatically with ME.md, projects.md, TASKS.md, LOCAL-PATHS.md) | Nothing to do, it is already in context |
| 2 | `memory\MEMORY.md` | Follow only the pointers that touch today's work. Do not recite it |
| 3 | `SOP\SOP-00-Master-Workflow.md` | The chain, logging, what goes to Zac |
| 4 | `TASKS.md`, "Today and this week" table | Header date. Any row with a date that has passed is stale: refresh it from disk and logs, or mark "status not verified, owner: X" |
| 5 | Newest `reports\*-Decisions-Triage.md` and the bottom of `logs\DECISIONS.md` | Only items on the "Needs Zac" list go to Zac. Anything appended since the triage gets triaged with the same rule |
| 6 | `logs\system-check\latest.txt` | GREEN, YELLOW or RED, and the date. Older than 2 days: run the check (step 9) |

## 2. Check (commands)

| Step | Command (Git Bash) | Pass |
|---|---|---|
| 7 | `git -C /d/WKP status --short \| wc -l` and `git -C /d/WKP log origin/main..main --oneline \| wc -l` | Know the uncommitted and unpushed counts. Unpushed commits go on Zac's list as "push" |
| 8 | Agent count: `ls /d/WKP/.claude/agents/*.md \| wc -l` against the agent list in this session | Equal. A spec on disk that is missing from the list loads next session, so run it through a general-purpose agent until then |
| 9 | `python D:\WKP\.claude\skills\wkp-system-check\scripts\system_check.py --no-updates` | Writes `logs\system-check\YYYY-MM-DD.md`. Fix RED items that need no money or permission. List the rest |
| 10 | `python D:\WKP\.claude\skills\wkp-system-check\scripts\spec_paths_check.py` | Exit 0. A new miss gets fixed (real path) or a stub with a header, never invented canon |
| 11 | `python D:\WKP\.claude\skills\wkp-system-check\scripts\spec_frontmatter_check.py` | Exit 0 (INFO lines for "inherits all tools" are fine) |

## 3. Staged jobs (run these first, no questions)

| Job | Owner | How |
|---|---|---|
| FrostCast EP 121 transcript to Matt (WWD-2026-11-18-01) | Jarvis (needs the Chrome tool) | Root CLAUDE.md FrostCast workflow step 6. File: `L:\Winter Wolfs Den review show\Frost-Cast\EP 121\The name_s Edwa-- er Bond _ Snyderverse 2_0 _ FrostCast Episode _121_transcript.txt`. Screenshot "Sent" with the filename before calling it done. No Chrome tool: say so to Zac in one line |
| Saturday and Monday task result 1 (INFRA-2026-11-16-01) | software-director | Read the task setup and the two skills, report the cause before Sat 11/21 05:30 |
| Nightly rollup stored prompt (INFRA-2026-11-18-01) | chief-of-staff | Find the cloud routine with the schedule skill, change it to read venture status fresh from root CLAUDE.md |
| QA on Transcription and Teacher pages (INFRA-2026-11-13-01) | qa-director | Normal QA pass, no spend |

Remove a row here the same session it is done, and update TASKS.md.

## 4. Every Wednesday after FrostCast (standing, no questions)

Root CLAUDE.md "FrostCast Transcription Workflow" steps 1 to 7. The episode number comes from the WWD calendar. Pass `--num-speakers` (3 for a full FrostCast). Pick between duplicate files yourself and say which in one line.

## 5. Before the session ends

Log rows in `logs\agent-runs.md` and `logs\jarvis-delegation.md`. Commit locally. Remind Zac to push (memory lives in git).


## 5. Project board (added 2026-11-21, Zac)
Step 0 of every session, before the staged jobs: open `REFERENCE\PROJECT-BOARD.md`. Check its "last updated" date. Older than 7 days, or the FrostCast latest episode does not match the newest `L:\...\Frost-Cast/EP <n>` folder: refresh it (chief-of-staff) before any other job. Then check that `REFERENCE\VIDEO-LIBRARY.md` has a row for every FrostCast episode folder on disk (media-manager). Wednesday after the chain: add the episode to the library and bump the board.
