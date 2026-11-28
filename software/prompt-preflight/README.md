# prompt-preflight (read this first)

A free checker for image and video prompts. You run it BEFORE you click Generate. It reads the words and tells you which ones have failed before on Zac's own clips, so you do not burn credits on a mistake we already know about.

It costs nothing, uses no internet, spends no credits, and generates nothing. It works on the words only. **It cannot predict what an engine will draw.** A clean verdict means "no known failure words", not "this will work".

## What the three verdicts mean
- **FAIL**: a rule backed by our own failed clips (or a plain structure mistake) fired. Fix it before you run the prompt. Exit code 1.
- **WARN**: a risk. Read the line. Fix it, or decide to run it anyway. Exit code stays 0.
- **PASS**: nothing fired. On a clean prompt the long `[PASS] R1 R2 ...` line lists every rule that was checked and found nothing. It is the proof the rule ran, not a problem. `--quiet` hides it.
- **INFO**: a note, nothing to fix necessarily. Never counts toward the verdict, exit code unaffected (only PF24 gives it).
- **OVERRIDDEN**: the author said `ALLOW` for that rule on purpose. It is shown, never hidden, and does not count as a FAIL.

Every finding line says: severity, rule id, what it found, WHY (plain words), FIX (plain words), and a tag in brackets. The tag tells you how sure we are: PROVEN means we saw it fail on Zac's clips (the count is in the rule table), PROPOSED means it is our idea and not yet tested, UNTESTED means a book or maker page says it and we have no failure of our own.

## Before you start (one time)
1. Find the Python line in `D:\WKP\LOCAL-PATHS.md`, section "Tools". That is the python.exe to use. Below it is written as `python`.
2. Open a terminal in `D:\WKP\software\prompt-preflight\`.

## Check one prompt you pasted (fastest)
1. Copy your prompt text.
2. Type this, put your text between the quotes, and press Enter:
   `python preflight.py --text "Static camera at floor level. A man turns a wrench." --kind video --engine veo`
3. Read the verdict on the first line. Fix every FAIL. Read every WARN.
4. For a long prompt, save it in a text file and run `python preflight.py myprompt.txt --kind video --engine veo`. Or pipe it in: `python preflight.py - --kind still` then paste and finish with Ctrl+Z, Enter on Windows.

Tell the tool what you are making, or it guesses and prints the guess:
- `--kind still` (a picture), `--kind video`, `--kind edit` (a "change this, keep that" edit), or `--kind auto`.
- `--engine veo` (or kling, seedance, runway, luma, flux, firefly, other). If you leave it out, only the engine-neutral rules run.
- Add what you know: `--start-frame yes` (a picture starts the video), `--end-frame yes`, `--audio on`, `--master NAME.png`, `--ref-type composition`.

## Check a file of prompts (the usual way for agents)
Prompts live in a markdown file inside blocks like this. The header keys are optional except the ones you need:

    ```prompt
    ID: GD-video
    KIND: video            (video | still | edit)
    ENGINE: veo
    START_FRAME: yes
    END_FRAME: yes         (NEW. Say yes if you will load a last frame)
    AUDIO: off
    SHOT: GD               (NEW. The shot name, used for history)
    MASTER: ball-v1.png    (NEW. The master reference file)
    REFERENCE_TYPE: style  (NEW. composition, style or none)
    MODE: new              (NEW. new or edit)
    ALLOW: PF04            (NEW. rule ids you override on purpose)
    NEGATIVE: text, logo   (NEW. The negative-field words, may run on to the next line)
    ---
    Static camera on the concrete floor. The baseball rolls and stops.
    ```

Run: `python preflight.py REBUILT-PROMPTS-2026-11-22.md --quiet`

**Important:** if you plan to use an End frame, write `END_FRAME: yes` in the header. Rule PF03 (rolling object ends at a boot or surface) warns only when no last frame is claimed. It counts as claimed when `END_FRAME: yes`, an `END_FRAME_FILE:` header key is filled in, or the prompt text says "last frame", "end frame" or "final frame" (for example "Image 2 is the last frame"; "no end frame" does not count). Notes outside the block are not read. The real source file `REBUILT-PROMPTS-2026-11-22.md` still has no `END_FRAME` key on the GD-video block (its SETTINGS line plans a last frame), so run on that file PF03 still warns until the key is added there.

The Ian format also works: a `prompt.txt` with a line starting `MAIN PROMPT`, the prompt, a blank line, a line starting `NEGATIVE FIELD`, and the negative words. Run `python preflight.py D:\WKP\data\firefly-prompt-log\ian-H1\prompt.txt`.

## Keep a retry history (so the tool can stop a fourth try)
1. Give the shot a name with `--shot S1` (or `SHOT:` in the block).
2. Point at a history file: `--history D:\WKP\data\firefly-prompt-log\S1\history.jsonl`.
3. Run the check. Add `--record` when you actually run the prompt. That adds one line (shot, attempt, date, text) to the file.
4. Next time the tool says: 1 or 2 tries so far and the same words, WARN "same words give the same result". More than 2 sentences changed since last time, WARN "stacked changes, change one thing". Three earlier tries, FAIL "redesign the shot, no fourth try".

**Safety of the history file.** A damaged or binary line in the history file is skipped, and the tool prints one line `NOTE: skipped N unreadable history lines`. It never crashes on it. A history path that is a folder, in a folder that does not exist, or not writable stops with a plain message and exit code 2.
**`--record` does not log a try whose verdict is FAIL**, because a prompt you were told not to run is not a try. It prints `not recorded: verdict FAIL`. If you ran it anyway, add `--record-anyway`.

The retry rule is printed under every video prompt: attempt 2 changes ONE thing, after attempt 3 redesign the shot.

## Check a settings.txt
`python preflight.py --settings D:\WKP\data\firefly-prompt-log\ian-H1\settings.txt`
It fails if any field from `SETTINGS-TEMPLATE.txt` was deleted, and warns if a credit number is typed but the panel readout is empty. Agents never type a credit number. Zac copies it from the Generate button.

## Typos in the header (PF31)
A KIND or ENGINE value the tool does not know (`ENGINE: veoo`) prints `[WARN] PF31` and falls back to the default (auto kind, engine other), which switches off the engine-specific rules. An unknown id in ALLOW (`ALLOW: PF99`) also prints a PF31 warning and overrides nothing. A block header with no `---` line after it prints a note, and a `.md` file with no ```prompt blocks prints `no prompt blocks found, treating the whole file as one prompt`. Empty text exits 2 with `no prompt text`.

