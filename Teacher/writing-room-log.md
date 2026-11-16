# Teacher writing room log

## 2026-11-12, Module 1 Lesson 1 "How to check what AI tells you"
Mode: GENERATE. File: D:\WKP\Teacher\site\docs\module-1\lesson-1.md

Pass 1 (structure, dialogue, originality; clearance not needed per brief)
- Structure follows the requested order. Quiz div is the last line.
- Teaching copy, no characters, so dialogue check reduced to plain-voice read. Second person, short paragraphs.
- Originality: own wording, own example prompt, nothing taken from Anthropic Academy or other courses. Academy appears only as two links.
- No statistics. No product settings named.
- Mechanical slop check: NOT RUN. Script-room had no Bash tool this session. Substitute: regex search for em dashes, en dashes and common AI-tell words, zero hits. Caller must run slop_check.py.

Pass 2 (2026-11-12, GENERATE, structure, plain language, originality, clearance, statistics)
- Structure: order holds, quiz div last. Fixed Further reading: it said "three questions follow" before links; now says links are optional, then announces the quiz.
- Plain language: fine for a beginner. Time line corrected to read plus try time. Added a line for a reader with no AI chat set up yet. Softened "Most of the time" to "Often" (an unsourced frequency claim).
- Originality and clearance: own wording, no Academy text copied, no quotes, lyrics or poems. Academy appears only as links.
- Statistics: none in the lesson. No primary source needed.
- Academy links: both point to the same root URL. Retrieval of the page was not done here, so UNVERIFIED. Link labels no longer claim specific course titles.
- Quiz (quizzes.js): 3 questions, answers match the lesson text.
- Mechanical slop check: NOT RUN, no Bash tool in this session. Substitute regex search for em and en dashes and AI-tell words over Teacher\site\docs. Caller or qa-director must run slop_check.py.
Handed to qa-director.

