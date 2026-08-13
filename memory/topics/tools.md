# Tools and Infrastructure

## Google Drive API destroys markdown [2026-08-03]
Drive's `create_file` converts text/plain uploads into Google Docs format unless
`disableConversionToGoogleType` is explicitly set. That flag was never set, which
silently broke every `@`-import in the first Second Brain. Never create
operational files (ME.md, TASKS.md, projects.md, CLAUDE.md, skills) through the
Drive API. Create them locally in the repo, commit, push. Drive is for reference
material only: manuscripts, images, spreadsheets.

## Claude Code install blocked by npm allow-scripts [2026-08-03]
`claude` came back as an unrecognized command after a normal global install
because npm's allow-scripts restriction blocked the postinstall step. Fix:
`npm install -g --allow-scripts=@anthropic-ai/claude-code @anthropic-ai/claude-code`

## Drive shows 1 byte after upload — false negative [2026-07-24]
A file created through the Drive API reports a size of 1 byte immediately after
creation. Reading it back with `read_file_content` confirms the content uploaded
fine. Do not re-upload on the strength of the size display.

## Drive folder search needs parentId chaining [2026-07-24]
Direct folder-path queries are unsupported — chain parentId queries to walk into
a folder. Title keyword searches work regardless of location. There are no
delete, move, or overwrite tools; replacing a file means creating the new one
and handing over direct links to the old ones for manual deletion.

## Claude Code native memory writes outside the repo [2026-08-06]
Claude Code has a built-in memory feature that writes an index (`MEMORY.md`) plus
flat topic files into `C:\Users\kingz\.claude\projects\D--WKP\memory\` — the home
folder, invisible to git, stranded on one machine. It writes these with ordinary
`Write` tool calls, no skill required. Fixed by making that path a directory
junction pointing at `D:\WKP\memory\`, so native writes land in the repo and get
committed. `mklink /J` does not require admin rights.

## claude-memory-skill is a command, not a skill [2026-08-06]
The third-party `claude-memory-skill` repo ships `mem.md` with no YAML
frontmatter — it is a slash command belonging in `.claude/commands/`, not a
skill. Installed into a skills folder it produces a truncated auto-generated
description and never fires. The repo also ships two contradictory versions:
the standalone file treats load/save/recall as automatic, the copy embedded in
`install.sh` treats them as manual `/mem` commands. Its installer is bash-only
and targets the home directory — do not run it on Windows.

## Windows hides dot-folders [2026-08-06]
Folders beginning with a dot (`.claude`) are hidden in File Explorer by default.
Turn on View → Show → Hidden items, or paste the path into the address bar
directly. Explorer also refuses to create a name starting with a dot unless a
trailing dot is added too (`.claude.` becomes `.claude`).

## VidIQ shortform rejects Facebook share links [2026-07]
Use Instagram or YouTube URLs instead. Asking it to "summarize claims, especially
factual and technical claims, list them for fact-checking" produces far better
output than a generic summary request.

## Some skills require Cowork, not chat [2026-07]
`wwd-shorts-clip-factory` and `wwd-video-transcriber` need real local filesystem
and ffmpeg access. They will not run in plain claude.ai chat.

## wwd-weekly-planner's transcript handoffs aren't all installed [2026-08-10]
The skill's "When a transcript arrives" section names four handoff skills
(`wwd-video-upload-package`, `wwd-frostcast-chapters`, `wwd-shorts-clip-factory`,
`wwd-video-transcriber`) but only `wwd-weekly-planner` and `wwd-video-transcriber`
actually exist under `C:\Users\kingz\.claude\skills\` on this machine — confirmed
by listing the folder. Don't assume a referenced handoff skill exists; check the
skills directory (or the `/skills` listing) before invoking one. When one is
missing, say so plainly and do the work directly instead of pretending the
handoff happened — this is what happened with The Last House upload package.

## Higgsfield account is on the free plan, 0 credits by default [2026-08-10]
`balance` came back `{"credits":0,"subscription_plan_type":"free"}`. This blocks
both weekly social-image generation and the FrostCast cold open Warden character
art. Check balance before attempting generation rather than assuming credits are
available — Zac is doing a cost analysis before topping up, so don't spend/trigger
a purchase without asking first.
