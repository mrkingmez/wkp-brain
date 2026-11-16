# Teacher fact pack: Claude power tools (Projects, Skills, connectors and MCP)

Retrieved 2026-11-14 by fact-research. Method: WebFetch and WebSearch only, no logins. Anthropic help pages show only "Updated X ago" and no calendar date, so every "page's own date" below is that relative stamp as seen on 2026-11-14. Treat everything as fresh as of the retrieval date and reverify before it ships, because Anthropic changes these pages often. The fetch tool summarizes pages, so wording is the tool's reading of the page. Paraphrased throughout.

Notes the writers must read first
- Naming drift. The pricing and help pages now use "Customize" in the app menu (older guides say Settings > Capabilities). Pages say Cowork is "now just Claude" in places (item 6). Menu names may differ on her screen.
- The pricing page text contains items I could not explain from other pages ("Fable" usage credits, Claude Data, Claude Science, Design, Slides). I report them as the page showed them and do not describe them.
- Several conflicts between Anthropic pages are listed in the Conflicts section at the end.

---

## 1. Paid plans for individuals

Question: names, monthly prices, what each adds over Free, and which plan unlocks which feature.

Answer (from claude.com/pricing)
- Free. No price.
- Pro. 20 US dollars a month billed monthly, or 17 dollars a month if billed yearly (200 dollars up front). Adds more usage than Free in both the 5 hour window and the weekly window, more models (Opus included), Claude Code, Projects, Claude in Chrome and Microsoft 365, scheduled and handed-off tasks.
- Max. 100 dollars a month, no yearly price shown. About 5 times Pro usage, priority access at busy times, early access to advanced features, and 100 dollars a month of API credits for the developer platform.
- Ultra. 200 dollars a month, no yearly price shown. About 10 times Pro weekly usage, no 5 hour limit for verified accounts, 200 dollars a month of API credits.
- The Pro help article (support.claude.com) agrees on 20 dollars and says Pro adds more usage per session, priority access at busy times, early access to new features, and Claude Code. It says Pro does not include API usage. It says there are no standard discounts for individual plans.
- Team and Enterprise are separate organization plans. Claude Code page lists Team at 20 dollars per seat per month billed yearly (teams of 2 to 150). Not individual, not needed for her.

Feature by plan (as the pages say it)
| Feature | Where it is available | Source |
|---|---|---|
| Projects | All plans including Free (Free capped at 5 projects). Paid plans get RAG, which expands knowledge capacity up to 10 times when a project nears its limit. | Projects help article |
| Skills | Free, Pro, Max, Ultra, Team, Enterprise, but code execution and file creation must be on. See conflict note on custom uploads. | Skills help articles |
| Connectors (web) | All users | Connectors help article |
| Custom connectors (remote MCP) | Free (limit of one), Pro, Max, Ultra, Team, Enterprise | Connectors help article |
| Research | Paid plans only (Pro, Max, Ultra, Team, Enterprise). Needs web search on. Pricing page lists it under Free, which conflicts. | Research help article, pricing page |
| File creation | Pricing page lists it under what Free includes. Help article says Free, Pro, Max, Ultra turn on "Code execution and file creation" in settings. | Pricing, Skills use article |
| Memory | On by default on Free, Pro, Max, Ultra. | Memory help article |
| Claude Code | Pro, Max, Ultra (also Team, Enterprise, Console accounts) | Claude Code help article, product page |
| Cowork | Paid only: Pro, Max, Ultra, Team, Enterprise | Cowork help article |

Primary URLs
- https://claude.com/pricing
- https://support.claude.com/en/articles/8325606-what-is-the-pro-plan
- https://support.claude.com/en/articles/9517075-what-are-projects
- https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context
- https://support.claude.com/en/articles/11088861-using-research-on-claude
- https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan
- https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork

