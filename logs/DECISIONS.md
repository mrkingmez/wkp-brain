# Decision Queue

Agents append. Zac clears. Nothing else writes.



**Blocked:** what cannot proceed

**Options:** A / B / C

**Recommendation:** which and why

**Status:** OPEN | DECIDED: <answer>

---

> Cleared 2026-11-11 (Zac). 20 open items kept. The other 63 (resolved, superseded, or stale overdue-row nags) are in `D:\WKP\_archive\cleanup-2026-11-11\DECISIONS-full-before.md`, and merge-conflict markers are gone.

---

## [POST-2026-11-11-01] 2026-11-11 | Post-Production | Ian trailer: what "do not reveal the father" means

**Blocked:** Ian (relayed by Zac) said no to "revealing the father". Draft 3 Q1 asked if the trailer may hint the father is gone. Two readings: (a) do not hint he is gone, (b) do not show him at all. Draft 3.1 is built on (a): father's hands and boots appear in the memory, nothing says he is gone.
**Options:** A. Reading (a), keep Draft 3.1 as written. B. Reading (b), drop S4 and S6 and use the swap written under the beat sheet (Section 3 of `Post-Production\reports\Ian-Wrench-Turner-Trailer-Draft3-1.md`).
**Recommendation:** A, and Zac confirms with Ian in one text before clips V4 to V6 are generated. Stills can start now.

**Status:** OPEN

---

## [FF-2026-11-10-01] 2026-11-10 | Fantasy Football (personal) | Bad closing line in the tracker: JAX at BAL Week 9 shows +3.0, the Odds API market was home -10

**Context:** predictions.csv closing_line for game 401873037 is +3.0 (nflverse schedules), but the Thursday Odds API median in pickem_probs_2026_wk9.csv is home -10.0 and JAX won 33-10. A 13 point gap looks like a data error, not movement. Grading uses the frozen line so the 20 graded rows are unaffected; only gap diagnostics are. The other BAL game (Week 7 CIN at BAL, card +3.5, closing -3.0) may be real or may be a sign problem, not checked.
**Options:** A. Leave predictions.csv alone (graded rows are locked) and have the labeling code prefer the Thursday Odds API market, falling back to nflverse only when none exists (already done in `fixes-2026-11-10\pickem_labels.py`). B. Also add a corrected closing column. C. Ignore.
**Recommendation:** A. No graded row is changed.

**Status:** OPEN

---

## [FF-2026-11-10-02] 2026-11-10 | Fantasy Football (personal) | Notes from the Thursday 11-05 lunch with the friend who plays FanDuel are not in any file

**Context:** TASKS.md says Zac was to be brought into the friend's system at lunch Thu 2026-11-05. No notes exist in TASKS.md, logs, memory or Fantasy-Football\LOG.md (searched). The DFS fix used only public research and in-house nflverse tests. Nothing about his method (stacks, ownership, slate choice, sizing) is reflected.
**Options:** A. Zac gives the key points by voice or text and the DFS report is amended. B. Skip.
**Recommendation:** A, five minutes, it is the only real-money-tested source in the whole DFS work.

**Status:** OPEN

---

## [FF-2026-11-10-03] 2026-11-10 | Fantasy Football (personal) | The two Week 9 DFS lineups do not reconcile: what was actually entered?

**Context:** Zac reported 107 and 149. The saved csv lineups score 121.4 and 143.2 on realized DraftKings points before the DST (nflverse stats, DK scoring, my formula). Lineup 2 fits (about 6 for the DST). Lineup 1 cannot (the DST would be about -14). Most likely the entered lineup differed from the csv, or a player was swapped or did not play.
**Options:** A. Zac sends the entered lineup. B. Leave the DFS comparison with one reconciled lineup only.
**Recommendation:** A.
---

---

## [ETSY-2026-11-02-01] 2026-11-02 | Etsy (WKD) | Listing cap (locked 15 Aug, expires 15 Nov) sunsets in 13 days having apparently never bound in practice

**Blocked:** Root CLAUDE.md's Etsy listing cap (max 3/day, 8/week combined
WKD + Kingdom Planners, "Anti-suspension rule, not a preference") is locked
2026-08-15 and set to expire 2026-11-15 — 13 days from tonight. Per tonight's
`ETSY/weekly-prep/2026-11-01.md` (committed in `80decef`): TASKS.md shows no
confirmed live listing from either shop since before the cap was locked, so
the cap looks to have never actually been tested against real posting
volume in the three months it's been in force — it has been a theoretical
ceiling over an idle shop, not a binding constraint. No existing entry in
this file addresses whether the cap itself should be renewed, adjusted, or
allowed to lapse on 11/15; the closest related entries (ETSY-2026-10-09-01,
the lapsed Friday manual-data-pull cadence; WKD-2026-09-24-01/WKD-2026-10-03-01,
process fights over who can authorize a production pass) are about
different questions.

