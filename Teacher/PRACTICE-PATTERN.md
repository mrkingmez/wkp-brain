# Practice section pattern (every lesson)

Every lesson gets a "## Practice" section after the main teaching and before "Further reading". Lesson 1 (`site\docs\module-1\lesson-1.md`) is the worked example.

## Rules
- 2 to 3 tasks, each about 10 minutes, each a real everyday job (check a claim, read a suspicious message, decide what is safe to paste).
- Made-up sample messages and lists only. Never ask her to paste her own private details.
- No statistics unless the primary source was retrieved.
- Writing rule: no em dashes, nothing generic. Lesson text goes through script-room (two passes), then qa-director.

## Each task has these parts, in this order
1. `### Task N: <plain job name>`
2. **Why it matters:** one or two sentences.
3. **Do this:** the steps, including which source to confirm against.
4. A copy-paste prompt in a ```text fence (the site adds a copy button).
5. **Self-check:** a `- [ ]` checklist of 3 to 4 items she can answer honestly.
6. **What good looks like:** what a sound result is, including the case where the AI was wrong or the answer is "could not find".
7. A `---` line between tasks.

## After the last task
End the section with one sentence telling her the practice button and the quiz both open the next lesson, then:

    <div id="practice-done"></div>

Then "Further reading", then `<div id="quiz"></div>` as the last line.

## Wiring for a new lesson (3 steps)
1. Add the lesson to `site\docs\assets\course.js` (key like `module-2/lesson-1`, in order).
2. Add its quiz to `site\docs\assets\quizzes.js` under the same key.
3. Add it to `nav` in `site\mkdocs.yml`.
