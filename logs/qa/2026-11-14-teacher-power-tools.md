# QA report: Teacher power-tools lesson drafts (2026-11-14)

Checked by qa-director. Report only, nothing edited. Budget: about 30 min, under 90k tokens, $0.
Files: D:\WKP\Teacher\drafts\power-tools\ (stay-safe-tools-that-act.md = L1, projects-and-memory.md = L2, skills-reusable-instructions.md = L3, quizzes-draft.js = Q).
Source of truth: D:\WKP\research\teacher\2026-11-14-claude-power-tools-fact-pack.md ("the pack"). Compared with 2026-11-14-video-picks.md.

## Verdicts
| File | Verdict |
|---|---|
| L1 stay-safe-tools-that-act.md | PASS WITH NOTES (note 1.1 should be fixed before she sees it) |
| L2 projects-and-memory.md | FAIL (Task 3 premise is broken) |
| L3 skills-reusable-instructions.md | FAIL (Tasks 2 and 3 cannot be done by a first-timer as written) |
| quizzes-draft.js | FAIL (answer-length tell on 6 of 9 questions) |

## What I ran
- slop_check.py on all four files: clean, exit 0 (mechanical pass only). Em dash and en dash grep: zero in all four.
- `wc -w` (counts headings, code blocks and URLs, so it runs higher than a prose count): L1 1799, L2 1809, L3 1939, Q 643 (quiz is not a lesson). All three lessons are over the 1,600 target (L1 +12%, L2 +13%, L3 +21%). The writer's ledger row said 1634 to 1682 (different counting method), so the over-target finding stands either way.
- `node --check` on quizzes-draft.js: syntax ok. Format (pass, questions, text, choices, answer, explain) matches the live quizzes.js entries. Only the global name differs (draft: TEACHER_QUIZZES_POWERTOOLS_DRAFT, live: TEACHER_QUIZZES), which is stated in the file header.
- Not run: a render in the site, a click-through on Windows or Mac, a judgment-pass no-ai-slop (main session or marketing-director owns that), the writing-room second pass. All NOT AVAILABLE here.

## Pack comparison, plan and free/paid status
No lesson quotes a price, a message count or a usage limit. Good. Only numbers used are "five projects on Free" and "up to ten times" with RAG, both in the pack (sections 1 and 2).

| Claim | Where | Pack says | Result |
|---|---|---|---|
| Projects on every plan, Free capped at 5 | L2 line 35 | Projects help article, yes | Supported. Pack section 1 also has the pricing page listing Projects under what Pro adds, which conflicts with the help article. The lesson follows the help article and says "check your own screen". Acceptable. |
| RAG on paid projects, up to 10x | L2 line 35 | yes | Supported. The video agent's "RAG is paid only" matches. |
| Memory on by default Free and paid, Settings > Your Claude, reset deletes project memories | L2 line 60 | yes | Supported. |
| Skills "available on every plan" vs custom upload paid-plan | L3 line 76 | Conflict 2 in the pack | Supported and honestly attributed, see 3.2 on how it is handled. The video agent's "Skills are free-plan" is the help-page half only. |
| Connectors, Research mode approvals, Allow always, disconnect path | L1 lines 39 to 44 | pack section 4 and 5 | Supported. Research is not marked paid-only, see 1.3. |
| Cowork and Claude Code "exist, not covered" | L1 line 19, L3 line 29 | pack section 6 | Supported, no plan claim made. |
| Skill recording Mac only | L3 line 78 | Mac Cowork, paid | Supported but the "do not look for it" tail is wrong for a Mac user, see 3.9. |

