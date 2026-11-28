# Drill 1: fantasy-football-director, DFS replay of Week 11 (2026-11-22 early slate)

Scope: DFS only. IRFL untouched. Free, no entry, no spend, no posting.
Pass bar source: copied unchanged from `SOP\leveling\fantasy-football-director.md` Step 3, which was written by chief-of-staff BEFORE this run. The agent added only the "how checked" column below, after reading the files. The agent may not grade itself: grader is qa-director with tracking-director for numbers.

## Task
Replay Week 11 from files only: the Sunday noon build, the file Zac entered, and the final scores. Show that a hand-off built from information available at lock passes the process checks, then compare projected to actual.

## Pass bar (written before the run, in the launch file)
| # | Criterion | CRITICAL | How checked (files) |
|---|---|---|---|
| 1 | Refresh checks done and logged: stats, odds, injuries, starting QBs | CRITICAL | `LOG.md` line 111, noon note, `qbs_confirmed_week11.json`, `build_report.txt`, injuries csv stamps |
| 2 | No chalk player in 3 or more lineups unless justified in writing | CRITICAL | lineup counts per player in each file version, own estimates from `sun\own_est_week11.csv` |
| 3 | Late-swap rule applied at the noon rerun (a QB or availability change gets a rebuild before lock) | | noon note, backups in `sun\` |
| 4 | Lineup file passes the DK template check | | `dk_validate.py` plus an independent slot, salary and distinct check |
| 5 | Drill reports its own projected-versus-actual error with numbers from files | | `scratch\leveling\drill1_score.py` against `ACTUAL_week11_espn.csv` |
| 6 | No entry made and no money spent | CRITICAL | agent actions this session (read only on `D:\Draft Kings`) |
| 7 | Every instruction handed to Zac tagged PROVEN, SOURCED or PROPOSED | | noon note text |

Pass: 6 of 7 with criteria 1, 2 and 6 passing. Process benchmark only. One slate proves little: repeat on 3 slates before Level 3.

## Grader checklist (qa-director, tracking-director)
- Re-run `scratch\leveling\drill1_check.py` and `drill1_score.py` with `python -I` and confirm the numbers in the result file.
- Confirm criterion 1 reading: is "stats refresh" required for a pre-game slate, and was any stats refresh logged.
- Confirm criterion 2: is Pollard (37.9 est) and Pickens (39.2 est) "chalk" under the build's own chalk pool of 21.
- Sign with name and date. No signature means UNGRADED.
