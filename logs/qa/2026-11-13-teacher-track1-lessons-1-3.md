# QA: Teacher Track 1 lessons 1 to 3 (2026-11-13)

Verdict: PASS WITH NOTES. Report only, drafts not edited.

Slop check (slop_check.py): lesson-1 clean, lesson-3 clean, quizzes-draft.js clean, lesson-2 one hit at line 19 "kind of" (HEDGE). It is a false positive ("the same kind of work"), not a hedge. Optional: swap to "the same sort of work". Grep for em dashes across the folder: none.

Links (curl, reachability only): claude.com/pricing 200, support.claude.com 200, chatgpt.com/pricing 200, chatgpt.com 200, claude.ai 403 (bot block on curl, normal for a login site, not a dead link). Page contents were not read, NOT AVAILABLE (no browser or fetch tool). No lesson text claims anything about free-tier limits, models or features, so nothing depends on the content. Makers: Claude = Anthropic, ChatGPT = OpenAI, correct.

Quiz answers: all 9 match lesson text (L1 answers 0,1,2; L2 1,2,0; L3 1,0,2).

Notes (none block):
1. lesson-1.md line 17: "You have used both" is not on record. Teacher\CLAUDE.md says she used free Claude once and has free ChatGPT. Soften to "You have both".
2. lesson-1.md line 48: "The Stay Safe track covers this in full" overpromises, only one Stay Safe lesson exists, rest are placeholders.
3. lesson-2.md Task 3 (line 109): arithmetic is muddled. Five of her own plus five from the AI is ten, then "keep the ten strongest" implies a cut. Say "keep ten in all" or ask for more candidates.
4. Click-level steps: nowhere does a lesson say how to start a new chat (needed in L3 Task 1 and Task 2, "open a new chat") or how to open a Google Doc (L2 Task 3, L3 Task 1). Add the button name or offer "paper is fine". Also lesson-1 Task 3 does not say which AI tool for the pharmacy test (Claude or ChatGPT or both).
5. lesson-2.md line 36 mentions "an upload button" without saying whether the free plan has one. Not a limit claim, but reword to "if a chat ever offers to attach a file".
6. Pattern: all 9 tasks have Why, Do this, text-fenced prompt, 4-item Self-check, What good looks like, and --- between tasks. practice-done div, Further reading and quiz div present in order. L2 Task 1 prompt is a fill-in notes template, not a paste prompt (acceptable).
7. Process: writing-room second pass and marketing gates not evidenced in the handoff beyond "from script-room". Confirm both passes are logged before ship.
