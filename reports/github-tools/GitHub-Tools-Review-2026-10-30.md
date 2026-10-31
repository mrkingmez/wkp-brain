# GitHub Tools Review (from Zac's notebook, 2026-10-30)

Zac's call: "if someone built the walls, we just need to decorate the place." 24 items from three notebook pages, checked on GitHub. Nothing installed yet. Every install runs someone else's code, so each one needs Zac's yes, and I read the code before it goes in.

Star counts and licenses come from web listings unless marked "checked", so treat them as close, not exact.

## Bottom line

**Install now (4):** Day Trader Skill, Task Observer, OpenWhispr, Voice Studio.
**Maybe later (4):** Graphify, Strix, Open Higgsfield AI, CAP.
**Bookmark, not install (3):** Free-for-Dev, Public APIs, Awesome MCP Servers.
**Skip (13):** the rest. Either we already have it, it costs money, or it fights our setup.

## Install now

### 1. Day Trader Skill (your "trading skill")
- **Repo:** github.com/Jakeschincariol/day-trader-skill (checked: MIT, about 3.6k stars).
- **What it is:** 11 Claude skills for day trading: chart scans, news, entry and exit timing, and replaying a trade before you risk money. Uses free public data (Yahoo, Nasdaq, SEC). No API key.
- **Fit:** Investing challenge (the $50 account). Investing is DORMANT on the board, but you asked directly.
- **Safety:** it cannot place an order on its own. Paper trading is the default. Orders only happen if you connect a broker, and I never place trades for you anyway. Not financial advice.
- **Install (in Claude Code):**
  1. `/plugin marketplace add Jakeschincariol/day-trader-skill`
  2. `/plugin install day-trader-skill@day-trader-skill`
  3. For the SEC tools, put your name and email in `trader/config.json`.
  4. Do NOT connect a broker. Leave it on paper.

### 2. Task Observer
- **Repo:** rebelytics/one-skill-to-rule-them-all (skill: task-observer).
- **What it is:** watches a session for friction and repeated mistakes, logs them, and suggests fixes to our skills later.
- **Fit:** matches what we do by hand with memory and "double check before missing." Light, one file.
- **Install:** `npx -y skills add rebelytics/one-skill-to-rule-them-all --skill task-observer --agent claude-code`, or copy its SKILL.md into `D:\WKP\.claude\skills\task-observer\` so it lives in git with everything else (recommended).

### 3. OpenWhispr (your "Open Whisper")
- **Repo:** github.com/OpenWhispr/openwhispr.
- **What it is:** a desktop dictation app. Hit a key, talk, and the text lands in whatever box you are typing in. It can run Whisper locally on your GPU, so it's free and private.
- **Fit:** you live on voice-to-text. This works on the desktop the way your phone does.
- **Install:** download the Windows installer from the repo's Releases page and run it. Pick local Whisper in settings. I'd ask your yes before downloading.

### 4. Voice Studio
- **Repo:** github.com/msrbuilds/voice-studio (local web app, no API keys).
- **What it is:** an offline ElevenLabs-style voice tool: six open text-to-speech engines, voice cloning included.
- **Fit:** Den Files narration, What If (faceless channel), RUBY TWO side voices, Kingdom Planners promo voice. Saves ElevenLabs credits. Your GPU can run it.
- **Install:** clone the repo, follow its README (Python plus the models download). About 30 to 60 minutes the first time.
- **Rule:** only clone voices of people who said yes (you, Matt, Gabby).

## Maybe later

| Tool | What it is | Why not now |
|---|---|---|
| Graphify (Graphify-Labs/graphify) | Turns a folder into a searchable map (graph) | Useful for Shattered Empire canon or the repo. But its `graphify claude install` step edits CLAUDE.md and adds a hook. If used, install the package only (`pip install graphifyy`) and skip that step. |
| Strix (usestrix/strix) | AI pentester that proves bugs with working exploits | Fits Cyber Security practice and CySA+. Needs Docker and a paid LLM API key. Only ever aim it at your own systems. |
| Open Higgsfield AI (Anil-matcha/Open-Higgsfield-AI, MIT, checked) | Free studio for image and video models | CORRECTED after checking the README: two modes. Cloud models go through a Muapi.ai key (README does not list prices). Local models in the desktop app run FREE on your GPU (sd.cpp for SD 1.5, SDXL, Z-Image; Wan2GP for video). Local mode makes this worth a test. |
| CAP (cap.so) | Open-source Loom: screen recording with a share link | Handy for Post-Production client walkthroughs or Cyber guides. Not needed today. |

## Bookmark, not install

These are big lists of other tools, not tools themselves. Tell me a job and I'll mine them.
- **Free-for-Dev:** free tiers of services (hosting, email, forms, and more).
- **Public APIs:** free data APIs (movies, sports, finance). Good for WWD and fantasy football ideas.
- **Awesome MCP Servers:** connectors for Claude. The place to look before we build a connector ourselves.

## Skip

| Tool | Why skip |
|---|---|
| OpenSEO (every-app/open-seo) | Free app, but needs a paid DataForSEO key for any data. VidIQ already covers YouTube. Revisit for Etsy keyword work. |
| AppFlowy (Notion alternative) | Our brain is the git repo plus TASKS.md. A second notes app splits it, the same way Drive rotted. |
| OpenProject (project management) | Same reason. TASKS.md is the one list. |
| Cal.com / Cal.diy (booking) | Cal.diy is the free self-host version (MIT, personal use only). No client bookings yet. Revisit for Post-Production clients. |
| Chatwoot (customer inbox) | No customer volume yet. Revisit when Etsy or eBay messages pile up. |
| WeKnora (Tencent knowledge base) | Heavy server setup. Graphify does the same job lighter. |
| Google Artemis (Android phone agent) | Drives your phone by AI. It could post Shorts for you, but posting stays your job, and it has an open credit dispute. |
| OpenTerminal (trading dashboard) | Several small projects share the name. The Day Trader Skill covers this. OpenBB is the stronger free terminal if you ever want one. |
| EasySpider (no-code scraper) | We already scrape with Chrome. Many look-alike repos, no clear original. |
| OmniRoute (AI router) | Routes Claude Code to "free" models through a proxy, with "stealth" features. Risky for the account and for security. |
| Headroom (context compression) | Puts a proxy between you and Claude. Small gain, new failure point. |
| Claude Code Setup (several repos) | Other people's whole setups. Ours is custom. Installing one would collide with the agents and rules we built. I can cherry-pick a single piece if you see one you like. |

## Sources
- https://github.com/Jakeschincariol/day-trader-skill
- https://claudemarketplaces.com/skills/rebelytics/one-skill-to-rule-them-all/task-observer
- https://openwhispr.com/use-cases/windows
- https://github.com/msrbuilds/voice-studio/releases/tag/v0.2.0
- https://github.com/Graphify-Labs/graphify
- https://github.com/usestrix/strix
- https://backiee.wasmer.app/http_github_com/Anil-matcha/Open-Higgsfield-AI
- https://github.com/calcom/cal.diy
- https://github.com/tencent/WeKnora
- https://pasqualepillitteri.it/en/news/25427/google-artemis-open-source-ai-agent-android-en
- https://trendshift.io/repositories/215916
- https://pinggy.io/blog/omniroute_ai_gateway_security/
- https://github.com/BuildOnX/headroom
- https://github.com/Nagi-Inaba/claude-code-setup
- https://github.com/every-app/open-seo
- https://github.com/tsstntsourcecode/EasySpider
