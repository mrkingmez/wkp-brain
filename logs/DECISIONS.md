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

**Status:** RESOLVED 2026-11-12 as a MISREAD (Jarvis, per Zac's correction). Zac: the secret is that Brandon is a father and the kid near the end is his, not Brandon's own dad. Ian's "the father must not be revealed" meant Brandon must not be revealed as a father and his child must not be seen or hinted. Brandon's own dad in the memory shots is fine. Draft 3.2 corrected the same day (Section 0 fence). No hold on V4 to V6. Options A and B are void.

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

**Status:** DECIDED 2026-11-12 (Zac, relayed by Jarvis): the CySA+ exam is punted because of the exam cost, no new date. Option C: stop re-flagging the date. Root CLAUDE.md, Cyber-Security/CLAUDE.md and TASKS.md updated the same day. The structural gap (no Cyber Security task table) is closed with a TASKS.md row. CLOSED.
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

**Status:** OPEN for vidIQ and the Matt call. UPDATE 2026-11-12: Zac received the OpusClip affiliate link (the OpusClip half of option A/B is effectively done). The link itself, terms and disclosure wording are not yet in the repo, see TASKS.md row and `memory\topics\marketing-sponsors.md`.

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

---

## [FF-2026-11-11-01] 2026-11-11 | fantasy-football-director | Taxi promotion rule and cost for Derrick Moore (DET DL)

**Context:** Wonnum (Q, concussion) 2.6 vs Moore (taxi) 2.9 at DL2. Director does not know the taxi activation rule, roster room or cap effect. Promotion is not a drop, no dead cap.

**Options:** A. Promote Moore if free. B. Keep Wonnum, rely on Thursday report.

**Recommendation:** A if the promotion is free, low confidence. Decide before Thursday 8:15 PM ET.

**Status:** OPEN

---

## [FF-2026-11-11-02] 2026-11-11 | fantasy-football-director | Is Zac in an Elimination Challenge this week?

**Context:** Zac was out of EC2 as of Week 8, a leftover "new EC" line is unconfirmed. If yes, JAX (about 79.5 percent) is the safest pick and is already the ATS pick.

**Status:** OPEN

---

## [FF-2026-11-11-03] 2026-11-11 | fantasy-football-director | No Week 10 DFS salary file

**Context:** Latest DK/FD file on disk is the Week 9 slate (11/7). No DFS lineup built, only projections csv.

**Options:** A. Zac drops the Week 10 salary file, director rebuilds. B. Skip DFS this week.

**Status:** OPEN

---

## [SW-2026-11-11-01] 2026-11-11 | software-director | College football data for the pick'em card
**Context:** Report `research\fantasy\2026-11-11-college-football-data-sources.md`. ESPN unofficial scoreboard gives 2026 schedule, results and odds keyless, but odds vanish when games finish, and injuries and depth charts are unusable.
**Options:** A. Build a small weekly ESPN snapshot script (lines history, rankings, leaders), about 20 calls a week, no cost. B. Also request a free CFBD key (Zac, email only, collegefootballdata.com/key). C. Do nothing, keep the 9-book line only.
**Recommended:** A now, B optional. ESPN API is unofficial with no published terms for it, Zac's call on that risk.
**Status:** IMPLEMENTED 2026-11-12 (Zac chose A). Code and tests: `software\cfb-espn-snapshot\` (builds on `Fantasy-Football\tracker\cfb_snapshot.py`). Output: `data\cfb\espn\YYYY-MM-DD\HHMM.json` plus `data\cfb\espn\line_history.json`. Scheduling is NOT registered, needs Zac's yes. CFBD key (option B) was already working.

---

## [FF-2026-11-12-01] 2026-11-12 | Fantasy Football (personal) | Play chance by practice status, in code, instead of rule 4 by hand

**Context:** Audit `Fantasy-Football\reports\Fantasy-Sim-Audit-2026-11-12.md`, finding 4. The sim plays every Questionable at 75 percent. The 11/10 study: Questionable and no Wednesday practice scored zero 53 to 67 percent of the time, Questionable and limited 13 to 38 percent. Rule 4 (locked 11/10) is applied by hand and was missed on Okereke Wednesday night (status unconfirmed, he did not practice). The injury file now carries a `practice` column, no behavior change yet.
**Options:** A. Put it in code: Questionable and no practice plays 0.40, Questionable and limited or full plays 0.85, rerun the 11/10 backtest first. B. Keep rule 4 by hand. C. A, but only the no-practice half.
**Recommendation:** A. It changes a locked rule, so it needs Zac's yes.

**Status:** IMPLEMENTED 2026-11-12 afternoon on Jarvis's relay of Zac's approval. Built as option C: no practice 0.40 (backtest error 65.2 to 64.0); the 0.85 for limited or full FAILED its backtest (68.8) and was not adopted. Zac confirmed in chat 2026-11-12 ("do all that is proposed"). `Fantasy-Football\CLAUDE.md` amended 2026-11-12 with the rule 4 text. CLOSED.

---

## [FF-2026-11-12-02] 2026-11-12 | Fantasy Football (personal) | Pick label percentages: use real-game cover rates by line band, and drop the play sim tilt

**Context:** Same audit, finding 5. The label uses a smooth curve; real scores bunch on 3, 7 and 10. This week: Seattle -3.5 label 59.0, real games 63.3 (n=390); Rams -7.5 label 56.0, real 49.2 (n=120). Separately, Wednesday's straight-up side leaned 15 percent on the play sim margin, which carries no information beyond the market (coefficient 0.18, error 0.19). Thursday used the market alone; no pick changed.
**Options:** A. Blend the curve with the real-game table and remove the tilt. B. Remove the tilt only. C. Leave both.
**Recommendation:** A. About 2 hours. Labels change, the LEAN, SLIGHT, NO EDGE gap rule does not.

**Status:** IMPLEMENTED 2026-11-12 afternoon on Jarvis's relay of Zac's approval. `ff-simulator\scripts\cover_table.py`, plus a HOOK rule for coin-flip games (walk-forward 54.1 vs 51.8 percent). Week 10 game 8 flipped to Detroit -2.5. Zac confirmed in chat 2026-11-12. `Fantasy-Football\CLAUDE.md` amended 2026-11-12 with the rule 2 text. CLOSED.

---

## [FF-2026-11-12-03] 2026-11-12 | Fantasy Football (personal) | Backfill the tracker for Weeks 2, 3 and 5

**Context:** `tracker\predictions.csv` holds Week 1 (6 games) and Weeks 6 to 10. The model doc and both of Zac's cards exist for Weeks 2, 3 and 5 in `D:\Documents\Pickups 2026\`. There is no Week 4 folder. No market pull was saved for those weeks, so a backfill adds graded picks but no line-gap data. Not done in the 11/12 run.
**Options:** A. Backfill 2, 3 and 5, labelled BACKFILL. B. Skip. Also: does a Week 4 card exist anywhere?
**Recommendation:** A, about 1 hour, low urgency.

**Status:** OPEN. Approved per Jarvis's relay 2026-11-12 but NOT done: the logger refuses post-kickoff rows by design and a safe backfill needs its own pass.

---

## DECISIONS RECORDED 2026-11-12 (Zac, picked from a choice list)
- WWD-2026-11-05-01: Ask Matt about vidIQ using Zac's email, and marketing-director builds a full OpusClip affiliate push research packet (ideas, scripts, assets needed vs on hand). Packet in progress at `WWD\reports\OpusClip-Affiliate-Push-Packet.md`. Matt's yes still needed for vidIQ.
- WWD-2026-11-05-02: DECIDED, both Bookshop.org and Amazon Associates for Den Files book links. Signups are Zac's, when an episode with a book is ready.
- WWD-2026-11-05-03: DECIDED, Ko-fi tip jar, low priority, joint with Matt.
- WWD-2026-11-05-05: DECIDED, adopt the one-sponsor-line layout. Copy goes to the writing room, then the slop check, before anything posts.
- WWD-2026-11-05-06: DECIDED, skip the sponsor-read audit.
- WWD-2026-11-05-08: DECIDED, wait for the Studio check.
- WWD-2026-11-05-04 and -07: STILL OPEN. Zac chose "Claude checks in Chrome." Studio redirected to a channel-creation page in the Chrome profile (no WWD channel on that login), so it could not be read. Needs Zac to open Studio on the WWD account, or send a screenshot.

## DECISIONS RECORDED 2026-11-12, batch 2 (Zac, picked from a choice list)
- FF-2026-11-11-01: DECIDED, do not promote Moore. Jordan Davis (traded PHI to JAX) is not on bye, so Zac starts him. Lineup unchanged. CLOSED.
- FF-2026-11-11-02: Zac answered "No EC2 is still going." Read as: no new Elimination Challenge, EC2 still running. Whether Zac is still alive in EC2 is not confirmed (he was out as of Week 8). No pick change either way, JAX is already the ATS pick. Closed unless Zac says he is in.
- FF-2026-11-11-03: DECIDED, DFS Week 10 is a Saturday task. Zac gets the salary file then.
- ETSY-2026-11-02-01: Zac said "put it on pause." Read as: no renewal decision now, shop stays on hold, the cap lapses 2026-11-15 as scheduled and is re-set the day a listing batch is planned. Confirm if he meant something else.

## DECISIONS RECORDED 2026-11-12, batch 3 (Zac, picked from a choice list)
- ANIM-2026-11-05-01: DECIDED, gitignore `ANIMATION/training/`. It was already ignored (line 25 of .gitignore) and nothing in it is tracked, verified with git check-ignore and git ls-files. CLOSED.
- VENTURE-2026-11-05-01: DECIDED, drop the Fort Gordon newcomer guide for now. CLOSED.
- ANIM-2026-11-05-02: Zac wants to see the picks list again. Docx re-sent to his phone 2026-11-12. Still OPEN until he answers.
- SW-2026-11-11-01: DECIDED, build the ESPN snapshot too (option A plus the CFBD key already in use). IMPLEMENTED 2026-11-12, softwareb-espn-snapshot. Scheduling needs Zac yes.
- WWD-2026-11-05-02 UPDATE 2026-11-12: Zac reports the Amazon Associates signup is DONE. Bookshop.org signup still to do when a Den Files episode with a book is ready. Needed from Zac: tracking ID and which account, so the disclosure line and link format can be locked. The 180-day, 3-sale clock is running from approval.
- FF-2026-11-10-01: DECIDED, ignore. Tracker closing line for JAX at BAL Week 9 stays as is. CLOSED.
- FF-2026-11-10-02: Lunch with the FanDuel friend was postponed (he got called into something). No notes yet. Revisit when it happens. Leave OPEN, not urgent.
- FF-2026-11-10-03: Zac sends the entered Week 9 lineup Saturday with the Week 10 salary file. OPEN until then.
- FF-2026-11-12-03: DECIDED, backfill Weeks 2, 3, 5 labeled BACKFILL, after the Thursday lock. Needs its own pass because the logger refuses post-kickoff rows. Open task.
- ANIM-2026-11-02-01 (three sign-offs): (1) STANDARDS.md markup, later when animation restarts. (2) Pipeline add-on (xavier150, GPL-3.0), HOLD, nothing installed. (3) Network ports: localhost-only Unreal bridges are fine for agents to enable, anything wider needs Zac's yes each time. Items 1 and 2 stay open as a parked animation restart list, item 3 is a standing rule now. Zac's call 2026-11-12.
- WWD-2026-11-05-04 (Spotify half): ANSWERED by Zac 2026-11-12. No WWD podcast is posted on Spotify yet, so there is no Spotify monetization to check. Spotify ads and Monetize page are moot until the audio-only podcast is back (TASKS: "Bring back audio-only podcast; fix Spotify metadata"). The YouTube Studio Earn tab half is still OPEN, as are -07 and -08.
- KINGDOM PLANNERS: Zac 2026-11-12 ("the back back burner"): moved to ACTIVE-UNSCHEDULED, back burner. Payhip test on ice. No agent, no schedule, not surfaced in planning. Root CLAUDE.md and TASKS.md updated.
- LLC: Zac 2026-11-12: the LLC is Matt's to handle, not Zac's (voice-to-text, which entity was said is not certain, likely the WWD one). No Warrior King Productions LLC until WKP is actually putting product out. TASKS row set to On ice. Open question only if it matters: confirm which entity Matt is forming.
- LLC CONFIRMED 2026-11-12 (Zac): it is the WWD LLC, handled by Matt.
- WWD-2026-11-05-01 UPDATE 2026-11-12 (Zac): Matt gave his YES on both vidIQ and OpusClip. Next per the push packet: copy through the gates (judgment pass, QA, originality and clearance re-read), then the fit poll, then Zac's yes on the exact public post. vidIQ signup (email and PayPal) is Zac's or Matt's action, not an agent's.
- WWD earnings, Zac 2026-11-12: about $4 a month for WWD right now, $0 for WKP. Source is Zac's word, no file. Closes the "no income evidence" question for the monetization plan: baseline is about $4 a month.

---

## [INFRA-2026-11-12-01] 2026-11-12 | Daily rollup | System check YELLOW: three items need Zac's yes

**Context:** `logs\system-check\latest.txt` is YELLOW. (1) WKP-daily-brief is retired but its scheduled task is still enabled. (2) `D:\WKP Reports` (167 deliverables) is not in git and has no second copy. (3) 126 uncommitted changes in the repo. The I: drive disk-event watch continues (no event names I: directly). Adobe stays off limits.
**Options:** A. Approve the disable command, a backup copy of `D:\WKP Reports`, and a commit and push. B. Pick some. C. Leave.
**Recommendation:** A. All reversible, no spend. The backup is the one that matters, since lost deliverables already happened once.

**Status:** OPEN
