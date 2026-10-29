# Agent network: how directors and departments work together

First locked 2026-10-20 (Zac). **Reorganized 2026-10-29 (Zac).** There are two kinds of desk: shared departments that everyone can use, and venture directors that run one line of work each.
Directors work with each other directly. Jarvis is not a switchboard.

## Shared departments (any director calls them directly)

| Department | Boss | Bench | Call it for |
|---|---|---|---|
| Writing room | script-room | room-writer, copywriting, dialogue-doctor, originality, clearance | **Every written word that is not one of Zac's books**: scripts, descriptions, captions, posts, ads, listings, emails, letters. Books only when fiction-director asks. |
| Marketing | marketing-director | social-media, market-research, video-ugc | What to say, to whom, where and when. Ad planning. How people like us market their work. The writing room writes the words. |
| Graphic design | graphic-design | (none) | Every Firefly prompt and every prompt for the other art tools, thumbnails (not WWD's, which Matt makes), social and listing graphics, cover briefs. |
| Music | music | (none) | Every music request: research, royalty-free finds with licenses, Suno and YouTube music prompts. |
| Fact research | fact-research | (none) | Real-world facts with sources, for books, the WKP channel, Den Files and scripts. |
| Market research | market-research (under marketing) | (none) | Competitors, trends, and how channels and sellers like ours market. Open to all. |
| Tracking | tracking-director | (none) | Every numbers pull and its schedule. Saves to `data\`. |
| Hostile review | devils-advocate | (none) | **Every new idea and every new product, any venture, before it is built.** Every short idea (Shorts, Reels, short films). **WWD: anything that might be off brand** (verdict says whether it is off brand and whether it is still a good idea). Any hostile read before something ships. |

## Venture directors

wwd-director, wkp-channel-director (new 2026-10-29), etsy-director, ebay-director, fiction-director, kdp-director, paws-director, fantasy-football-director.

## Approval and send-backs (locked 2026-10-29)

1. A director orders work from a department.
2. The **department boss approves** it against the standard before it leaves the department.
3. The **ordering director accepts** it or sends it back with a specific reason.
4. Either one may send it back **once**. After the **second send-back** the job stops and goes to Zac with both versions and what is wrong with each. No endless loops.
5. Each boss keeps a short checklist of Zac's standard in its own file. "Not good enough" has to point at a line on that checklist or at a concrete problem.

## Handoff note (put this at the top of every task you send)

- FROM: your agent name
- TO: the agent
- TASK: one or two sentences
- FILES: full paths the receiver needs
- NEED BACK: what you want returned and in what form
- RULES THAT APPLY: book, venture, mode (GENERATE or SCRUB), anything locked

## Talking across departments

Department bosses may bounce ideas back and forth directly. For example, graphic-design and wwd-vfx can work out a Firefly plate together, and music can work with wwd-sound on levels. Keep it to the job at hand.

## Who is called only through their boss

- room-writer, copywriting, originality: through script-room. dialogue-doctor: through script-room, or fiction-director for book edits. clearance and devils-advocate may be called direct.
- social-media, video-ugc: through marketing-director. market-research: any director may call it, with a line to marketing-director.
- wwd-vfx, wwd-color, wwd-run-sheet, wwd-pictures, wwd-clip-scout, wwd-sound, wwd-rights: through wwd-director. Standards page: `WWD\STANDARDS.md`. wwd-vfx may talk to graphic-design directly.
- ebay-researcher: through ebay-director, which sets its schedule.
- shattered-empire-director and military-scifi-director: canon-keeper benches under fiction-director.

## Called by Jarvis only

- venture-scout (new-venture research desk): when Zac asks "what else could we make money on" or wants a saturation check. Read-only. It only proposes. Promoting a venture is Zac's call.

## Limits (these stop loops)

1. Never send a task back to a desk that is waiting on you.
2. No chains longer than three handoffs on one task (director, department, bench). A fourth goes to Jarvis.
3. A desk may decline a handoff with a reason. The caller then goes to Jarvis.
4. Peers do not give each other orders about priority, money, schedule, or what Zac decided. Those go to Jarvis and Zac.
5. Decisions still go to `logs\DECISIONS.md`. Nobody answers one for Zac.
6. Review gates still apply (root CLAUDE.md). Scripts: two passes through the writing room. Public copy: written by the writing room, then no-ai-slop. Short ideas: devils-advocate first.
7. Zac's rules travel with the task: no em dashes, never invent lines in his writing, draft only, Zac posts.

## Reporting

- The result goes back to the caller, not to Jarvis.
- The caller puts one line in its own report: who it asked, what came back, and the file path.
- A handoff that fails or can't be reached is reported plainly. Do not fake it, and do not do the other desk's job yourself.
- Anything a subagent can't do (ask Zac a question, use a browser) goes up to Jarvis as a flag.
