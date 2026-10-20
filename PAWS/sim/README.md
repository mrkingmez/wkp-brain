# Scout PC sim (Phase 1 milestone: state machine on PC, no hardware)

Built 2026-10-15. Python 3.12 standard library only (tkinter), nothing to install.

- `Run Scout.bat` opens the window. Pick a scenario, tick Evening to see the recap, Reset memory to replay event reactions.
- `python scout_sim.py --headless` prints what Scout shows for every scenario.
- `python test_scout_state.py` checks the character rules (7 tests).
- Edit any `mock_data\*.json` while the window is open; Scout re-reads within a second.

| File | Job |
|---|---|
| scout_state.py | The state machine. Pure logic, ports to firmware later. |
| sprites.py | Placeholder 18x14 pixel art (2 moods). Real art: 8 states x 3 frames, not done. |
| scout_sim.py | Stand-in screen. |
| mock_data\ | Five scenarios shaped like the future dashboard\data JSON. |

Rules implemented (SCOUT-CHARACTER-BIBLE.md, CAPABILITIES.md): THRIVING and BURIED moods from the four composite signals;
special event layered on top, never replacing the mood; event reactions fire once per new event; evening recap picks the
single highest-effort thing done today; concern never blame (banned-phrase check on every line).

Not canon, tunable: load weights (overdue 2, blocked 3, calendar over 5 items 0.5 each, decisions over 3 0.5 each),
BURIED at load 5, hold-the-last-mood band between the triggers, recap at 7 PM.

Still open: PAWS-001 (real task source; mock JSON stands in), the dashboard\data JSON write path (does not exist yet),
real art, voice lines.