Date retrieved: 2026-11-14. Page's own date: pricing page none shown (tool noted the visible text was truncated). Pro article "Updated over 2 weeks ago".
Confidence: high on Pro 20 dollars and the Pro feature list. Medium on Max and Ultra (pricing page only, one page). Medium on the feature table because pages disagree in places.

---

## 2. Projects

Question: what they are, how a non-developer creates one, what goes in knowledge and instructions, limits.

Answer
- A project is a self-contained workspace with its own chat history and its own knowledge base. You upload documents, text or code as background, and every chat in the project can use them.
- Create one: left sidebar, click Projects (or go to claude.ai/projects), click "+ New Project" top right, enter a name and description (Claude cannot see the name and description), and save. Team and Enterprise add visibility and tag steps, which do not apply to her.
- Add knowledge: on the right side of the project page, click "+" and upload files or text.
- Add instructions: click "Set project instructions", type how Claude should behave in this project, click "Save instructions". They apply to every chat in the project.
- Limits stated: Free is capped at five projects. On paid plans, when knowledge nears the context limit, Claude turns on RAG automatically and capacity grows by up to 10 times. Context does not carry between chats unless it is in project knowledge.
- Usage tip stated on the usage limits page (item 8): project content is cached and counts less against limits when reused, but the cache expires after inactivity.
- A newer version of projects is rolling out in stages to Pro, Max and Ultra as a beta, starting in Claude Code, where a project is one conversation with parallel threads. The page does not say when it reaches the regular app. Her screen may differ.

Primary URLs
- https://support.claude.com/en/articles/9517075-what-are-projects
- https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects

Date retrieved: 2026-11-14. Page's own date: "Updated over 2 weeks ago" and "Updated over a week ago".
Confidence: high on creation steps, medium on exact button wording (read through a summarizing tool). No numeric file-size limit was stated on the pages I read: not available.

---

## 3. Skills

Question: what a skill is, how to turn it on, use built-in ones, upload or create one, file format, where managed, plans.

Answer
- In Anthropic's words (Help Center): folders of instructions, scripts and resources that Claude loads dynamically, and only the relevant ones for a task. In the developer docs: modular capabilities that package instructions, metadata and optional resources that Claude uses automatically when relevant.
- Anthropic contrasts skills with prompts. Prompts are one-off instructions for a conversation. Skills load on demand so you do not repeat the guidance.
- Turn on (Free, Pro, Max, Ultra): Settings > Capabilities, enable Code execution and file creation (the page says the toggle is called "Create and edit files" in the updated layout). Then Customize > Skills and toggle individual skills on or off.
- Built-in skills: Anthropic provides ones for Excel, Word, PowerPoint and PDF. Claude uses them automatically when a request needs one, for example asking for a presentation. No manual invoking.
- Upload a custom skill: build the skill folder, zip it, go to Customize > Skills, click "+", then "+ Create skill", choose "Upload a skill", upload the zip, toggle it on. Upload fails if the zip is too big, the folder name does not match the skill name, the SKILL.md file is missing, or the name or description has invalid characters. The zip must contain the folder as its root.
- Browse: Customize > Skills, "+", "Browse skills".
- Delete or download: open the skill, use the three-dot menu by the toggle.
- File format at a high level: each skill is a folder with a SKILL.md file. The file starts with a short header (YAML frontmatter) holding a name and a description, then Markdown instructions below. Optional extra files (for example a REFERENCE.md) and scripts can sit beside it. Claude reads the description to decide when to use the skill. Developer docs say name is up to 64 characters, lowercase letters, numbers and hyphens, and the words "anthropic" and "claude" are reserved.
- Recording a skill (screen record) exists only in Cowork in Claude for Mac on Pro, Max, Ultra and Team. Not on Windows. Relevant if she uses Windows: not available to her.
- Custom skills do not sync across surfaces. A skill uploaded in claude.ai is not in the API or in Claude Code, and the reverse.
- Anthropic also has a help article "Teach Claude your way of working using Skills" (https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills). Linked from the developer docs, I did not open it. Unverified content.

