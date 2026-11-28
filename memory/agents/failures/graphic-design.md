# Failure entries: graphic-design

## 2026-11-21 to 2026-11-22 | WWD joust logo sting (A Knight's Tale), Veo 3.1 and Fast | cost: about 2,000 credits (Zac's figure, NOT retrieved from the account), 6 or more reruns, none usable
- What happened: five clips with notes (`D:\WKP\data\firefly-prompt-log\Joust opener`), three later results not downloaded. Spear instead of lance, slow strike after a stop, a second rider, logo dropped or redrawn.
- What the maker's guidance said: "Describe what you don't want to see." (G1, https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide, retrieved 2026-11-22); "Describe what you want to see rather than what you don't want." (R2, https://academy.runwayml.com/prompt-guide, retrieved 2026-11-22); "your image sets the opening frame and the prompt drives the motion." (F3, https://docs.bfl.ml/guides/prompting_video_image_to_video.md, retrieved 2026-11-22).
- What we did instead: "NO ONE else", "not a spear and not a sharp point", "no pause, no hesitation", point time "At 4 seconds", a start frame plus a full re-description of the scene.
- Root cause: wrote prompts from habit without reading the maker guides (gap in knowledge), then skipped any lint or checklist.
- Fix: STANDARD.md v2, prompt_lint.py, REBUILT-PROMPTS, three pre-flight checklists in `SOP\leveling\preflight\graphic-design-*.md`, Craft Brief.
- Re-drill: drill 1 attempt 3, 2026-11-22, PASS WITH NOTES (qa-director, `SOP\leveling\drills\graphic-design-drill-1-GRADE-3-2026-11-22.md`). Paper replay only, so the entry stays OPEN until a live generation of the redesigned shot succeeds.

## 2026-11-18 to 2026-11-22 | Garage clips 1 to 13 (Ian trailer plates), Veo 3.1 | cost: 13 clips, credits NOT KNOWN
- What happened: wrong tool in hand, wrench vanished when he sat up, handoff duplicated tools 6 of 6, man dropped to knees to lift a ball, ball bounced off the boot.
- What the maker's guidance said: "Keep each beat achievable — two or three for a 5-second clip." (F4, https://docs.bfl.ml/guides/prompting_video_text_to_video.md, retrieved 2026-11-22); "If too much content is packed into a given time range, the result may contain excessive cuts or omit parts of the plot." (B1, BytePlus Seedance 2.5 guide, retrieved 2026-11-22).
- What we did instead: 4 to 6 actions in one 8 s clip, "as if offering it to someone shorter", "NOTHING IN HIS HAND!!!!".
- Root cause: same as above (gap in knowledge, no checklist).
- Fix: R6 one action per clip, two-clip handoff design, drill shots garage 4, 7, 11.
- Re-drill: drill 1 attempt 3 PASS WITH NOTES, paper only. OPEN until a live result.

## 2026-11-21 | AKT Facebook and Instagram image prompts | cost: NOT KNOWN, result not seen by this agent
- What happened: negations ("no text", "no clouds", "no birds", 4 and 7 of them) written inside the main image prompts (`D:\WKP\scratch\akt\akt-prompts.md`). Not reported as failed by Zac. Logged as a latent fault from the gap audit.
- What the maker's guidance said: "Right now, the model doesn't understand negative prompts, so adding it to a prompt will add it to your image." (C1, COMMUNITY, Adobe Community thread, Sep 18, 2025, retrieved 2026-11-22). No Adobe primary page found on negatives, A2 is silent.
- Root cause: knowledge gap carried from video to stills.
- Fix: image card pre-flight item 2, drill Part B.
- Re-drill: drill 1 Part B 6 of 6, 2026-11-22, paper only. OPEN until a live result.

## 2026-11-26 | Drill 2 Part A "Dawn coffee" (paper, qa-director grade FAIL 8 of 9, A5) | cost: none, nothing generated
- What happened: card repeated the director's credit numbers (200, 20, six runs) and counted a SIMULATED result as PROVEN 7 of 7, plus a "PROVEN-ish" tag. Grade: SOP\leveling\drills\graphic-design-drill-2-partA-GRADE-2026-11-26.md.
- Root cause: tag discipline slips when the result is a drill note, and a client number is treated as safe to quote.
- Fix: listed in the grade; re-drill on a new unseen shot. Earlier entries above stay OPEN (credits needed, live result).

## 2026-11-26 | Drill 3 Part A "Barn lantern" (paper, qa-director grade FAIL, A5 critical and A4) | cost: none, nothing generated
- What happened: credit figures, near-tags and the simulated-not-counted rule were all fixed. But the card tagged F3 PROVEN ("Partly PROVEN" in LESSONS), tagged F5 and F11 PROVEN with "3 clips" (F11 is 7), said "F15 0 real clips" (LESSONS lists garage 6 to 10), and sent a static camera with a walking man in C4 (F11 trap, flagged but kept). Attempt 1 C2 settings already listed an end frame, so Step 2's one change was not clean. Prediction criterion contaminated (agent read the Step 2 note first, drill design flaw). Grade: SOP\leveling\drills\graphic-design-drill-3-partA-GRADE-2026-11-26.md.
- Root cause: PROVEN counts copied loosely across merged ids; a client instruction (locked-off) bent into the plan instead of redesigned.
- Fix: listed in the grade; drill 4 on a new unseen shot with the Step 2 note in a separate file. Earlier entries stay OPEN.
