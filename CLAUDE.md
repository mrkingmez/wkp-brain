# WKP â€” Warrior King Productions
## Root context file. Read this first, always.

@./ME.md
@./projects.md
@./TASKS.md
@./LOCAL-PATHS.md

---

## What this is
Top-level routing intelligence for all WKP ventures. Any session that starts here should read ME.md, projects.md, and TASKS.md, then route to the relevant venture folder.

## Ventures and where they live
| Venture | Folder | Priority |
|---|---|---|
| Etsy â€” WarriorKingDesigns (puzzles + wall art) | ./ETSY/ | 1 |
| Etsy â€” Kingdom Planners (digital planners) | ./Kingdom-Planners/ | 2 |
| Shattered Empire novels (Books 1 and 2) | ./Shattered-Empire/ | 3 |
| Winter Wolf's Den / FrostCast / Den Files | ./WWD/ | 4 |
| WKP Channel â€” What If / Hidden Hinge / AAR Commander | ./WKP-CHANNEL/ | 5 |
| Post Production house | ./Post-Production/ | 6 |
| Military SciFi novel | ./SciFi-Novel/ | 7 |
| RUBY TWO (WWII short film) | ./RUBY-TWO/ | 8 |
| Cyber Security (day job practice) | ./Cyber-Security/ | 9 |
| Investing challenge | ./Investing/ | 10 |
| KDP Publishing (math mystery + puzzle books) | ./KDP/ | active-unscheduled (was 1b, downgraded 1 SEP 26) |
| eBay Dropship (working name WKP Commerce) | ./ebay-dropship/ | Phase 0, scaffold built, awaiting Zac setup items (not yet placed in a venture-status category, Zac decides) |

## Standing rules

**Files and source of truth**
- GitHub (`wkp-brain`, cloned to C:\WKP) is source of truth for all operational brain files: ME.md, projects.md, TASKS.md, LOCAL-PATHS.md, and every CLAUDE.md.
- Google Drive holds reference material only â€” manuscripts, images, spreadsheets, production bibles, PDFs. Not operational files.
- Local drives hold raw media and large files, mapped in LOCAL-PATHS.md. LOCAL-PATHS.md is per-machine and must be rebuilt on each new computer, never copied.
- NEVER create operational files through the Google Drive API. It silently converts markdown to Google Docs and breaks every @-import. Create locally in C:\WKP, commit, push.
- One folder per venture, one CLAUDE.md per folder. A piece of a venture (a cold open, a single book, a template, an episode) is a section inside that venture's CLAUDE.md, not its own folder. New folders only for genuinely separate operations.

**Task tracking**
- TASKS.md is the single task list across all ventures. New work goes in it the same turn it comes up.
- When something in a conversation should update a file, flag it in the moment â€” which file, what changed. Do not let updates accumulate silently. Unmerged patch files are how the Drive version of this system rotted.

**How to work with Zac**
- Fire-and-forget: take initiative, propose next steps, execute reversible actions without asking. Zac pulls the trigger on anything irreversible.
- Real opinions and pushback with evidence. Buddy-cop / writer-editor engagement, not hedged responses.
- Zac uses voice-to-text, often while driving. Interpret phonetically, not literally. "roger" and "copy" mean yes. Don't flag typos. Pauses and self-talk during voice sessions are not directed at Claude â€” wait rather than treating silence as a complete answer.
- Step-by-step with every click spelled out. Plain language, no jargon. Word (.docx) format for any output/deliverable document â€” guides, upload packages, reports, worksheets, anything that isn't an operational repo file â€” so it can be printed and worked from physically; save the .md too. See "Output document format" rule below.
- Zac has ADHD. Structure helps. Keep responses tight so it's easy to snap back to task.

## Daily rhythm
- **Morning** â€” calendar + TASKS.md: what's on today, what's overdue, what comes first
- **Midday** â€” accountability: what was committed to, what's done, update TASKS.md
- **Evening** â€” review: what got done, what rolls to tomorrow, update TASKS.md

## Recurring commitments
- FrostCast records **Wednesdays 9pm**, weekly, does not stop for other projects
- Etsy posts new designs Monday and Wednesday, digital printables only (locked 8/31 â€” physical puzzle/canvas listings discontinued, see ETSY/CLAUDE.md)

