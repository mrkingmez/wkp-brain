# Batch B: skills and learning (notebook list, 2026-11-10)

Read date for every source below: 2026-11-10. Nothing installed, downloaded or run. Stars and dates come from GitHub pages and the GitHub API read today. Where a fact was not retrieved it says NOT AVAILABLE.

## Ranked list (best first)

1. Diagram Design: USE WITH LIMITS
2. Scientific Agent Skills: MAYBE LATER (install a few skills, never the pack)
3. Anthropic Cybersecurity Skills (community pack, NOT from Anthropic): USE WITH LIMITS (read-only study, defensive skills only)
4. AI Engineering from Scratch: MAYBE LATER
5. ecc-universal 2.2.3 (ECC): SKIP
6. Operation Reach (best match Agent-Reach): SKIP

## Matching notes

- "Operation Reach": no project by that name found. Best match is Agent-Reach (github.com/Panniantong/Agent-Reach). Confidence LOW to MEDIUM. Alternative: none strong. A search hit "ReachAgent" is an arXiv paper about mobile GUI agents, not a tool.
- AI Engineering from Scratch: matched rohitg00/ai-engineering-from-scratch. Confidence HIGH.
- Scientific Agent Skills: matched K-Dense-AI/scientific-agent-skills. Confidence HIGH.
- Diagram Design: matched cathrynlavery/diagram-design. Confidence MEDIUM. Alternatives seen in search: coleam00/excalidraw-diagram-skill, SpillwaveSolutions/design-doc-mermaid (not read).
- Anthropic Cyber Security Skills: matched mukul975/Anthropic-Cybersecurity-Skills. Confidence MEDIUM. Its README says it is community made and "Not affiliated with Anthropic PBC". Anthropic's own cyber material (for example its own skills repo or security guidance): NOT AVAILABLE, not searched in this pass.
- ecc-universal: matched npm package ecc-universal, repo github.com/affaan-m/ECC. Confidence HIGH on the name. The version 2.2.3 exists. The "--guided" flag is real: `npx ecc-universal@2.2.3 install --guided` is documented in the README.

---

## 1. Diagram Design (cathrynlavery/diagram-design)

- Source: https://github.com/cathrynlavery/diagram-design and https://api.github.com/repos/cathrynlavery/diagram-design
- What it is: a skill that makes diagrams from a plain request. Output is one self-contained HTML file with inline SVG, exportable to SVG or PNG. README lists 45 diagram types, each in light, dark and full-editorial looks. Can import draw.io, Mermaid, Excalidraw and PlantUML files.
- License: MIT. Stars 66,256. Created 2026-04-16. Last push 2026-11-09 (very active). Contributors: NOT AVAILABLE.
- Cost: free.
- Security: no network use except Google Fonts by default (system fonts avoid it). PNG export needs Playwright and Chromium, which is a pip install plus a browser download, so it adds new software. Scripts are Python (extractors, exporters, validators). Read them before any install.
- Plug-in: Claude Code plugin marketplace route, or copy or symlink the skill folder into the skills folder. Do not use the cross-agent npx route, it writes to places we did not choose.
- WKP fit: the .docx reports have no diagrams today. PNG export at 2x drops straight into a Word doc, and black and white print needs a check. That Word workflow is my inference, the README does not mention Word.
- Verdict: USE WITH LIMITS. It fills a real gap (flow and org charts for guides, KP, Cyber study, pipeline maps).
- First safe test: copy the skill into a scratch folder first, read the scripts, then render ONE diagram (the WWD review pipeline) as SVG with system fonts, check it prints in grayscale. Add Playwright only if SVG will not insert into the docx tool.

## 2. Scientific Agent Skills (K-Dense-AI/scientific-agent-skills)

- Source: https://github.com/k-dense-ai/scientific-agent-skills and API https://api.github.com/repos/K-Dense-AI/scientific-agent-skills
- What it is: 177 skill packs for science work (biology, chemistry, medicine, physics, data analysis) covering databases and Python packages. Version 2.72.0. The 2.72.0 release removed its bundled docx, pdf, pptx and xlsx skills and points users to Anthropic's own skills repository for those.
- License: repo MIT, but each skill may carry its own license in its SKILL.md. Stars 56,701. Last push 2026-11-09. Created 2025-10-19.
- Cost: pack is free. Some skills need API keys or paid services (Exa, Parallel, Benchling, NCBI, Materials Project, OpenRouter, Modal, Fictiv named). Which are paid: NOT AVAILABLE, check each SKILL.md.
- Security: the README itself warns skills can execute code, install packages, make network requests and modify files. It runs LLM security scans but puts review on the user.
- Fit: Shattered Empire medical research (the dextrocardia brief) is human biology and a literature check, which a few skills (PubMed or NCBI style) might help. Most of the 177 are lab science WKP will never use. Loading many skills also bloats context.
- Verdict: MAYBE LATER. Cherry-pick only. Do not install the whole pack.
- First safe test: browse the skill list on GitHub, pick at most two literature-search skills, read their SKILL.md and scripts, ask Zac before copying one in.

