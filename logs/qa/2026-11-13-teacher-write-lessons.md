# QA report: Teacher "Write with AI" lessons W1 to W5 plus quiz draft
Date 2026-11-13. Checker: qa-director. Reports only, nothing edited.
Files: D:\WKP\Teacher\drafts\track-2\write-1.md to write-5.md, quizzes-draft-write.js
Guideline: Teacher\guidelines\write-with-ai-guideline.md. Pattern: Teacher\PRACTICE-PATTERN.md. Facts: research\teacher\2026-11-13-fact-pack.md.

## VERDICT: PASS WITH NOTES (no blockers; one gate item needs a decision, see N1)

## 1. Word counts (wc -w, run with Bash)
| File | Whole file | Excluding the two div lines | Excluding div lines, "---" lines and code-fence markers |
|---|---|---|---|
| write-1 | 1493 | 1489 | 1481 |
| write-2 | 1390 | 1386 | 1378 |
| write-3 | 1335 | 1331 | 1321 |
| write-4 | 1307 | 1303 | 1295 |
| write-5 | 1437 | 1433 | 1425 |
All inside 1,300 to 1,700 by the stated measure. write-4 is the thin one: with fence and rule lines stripped it is 1,295, 5 under the floor. Immaterial, not a blocker.

## 2. slop_check.py (Python 3.12, run on each file)
| File | Exit | Hits |
|---|---|---|
| write-1.md | 1 | line 29: "might" (HEDGE) |
| write-2.md | 1 | line 38, three hits: "might" x3 (HEDGE) |
| write-3.md | 0 | clean |
| write-4.md | 1 | line 25: "might" (HEDGE) |
| write-5.md | 0 | clean |
| quizzes-draft-write.js | 0 | clean |
Context: all five hits are the plain modal in a description ("questions a reader might ask", "one might run in time order, one might open with the ending", "where a reader might want a little more"). None is a real hedge. The root rule still says exit 1 means fix and rerun.

## 3. Em dashes
grep for the em dash character across all five lessons and the quiz js: 0 hits. En dashes: 0.

## 4. Checklist
- Practice pattern: each lesson has 3 tasks, each with Task heading, Why it matters, Do this, ```text prompt, Self-check (4 items each), What good looks like. Order correct. "---" between tasks (2 per lesson, none after the last). Practice-done div present, then Further reading, then quiz div last line. PASS. Small deviations, none a problem: W3 Task 1 has two prompt fences (vague and clear, needed for the comparison); the practice-done sentence is three sentences not one; W5 says only "It saves that you finished" (correct, last lesson).
- Free-tier limits, prices, settings, context sizes, laws: none stated as fact. W3 "Settings" says plainly it was not checked and sends her to the vendor pages. W5 points her to look up chat capacity rather than stating it. PASS.
- Mentor-text rule: W3 "Mentor texts, from your own hand" says only her own writing, not an author's, not something found online. Repeated in Task 2 self-check ("entirely my own writing") and quiz Q2. PASS.
- Private details: every lesson tells her to keep private details out and use nicknames or initials. W5 Task 1 uses a made-up cookbook. No lesson asks for private details. PASS.
- Cross-references verified against disk: "What AI is, in plain words" (track-1 lesson-1), "Your first good prompt" (lesson-3), "Give it a role and context" (lesson-4), "Show it examples" (lesson-5), "Long tasks: files, chats and memory" and the handoff note (lesson-7), "How to check what AI tells you" (stay-safe live lesson). All titles match. The claim in W1 and W5 that lesson 1 showed the AI "writes what sounds right" matches track-1 lesson-1 line 31. PASS.

## 5. Quiz (quizzes-draft-write.js)
- node exists (C:\Program Files\nodejs\node). node --check: exit 0, valid syntax.
- 5 keys, 3 questions each, pass: 2 each. PASS.
- Answer positions (0-indexed): W1 1,2,0; W2 2,0,1; W3 0,2,1; W4 1,0,2; W5 2,1,0. Five each of positions 0, 1 and 2. Well spread, no repeated pattern.
- Longest correct option (by character count): 3 of 15 (W1 Q3, W4 Q2, W5 Q2). Most correct answers are the shortest or middle option. Good, no length tell.
- Answers match the lesson text: yes on all 15 (ideas/true details, voice card, ten angles, three outlines, "ask the weakest part", goal/audience/rules, own writing only, borrow an idea, "Do not rewrite", added-fact flag, read aloud, hallucination, cut or label as memory, project card).
- Keys are "make-things/write-..." and flagged in the file as working keys. Wiring to course.js and mkdocs nav is software-director's, not checked here.

## 6. Your question: confirmed / could not find / wrong (W5) vs matched / did not match / could not find (Stay Safe)
Verified in the live lesson: it uses matched, did not match, could not find. W5 uses confirmed, could not find, wrong, and also tells her the Stay Safe lesson "has the full method." Does it matter? Small, but yes. Same job, two vocabularies, one lesson telling her to go read the other. A beginner may wonder if "wrong" and "did not match" are different marks. They are not: "did not match" is the more careful wording (the page disagrees, which is not always proof the AI is wrong). Recommend W5 adopt matched / did not match / could not find, or one line saying they mean the same. Not a blocker.

## Notes
N1 (gate, needs a call). slop_check exits 1 on W1, W2, W4 for "might". They are false positives of the HEDGE rule, but the standing rule is to fix and rerun. Fix is easy: reword the four spots (for example "can" or "may", or restate the clause) and rerun until exit 0. If Jarvis would rather log them as a waiver, say so in writing-room-log.md. I did not treat this as a FAIL because the lessons are family-use copy, not public, and every hit is benign.
N2. W1 line 55 says "The Stay Safe track explains why" about private details. The live Stay Safe track has one lesson (check-what-ai-tells-you) and the others are placeholders; the home page says privacy is in that track but no privacy lesson exists yet. Reword to "will explain" or wait for the lesson. Claim not backed by a real file today.
N3. W5 quiz Q3, distractor "Nothing at all, because it keeps everything from your earlier chats." The fact pack (line 17) says free Claude includes memory across conversations, so the distractor is not flatly false for every tool, and track-1 lesson-7 says new chats start empty "by default". The right answer still holds (a card is better), but the distractor teaches a claim about memory that the research does not support as clean fact. Suggest rewording the distractor to something unambiguous (for example "Nothing, and hope it guesses the project"). Low risk.
N4. Interface directions ("New chat at the top left of the page, or the plus sign if you see one"; "click the title at the top left" in Google Docs) are not in the fact pack. They are hedged and match the style used in track-1 lesson-8, so acceptable, but they are unverified screens that can change. Zac or her will find out on first use.
N5. W4 line 33: "The last lesson in this course covers checking your piece" is ambiguous (this track, W5). Say "the last lesson in this track."
N6. Quiz explanation W5 Q2 "The AI often agrees with itself" is a general claim with no source. The lesson says only that asking it again checks nothing. Consider cutting "often."
N7. W4 has a line that tells her to test one task in ChatGPT too; fine, but the prompts and steps are Claude-specific while the brief says both free tools. All five lessons work in either tool in practice. Not a violation.

## Not checked
- No live render of the lessons on the site (not wired yet). No click-through of Claude or Docs screens. Script-room two-pass logs for these five lessons were not part of this task, so I did not verify the two passes happened. Check writing-room-log.md before they go live.
