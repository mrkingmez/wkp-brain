---
name: bash-quoting
description: This Bash tool's git-bash environment breaks on trailing backslash-before-quote paths and on inline PowerShell -Command strings with $ variables
metadata:
  type: feedback
---

Two recurring quoting failures in this environment's Bash tool (git-bash on
Windows), both hit repeatedly on 2026-08-31 during the Good Boy (2025) run:

1. A double-quoted Windows path ending in a trailing backslash right before
   the closing quote (`"...\some\path\"`) breaks bash parsing — the `\"` is
   read as an escaped literal quote, not a path separator plus string end,
   producing `unexpected EOF while looking for matching` errors. Fix: never
   end a double-quoted path argument with a trailing backslash; drop it
   (`"...\some\path"` with no trailing `\`).

2. Passing a multi-line PowerShell script inline via
   `powershell -Command "..."` where the script itself uses `$variables`
   gets mangled — bash tries to expand `$i`, `$exists`, `$size`, etc. as its
   own (empty) variables before PowerShell ever sees them, even inside
   double quotes. This silently strips all the `$`-prefixed tokens and
   PowerShell then throws parser errors like "Missing expression after
   unary operator." Fix: never inline a PowerShell script with variables as
   a `-Command` string through this Bash tool. Always write it to a `.ps1`
   file with the Write tool first, then run
   `powershell -NoProfile -ExecutionPolicy Bypass -File "<path>.ps1"`.
   Confirmed reliable both for quick one-liners (`check_lock.ps1`) and a
   longer polling loop (`wait_for_export.ps1`), including as a
   `run_in_background` job.

**Why:** saves re-discovering this mid-task; both failures look like
generic tool flakiness on first hit but are fully deterministic and
avoidable with the fixes above.

**How to apply:** any time a Bash call against this environment needs a
Windows path, drop trailing backslashes before the closing quote. Any time
a task needs more than a trivial one-line PowerShell command (especially
anything with a loop, a variable, or conditional logic), write it to
`D:\WKP\scratch\*.ps1` first and invoke with `-File`, don't inline it.