## 3. Anthropic Cybersecurity Skills (mukul975/Anthropic-Cybersecurity-Skills)

- Source: https://github.com/mukul975/Anthropic-Cybersecurity-Skills and API https://api.github.com/repos/mukul975/Anthropic-Cybersecurity-Skills
- What it is: a community library of about 817 or 818 cyber skills (the README disagrees with itself) in 29 to 34 domains, mapped to MITRE ATT&CK, NIST CSF 2.0, ATLAS, D3FEND and NIST AI RMF. Domains include SOC operations, threat hunting, forensics, incident response, red teaming (35 skills) and pen testing (23).
- IMPORTANT: despite the name it is NOT an Anthropic product. README says "independent, community-created project" and "Not affiliated with Anthropic PBC."
- License: Apache 2.0. Stars 35,870. Created 2026-02-25. Last push 2026-08-31 (about 10 weeks ago, slower than the others). README shows 14 contributors and a review backlog with pull requests open for months. Latest tagged release v1.0.0 dated 2026-03-11 per the README (a search snippet said v1.3.0, unverified, conflicts).
- Cost: free.
- Security: skills may carry a scripts folder (Python). Includes offensive and dual-use material (C2, phishing simulation, exploitation). Unreviewed contributors. Per the README, no count of how many skills ship scripts.
- Fit: Zac's day job is a defensive analyst role, CySA+ target. The blue-team skills (SOC triage, incident response, threat hunting mapped to ATT&CK) could back Cyber guide drafts and study. Cyber-Security\CLAUDE.md bans writing working attack tooling, so the red-team skills must stay off. It also forbids inventing county-specific facts, which a generic pack cannot supply.
- Verdict: USE WITH LIMITS. Study and reference only, defensive domains only, never aimed at county systems from this PC.
- First safe test: do not install. Read the repo's file list on GitHub for 5 defensive skills (incident response, log analysis), read them as plain text, and judge whether they beat what Claude already knows. Ask Zac before any copy in, and use his day-job IT rules first (he has not answered the outside-product question in the CMMC work, see TASKS).

## 4. AI Engineering from Scratch (rohitg00/ai-engineering-from-scratch)

- Source: https://github.com/rohitg00/ai-engineering-from-scratch and API https://api.github.com/repos/rohitg00/ai-engineering-from-scratch
- What it is: a free course, 542 lessons in 20 phases (math, ML, transformers, LLMs, agents, MCP). Python, TypeScript, Rust, Julia, Go. Includes teaching skills (placement quiz writes LEARNING.md, learn-mcp, learn-agent-skills and others).
- License: MIT. Stars 78,229. Created 2026-03-18. Last push 2026-11-10 (today). Cost: free, but labs may need model API usage or GPU time (not itemized by the README). It takes sponsorships.
- Security: `npx skills add` runs a third-party installer and writes to the skills folder, plus writes learning files into the working folder. README does not mention hooks.
- Fit: general AI engineering learning is not WKP's work. Closest uses are MCP and agent skills lessons for the Software division and PAWS firmware thinking. Zac is time-fragmented, has a CySA+ goal and ADHD, and this is a 542-lesson rabbit hole.
- Verdict: MAYBE LATER. Not a business tool. If Zac wants to learn, read the MCP and agent-skills lessons on GitHub in a browser, no install.
- First safe test: read one MCP lesson on the web page, no install.

## 5. ecc-universal 2.2.3 (the ECC harness, affaan-m/ECC)

