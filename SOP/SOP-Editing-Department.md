# SOP: Editing Department

Created 2026-11-19 (system reset). Boss: **studio-director**. Members: head-editor, assistant-editor, documentary-editor, media-manager.

## Scope (who does what)

| Agent | Owns | WWD role (new 2026-11-19) |
|---|---|---|
| head-editor | Advice: structure, pacing, retention, cut points, sound placement, color grade steps for Premiere and Resolve | Notes on every WWD prep stringout and, on request, on Zac's WWD cut. Never cuts |
| assistant-editor | Rough cuts and Premiere-ready sequence plans for non-WWD video. Point man on studio jobs | **WWD practice and prep job**: assembly plan plus PREP stringout for every review from the run sheet, pictures and clips (SOP-WWD-Review-Workflow step 5) |
| documentary-editor | Assembly plans for What If, Hidden Hinge, AAR Commander, Today in Military History. wkp-channel-director owns the episode list, research and script order and approves the plan before studio-director gates | None |
| media-manager | Where every file lives: media map, P: index, music catalog | Asset list for each WWD prep job; keeps `music-catalog.md` current for music |

## The WWD rule (resolves the old spec conflict)

Old specs said "WWD edits are Zac's" and pointed the editing department away from WWD, so the department sat idle while Zac waited on WWD prep. Ruling 2026-11-19:
- **Zac is still the WWD editor.** Nobody else makes the cut.
- **wwd-director still owns WWD.** It orders the prep job like any bench job.
- The editing department produces a **PRACTICE AND PREP** layer: an assembly plan and a silent stringout that puts every run-sheet picture and clip at its time on black. Zac drops it on V2 above his cut (blend mode Screen so the black drops out) and keeps or deletes pieces. He may ignore it entirely.
- It never replaces Zac's cut, never edits his project file, never changes the run sheet (wwd-run-sheet owns that), never touches source media.
- wwd-* benches keep their jobs (pictures, clips, kit, sound, color, run sheet, rights). The editing department builds on their output, it does not redo it.

## Practice jobs (how the department gets better)

- Every WWD review is a practice rep for assistant-editor and head-editor. The model job is A Knight's Tale (2026-11-19).
- After each rep: head-editor writes top 3 notes; assistant-editor writes one lesson to `memory\agents\assistant-editor.md`; head-editor writes one to `memory\agents\head-editor.md`.
- When Zac's final export lands, head-editor compares the prep stringout to what Zac actually used (frame pulls at each stop time) and writes what Zac kept, moved or cut. That comparison is the training signal. It goes into the lessons files, never to Zac as homework.

## Job flow (non-WWD)

1. studio-director appoints the point man (assistant-editor default, documentary-editor for documentary work).
2. media-manager supplies the asset list with paths and license notes.
3. Point man builds the plan or rough cut (ffmpeg, contain and fit, never crop, free tools).
4. head-editor notes. Clear fixes applied, creative calls listed for Zac with a pick.
5. qa-director media check. studio-director gates. Then Zac.

## Hard limits

No credits or money, no posting, no Adobe settings, never modify or move source media, work on copies in `D:\WKP\scratch\` or the project's prep folder. Nobody can hear audio: say so. No em dashes.

## Logs

`logs\agent-runs.md` row per job, `logs\studio-director.md` for studio jobs only, `logs\wwd-director.md` line when the job was a WWD prep job (studio-director does not log or gate WWD prep jobs), one lesson per agent per job.

## Budgets and priority

- WWD prep: assistant-editor 30 min (parse plus render), head-editor notes 10 min. Over 50 percent: stop, report the partial and what is left.
- When a WWD prep job and a studio job collide, the studio job keeps priority unless Jarvis says otherwise.
- Channel episodes (documentary-editor): creative calls go to **wkp-channel-director** first (it owns the episode list, research and script order, and approves before studio-director gates). Only what it cannot settle goes to Zac.
