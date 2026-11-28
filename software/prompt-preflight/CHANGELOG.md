# CHANGELOG

## 2026-11-24 noise reduction (four changes, one at a time, full suite rerun after each; good set 28 prompts, 0 FAIL throughout)
Good-set prompts with at least one WARN: 25 before, 22 after 1, 21 after 2, 21 after 3, 21 after 4.
1. PF24 is INFO only: new severity INFO, printed as `[INFO] PF24`, never WARN, never in the verdict. Evidence row kept, table text updated. (PF24 WARN 10 to 0.)
2. PF01 skips camera-relative and screen-relative wording (camera/screen/frame left/right, left/right of frame, nearest camera, farthest from camera). Bare sides still fire; video with START_FRAME yes keeps its message. (PF01 16 to 14.)
3. PF09 narrowed to real logo or text requests. Bare plate, reads, letter(s), text no longer fire. Old tests that expected 'A plate on the car', 'The sign reads open' and 'Letters on the wall' to WARN were changed to expect PASS, on purpose. Joust text with no start frame and an emblem still FAILs. (Good set PF09 stays 3: the real joust emblem prompts.)
4. PF03 warns only when no last frame is claimed (END_FRAME yes, END_FRAME_FILE header key, or 'last frame' / 'end frame' / 'final frame' in the text). New message 'no end frame claimed; if you plan one, write END_FRAME: yes'. New header key END_FRAME_FILE. Fixture GD-video got `END_FRAME: yes` because its card plans a last frame (GD-still-end, in the card's SETTINGS line). (PF03 1 to 0.)
- Tests 86 to 93. prompt_lint.py not touched, sha256 test and legacy baselines pass.

## 2026-11-24 tester fixes
- B1 damaged or binary history lines are skipped with one note, no traceback. B2 bad --history path (folder, missing folder, unwritable) exits 2 with a plain message.
- Empty or whitespace text exits 2 with 'no prompt text'.
- New rule PF31 (WARN): unknown KIND or ENGINE header value (falls back to defaults), unknown rule id in ALLOW.
- Notes for a .md file with no prompt blocks, and for a block header with no --- line.
- --record skips a FAIL verdict unless --record-anyway (also prints why when no SHOT).
- PF09 narrowed: bare text, letter(s), sign(s), caption(s), title(s) no longer fire; 'text/letters reading|saying|that says|on the', 'the words', 'reads' added.
- README lines added, RULE-TABLE.md regenerated. prompt_lint.py not touched (sha256 test passes).

## 2026-11-24 first build
- preflight.py, checks.py, rules.py, gen_rule_table.py, RULE-TABLE.md, README.md.
- Wraps prompt_lint.py R1 to R13 by path (unchanged logic). Adds PF01 to PF16, PF20 to PF26, PF28 to PF30 (PF17 folded into R2, PF27 is a context line on R1).
- Tests: unit and regression, frozen fixtures in tests/fixtures (MANIFEST.json), legacy baseline in tests/baseline.
- prompt_lint.py: one docstring pointer line added, no logic change (sha256 stored in tests/LINT_SHA256.txt).
- Changed from SPEC.md, with reasons: see the build report (PF04, PF05, PF10, PF11 wording of triggers; PF03 and PF24 header caveat).
