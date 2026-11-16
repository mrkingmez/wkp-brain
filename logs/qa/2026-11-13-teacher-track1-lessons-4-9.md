# QA report: Teacher Track 1, lessons 4 to 9 and quizzes-draft-b.js
Date: 2026-11-13. Checked by qa-director (read and run only, nothing edited).
Files: D:\WKP\Teacher\drafts\track-1\lesson-4.md to lesson-9.md, quizzes-draft-b.js. References: lesson-1 to 3, D:\WKP\Teacher\PRACTICE-PATTERN.md.

## VERDICT: PASS WITH NOTES
Nothing here needs a rewrite. One mechanical item should be cleared before merge (the slop script exits 1 on lessons 4 and 9). Everything else is a note.

## 1. Mechanical slop pass (run, not assumed)
Command: Python312 slop_check.py <file>
| File | Result |
|---|---|
| lesson-4.md | EXIT 1. Line 19 [HEDGE] "might" ("a note you might need written") |
| lesson-5.md | clean |
| lesson-6.md | clean |
| lesson-7.md | clean |
| lesson-8.md | clean |
| lesson-9.md | EXIT 1. Line 142 [HEDGE] "might" x3 ("The review might catch... It might raise... Or it might say all is fine") |
| quizzes-draft-b.js | clean |
Em dash (U+2014) count: 0 in all six lessons and the quiz. En dash count: 0.
All four hits are honest possibilities, not filler. Fix is a one-word swap each ("can", "may", or restructure), then rerun. The script is the mechanical pass only. The judgment pass (generic, sounds like her teacher) was not run by me.
Syntax: `node --check quizzes-draft-b.js` passed.

## 2. Accuracy
- Lesson-6 Task 1 arithmetic (line 91) is CORRECT. 8 x 0.5 lb = 4 lb. 4 x $3.50 = $14. Rice $2. Vegetables $12. Total $28. $60 - $28 = $32 left. The lesson text matches. It also tells her the calculator is the authority.
- Free-tier limits, file-upload limits, memory features, prices, models: none are stated as fact. Lesson-7 lines 32 to 36 and 50 hand attachment, size, memory and plan questions to the vendors' pages with "check this yourself" and "write the date". Good.
- No laws or statistics anywhere.
- Notes (stated as fact or unverified):
  - lesson-9.md line 35: "on the free versions it costs you nothing but a few minutes." Free tiers have usage caps that are not verified here. Lessons 7, 8 and 9 ask for many chats across two tools in one sitting. Add one line telling her that if a tool says she hit a limit, she should stop and come back later. This is the most useful practical addition.
  - lesson-8.md line 45: "It is free with your account" (Google Docs) is stated as fact, not retrieved. Low risk.
  - lesson-7.md line 44: "Long chats can drift... early details may get less attention." Reasonable and hedged ("may"). Fine, no source needed.
  - lesson-6.md line 56: "inventing something plausible is the thing these tools do." Broad but fair as teaching language.
  - URLs (claude.com/pricing, support.claude.com, chatgpt.com/pricing, claude.ai, chatgpt.com, docs.google.com) were NOT fetched by me. WebFetch is NOT AVAILABLE to qa-director. They match the URLs already used in lesson-2 (Task 1), so they are consistent with the approved house set. Recommend qa-claims or fact-research confirm once for the whole track.
- UI click claims, NOT VERIFIED (no live access to the products):
  - Google Docs "Blank document" tile (lesson-7 line 77). Same wording as lesson-2 line 109. Plausible and matches the current layout as I know it.
  - "Normal text" style box and "Heading 2" (lesson-8 line 72). Hedged with "usually". Plausible.
  - Click the Doc title at the top left to rename (lesson-8 line 72). Plausible.
  - claude.ai "New chat at the top left, or the plus sign if you see one" (lessons 4, 7, 8). Hedged and identical to lesson-3 line 67, so it is house wording. Low risk.
  Recommendation: Zac or his wife spot-checks these four on screen once, since menus move.
- Cross-references: lesson-4 "last lesson... four parts: job, details, reader, shape" matches lesson-3 lines 27 to 56. Lesson-7 line 38 "what you learned in lesson 2: anything you attach or paste is something you are sharing" is supported by lesson-2 line 36 ("treat that as sharing the file"), though lesson 2 says it in one clause, so "learned" is a slight stretch. Note only. Lesson-8 "lessons 3 to 7" points to prompts that do exist (grocery list in 4, thank-you template in 5, handoff note in 7).