Primary URLs
- https://support.claude.com/en/articles/12512176-what-are-skills
- https://support.claude.com/en/articles/12512180-use-skills-in-claude
- https://support.claude.com/en/articles/12512198-how-to-create-custom-skills
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

Date retrieved: 2026-11-14. Page's own date: "Updated this week" (use), "Updated over 2 weeks ago" (what, create). Developer docs page shows no date.
Confidence: high on definition and structure, medium on which plans can upload (conflict, see end).

---

## 4. Connectors and MCP

Question: what MCP is, what connectors are, how to add one, which plans allow custom ones, how permissions work.

Answer
- MCP (Model Context Protocol), from modelcontextprotocol.io: an open-source standard for connecting AI applications to external systems such as local files, databases, search tools and workflows. The site's own comparison is a USB-C port for AI applications.
- Connectors (Help Center): they let Claude reach your apps, retrieve your data and take actions in connected services. Claude inherits your permissions in that service, so it cannot reach anything you cannot.
- Add one from a chat: click "+" lower left (or type "/"), hover Connectors, choose "Manage connectors", click "+" next to Connectors.
- Add one from settings: Customize > Connectors, click "+" next to Connectors, browse by category or full list.
- Then click the connector, read its description, click "Connect" or "Install", follow the sign-in prompts, set any permissions.
- Use one in a chat: "+" menu, hover Connectors, toggle on the services you want. The "Search and tools" menu can disable individual tools.
- Web connectors are available to all users. Custom connectors (a remote MCP server URL you supply) are on Free (limit one), Pro, Max, Ultra, Team, Enterprise. Steps: Customize > Connectors > Add, hover Custom, pick Web, enter a name and the server URL, choose a sign-in option ("Sign in now", "Sign in when needed", "No sign in"), click Add. The server must be reachable on the public internet.
- Approvals: Claude asks before using a connector tool. The page on remote MCP says review those requests and click "Allow always" only for servers and tools you trust. In Research mode Claude can use connector tools without further approval, so turn off write-action tools. The "Always allow / Needs approval / Blocked" per-tool setting is described as an admin control for Team and Enterprise owners, not for individuals.
- Mobile connector installation is in beta.

Primary URLs
- https://modelcontextprotocol.io/docs/getting-started/intro
- https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
- https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp

Date retrieved: 2026-11-14. Page's own date: "Updated over a week ago" (connectors), "Updated today" (remote MCP). MCP site shows no date, its links reference a "2026-07-28" spec version.
Confidence: high on definitions and steps, medium on button wording.

---

## 5. Safety of connectors and skills

Question: Anthropic's guidance on trust, prompt injection, scopes, removal.

Answer
- Connectors, trust: only connect services you trust and need. Custom connectors are not verified by Anthropic. Connect only to servers built and hosted by organizations you trust, and watch for unexpected changes in tool behavior.
- Prompt injection: the remote MCP page says malicious servers can carry hidden instructions meant to make Claude do unintended things. It says Claude has built-in protections but you should still watch tool inputs and outputs. The Cowork page warns that agentic work with internet access has unique risks and assesses trust in any MCP or website before extending access.
- Scopes: during sign-in, read what the server asks for, limit scopes when possible, and refuse if the request seems unnecessary. Sync is limited to content you can already view in the source. Data is encrypted in transit. Third-party services handle your data under their own terms, possibly outside the US.
- Remove: Customize > Connectors shows everything connected. Disconnect there, change settings or review permissions. The page recommends disconnecting services you no longer use. You can also revoke in the third-party service's own security settings.
- Skills, trust: install skills only from trusted sources. Developer docs say use skills you made yourself or got from Anthropic, treat a skill like installing software, and audit every bundled file (SKILL.md, scripts, images) for odd network calls or file access. A skill that fetches outside content is riskier because the fetched text could hold malicious instructions. Main risks named: prompt injection and data exfiltration. Enterprise scanning exists only on Enterprise plans, so she would not have it.
- Remove a skill: Customize > Skills, open the skill, three-dot menu, Delete. Or toggle it off.
- Memory control (related privacy item): Settings > Your Claude, "Generate memory from chats" toggle, with Pause or Reset memory (reset permanently deletes all memories including project memories).

