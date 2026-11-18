# last30days vet, 2026-11-17

Verdict: CLEAN WITH GUARDRAILS. Installed as a skill by copy. Zac's yes (2026-11-17) covers last30days only.

Pinned commit: a854f3bcb2c4344d7498426d653378510f8b253a (repo mvanhorn/last30days-skill, MIT, skill version 4.3.2). Cloned into D:\WKP\scratch\last30days-vet\clone\repo (untrusted, never run from there).

## What I read
- Repo layout, plugin manifests, .skillignore, SKILL.md front matter and contract, the runtime and setup references (grep and spot reads), env.py, setup_wizard.py, health.py, hosted.py, cookie_extract.py, the URL list of every Python file in scripts (excluding the vendored bird-search X client), and the npm package @mvanhorn/printing-press-library@0.1.27 (tarball fetched with npm pack --ignore-scripts, never installed, never run).
- No hooks directory, no package.json at the repo root. The npm package has no install scripts (scripts: build, test, version only; one dependency, cross-spawn; maintainers tmchow and mvanhorn).
- I did NOT read every line of the roughly 190 files (about 4 MB of Python). The vendored X client (scripts\lib\vendor\bird-search, node) was not read. It only matters if X cookies are enabled, which we keep off.

## Findings
Nothing that sends data out silently, no hooks, no settings edits, no eval or base64-decoded code execution in the default path.

Things Zac should know (all optional or gated, covered by guardrails):
1. First-run setup wizard. Gated, but if run it (a) may read browser cookies after consent and (b) runs `npx -y @mvanhorn/printing-press-library@0.1.27 install digg --cli-only`. The npx package is pinned, but it then runs `go install <module>@<ref>` and compiles a third-party Go program from GitHub (older catalog entries fall back to @latest per the package source). That is remote code. Guardrail: never run setup. I did not run it.
2. Credentials in the environment are used automatically. Preflight showed Zac's GEMINI_API_KEY as present, which would send topic text to Google. Guardrail: unset it before every run.
3. Keyless fallbacks send the query to third parties: wikidata (entity lookup), Hacker News Algolia and Firebase, Reddit, and for the Reddit fallback Brave, DuckDuckGo and Startpage web search, plus arctic-shift (Reddit archive) and r.jina.ai (page reader, fallback fetch). Documented lookups, not exfiltration, but topics are visible to those services.
4. Default save location is Documents\Last30Days and config is under the home .config folder. Redirected with LAST30DAYS_MEMORY_DIR and LAST30DAYS_CONFIG_DIR into scratch.
5. Many optional paid or keyed sources exist (ScrapeCreators, xAI, Perplexity, Brave API, Bright Data, Apify, X API). None active without keys.
6. Under Claude Code the engine refuses to plan itself (LAW 7) and wants the host model to write a --plan. That keeps runs free of any LLM key.

## Installed
D:\WKP\.claude\skills\last30days\ : SKILL.md, scripts, references (183 files, 4.4 MB), plus VERSION.md and README-WKP.md. Left out: assets (14 MB sample media), agents\openai.yaml, plugin manifests, mcp Go server, tests. No settings, hooks or CLAUDE.md edited.

## Tests
Preflight (python -I, safe config dir): ready, browser cookies off, planned writes only under D:\WKP\scratch\last30days, preflight itself wrote nothing. With GEMINI_API_KEY set it listed it as a present credential. With it unset, credentials: none.

Test run "Vision Quest Disney+ reactions" (--quick, free sources, no cookies, --debug): finished in 5.8 s, exit 0. Calls seen in the debug log: wikidata, hn.algolia.com, hacker-news.firebaseio.com, www.reddit.com (HTTP 403 Blocked, so Reddit coverage was 0), search.brave.com (429), html.duckduckgo.com, www.startpage.com. Result: 1 Hacker News item, unrelated to the show (a VR app). The tool itself said evidence is thin.

Files written, all in scratch: config\last-run.json, last-report.json, last-report.lock, reddit-health.json (Reddit skipped for 6 h), out\ raw report md, library db, plus my stdout and stderr logs. Nothing under the user home folder or Documents (checked).

Not tested: the YouTube/yt-dlp, Polymarket and GitHub paths. The plan was trimmed by the engine to reddit and hackernews, so those never ran. No network capture beyond the engine's own debug log.
