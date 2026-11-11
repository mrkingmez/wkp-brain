# Batch A: agent infrastructure tools from Zac's notebook

Date read: 2026-11-10 (every source below was read on this date, so none is stale). Research only. Nothing installed, downloaded or run.
Method note: pages were read through a fetch tool that summarizes, so descriptions are paraphrase. Repo dates and star counts come from the GitHub API (api.github.com/repos/<owner>/<repo>), read 2026-11-10. API "open issues" counts include pull requests. LICENSE files were not opened, license is from the API or README.
Earlier work reused, not redone: GitHub Tools Review 2026-10-30 (OmniRoute SKIP, Headroom SKIP) and 2026-11-10-browser-use.md (USE WITH LIMITS).

## Ranked list (best first)

| Rank | Item | Matched project | Verdict |
|---|---|---|---|
| 1 | Awesome Harness Engineering | ai-boost/awesome-harness-engineering | USE (as a reading list) |
| 2 | Apify MCP | apify/apify-mcp-server | USE WITH LIMITS |
| 3 | Agent Memory | thedotmack/claude-mem (best guess) | MAYBE LATER |
| 4 | Headroom | chopratejas/headroom | MAYBE LATER (upgraded from the old SKIP) |
| 5 | Claude x Dev skill | SawyerHood/dev-browser or obra/superpowers (guess) | MAYBE LATER (cherry-pick only) |
| 6 | OpenViking | volcengine/OpenViking | SKIP for now |
| 7 | OmniRoute | diegosouzapw/OmniRoute | SKIP (reaffirmed) |

## Fit against WKP's five problems

| Problem | What actually helps from this batch |
|---|---|
| Agents forget between sessions | WKP already has Claude Code's built-in subagent memory (`memory:` field in an agent file, stored at `.claude/agent-memory/<agent>/`, first 200 lines or 25 KB of MEMORY.md loaded at start). Source: https://code.claude.com/docs/en/sub-agents (2026-11-10). The repo already has `.claude/agent-memory/clearance` and `originality`, so some agents use it. Cheapest fix is to turn it on for more agents. claude-mem and OpenViking are bigger add-ons on top. |
| Main session does too much | None of these tools. That is an agent spec and routing problem. |
| Agents cannot browse or see images | Apify MCP (scraping, no login), browser-use (already researched), dev-browser (not on Windows yet). |
| Long runs overflow context | Headroom (compression), or the context practices in the Awesome Harness list. |
| Nothing independently verifies claims | No tool here does it. The Awesome list has an Evals and Verification section worth mining for the QA department design. |

---

## 1. Awesome Harness Engineering

- Matched: ai-boost/awesome-harness-engineering. Confidence MEDIUM-HIGH on the name. Three other lists share a similar name (walkinglabs/awesome-harness-engineering, Picrew/awesome-agent-harness, AutoJunjie/awesome-agent-harness). Source for the alternatives: web search 2026-11-10. Matched ai-boost because the notebook reads "Awesome Harness Engineering" exactly.
- Source: https://github.com/ai-boost/awesome-harness-engineering (read 2026-11-10).
- What it is: a curated list of articles, specs and projects on building agent harnesses. Sections include Context Delivery and Compaction, Skills and MCP, Permissions and Authorization, Memory and State, Task Runners and Orchestration, Verification and CI Integration, Human-in-the-Loop, Security Sandbox and Permissions, Evals and Verification, Templates. The entries I could see were mostly Anthropic and OWASP documents (for example "Effective Context Engineering for AI Agents", "Beyond Permission Prompts", OWASP LLM06 Excessive Agency). Entries under Memory, Orchestration and Evals were not read (page text was cut off). NOT AVAILABLE.
- License: API reports "Other" (NOASSERTION). Not a concern for reading a list.
- Activity: last push 2026-11-10 09:16 UTC, created 2026-03-29, 5,115 stars, not archived.
- Cost and keys: none.
- Security: it is a list of links, runs nothing. The repo contains AGENTS.md and CLAUDE.md files, which only matter if someone clones it into the working directory. Do not clone it inside D:\WKP. Read it on the web.
- Plug-in: none. It is reading material. Specifically useful for the new QA department spec (Evals and Verification section) and for context rules.
- Verdict: USE. Zero risk, and it targets the verification and context problems directly. Caveat that star counts on lists like this are popularity, not quality, and the links inside were not individually vetted.
- First small safe test: open the Evals and Verification and Context sections in a browser, pick 3 articles, and ask a research agent to summarize them into the QA department spec.