Primary URLs
- https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp
- https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities
- https://support.claude.com/en/articles/12512180-use-skills-in-claude
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork
- https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context

Date retrieved: 2026-11-14. Page's own dates are the relative stamps above.
Confidence: high.

---

## 6. Claude Code and Cowork

Claude Code. Anthropic's AI coding agent. It runs from the desktop app, a terminal, an IDE, Slack or the web. You hand it tasks like bug fixes, tests and refactors and set its permissions and review its work. Aimed at developers and engineering teams. Access comes with Pro, Max or Ultra (one login shared with the Claude apps), with Team or Enterprise, or with a Console account billed at API rates. Usage counts against the same limits as regular Claude chat. If an ANTHROPIC_API_KEY variable is set on the computer it is used instead of the subscription and bills API charges. For a non-developer course this is optional and not recommended as a starting point (writer's call).
URLs https://claude.com/product/claude-code and https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan. Retrieved 2026-11-14. Page date: "Updated over 2 weeks ago" (help), none (product). Confidence high.

Cowork. Anthropic's agent for knowledge work, from the official help article. It brings Claude Code's agentic abilities to knowledge work without a terminal. You describe an outcome and Claude plans and carries out multi-step tasks such as organizing files, producing spreadsheets and presentations, and synthesizing research. Sessions run in an isolated environment on Anthropic's servers and are saved to the account. Paid plans only (Pro, Max, Ultra, Team, Enterprise). Claude Desktop on macOS, Windows and Linux (Linux in beta) is needed for local file, browser and computer access. It can read and write only folders you connect, asks explicit permission before permanently deleting files, and has three permission modes (Manual, Auto, Skip). Deleted tasks leave history immediately and backend storage within 30 days. The article advises staying close to tasks with real consequences such as money or messages sent for you.
Status caution: a search summary (unverified, search tool text) says some support pages now say "Claude Cowork is now just Claude" and that Cowork and chat share one interface. I did not confirm this on a page I opened. The name and menu may differ on her screen. Desktop page to check: https://claude.com/product/cowork (appeared in search, not opened).
URL https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork. Retrieved 2026-11-14. Page date "Updated over 2 weeks ago". Confidence medium to high.

---

## 7. Official learning resources

Answer
- Anthropic Academy, https://academy.claude.com/ (anthropic.com/learn redirects there, HTTP 308). Described on its page as "Free courses on Claude and AI, from Anthropic." Three courses listed, no dates shown on the page (only a 2026 copyright footer):
  - AI Fluency: Framework and foundations, 14 lessons, 1 quiz, about 4 hours. Path /courses/ai-fluency-framework-foundations
  - AI capabilities and limitations, 13 lessons, 1 quiz, about 3.5 hours. Path /courses/ai-capabilities-and-limitations
  - Building effective human-agent teams (beta), 5 lessons, 1 quiz, 45 minutes. Path /courses/building-effective-human-agent-teams
  Full URLs are the academy domain plus those paths (the page gave paths only). Whether a signup is needed to take a course: not available, not checked (no signups allowed).
- Claude Help Center, https://support.claude.com (the pages cited in this pack). Dates are relative only.
- Developer docs, https://platform.claude.com/docs/en/intro (docs.claude.com redirects to it, HTTP 302). I did not open it. Aimed at developers. Agent Skills overview was opened (item 3).
- Claude Code docs, https://code.claude.com/docs/en/overview (linked from the skills docs, not opened).
- Anthropic engineering post on skills, https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills (linked from the docs, not opened, no date).
- Anthropic YouTube channel. Tried https://www.youtube.com/@anthropic-ai. The page returned only the channel title "Anthropic", with no description, video titles or dates. Not available. Zac or the writer should confirm the exact channel URL by hand, and I cannot give video dates.
- Teacher's own file notes an AI Fluency license check is still open (TASKS.md), so link to the course, do not copy its text.