Rule PF24 (no master named, or reference words with no role) is **info only** since 2026-11-24: it prints `[INFO] PF24 ...` as a note, never a WARN, and never counts toward the verdict. It still notes a missing `MASTER:` header, `--master`, "as in the first frame" (video with a start frame) or "as in the source" (edit).

Rule PF01 (side words) does not fire on camera-relative or screen-relative wording: camera left/right, screen left/right, frame left/right, left or right of (the) frame, nearest (the) camera, farthest (from) (the) camera. Bare `left` or `right` still fires, and for a video with START_FRAME yes the message tells you to remove them from the text.

Rule PF09 (text or logo) fires only on real requests: logo, wordmark, lettering, license or number plate, numerals, title card, an emblem painted or on a shield, "the words", "text reading/saying/that says", "letters reading/spelling". A dinner plate, "he reads a book", "a letter on the table" do not fire.

## Overriding a rule on purpose
Write `ALLOW: PF04` in the block header (or `--allow PF04,PF14`). The finding still prints as `[OVERRIDDEN]`. Use this only when you have a reason, and say the reason in the prompt notes.

## Other switches
- `--quiet` hides the PASS line. `--no-checklist` hides the nine-point checklist. `--json` prints machine-readable output. `--rules` prints the rule list.
- Exit codes: 0 = no FAIL, 1 = at least one FAIL, 2 = you typed the command wrong, a path is bad, or there was no prompt text. `--record-anyway` logs a try even when the verdict is FAIL.

## The nine-point start-frame check
For every video prompt the tool prints the nine points from `D:\WKP\REFERENCE\PROMPTING-PLAYBOOK.md` section D3 (identity, costume, place, camera language, light direction, grade, scale, perspective, time of day) plus our three extras: 10 hands and face clean at full size, 11 no text or logo in the picture unless it will be replaced, 12 the geometry the video needs (which hand, which side) is visible. The tool cannot see your picture. You tick these by eye on the start frame at full size.

## Where the rules come from
`RULE-TABLE.md` lists every rule with its evidence and the file the evidence came from. It is made from `rules.py` by `python gen_rule_table.py`, so the docs cannot drift from the code. Rules R1 to R13 come from the older checker `D:\WKP\data\firefly-prompt-guide\prompt_lint.py`, which this tool calls and does not copy. If you ever move the guide folder, set the environment variable `PREFLIGHT_LINT_DIR` to the new folder.

## Running the tests
Double-click `tests\run_tests.bat`, or run `python -m unittest discover -s tests -v` from this folder. All tests must pass. If the test "prompt_lint.py unchanged" fails, someone edited the old lint. If that was on purpose, put the new sha256 in `tests\LINT_SHA256.txt` and re-check the legacy baseline files in `tests\baseline\`.

## Files
- `preflight.py` the command and the `run_checks(text, meta, negative=None, history=None)` function
- `checks.py` one small function per new rule
- `rules.py` the rule table as data (evidence, sources, fixes)
- `gen_rule_table.py` writes `RULE-TABLE.md`
- `tests\` unit tests, regression tests, frozen copies of the real failed and good prompts (`fixtures\MANIFEST.json` records where each came from)
- `CHANGELOG.md` what changed

## Known limits
- It reads words. It cannot see a picture and cannot catch typos (no dictionary).
- Several rules are PROPOSED or UNTESTED, and the table says which. Do not treat a WARN from one of those as a law.
- Whether the Firefly panel has an End slot, a negative box, a seed field or a 750-character limit is NOT verified. Zac checks the panel once.

## Expect warnings (honest numbers, added after QA)
- On our 28 known-good prompts there are 0 FAIL, and 21 of the 28 still show at least one WARN (measured 2026-11-24 after the four noise fixes; it was 25 of 28). WARN counts per rule on that set: PF01 (bare side words) 14, PF02 (tool plus hands, no hand named) 8, PF26 (negative box) 4, PF09 (emblem painted on a shield, the real joust prompts) 3, R3 (length) 3, PF25 (over 750 characters) 2, and one each for PF06, PF10, PF15. PF24 (no master named) is now INFO only: 10 notes on that set, 0 WARN, and it never changes the verdict. PF03 fires on 0 of the 28 (the garage ball card now says `END_FRAME: yes`). A WARN is a "look at this" line, not a verdict on the prompt.
- Garage clip 5, our best clip, would FAIL here: R1 (it says "no camera movement"), R2 (caps RIGHT and LEFT) and R3 (189 words). So a FAIL on R1 or R3 is strong advice from our logs, not proof. If you run the prompt anyway, add `ALLOW: R1` style overrides in the block so it shows as OVERRIDDEN.
- Never read a clean PASS as "this will work". It only means no known failure words.