## 2. Apify MCP

- Matched: apify/apify-mcp-server. Confidence HIGH.
- Source: https://github.com/apify/apify-mcp-server (read 2026-11-10).
- What it is: official MCP server that lets an agent run "Actors" (ready-made scrapers and automations in the Apify Store) for search engines, maps, social sites, e-commerce, any site.
- License: MIT. Activity: last push 2026-11-10 13:15 UTC, created 2025-01-02, 15,574 stars.
- Cost: connecting is free. Actor runs bill to your Apify account per Actor. Free plan includes $5 of monthly platform usage (per the README). Run caps exist in `call-actor` options (`maxTotalChargeUsd`, `maxItems`). Apify Store Actor prices were NOT checked. Current Apify pricing page NOT checked.
- Auth: hosted `https://mcp.apify.com` uses OAuth in the browser or a bearer API token. Local stdio uses `APIFY_TOKEN`. README says treat the token like a password.
- Data leaving the machine: Actor inputs and results go through Apify's platform. Telemetry on by default (session id, and a model-written one-sentence use case on actor searches). Opt out with `TELEMETRY_ENABLED=false`. Stdio mode uses Sentry for errors.
- Security: full-permission Actors need a one-time approval. Actor tools are marked destructive unless Apify-maintained. Default tool set changes between versions, so pin `tools` explicitly. Advisories: none found, the advisories page was NOT opened.
- Plug-in: `claude mcp add apify "https://mcp.apify.com" -t http` (from the README). Subagents inherit MCP tools unless an agent file limits `tools`, and `mcpServers` in an agent file can scope a server to one agent (sub-agents doc, 2026-11-10). So only the web-ops agent could hold it.
- Verdict: USE WITH LIMITS. It gives agents a way to read the web without Zac's logged-in Chrome, which fits the web-ops agent, and it is more constrained than a free-roaming browser. Limits: no Apify account linked to a card until Zac says so (free $5 only), only the web-ops agent gets it, a per-run cost cap in the agent prompt, explicit tool list, telemetry off, and scraping social sites like Facebook or Instagram stays off the table because of platform terms (not checked, flag for Zac). It does not help with viewing images the way a browser screenshot does. Whether Actors return image files an agent can look at is NOT AVAILABLE.
- First small safe test: free Apify account, no card, hosted server added at project scope for one agent, one run of a public-page Actor with `maxItems` 5, read the result and check the Apify usage page for what it cost.

## 3. Agent Memory (which project?)

- The notebook name is too generic. Candidates found by search, none opened beyond the first:
  1. thedotmack/claude-mem (best guess, because it is built for Claude Code). Confidence LOW-MEDIUM.
  2. mem0ai/mem0 (memory layer, MCP, hosted or self-hosted). Apache-2.0, last push 2026-11-06, 68,750 stars (API). Not read in depth. NOT AVAILABLE: pricing and self-host requirements.
  3. OpenViking (item 6 below), which also calls itself agent memory.
  4. Anthropic's built-in subagent memory (already available, see top table).