## 3. Quiz answers vs lesson text
All 18 questions have exactly one correct answer, the explain text matches the lessons, and `pass: 2` matches "2 of 3" in every lesson.
Correct answer index per quiz (0=A, 1=B, 2=C):
- role-and-context: 2, 0, 1
- show-examples: 1, 2, 0
- show-its-work: 1, 2, 0
- long-tasks: 1, 2, 0
- prompt-library: 1, 2, 0
- chains-and-checking: 1, 2, 0
Findings:
- Positions are spread within each quiz and balanced overall (six each), but five of the six quizzes use the identical 1, 2, 0 sequence. A quick learner will spot it. Shuffle some (quizzes-draft-b.js lines 33/36/42, 56/62/68, 77/83/89, 99/105/111, 123/129/135 and the others).
- Longest-answer tell: in about 14 of 18 questions the correct choice is the longest or most detailed one (e.g. lines 38, 44, 61, 78, 84, 90, 124, 130, 136). A learner can pass by picking the longest. Fix by lengthening some wrong answers or shortening the right ones.
- Keys are working keys (`start-here/...`) and the file header says software-director sets the final ones. Not a defect, but the merge step must match them to the nav and to course.js.

## 4. Practice pattern
All six lessons pass. Each has 3 tasks. Every task has the heading, Why it matters, Do this, a text fence, Self-check with 4 checkbox items (pattern allows 3 to 4), What good looks like, and a `---` between tasks (after tasks 1 and 2, none after task 3). Each ends with the one sentence about the practice button and quiz, then `<div id="practice-done"></div>`, then Further reading, then `<div id="quiz"></div>` as the last line. Lesson-9's closing sentence is correctly adapted to Track 1 finishing. All sample material is made up, and no task asks her to paste private details. Minor: lesson-4 Task 2 and lessons 5, 6, 7, 9 use two or three prompt fences in a task. The pattern says "a" prompt, but this reads fine and matches lesson 1 to 3 style.

## 5. Readability, length, constraints
Word counts (whole file / excluding code fences / teaching part before "## Practice, no fences"):
| Lesson | Whole file | No fences | Teaching only |
|---|---|---|---|
| 4 | 1921 | 1624 | 781 |
| 5 | 1753 | 1495 | 701 |
| 6 | 1714 | 1562 | 735 |
| 7 | 1854 | 1623 | 885 |
| 8 | 1723 | 1609 | 702 |
| 9 | 1893 | 1626 | 792 |
(wc -w gave 1885 for lesson-9; my count of 1893 splits differently. Both are over by the same margin.)
For comparison, lessons 1 to 3 are 1689, 1529 and 1383 whole file. Against the 1,300 to 1,700 target, all six are over on a whole-file count (lesson 6 by 14 words, lessons 4, 7, 9 by 150 to 220). Without the prompt fences all six are inside the range. The target was probably meant to include or exclude fences, so Jarvis should say which. Lessons 4, 7 and 9 run longest and could lose a short paragraph each if whole-file is the rule. Lesson-7 has the longest practice section (885 teaching words before it).
- Plain words: yes throughout. Short sentences, concrete examples. Terms like "chain", "checkpoint", "thread" and "context block" are each explained when first used.
- Nothing needs a paid plan. All tasks use free Claude and free ChatGPT plus a free Google Doc. No Firefly or Veo credits are used or mentioned. Google account is assumed, and lessons 2 and 3 already assume it.
- Time claims: headers say about 40 to 50 minutes of practice. Three tasks at 10 to 20 minutes each match.
- Note, lesson-8 Task 2 (line 97 to 110): the long ten-item suggestion list sits between the instruction and the prompt, so the "Do this" paragraph is hard to follow on paper. Consider moving the list below or giving it its own label. Not blocking.
- Note, lesson-9 Task 1: ChatGPT is used for review in Tasks 2 and 3 only, fine. Step 3 asks her to start a new chat and paste two things, which is clear.

## Gates
Handoff says script-room wrote these (two passes and its log live under Teacher\writing-room-log.md, not checked by me). Not run by me: marketing and no-ai-slop judgment pass (these are course lessons, not public posts). devils-advocate not required.

## Items for the fixer (describe only)
1. lesson-4.md line 19 and lesson-9.md line 142: replace "might" with a non-hedge, rerun slop_check, expect exit 0.
2. lesson-9.md line 35: soften "costs you nothing" and add a "hit a limit, come back later" line to lessons 7 to 9 practice intros.
3. quizzes-draft-b.js: vary the correct-answer positions across quizzes and even out answer lengths.
4. Decide the word-count rule (with or without fences) and trim lessons 4, 7, 9 if whole-file applies.
5. One-time check of the four UI click claims and the URL set by a person or by qa-claims with a browser.

No DECISION QUEUED entries were needed.
