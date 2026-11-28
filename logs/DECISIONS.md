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

---

## [ANIM-2026-11-05-02] RESOLVED 2026-11-13 | Zac's answers on the tutorial picks

**Resolution (Zac, 2026-11-13):**
- YES list: S2 (Grant Abbitt, Master Blender Sculpting), L1 (Unreal Sensei, Mesh Terrain landscape), H1 (Ryan King Art, Stylized Low Poly Wooden Cabin), B1 (Blender Guru, private jet, hull method), U1 (Unreal Sensei, UE5 Starter Course 2026, chapters only), U2 (William Faucher, Lighting in Unreal Engine 5 for Beginners).
- NOT on the yes list, so not processed: S1 (Ryan King Art sculpting) and R1 (Ryan King Art retopology). Zac can add them. Retopology and baking have no approved source until then.
- Boat gap: option B. A separate agent searched outside the five channels, report `research\animation\2026-11-13-boat-and-scifi-ship-picks.md`. Boat pick and sci-fi ship picks still need Zac's approval before any caption pull.
- **Boat and sci-fi ship picks answered 2026-11-13 (Zac):** REJECTED BH3, SF4, SF5. APPROVED BH1, BH2, SF1, SF2, SF3. Captions pulled for the five approved (H1 retried, still HTTP 429, not worked around). Tags and delta sheets for the five: `research\animation6-11-13-version-tags-and-delta-sheets.md` section 5.
- Landscape: teach BOTH routes. Experimental Mesh Terrain (L1) and classic Landscape (U1 chapters at 1:56:50 and 2:08:16). L2 not approved.
- Version tagging: "Be sure to tag the version trained on and then find a way to close the gap between the versions." Method written at `ANIMATION\VERSION-GAP-METHOD.md`.
- Caption files for the six approved videos pulled (5 of 6, H1 blocked by HTTP 429 rate limit), saved under `research\animation\transcripts\<id>\`, gitignored.
- Version tags and delta sheets: `research\animation\2026-11-13-version-tags-and-delta-sheets.md`. Docx: `D:\WKP Reports\Animation Tutorial Picks\2026-11-13 - Animation Training Version Tags.docx`.

**Follow-ups still open:** (1) retry H1 captions later. (2) Blender MCP link was down, so Blender UI paths and shortcuts need one live pass in a scratch scene. (3) Enabling Mesh Terrain plugins in Unreal needs Zac's yes at the time. (4) Licenses to read and log: Poliigon files (B1), Sensei downloads (L1, U1), blueprints (B1). (5) DONE 2026-11-13, boat and sci-fi picks answered (see the bullet above). (6) New: licenses to read and log for SF1 texture sources, SF2 and SF3 Gumroad and kitbash downloads, Ucupaint (already on disk, GPL-3.0-or-later, not in the asset log).

**Status:** RESOLVED (picks); follow-ups above open

---

## [ANIM-2026-11-13-01] 2026-11-13 | Daily rollup | Animation research blocked items and no QA on it

**Context:** Animation research jobs ran 2026-11-13. (1) H1 (Ryan King Art cabin) captions hit HTTP 429 twice, not worked around. (2) Blender MCP link was down, so every Blender menu path and shortcut is UI-UNVERIFIED. (3) No qa-director verdict on the version tags and delta sheets. (4) Licenses still unread: Poliigon, Sensei downloads, SF1 to SF3 Gumroad and kitbash files, Ucupaint not in the asset log.
**Options:** A. Let animation-director retry H1 later, run the live Blender pass when the MCP link is up, and send the research to qa-director. B. Skip QA, research only. C. Hold all of it.
**Recommendation:** A. No spend, all reversible. License logging is the one that must happen before any asset is used.

**Status:** OPEN

---

## [INFRA-2026-11-13-01] 2026-11-13 | Daily rollup | Transcription system and Teacher site: unverified, no QA

**Context:** The Transcription (Fiverr) system passed a fake-job test only, no real client audio and no qa-director verdict. Fiverr AI-delivery rules unchecked (Zac's step). The Teacher site was restructured and restyled with no judgment pass or QA on the new index pages, and has not been tried from her phone. Also INFRA-2026-11-12-01 still open: system check is YELLOW again (176 deliverables uncopied, 63 uncommitted changes, WKP-daily-brief task still enabled).
**Options:** A. Run qa-director over the Transcription system and the Teacher index pages, and Zac tests the Teacher link from her phone. B. Wait until real jobs exist. C. Leave.
**Recommendation:** A, plus approve INFRA-2026-11-12-01 option A. The backup of D:\WKP Reports is the one that matters.

**Status:** OPEN

## TEACHER-2026-11-14-QA-01 (qa-director)
**Decision needed:** Which paid Claude plan will Zac's wife have, which computer (Windows or Mac), and may the course teach connecting her real accounts or made-up ones only?
**Context:** QA of the power-tools drafts. Skills Task 3 (custom upload) and the safe-tools lesson depend on it. Anthropic pages disagree on whether free plans can upload custom Skills. Drafts currently assume paid and keep all practice on made-up material.
**Options:** A. Name the plan and OS, keep practice made-up only. B. Teach real connections with Zac's explicit list of accounts. C. Keep everything free-safe until she is on paid.
**Recommendation:** A.

**Status:** OPEN

- TEACHER-2026-11-14-QA-01 ANSWERED by Zac 2026-11-14: plan Pro, Mac, real accounts allowed ("I believe"), read-only first with approvals.

## [INFRA-2026-11-16-01] 2026-11-16 | Daily rollup | Monday brief and Saturday wrap tasks returned nonzero
**Decision needed:** Look into why WKP-Monday-Brief (last run 11/16 05:30) and WKP-Saturday-Wrap (last run 11/14 05:30) both ended with result 1, and whether the .docx files were made.
**Context:** logs\system-check\2026-11-16.md, scheduled tasks section. Not investigated, rollup does not start new work. The Saturday wrap was registered only on Zac's yes, so this may be a task-setup issue or the skill failing.
**Options:** A. Have software-director read the task logs and the two skill specs and report the cause. B. Zac checks D:\WKP Reports\Monday Brief and Saturday Wrap for a file first. C. Leave.
**Recommendation:** B first (30 seconds), then A only if the files are missing.

**Status:** OPEN

## [POST-2026-11-16-01] 2026-11-16 | Post-Production | Ian trailer: push into the cover past 100 percent?
**Decision needed:** Draft 3.2 Section 6 says never push in on the cover past 100. The cover opener needs a view-only push toward the car grille (never the toddler) to match clip V2. The artwork file is never changed.
**Options:** A. Yes, view-only push. B. No, hold the cover and dip to black into V2 (strict fallback in the plan).
**Recommendation:** A. DECISION QUEUED. Plan: `Post-Production\reports\Ian-Trailer-Asset-Review-and-Cover-Opener-2026-11-16.md` Section 3.
**Status:** CLOSED 2026-11-19 (moot), settled by Zac 2026-11-17 per `memory\project-ian-trailer-settled.md`: "The cover is NOT the trailer opener. It is its own 9:16 Facebook or Instagram story piece: garage door opens, man comes home, the cover comes alive into the man working on the car." No cover push opens the trailer.

## [POST-2026-11-16-02] 2026-11-16 | Post-Production | Ian trailer: animate the cover artwork by splitting it into layers?
**Decision needed:** Cutting the car, man and toddler out of the cover to move them alters Ian's cover, singles out the toddler, needs Ian's OK and may need credits.
**Recommendation:** NO. DECISION QUEUED.
**Status:** CLOSED 2026-11-19, settled by Zac 2026-11-17 per `memory\project-ian-trailer-settled.md`: the cover is its own story piece where "the cover comes alive into the man working on the car", and "No Veo or Firefly credits left. Work from what is on disk." Built as the 9:16 cover story animatic from what is on disk; no credits.

## [POST-2026-11-16-03] 2026-11-16 | Post-Production | Ian trailer: make wide stills R1w and R5w in Firefly?
**Decision needed:** R1, R3, R5 are vertical only, 768 px wide. In 16:9 they show as strips. Credit cost per image run NOT RETRIEVED.
**Recommendation:** Try the blur-sides frame in the rough cut first, decide after Zac sees it. DECISION QUEUED.
**Status:** CLOSED 2026-11-19, settled by Zac 2026-11-17 per `memory\project-ian-trailer-settled.md`: "No Veo or Firefly credits left. Work from what is on disk." No wide stills get made; blur-sides framing is the route.

## [WWD-2026-11-17-01] 2026-11-17 | market-research | VidIQ go-ahead for the retention pull
**Decision needed:** Zac's explicit yes to spend VidIQ credits on a fresh WWD pull (per-video retention, traffic sources, outliers, competitor review channels).
**Context:** The retention plan was built from existing pulls (2026-11-02, 2026-11-13, 2026-10-26). An agent's request is not Zac's consent, so no VidIQ tool was called. Retention curves and click-through rate were never in those pulls. Studio (free) shows curves and Earn tab status.
**Options:** A. Zac reads Studio retention for the last 6 reviews and the Earn tab, no credits. B. Zac okays a VidIQ pull with a credit cap. C. Both.
**Recommendation:** A first.
**Status:** OPEN. Plan: `WWD\reports\WWD-Retention-Plan-2026-11-17.md`

## [ORG-2026-11-17-01] 2026-11-17 | org gap audit | Pilot the agent self-improvement loop?
**Decision needed:** Zac's yes to pilot the loop in `reports\Skills-Repos-and-Limits-2026-11-16.md` Part C (after-order note, 8-question self-test, lessons to `memory\topics\lessons\<agent>.md`, director review, Ares weekly review) on a few agents first.
**Context:** Zac asked for agents that get better each run (2026-11-16, 2026-11-17). Not built: the proposal says it needs his yes. chief-of-staff only lists lessons, it does not start the loop.
**Options:** A. Pilot on 3 agents (trading-researcher, channel-researcher, one WWD bench). B. Hold. C. Roll to all.
**Recommendation:** A.
**Status:** CLOSED 2026-11-19. Zac ordered it on 2026-11-19: "formalise everything... agents are supposed to learn." The system reset of 2026-11-19 put the loop in place for ALL agents (option C, not a pilot): one lessons file per agent in `memory\agents\` (63 files), every spec has a "Memory and learning" section (read lessons before a job, write one after), same-mistake-twice rule fixes the spec the same day, protocol in `SOP\SOP-Agent-Memory-and-Learning.md`. Path is `memory\agents\<agent>.md`, not the proposal's `memory\topics\lessons\`.

## [ORG-2026-11-17-02] 2026-11-17 | org gap audit | Install last30days (and claude-hud)?
**Decision needed:** Zac said "a hard yes" to last30days on 2026-11-16. Installing runs third-party code, so the install commands in report section A7 need his go. claude-hud is ADOPT in the same report, no yes on record.
**Context:** Org chart shelf 3 lists last30days as approved, not installed.
**Options:** A. Install both after the A6 pre-install checks. B. last30days only. C. Wait.
**Recommendation:** B.
**Status:** last30days part DONE 2026-11-17 (Zac's direct yes, installed as a skill by copy at commit a854f3bc, vet note `reports\2026-11-17-last30days-vet.md`, rules in `.claude\skills\last30days\README-WKP.md`). claude-hud part DONE 2026-11-17 (Zac's direct yes, vetted CLEAN, plugin pinned at commit 9d2b6fa, statusLine added to user settings.json with backup, auto-update off, no --extra-cmd; vet note and undo steps in `reports6-11-17-claude-hud-vet.md`). Zac only needs to start a new session to see it. ORG-2026-11-17-02 is fully closed.

---

## [INFRA-2026-11-18-01] 2026-11-18 | Nightly rollup | The rollup's own stored scheduled-task prompt is out of date against current venture status

**Blocked:** Tonight's nightly rollup prompt (the stored instructions this scheduled task fires) states step 5 as: "MAIN EFFORT is Kingdom Planners; ACTIVE ventures are WWD/FrostCast, Shattered Empire, Cyber Security, WarriorKingDesigns." Root `CLAUDE.md` as it stands tonight says the opposite on both counts: "MAIN EFFORT: none set. Kingdom Planners was removed as main effort 2026-11-11 (Zac's call)," and ACTIVE is "WWD/FrostCast, Shattered Empire, WarriorKingDesigns (triage complete, hold)" with Cyber Security under ACTIVE-UNSCHEDULED (CySA+ punted 2026-11-12, already closed in CS-2026-10-28-01 above). Both of those venture-status changes are themselves already decided and logged (see the KINGDOM PLANNERS and CS-2026-10-28-01 entries above, both 2026-11-12). The scheduled task's stored prompt was evidently written before those calls and never updated, so every future nightly run risks misreading which ventures to surface or suppress unless whoever reads this rollup's output catches the mismatch by hand, as done tonight. I have no tool to edit a scheduled task's stored prompt from inside a read-only rollup run.
**Options:** A. Zac (or chief-of-staff, next session) updates the nightly-rollup scheduled task's stored prompt to reference current CLAUDE.md venture status by name, or better, to say "read venture status fresh from root CLAUDE.md each run" instead of hardcoding a venture list that will drift again. B. Leave it — tonight's run caught the drift and followed the live CLAUDE.md instead of the stale prompt, so no harm was done this cycle. C. Ignore, re-check manually each night.
**Recommendation:** A (the "read it fresh" phrasing specifically, so this exact drift can't recur) — cheap, one-time, prevents a repeat of tonight's silent-mismatch risk on every future rollup.

**Status:** OPEN

---

## [PHOTO-2026-11-19-01] 2026-11-19 | Nightly rollup | Photo Restore side income: stop rule (Fri 11/13) is 6 days overdue, no record either way

**Blocked:** TASKS.md's "Photo restore (side income, first)" row still reads "Stop rule Fri 11/13 | In Progress | Zac: groups list with member counts and selling rules by 11/13 or it stops. Also 3-photo quality test, Photoshop practice photo, timed EP 89 transcript check, payment app, names, Firefly backgrounds yes/no." Today is 2026-11-19, six days past that deadline. `git log` shows the repo was essentially quiet in that window (no commits 2026-11-13 to 2026-11-15, nothing substantive 2026-11-17 evening through tonight) — no groups list, quality test, payment app, names or Firefly yes/no appear to have landed (checked for new commits/files only, not confirmed negative beyond that, per the Honesty rule). Nothing in `logs\DECISIONS.md` or `memory\MEMORY.md` addresses whether the stop rule actually triggered, was met some other way (text/voice to Zac that never made it into a file), or was waived. This is Zac's own stated rule for this venture, so whether it stops or continues is not mine to decide.

**Options:**
A. Treat the rule as triggered — the venture stops as of 11/13 until Zac explicitly restarts it with the missing pieces (groups list, selling rules, payment app, names, Firefly yes/no).
B. Zac confirms the groups list/selling rules were supplied some other way that never made it into a file, and the venture continues — needs that confirmation captured in TASKS.md or memory.
C. Zac extends the deadline.

**Recommendation:** A by default, since nothing on file shows the rule was met, but this is Zac's rule to enforce or waive, not an agent's call — flagging rather than assuming either way.

**Status:** OPEN

## [WWD-2026-11-18-01] 2026-11-18 | Nightly rollup (from wwd-director log) | FrostCast EP 121 transcript not yet delivered to Matt

**Blocked:** Step 6 of the FrostCast Transcription Workflow (send the full transcript .txt to Matt over Facebook Messenger) was NOT done. The wwd-director run had no claude-in-chrome tools, so it could not use Zac's logged-in Facebook session. The Composio Facebook API route is a known dead end (public URL only). Transcript path: `L:\Winter Wolfs Den review show\Frost-Cast\EP 121\The name_s Edwa-- er Bond _ Snyderverse 2_0 _ FrostCast Episode _121_transcript.txt`. Only the log was read, delivery to Matt not confirmed either way.
**Options:** A. Main session (Jarvis) runs the Messenger send next session where the Chrome tool is available, screenshots "Sent" with the filename before reporting done. B. Zac sends it himself. C. Gmail attachment as a one-off (email is retired for this step, so needs Zac's yes).
**Recommendation:** A.

**Status:** OPEN

## WWD-2026-11-19-01 - Attorney question: blacked-out Movieclips logo bar (A Knight's Tale)
**Raised by:** wwd-rights, 2026-11-19
**Question for an attorney (not a guess):** For the A Knight's Tale review, five muted clips of 6.4 to 8.0 s each (35.08 s total, re-cut 2026-11-19 under Zac's new rule; first cut was under 4 s each, 19.14 s) come from Movieclips YouTube uploads. The uploader logo sits in the letterbox bar under the picture and was blacked out in our copies; the picture is untouched. Does covering an uploader's channel logo on short commentary clips raise any copyright-management-information risk, and does it matter for a fair use position?
**Cost to ask:** unknown. **Blocks:** nothing, edit can proceed. Risk read in `WWD\reports\A-Knights-Tale-Rights-Note.md`.
**Status:** OPEN

## WWD-2026-11-19-02 - ElevenLabs Music generation for A Knight's Tale intro and outro (spend)
**Raised by:** music, 2026-11-19
**Question:** May the A Knight's Tale intro (12 s) and outro (18 s) be generated in ElevenLabs Music (music_v2_5), and which ElevenLabs plan is Zac on? Free plan cannot download and needs attribution; Starter and up can download, no attribution. Prompts ready in `reports\music-stomp-clap-prompt-2026-11-19.md`.
**Cost:** credits per generation, exact figure not retrieved. **Blocks:** the new intro and outro only. Owned fallback named in the same file.
**Status:** OPEN

---

## READINESS PASS 2026-11-19 (Jarvis closing agent): triage of every open row

Rule used: only money, public posting or a preference only Zac holds goes to Zac. Everything else was decided by the owning director or Jarvis and is logged here. Zac's short list: `reports\2026-11-19-Decisions-Triage.md`.

- POST-2026-11-11-01, CS-2026-10-28-01, INFRA-2026-11-11-01, ORG-2026-11-17-02, FF-2026-11-12-01, FF-2026-11-12-02, SW-2026-11-11-01, ANIM-2026-11-05-02 (picks): already closed in their own rows. No change.
- ORG-2026-11-17-01, POST-2026-11-16-01, -02, -03: CLOSED in their rows today (see above).
- FF-2026-11-10-01: CLOSED (Zac 2026-11-12, "ignore", batch 3).
- FF-2026-11-10-03: CLOSED, stale (fantasy-football-director). Week 9 is three weeks past; the DFS comparison keeps the one reconciled lineup (option B). Reopen only if Zac sends the entered lineup.
- FF-2026-11-11-01, -02, -03: CLOSED (Zac 2026-11-12, batch 2).
- FF-2026-11-12-03: DECIDED by Zac 2026-11-12, now a task (TASKS Personal, tracker backfill). Not a decision any more.
- FF-2026-11-10-02: PARKED, not a decision. Notes exist only when the FanDuel lunch happens. Zac mentions it if it does.
- ETSY-2026-11-02-01: CLOSED. Zac said "put it on pause" 2026-11-12; the cap lapsed 2026-11-15 as scheduled; etsy-director sets a new cap the day a listing batch is planned.
- WWD-2026-10-27-01: CLOSED, superseded (wwd-director). Vision Quest EP 7 is uploaded and EP 8 is in release; the eps 3 and 4 card and sheet questions are past.
- PAWS-2026-10-31-01: CLOSED (visibility flag only). PAWS is paused (Zac 2026-11-12); PAWS-001 and PAWS-004 live in `PAWS\decisions\DECISIONS.md`.
- ANIM-2026-11-02-01: CLOSED (Zac 2026-11-12, batch 3): STANDARDS markup and pipeline add-on parked for the animation restart, port rule is a standing rule.
- ANIM-2026-11-05-01: CLOSED (Zac 2026-11-12, already gitignored).
- ANIM-2026-11-13-01: DECIDED A (animation-director): retry H1 captions later, live Blender pass when the MCP link is up, licenses logged before any asset is used, qa-director over the research. Task, no spend.
- VENTURE-2026-11-03-01: CLOSED. The day-job outside-work check is settled (Zac 2026-11-10, `memory\project-day-job-outside-work-cleared.md`, "do not ask again"). The CMMC kit itself stays On ice in TASKS (market not shown).
- VENTURE-2026-11-05-01: CLOSED (Zac 2026-11-12, dropped).
- WWD-2026-11-05-02, -03, -05, -06, -08: CLOSED (Zac 2026-11-12, batch 1). The open action from -02 (Amazon tracking ID) is a TASKS row.
- WWD-2026-11-05-01: CLOSED as a decision (Matt said yes 2026-11-12). Remaining steps run through marketing-director; the vidIQ signup is Zac's or Matt's account action and any public post is Zac's yes.
- WWD-2026-11-05-04 (Earn tab half), -07 (Shopping tab) and WWD-2026-11-17-01 option A: MERGED into one free Zac look at YouTube Studio (optional, not blocking). The VidIQ credit pull (option B) stays a money item.
- TEACHER-2026-11-14-QA-01: CLOSED (Zac answered 2026-11-14: Pro, Mac, real accounts, read-only first).
- INFRA-2026-11-12-01: DECIDED by Jarvis (reversible, no spend, consistent with Zac retiring the daily brief 2026-11-12): (1) disable the WKP-daily-brief task, (2) additive copy of `D:\WKP Reports` (276 files, 28.5 MB, measured 2026-11-19) to `L:\WKP Reports Backup`, (3) commit locally, push stays Zac's. Steps 1 and 2 were attempted 2026-11-19 and BLOCKED by the permission classifier, not run. Exact commands are on Zac's list. The task is still Ready, last result 1 on 11/19 05:30 (checked).
- INFRA-2026-11-13-01: DECIDED A (Jarvis): qa-director over the Transcription system and the Teacher index pages next session; the phone test is her call. TASKS rows.
- INFRA-2026-11-16-01: DECIDED (Jarvis): the Monday Brief 11/16 .docx exists although the task returned 1; the Saturday Wrap 11/14 made no file (its folder did not exist until 2026-11-19). software-director reads the task setup and the skill and reports the cause before Sat 11/21 05:30. TASKS row.
- INFRA-2026-11-18-01: DECIDED A (Jarvis): the rollup's stored prompt is not on this machine (searched the repo and ~/.claude). chief-of-staff checks the cloud routine list with the schedule skill next session and changes the prompt to "read venture status fresh from root CLAUDE.md each run". Not Zac's.
- PHOTO-2026-11-19-01: DECIDED by Zac's own rule as written ("by 11/13 or it stops"): Photo restore is STOPPED as of 2026-11-13 and restarts only when Zac says so. One line to Zac, not a question.
- WWD-2026-11-18-01: DECIDED A (wwd-director): Jarvis runs the Messenger send to Matt as the first job of the next session with the Chrome tool and screenshots "Sent" with the filename. Staged in `SOP\SOP-Session-Start-Checklist.md`.
- WWD-2026-11-19-01: ON ZAC'S LIST (attorney cost). Does not block the edit.
- WWD-2026-11-19-02: ON ZAC'S LIST (credits). Note: the prompt file still says a 12 s intro. Zac locked intros at 6 s or less on 2026-11-19 (`memory\feedback-intro-length.md`) and prefers one generation cut into intro and outro, so the ask is ONE ElevenLabs Music generation of the 60 s "Long build" prompt in `reports\music-stomp-clap-prompt-2026-11-19.md`, cut to an intro of 6 s or less and an outro. Credit cost not retrieved. A free owned fallback exists.

## ZAC ANSWERS 2026-11-19 (verification notes)
- INFRA-2026-11-16-01: CLOSED. Cause is no tokens when the Monday brief and Saturday wrap tasks ran (Zac). Not a task setup bug. Same family as the 2026-11-09 missed brief in root CLAUDE.md: acceptable, do not alert-engineer.
- WWD-2026-11-19-02: still OPEN as a spend ask, now with the plan facts. ElevenLabs has a free tier, but downloading the music likely needs the $11 package (Starter) (Zac). Not approved. Owned fallback stays in use until Zac says buy.
- Percy Jackson confirmed as the next Next Up card.
- Vision Quest EP 8 is live. Shorts and social posts not done yet.

## [WWD-2026-11-19-03] 2026-11-19 | Nightly rollup (from wwd-director log) | A Knight's Tale on-air errors: cut, keep or correct
**Blocked:** The wwd-director flags list (2026-11-19 21:25 entry) names on-air errors in the transcript (Colville is Prince Edward per fact-research but the hosts disagree, 1999, $244M, "Heelan", "Shannon Lord", runtime "hour and 29") and asks Zac to cut, keep or correct each. Not queued before tonight, so the edit could go out with them.
**Recommendation:** A. Zac rules each one while he edits (they are his words on air). Per the zero-question rule on-air chat answers are context, but these are facts in a public video. Brief: `D:\WKP\scratch\akt\facts.md`.
**Status:** OPEN

## [DENFILES-2026-11-22-01] 2026-11-22 | script-room | Den Files EP 1: Rogers death and Pierce on-air call, and P10 ruling for Segment 7
**Blocked:** Mike Rogers is REPORTED dead (Feb 6, 2026), UNCONFIRMED: skeptic blogs only, no obituary found. A secondhand disputed deathbed claim and Steve Pierce's Aug 2026 statement exist. P47, P91, P115, P145, P172 to P180, P187 to P191, P199, P200, P206, P212, P213 all speak as if nothing happened after 2021. Separately P10 reserves calls for Winter Wolf while P61 promises both hosts say where they land.
**Recommendation:** Rule before recording tonight (7:30 PM), owner Zac. Rogers: option 1 acknowledge (site A end of Segment 5 Piece 5 after P178, attributed, reported and unconfirmed), option 2 date the record once on air, or option 3 two takes of that passage only. P10: bend in Segment 7 so each host says where he lands, or narrow the P61 promise. Detail: `Post-Production\writing-room\den-files-ep1\suggested-changes-v2.md` Section 1 items 4 and 6.
**Status:** OPEN

## TRADING (trading-director, 2026-11-26)
- TRADING-2026-11-26-01: DECIDED by Zac 2026-11-26 (relayed in the job brief): paper watch week on the Alpaca Trading API, paper account, NOT the Broker API. Closes the Robinhood versus Alpaca open item. Stock data from Alpaca market data (IEX feed on the free account, SIP denied, checked 2026-11-26) replaces yfinance. Robinhood stays Zac's manual execution venue. Plan `Investing\watch-week\WATCH-WEEK-PLAN.md`.
- TRADING-2026-11-26-02: CLOSED 2026-11-27. Zac in chat: "yes on paper, I have said yes this is the third time." The four-week paper watch week may run while Investing stays DORMANT (standing exception, paper only). Never ask again. (closed by trading-director on coordinator relay)
- TRADING-2026-11-26-03: OPEN, optional, not blocking. Default NO: the watch week logs paper trades in our own files and makes read-only Alpaca calls only. If Zac wants paper orders sent to Alpaca's paper account too, he says so in writing and the spec is updated first.
- TRADING-2026-11-26-04: OPEN, not blocking the watch week. Which broker executes LIVE stocks later: Robinhood (Investing\CLAUDE.md, manual, fractional) or Alpaca (locked rules)? Recommendation: decide only at the go-live gate; judge paper results on the "Zac can act" ledger either way.

## [TOOLS-2026-11-26-01] 2026-11-26 | chief-of-staff | Spec tool-list fixes from the tool-gap audit (needs Jarvis, specs are outside chief-of-staff authority)
**Blocked:** Audit `SOP\leveling\tool-gap-audit-2026-11-26.md`. Gap 1: wwd-pictures spec has no claude-in-chrome tool though its skill needs it (SKILL.md L37 to L39), so the PJ S3 follow-up never tried IMDb or TV Insider. Gap 2: script-room and room-writer have no Bash for slop_check. Gap 3: clearance and originality have no WebFetch. Gap 4: wwd-clip-scout spec L20 says no downloads but its lesson uses yt-dlp for captions (rule wording). Gap 5: 33 specs lack WebFetch, run leveling Step 1 through general-purpose.
**Recommendation:** Jarvis edits the specs (1 to 4) in one change at a time, then launches wwd-pictures once to call `list_connected_browsers` ($0) to prove the tool reaches a subagent. Not a Zac decision unless Jarvis wants him in.
**Status:** OPEN (owner Jarvis)

## [LEVEL-2026-11-26-01] 2026-11-26 | chief-of-staff | Wave 1 failure entries that need credits to close
**Blocked:** graphic-design (3 entries) and wwd-vfx (joust sting) stay OPEN until a live generation of the redesigned shot succeeds (`memory\agents\failures\graphic-design.md`, `wwd-vfx.md`). A live run spends Firefly or Veo credits. Cost per generation NOT RETRIEVED. Zac's credit balance and reset date NOT GIVEN (TASKS "Firefly credits refilled" row).
**Recommendation:** Do nothing until Zac names a credit budget. When he does, graphic-design shows the exact cost at the Generate button, runs the cheapest test first (one still, not a clip), and qa-director grades the result. Until then the entries stay OPEN and the agents carry UNDRILLED on credit work.
**Status:** OPEN (needs Zac: spend)
- TRADING-2026-11-26-05: OPEN, not blocking. Spec rename: record "FAWN FOREST INVESTMENTS" in `.claude\agents\trading-director.md` (and the trader-* skills if wanted). Recorded on the board and plan only, because an agent message cannot authorize a spec edit. Needs a one-line yes from Zac or Jarvis.

- TRADING-2026-11-26-06 (crypto Q1, 05 was already taken): OPEN, blocks build step 2. Code layout. Recommendation: copy the pure stock modules with a parity test now, extract a shared library after both watchers have 50 counted trades. Source: software\wkt-crypto-watcher\DESIGN.md section 13.
- TRADING-2026-11-26-07 (Q2): OPEN. Bar settle setting in the frozen config. Recommendation: 60 minutes for the first count, measure candle revisions in Phase A.
- TRADING-2026-11-26-08 (Q3): OPEN. Weekend rule. Recommendation: weekend and overnight entries only at score 90+, plus 20 bps extra haircut and a 10 bps spread limit. Alternative: block them. Needs Zac.
- TRADING-2026-11-26-09 (Q4): OPEN. Day and week boundary. Recommendation: ET midnight, week starts Monday 00:00 ET.
- TRADING-2026-11-26-10 (Q5): OPEN. Monday watch-day for crypto. Recommendation: carry it over (Monday ET, score 90+ only).
- TRADING-2026-11-26-11 (Q6): OPEN. Universe. Recommendation: frozen list of about 12 liquid USD pairs, reviewed monthly, change = config change. Locked rule "scan the whole list" conflicts with a frozen config. Needs Zac.
- TRADING-2026-11-26-12 (Q7): OPEN. Correlation limits. Recommendation: total open risk cap 4 percent, max 2 correlated alts, tiered position caps 25/15/10 percent, placeholders.
- TRADING-2026-11-26-13 (Q8): OPEN, blocks build. Zac-can-act windows. Recommendation: 12:00 to 13:00 and 18:00 to 21:00 ET. Zac confirms real times and whether lunch entries are possible.
- TRADING-2026-11-26-14 (Q9): OPEN, blocks build, Zac, 5 minutes, no order placed. Open the Robinhood crypto order screen and report: stop or stop-limit on crypto possible, resting limit sell possible, minimum order and quantity increment, fee or spread shown in the preview of a small BTC buy.
- TRADING-2026-11-26-15 (Q10): OPEN. Phase B Robinhood spread measurement. Recommendation: defer until Phase A has two clean weeks. If yes, Zac creates a read-only key himself (ROBINHOOD_CRYPTO_API_KEY, ROBINHOOD_CRYPTO_PRIVATE_KEY), no agent sees it.
- TRADING-2026-11-26-16 (Q11): OPEN. Terms of use for Coinbase (403 to our fetch) and Kraken unread. Recommendation: trading-researcher reads them by another route before the counted run; keep call rate low.
- TRADING-2026-11-26-17 (Q12): OPEN. Haircut labels. Recommendation: main 15 bps, Zac ledger 30 bps, ladder 5/15/30/50/100 plus Robinhood 2 percent scenario, all placeholders, 50+ labeled STRESS, pass line is Zac ledger at 30.
- TRADING-2026-11-26-18 (Q13): OPEN. Simulated account size. Recommendation: 100000 for percent-based ledgers plus the $60 view on the Zac ledger.
- TRADING-2026-11-26-19 (Q14): OPEN, for trading-director, before Mon 2026-11-30. Design author's read of the stock watcher code: it counts all fresh evaluations (not "score 70+ once per setup") and shows no config hash or weekly cap on log lines. Confirm and fix or correct the read.
- TRADING-2026-11-26-20 (Q15): OPEN, later. Memecoin guide test. Recommendation: trading-researcher first writes its rules as a fixed rule set; drop if not testable; listed coins only.
- TRADING-2026-11-26-21 (Q16): OPEN, blocks build, Zac. Does the PC run 24/7? If not, accept logged OFFLINE gaps and count only fully watched stretches.
- TRADING-2026-11-26-22 (Q17): OPEN, blocks build, Zac. Investing is DORMANT. Recommendation: cover the crypto watcher with the same standing exception as the stock watch week, in his own words.
- TRADING-2026-11-26-23 (Q18): OPEN. Real-money crypto test. Recommendation: NO, outside this design, needs a written decision and his own config.
- TRADING-2026-11-26-24 (Q19): OPEN. First frozen config. Recommendation: step-up OFF, regime size multipliers 1.0, regime logged only.
- TRADING-2026-11-26-25 (Q20): OPEN. PDT for crypto. Recommendation: Zac checks Robinhood's crypto trading rules page; no PDT counter until then.
- TRADING-2026-11-26-26: OPEN. Crypto design ruled GO WITH CHANGES. Zac-only item: preview a small BTC buy in the Robinhood app three times on different days, NO order placed, note price vs Coinbase ticker, default order type, whether stop orders exist. Not blocking the stock watch week.
- TRADING-2026-11-26-27 (insider scanner, trading-director): OPEN, blocks only the LIVE SEC pull, not the build. SEC fair access asks every automated client to declare a User-Agent with a company name and contact email. Zac sets the user environment variable SEC_USER_AGENT himself (example shape: "<company or app name> <contact email>"), in his own config. No agent types or stores it; the tool reads it by name and refuses to run if unset. Recommendation: use a generic app name plus an email he is fine with SEC seeing. Until set, only the offline demo and tests run.
- TRADING-2026-11-26-28 (insider scanner, trading-director): OPEN, not blocking. Cover the insider scanner under the same standing exception as the stock watch week while Investing is DORMANT (see -02), paper only, data only, no orders. Recommendation: yes, in his own words. Also: OpenInsider terms on automated use are unread, so the tool uses SEC data only; Jarvis may open OpenInsider by hand in Zac's browser as a cross-check.
- TRADING-2026-11-26-29 (trading-researcher, Rule One docs): OPEN, not blocking. Zac's course files never define the sticker price formula, the margin of safety rule or the Big Five; they point to the Rule One Toolbox calculator. To rebuild the stock method for paper design we need the formula from a source Zac owns (book chapter or Toolbox screenshot) or fact-research pulling it from a published source. Recommendation: Zac drops the page or screenshot in `D:\Documents\Rule 1 Documents\`, or says go to fact-research.
- TRADING-2026-11-26-30 (trading-researcher): OPEN, not blocking. Scope: add a paper-only Rule One options design track (Stages 0 to 3 in `Investing\research\rule-one-from-zacs-documents-2026-11-26.md`) under the same standing exception as the watch week, as a separate folder and config, no change to the stock watcher. Recommendation: yes, Stage 1 design doc first, then devils-advocate.
- TRADING-2026-11-26-31 (trading-researcher): OPEN, not blocking. $500 fit: RUT 5-point spread risks about $470 (94 percent of $500), 10-point about $957. Does Zac want the design to study a smaller underlying (XSP or ETF options) as a new design, clearly labelled not Rule One as documented? Recommendation: yes on paper only; also Zac reads Robinhood's options collateral and fee pages himself before any real step.

## DECISION QUEUED: FFDASH-2026-11-27-01 (software-director)
Fawn Forest dashboard on Zac's phone. It runs on the PC only (localhost). Seeing it on the phone needs a private link (Tailscale, free, install status NOT VERIFIED). Options: A) leave PC-only for now. B) Zac sets up Tailscale serve (no money, private to his devices, never public). Recommendation: A until the watch week starts, then B. Blocked: nothing.

## DECISION QUEUED: FFDASH-2026-11-27-02 (software-director)
Go-live checklist file `software\fawn-forest-dashboard\data\go-live-checklist.json` holds 0 of 7 as Zac said. Items 4 to 6 may be true in fact (security pass, demo proof, devils-advocate rulings exist). trading-director should sign each item PASS by hand when it is satisfied. Blocked: nothing.

## DECISIONS QUEUED 2026-11-27 (software-director, insider scanner v0.2.0, order from trading-director)
- TRADING-2026-11-26-32 (insider scanner, software-director): OPEN, blocks the first counted cluster, not the build. Confirm the ONE primary horizon in `wkt-insider-scanner\config.yaml` (`primary_test.horizon_trading_days`). I picked 5 trading days because it fits the locked 5-day time stop of the stock rules, so a pass would not need a longer hold. 20 days matches the published literature but a pass at 20 needs a locked-rule change from Zac. Changing it later is a config reset (K7 counts resets). Recommendation: keep 5.
- TRADING-2026-11-26-33 (insider scanner, software-director): OPEN, blocks the first counted cluster. Confirm or move the freeze time `freeze.counted_signals_from_et` (placeholder 2026-11-28T00:00:00 ET) at the moment trading-director writes `LIVE-OK.flag`. Only clusters signaled after it count, and nothing from the 2026-11-26 OpenInsider pull can. Also confirm the K1 reading (binding benchmark: the smaller of the mean and median excess against SPY and IWM). Recommendation: set the freeze to the evening of the LIVE-OK day.
- TRADING-2026-11-26-34 (insider scanner, software-director): OPEN, not blocking. Bid and ask are not available: the stock watcher read-only client whitelist has no quotes path and the scanner may not edit the watcher. Every cluster therefore costs the 30 bps floor (`spread_unmeasured`) and fills are FILL_UNKNOWN, so kill criteria K2 and K3 cannot be fully checked. Ask the watcher owner to add `/v2/stocks/quotes` (GET, feed=iex) to its whitelist, or accept the floor. Recommendation: add it after the stock watch week scorecard.
- TRADING-2026-11-26-35 (insider scanner, software-director): OPEN, not blocking. Before a backtest is built: pick the quarters (suggested every complete quarter from 2016 Q1) and who writes the dated pre-registration file before any run (`docs\BACKTEST-DESIGN.md`). The ruling gates all building on the stock watch week first scorecard passing qa-claims and Zac setting `SEC_USER_AGENT` (TRADING-2026-11-26-27). Recommendation: trading-director writes it, nothing built until both gates clear.
- TRADING-2026-11-26-36 (stock watcher, software-director, 2026-11-27): OPEN, not blocking the paper run. (a) PDT overshoot S4 is LABELED not fixed ("Zac ledger not go-live evidence until fixed"); a real fix changes entry counts and restarts counts under a new hash, trading-director picks when. (b) MAIN ledger entries can still fill at the 09:00 bar open (pre-open prints) after an overnight signal; only the Zac ledger entry and time-stop exits moved to the 10:00 open. Say if main should move too (one config-driven change, new hash). (c) Alpaca /v2/calendar is not whitelisted, so the 12-24 end day was verified on nyse.com not Alpaca.
- TRADING-2026-11-26-37 (insider scanner, software-director, from software-tester F1): OPEN, BLOCKS LIVE-OK.flag. clusters.jsonl is append-only, so a cluster that a later 4/A removes, or whose id changes (id uses the first trade date), keeps counting and --score would score it. Fix needed before any live run: stable cluster id plus a RETRACTED line when a re-run no longer produces the cluster. Also open from tester and QA (docs\TESTER-REPORT-2026-11-27.md, docs\QA-REPORT-2026-11-27.md): F4 UTC offset in acceptance time ignored, F5 missing exit-day bar not counted as MISSING, F6 same-day 4/A sort order on the dataset route, F7 offering word list gaps, F8 config validation gaps, QA N1 (status and type use filings accepted after the signal), and verify one real acceptance timestamp against timing.accepted_tz. Recommendation: order a v0.2.1 fix round for F1 first, then F4 to F8, before LIVE-OK. [renumbered from -36 by trading-director 2026-11-27: -36 was used twice, -36 stays with the stock watcher PDT/calendar item]

- TRADING-2026-11-26-38 (stock watcher, software-director, 2026-11-27): OPEN, not blocking the paper run. Items 36(a) and 36(b) are now DONE in code: PDT guard counts same-day open entries (S4 fixed, scorecard label removed) and the MAIN ledger entry fills at the 10:00 ET bar open. Both changed behavior while config.yaml stayed untouched, so the config hash is still 7a0c25c7a871b79b. Needs Zac or trading-director: (a) confirm the four-week counts start with THIS code (no counted run exists yet, GO-COUNTED.flag not created, so no counts restart); any later code or config change after GO-COUNTED should restart the counts under a new hash. (b) The new PDT guard is deliberately conservative (an entry opened today counts as a possible day trade, so it can refuse an entry that would never have been day-traded); the FINRA/Robinhood rule text is still NOT confirmed, say if you want it looser. (c) Tester and QA verdicts are in D:\WKP\logs\qa\2026-11-27-wkt-alpaca-watcher-tester-pass3.md and -qa-pass3.md.
- TRADING-2026-11-26-39 (stock watcher, software-director, 2026-11-27, from software-tester F1 and F2): OPEN, not blocking the paper run. F1 (medium): the PDT guard uses the scan date, not the fill-bar date, so after an outage or restart that spans the 10:00 hour, backfilled same-day fills are not counted and the Zac ledger could exceed 3 day trades. Normal live running is safe. F2 (medium): Zac-ledger pending signals never expire and the Zac ledger has no gap cancel (zac_ledger.max_gap_atr null), so a stale signal can fill days later. Fix order needed from trading-director BEFORE GO-COUNTED.flag if you want them closed, since any code change after GO-COUNTED restarts the counts. QA pass3 notes: nothing logs the code hash into config-history, so a code edit during the four weeks goes unnoticed unless CODE-SHA256.txt is rechecked.
- TRADING-2026-11-26-40 (stock watcher, software-director, 2026-11-27): DECISION QUEUED, not blocking the paper run. Closes the fixable parts of -39: F1 (PDT guard now dates a fill by its fill bar), F2 (Zac-ledger pending signals expire after zac_ledger.max_pending_sessions = 2 weekdays), F3 (bad entry_bar_t on an open position logged UNKNOWN, fails safe) are fixed in changes 6 to 8, 112 tests OK, config hash now b559c847b5717f4a (counts had not started, nothing restarted). Tester pass 4 and QA pass 4 verdicts are in logs\qa\. For trading-director or Zac to rule BEFORE GO-COUNTED.flag (any later code or config change restarts the counts): (a) the MAIN ledger has no date expiry, only the 1 ATR gap cancel, so a stale main signal after an outage is bounded by the gap but not by time; add the same 2 weekday expiry to main (one more config value, hash changes again)? Software-director recommends yes only if you want it closed now, it was outside the order. (b) _check_exit still raises on a bad entry_bar_t (needs a hand-damaged state file; low). (c) Holidays are not modeled in the PDT window or the expiry (a holiday can expire a signal one day early or count a day trade one day long; conservative). (d) Nothing logs the code hash into config-history, so a code edit during the four weeks is only caught by rechecking CODE-SHA256.txt. Monday pre-open smoke steps: Investing\watch-week\smoke-2026-11-30-checklist.md.
- TRADING-2026-11-26-41 (trading-director rulings on -40, 2026-11-27, FYI, no action): main-ledger date expiry NOT added, N1, N2 NOT fixed, holidays NOT modeled (window to 2026-12-24 has no full NYSE holiday, Dec 24 is an early close), code hash checked by hand against CODE-SHA256.txt each Monday pre-open. Reason: any code change after the flag restarts the counts; reviewers advised leaving them. GO-COUNTED.flag created 2026-11-27, config hash b559c847b5717f4a.

## DECISION QUEUED: WWD-2026-11-27-01 (wwd-rights)
Attorney question, not a guess. Percy Jackson S3 E1-2 review, Assembly v7: two Disney+ promo clips (7 s and 8 s) are cropped and brightened so the service's corner marks do not show (a small mark remains on one). Does that create exposure beyond the ordinary fair use question (for example copyright management information, 17 U.S.C. 1202), and does it change the fair use weighing? My read: neutral to slightly risky, cheapest fix is dropping the 7 s clip. Not blocking the note. Risk flag, not legal advice. Note: `WWD\reports\Percy-Jackson-S3-E1-2-Rights-Note.md`.
---

## [ETSY-2026-11-23-01] 2026-11-23 | Nightly rollup | Should the weekly Etsy scheduled task keep firing while both shops are paused, and what to do with the dead Friday manual data pull?

**Blocked:** `ETSY/weekly-prep/2026-11-22.md` (committed `e4eca59`, 2026-11-22) is the first weekly-prep cycle to run since WarriorKingDesigns went on hold and Kingdom Planners moved to the back burner (both Zac, 2026-11-12). It correctly proposed no listings, but flagged two open questions it has no authority to answer itself: (1) whether this weekly scheduled task should keep running against two paused/parked shops, or be paused itself until one of them restarts; (2) whether to revive, retire, or replace the Friday manual Etsy data-pull, which has been dead since 2026-08-20 (94 days as of this pull, confirmed again in `data/weekly-2026-11-20.md`) and is the only source for Etsy's Closed-loop numbers. Neither question has reached this queue before.
**Options:** A. Pause the weekly Etsy routine until Zac un-pauses WKD or lifts KP's back burner, and decide the manual-pull question separately (revive, retire, or replace it). B. Leave the routine running weekly as a cheap holding check (it cost little and caught the Cyber Sale timing note this cycle). C. Leave both as is.
**Recommendation:** A for the routine, with one exception: keep it live through BFCM/Cyber Sale week (11/24-12/2) in case Zac lifts the pause mid-window, since the 11/22 prep doc notes the listing-refresh window is closing in real time. For the manual pull, recommend formally retiring it rather than leaving it indefinitely lapsed, since both shops are inactive; revive it only when a shop goes live again.
**Status:** OPEN

---

## [INFRA-2026-11-23-01] 2026-11-23 | Nightly rollup | The fix for INFRA-2026-11-18-01 was marked DECIDED but was never actually applied - tonight's rollup fired on the identical stale prompt

**Blocked:** `INFRA-2026-11-18-01` (2026-11-18) flagged that this scheduled task's own stored prompt hardcodes a stale venture list ("MAIN EFFORT is Kingdom Planners; ACTIVE ventures are WWD/FrostCast, Shattered Empire, Cyber Security, WarriorKingDesigns") that contradicts root CLAUDE.md. It was marked "DECIDED A (Jarvis)" in the 2026-11-19 readiness pass, with chief-of-staff to change the prompt to "read venture status fresh from root CLAUDE.md each run" at the next session start. Tonight's rollup (2026-11-23, four days later) was fired by the scheduler with that exact same stale text, word for word - the fix was never actually made. This run has no tool to edit a scheduled task's stored prompt, and per its own instructions should touch nothing outside this file, so it again worked around the drift by hand (reading venture status fresh from the live root CLAUDE.md instead of the stale prompt) rather than fixing the source. No harm to tonight's output, but the underlying prompt is still wrong for next time.
**Options:** A. Zac or chief-of-staff actually edits the scheduled task's stored prompt this time (e.g. via `update_trigger`), not just logs the decision again. B. Leave it - every rollup so far has caught and worked around the drift by hand, so it is self-correcting even though it is not fixed.
**Recommendation:** A. This is the second rollup in a row to flag the identical gap between a "DECIDED" note and an actually-executed fix; a third recurrence without action would suggest the chief-of-staff handoff step itself isn't landing.
**Status:** OPEN

---

## [INFRA-2026-11-24-01] 2026-11-24 | Nightly rollup | Scheduled task prompt drift is now a THIRD consecutive night unfixed (INFRA-2026-11-18-01, INFRA-2026-11-23-01)

**Blocked:** Tonight's fired prompt again states step 5 as "MAIN EFFORT is Kingdom Planners; ACTIVE ventures are WWD/FrostCast, Shattered Empire, Cyber Security, WarriorKingDesigns" — identical, word for word, to the text flagged on 2026-11-18 and 2026-11-23. Root CLAUDE.md still says the opposite (no MAIN EFFORT set; ACTIVE is WWD/FrostCast, Shattered Empire, WarriorKingDesigns; Cyber Security is ACTIVE-UNSCHEDULED, CySA+ punted). INFRA-2026-11-23-01 already predicted this exact recurrence and recommended Zac or chief-of-staff actually call update_trigger on the scheduled task itself, not just log the decision again — that still has not happened three cycles in. This run again worked around it by hand (read CLAUDE.md fresh, ignored the stale embedded list) rather than touching the stored prompt, consistent with its own read-only scope.
**Options:** A. Zac or chief-of-staff edits the trigger's stored prompt directly this cycle, replacing the hardcoded venture list with "read venture status fresh from root CLAUDE.md each run." B. Leave it — the rollup keeps self-correcting by hand, so there is no actual misreporting risk, just repeated identical noise in this log.
**Recommendation:** A. Three identical flags without the one-line fix landing points at the chief-of-staff handoff step itself not executing, not at the fix being hard — worth Zac's or Jarvis's direct attention rather than a fourth log entry tomorrow night.
**Status:** OPEN

---

## [WWD-2026-11-24-01] 2026-11-24 | Nightly rollup | TASKS.md unchanged since 2026-11-19; several dated items in that window have no record either way

**Blocked:** TASKS.md's last commit is 2026-11-19 (`git log -- TASKS.md`), and the repo had zero commits in the 24 hours before this rollup beyond last night's own rollup entry (`f44fb5a`, 2026-11-23 03:11 UTC). Several TASKS.md rows carry target dates that have since passed with nothing on record to say what happened: Den Files EP1 (Fire in the Sky) recording was targeted Sun 2026-11-22 about 7:30 PM, still marked "Not Started" as of the 11-19 snapshot with script gate 2 (two logged writing-room passes) not seen in logs; Percy Jackson S3 Ep1 watch/record was targeted Fri-Sun 11/20 to 11/22, same "Not Started" status; DraftKings Week 11 lineups were targeted Sat/Sun 11/21 to 11/22 and TASKS.md itself already notes "finish status not verified." Per the Honesty rule, reporting this as genuinely unknown rather than assuming either way — no commit or log entry confirms completion, slippage, or cancellation for any of the three.
**Options:** A. Chief-of-staff or Jarvis checks with Zac directly on these three dated items next session and updates TASKS.md accordingly. B. Leave it — Zac mentions it unprompted if something slipped, same as other personal/schedule items. C. Treat the Den Files recording specifically as still blocked until the two logged writing-room passes exist, regardless of what actually happened Sunday.
**Recommendation:** A — cheap, and the fastest way to get TASKS.md current again now that it is 5 days stale with multiple expired target dates still sitting on it unresolved.
**Status:** OPEN

---

## [INFRA-2026-11-26-01] 2026-11-26 | Nightly rollup | Scheduled task prompt drift is now a FOURTH consecutive logged occurrence (INFRA-2026-11-18-01, -23-01, -24-01) — confirmed directly against the trigger this time, not inferred

**Blocked:** Called `list_triggers` directly this run and read the "WKP Nightly Rollup" trigger's stored `prompt` field verbatim (id `trig_01FkRBY9ZbXXjHurmZbUJ2P9`). It is byte-identical to the stale text flagged on 11-18, 11-23, and 11-24: step 5 still reads "MAIN EFFORT is Kingdom Planners; ACTIVE ventures are WWD/FrostCast, Shattered Empire, Cyber Security, WarriorKingDesigns," which contradicts the live root CLAUDE.md (no MAIN EFFORT set; ACTIVE = WWD/FrostCast, Shattered Empire, WarriorKingDesigns; Cyber Security is ACTIVE-UNSCHEDULED). This run again worked around it by hand, reading venture status fresh from CLAUDE.md as instructed. New fact this cycle: this session's own tool list includes `mcp__Claude_Code_Remote__update_trigger`, which could fix the stored prompt directly in one call — but this run's own instructions scope it to read-only review plus append-only writes to this file, so it did not call it. Separately: there is no git commit and no DECISIONS.md entry dated 2026-11-25 — either the trigger did not fire that night or it fired and found nothing new to log; `list_triggers`' `last_run` field only retains the most recent firing (today's), so this cannot be confirmed either way from this session. Not alert-engineering a single possible miss per the root CLAUDE.md note on occasional missed runs, but naming it since the Honesty rule requires saying what is actually unknown.
**Options:** A. Zac, or any session not scoped read-only (e.g. chief-of-staff, or Jarvis in an ordinary working session), calls `update_trigger` directly on `trig_01FkRBY9ZbXXjHurmZbUJ2P9` with a corrected prompt that reads venture status from CLAUDE.md each run instead of hardcoding a venture list — now a one-line, already-fully-specified fix with the exact tool and trigger ID confirmed. B. Leave it; a fifth identical log entry costs little and the hand-correction keeps tonight's report accurate regardless.
**Recommendation:** A, this cycle specifically. The blocker was never finding the fix, it was that three straight "DECIDED A" entries never got an actual non-restricted session to place the one call. The path is now fully spelled out (tool name and trigger ID both confirmed live) rather than needing further diagnosis.
**Status:** OPEN

---

## [INFRA-2026-11-28-01] 2026-11-28 | Nightly rollup | Scheduled task prompt drift is now a FIFTH consecutive logged occurrence (INFRA-2026-11-18-01, -23-01, -24-01, -26-01) — still not fixed, no 11-27 run on record either way

**Blocked:** Tonight's fired prompt (the text this rollup was started with) again states step 5 as "MAIN EFFORT is Kingdom Planners; ACTIVE ventures are WWD/FrostCast, Shattered Empire, Cyber Security, WarriorKingDesigns" — byte-identical to the stale text flagged on 11-18, 11-23, 11-24, and 11-26 (trigger id `trig_01FkRBY9ZbXXjHurmZbUJ2P9` per the 11-26 entry). Root CLAUDE.md still says the opposite (no MAIN EFFORT set; ACTIVE = WWD/FrostCast, Shattered Empire, WarriorKingDesigns; Cyber Security is ACTIVE-UNSCHEDULED, CySA+ punted). This run again worked around it by hand, reading venture status fresh from the live CLAUDE.md as instructed, and did not call `update_trigger` itself, consistent with every prior rollup's read-only/append-only scope. Separately: there is no DECISIONS.md entry and no git commit evidence tying to a nightly rollup firing on 2026-11-27 — same gap already named without alarm on 11-26 (the root CLAUDE.md note on occasional missed runs covers this), noted here only per the Honesty rule, not as a new problem.
**Options:** A. Zac, or any session not scoped read-only (chief-of-staff, or Jarvis in an ordinary working session), calls `update_trigger` on `trig_01FkRBY9ZbXXjHurmZbUJ2P9` with a corrected prompt that reads venture status from CLAUDE.md fresh each run instead of hardcoding a venture list. B. Leave it; the hand-correction has now kept five straight nightly reports accurate despite the stale source text, so there is no actual misreporting risk, just repeated identical log noise.
**Recommendation:** A. Five identical flags with a fully-specified one-line fix (exact tool, exact trigger ID) and still no action taken points at this falling through the gap between sessions rather than being hard to do — worth a direct nudge to chief-of-staff or Zac rather than a sixth log entry tomorrow night.
**Status:** OPEN