- Matched in depth: claude-mem. Source: https://github.com/thedotmack/claude-mem (read 2026-11-10).
- What it is: a plugin that records what the agent does, has an AI model compress it into observations, stores them locally in SQLite at `~/.claude-mem`, and injects relevant context into later sessions. Works with Claude Code, Codex, Cursor and others.
- License: Apache-2.0 (API). Activity: last push 2026-11-10 10:44 UTC, created 2025-08-31, 115,679 stars, 97 open issues. Version badge 15.15.1.
- Needs: Node 20.19+ or 22.12+ (Bun and uv auto-installed). Install is `npx claude-mem install` or the `/plugin` marketplace route. Windows is listed as supported, no Git Bash needed.
- Cost: the observer needs a model. Options after sign-in are the project's own paid observer (30-day trial, payment method required), your own OpenRouter or Gemini key, or "your Anthropic plan". Whether the Anthropic plan route uses subscription OAuth, and whether that collides with Anthropic's rule on third-party tools, is NOT VERIFIED. See item 7 for that rule. Use a skip-sign-in flag or `CLAUDE_MEM_ONLINE_OPTIN=false` per the README.
- Security: hooks fire on nine Claude Code events (SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, PostToolUseFailure, Stop, SubagentStop, SessionEnd, Setup), so every tool call passes through a local worker. Anonymous telemetry is on by default (`npx claude-mem telemetry disable`). Cloud sync is opt-in. `<private>` tags keep text out. The README says nothing on a threat model or audit. Third-party reports of database corruption when sessions are killed are anecdotal, from a single comment (search result, 2026-11-10).
- Plug-in: plugin plus hooks plus a local worker, edits Claude settings.
- Verdict: MAYBE LATER. It targets a real WKP pain, but WKP already has native subagent memory that is not fully used, claude-mem adds hooks on every tool call across all sessions, needs a model for compression (cost or an account question), and is a very large fast-moving project. Try the native route first. If agents still forget after that, trial claude-mem.
- First small safe test (when approved): clone nothing, read the repo's hook scripts first, then in a scratch copy of the repo (not D:\WKP) run the install with `CLAUDE_MEM_ONLINE_OPTIN=false` and telemetry disabled, run two short sessions, and check what the second session was told.
- Cheapest fix now, no install: add `memory: project` to more agent specs and make each agent's MEMORY.md short and curated. Not tested by me.

## 4. Headroom

- Matched: chopratejas/headroom (Python and npm package `headroom-ai`). Confidence MEDIUM. NOTE: the 2026-10-30 review linked github.com/BuildOnX/headroom, which is a different repo. The earlier "puts a proxy between you and Claude, small gain" verdict may have judged a different project or only the proxy mode. Flagged for correction.
- Source: https://github.com/chopratejas/headroom (read 2026-11-10), SECURITY.md same repo.
- What it is: compresses tool outputs, logs, files and chat history before they reach the model. The README claims 21 to 57 percent fewer input tokens on four agent scenarios and over 90 percent on repetitive JSON and logs. Those are the project's own numbers, not independently checked.
- License: Apache-2.0. Activity: last push 2026-11-10 14:44 UTC, created 2026-01-07, 79,291 stars, 276 open issues and PRs.
- Run modes: library (in process), local proxy on port 8787, MCP server (`headroom_compress`, `headroom_retrieve`, `headroom_stats`), Docker. `headroom wrap claude` launches Claude Code through the proxy (reversible with `unwrap`).
- Cost: free. No Headroom key. Still uses your own Anthropic credentials as normal.
- Data: compression is local. Prompts still go to Anthropic as normal. Model downloads come from Hugging Face. Anonymous beacon and daily update check on by default, can be disabled (`HEADROOM_BEACON=off`, `DO_NOT_TRACK=1`, `HEADROOM_UPDATE_CHECK=off`).
- Security (from its own SECURITY.md, reviewed by them 2026-09-10): some credentials stored in plaintext in settings; cached request content kept in an unencrypted local SQLite database (can be disabled); only the latest release gets fixes; two unpatched dependency advisories listed, both in optional extras (CrewAI and ChromaDB, Accelerate in a voice-train extra). Do not expose the proxy beyond loopback.
- Open question: whether the proxy works with Claude Code logged in by subscription, or only with an API key, is NOT AVAILABLE. This matters because of the Anthropic rule in item 7.
- Verdict: MAYBE LATER. Long runs overflowing context is a real WKP problem and the MCP-only mode adds no proxy, which answers the earlier objection. But gains are unproven on WKP's workload (mostly document and transcript text, where claimed savings may be lower), the cache holds sensitive prompt content unencrypted, and Claude Code already compacts. Revisit when overflow is measured.
- First small safe test (when approved): MCP mode only, no `wrap`, telemetry and beacon off, in a throwaway project, compress one 100 KB transcript and compare token counts, check that retrieval returns the original.

