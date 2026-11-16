# wkp-system-check README

Plain version: every night at 23:30 this checks the machine (disks, GPU, updates, backups, tasks, tools) and writes a report to D:\WKP\logs\system-check\. Since 2026-11-12 it can also tidy four harmless things.

## Run it
1. Open a terminal.
2. Dry run (shows what it would tidy, deletes nothing):
   `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe D:\WKP\.claude\skills\wkp-system-check\scripts\system_check.py --no-updates --fixes-dry-run`
3. Open D:\WKP\logs\system-check\<today>.md and read section 13 (what it would do) and section 14 (proposals).
4. Read the itemized log it names (logs\system-checkixes-items-<date>-<time>-dry.tsv): every file, its size and age, and every file it PROTECTED.
5. Live, scratch only, SAME DAY: same command with `--fixes-live --fixes-only scratch` instead of `--fixes-dry-run`. It refuses unless today's dry-run log exists with the same action list and the planned deletions match it exactly. Use the same `--fixes-only` list for both runs.

## The four tidy actions
Scratch files older than 14 days. User TEMP files older than 7 days (locked files skipped). __pycache__ in D:\WKP. System-check reports older than 90 days moved to an archive folder (not deleted).

## Protect list (scratch only, added 2026-11-13)
Never deleted from scratch: anything under scratch\ian\; any folder or file whose name contains photo, restore, client, ian, dk or salaries; and any folder holding a file named `.keep` or `.protect` (the whole folder and everything below it). To protect a folder yourself, drop an empty file named `.keep` in it. The list is in machines.json under safe_fixes, protect. Your edits are added to the built-in list, they cannot remove it. The words are broad on purpose (a false protect costs disk space, a false delete costs client work).

## Item logs
Every run, dry or live, writes logs\system-checkixes-items-YYYYMMDD-HHMMSS-dry (or live).tsv: action, status (would-delete, deleted, would-move, PROTECTED, SKIPPED-LOCKED), full path, size in bytes, age in days. Files are created new each time, so a later run cannot overwrite one.

## Safety
- Live gate: a live run refuses to start without today's matching dry-run log. Files not in that log are never deleted. Nightly live mode therefore needs a dry-run step earlier the same day (not wired, mode stays dry-run).
- Off for any machine not listed in machines.json. Starts in dry-run.
- Caps: 3000 files and 5 GB per run, one action at most half.
- Kill switch: create the file D:\WKP\data\system-check-fixes.disabled.
- Never touches Adobe, drive E:, your files outside scratch, security settings, git, env vars or scheduled tasks. Anything else is a proposal with the exact command, never run.

## Turn on nightly live mode
Edit machines.json, in the safe_fixes block change `"mode": "dry-run"` to `"mode": "live"`.

## Limits and risks
- Counts are exact for the files handled. The cap means a big backlog clears over several nights.
- Deleted files skip the Recycle Bin. Anything you want to keep must not live in scratch or TEMP, or must sit in a protected folder. The protect list only guards scratch, not TEMP.
- Cost to run: none.
