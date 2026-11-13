# Agent run ledger (started 2026-11-12, Zac's yes)

One row per agent job. Fill only what was actually retrieved. Unknown = "not available". Dollars stay "not available" unless a bill or dashboard shows them.

Columns: date | agent | job | budget (time/tokens/cost, set before the run) | actual tokens | tool calls | one thing changed vs baseline | what it did | what it verified (and how) | not verified

| date | agent | job | budget | actual tokens | tool calls | changed vs baseline | did | verified | not verified |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-12 | general-purpose | AI learning resources research | none set | 158,702 | 37 | n/a | report in research\teacher\ | sources cited in report | FTC/FBI primary pages, OpenAI Academy terms |
| 2026-11-12 | software-director | Teacher site skeleton | none set | 82,839 | 12 | n/a | MkDocs site, lesson 1, quiz, server | served over LAN IP, progress POST tested | quiz not run in a browser |
| 2026-11-12 | script-room | Lesson 1 pass 2 + QA handoff | none set | 70,851 | 15 | n/a | 4 lesson fixes | quiz answers match lesson | Academy links, qa-director verdict |
| 2026-11-12 | software-director | Teacher Module 5 repo + practice + unlocking | ~1 h, <150k tokens | 144,493 (task result; under budget, about 9 min wall time) | 63 | n/a | cloned MIT repo to vendor (gitignored), Module 5 page, practice pattern, Lesson 1 practice, unlock flag + endpoints | served over LAN IP, headless Edge dump-dom lock/open states, node logic test, slop_check | real browser clicks (no claude-in-chrome tools available), qa-director verdict pending at write time |