Date retrieved: 2026-11-14. Confidence high for the academy list, not available for YouTube details.

---

## 8. How a person hits usage limits on paid plans

Answer (from Anthropic's usage limit page and the Pro article)
- Paid plans have a five-hour session limit and a weekly limit, shown as progress at Settings > Usage. The weekly reset happens at a fixed time assigned to the account. Ultra has a weekly limit and verified accounts have no five-hour limit.
- The page gives no message counts. Use none in lessons.
- What drains usage faster, per the page: long messages and big attachments, long conversations, tools like Research and web search, model choice and effort level, building artifacts, and multi-step tasks such as running code, creating files or browsing.
- Tips on the page: plan first and combine related questions, be specific, reuse context in the same chat, batch similar tasks, use projects for repeated content (cached content counts less, but the cache expires after inactivity), and watch Settings > Usage.
- Usage in regular Claude and Claude Code counts against the same limits.
- When you hit a limit: turn on usage credits (extra pay as you go, billed separately), upgrade (Pro to Max, Max to Ultra), or wait for the reset. A small, gradually rolling-out "wrap-up" allowance may let a response in progress finish after the five-hour limit.
- Anthropic does not guarantee uninterrupted service.

Primary URLs
- https://support.claude.com/en/articles/9797557-usage-limit-best-practices
- https://support.claude.com/en/articles/8325606-what-is-the-pro-plan
- https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan

Date retrieved: 2026-11-14. Page date "Updated over 2 weeks ago".
Confidence high.

---

## Conflicts between Anthropic pages (writers must not pick silently)
1. Research. Research help page says paid plans only. Pricing page text lists Research under Free. Safest wording for her: "on paid plans". She will be paid anyway.
2. Custom skill upload. Skills help page says Skills are on all plans. Developer docs say uploading custom skills is Pro, Max, Ultra, Team, Enterprise. She is on paid, so both work for her.
3. Skill description length. Help article says 200 characters max. Developer docs say 1,024. Use "keep it short" and do not quote a number.
4. The help article on creating skills shows an example that does not match its own header rule (tool noted it). Do not reuse that example. Use the developer docs format.
5. Cowork naming. See item 6.

## Not available
- Anthropic YouTube channel contents (page returned the title only). URL for Zac to check by hand: https://www.youtube.com/@anthropic-ai
- Calendar dates for any help article (relative stamps only).
- Claude Cowork product page https://claude.com/product/cowork, not opened.
- Academy signup requirement, not checked.
- Max and Ultra yearly prices, none shown.
- Numeric project knowledge size limit, not on pages read.

## Unverified (search-tool summary only)
- That "Claude Cowork is now just Claude" on some support pages, and that Cowork and chat share one interface.

## Questions only Zac can answer
1. Which paid plan will she have (Pro, Max or Ultra)? Pro covers every lesson in this pack.
2. Which computer does she use, Windows or Mac? Skill recording is Mac Cowork only. Cowork local files need the Desktop app.
3. Does she have the Claude Desktop app installed, or does she use the website only?
4. Will she use her own Claude account, or one that sits on a shared family login? Memory and connectors tie to the account.
5. Which accounts may she connect (Gmail, Google Drive, Calendar, Notion)? Zac decides whether the course teaches connecting her real email and files or a practice account.
6. Does the course teach custom connectors and uploaded skills, or only the directory ones and built-in skills? Anthropic itself says only trusted ones.
7. Is Claude Code in scope for her at all? It targets developers.
8. Who pays if she turns on usage credits, and what monthly cap does Zac set? Money is Zac's call.
9. Is a network-level restriction on her computer (home filtering) likely to block connectors? Not checked.
