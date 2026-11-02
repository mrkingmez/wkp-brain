---
name: show-session-means-resume-command
description: "When Zac says \"show session\" or \"sh session\" he wants the exact command to resume this chat after a restart"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ff5429f8-2c98-4fb1-a9f4-a997facb40e7
  modified: 2026-11-01T17:03:17.707Z
---

"Show session" / "sh session" = give the exact resume command, not session info.

**Why:** Zac restarts Claude Code (new agents/skills load only at restart) and wants to land back in the same chat.

**How to apply:** Reply with two lines: `cd D:\WKP` then `claude --resume <session-id>`. The id is the transcript filename under `C:\Users\kingz\.claude\projects\D--WKP\` (without `.jsonl`). Mention `claude --continue` as the fallback (most recent chat). Warn that session-only timers (CronCreate) die on restart.
