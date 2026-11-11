# browser-use: can it give WKP subagents a browser?

Date read: 2026-11-10 (all sources below read that day, fresh). Research only. Nothing installed, downloaded or run.
Method note: pages were read through a fetch tool that summarizes, so quotes are paraphrase. The LICENSE file itself was not opened, only the README statement.

## Verdict
USE WITH LIMITS. See the last section.

## 1. What it is and how it works
- Open source Python library (also a CLI and a TypeScript option) for AI browser agents. The model writes Python in a persistent REPL, which drives Chrome over the DevTools Protocol (CDP). Not Playwright based per the README. Source: https://github.com/browser-use/browser-use (2026-11-10).
- Needs Python 3.11 or newer. Same source.
- Version state: 1.0.0 and 1.0.1 were both published 10 Nov 2026, preceded by release candidates on 9 Nov. Plain `pip install browser-use` still gave 0.13.14 per the release notes. The 1.0 line is brand new and rewritten (the README points to a MIGRATING.md). Source: https://github.com/browser-use/browser-use/releases (2026-11-10).
- What costs money or needs a key:
  - Default model `bu-fast` runs through Browser Use's gateway and needs `BROWSER_USE_API_KEY`. That key pays for the model and the cloud browser. Billed, not free.
  - Cloud browser is $0.02 per browser hour. New signups get $1 credit. Source: README, same URL.
  - Bring your own key instead: OpenAI, Anthropic (`ChatAnthropic`) or Google, billed by that vendor. Ollama local works with a placeholder key.
  - The library itself is free. A local Chrome, Chromium or Edge can be used instead of the cloud browser.
- Cloud pricing detail (pay as you go, $100 top up raises concurrency): https://docs.browser-use.com (2026-11-10). Current rates page browser-use.com/pricing was NOT checked.

## 2. License, safety, maintenance, data leaving the machine
- License: MIT per README (LICENSE file not opened).
- Size and activity: about 120.5k stars, 13.5k forks, 10,980 commits, 184 open issues, 433 open PRs. Eight commits on 10 Nov 2026 alone. Very active. Source: GitHub page and commits page (2026-11-10).
- Advisory: one published, GHSA-x39x-9qw5-ghrf, Critical, 4 May 2025. `allowed_domains` could be bypassed with a decoy domain in the URL username part. Source: https://github.com/browser-use/browser-use/security/advisories (2026-11-10). Whether it is fixed in 1.0 was NOT checked. The 1.0.0 notes say domain rules now apply in every mode.
- Own security warnings in the README:
  - Secret redaction "is not a sandbox", model written code can read values.
  - `Browser('chromium')` and `Browser('chrome', profile=...)` open an unauthenticated debugging port on 127.0.0.1. Other local users could attach to that browser and its logins.
  - Domain limits are "a guard for an aligned model, not a sandbox." Run untrusted tasks in a container or VM.
- Open issues of note (all 2026-11-10 list): #6218 MCP server resets the security profile to allow all when config.json fails to parse (26 Oct). #6119, #6190, #6214, #6233 are requests for pre-action guardrails, meaning none exist yet. No prompt injection issue found.
- Telemetry: the 1.0.0rc5 notes say telemetry is anonymized, can be turned off with `ANONYMIZED_TELEMETRY=false`, and saved telemetry is now sent. Recent commits are about "stats scrub" of typed text. Exactly what is collected NOT VERIFIED.
- Data leaving the machine: with the default setup, the task, page content and screenshots go to Browser Use's gateway. With your own Anthropic key they go to Anthropic. With Ollama, nothing leaves except page traffic.
- Windows 11: no blocking issue found. Open Windows bugs #6367 (cloud download filenames with a colon) and #6280 (doubled carriage returns). 1.0.1 fixed UTF-8 for piped code on Windows. The README notes a Windows exception that open Chrome must be closed for the profile-copy mode.

## 3. MCP server and Claude Code skill
- MCP: yes. `browser-use --cli-mcp` runs the MCP server. Tools are `browser_exec`, `browser_screenshot` and `browser_login`. The older `--mcp` is deprecated and now serves the same tools. 1.0.1 made `--cli-mcp` launch its own Chromium when no browser is available. Source: releases page (2026-11-10).
- Claude Code skill: yes. `browser-use skill install` registers a skill, and the README's CLI quickstart is written as a prompt for coding agents like Claude Code. What the skill contains was NOT AVAILABLE.
- Could a Claude Code subagent call it? Probably, by one of two routes, neither tested:
  1. MCP: add it with `claude mcp add` (command `browser-use --cli-mcp`). A subagent sees MCP tools only if its agent file lists them in `tools` or inherits all tools. Exact config text was not in the README, so the command line is NOT VERIFIED.
  2. Bash: a subagent with Bash can pipe Python to the `browser-use` CLI.