- Sources: https://github.com/affaan-m/ECC, https://api.github.com/repos/affaan-m/ECC, https://registry.npmjs.org/ecc-universal and https://registry.npmjs.org/ecc-universal/2.2.3. The npmjs.com package page itself returned HTTP 403, so the facts come from the registry JSON.
- What it is: a toolkit that bundles, per the README, 71 agents, 314 skills, 98 command shims, hooks, rules, memory, "continuous learning" and a security scanner (AgentShield) for Claude Code, Codex, Cursor and others. It also sells ECC Pro (hosted GitHub App) and takes sponsors.
- Publisher: author Affaan Mustafa, one npm maintainer account "cogsec". Package first published 2026-02-11, 13 versions. Version 2.2.3 published 2026-10-02 01:56 UTC, the latest. Registry shows two signatures and a SLSA provenance attestation link (I did not fetch or verify the attestation). 2,805 files, 19.5 MB unpacked.
- License MIT. Repo stars about 300,573, created 2026-01-18, last push 2026-11-09, 248 open issues.
- Install scripts: package.json has NO preinstall, install, postinstall or prepare. So merely downloading it does not run code by itself. The danger is the command you then run: `npx ecc-universal@2.2.3 install --guided` or `setup` executes its 6 bin scripts (ecc, ecc-install, ecc-memory-mcp, ecc-plan-canvas, ecc-control-pane).
- What the install changes (README, not tested): inventories your existing Claude scopes then installs the plugin `ecc@ecc`. The manual path copies skills to `~/.claude/skills/`, rules to `~/.claude/rules/ecc/`, copies hook scripts under `~/.claude/` and registers hooks in `~/.claude/settings.json`. Hooks need an explicit `--enable-hooks` or `--no-hooks` choice. `--dry-run` previews. Guided mode asks a final confirmation. Plugin installs do not auto-enable its bundled MCP servers. Uninstall: remove the plugin, then `node scripts/ecc.js uninstall --dry-run`.
- Supply-chain risk, stated plainly:
  - One person's account controls the package, and the repo moves fast (4,327 commits). A future bad version would arrive through the same pipe.
  - Unofficial re-uploads exist and the README warns they "may contain malware". A typo in the package name is a real danger. A third-party review site also mentions this.
  - The package has a "welcome" message with a compute sponsor link and mentions an opt-in `ecc ito find` that submits a live authenticated RFQ (a request-for-quote to an outside service). It is opt-in, but it shows outside commerce wired into the tool.
  - `/astra-review` sends your diff to OpenAI when invoked (README).
  - Its hooks are real executable config running on every session. WKP already has its own hooks, agents, skills and rules. README itself says stacking install paths duplicates hooks and skills, and issues #29, #52 and #103 track duplicate hook errors.
  - The README admits "a version pin is not a security audit" and that no audited pin of AgentShield is supplied.
  - Windows: README lists no Windows defects but only shows PowerShell commands and says native Windows has known open defects for some optional features (found in the first read). Zac's PC freezes were already traced to bad tool installs, so a heavy toolkit is a stability risk.
  - Size: 314 skills and 71 agents would collide with the department structure WKP locked and bloat context.
- Verdict: SKIP. The earlier review already skipped "Claude Code Setup" repos for the same reason (they collide with the custom agents and rules). This is the same case, larger.
- First safe test if Zac insists: do NOT run it on the main PC. Read the repo's `hooks/` folder and `scripts/ecc.js` on GitHub, run nothing, and cherry-pick one skill file as plain text, as the earlier review recommended.

## 6. Operation Reach (best match Agent-Reach, Panniantong/Agent-Reach)

- Source: https://github.com/Panniantong/Agent-Reach and API https://api.github.com/repos/Panniantong/Agent-Reach
- What it is: a CLI that gives agents read and search access to X, Reddit, YouTube, GitHub, Bilibili and others with no paid API. License MIT. Stars 110,830. Created 2026-02-24. Last push 2026-11-08.
- Cost: free, but speech-to-text needs a Groq or OpenAI key (price NOT AVAILABLE).
- Security: the install is "give your agent this URL and let it install", which makes the agent run an install guide from the web. It installs uv and several upstream tools into `~/.agent-reach/`, and for login-gated sites it COPIES cookies from your Chrome profile into a background browser. README says the copied login is usually your main account and recommends a burner. WKP's Chrome holds Zac's logged-in Facebook and Google sessions.
- Fit: overlaps browser-use (already researched), the existing Chrome automation and yt-dlp. Little new for WKP.
- Verdict: SKIP. If match is wrong (Zac meant a different "Operation Reach"), ask him what it was about.
- First safe test: none recommended.

---

## Open questions for Zac

1. What was "Operation Reach" about (course, tool, topic)? The match is a guess.
2. Does he want diagrams in the docx deliverables? If yes, item 1 is the only one to try first.
3. Is the Diagram Design Playwright and Chromium add-on acceptable, or SVG only?
4. Cyber pack: day-job IT rules on outside tools are unanswered, so keep it read-only on web pages.

## Sources (all read 2026-11-10)

- https://github.com/affaan-m/ECC
- https://registry.npmjs.org/ecc-universal
- https://registry.npmjs.org/ecc-universal/2.2.3
- https://www.promptquorum.com/ja/power-local-llm/ecc-review (third-party, via search snippet only, not opened)
- https://github.com/mukul975/Anthropic-Cybersecurity-Skills
- https://github.com/k-dense-ai/scientific-agent-skills
- https://github.com/cathrynlavery/diagram-design
- https://github.com/rohitg00/ai-engineering-from-scratch
- https://github.com/Panniantong/Agent-Reach
- GitHub API repo endpoints for each of the above (dates, stars, licenses)
- Earlier review reused for the "other people's whole setups" verdict: D:\WKP\reports\github-tools\GitHub-Tools-Review-2026-10-30.md

Not retrieved: npmjs.com ecc-universal page (HTTP 403), npm download counts, the SLSA attestation contents, last commit dates inside README pages, Anthropic's own cyber material.
