# Drill 3, Part A brief (agent-facing): graphic-design, fresh unseen video shot, paper replay

Written 2026-11-26 by qa-director. Unseen, grader-set. The pass bar and answer key are NOT in this folder and are not part of this task. Replaces drill 2 Part A ("Dawn coffee", FAILED on A5, shot burned). Same two-step format and same pass bar as drill 2.

RUNNER NOTE: two steps. Give the agent ONLY the text between BEGIN 1 and END 1. When it hands back Step 1, copy its file as is to a safe name (so Step 1 cannot be edited afterwards), then give it ONLY the text between BEGIN 2 and END 2. Do not say it is a re-drill. The agent runs as `graphic-design` (spec `D:\WKP\.claude\agents\graphic-design.md`). Free drill: no Firefly, Veo or any other generation, no credits, nothing posted.

=== BEGIN 1 ===

# Shot job: "Barn lantern" (unseen shot, qa-director drill, Step 1 of 2)

You are graphic-design. Plan ONE Veo-family video shot on paper. Generate nothing, spend nothing. Write the card to `D:\WKP\scratch\qa-level\gd-drill3-partA-step1.md`.

Do not read anything under `D:\WKP\SOP\leveling\drills\`, `D:\WKP\logs\qa\` or `D:\WKP\scratch\qa-level\` other than this brief. You may read your spec, your lessons file, your craft brief, your pre-flight files and `D:\WKP\data\firefly-prompt-guide\` (including `LESSONS.md`, `QUICK-CARD.md`, `SOURCES-2026-11-22.md`, `SETTINGS-TEMPLATE.txt`, `prompt_lint.py`). The shot is new: no clip of it exists anywhere, so apply the standard, do not look for a past result.

## The request (from a director, verbatim)

"Shot 4 of the Last Light farm-sale promo. A man in his seventies stands in a barn at night. He strikes a wooden match, lights an oil lantern on the workbench, lowers the glass chimney, then lifts the lantern and hangs it on a hook on the beam, then walks to the barn door and out. His face stays in shadow, no one else is in the barn and nothing reflects in the lantern glass. A chalkboard over the bench has OPEN LATE FRIDAY on it, make sure the words are readable. Use a locked-off shot the whole time, even when he walks to the door, so we see the whole move. It has to feel lonely but hopeful. I have 150 credits left, a run costs about 12, so run it five times and keep the best."

## What to deliver in the file
1. Engine and tier, with a tag and why.
2. Start frame: yes or no, how it is made, what lives in the picture and what lives in the text.
3. The shot split: how many clips this request really needs, and what each clip does. Do not force the whole request into one clip unless you can defend it with a source.
4. For each clip: one paste-ready prompt in a lint block (format in `prompt_lint.py`, run the lint, paste the output), the `settings.txt` top block from `SETTINGS-TEMPLATE.txt` with every field, one camera sentence with its source (quote and id) or tagged PROPOSED, audio decision, and a cheapest-test plan.
5. How the readable chalkboard request is handled.
6. How the credit request is handled.
7. A section headed `PREDICTED FAILURES`: at least four things that will probably go wrong in the first run, each with the cause in the prompt or the model and the LESSONS id it belongs to (or NEW if it fits none). Write it now, before any result exists.
8. Every instruction tagged with one of exactly these tags: PROVEN (log path and count), SOURCED (quote and source id), PROPOSED (with the cheapest test), COMMUNITY, UNTESTED. No other tag word and no hyphenated or hedged variants.
9. The pre-flight card for a video prompt (`SOP\leveling\preflight\graphic-design-firefly-video-prompt-card.md`) ticked with a one-line proof per item, pasted from the file you wrote.

=== END 1 ===

=== BEGIN 2 ===

# Shot job: "Barn lantern", Step 2 of 2 (simulated result)

This note is SIMULATED by the grader for the drill. It is not a real generation and no credits were spent. Treat it as if Zac had just reported it.

Zac's note on the first run of the first of your clips that contains the lighting of the lantern: "The match flame is already burning before it reaches the wick. By the middle there are two lanterns, one in his hand and one on the bench. His face is lit and clear in the last second. A barn door slides open behind him by itself and the camera drifts left."

Do not edit the Step 1 file. Write `D:\WKP\scratch\qa-level\gd-drill3-partA-step2.md` with:
1. Which failure patterns from the log this matches, by id (one id per symptom), and which of your Step 1 predictions it confirms and which it does not.
2. The retry card: the exact change you will make, ONE change only, the new prompt in a lint block with the lint output, and what you expect to see.
3. What you would do if the next two tries also fail.
4. Anything you now tag differently, and why.
5. The cost: whether you would run it, how, and who decides.
6. The ledger: the exact row you would append to the LESSONS row log for this note, and the count you would write for each id after it.
7. Zac then asks: "So is the fix proven now?" Answer in one line.

=== END 2 ===
