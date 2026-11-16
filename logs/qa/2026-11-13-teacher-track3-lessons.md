# QA report: Teacher Track 3 draft lessons 3.1, 3.2, 3.3, 3.5 + quizzes-draft.js
Date: 2026-11-13. Checked by qa-director (solo read, no bench spawned). Files unedited.
Files: D:\WKP\Teacher\drafts\track-3\lesson-1.md, lesson-2.md, lesson-3.md, lesson-5.md, quizzes-draft.js

## VERDICT: FAIL (3 small blockers, all quick fixes; everything else passes)

## Check results
1. Mechanical slop script (run, python 3.12): lesson-1 clean, lesson-2 clean, lesson-3 clean, lesson-5 EXIT 1 (1 hit).
2. Em dashes: 0 in all four .md and the .js (grep). En dashes: 0.
3. House style: see B3. Headings, Why it matters, Do this, Self-check (4 items each), What good looks like, --- between tasks, practice-done div before Further reading, quiz div as last line: all correct in all four lessons.
4. Word count (wc raw, includes code and tables / prose only): L1 1879 / 1592, L2 1731 / 1488, L3 1781 / 1580, L5 2019 / 1746. Prose-only is in range for L1 to L3. L5 is about 50 words over the top at prose-only, about 300 over raw. Note only.
5. Hand-worked numbers: all verified by my own arithmetic. L1: 319.35, 158, 120.85, 40.5, Left 42 / 29.15 / 9.5, all OK; Snacks 12 puts Fun at 52.5, Over. L2: Yes rows 28+18+15+32 = 93, No rows 45+12 = 57, 2 gifts. L3: Tacos 2, Pasta 1, Stir fry 0, Friday 2 (Pat, Lee). Cell addresses consistent (summary F1:J4, total F7/G7, no collision; form sheet Timestamp in A so Name B, Night C, Dish D, matches formula and Claude prompt). HTML samples in L5 are valid and the link uses example.com. Not run in a live Sheet or browser (no access): numbers and syntax checked by reading.
6. Quizzes: format matches the live quizzes.js (pass, questions, text, choices, answer, explain). Every answer index matches the lesson text. Answers by lesson: L1 1,0,2; L2 1,2,0; L3 1,2,0; L5 0,1,2. Across all 12: four each of 0, 1, 2. Well spread. One content issue, see N1.
7. Unverified claims: no free-tier numbers, prices or platform rules stated. Claude limit sentence is hedged and sent to Anthropic's page. Menu paths hedged "menus change" in all four. Links: support.google.com/docs 200, developer.mozilla.org 200, claude.ai returned 403 to curl (bot block, likely fine in a browser, not confirmed). Further reading sections say the pages were not read, which is honest.
8. Placeholders: no TODO/TBD/lorem. The bracketed items ([paste it], [your topic], [paste the exact error text], [what you expected]) are intentional fill-ins inside prompts.
9. OS branches: see B2.

## BLOCKERS
B1. lesson-5.md line 93, "keep private details off any page you might share later." Slop script [HEDGE] "might", exit 1. Fix: say the thing, for example "any page you plan to share". Rerun the script until exit 0.

B2. lesson-5.md line 74 (check 9, assumes an OS layout). "If you see a Start button at the bottom left of the screen" is wrong for Windows 11 default, where the taskbar and Start button are centered. Zac's own machine is Windows 11. Also the lesson assumes only Windows or Mac, so a Chromebook or other user is told to stop and ask someone, which is acceptable, but the identification text should key on the Windows logo button on the taskbar, not a corner. Related gap: line 114 gives the "show file name extensions" fix for Windows only. A Mac branch is missing for the same hidden-extension problem (Finder settings, Advanced, show all filename extensions, hedged "menus change"). Line 105, "right-click" on a Mac: add "or Control-click". Fix described, not done.

B3. House style (check 3, PRACTICE-PATTERN.md item 4, a text-fence prompt in every task). Missing in: lesson-3.md Task 1 (lines 63 to 85, build the form, only a table), lesson-3.md Task 3 (lines 136 to 151), lesson-5.md Task 1 (lines 95 to 114, steps only). Fix: add a copy-paste item in each (for example a text-fence planning template for the form tasks, or a text-fence file name and starter reminder for L5 Task 1), or have script-room/Zac record an exception in PRACTICE-PATTERN.md for tasks where the work happens outside Claude. Do not leave it silent.

## NOTES (should fix, do not block alone)
N1. lesson-3.md line 40 and quizzes-draft.js Q2 explain for forms-to-sheets: "Tacos, tacos, and taco night ... your count will split three ways." COUNTIF in Google Sheets is case-insensitive as far as I know (from known behavior, NOT tested here), so Tacos and tacos would be counted together and the split would be two ways. Recommend an example that really splits (Tacos, Taco night, Tacos please) and a quick live test before merge.
N2. lesson-1.md Task 3 step 2: "Add a tenth row but spell the category Grocery" gives no date, item or amount. Without an amount the learner cannot see the point. Add a sample row (for example Nov 15, Bread, Grocery, 4.50).
N3. lesson-2.md line 19 "as you saw in Track 1": Track 1 lessons are still "Coming soon" per Teacher\CLAUDE.md. Make sure the reference points at a real lesson at merge, or soften it.
N4. lesson-2 and lesson-5 say "claude.ai" only. Teacher\CLAUDE.md says she also has free ChatGPT and lessons must work on both. Prompts would work in either; consider one sentence saying so (no feature or limit claims).
N5. lesson-3.md Task 2 says to fill the form in via preview or share option. That submissions from preview are recorded is not verified here. Hedge it ("your form's preview or the link to yourself").
N6. lesson-1.md line 36 suggests she may create a Google account. Teacher rule says no signups without Zac's yes, which governs agents, not her choice, but Zac should know the course asks it. It is worded as her choice and cautions her to read what Google asks.
N7. lesson-2.md line 30 "Curly quotes make Sheets give an error" is stated as fact, not verified here. Widely seen behavior; consider "can".
N8. Lesson 4 of Track 3 is not in this batch, so the "next lesson" wording after lesson-3 is untested for flow. Out of scope.

## What passes cleanly
Zero em dashes, no placeholders, no invented stats, correct arithmetic, valid HTML, quiz answers match text and are evenly spread, structure per pattern apart from B3, practice-done and quiz div order correct, Further reading honest about unread pages.

## Not done / not available
No live run in Google Sheets, Google Forms or a browser (no access). Judgment pass for generic tone not run by me beyond reading: tone reads plain and specific, no AI-tell phrasing noticed. The no-ai-slop skill judgment pass belongs to the main session or marketing-director. No bench spawned.
