# claude-hud vet and install, 2026-11-17

Verdict: CLEAN. Installed (Zac's yes, 2026-11-17).

Pinned commit: 9d2b6fa4df43c8ced61c0c23956fd291551726ac (jarrodwatts/claude-hud, release v0.15.3, MIT, dated 2026-11-10). Vetted in D:\WKP\scratch\claude-hud-vet\clone (untrusted, nothing run from inside it).

## What I read
Plugin manifest and marketplace file, package.json, install.mjs, scripts\statusline.mjs, fence.mjs, dist\index.js (a 3-line re-export of hud.mjs), skills\hud\SKILL.md, and grep sweeps of hud.mjs, collector.mjs and src\*.ts for network calls, process spawning, eval, credential and settings access. The installed cache copy matches the reviewed clone byte for byte (diff, only an .in_use marker added).
NOT read line by line: tests, verify, maintainer, the i18n and render folders, CHANGELOG.

## Findings (plain words)
- No hooks, no postinstall or preinstall scripts. package.json scripts are typecheck and test only. Runtime needs Node 22.18 or newer (this machine has 26.13).
- No network code. No fetch, http, https or net use in the runtime files. The only URLs are github.com links it prints for the git branch and a list of API base URLs it compares against. It does not phone home and has no auto-update.
- It reads: the session stdin Claude Code gives it, the transcript file (to show tools, agents, todos), settings files, git status, and ~/.claude.json only for the plan name (oauthAccount block). Code comments say it never reads .credentials.json. It does not read API keys: the logic process sees ANTHROPIC_API_KEY only as the word "set".
- Safety design: the logic runs in a separate Node process with the permission model, an import allow list, and fetch/WebSocket/net removed (fence.mjs). The authors say that is not proven complete, so treat it as defense in depth, not a wall.
- Spawns: git (status), taskkill on Windows (cleanup), and a node child for the caged logic. `--extra-cmd` runs an arbitrary shell command but only if env CLAUDE_HUD_ALLOW_EXTRA_CMD is set. It is not set and we never use it.
- Writes: small state files under ~/.claude/plugins/claude-hud (heartbeat, data, stripped copy of src), a daily cost ledger and speed/transcript cursors with mode 0600. `hud install` writes settings.json (atomic, backs it up first, refuses to replace another status line without --replace).
- Residual risk: it is third-party code that runs on every status line refresh as Zac, and the statusLine command runs outside the cage (only the logic is caged). Reviewed commit is pinned, so a later upstream change cannot reach this machine unless we re-pin.

## What was installed
1. `claude plugin marketplace add "jarrodwatts/claude-hud#9d2b6fa4df43c8ced61c0c23956fd291551726ac"` (pinned to the reviewed commit, verified in `claude plugin marketplace list`: GitHub jarrodwatts/claude-hud@9d2b6fa...).
2. `claude plugin install claude-hud@claude-hud` (scope user). `claude plugin list` shows claude-hud@claude-hud 0.15.3, enabled.
3. `node <plugin cache>\hud.mjs install --shell gitbash` (the same script the /hud setup step runs; I used it instead of the slash command). It copied statusline.mjs and statusline.cmd into C:\Users\kingz\.claude\plugins\claude-hud\ and wrote the statusLine entry. No --extra-cmd. No auto-update setting.
Project settings D:\WKP\.claude\settings.json: unchanged (diffed).

## Exact diff to C:\Users\kingz\.claude\settings.json
Backups: D:\WKP\scratch\settings.user.20261117-185411.bak (mine, taken before any change) and C:\Users\kingz\.claude\settings.json.bak.20261117T235441 (made by the installer). Project backup: D:\WKP\scratch\settings.project.20261117-185411.bak.

Added:
```
"extraKnownMarketplaces": { "claude-hud": { "source": { "source": "github", "repo": "jarrodwatts/claude-hud", "ref": "9d2b6fa4df43c8ced61c0c23956fd291551726ac" } } },
"enabledPlugins": { "claude-hud@claude-hud": true },
"statusLine": { "type": "command", "command": "exec \"${CLAUDE_CONFIG_DIR:-$HOME/.claude}/plugins/claude-hud/statusline.cmd\"" }
```
There was NO statusLine before, so nothing was replaced and nothing needs restoring other than deleting these keys.

## Undo
Fastest: type `/plugin uninstall claude-hud@claude-hud`, then remove the "statusLine" key from C:\Users\kingz\.claude\settings.json (or copy back D:\WKP\scratch\settings.user.20261117-185411.bak). Blank it for one session without editing anything: start Claude Code with CLAUDE_HUD_DISABLE=1.

## What Zac must do
Start a NEW Claude Code session (status line and plugin load at session start). Optional: type `/hud` for its menu (doctor, preview, set options). Nothing else is required.

## Verified
- Plugin list shows it enabled at 0.15.3; marketplace source shows the pinned commit.
- Settings diff read after the change (above).
- Ran the installed statusline.cmd with sample stdin: it printed "[claude-hud] Initializing..." and exited cleanly (first run, builds its cache). That is not a view of a real HUD.

## Not verified
- The live HUD display in a real session (needs a new session). The "Initializing" message on first render is expected but not confirmed to clear on its own.
- Full line-by-line read of tests, verify, i18n and render code. Network absence is by grep and by the cage design, no packet capture.
- Whether Claude Code on this machine runs statusLine through Git Bash (I chose gitbash because it detected one; if no status line shows, rerun with `node "C:\Users\kingz\.claude\plugins\cache\claude-hud\claude-hud\0.15.3\hud.mjs" install --shell powershell`).
