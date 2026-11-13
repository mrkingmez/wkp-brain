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