## 5. "Claude x Dev skill" (unclear)

- Confidence LOW. Nothing in the name points to one project. Candidates:
  1. SawyerHood/dev-browser, "A Claude Skill to give your agent the ability to use a web browser". MIT, last push 2026-11-03, created 2025-12-02, 6,728 stars, 22 open issues (API, 2026-11-10). Fits "Dev" literally and fits the browse problem. README: https://github.com/SawyerHood/dev-browser (read 2026-11-10). BLOCKER: it says supported platforms are macOS and glibc Linux, "Windows and musl Linux aren't supported yet." Runs scripts via `node:vm`, which the README says is not a security boundary. MCP add line: `claude mcp add dev-browser -- dev-browser mcp --headless`.
  2. obra/superpowers, "An agentic skills framework and software development methodology". MIT, last push 2026-11-03, 315,489 stars (API). A whole workflow framework, so it would collide with WKP's custom agents. Which of its skills (for example any verification step) would be worth cherry-picking was NOT verified. The README was not opened.
  3. anthropics/skills (Anthropic's own skills repo). Not opened. NOT AVAILABLE.
- Alternative reading: a skill from "Jev", a person's name. Nothing found.
- Verdict: MAYBE LATER (cherry-pick only). dev-browser cannot run on Zac's Windows PC today, so SKIP it until Windows support lands (browser-use already covers that need). Superpowers: do not install the whole thing, it would fight the agent system. Zac could say what the notebook line really says.
- First small safe test: none until Zac clarifies. For superpowers, read two or three skill files in the browser and copy ideas into QA specs, no install.

## 6. OpenViking

- Matched: volcengine/OpenViking. Confidence MEDIUM-HIGH ("Open Vikings" in the notebook).
- Source: https://github.com/volcengine/OpenViking (read 2026-11-10).
- What it is: an open source "context database" for agents. Knowledge, memory and skills live in a virtual filesystem under `viking://`, with generated summaries per directory so an agent scans before opening files.
- License: AGPL-3.0 for the main project, Apache-2.0 for the CLI crate and examples, mixed elsewhere. AGPL matters only if WKP modifies it and offers it over a network. Not a blocker for private use, but flagged.
- Activity: last push 2026-11-10 14:49 UTC, created 2026-01-05, 41,941 stars. Open issues plus PRs 1,373 (API). Owned by Volcengine (ByteDance cloud), per the org name. NOTE: that organization link is from the repo path, the ownership claim is my reading, not a quote.
- Needs: Python 3.10+, `uv`, and a model provider for embeddings and a vision-language model (Volcengine, OpenAI, Kimi, GLM, or local Ollama). A hosted Volcengine service exists (first 50 files free per the README).
- Windows: the Claude Code memory plugin installer says macOS or Linux and uses `curl -fsSL https://openviking.ai/install | bash`. A Windows desktop app exists in beta. The server via `uv tool install` may run on Windows, NOT VERIFIED.
- Data: with a cloud provider, content goes to that provider for embeddings. The README does not detail data handling. The installer writes to the home directory and stores an API key in `~/.openviking/ovcli.conf`. The README includes instructions aimed at AI agents to run installers, which is a prompt injection style pattern, so any agent reading it should be told to ignore them.
- Plug-in: hooks and MCP for Claude Code.
- Verdict: SKIP for now. It is a heavy server stack that duplicates what folders, markdown and the native memory already do for a one-person company, the Claude plugin installer is not for Windows, it needs a second model provider, and it is a curl-pipe-bash installer from a very busy repo. Revisit only if the canon and research folders outgrow grep.
- First small safe test (if ever): read the install script as text first, then run the server alone with local Ollama against a scratch folder, no hooks.

## 7. OmniRoute (earlier SKIP, reaffirmed with new facts)

- Matched: diegosouzapw/OmniRoute. Confidence MEDIUM-HIGH. Source: https://github.com/diegosouzapw/OmniRoute (read 2026-11-10, first 100,000 of 157,919 characters only; the rest NOT READ).
- What it is: a local AI gateway on `localhost:20128/v1` that routes requests across hundreds of providers, many free tiers, with fallback and token compression. `omniroute run claude` launches Claude Code through it.
- License MIT. Activity: last push 2026-11-10 14:56 UTC, created 2026-02-13, 86,172 stars (API). Nine months of life, 12,557 commits per the page.
- Concerns found: the README lists "TLS stealth", a 3-level proxy and a transparent MITM decrypt feature with a CA trust-store installer. 12 providers are marked terms-risk "avoid". Affiliate links and a sponsored section appear in the README. A tutorial dated 2026-10-08 (https://pinggy.io/blog/omniroute_ai_gateway_security/) notes a default dashboard password fallback ("CHANGEME") if not set, that the gateway holds every provider key, and that unauthenticated provider pools are on by default (63 of 99 models in its test). It names no CVEs.
- Anthropic rule: Anthropic's documentation, updated 2026-02-19, says subscription (Free, Pro, Max) OAuth tokens cannot be used in third-party tools, and enforcement started earlier in January 2026 (secondary reporting: https://www.theregister.com/2026/02/20/anthropic_clarifies_ban_third_party_claude_access, https://alternativeto.net/news/2026/2/anthropic-officially-bans-using-subscription-authentication-for-third-party-claude-use). I did not read Anthropic's own legal page. NOT VERIFIED from the primary source. This applies to any tool in this batch that reuses Zac's subscription login.
- Verdict: SKIP. WKP's problem is not model cost, it is agent structure. Routing through free third-party pools sends WKP's business content to unknown operators, and the stealth and MITM features plus the Anthropic rule put Zac's Claude account at risk.
- First small safe test: none recommended.

---

## Overall recommendation for the plan

1. Read the Awesome Harness list for the QA department design (free, no risk).
2. Turn on native subagent memory for the agents that matter and keep each MEMORY.md short. This may fix "agents forget" with no install.
3. Web-ops agent: browser-use trial per the earlier report, plus Apify MCP scoped to that one agent, free tier only.
4. Hold Headroom and claude-mem until the simple fixes are measured.
5. Skip OpenViking and OmniRoute.

## Not verified / not available
- LICENSE file texts (taken from API or README).
- Apify pricing page, Apify advisories page, Actor image output.
- Headroom with subscription login versus API key. Earlier review's repo link (BuildOnX/headroom) not examined.
- claude-mem "Anthropic plan" provider mechanism, its SECURITY policy text, its release dates (page showed none).
- OpenViking on Windows server mode, its data handling docs, last 58,000 characters of OmniRoute's README.
- Awesome Harness list entries under Memory, Orchestration, Evals (page cut off).
- obra/superpowers and anthropics/skills contents. mem0 details.
- Anthropic's primary legal text on third-party tools.
- Which project "Agent Memory" and "Claude x Dev skill" really meant. Handwriting match only.

## Questions for Zac
- Can he read the notebook lines "Agent Memory" and "Claude x Dev skill" again, or is there a repo name nearby on the page?
- Is a free Apify account (no card) fine for a test?
