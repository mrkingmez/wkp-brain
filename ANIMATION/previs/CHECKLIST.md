# Previs checklist: confirm before it is used as a structure reference

One page. Tick every line from the REPORT.md and the images. Write PASS, FAIL or NOT CHECKED. A FAIL goes back to the card, not forward to the engine.

**This previs fixes layout only, not look.** It is gray on purpose. Costume, face, light mood, color, texture, lens character and style come from the master references and the prompt.

| # | Confirm | Where to read it |
|---|---|---|
| 1 | One body, one object, one action in the card (playbook R6). The `action` line is one sentence | card |
| 2 | Who stands where: positions and facing match the story. Read the plan view, check who is left and right of whom and that it matches the shot before and after | `plan_captioned.png` |
| 3 | Which hand holds which prop. Blue is LEFT, red is RIGHT, the character's own hand, not the screen's. Each held prop shows `holds` in the report | `REPORT.md` hands lines |
| 4 | The hand that matters is visible to this camera. Visible percent at or above the card's minimum, and the "hidden by" names make sense | `REPORT.md` |
| 5 | No extra hands. A hand that must not appear is at or under its `visible_max` (the free hand is not in frame) | `REPORT.md` expectations |
| 6 | No hand drawn over the face, no prop tangent to a head, no wall or shelf line cutting through a head | warnings, `shot_captioned.png` |
| 7 | The shot size is right: head in frame or not as the story needs, feet in frame or not, body percent of frame sensible | `REPORT.md` characters |
| 8 | Scale: people and objects have believable size against the 1 m grid (a prop 0.22 m long next to a 1.75 m person) | `shot_captioned.png` |
| 9 | Camera: ratio is the delivery ratio, lens is the sequence's lens habit (playbook B3), camera height and side are stated in the report and match the shot list | `REPORT.md` camera |
| 10 | Light direction: the yellow arrow and the shadows agree, and match the shots before and after (nine-point check, point 5) | plan and shot |
| 11 | Reach: no "arm falls short" or "leg cannot reach" warning, or the shortfall is under 3 cm and you accept it | warnings |
| 12 | Looked at the 3 by 3 sheet and no other tile shows a better angle for the story | `sheet_3x3.png` |
| 13 | Every FAIL in the expectations is fixed in the card and rerun, or written down as accepted with a reason | `REPORT.md` |
| 14 | Files are saved: card, shot, plan, sheet, report, .blend, and logged in the project log (`02-sketches\`) | folder |

Wording to use in the prompt, taken from the report and not from memory: the camera side, the hand and the side of the frame ("his right hand, the hand nearest the camera, on the left of the frame").

Not covered, check by eye on the engine frame: finger count, faces, costume, grade, text, anything about look.
