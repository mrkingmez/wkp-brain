# wkp-system-check README

Plain version: every night at 23:30 this checks the machine (disks, GPU, updates, backups, tasks, tools) and writes a report to D:\WKP\logs\system-check\. Since 2026-11-12 it can also tidy four harmless things.

## Run it
1. Open a terminal.
2. Dry run (shows what it would tidy, deletes nothing):
   `C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe D:\WKP\.claude\skills\wkp-system-check\scripts\system_check.py --no-updates --fixes-dry-run`
3. Open D:\WKP\logs\system-check\<today>.md and read section 13 (what it would do) and section 14 (proposals).
4. Live, scratch only: same command with `--fixes-live --fixes-only scratch` instead of `--fixes-dry-run`.

## The four tidy actions
Scratch files older than 14 days. User TEMP files older than 7 days (locked files skipped). __pycache__ in D:\WKP. System-check reports older than 90 days moved to an archive folder (not deleted).

## Safety
- Off for any machine not listed in machines.json. Starts in dry-run.
- Caps: 3000 files and 5 GB per run, one action at most half.
- Kill switch: create the file D:\WKP\data\system-check-fixes.disabled.
- Never touches Adobe, drive E:, your files outside scratch, security settings, git, env vars or scheduled tasks. Anything else is a proposal with the exact command, never run.

## Turn on nightly live mode
Edit machines.json, in the safe_fixes block change `"mode": "dry-run"` to `"mode": "live"`.

## Limits and risks
- Counts are exact for the files handled. The cap means a big backlog clears over several nights.
- Deleted files skip the Recycle Bin. Anything you want to keep must not live in scratch or TEMP.
- Cost to run: none.