Conflict with the video agent: none that the lessons repeat. Its claim that one custom connector is free is not used in any lesson (L1 says skip custom connectors for a beginner, which is the writer's call and is safe).

## L1 stay-safe-tools-that-act.md, PASS WITH NOTES
Safety read: plain, accurate, not alarmist. The "trick email" is a toy, nothing connects, Task 2 hides a harmless instruction, no step asks her to connect a real account. Disclaimer that the warning line "is never a guarantee" is correct.

1.1 (fix before ship) Lines 70 to 100, Tasks 1 and 2. Her Claude may already have a connector on (CLAUDE.md says Zac gave her a prompt to clean out her email, so a Gmail connector is plausible). If one is on, pasting an email that says "reply that I sent the member list" is no longer a pure talk test. Fix: add a first step to Tasks 1 and 2: open a new chat, click "+" lower left, hover Connectors, switch every connector off for the practice chats (pack section 4 menu path).
1.2 Line 115 "Your own approval is the layer that does not fail" overstates. People click through. Fix: "is the layer you control."
1.3 Line 43 Research mode is not labeled as a paid-plan feature (pack: paid only, pricing page conflicts). Fix: add "Research is a paid-plan feature, so you may not see it yet."
1.4 Line 43 "Turn off any tools that write, send or delete" gives no way to do it. Pack says the "Search and tools" menu can disable individual tools. Fix: name that menu and add "if you cannot find it, do not use Research with a connector."
1.5 Line 52 "If read-only is enough, pick read." Pack says the per-tool Always/Needs approval/Blocked setting is an admin control, so a read-only choice may not exist for her. Fix: "if the connector offers a read-only choice."
1.6 Line 54 Habit 3 "make a throwaway version" can mean a new throwaway account, which is a signup (Teacher rule: no signups without Zac's yes) and unverified against provider terms. Fix: say "a test folder or test calendar with made-up entries in your own account, ask Zac before opening any new account." Related open question for Zac (pack Q5, which accounts she may connect) is queued as DECISION below.
1.7 Lines 19 and 21 "Until now every lesson", "Skills ... come two lessons from now" assume reading order. This lesson sits under Stay Safe, the other two under power-tools, so "two lessons" can be wrong. Fix: name the lessons ("the Skills lesson") and drop "until now".
1.8 Line 142 says the practice button and the quiz "both open the next lesson". Fine here, but L3 line 166 omits it. Make them consistent.
1.9 Lines 68 and 105 etc. "your prompt library Doc" is not defined anywhere in site\docs (grep found no match). Fix: confirm an earlier lesson creates it, or add a one-line "a Google Doc or Word file where you keep prompts."
1.10 Word count 1799, trim about 200 (the second Further reading link and the "Keep this in your pocket" repeat of the habits are the easy cuts).

## L2 projects-and-memory.md, FAIL
Facts and menu path pass. Free-tier safe (works with her current free account, good). Blocker is in the practice.

2.1 BLOCKER Lines 109 and 155 to 168, Task 3. The pretend file already says "one dog named Biscuit" and "the vet is Dr. Lindqvist", yet Task 3 asks her to find what the first note was missing (the dog's name) and then add it. The first note will already have Biscuit. "What good looks like" (line 168) then credits a result that was already there. Fix: take the dog's name out of the file, or change Task 3's gap to something the file does not hold (a sign-off name, a tone rule), and keep "how to act goes in instructions, what to know goes in a file."
2.2 Line 97 "create a short text file on your computer" has no steps. Windows: Notepad, check Save as type is Text Documents so it does not save as .txt.txt or hide the extension. Mac: TextEdit saves rich text (.rtf) by default unless Format > Make Plain Text. Both are general OS knowledge, not from the pack. Fix: add both sets of steps, or use the pack's "+ upload files or text" option and paste the text instead (pack section 2 supports adding text), and change self-check line 116 "one uploaded file" to match.
2.3 Lines 99 to 112 The code blocks start with the labels "INSTRUCTIONS:" and "FILE: pretend-household.txt". If copied whole, those labels land in the project. Fix: say "do not copy the label line" or remove the labels.
2.4 Lines 56 and 58 say nothing from last week is on the desk "unless you put it there, or a project did" and context does not carry unless it is in project knowledge. Memory is on by default (line 60) and the quiz answer itself says "or memory". Lesson text is more absolute than the quiz. Fix: add "or memory" at lines 56 and 58, or move line 60 up before them.
2.5 Line 57 "early details may get less attention as a chat grows" is not in the pack. It is common knowledge, not an Anthropic claim here. Fix: attribute it as "often" (already hedged) or cut it.
2.6 Line 81 "You can delete a file from a project, or the project" is not in the pack (deletion steps not retrieved). Fix: soften to "check your own screen for how to remove a file" or have fact-research confirm from the manage-projects article.
2.7 Line 143 self-check "The chat outside it did not know." Fine if memory has no copy, but the user may have the project's own memory off. Low risk, note only.
2.8 Plan assumption: none that blocks. The "paid plan gives more room" (line 35) rests on the RAG note and is fair. Line 48 new-version note is correct per pack.
2.9 Word count 1809, trim about 200 (Memory paragraph can move to a short box, one Further reading link can go).

## L3 skills-reusable-instructions.md, FAIL
Facts pass (name rules, zip must have the folder as root, failure reasons, delete menu, trusted sources, no sync). Safety teaching passes. The practice does not work for a first-timer.

Direct answer on the manual folder and zip steps: the lesson contains NO manual steps. Task 3 (line 147) says "put your folder in a zip" and points back to the upload section, which only describes the upload, and Task 2 (line 126) hands zipping to Claude's own instructions, which will not know her operating system. So a first-timer has nothing to follow. The idea is safe (local, made-up content, uploads only her own file, no install, scripts absent) but unconfirmed: the pack confirms the upload path and the zip-root rule, not any OS click path. Recommendation: do not cut the upload, but do not ship Task 3 until either (a) Claude creates the zip for her as a download (file creation is already switched on in Task 1, ask Claude to "make the folder and give me a downloadable zip", then check the zip opens with the folder inside) or (b) the lesson gives checked steps for Windows and Mac. Zac or a tester should run (b) once on each OS before it ships. Typical traps for the steps, all general knowledge and unconfirmed here: Windows Notepad saves SKILL.md as SKILL.md.txt unless Save as type is All files, and hidden file extensions; Mac TextEdit needs plain text and may append .txt, and a Mac zip adds a hidden __MACOSX folder (whether Anthropic's upload accepts it is not stated in the pack).

3.1 BLOCKER Lines 126 and 147, Tasks 2 and 3. No zip or folder steps (see above). Fix: add the Claude-makes-the-zip path as the main route, with a short, tested Windows list and Mac list as the backup.
3.2 BLOCKER Line 76 "You are on a paid plan, so it should work for you." Zac has not named her plan and CLAUDE.md says she is on free today. Also the lesson shows two Anthropic pages disagreeing, which a beginner cannot resolve. Fix: write "Uploading a custom Skill may need a paid plan. If you do not see Create skill, skip to the stop-here box" and give Task 3 a free-plan fallback (read and check the SKILL.md only, then finish). Move the page disagreement to the further reading. Per Zac's rule every paid-only feature must be marked paid, so label Task 3 "may need paid plan".
3.3 Line 164 and Task 3 test: she cannot tell whether the Skill ran. A plain Claude reply to line 150 also gives a short friendly note. Fix: add one distinctive rule to the Skill (for example a fixed closing line) in the Task 2 prompt so a result is visibly from the Skill, and have her run line 150 once before upload for comparison.
3.4 Line 126 and line 129 Claude may add scripts or extra files. The lesson says "nothing extra" but the self-check (lines 134 to 137) does not say "only a SKILL.md, no scripts, no links." Fix: add that to the Task 2 prompt and a self-check line, consistent with the lesson's own warning (lines 82 to 89).
3.5 Line 62 menu path starts at "Settings, then Capabilities" and then jumps to "Customize" (pack naming-drift note). It says "Menus change", but a beginner may dead-end. Fix: add "if you cannot find Capabilities, look under Customize."
3.6 Line 105 "your prompt library Doc" (see 1.9).
3.7 Line 118 "a document I could open": she may not own Word. Fix: add "Word, Pages or Google Docs all open it."
3.8 Line 166 omits the "practice button and quiz both open the next lesson" sentence that L1 and L2 have. Make consistent or intentionally last-lesson.
3.9 Line 78 "Recording a Skill ... only in a Mac app on paid plans, so do not look for it." If she uses a Mac this tells her to ignore something she may have. Fix: "Windows: not available. Mac with a paid plan: it exists in Cowork, this course skips it."
3.10 Line 82 "which you met two lessons ago" (see 1.7). Fix: name the lesson.
3.11 Word count 1939, trim about 340. Cuts: the page-disagreement paragraph (line 76), line 78, the "Be careful" bullets can be shortened, second and third Further reading links.

## quizzes-draft.js, FAIL
Content is supported by the lessons, no unsafe or plan-assuming answers. Fairness is the problem.

Q.1 Correct answer is the longest choice on 6 of 9 questions: lines 30 to 34 (Projects Q1), 36 to 40 (Q2, 79 vs 34 and 42 characters), 42 to 46 (Q3), 53 to 57 (Skills Q1, 97 vs 31 and 46), 59 to 63 (Q2, 81 vs 36 and 42), 65 to 69 (Q3, 74 vs 19 and 23). A guesser who always picks the longest choice passes both Projects and Skills quizzes. Fix: rewrite the distractors so they are as long and as plausible as the answer, or shorten the answers, so lengths are mixed.
Q.2 Several distractors are jokes that no one would pick: lines 67 ("Your internet speed", "The color of the folder"), 38 ("Claude deletes chats after a day"). Fix: use real beginner mistakes (for example "the folder name", "the file size" are plausible Skill upload issues from lesson line 71 to 74).
Q.3 Lesson 1 quiz is the opposite: correct answer is the shortest on Q2 (line 16, 25 characters) and Q3 (line 21, a sentence fragment "Calendar only, read-only if enough", while the distractors are full sentences). The fragment is a tell. Fix: write all three choices in the same form.
Q.4 Answer positions: L1 is 0, 1, 2 in order, L2 is 2, 0, 1, L3 is 1, 2, 0. Overall 3 each, but the L1 staircase is predictable. Fix: reorder L1 (for example 1, 0, 2).
Q.5 Line 15 "Click Allow always so it stops asking": reasonable trap and matches the lesson. Line 16 "Stop, read it, and refuse" slightly muddled order. Fix: "Read it, and refuse if you did not ask for it."
Q.6 Keys at lines 4, 27, 50 mix prefixes (stay-safe/ vs power-tools/). Draft file says software-director will set final keys. Make sure the key matches the nav or progress will not save.
Q.7 Line 38 "Free plans cannot remember anything at all": false per pack (memory on by default on Free), correctly marked wrong. Good, no change.

## Decision queued
DECISION QUEUED TEACHER-2026-11-14-QA-01 (logged in D:\WKP\logs\DECISIONS.md): which paid Claude plan she will have, Windows or Mac, and whether the course may teach connecting her real accounts or only made-up ones. L3 Task 3 and L1 habit 3 depend on it. Until Zac answers, the lessons should keep every practice on made-up material and give a free-plan fallback.

## Overall standard
Would Zac be proud to hand this to his wife? The writing is clear, honest about uncertainty, and the safety lesson is the right level. L1 is close. L2 and L3 need their practice tasks repaired and a trim, and the quiz needs rebalancing. Send back once to the writing room (script-room), then recheck. The writing room second pass and the no-ai-slop judgment pass are still owed.
