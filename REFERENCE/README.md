# REFERENCE: the project board and reference library

Created 2026-11-21 (Zac's order: agents kept guessing the FrostCast episode number and spellings, so every director needs one place to look). All local, no spend, no posting.

## How to use it (10 lines)
1. Before any job, read `PROJECT-BOARD.md` (state of the enterprise, one screen). Check its "last updated" line. Older than 7 days means STALE: say so in your report and verify from disk or TASKS.md.
2. Read `NAMES-AND-SPELLING.md` before you write any name, title or label.
3. Check `LOCKS.md` for any format, cadence or limit rule before you build. A locked rule beats your spec.
4. Need a past video, its ID, or its package path? `VIDEO-LIBRARY.md` (summary) and `VIDEO-LIBRARY.csv` (everything).
5. Unsure what a term means (run sheet, USE, sting, stop)? `GLOSSARY.md`.
6. Workers: ask your director first. Directors: ask the board, then ask chief-of-staff, then Jarvis. Zac is last, and only for money, public posting, or a taste call only he has.
7. A fact you could not find is written NOT VERIFIED or NOT KNOWN. Never guess an ID, episode number, date or spelling.
8. Found something wrong or old? Fix it in the file you own, or tell the owner (table below) the same turn.
9. These files are reference, not decisions. Decisions live in CLAUDE.md files and `logs\DECISIONS.md`.
10. Everything here is internal and may be committed. Keep private money data out.

## Ownership and update rule (locked 2026-11-21, Zac's order)
| File | Owner | Update when |
|---|---|---|
| PROJECT-BOARD.md | chief-of-staff | Weekly, and whenever a director starts or finishes a job. Directors may edit their own venture row and must put the date and their agent name in the "last updated" line. Stale after 7 days. |
| LOCKS.md | chief-of-staff | Same turn Zac locks or changes a rule. Add date, who, source file. |
| VIDEO-LIBRARY.md and .csv | media-manager | A row when a video goes live or is finalized, and every Wednesday after the FrostCast chain (new episode row, ID if Zac pasted the link). |
| NAMES-AND-SPELLING.md | chief-of-staff | Whenever a new name, title or recurring misspelling appears. |
| GLOSSARY.md | chief-of-staff | When a term is defined in an SOP or spec, or Zac defines one. |

Every director updates the board when they start or finish a job (one line in their venture row). Wednesday FrostCast chain adds a step: add the episode to `VIDEO-LIBRARY` and bump `PROJECT-BOARD` (root CLAUDE.md step 8, `SOP\SOP-00-Master-Workflow.md`).

## Who may not
No agent changes a lock on its own. A lock changes only with Zac's words in the repo. Chief-of-staff records, never decides.
11. Prompting standard: before ordering or writing any generated image, video, audio or 3D asset, read `PROMPTING-PLAYBOOK.md` (venture-neutral method, owner graphic-design). It is a standing standard, not a format lock.
