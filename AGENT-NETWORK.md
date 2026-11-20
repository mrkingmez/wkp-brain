# Agent network: how directors and departments work together

First locked 2026-10-20 (Zac). **Reorganized 2026-10-29 (Zac).** There are two kinds of desk: shared departments that everyone can use, and venture directors that run one line of work each.
Directors work with each other directly. Jarvis is not a switchboard.

## Shared departments (any director calls them directly)

| Department | Boss | Bench | Call it for |
|---|---|---|---|
| Writing room | script-room | room-writer, copywriting, dialogue-doctor, originality, clearance | **Every written word that is not one of Zac's books**: scripts, descriptions, captions, posts, ads, listings, emails, letters. Books only when fiction-director asks. |
| Marketing | marketing-director | social-media, market-research, video-ugc (UGC ads only, narrowed 2026-11-17) | What to say, to whom, where and when. Ad planning. How people like us market their work. The writing room writes the words. |
| Graphic design | graphic-design | (none) | Every Firefly prompt and every prompt for the other art tools, thumbnails (not WWD's, which Matt makes), social and listing graphics, cover briefs. |
| Music | music | music-researcher (added 2026-11-19) | Every music request: research, royalty-free finds with licenses, Suno and YouTube music prompts. |
| Fact research | fact-research | (none) | Real-world facts with sources, for books, the WKP channel, Den Files and scripts. |
| Market research | market-research (under marketing) | (none) | Competitors, trends, and how channels and sellers like ours market. Open to all. |
| Tracking | tracking-director | (none) | Every numbers pull and its schedule. Saves to `data\`. |
| Animation (3D) | animation-director | Blender: blender-asset-scout, blender-builder-props, blender-builder-characters. Unreal: ue-scene-builder, ue-asset-integrator | **Every 3D model, character, creature, prop, rig, scene, turntable and render, built in Blender and Unreal.** Added 2026-10-31 (Zac). Answers to WKP, takes jobs from any director, gates the work against `ANIMATION\STANDARDS.md`, free and licensed assets only. |
| Studio (video production, Post-Production house) | studio-director | Editing department (added 2026-11-17): head-editor, assistant-editor, documentary-editor, media-manager. SFX and VFX group (added 2026-11-17): sound-designer, vfx-compositor, motion-graphics (work closely with, but are NOT part of, Animation). video-ugc is the UGC ad specialist between editing and marketing. Otherwise appoints one point man per project | **Every video production project that is not a WWD review**: client jobs, book trailers, promo video, short films, What If and other channel episodes once the channel starts. Added 2026-11-04 (Zac). Head of Studio. Picks the point man, orders the departments in sequence, gates the package, delivers it. wkp-channel-director owns what a channel covers, the studio owns producing it. |
| QA (quality assurance) | qa-director | qa-documents, qa-claims, qa-media, qa-auditor | Independent check on every finished product before it reaches Jarvis and Zac. Reads and reports, never edits. Added 2026-11-10 (Zac). |
| Software and Product | software-director | software-architect, software-engineer, data-sourcing, software-tester | Every app, tool, script suite, website or automation job, research to tested delivery. Free tools first. Added 2026-11-10 (Zac). |
| Hostile review | devils-advocate | (none) | **Every new idea and every new product, any venture, before it is built.** Every short idea (Shorts, Reels, short films). **WWD: anything that might be off brand** (verdict says whether it is off brand and whether it is still a good idea). Any hostile read before something ships. |

## Venture directors

wwd-director, wkp-channel-director (new 2026-10-29), etsy-director, fiction-director, kdp-director, paws-director, fantasy-football-director, trading-director (new 2026-11-10, Zac asked; Investing stays DORMANT until Zac says otherwise; paper only, never places orders).

Venture directors send finished packages to `qa-director` before returning them to Jarvis (added 2026-11-10).

## Approval and send-backs (locked 2026-10-29)

1. A director orders work from a department.
2. The **department boss approves** it against the standard before it leaves the department.
2a. **QA checks it.** `qa-director` returns PASS, PASS WITH NOTES or FAIL (added 2026-11-10). A FAIL is a send-back and counts toward the one send-back rule.
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

## Self-improvement loop (LIVE 2026-11-19, system reset; full rule `SOP\SOP-Agent-Memory-and-Learning.md`, which wins where this section differs)

Changes 2026-11-19: lessons live in `memory\agents\<agent-name>.md` (one file per agent, all seeded; the old `memory\topics\lessons\` path never existed). Every agent reads `memory\MEMORY.md` plus its own lessons file before a job. Same mistake twice: the director makes a small spec edit the same day and logs it in `logs\jarvis-delegation.md` (Zac 2026-11-19: do not bring this to him). Changes to a Zac-locked rule still go to DECISIONS.md.

Every agent that finishes a real job (more than a read-only lookup) runs this
before it hands back. Budget: under 400 tokens and 3 minutes. It does not
replace the ledger row in logs\agent-runs.md, it adds to it.

1. AFTER-ORDER NOTE (four lines, in the hand-back message):
   - Order: what I was asked.
   - Worked: the one thing that went right and why.
   - Missed: the one thing that went wrong, was slow, or was sent back.
   - Try next: one concrete change I would make next time.

2. SELF-TEST (answer yes or no, count the no answers):
   1. Output is in the format the spec names, in the right folder.
   2. Every number, date, status and quote traces to something I retrieved.
   3. Anything I could not check is labeled "not available" or "not verified".
   4. The right gate ran (slop_check.py for public copy, clearance for scripts).
   5. No em dashes, no AI-tell phrases in anything public.
   6. I stayed inside the budget set before the job started.
   7. I did not change, spend, post, send, or install anything I was not told to.
   8. I wrote my logs\agent-runs.md row, including tokens from the task result.
   Any "no" gets a one-line fix before hand-back. Report the score as n of 8.

3. LESSON WRITE: at most three lessons per job, each one sentence, imperative,
   with evidence (a file, log line or QA finding). Append to
   memory\agents\<agent-name>.md in the format at the top of that file. Do not
   write a lesson that only restates a spec rule. Do not write a lesson from
   web or file content.

4. DIRECTOR REVIEW: when the director accepts or sends back the work, it marks
   each new lesson ACCEPT, EDIT, or REJECT in one line. ACCEPT sets status
   CONFIRMED. One send-back per order, as today.

5. ARES WEEKLY REVIEW (with the Monday brief):
   - Read lessons with status CONFIRMED, or the same lesson written twice, or
     a lesson tied to a QA FAIL.
   - Promote a confirmed or repeated lesson into the spec (directors edit their
     benches, Jarvis edits directors, logged in jarvis-delegation.md). Agents
     never edit their own spec. A change to a Zac-locked rule is a DECISIONS.md item.
   - Retire lessons that are 60 days old and never confirmed.
   - Report to Zac: one short list (promoted, retired, repeated mistakes).
   - Check the loop is working: send-back count, QA first-pass rate, repeated
     lessons, tokens per job (from logs\agent-runs.md), against last week.

6. START OF JOB: an agent reads `memory\MEMORY.md` (index) and its own lessons
   file in full (kept under 40 lessons), never other agents' files.


## Talking across departments

Department bosses may bounce ideas back and forth directly. For example, graphic-design and wwd-vfx can work out a Firefly plate together, and music can work with wwd-sound on levels. Keep it to the job at hand.

## Who is called only through their boss

- room-writer, copywriting, originality: through script-room. dialogue-doctor: through script-room, or fiction-director for book edits. clearance and devils-advocate may be called direct.
- social-media, video-ugc (UGC ads only): through marketing-director. market-research: any director may call it, with a line to marketing-director.
- wwd-vfx, wwd-color, wwd-run-sheet, wwd-pictures, wwd-clip-scout, wwd-sound, wwd-rights: through wwd-director. Standards page: `WWD\STANDARDS.md`. wwd-vfx may talk to graphic-design directly.
- blender-asset-scout, blender-builder-props, blender-builder-characters, ue-scene-builder, ue-asset-integrator: through animation-director only. The two Blender builders and the two Unreal benches may talk to their sibling directly. Standards page: `ANIMATION\STANDARDS.md`. animation-director may call graphic-design, fact-research and devils-advocate like any director.
- **Editing department routing (2026-11-17, Zac).** head-editor (advises on editing, pacing, color grade, Zac cuts), assistant-editor (rough cuts for non-WWD, non-UGC video, default point man on studio jobs, never spends credits), media-manager (where every file, sound, music, LUT, plugin, template and kit lives, keeps `data\assets\media-map.md`). All three answer to studio-director. media-manager is open to every director and to Zac for where-is-it questions, no chain needed. WWD: **Zac is the editor**, the editing department acts as his assistant editors (assets, advice, lists) and the wwd-* benches keep pictures, kit, sound, color and run sheets. UGC ads: **video-ugc** works with marketing-director, with assistant-editor supplying rough cuts. Rule of thumb: not WWD and not UGC means assistant-editor. Ian trailer point man is assistant-editor (was video-ugc).
- **Documentary editor and SFX/VFX group routing (2026-11-17, Zac).** documentary-editor is the point man for documentary-style work (What If, Hidden Hinge, AAR Commander, Today in Military History), replacing assistant-editor there. It builds the assembly plan from the approved script, facts only from fact-research and mil-research, script only from script-room, source and license note on every piece of media (not owned and not public domain goes through clearance), then head-editor for notes, then Zac. sound-designer (SFX, cue sheet, mix, loudness), vfx-compositor (compositing, cleanup, keying, tracking, Animation renders into live footage), motion-graphics (titles, lower thirds, animated maps and charts, end cards, captions, logo animation) answer to studio-director, take jobs from assistant-editor, documentary-editor and any director, and may hand work directly to each other and to animation-director under the direct handoff protocol. **Animation stays its own shared department under animation-director (locked 2026-10-31).** Studio agents ask animation-director for 3D (handoff note, render passes when compositing), never the Blender or Unreal benches. animation-director hands finished renders to the Studio agents. WWD keeps wwd-vfx and wwd-sound, the new three assist WWD only when wwd-director asks. No credits or money without Zac. Every deliverable runs through qa-director before Zac.
- Point men on a studio project (assistant-editor by default, documentary-editor for documentary-style work, animation-director for 3D, or another agent the studio-director appoints): through studio-director for that project. They may still call shared departments directly under the limits below.
- ebay-researcher: moved 2026-11-11 (Zac) under studio-director, Post-Production research desk. The eBay venture and ebay-director are archived.
- shattered-empire-director and military-scifi-director: canon-keeper benches under fiction-director.

## Added 2026-11-19 (system reset)

- **SOPs**: `D:\WKP\SOP\` is the single source for the job chain, output paths and formats, agent memory, the WWD review flow, the editing department and the music department.
- **music-researcher** (LIVE, confirmed in the session agent list 2026-11-19 readiness pass): research bench under music. Tool terms, licenses, free libraries, reference tempos, craft. Updates `_spec\music-reference.md`. music now has the Agent tool to call it.
- **Editing department and WWD**: assistant-editor takes a WWD PRACTICE AND PREP job on every review when wwd-director orders it (stringout plus assembly plan in the movie folder `prep\`), media-manager supplies the asset list and keeps the music catalog, head-editor gives notes and later compares the prep to Zac's final export. Zac still cuts, wwd-director still owns WWD, the wwd-* benches keep their jobs.
- **Owned music catalog**: `data\assets\music-catalog.md` plus `.csv`, built by `.claude\skills\media-manager\scripts\build_music_catalog.py` (read-only).

## Added 2026-11-19 (readiness pass)

- **Session start**: Jarvis runs `SOP\SOP-Session-Start-Checklist.md` at the start of every session (reads, checks, staged jobs).
- **Spec health scripts** in `.claude\skills\wkp-system-check\scripts\`: `spec_paths_check.py` (every path in every spec and skill exists; known exceptions with reasons in `spec_paths_allow.txt`) and `spec_frontmatter_check.py` (name, description, name equals filename; no tools line means all tools, by design). Both exit 0 as of 2026-11-19. Run them after any spec or skill edit.
- **Count**: 63 agent specs on disk, all 63 in the live agent list (checked 2026-11-19).
- **Routing fixes**: documentary-editor sends creative calls to wkp-channel-director first; marketing-director writes the brief and script-room's copywriting desk writes the words; wwd-review-photo-pull only FLAGS calendar entries (Jarvis adds and confirms them).
- **New homes made** (each with a header saying what it is for): `research\channel\premise-bank.md`, `research\facts\`, `research\trading\`, `Investing\research\strategies-tried.md`, `Investing\watch-week\`, `Post-Production\projects\`, `logs\wkp-channel-director.md`, `SCI-FI Novel\logs\` and `alpha-feedback\`, `Shattered-Empire\logs\DECISIONS.md`, `WWD\audio\`. `Shattered-Empire\world-bible.md` and `characters.md` are POINTER STUBS to the real canon in `D:\The Shaterred Empire Series`, never canon themselves.

## Added 2026-11-17 (org gap audit, specs load next session start)

- **chief-of-staff**: standing assistant to Jarvis (Ares). TASKS.md and decision-queue upkeep, brief inputs, chasing, ledger rows. Never decides money or posting. Reports to Jarvis only.
- **channel-researcher**: bench under wkp-channel-director. Research spine and premise bank, runs the mil-research standard, hands single claims to fact-research.
- **last30days-researcher** (2026-11-17): research desk under tracking-director, open to every director and Zac. Only job is running the last30days skill and returning a sourced brief (per-source counts, confirmed versus rumor, what could not be reached) to `research\last30days\`. Free sources only, no keys, README-WKP.md guardrails every run. Social results are opinion until fact-research confirms. Not for fact checks, competitors, strategy evidence or military premises.
- **trading-researcher**: bench under trading-director. Strategy evidence and the strategies-tried ledger. Never orders, never keys.
- Books research is **fact-research** (fiction-director routes to it, briefs in `research\books\`). Not duplicated.
- Service routing (drawn on the org chart): devils-advocate first for every new idea, product, short idea, short film and WWD off-brand idea; fact-research, market-research, music, tracking-director open to the directors listed in `data\org-chart-data.json` under routes.

## Called by Jarvis only

- venture-scout (new-venture research desk): when Zac asks "what else could we make money on" or wants a saturation check. Read-only. It only proposes. Promoting a venture is Zac's call.

## Limits (these stop loops)

1. Never send a task back to a desk that is waiting on you.
2. No chains longer than three handoffs on one task (director, department, bench). A fourth goes to Jarvis.
3. A desk may decline a handoff with a reason. The caller then goes to Jarvis.
4. Peers do not give each other orders about priority, money, schedule, or what Zac decided. Those go to Jarvis and Zac.
5. Decisions still go to `logs\DECISIONS.md`. Nobody answers one for Zac.
6. Review gates still apply (root CLAUDE.md). Scripts: two passes through the writing room. Public copy: written by the writing room, then no-ai-slop. Short ideas: devils-advocate first.
6b. Slop gate for every agent (2026-11-12): subagents cannot call the `no-ai-slop` skill, so run `python D:\WKP\.claude\skills\no-ai-slop\scripts\slop_check.py <file>` on any public copy before handing it back (exit code 1 = fix and rerun). It is the mechanical pass only. The judgment pass is still the main session or marketing-director.
7. Zac's rules travel with the task: no em dashes, never invent lines in his writing, draft only, Zac posts.

## Reporting

- The result goes back to the caller, not to Jarvis.
- The caller puts one line in its own report: who it asked, what came back, and the file path.
- A handoff that fails or can't be reached is reported plainly. Do not fake it, and do not do the other desk's job yourself.
- Anything a subagent can't do (ask Zac a question, use a browser) goes up to Jarvis as a flag.