**Options:**
A. Let it lapse silently on 11/15 — if it's never bound, nothing changes
   operationally either way, so it's not worth a dedicated decision.
B. Flag it now so Zac decides, before 11/15, whether to renew it as-is
   (useful insurance once real posting finally starts, especially heading
   into BFCM per tonight's prep doc), loosen it, or let it expire and
   revisit if/when the shops are actually posting again.

**Recommendation:** B — low urgency, but cheap to resolve, and the timing
matters only in one direction: if Zac wants it renewed, that's easiest to
do before it expires rather than after, especially with BFCM prep already
underway and the backlog of unposted Military/Landscape/Christian designs
this same prep doc flags as still gated on listing copy, not cap headroom.

**Status:** OPEN

---

---

## [CS-2026-10-28-01] 2026-10-28 | Cyber Security | CySA+ exam deadline now 28 days overdue (was 15 days at CS-2026-10-15-01) with zero record either way, and zero repo activity in the 13 days since that entry to check

**Blocked:** CS-2026-10-15-01 flagged the CompTIA CySA+ exam target
(30 Sept 2026, per `Cyber-Security/CLAUDE.md` and root `CLAUDE.md`) as
15 days overdue with no recorded outcome. Tonight that gap is 28 days,
not because anything new happened but because nothing has: `git log`
shows no commits at all between 2026-10-26 03:12 UTC and now
(2026-10-28 03:10 UTC, this rollup's run time) — the longest gap between
commits in the recent history this rollup has checked. Cyber Security
still has no task table in TASKS.md, so there is still no row this
rollup can mark Blocked/In Progress/Done, and still no way to tell
whether Zac sat the exam, passed, failed, or punted it again. Per the
Honesty rule, reporting as genuinely unknown rather than assuming either
way.

**Options:**
A. Leave it — same reasoning as CS-2026-10-15-01 Option A: a day-job
   cert deadline, not venture money or legal exposure, and Zac would
   likely mention it unprompted either way.
B. Re-flag now that the gap has nearly doubled with zero movement, and
   treat the complete absence of a Cyber Security TASKS.md table as its
   own standing gap worth closing independent of this one exam date —
   the venture is marked ACTIVE in root CLAUDE.md but has no tracked
   tasks at all, so nothing about it can ever show up as "newly changed"
   in a nightly rollup even when something real happens there.
C. Stop re-flagging this specific exam date on every rollup cycle since
   CS-2026-10-15-01 already said what needs saying — repeating the same
   open question with a bigger day-count doesn't add new information.

**Recommendation:** B for the structural gap (give Cyber Security a real
TASKS.md table so future activity there is actually visible to this
process), C for not mechanically re-flagging the same exam date every
few nights once the first flag is on record — this entry exists mainly
to note that the 48-hour commit drought tonight means literally nothing
in the repo moved to check against, not to manufacture urgency on a
question CS-2026-10-15-01 already asked correctly.

**Status:** OPEN
## WWD-2026-10-27-01 - Vision Quest eps 3 and 4: end card and sheet density
**Raised by:** wwd-director, 2026-10-27
**Question:** (1) What follows eps 3 and 4 for the end card (stop 24 is an empty marked slot)? (2) The sheet has 24 stops, not 35 to 40, because only 10 of 38 stills are verified. Pull verified Paladin, Edith, Friday, Jarvis, pirate ship and gala pictures (IMDb per-actor galleries, needs a browser session) to add about 8 stops? (3) Wrong-name tally sticker for stop 18: series count 4, 5, 6 or "THIS VIDEO" 1, 2, 3? (4) Reuse eps 1-2 opener?
**Recommendation:** Pull the pictures via main session, then wwd-vfx builds the tally sticker.
**Status:** OPEN

---

---

## [PAWS-2026-10-31-01] 2026-10-31 | PAWS | PAWS-001 and PAWS-004 block all firmware work and have been open since the venture's scaffold, but have never been cross-logged in this file despite PAWS being ACTIVE in root CLAUDE.md

**Blocked:** `PAWS\decisions\DECISIONS.md` carries PAWS-001 (task
source — Todoist / Microsoft To Do / Google Tasks / Notion / local
file, "blocks all firmware work") and PAWS-004 (realistic hours per
week, so the build timeline means something) as OPEN, both since the
venture's scaffold commit. Root `CLAUDE.md` lists PAWS under ACTIVE
venture status. TASKS.md's PAWS table shows every Phase 0/1 firmware-
adjacent row ("Decide task source," "Set realistic hours per week,"
"Task API call, parse JSON...," "Port state machine to firmware...")
as "Not Started," consistent with both blockers still being open. This
is the first time this specific gap has been cross-logged in the main
nightly-rollup decision file — it has only ever lived in PAWS's own
venture-level queue, so it has never been visible to whoever reviews
this file without also opening PAWS's queue separately.

**Options:**
A. Leave it in PAWS's own queue only — that file already tracks it
   correctly with the right context (board boots, state-machine-on-PC
   work already done and not actually blocked by either question), and
   duplicating it here risks the two queues drifting out of sync.
B. Cross-log once (this entry) so a scan of this file alone surfaces
   that an ACTIVE venture has a standing firmware blocker, without
   trying to own or duplicate PAWS's queue going forward.

**Recommendation:** B for this one entry, then back to A — PAWS's own
queue is the right home for PAWS-001/PAWS-003/PAWS-004/PAWS-006/
PAWS-007/PAWS-008 going forward; this is a one-time visibility flag,
not a decision to start mirroring that whole queue here every night.

**Status:** OPEN

---

---

## [ANIM-2026-11-02-01] 2026-11-02 | Animation (Blender/Unreal, shared) | Three Zac-only sign-offs from the 2026-10-31/11-01 build have never been escalated to this queue

**Blocked:** TASKS.md's Animation department row and `ANIMATION\CLAUDE.md`
both carry "OPEN FOR ZAC" items from the 2026-10-31 build (specs for
`animation-director`, 5 benches, 7 training skills, and `ANIMATION\STANDARDS.md`
all written and committed, most recently in `87705c1`, 2026-11-01): (1) Zac
needs to mark up `ANIMATION\STANDARDS.md` — every number in it is currently
a Claude-drafted guess; (2) Zac needs to pick the Blender-to-Unreal pipeline
repo from the candidates report (`D:\WKP\reports\animation\2026-10-31-Blender-UE-Pipeline-Candidates.md`)
before anything gets installed — xavier150's Blender-For-UnrealEngine-Addons
(GPL-3.0) is the only one proposed so far, nothing is installed; (3) Zac
needs to say yes or no to any Unreal bridge that opens a network port (Epic's
built-in MCP plugin on port 8000, no auth found, is currently off by default
per his 2026-11-01 answer, but the broader "any future port" question is still
open). None of these three have ever been logged in this file — they have
only ever lived inline in TASKS.md and `ANIMATION\CLAUDE.md`, which this
nightly rollup does not treat as the decision queue.

**Options:**
A. Leave it — Zac already has the full list sitting in `ANIMATION\CLAUDE.md`
   and the open item is naturally visible the next time he opens that file
   or the Animation department comes up.
B. Cross-log once (this entry) so a scan of this file alone surfaces that a
   shared department with real spend/security implications (GPL licensing,
   an open port) has three unresolved sign-offs, without trying to mirror
   `ANIMATION\CLAUDE.md`'s open-items list every night going forward.

**Recommendation:** B, one-time visibility flag — nothing here is urgent
(no work is blocked on it since the Blender/Unreal benches have other
backlog), but a license pick and a network-port question are exactly the
kind of irreversible-ish calls that should have a paper trail in the
decision queue, not just a venture file.

**Status:** OPEN

---

---

## [ANIM-2026-11-05-01] 2026-11-05 | animation-director | Keep the copyrighted starterKit images inside the git repo folder?

**Context:** Zac's starterKit (3D Total planar head references, copyrighted, plus 5 kit images of unstated author) sits in `D:\WKP\ANIMATION\training\starterKit-2026-11-05\`. That folder is inside the repo and not gitignored (checked with git check-ignore, no match), so a normal commit and push would upload copyrighted images to GitHub (wkp-brain). Nothing was committed or ignored by me.

**Options:** A. Add `ANIMATION/training/` to .gitignore (images stay on disk, never pushed). B. Move the folder outside the repo, for example `D:\Training Refs\`, and update the skill and asset log paths. C. Leave as is and accept pushing them (not recommended).

**Recommendation:** A, one line, reversible.

**Status:** OPEN

---

## [ANIM-2026-11-05-02] 2026-11-05 | fact-research for animation-director | Tutorial picks: approve, and the boat gap

**Context:** Picks file `research\animation\2026-11-05-tutorial-picks.md` (docx in `D:\WKP Reports\Animation Tutorial Picks\`). None of the five Blender channels has a boat or hull tutorial. Mesh Terrain (top landscape pick) is experimental in Unreal 5.8.

**Options:** A. Approve the yes/no list at the top of the file, then transcripts are pulled for yes items only. B. For the boat topic, let the department search outside the five channels for one video and bring it back for approval. C. Use the Blenderfast track for the boat. D. Teach Mesh Terrain as main landscape route or classic Landscape only.

**Recommendation:** A, B (one video, approval before any transcript), and teach both landscape routes with classic first for anything that must ship.

**Status:** OPEN

---

## [VENTURE-2026-11-03-01] 2026-11-03 | Venture scout | CMMC Level 1 kit: day-job conflict check must be done by Zac before any build or public sale

**Context:** Deep dive at `research\ventures\cmmc-l1\01-scope-deep-dive.md`. The venture sells cyber compliance documents. Zac works in cyber for a day job. An agent cannot read his employment terms and must not assume.

**Question for Zac:** Read his employment agreement, outside-work/moonlighting policy, any ethics or conflict-of-interest form, and (if the employer touches DoD or contractors) any rule about advising defense contractors. Does it allow selling CMMC Level 1 templates? Checklist is in section 4 of the deep dive.

**Options:**
A. Check and get written OK (or a yes from HR/ethics) before building anything public.
B. Drop the venture if the policy blocks it.

**Recommendation:** A. Cost is one read-through plus maybe one email from Zac. Nothing is built or sold until answered.

**Status:** OPEN


---

---

## [VENTURE-2026-11-05-01] 2026-11-05 | Venture scout | Fort Eisenhower/Fort Gordon newcomer guide: verdict is slow/no demand proof, cheap free test proposed, never logged to the decision queue

**Blocked:** Venture-scout idea 3 from the 2026-10-26 first scan (`research\ventures\2026-10-26 venture scout first scan.md`) got two research passes on 2026-11-03, both committed in that day's batch (`61a5200`): `research\ventures\newcomer-guide\01-market-research.md` and `02-fact-and-risk-brief.md`. Market research verdict: "Slow, off-season, free competition is good, and no demand proof" — no paid Fort Eisenhower/Fort Gordon PCS guide found on Etsy, Gumroad, Payhip, Amazon, or TpT; demand signal is two stale, mostly unreadable forum threads; and a free, active Facebook PCS group (Fort Gordon PCS Pay-It-Forward) already covers much of the same ground. The research's own recommendation is a $0, about one-hour free test post in that group to count real requests before writing anything paid. The fact/risk brief adds 17 open questions only Zac can answer (audience and scope, which gates/areas/schools, VA and spouse content, personal "what I wish I knew" material) plus real fair-housing, platform-disclosure, and licensed-data (GreatSchools) guardrails if it ever gets built. Neither file has reached this queue — the same gap already flagged for the parallel CMMC-L1 idea from the same scan in `VENTURE-2026-11-03-01`.

**Options:**
A. Run the free test first (post in the Fort Gordon PCS Pay-It-Forward Facebook group, count real requests) before building or writing anything, per the research's own recommendation.
B. Skip the test and draft the paid guide anyway, treating this as content Zac already knows firsthand regardless of the no-demand-proof finding.
C. Drop the idea for now — slow season, free competition already covers most of it, and the stronger lead from the same scan is CMMC L1 (already queued in `VENTURE-2026-11-03-01`), not this.

**Recommendation:** A — costs nothing but Zac's time, and directly tests the one gap the research actually found (no demand proof) before any of the 17 open questions are worth spending time answering.

**Status:** OPEN
---

---

## [WWD-2026-11-05-01] 2026-11-05 | marketing-director | Apply to OpusClip and vidIQ affiliate programs (first monetization test)?

**Context:** Research in `WWD\reports\Monetization-Options.md`. Both are free signups for tools WWD already uses. OpusClip: 25% recurring, 20 dollar first payout, application reviewed, no paid ads with the link, deactivated after 6 months of no traffic. vidIQ: 15 to 25% lifetime recurring, 10 dollar payout, self-service. vidIQ sits under Matt's login, so that one is a joint call with Matt. Signup means entering an email and a PayPal address. Nothing was entered.

**Options:** A. Apply to both, then wait four weeks. B. OpusClip only. C. Skip, nothing at this size pays.

**Recommendation:** A, with Matt's yes on vidIQ. Expect tens of dollars at best, no income evidence exists for channels this size.

**Status:** OPEN

---

## [WWD-2026-11-05-02] 2026-11-05 | marketing-director | Amazon Associates or Bookshop.org storefront for Den Files book links?

**Context:** Amazon closes a new application that does not drive 3 qualifying sales in 180 days (SECONDARY, verify on Amazon). Bookshop has no audience minimum, 48-hour attribution, non-bookstore rate unverified. Signup enters personal and payment data. Nothing entered.

**Options:** A. Bookshop only, when a Den Files episode with a book is ready. B. Both. C. Neither.

**Recommendation:** A. Skip Amazon until a video exists that sends real clicks.

**Status:** OPEN

---

## [WWD-2026-11-05-03] 2026-11-05 | marketing-director | Open a Ko-fi tip jar (and link it in descriptions)?

**Context:** Free, no minimum, no fee on tips (SECONDARY). Joint with Matt since it touches branding. Real small movie-show Patreon pages show about 7 to 37 dollars a month. Not recommended: Patreon (10% fee plus extra bonus-episode workload).

**Options:** A. Ko-fi page only. B. Skip. C. Patreon.

**Recommendation:** A, low priority, after 01.

**Status:** OPEN

---

## [WWD-2026-11-05-04] 2026-11-05 | marketing-director | Two numbers only Zac can pull: YouTube Studio Earn tab and Spotify Monetize page

**Context:** Which methods are even open (memberships, Shopping affiliate, merch shelf, Spotify ads) depends on WWD's YPP status, long-form watch hours, and Spotify audience. Not in any file. No signup, just a screenshot or one line.

**Recommendation:** Do this first. Or ask tracking-director to add watch hours to the next pull.

**Status:** OPEN

---

## [WWD-2026-11-05-05] 2026-11-05 | market-research | Adopt the one-sponsor-line layout for WWD descriptions and pinned comments?

**Context:** 15 channels read (`research\wwd-monetization\links-per-video.md`). Sponsored large-channel videos carry exactly 1 sponsor link on line 1, a pinned repeat, and no second commercial link. Shorts carry no third-party link.

**Options:** A. Surfshark on line 1, at most 1 other link, sponsor-only pinned comment, no sponsor links on Shorts. B. Keep the current layout. C. Add more links.

**Recommendation:** A. Copy goes to the writing room, then no-ai-slop.

**Status:** OPEN

---

## [WWD-2026-11-05-06] 2026-11-05 | market-research | Audit the spoken and on-screen sponsor reads of the sampled channels?

**Context:** This pass read descriptions and pinned comments only. Spoken reads, cards and end screens were not watched. Transcripts could be pulled from VidIQ, which needs Zac's go-ahead and uses credits (0 until 11-11).

**Options:** A. Skip. B. Do it after 11-11 for the 6 sponsored videos. C. Watch by hand.

**Recommendation:** B only if the layout decision above is made and read length matters.

**Status:** OPEN

---

## [WWD-2026-11-05-07] 2026-11-05 | market-research | Check WWD's Studio Shopping eligibility

**Context:** YouTube Studio redirected to the home page in the research Chrome session, so the Earn page could not be read. Shopping tab shows only if the channel is eligible. Details in `research\wwd-monetization\youtube-shopping.md`.

**Options:** A. Zac opens Studio, Earn, and says whether a Shopping tab exists. B. Skip until YPP status is known (see WWD-2026-11-05-04).

**Recommendation:** A, one minute, no clicks that change anything.

**Status:** OPEN

---

## [WWD-2026-11-05-08] 2026-11-05 | market-research | Amazon Associates or a print-on-demand store for WWD product tags?

**Context:** Both need a signup, a POD store may cost money (prices not verified). Neither started. Only useful once WWD is in YPP.

**Options:** A. Wait for the Studio check. B. Open an Amazon Associates account (Zac signs up). C. Open a free-to-start POD store such as Spring or Spreadshop (cost not verified).

**Recommendation:** A first.

**Status:** OPEN

---

## [INFRA-2026-11-11-01] 2026-11-11 | Nightly rollup | Conflict markers in this file (flagged by the nightly rollup)

**Status:** RESOLVED (option A done 2026-11-11 during the Zac-approved cleanup: markers removed, both sides' entries kept, full old file archived at `_archive/cleanup-2026-11-11/DECISIONS-full-before.md`). Option C (a hook or rule refusing a commit that contains `<<<<<<<`) is still optional, Zac's call.