- Caution found: MCP issue #6296 (tab management) and #6278 (client crash on JSON Schema type arrays) are open.

## 4. Images, screenshots, logins
- Screenshots: `browser_screenshot` exists as an MCP tool. How the image reaches the model, and whether it comes back to the calling Claude agent as an image it can judge, is NOT AVAILABLE in what I read. Judging would be done by whatever model the agent uses (bu-fast or your own key), unless the screenshot returns to Claude through MCP. Needs a test.
- Downloading images and the 1.0 `http_get` helper: exists per the 1.0.1 notes, fetches from the local machine.
- Zac's existing logged in Chrome:
  - `Browser('chrome')` drives the Chrome you already have open, with your logins, after you enable `chrome://inspect/#remote-debugging` once.
  - `Browser('chrome', profile='Work')` opens a new Chrome on a temporary copy of that profile.
  - `Browser('chromium', user_data_dir=...)` keeps a separate persistent profile.
  - 1.0.0rc5 stopped it from attaching to any Chrome answering on port 9222. Source: README and releases.
  - Unknown: whether the MCP and CLI route offers the same attach mode as the Python library. NOT VERIFIED.

## 5. Overlap with Claude in Chrome, and what it adds
- I did not read the Claude in Chrome docs this run, so the comparison relies on what the main session already uses (navigate, find, file_upload, screenshot, per CLAUDE.md).
- Overlap: navigate, click, type, screenshot, use Zac's logged in session.
- Possible additions: runs without the main session (any agent can call it by MCP or CLI), a Python REPL so one call can do many steps, cloud or headless browsers with stealth and proxies, structured output, domain allow lists, a local Ollama option with no vendor cost.
- Possible losses: Claude in Chrome is built by Anthropic and tied to the extension in Zac's own browser. browser-use is a third party and 1.0 is one day old.

## 6. Risks for WKP
- Prompt injection: the agent reads untrusted pages and can run model written Python. Domain lists are advertised as not a sandbox, and the one advisory was a bypass of them. No guardrail layer exists yet (open requests). Highest risk if attached to Zac's real logged in Chrome (Facebook, Etsy, eBay, Google).
- Debugging port: unauthenticated on 127.0.0.1 in profile modes, and a Chrome attach exposes every login to anything local.
- Runaway cost: the default setup bills Browser Use credits per model call and browser hour. A loop with no step cap could spend. No spend cap was found in what I read.
- CLAUDE.md rules: "no posting, no spending, no downloads without Zac's yes" are not enforced by the tool. They would have to be enforced by the agent prompt and a read only allow list (allowed_domains, prohibited_domains). Posting, buying and uploading are all possible once logged in.
- Supply chain: three releases in two days, MIT, but a very large and fast moving codebase. Pin an exact version and read the code before any install, as done with Open Generative AI and OpenMontage.
- Past WKP experience (TASKS.md): Open Generative AI was removed for bugginess. Similar caution applies to a day old 1.0.

## Verdict: USE WITH LIMITS
Worth a sandboxed trial, not yet for production. It is real, MIT, huge and very active, and it does ship both an MCP server and a Claude Code skill, so a subagent could drive a browser without the main session. But 1.0 landed today with hot fixes, there is no guardrail layer, the default path sends data and billing to a third party, and the best feature for WKP (using Zac's logged in Chrome) is also the most dangerous one. Limits if Zac says yes: (1) public pages only, a separate empty profile or `chromium` with its own `user_data_dir`, never Zac's real Chrome; (2) your own key or Ollama, not the default Browser Use gateway, and no cloud top up; (3) `allowed_domains` set per task, telemetry off with `ANONYMIZED_TELEMETRY=false`; (4) read only subagents (view pages and images, no login, no posting, no downloads) and a pinned version after one code read; (5) first test screenshot return to a Claude agent before committing. Any logged in work (Facebook, Etsy, eBay, IMDb pulls that need a session) stays with the main session's Claude in Chrome.

## Open questions for Zac
- Is the goal public page and image viewing only, or logged in sites too? That decides everything above.
- Is a first trial on a throwaway profile approved (pip install of a pinned version is not spending, but the model key is)?

## Not verified
LICENSE file text, exact MCP add command, skill contents, how screenshots return to a calling agent, what telemetry collects, whether the May 2025 advisory is fixed in 1.0, current cloud pricing page, Claude in Chrome feature list.
