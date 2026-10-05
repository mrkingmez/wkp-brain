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

## Adobe MCP connection can't batch-process local files [2026-08-24]
The Adobe for Creativity tools (Photoshop/Lightroom image ops) require a
presigned URL or an Adobe-hosted asset — there is no programmatic upload path
for a genuine local file (`L:\...`, `D:\...`). The only route in is
`asset_add_file`, an interactive file picker Zac has to click through once per
file. Adobe's own docs also cap batch jobs around ~20 files regardless. For
"resize/convert N local images" tasks past a handful of files, skip the Adobe
connection entirely and use a local Pillow script instead — see the
wwd-broll-prep skill. Only worth routing through Adobe when Zac specifically
wants Photoshop's cloud tools touching each file and is fine clicking the
picker per image.

## "Content built in a web/Cowork session, never integrated into the repo" is a recurring failure mode, not a one-off [2026-10-03]
Second confirmed instance of the same pattern that cost Kingdom Planners
its Complete Budget System file: a real, genuinely-Zac-authored skill
(`Listing Factory Skill - SKILL.md`, plus a `30-Day AI Productivity Plan.md`
companion) was found sitting as plain files in
`D:\04 New Warrior King Designs\` — never moved into
`D:\WKP\.claude\skills\`, so `etsy-director.md`'s frontmatter reference to
it as `listing-factory-weekly-batch-skill` silently resolved to an
unrelated global Anthropic catalog skill of the same name instead,
carrying wrong facts (different art path, different fulfillment vendor,
different pricing) into at least one real task. First read was wrong — it
looked like generic demo content with a coincidental name collision; the
real explanation was simpler and matches the KP pattern exactly: genuine
user content, built outside the repo, never downloaded/moved in.

**How to apply:** when a referenced skill/file doesn't exist where it's
supposed to, don't stop at "it's generic/fake" as the first explanation —
check whether the real content is sitting somewhere adjacent (the relevant
venture's working folder, Downloads, a web-session export path) before
concluding it was never real. Two for two so far on this exact failure
mode across two different ventures.

## Google Drive MCP connector (plugin_small-business_google-drive) fails auth entirely on this account [2026-09-24]
`search_files`, and presumably every other tool in this connector, returns
`Incompatible auth server: does not support dynamic client registration` on
every call — confirmed on 2+ separate attempts same session, not a transient
blip. This is a different failure mode than the old Drive-API markdown-
corruption issue above; this one means the connector can't even authenticate,
so nothing can be read or searched, not just written. Blocks any task that
needs a Drive-only reference file (e.g. Shattered Empire's Master Character
Annex / Aether Stone Magic System / voice bible, which only live on Drive per
Shattered-Empire/CLAUDE.md's workflow note, not in the repo or on L:\03 My
writing). Don't keep retrying this within one session past 2-3 attempts —
it needs Zac to reconnect/reauthorize the connector, not a different query.

## Higgsfield account is on the free plan, 0 credits by default [2026-08-10]
`balance` came back `{"credits":0,"subscription_plan_type":"free"}`. This blocks
both weekly social-image generation and the FrostCast cold open Warden character
art. Check balance before attempting generation rather than assuming credits are
available — Zac is doing a cost analysis before topping up, so don't spend/trigger
a purchase without asking first.