## Current state â€” August 2026
- Second Brain rebuilt on GitHub after the Drive/Google Docs conversion failure. Phase 1 in progress.
- FrostCast at episode 106. New cold open pushed 2 weeks (Zac's call, 2026-09-01) â€” now targeted for ~episode 112 / mid-to-late September 2026, was ~episode 110 / early September.
- Kingdom Planners: seven finished products, zero listings, shop not yet created. The pipeline is far ahead of the storefront.
- Den Files episode 1 (Fire in the Sky) targeted for release 1 October 2026 (locked 26 Aug 26).
- CySA+ exam targeted 30 Sept 2026 (punted from end of August 2026, moved 8/31).

## Memory

There is a memory system in this repo at `memory/`.

- **Session start:** read `memory/MEMORY.md`, then follow pointers relevant to
  the work at hand. Do not recite it back unless asked.
- **During the session:** when something worth keeping is learned, append it to
  `memory/topics/<topic>.md` and add a pointer line to `memory/MEMORY.md`.
- **When stuck:** grep `memory/MEMORY.md` and follow pointers to past learnings
  before troubleshooting from scratch.

**Routing rule.** Decisions go in a CLAUDE.md. Machine-specific paths go in
LOCAL-PATHS.md. Learnings go in memory. Anything Zac decided on purpose must be
written to the right file and flagged out loud the same turn it comes up.

**Never write memory to `C:\Users\...\.claude\projects\`.** That path is a
junction pointing here. Always write to `memory/`.

Full protocol: `.claude/commands/mem.md`, also `/mem show` and `/mem forget`.

Memory lives in git. Prompt Zac to commit and push before a work session ends.

## FrostCast Transcription Workflow

When Zac says an episode is downloaded, run the whole chain without asking for
details:

1. Find the episode file under the FrostCast path in LOCAL-PATHS.md
2. Launch `skills\wwd-video-transcriber\scripts\transcribe.py` against it,
   detached, on the GPU
3. Save the transcript as `.txt` in the same folder as the video
4. Return chapter timecodes when it finishes
5. Run the `wwd-audio-cut` skill against the transcript and save the cut
   document to `L:\Winter Wolfs Den review show\Audio\podcast Frostcast audio files\`
6. Send the full transcript file to Matt over Facebook Messenger â€” changed
   2026-09-16 from email (email is retired for this step, per Zac's call
   after testing the Messenger route). Use `claude-in-chrome` browser
   automation against Zac's already-logged-in Facebook session, not the
   Composio Facebook API connection (the API's `FACEBOOK_SEND_MEDIA_MESSAGE`
   only accepts a public URL and can't take a local file â€” dead end, don't
   retry it). Steps:
   a. Navigate to `https://www.facebook.com/messages` and open Matt Khourie's
      personal thread (find it in the chat list, or search Messenger for his
      name if it's not already pinned/recent).
   b. Use `find` to locate the file-attach input in the compose toolbar
      (matches "attach photo or file button").
   c. Use `file_upload` with the transcript's full local path (the same
      `.txt` saved in step 3) against that input's ref.
   d. Click Send.
   e. Screenshot the thread afterward and confirm the message shows
      "Sent" with the correct filename before reporting done â€” don't
      report success without that confirmation.
   Send the whole transcript file as an attachment, not pasted as chat text
   (Messenger caps messages around 2,000 characters â€” the full transcript is
   far larger) and not a summary or excerpt.

Do not ask which file or where to put the output. The episode number comes from
the WWD calendar, so check there rather than asking. Steps 5 and 6 are standard
for every episode now, run automatically as part of the same chain â€” do not
wait for Zac to ask for the audio cut or the Messenger send each time. If
Chrome/the claude-in-chrome extension isn't available or Zac isn't logged into
Facebook when this step runs, flag it back to Zac rather than silently
skipping the transcript delivery.

**Status:** EP106 transcript generated 2026-08-09 (see TASKS.md). Speakers
came back as Guest/Unknown â€” voiceprints still aren't enrolled, so it needs
hand-mapping to Matt/Zac/Gabby before downstream use.

**Voiceprints are not enrolled.** `voiceprints/` is empty, so speakers come back
as Guest/Unknown and need mapping by hand. Enrolling Matt, Zac, and Gabby
requires a clean solo audio clip of each.

## Escalation rule â€” applies to every agent
You cannot ask Zac a question directly. The tool does not exist
inside a subagent. When you hit a decision you are not authorised
to make: do NOT guess. Append to D:\WKP\logs\DECISIONS.md, then
return DECISION QUEUED plus the ID. Keep working on anything not
blocked by it.
 
## Honesty rule â€” applies to every agent
Never report a number, status, or result you did not actually
retrieve. If a source is unreachable, a key is missing, or a tool
failed, say "not available" and name what is missing.
 
## Scratch and output routing
- Scratch: D:\WKP\scratch\ (gitignored). Never system Temp.
- Reusable scripts: the owning skill's scripts\ folder.
- Deliverables: L:\ per LOCAL-PATHS.md, with a log line in logs\.
- Paths and interpreters: read LOCAL-PATHS.md. Never hardcode.

## File retention
Any file produced in a chat gets downloaded to disk the same session it
is created. Chat outputs are not storage. Deleting a chat deletes the
only copy. This rule exists because five Kingdom Planners spreadsheets
were lost exactly that way.

## Writing rule â€” LOCKED 14 SEP 26
No em dashes, anywhere, ever. Nothing generic â€” no throat-clearing opens,
no AI-tell phrases (elevate, unlock, game-changer, dive into, boundaries,
seamless, etc.), no line that could sit unchanged in any other channel's
copy. Before anything public-facing ships â€” social post, sponsor read,
video description, Etsy listing, pinned comment, sponsor email â€” run it
through the `no-ai-slop` skill. Internal files (TASKS.md, memory, logs,
decisions) are exempt.

## Review gates â€” LOCKED 19 OCT 26 (Zac), applies to every venture
1. **Social media.** Nothing goes to a social platform (post, caption, promo, short description, pinned comment) until it has been through the writing room (`script-room`) and marketing (`marketing-director`, routing to `copywriting` / `social-media`), then `no-ai-slop`. Drafts written in a pipeline skill do not count. Agents draft, Zac posts.
2. **Scripts.** Every script goes through the writing room TWICE (two full passes: structure, dialogue, originality, clearance as `script-room` runs them) before it is called final. Log both passes.
3. **Teasers, not verdicts.** Promo copy leads with the hook and never hands over the answer the video exists to give.
If an agent in the chain is unavailable, say so in the deliverable. Do not skip a gate silently or hand-write around it.
**Wired 2026-10-20:** every venture director (wwd, etsy, kdp, paws, ebay, fiction, shattered-empire, military-scifi, fantasy-football) has a "Writing room and marketing" section and the Agent tool. Scripts go to `script-room`, public copy to `marketing-director`. A director that cannot reach one returns NEEDS WRITING ROOM or NEEDS MARKETING and the main session (Jarvis) runs it.
**Org change, LOCKED 2026-10-29 (Zac):** the writing room (script-room) writes every word for every department except Zac's books (books only on request). Copywriting moved into the writing room. Marketing, graphic design, music, fact research, market research, and the new tracking department are shared and open to every director. Every new idea and every new product in any venture, every short idea (Shorts, Reels, short films), and anything that might be off brand for WWD goes to devils-advocate first. For WWD off-brand ideas it rules on both "off brand?" and "still a good idea?". Every music request goes to the `music` agent. Department boss approves, the ordering director accepts, at most one send-back each, then it goes to Zac. WWD thumbnails are Matt's. Full map: `AGENT-NETWORK.md`.
**Direct handoffs, 2026-10-20 (Zac):** directors talk to each other without going through Jarvis. Protocol in `AGENT-NETWORK.md`. Departments and benches stay behind their boss.

## Output document format â€” LOCKED, repeated correction (again 12 SEP 26, folder rule added 5 OCT 26)
Test: is this file needed as a repo file (operational â€” CLAUDE.md,
TASKS.md, skill/agent definitions, code, README)? If yes, .md/code stays
as-is, git-tracked. If no â€” it's an output/deliverable document a human
reads, prints, or ships (upload packages, guides, reports, worksheets,
tracker docs, anything handed to Zac or Matt as a finished piece) â€”
it goes out as **.docx**. This is not new â€” ME.md has said "Word format for
guides" since the start â€” but it keeps getting narrowed to "guides only"
and skipped on everything else (WWD upload packages have shipped as
.md or .txt repeatedly). The rule is broader than guides: any
non-repo output document, full stop. Do not re-narrow it again.

**One delivery folder, locked 5 OCT 26 (Zac's call â€” he kept losing
track of which report lived where):** every deliverable .docx for Zac
goes to `D:\WKP Reports\<Deliverable Name>\<YYYY-MM-DD> -
<Deliverable Name>.docx` â€” one subfolder per deliverable type, every
dated version inside it, filename starts with the date. This is the
ONE place Zac looks, full stop â€” don't leave a deliverable .docx
sitting only in some venture folder instead. The matching .md (still
needed â€” it's the working source, and it's what makes future edits
and git version history usable, not something Zac has to see) stays
in the repo near the venture it belongs to (e.g.
`Kingdom-Planners\reports\`, `reports\monday\`), never in
`D:\WKP Reports\` itself. Zac confirmed explicitly he doesn't need the
.md as long as I can still do my job with it living elsewhere.
Migrated 5 OCT 26: Monday Briefs (`reports\monday\` â†’
`D:\WKP Reports\Monday Brief\`) and the KP listing prep batch
(`D:\05 Kingdom Planners\` â†’ `D:\WKP Reports\Kingdom Planners Listing
Prep\`, .md moved to `Kingdom-Planners\reports\`). WWD upload packages now ALSO go to `D:\WKP Reports\WWD Upload Packages\<Movie> Upload Package\` (Zac's call 2026-10-19). The movie folder keeps its own copy because the editor works from it, the reports folder is the one place Zac looks.
 
## Etsy listing cap â€” LOCKED 15 AUG 26, expires 15 NOV 26
Maximum 3 new listings per day, maximum 8 per week, across both
shops combined. Anti-suspension rule, not a preference.
 
## Venture status â€” set 15 AUG 26, amended 24 AUG 26, amended 1 SEP 26, review 15 NOV 26
MAIN EFFORT: Kingdom Planners
ACTIVE: WWD/FrostCast, Shattered Empire, Cyber Security,
        WarriorKingDesigns (triage complete, hold), PAWS (director:
        paws-director, character locked - Scout, an original dog,
        not the WWD wolf - hardware direction locked - fused
        personality-device-plus-USB-C-hub product from day one, not
        a screen-first build - still blocked on PAWS-001 - task
        source not yet chosen - and PAWS-004 - hours per week not
        yet set - both block firmware work)
ACTIVE-UNSCHEDULED: KDP Publishing (math mystery / puzzle books), WKP Channel,
        Post-Production, RUBY TWO, Spark Capture (Android app, scaffold
        applied, no director, at D:\WKP\spark-capture\, Phase 2 not yet
        scheduled)
  - No agent, no schedule. Do not surface in daily planning.
DORMANT: Investing, SciFi Novel, Shadows, Survival-SciFi, Website
  - Capture only. Do not surface unless Zac asks directly.

KDP downgraded from PRIORITY 1B to ACTIVE-UNSCHEDULED 1 SEP 26 â€” Zac's
direct call, pivoting away from it. Was priority 1B added 24 AUG 26.

No agent may promote a venture between categories. That is a
Zac decision. Queue it in DECISIONS.md if the case is strong.
 
## Closed loop â€” applies to every director
Before planning any week's work, check D:\WKP\data\ for a recent
file for your venture. If none exists in the last 10 days, say the
plan is unguided rather than inventing a number.

## Etsy data â€” manual, not exported
Etsy provides NO traffic CSV export. Views, favorites, and visits
live only in D:\WKP\data\etsy-manual-YYYY-MM-DD.md, typed by hand
each Friday. Do not look for an Etsy traffic CSV. Do not report a
view or favorite count that is not in that file.