## 2026-11-12, Lesson 1 Practice section and Module 5 index
Mode: REVIEW and fix (room-written teaching copy, not Zac's prose). Files: module-1\lesson-1.md (Practice section, closing two sentences), module-5\index.md.

Pass 1 (structure, plain voice, originality, clearance, statistics)
- Practice: pattern order held in all 3 tasks (heading, why, do this, text fence, self-check, good looks like, rules). practice-done div and quiz div intact, quiz last.
- Private data: Task 1 asks only for a household brand and model. Task 2 text is made up and uses "[link]". Task 3 list is made up. Each task tells her not to paste real private data.
- Statistics: none. Task 1 "Why it matters" overstated ("exactly the ones AI gets wrong"), softened to a claim with no frequency.
- Unverified UI claim: "copy button in the top right corner". Position not confirmed, reworded to say each prompt box has a copy button.
- Closing sentences reworded: "practice button below" so it points at the div that follows.
- Module 5: checked against the local clone. 542 lessons and 20 phases match the README. Type, time and prerequisite lines match for all five lessons. Heading names match for lesson 11/01 (Role Prompting, Instruction Clarity, Constraint Specification, Anti-Patterns, Build It), 18/04 (The Problem), 18/15 (delivery vectors for RAG, email, tool output), 18/23 (Limitations), 18/24 (opening). Phase 0 setup and Phase 1 math confirmed in README. Phases on training models not confirmed, the page already says folder names only.
- Fixed: Sycophancy row claimed "the math section", but its headings show "The two-stage formalism", so reworded to say that.
- Plain voice: replaced "look under the hood" and "click harder".

Pass 2 (same checks, fresh read)
- No em or en dashes found by reading. No AI-tell words spotted. Second person, short sentences, fine for a beginner.
- Originality and clearance: own wording, no quotes from the repo, no lyrics or poems. Repo is linked, MIT, credited as someone else's course.
- Module 5 makes no claim about a lesson beyond its header or headings, except the Phase "I did not open them" caveats, which are stated as such.
- Statistics: none in lesson. Module 5 mentions repo count and dates only, sourced to README.
- Mechanical slop_check: NOT RUN by script-room (no Bash). Caller ran it: clean except known CSS class and endpoint-name false positives.
Open flags: Task 2 and 3 point to Module 3 and Module 2 as covering scams and privacy. Those modules are planned, not confirmed built. Module 5 "latest commit 2026-11-12" and MIT were taken from the Teacher CLAUDE.md note, not re-checked here.

## 2026-11-13, Track 1 Start Here, lessons 1 to 3 (drafts)
Mode: GENERATE. Files: D:\WKP\Teacher\drafts\track-1\lesson-1.md (What AI is, in plain words), lesson-2.md (Meet Claude), lesson-3.md (Your first good prompt), quizzes-draft.js. Not in the live site. Format copied from stay-safe\check-what-ai-tells-you.md (the live lesson has no front matter, so none added). Wiring (course.js, quizzes.js, mkdocs nav) is left to software-director.
Passes were run by script-room itself, inline. No separate bench agents were called (no Bash and a 150k budget).

Pass 1 (structure)
- L1: Task 3 told her to try "the last two" jobs but the prompt covers only store hours. Fixed to the store-hours job. Further reading used two deep vendor URLs not retrieved, replaced with chatgpt.com and claude.ai.
- L2: "What you will make" said five uses, Task 3 makes ten. Fixed. Removed a promise that the next lesson reuses the page. Hedged "cannot do things in the real world" to what a plain chat does, since connected tools exist. Pricing links claude.com/pricing, support.claude.com, chatgpt.com/pricing are UNVERIFIED, sent to qa-director.
- L3: Task 1 versions now each in a new chat so earlier answers do not bias later ones. Task 3 now starts a new chat with version C so "make the plan shorter" has one plan to act on. Further reading labels fixed.
- Practice parts present in every task: heading, why, do this, text fence, self-check, good looks like. Quiz div last in each file.
- Quiz: 3 questions per lesson, answers checked against lesson text. Correct answers are spread across positions, not all first.

Pass 2 (plain words, originality)
- Plain words: short sentences, no jargon beyond "prompt" (defined in L3 before use; L1 and L2 use "AI chat tool" and "message"). Checked for em dashes, en dashes and AI-tell words by regex over the folder, zero hits.
- Originality: own structure, own examples (dinner, birthday party, pharmacy hours, her email cleanup). No text from the research report's link-only courses. The four-part prompt frame is own wording.
- Facts: only that Claude is made by Anthropic and ChatGPT by OpenAI, and the general descriptions of how these tools work. No free-tier limits, model names, memory, search or image feature claims. Free-plan rules are "check this yourself" with the pricing links and a dated note in Task 1.
- Clearance: no quotes, lyrics, poems or third-party text.
- Mechanical slop_check.py: NOT RUN by script-room (no Bash tool). qa-director ran it afterward: all files clean except one false positive ("kind of" in lesson-2, since reworded).

QA verdict (qa-director, arrived after hand-back): PASS WITH NOTES, report D:\WKP\logs\qa\2026-11-13-teacher-track1-lessons-1-3.md. Quiz answers match, links return 200 (claude.ai 403 to curl, normal), page contents not read. Fixes applied after the verdict: "You have both" (L1), Stay Safe overpromise softened (L1), AI tool named for the pharmacy test (L1), upload-button claim reworded (L2), ten-uses wording fixed (L2), Google Doc click steps added (L2), New chat click step added (L3). Still open: Google Doc steps in L3 Task 1 and a second New chat mention in L3 Task 2 and 3 are not spelled out beyond the first.

## 2026-11-13, Track 1 Start Here, lessons 4 to 9 (drafts)
Mode: GENERATE. Files: D:\WKP\Teacher\drafts\track-1\lesson-4.md (Give it a role and context), lesson-5.md (Show it examples), lesson-6.md (Make it show its work), lesson-7.md (Long tasks: files, chats and memory), lesson-8.md (Build a prompt library), lesson-9.md (Advanced: chains and checking), quizzes-draft-b.js (keys start-here/role-and-context, show-examples, show-its-work, long-tasks, prompt-library, chains-and-checking). Not in the live site. Site folder untouched. Fact pack (research\teacher\2026-11-13-fact-pack.md) did not exist when lessons 7 and others were written, so every free-tier, upload, memory and price point is "check this yourself" with the vendor link.
Passes were run by script-room inline (no bench agents; the Bash tool was not available in this session either, so the mechanical slop check went to qa-director).

Pass 1 (structure, 2026-11-13)
- Every lesson has: what you will be able to do, what you will make, teaching, Keep this in your pocket, Practice with 3 tasks, practice-done div, Further reading, quiz div last.
- Fixed in pass 1: lesson-6 Task 1 arithmetic was wrong (chicken is 4 lb at $14, total $28, $32 left, not $28 chicken); lesson-4 pointed to "lesson 1.8" which the learner never sees, now says the prompt library lesson; lesson-8 Tasks 2 and 3 had no copy-paste prompt fence, added one each; lesson-9 "often catches" softened to "can catch" (unsourced frequency).
- Quiz: 18 questions, correct answers spread across positions 0, 1, 2 (six each). Answers checked against lesson text.
- Per lesson "what she makes": 4 grocery list in three voices, school note in two voices, firm letter; 5 reusable template with two examples; 6 checked-answer sheet (arithmetic, claims list, sources opened); 7 summary, action list, draft reply and handoff note from a made-up newsletter; 8 ten-prompt Google Doc notebook; 9 a three-step chain for a real chore, with a review pass.

Pass 2 (plain words, originality, clearance, facts)
- Plain words: regex search over lessons 4 to 9 for em dashes, en dashes and AI-tell phrases. Hits were "kind of" (3 places), all reworded. Remaining text is short second-person sentences.
- Overclaims softened: lesson-6 "you now know it is reliable on arithmetic" changed to "one clean result, not a guarantee"; "once and for all" removed.
- Originality: own examples (dinner chain, Maple Court newsletter, blender letter, pantry cards, Rosa thank-you). The role, context, audience frame is own wording. No text from Anthropic or DeepLearning.AI courses, no quotes, lyrics or poems.
- Facts: no statistics. Free-tier limits, file attach, memory and prices are all "check this yourself" with claude.com/pricing, support.claude.com, chatgpt.com/pricing (links as used in lesson-2, not read by script-room). Unverified UI claims: Google Docs "Blank document" tile, "Heading 2" in the style box, Claude "New chat" at top left (copied from lesson-3).
- No Firefly or Veo credits, no paid features, no signups beyond her own Google account for Docs (lesson 2 already uses a Doc).

## 2026-11-13, Track 3 Build and Automate, lessons 3.1, 3.2, 3.3, 3.5 (drafts)
Mode: GENERATE. Files: D:\WKP\Teacher\drafts\track-3\lesson-1.md (Automate with a spreadsheet), lesson-2.md (Ask Claude to write a formula), lesson-3.md (Forms to sheets), lesson-5.md (Your first web page), quizzes-draft.js (keys build-automate/automate-with-a-spreadsheet, ask-claude-for-a-formula, forms-to-sheets, your-first-web-page). Not in the live site, D:\WKP\Teacher\site\ untouched. 3.4 not written (outline says verify free limits first). Fact pack at research\teacher\2026-11-13-fact-pack.md did not exist at write time, so no vendor facts are used. Passes run by script-room inline (no Bash, no bench agents, to hold the budget).

Pass 1 (structure)
- All four: header block, can-do list, what you will make, teaching, Keep this in your pocket, three practice tasks with every PRACTICE-PATTERN part, --- between tasks, practice-done div, Further reading, quiz div last.
- L1: Total cell was told to go in F6, which could collide with the summary block built in Task 2. Moved to F7 and G7 and told her to keep it out of column D (a total in D2:D100 would add itself). Range to row 100 explained before the practice, then shown failing in Task 3 (Grocery vs Groceries).
- L2: made self-contained (own gift-list sheet) so she can do it without lesson 1. Task 3's broken formula (Yes without quotes) is a real error case. Added the straight-quote warning for pasted formulas.
- L3: Task 2 tells her to read the headings and find the column instead of assuming one, since the time column may shift everything. Task 3 says plainly: the link goes to nobody in this lesson.
- L5: OS branch is a "Which computer do you have" check (Start button or Windows logo versus Apple logo, stop and ask if unsure), then Windows Notepad and Mac TextEdit steps side by side. File name trap (index.html.txt) and the Mac plain text switch are covered, both hedged "menus change". Asks Claude for HTML and CSS only, tells her to look for script lines and unrequested web addresses. Page stays on her computer, nothing is put online.
- Quizzes: 3 per lesson, answers checked against lesson text. Correct positions L1 1,0,2; L2 1,2,0; L3 1,2,0; L5 0,1,2.

Pass 2 (plain words, originality)
- Plain words: formula, range, tag and CSS each defined before use. No em dashes, en dashes or AI-tell words (regex over the folder, zero hits). Word counts estimated 1,400 to 1,900 by eye.
- Originality: own examples (a three-category budget, a gift list, a dinner vote form, five things I love). No text from TripleTen or other link-only courses. Own wording throughout.
- Facts: only stable general spreadsheet and HTML basics (SUM, SUMIF, COUNTIF, IF, tags, plain text editors, F5 and Command R reload). No free-tier limits, prices, plan features or platform rules. Every menu path hedged "menus change, look for the closest name". Google account and Claude limits are "check this yourself" with links. UNVERIFIED by click-through: the exact SUMIF behavior with these ranges, #NAME? for the unquoted Yes, comma versus semicolon by region (told her to check Google's help), and the TextEdit and Notepad dialog wording.
- Clearance: no quotes, lyrics, poems or third-party text. example.com used for the sample link.
- Mechanical slop_check.py: NOT RUN by script-room (no Bash). Handed to qa-director.
QA verdict (qa-director, arrived after hand-back): FAIL with 3 small blockers, report D:\WKP\logs\qa\2026-11-13-teacher-track3-lessons.md. Fixes applied after the verdict: B1 hedge word removed (L5); B2 Windows logo button wording, Control-click and Mac Get Info for extensions (L5); B3 text-fence items added to L3 Task 1 and Task 3 and L5 Task 1; N1 tie-in example now really splits (Tacos, Taco night, tacos please), quiz Q2 matched; N2 Grocery row now has an amount; N3 Track 1 reference softened; N4 ChatGPT named in L2 and L5; N5 preview-recording hedge in L3; N7 curly quotes softened to "can". slop_check after the fixes: qa-director ran it, exit 0 and no hits on lessons 1, 2, 3 and 5 (B3 fences confirmed by read). Not re-run: a full second QA pass, and B1/B2 were not re-checked by QA. Still open: N6 (Google account signup is worded as her choice, Zac should know), live Sheets and Forms click-through, no-ai-slop judgment pass.

## 2026-11-13, Track 4 Stay Safe, privacy and when-not-to-use (drafts in drafts\stay-safe\)

Pass 1 (structure, room-writer, PRACTICE-PATTERN check)
- Both lessons: outcomes, what you will make, teaching, Keep this in your pocket, three practice tasks with every PRACTICE-PATTERN part in order, --- between tasks, practice-done div, Further reading, quiz div last. Quiz draft: 3 questions per lesson, answer positions privacy 2,0,1 and when-not-to-use 1,2,0.

Pass 2 (plain words and originality, dialogue-doctor)
- Edits made: removed stock reassurance lines, spelled out the Settings click path hedged as unchecked, removed the husband-as-approver line, trimmed sentimental lines. After the mechanical check: three "kind of" hits reworded in privacy.md, and about 105 words trimmed from privacy.md and 28 from when-not-to-use.md to get under 1,500.
- Originality and clearance: no copied source, no vendor facts stated (training defaults and settings are "check this yourself" by design). Made-up samples only.

Results
- slop_check.py: first run privacy.md exit 1 (3 "kind of" hits), when-not-to-use.md and quizzes-draft.js clean. After fixes all three exit 0. Grep for em dashes: zero in all three.
- Word counts (python split, div lines excluded): privacy.md 1,494; when-not-to-use.md 1,489. Both inside 1,000 to 1,500.
- Fact pack comparison (research\teacher\2026-11-13-fact-pack.md): no lesson sentence conflicts. The "click your name, Settings, privacy or data" path is consistent with the pack's Claude path and is hedged.
- qa-director verdict: PASS WITH NOTES, no blockers. Notes (not applied, word counts have only 6 and 11 words of headroom): unhedged "left side of claude.ai" and "New chat at the top left" clicks; when-not-to-use Q1 explain borrows a line from lesson 1; correct quiz answer is the longest option in 4 of 6 questions; Task 1 pile definitions not stated in the lesson body; privacy Task 2 opener reads oddly; Find and replace and Ctrl+H steps are unretrieved but standard.

## 2026-11-13, Track 2 Make Things, "Write with AI" W1 to W5 (drafts in drafts\track-2\)

Pass 1 (structure, script-room GENERATE from Zac's guideline)
- Five lessons: W1 partner not ghostwriter, W2 brainstorm and outline, W3 drafting with context (own-writing mentor texts only), W4 revising with AI as editor, W5 long projects and fact-checking. One running piece (400 to 700 words) through all five, one-page "my writing method" checklist in W5 Task 3. Every task has all PRACTICE-PATTERN parts. No settings, context size or free-tier numbers stated; W3 says check whether your tool offers a creativity setting, links the tool pages.

Pass 2 (plain words and originality, dialogue-doctor)
- Fixed ambiguous "lesson N" references (now by title), removed claims about how models behave, cut stock lines, spelled out New chat and Docs clicks, fixed a self-check that contradicted its task (W4). Concern left: generic headings (W3 "Context is everything", W2 "Outlining without a straitjacket").

Results
- qa-director (D:\WKP\logs\qa\2026-11-13-teacher-write-lessons.md): PASS WITH NOTES. Word counts 1,303 to 1,489. slop_check had 5 "might" hits (W1 1, W2 3, W4 1), reworded afterwards. Not re-run, no Bash in this session.
- Applied after QA: "might" rewording, W1 and W4 pointer wording, W5 labels now matched / did not match / could not find (same as Stay Safe lesson), quiz Q3 and Q2 wording.
