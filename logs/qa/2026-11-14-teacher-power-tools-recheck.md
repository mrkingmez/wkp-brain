# QA recheck: Teacher power-tools drafts (2026-11-14)
qa-director. Report only, nothing edited. Files in D:\WKP\Teacher\drafts\power-tools\. Source: fact pack 2026-11-14-claude-power-tools-fact-pack.md. First QA: 2026-11-14-teacher-power-tools.md.

## Verdicts
| File | Verdict |
|---|---|
| stay-safe-tools-that-act.md (L1) | PASS WITH NOTES |
| projects-and-memory.md (L2) | PASS WITH NOTES |
| skills-reusable-instructions.md (L3) | PASS WITH NOTES (3.1 to be tested on a Mac before she sees it) |
| connectors-and-mcp.md (L4, new) | PASS WITH NOTES (4.1 should be fixed before ship) |
| quizzes-draft.js | PASS |

## What I ran
- slop_check.py on all 4 lessons: clean, exit 0 (mechanical only). Em and en dash grep on the folder: zero.
- Word counts excluding code fences, headings included: L1 1595, L2 1536, L3 1555, L4 1504. All within about 6 percent of 1,600.
- node --check quizzes-draft.js: ok. Scratch script D:\WKP\scratch\qlen.js printed answer index and choice lengths per question.
- Not run (NOT AVAILABLE): site render, real Mac click-through, no-ai-slop judgment pass, writing-room second pass.

## Earlier findings, re-verified in the files
L1: 1.1 fixed (lines 69, 96, connectors off first). 1.2 fixed (111). 1.3 fixed (41). 1.4 fixed (41). 1.5 fixed (49). 1.6 fixed (51). 1.7 fixed (19). 1.8 consistent in all four. 1.9 fixed (63 defines the prompt page). 1.10 fixed.
L2: 2.1 fixed (file has no sign-off name, Task 3 adds name plus tone rule, lines 151 to 164). 2.2 fixed (95, TextEdit, Make Plain Text, Finder, Command keys, text-paste option first). 2.3 fixed (no label lines). 2.4 fixed (56, 58). 2.5 hedged. 2.6 fixed (81). 2.9 fixed.
L3: 3.1 fixed in design (Claude makes the zip, 126 and 129), residual risk below. 3.2 fixed (75, Pro stated, free fallback gone, no leftover, no quiz question on it). 3.3 fixed (closing line). 3.4 fixed (129, 137). 3.5 fixed (61). 3.6 fixed. 3.7 fixed (113). 3.8 fixed. 3.9 fixed (79, matches pack). 3.10 fixed (83). 3.11 fixed.
Quiz: Q.1 fixed, the correct answer is the longest choice on none of 12 questions. Q.2 fixed. Q.3 fixed. Q.4 fixed, positions 1,2,0 / 0,2,1 / 1,0,2 / 2,0,1, four of each index. Q.5 fixed.

## Fact trace
All plan, menu and limit claims trace to the pack: Projects on Pro, RAG up to 10x (L2 35); project steps (41 to 46); memory default and reset (L2 60); Skills definition, built-ins, upload failures, zip root, delete, no sync, trusted sources, name rules (L3); Mac-only recording (L3 79); MCP/USB-C, inherited permissions, Allow always, Research approvals, Search and tools menu, custom connectors unverified, disconnect path (L1, L4). No price, message count or usage limit anywhere. Outside-pack items (TextEdit, Pages, Finder, Command keys) are general OS knowledge and the menus carry "check your own screen".

## Numbered findings
### L1 stay-safe-tools-that-act.md
1.1 Line 111 "The warning line often helps" is not in the pack. Hedged, acceptable. Fix: "may help".
1.2 Lines 43 to 44 stray double blank line. Fix: delete one.
No line says Zac or an agent connects anything. Pass.

### L2 projects-and-memory.md
2.1 Line 33 heading "What Pro adds" implies Pro adds Projects, but the pack says Projects are on all plans (Free capped at five). Fix: retitle "Projects and your Pro plan".
2.2 Line 95 is one dense paragraph of Mac steps. Fix: split into short numbered steps.

### L3 skills-reusable-instructions.md
3.1 Lines 129 and 147. The pack does not confirm Claude can hand over a zip through file creation, and on a Mac Safari may auto-unpack a downloaded zip into a folder. The lesson never says where the download lands or how to find it in Finder. General knowledge, untested here. Fix: add "the zip lands in Downloads, find it in Finder; if you see only a folder, right-click it and choose Compress", and have Zac or a tester run Tasks 2 and 3 once on a Mac. Stop rule at 126 is a safe fallback.
3.2 Task 3 self-check (157 to 162) does not check zip structure. Fix: add "my zip opened to one folder with SKILL.md inside".

### L4 connectors-and-mcp.md (new)
Safety checklist, all pass: Task 2 optional (3, 64, 89, 93); read-only first (50, 98, 103); approve each, no Allow always (44, 99, 112); no send, delete or share (64, 103, 106, 113); no banking or health (56, 64, 93); nothing connected for anyone else (64, 93, 111); custom flagged unverified, trusted source, ask Zac (40); disconnect works and is found first and confirmed after (60, 95, 100, 114), matching pack section 5. The only Zac mentions are "ask Zac first" gates (9, 40); nothing says Zac or an agent connects for her.
4.1 (fix before ship) Lines 93 and 103. Example is "your own calendar", yet line 56 says Claude sees everything you can in that app, and a real calendar usually holds other people's invites and possibly health items, so the "holds nothing sensitive" self-check (111) fails for most people. Also nothing tells her to create the made-up events "Practice lunch" and "Garden club test" first. Fix: add a step 0 to create the two made-up entries, and add "if the account has anything sensitive on it, skip Task 2 and stop after Task 1".
4.2 Line 110 "I connected only one connector" is ambiguous if she already has some. Fix: "I switched on only one connector in the chat".
4.3 Line 132 "the safe-tools check from the earlier lesson" is unnamed, and line 18 "Until now Claude only knew what you typed" ignores uploaded files. Fix: name "When AI can act, not just talk" and say "apart from files you uploaded".
4.4 Lines 70 and 124 "your prompt page" is defined only in L1 line 63. Fix: one clause defining it.
4.5 Real-account teaching rests on Zac's hedged "I believe" (Teacher CLAUDE.md, 2026-11-14). Safe here because Task 2 is optional and she decides. Confirm with her before release.

### quizzes-draft.js
Pass. Valid JS, 12 questions, 4 keys, pass 2. Each question is answerable from its lesson (L3 Q3 from lines 33 and 164, L4 Q2 from line 40). No question on the removed free-account fallback.
Q.1 Keys mix "stay-safe/" and "power-tools/" prefixes. Header says software-director sets final keys. Confirm they match the nav before merge or progress will not save.

## Decisions
None new. TEACHER-2026-11-14-QA-01 is largely answered by Zac's 2026-11-14 answers. Whether she agrees to connect real accounts is still unasked.

## Overall standard
Every earlier blocker is verified fixed in the files, not on the fixers' word. Honest, Mac-ready, safety-first. Still owed: writing-room second pass, no-ai-slop judgment pass, one human Mac run of the Skills zip steps. Ship to Jarvis after 4.1 is fixed.
