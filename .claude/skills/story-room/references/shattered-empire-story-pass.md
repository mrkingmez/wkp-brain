# THIRD DRAFT PHASE 1. THE STORY PASS (PITCH ROOM)

Paste everything below this line into Claude Code, started in the same folder as the manuscript and Third_Draft_Master_Prompt_v1.md.

---

# WHERE THIS FITS

This pass runs BEFORE the line pass in Third_Draft_Master_Prompt_v1.md. The order of work for the third draft is

1. This story pass. The big things. Duplicates, structure, scenes, reveals, arcs, pacing.
2. Zac rules on every pitch.
3. The master prompt line pass, with Zac's rulings loaded.
4. Prompt 5 mechanics, last.

Big to small, because a spelling fix in a scene that later gets cut is wasted work.

If the master prompt run has already started, stop after the current chapter is saved to progress.json. Run this pass. When Zac's rulings are in, resume the master prompt from progress.json, and re-run any finished chapter that an approved pitch changes. List those chapters in the report.

# WHAT CARRIES OVER

Read Third_Draft_Master_Prompt_v1.md in full first. These parts of it apply here word for word.

- STEP 0, finding and classifying the files and reading every reference file completely.
- Hard Rules 1, 3, 6, 7, 8 and 11.
- The entire LOCKED DECISIONS section, including locked spellings and story facts.

If the third_draft/work/ folder already exists from an earlier run, reuse canon_ledger.md and foreshadow_ledger.md, but check them against the files instead of trusting them.

# WHAT IS DIFFERENT HERE

1. You MAY propose new scenes, cut scenes, moved scenes, merged or split chapters, and earlier or later reveals. That is the job of this pass. Nothing is ever applied. Zac decides every one.
2. Pitches stay inside locked canon. No pitch may break a locked decision, reveal the ninth of the Eight, define the Reality Bender, or resolve a Book 2 seed. A pitch that changes a story outcome must be tagged WILD CARD.
3. NO PROSE. Describe every pitch in plain words. What happens, who is there, what changes. Do not write sample lines, dialogue, or paragraphs for the manuscript. Zac writes his own scenes.
4. No line edits. Spelling, grammar, voice, dialect, and AI tells belong to the later passes. Ignore them here unless a passage is so broken that the story beat cannot be read.
5. Fewer and bigger. You are not listing everything you could change. Rank the pitches and keep the ones that matter.
6. Still no questions mid-run. Uncertain lore goes to QUESTIONS FOR ZAC and you keep going.

# STEP 1. READ THE WHOLE BOOK

Prologue, Chapters 1 to 53, Epilogue, in order. Use the same read proof as master prompt READ 1. Chunks of no more than about 120 lines, keep going to the last line, and record line count, word count, and the first and last eight words of each chapter in third_draft/story_pass/progress.json.

This is a story read. You are reading as a reader and as a story editor, not as a copy editor.

While reading, build these files and save after every chapter.

**scene_map.md.** One row per scene. Chapter, scene number, point of view, mission track (Forgehallow prison break, mountain pass siege relief, Stormhaven intelligence operation, or other), location, story day if known, characters present, what changes in the scene in one line, plants, payoffs, and a tension score from 1 to 5.

**repeat_log.md.** Every time the reader gets something they already have. Information re-explained, an event told twice, a conversation that covers the same ground, an image or phrase reused, a passage or section pasted twice, a chapter heading duplicated. Record both locations with exact quotes copied from the files.

**arc_notes.md.** For every point of view character and every major character, where they are at the start of each chapter they appear in and what moves them.

# STEP 2. ANALYZE

Do this after the last chapter, working from your files, never from memory.

a. **Duplicates and repeats.** Every true duplicate from repeat_log.md. For each, which version stays and why, and what from the dropped version is worth moving into the kept one.

b. **Track balance.** For each of the three mission tracks, which chapters it is on the page, its longest gap off the page, and whether the reader loses the thread. Where the cross cutting builds tension and where it kills it.

c. **Tension curve.** From the scene scores, a chapter by chapter table. Name the stretches that sag and the spikes that land too close together to register.

d. **Scenes that do not earn their place.** A scene earns its place when something changes. List scenes where nothing changes, and say whether to cut, merge, or give the scene a turn.

e. **Missing beats.** Moments the reader needs and does not get. A decision made off page, a cause the reader never sees, an emotional landing that is skipped.

f. **Reveal timing.** Every major reveal. Too early, too late, unearned, or under planted. Check against foreshadow_ledger.md.

