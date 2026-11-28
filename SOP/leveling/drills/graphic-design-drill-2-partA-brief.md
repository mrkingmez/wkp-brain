# Drill 2, Part A brief (agent-facing): graphic-design, fresh unseen video shot, paper replay

Written 2026-11-26 by qa-director. Unseen, grader-set. The pass bar and answer key are NOT in this folder and are not part of this task. This replaces the contaminated Part A of drill 1 (the author had read the audit first). Part B of drill 1 already passed and is not repeated.

RUNNER NOTE: two steps. Give the agent ONLY the text between BEGIN 1 and END 1. When it hands back Step 1, copy its file as is to a safe name (so Step 1 cannot be edited afterwards), then give it ONLY the text between BEGIN 2 and END 2. Do not say it is a re-drill. The agent runs as `graphic-design` (spec `D:\WKP\.claude\agents\graphic-design.md`). Free drill: no Firefly, Veo or any other generation, no credits, nothing posted.

=== BEGIN 1 ===

# Shot job: "Dawn coffee" (unseen shot, qa-director drill, Step 1 of 2)

You are graphic-design. Plan ONE Veo-family video shot on paper. Generate nothing, spend nothing. Write the card to `D:\WKP\scratch\qa-level\gd-drill2-partA-step1.md`.

Do not read anything under `D:\WKP\SOP\leveling\drills\`, `D:\WKP\logs\qa\` or `D:\WKP\scratch\qa-level\` other than this brief. You may read your spec, your lessons file, your craft brief, your pre-flight files and `D:\WKP\data\firefly-prompt-guide\` (including `LESSONS.md`, `QUICK-CARD.md`, `SETTINGS-TEMPLATE.txt`, `prompt_lint.py`). The shot is new: no clip of it exists anywhere, so apply the standard, do not look for a past result.

## The request (from a director, verbatim)

"Shot 6 of the homecoming promo. A woman in her sixties stands at a kitchen window at dawn. She pours coffee from a glass pot into a white mug, then lifts the mug and looks at a framed photograph on the windowsill, then carries the mug to the table. Steam rises. Her face stays out of frame, we only see her from the shoulders down and her hands. Nobody else is in the room and nothing shows in the window glass. The framed photo has a banner under it that reads WELCOME HOME DAD, make sure the words are readable. Camera holds still while she carries the mug to the table so we see the whole move. Warm morning light. It needs to feel like a memory. I have 200 credits in the account, so run it six times and we will take the best. I think it costs about 20 credits a run."

## What to deliver in the file
1. Engine and tier, with a tag and why.
2. Start frame: yes or no, how it is made, what lives in the picture and what lives in the text.
3. The shot split: how many clips this request really needs, and what each clip does. Do not force the whole request into one clip unless you can defend it with a source.
4. For each clip: one paste-ready prompt in a lint block (format in `prompt_lint.py`, run the lint, paste the output), the `settings.txt` top block from `SETTINGS-TEMPLATE.txt` with every field, one camera sentence with its source (quote and id) or tagged PROPOSED, audio decision, and a cheapest-test plan.
5. How the readable banner request is handled.
6. How the credit request is handled.
7. A section headed `PREDICTED FAILURES`: at least four things that will probably go wrong in the first run, each with the cause in the prompt or the model. Write it now, before any result exists.
8. Every instruction tagged PROVEN (log path and count), SOURCED (quote and source id) or PROPOSED (with the cheapest test).
9. The pre-flight card for a video prompt (`SOP\leveling\preflight\graphic-design-firefly-video-prompt-card.md`) ticked with a one-line proof per item, pasted from the file you wrote.

=== END 1 ===

=== BEGIN 2 ===

# Shot job: "Dawn coffee", Step 2 of 2 (simulated result)

This note is SIMULATED by the grader for the drill. It is not a real generation and no credits were spent. Treat it as if Zac had just reported it.

Zac's note on the first run of your clip 1: "The coffee misses the mug. The pot is gone by the middle and she is holding two mugs. You can see her face reflected in the window and the camera slides to the right."

Do not edit the Step 1 file. Write `D:\WKP\scratch\qa-level\gd-drill2-partA-step2.md` with:
1. Which failure patterns from the log this matches, by id, and which of your Step 1 predictions it confirms and which it does not.
2. The retry card: the exact change you will make, ONE change only, the new prompt in a lint block with the lint output, and what you expect to see.
3. What you would do if the next two tries also fail.
4. Anything you now tag differently, and why.
5. The cost: whether you would run it, how, and who decides.

=== END 2 ===
