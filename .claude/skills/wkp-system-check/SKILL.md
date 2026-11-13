---
name: wkp-system-check
description: SYSTEM CHECK (read-only checks plus a tiny allowlisted SAFE FIXES tier, dry-run by default) of Zac's machine (and later other machines). Replaces the old nightly rollup as the machine-health check and keeps its director-log rollup. Checks disk space on every drive, the I: errors watch, drive health, GPU/CUDA, RAM, CPU temp, Windows updates, Defender, backups, WKP scheduled tasks, key tool paths, env var names, and repo hygiene. Writes logs\system-check\YYYY-MM-DD.md plus a one-line GREEN/YELLOW/RED status. Trigger on 'system check', 'nightly check', 'is the machine ok', 'machine health'.
---

# WKP System Check

Added 2026-11-12 (Zac): the nightly rollup becomes a full system check of his machine, and soon more machines.

## Run it

    python D:\WKP\.claude\skills\wkp-system-check\scripts\system_check.py

Flags: `--no-updates` (skip the Windows Update search, about a minute), `--stdout` (also print the full report). Interpreter per LOCAL-PATHS.md. Takes about one minute.

Output: `D:\WKP\logs\system-check\YYYY-MM-DD.md` (full report), `D:\WKP\logs\system-check\latest.txt` (one line: `GREEN|YELLOW|RED | machine | date | reasons`). Exit code 0, 1, 2 for GREEN, YELLOW, RED.

## Rules

- The CHECKS are read-only. The only changes allowed are the SAFE FIXES allowlist below. No installs, no setting changes, no repairs (chkdsk, sfc), no task registration, no service changes. Anything that would change the machine goes to Zac as an exact command.
- ADOBE IS OFF LIMITS. The only Adobe contact is an existence check on the Premiere install folder. Adobe scheduled tasks are never queried, listed or touched.
- Env vars are reported PRESENT or MISSING by name. Values are never read into a report.
- Honesty rule: anything the check cannot read (SMART counters and the dirty bit need an elevated shell, CPU temp needs a sensor tool) is reported "not available" with the reason, never guessed.
- A missed or failed scheduled run is not an emergency (Zac, 2026-11-12). Do not alert-engineer.

## Status levels

- RED: something that can lose work or stop the chain now: a drive nearly full (under 5% and under 100 GB free), Defender off with no other active AV, GPU not visible, tracked files with merge-conflict markers, nothing pushed for 7+ days, python or ffmpeg missing.
- YELLOW: needs a look soon: disk under 15% and under 250 GB free, disk-class error events in the last 14 days, pending reboot, critical updates, uncommitted changes over 40, unpushed commits, deliverables not backed up, a nonzero scheduled task result, a retired task still enabled, a missing env var.
- GREEN: none of the above.

## Sections in the report

1 Machine, 2 Disk space (C, D, E, I, L, P), 3 I: errors watch, 4 Drive health (Get-PhysicalDisk, SMART where allowed), 5 GPU/CUDA, RAM, CPU, 6 Windows Update and Defender, 7 Backups (D:\WKP Reports is not in git, git counts, last push), 8 WKP scheduled tasks, 9 Key tools, 10 Env vars, 11 Repo hygiene, 12 Director-log rollup (kept from the old nightly rollup: logs touched in 24 h, open decisions, commits).

## Adding a second machine

1. On the new machine run `hostname`. Add a block under `machines` in `machines.json` with that name in upper case (copy the MAIN DESKTOP block, change drives, tool paths, env names, `local_paths_section`).
2. Add a `## MACHINE: <name>` section to LOCAL-PATHS.md (rebuilt on that machine, never copied, per root CLAUDE.md).
3. Run the check there. An unconfigured machine falls back to `default` and reports YELLOW "No block for <name>".
4. The machine with `"primary": true` writes `YYYY-MM-DD.md` and `latest.txt`. Every other machine writes `YYYY-MM-DD-<NAME>.md` and `latest-<NAME>.txt`, so two machines never overwrite each other.

## Scheduling

Not registered. Exact command is printed at the bottom of every report and needs Zac's yes. Wrapper script: `D:\WKP\scripts\nightly-system-check.bat` (pull, check, old log rollup, commit, push). The old `scripts\nightly.bat` is kept untouched.

## Safe fixes tier (added 2026-11-12, Zac)

Code: `scripts\safe_fixes.py`, called from system_check.py as report section 13 (section 14 lists proposals). Config: the `safe_fixes` block in the machine's entry in `machines.json`. A machine with no block, or `"enabled": false`, or the unconfigured `default`, gets NO fixes.

Allowlist, nothing else exists in the code:
1. `scratch`: delete files older than 14 days under D:\WKP\scratch.
2. `temp`: delete files older than 7 days in %TEMP% (must be under the user profile). Locked files are skipped, never forced. A folder named `claude` is skipped.
3. `pycache`: delete .pyc files in __pycache__ folders under D:\WKP, remove the emptied folders. `.git` is skipped.
4. `logrotate`: MOVE dated reports (YYYY-MM-DD*.md) older than 90 days from logs\system-check\ into logs\system-check\archive\. Moved, never deleted. latest.txt never moves.

Rails: mode `dry-run` (default, deletes nothing) or `live`. Hard cap per run `max_files` 3000 and `max_bytes` 5 GB, shared, and no single action may use more than half. Kill switch: create the file `D:\WKP\data\system-check-fixes.disabled` and no fix runs (delete it to re-enable). Never followed or touched: junctions and symlinks, any path containing adobe, malwarebytes or defender, drive E:, .git. No admin: a permission error is skipped and counted. No git, env var, task, service or registry calls.

Logging: section 13 of the day's report, plus an append-only `logs\system-check\YYYY-MM-DD-fixes.md` so a rerun never erases what a live run did. Counts and bytes are real (what the OS handled); dry-run numbers are labelled "would be freed".

Flags: `--fixes-dry-run` (force list-only), `--fixes-live` (force live, still needs `enabled`), `--fixes-only scratch,temp,pycache,logrotate`.

To go live nightly: in machines.json set `"mode": "live"`. To stop: the kill switch file, or `"enabled": false`.

PROPOSAL ONLY (section 14, exact command, never run): disk cleanup beyond the list, startup items, services, drivers, Windows Update, power plans, registry, antivirus settings, chkdsk, SFC, any install.
HARD NEVER: Adobe, drive E:, user files outside scratch, Defender or Malwarebytes settings, git history, env vars, scheduled tasks, anything needing admin.