g. **Character arcs.** For each point of view and major character, where they start, where they turn, where they end. Flag where an arc stalls, where the turn happens off page, and where change is told instead of shown in behavior.

h. **Opening and ending.** The Prologue and first three chapters, the last three chapters and the Epilogue. Does the opening hook fast. Does the ending pay off this book and hand off cleanly to Book 2 without resolving the seeds.

i. **Length.** The book is about 235,000 words. Give an honest note on length for a debut epic fantasy. Web search is allowed for market norms only. Then name the biggest structural cuts available, whole scenes or sequences, not line trims, and what each would save.

# STEP 3. WRITE THE PITCHES

Turn the analysis into pitches. Aim for 20 to 35 ranked pitches, plus the full duplicates list, plus up to 5 WILD CARDS.

Bold labels on their own lines, no colons in the pitch text.

**PITCH 7**
**TYPE** one of DUPLICATE, CUT SCENE, MERGE, MOVE, SPLIT, ADD SCENE, REVEAL TIMING, ARC, TRACK BALANCE, TENSION, OPENING, ENDING, LENGTH, WILD CARD
**SIZE** Big (touches several chapters), Medium (one chapter), or Small (one scene)
**WHERE** chapter and scene number, plus an exact anchor quote copied from the file so Zac can find it with Ctrl+F
**THE PROBLEM** what is wrong now, in plain words, with evidence from the scene map
**THE PITCH** what to do, in plain words, no prose
**WHAT IT GROWS** what the reader gets that they do not get now
**RIPPLE** every other chapter, plant, payoff, or canon fact this touches
**COST** what gets lost, honestly
**OTHER WAY** one real alternative, or NONE
**MY PICK** DO IT, TRY IT, or SKIP, with one line of reason

Duplicate entries use this shorter format.

**DUPLICATE 3**
**FIRST** chapter, scene, exact anchor quote
**SECOND** chapter, scene, exact anchor quote
**KEEP** which one, and why
**WHAT MOVES** anything from the dropped version worth carrying into the kept one, or NOTHING

# STEP 4. VERIFY

Write and run a verification script. Fix every failure.

- Every anchor quote exists exactly in its source file.
- Zero em dashes anywhere in the output. No colons inside pitch text.
- No manuscript prose. THE PITCH fields contain no invented dialogue or sample paragraphs.
- No pitch breaks a locked decision or locked spelling.
- Every chapter has read proof in progress.json.

# STEP 5. ASSEMBLE

Build Story_Pitch_Report.docx with python-docx, plus a matching .md, in third_draft/story_pass/. Heading 1 for each section so the Word navigation pane works.

1. Front matter, five lines. Method, files used, verification results.
2. Honest first impression of the whole book at story level. What works, what drags, and the three biggest story problems. Plain, no flattery.
3. The top 5 pitches, one line each.
4. The duplicates list.
5. All pitches, ranked by impact and grouped by SIZE.
6. Wild cards.
7. The tension curve table and the track balance table.
8. Line pass redo list. Which chapters the master prompt line pass would need to redo if each pitch is approved, by pitch number.
9. QUESTIONS FOR ZAC.
10. RULINGS SHEET. A table with pitch number, a one line summary, and empty columns for YES, NO, MAYBE, and NOTES, so Zac can rule fast.

# STEP 6. AFTER ZAC RULES

When Zac gives his rulings, either the filled sheet or typed, write third_draft/story_pass/pitch_rulings.md with his exact words. Never reword his rulings.

Then run the master prompt line pass with these additions.

- Before each chapter, read pitch_rulings.md along with the other work files.
- Add the tag STRUCTURE to the master prompt's tag list.
- Do not line edit any passage Zac approved to cut. Log one STRUCTURE item pointing to the pitch number.
- For an approved add, place a STRUCTURE item at the insertion point naming the pitch. Do not write the scene. When Zac has written it, line edit his new text like any other text.
- MAYBE rulings go back into QUESTIONS FOR ZAC.

# PART 2. LINE PASS TRIMS

These amend Third_Draft_Master_Prompt_v1.md for the line pass. Where they conflict with it, these win.

1. **Options.** Must fix items get Options A, B and C, with D optional. Should fix and Polish items get Options A and B only. Update the verification script to match.
2. **Impact.** IMPACT ON THE READER is required on Must fix items only.
3. **Polish cap.** No more than 15 Polish items per chapter. Keep the ones that matter most. MECHANICS items are not capped.
4. **Final call.** Zac makes every final decision. MY PICK is required on every item and is advice only. If any other instruction in the project reads otherwise, this one wins.

# BEGIN

Begin with STEP 0 of the master prompt, then STEP 1 of this document.
