# WKP Fable Scan, 2026-11-10

Read-only scan. Nothing was posted, sent, bought, installed, or edited. The watcher zip was read in place, never unpacked or run. Anything I could not check is marked UNVERIFIED. Trading notes are plan critique, not financial advice.

## Executive summary

1. The company builds org chart faster than it ships product. Since the 10/29 audit, 20 agent files and 5 departments were added (Animation, Studio, QA, Software, Trading). No sale is recorded anywhere in the repo.
2. The stated priority order is not the real one. Real effort goes to WWD, fantasy football, and infrastructure. The MAIN EFFORT (Kingdom Planners) has no storefront, and its director had 0 launches in the audited month.
3. The only cash source with evidence is the weekend delivery job (about $196 a weekend, TASKS.md). The fastest new dollar is photo restore, and it is blocked by one 10-minute list due Fri 11/13.
4. The bottleneck is Zac's decision queue, not agent capacity. `logs\DECISIONS.md` has 70 OPEN entries. No triage has ever run. More agents make that queue longer.
5. The new QA and operating procedure exist on paper only. `logs\qa\` is empty and `logs\jarvis-delegation.md` has a header and no lines. 70 files are uncommitted since 11-05.

---

## 1. Structure

**Overbuilt**
- 52 agent files in `.claude\agents\`. The 10/29 audit (`reports\agent-audit\2026-10-29-agent-audit.md`) counted 32, with 10 never launched. Nothing was folded or retired after that audit. 20 more were added.
- Departments with no finished job on record: Animation (6 agents, log shows training only, "NOT run"), Studio (no log file), Software (`software\` is empty), QA (`logs\qa\` is empty), Tracking (no log file), Trading (no log file). Launch counts after 10/29 are UNVERIFIED, I did not recount sessions.
- The Ian trailer shows the cost. One free 60-second trailer for a friend produced 23 OPEN decisions (WRENCH-*), 4 script passes, a v1 rejected as "garbage" (BUILD file), and a v2 restart.

**Redundant or unclear owner**
- graphic-design and video-ugc duplicate wwd-vfx and shorts-factory in practice (audit finding, unchanged).
- Three trading toolsets overlap with no stated winner: the 11 `trader-*` skills (Alpaca based), the WKT watcher zip (Coinbase and yfinance), and the Alpaca scanner spec in `Investing\CLAUDE.md`.
- Kingdom Planners is the MAIN EFFORT but shares etsy-director with WKD. No one owns "get KP its first sale" across Etsy and Payhip.
- CySA+ (day job) has no owner and no TASKS.md row. Two decisions (CS-2026-10-15-01, CS-2026-10-28-01) ask what happened. No answer on file.

**Missing gates and contradictions**
- AGENT-NETWORK.md limit 2 says no chain longer than three handoffs. The new chain (director, department, bench, QA, QA bench, Jarvis) breaks that by design. One rule has to change.
- "QA never edits" is not enforced by tools. Every QA agent has Write and Bash.
- devils-advocate is required for every new idea. I found no ruling on file for the trading department or the dashboards (grep of `logs\` and `research\` for trading-director and WKT returned nothing).
- No gate checks that a flag for the main session was ever acted on. Example: "reminder NOT set, main session to set it" repeats across TASKS.md rows.

**What breaks when something fails**
- Single point: the main session. Only it has the browser, calendar, and scheduler. Subagents log "NEEDS CHROME PULL" and "CALENDAR NEEDED" and stop. Godzilla shipped with 11 of 18 pictures for this reason.
- Single point: Zac. Every blocked agent writes to one file that already has 70 open items.
- Silent skips that are disclosed but still ship: "no-ai-slop skill not invoked, rules applied by hand", "bench not launched, I built it directly", "final not re-read by benches" (`logs\wwd-director.md` 11-01, 11-07, 11-09, `logs\script-room.md` 11-10).
- New agents only load at session start. Every department built today is covered by a general-purpose stand-in until then.
- Git: local is 1 commit behind origin (nightly rollup 11-08 edited `logs\DECISIONS.md`). Local also edited that file. The cloud rollup reads a repo that is 5 days stale and files "stale deadline" decisions about work that is already done locally.
- File damage: TASKS.md has 195 lines of broken characters and CLAUDE.md has 42. TASKS.md also has paths eaten by escape codes (example: `WWD` then a line break then `eports\`, and `.claudegents\studio-director.md` in CLAUDE.md). Some tool is writing backslashes as escape codes. Paths in those rows cannot be trusted.
- TASKS.md is 130 KB and loads into every session through the @-import. Most of it is Done rows.

---

## 2. Money

**Ranking by realistic time to first dollar** (dollar figures are from repo files, most are labeled assumption there)

| Rank | Thread | Time to first dollar | Effort | Evidence |
|---|---|---|---|---|
| 1 | Weekend delivery job | Already paying | Known | About $196 a weekend (TASKS.md). Only proven source. |
| 2 | Photo restore, direct, as "Zac in Grovetown" | 7 days if the network exists | 3-photo test plus one post | Devils-advocate GO WITH CHANGES. Blocked on the groups list. |
| 3 | KP on Payhip, 2 products | 7 to 30 days | 1 hour | $0 to $70 in 30 days (assumption in the prep file). VA tables go stale Dec 1. |
| 4 | WKD Etsy, existing live shop | Unknown | Low, copy only | 22 Christian designs zipped 9/1 and 6 designs prepped 10/3, none posted. No traffic data since 8/20. Listing fees UNVERIFIED. |
| 5 | KP Etsy shop | After $29 fee | Low, prep is done | Blocked since 9/7. Zac decided wait. |
| 6 | WWD affiliates, tip jar | Months, small | Low | 744 subs. Research says plan on tens of dollars a month. |
| 7 | eBay parts and salvage | Months | High | Quotes sent 10/24. No replies on file. |
| 8 | Transcription, CMMC kit, KDP, PAWS, Spark, Animation | Not near | High | HOLD or on ice by devils-advocate or Zac. |
| n/a | Trading | Not income | High | About $60 account. A hobby with risk, not a cash plan. |

**Pushback on the priority order**
- CLAUDE.md says MAIN EFFORT is Kingdom Planners. The logs say the main effort is WWD review packages. WWD is a partnership with 744 subs and gains falling 17, 13, 6 (Aug to Oct, TASKS.md). It earns the least per hour of anything here and gets the most hours.
- WKD is on "hold" while holding 28 unposted, finished designs in a live shop, in the holiday quarter. KP is "main effort" with no shop. That is backwards for a cash problem. Whether WKD designs sell is UNVERIFIED because the Friday data pull lapsed in August.
- The venture review is due 15 NOV. Use it. My recommendation: name one money line as the main effort for 30 days (photo restore test, then KP Payhip), run WWD in maintenance mode (FrostCast plus one review a week, standard package, no custom openers or kit builds), freeze the rest.

**Single best action this week:** Zac writes the groups list (name, member count, selling rules) and runs the 3-photo test before Fri 11/13. Two gates have now said the same thing (11-04 and 11-10). The response to the first was more research and a second business idea. No agent can do this step.

**Freeze or drop**
- Freeze: Animation, Studio, Software builds, comic series, PAWS, Spark, eBay white label, transcription, CMMC, any new department.
- Cap: Ian trailer. It is free. Pick the simplest cut, send Ian the questions, stop adding passes.
- Keep small: fantasy football. It is personal, it had 10 launches in the audit month, and on 11-10 it got a five-part fix project. It is taking main-effort hours.
- Do not treat trading as part of the money plan.

---

## 3. Follow-through: the 10 open loops that matter

| # | Open loop | Blocks |
|---|---|---|
| 1 | Groups list and 3-photo test, stop rule Fri 11/13 | Photo restore and the KP Payhip test. The only near money. |
| 2 | 70 uncommitted or untracked entries, last commit 11-05, local behind origin by 1 on DECISIONS.md | Loss risk for every new agent spec, memory file, and report. Cloud rollup works from stale data. |
| 3 | 70 OPEN decisions, never triaged. Many are already answered in TASKS.md (Heat, Resident Evil, Clayface shorts, Halloween short, Ian price path) | Real decisions are buried. Agents keep re-flagging. |
| 4 | 15 NOV: Etsy listing cap expires and venture status review is due | Whether the cap renews. Whether priorities get reset. |
| 5 | Etsy Friday data pull lapsed since 8/20 (ETSY-2026-10-09-01). Last weekly data file is 10-30, 11 days old | Closed-loop rule. Every plan is "unguided" today. |
| 6 | Surfshark FTC disclosure question, open since 9/18 (WWD-2026-09-18-01, WWD-2026-10-15-01). Whether the read aired is UNVERIFIED | The only sponsor deal. Possible disclosure exposure. |
| 7 | Godzilla Minus Zero: release date, loudness -24.7 LUFS not fixed, 10 unsourced pictures, about 18 s of trailer footage | The current review. Release status is UNVERIFIED. |
| 8 | KP product readiness: Google Sheets test never run, Complete Budget System lost, no screenshots, VA table stale Dec 1 | Any KP sale on any platform. |
| 9 | Ian trailer: 23 open decisions, text-rights STOP open, 22 questions not sent to Ian, Veterans Day target is tomorrow | Evening hours through the photo restore window. |
| 10 | Trading: Robinhood versus Alpaca conflict not queued, watcher never run, watch week not started | Any honest "ready" claim. |

Also open: CySA+ outcome unrecorded. Matt brief on channel changes not sent. Voiceprints still not enrolled, so every transcript since August needs hand mapping. Vision Quest 3+4 and 5+6 shorts not posted. PAWS-001 and PAWS-004. No Monday brief for 11-09 in `D:\WKP Reports\Monday Brief\` or `reports\monday\`.

---

## 4. Trading department critique (plan critique only)

**What is sound**
- `trading-director.md` is the best-written spec in the repo. Never places orders, never touches keys, UNKNOWN counts as FAIL, a 7-item go-live checklist that Zac signs.
- I read the watcher code inside the zip without unpacking. `run.py` exits unless mode is "watch". I found no order-placing code. Network calls go to Coinbase public candles, yfinance, and Twilio only. This was a read, not a test or a security review. Still UNVERIFIED as working software.

**The conflict (three stories, pick one)**
- `Investing\CLAUDE.md` (locked 7/24): execute by hand on Robinhood, Alpaca for data only, move to Alpaca at $25k.
- `wkt-locked-rules.md` (10/19): live crypto through the Robinhood Crypto API, stocks on Alpaca "once open and funded", data from Coinbase and yfinance. Alpaca data is not used at all.
- `trader-broker` skill (installed 11/01): builds tickets for an Alpaca MCP.
- The director spec says to queue this. It is not in `logs\DECISIONS.md`.

**Risky or missing before any live money**
1. "Twilio YES/NO approval with auto-execute if no reply" is in the locked rules. That means silence spends money. It contradicts the director's hard limits and the root rule that spending needs Zac's yes. Zac works 8 to 5 and cannot answer texts on demand. This rule should flip to "no reply means no trade".
2. The paper account is $1,000 (`config.yaml`). The real account is about $60 (balance as of 7/24, current balance UNVERIFIED). At $60, a 0.5 percent risk is 30 cents and the 25 percent cap is $15 (my arithmetic). Spreads and minimum order sizes can swamp that. Paper results at $1,000 do not transfer.
3. No fees, spread, or slippage in the grader (`learn.py`). Entries fill at the bar close and targets fill at the exact price. The checklist asks for a haircut. The code has none.
4. The kill switch counts closed paper trades only and only blocks new trades. Four open positions at up to 2 percent risk each are not counted until they close.
5. There are no real stop orders in the design. Stops exist only while the PC is awake and the script is running. TASKS.md records 18 Kernel-Power 41 hard resets on this machine. For 24-hour crypto, that is the main operational risk.
6. The crypto universe includes SHIB, PEPE, BONK and WIF. The director's own lesson says not to chase memecoins. The stock list is four volatile small caps.
7. Self-adjusting weights start moving at 8 graded trades. That is tuning on noise. The spec's own rule (change one thing per 50 to 100 trades) is stricter than the code.
8. The only test checks the Monday rule and the size cap. Kill switch, stop logic, and time stop are untested. Checklist item 5 needs tests that do not exist.
9. yfinance is an unofficial feed. Terms and reliability at 1-minute polling are UNVERIFIED. data-sourcing should check before the watch week counts.
10. `make_robinhood_key.py` writes a private key into a plain `.env` file in the watcher folder. Decide where that folder lives (never the repo, never a synced drive) before the key exists.
11. Twilio costs money (price UNVERIFIED). That is a spend decision.
12. Missing from the plan: a written max loss in dollars, a trade record for taxes, what happens to open positions when the machine dies, and who checks the watcher is still alive.
13. Phase 4 (vertical spreads) is far outside a $60 account. Remove it from the active plan so "ready soon" means phase 1 only.
14. Investing is DORMANT in root CLAUDE.md and now has a director. The status change is not queued.

**Honest framing:** a watch week costs nothing and is worth running in paper mode from scratch. Going live does nothing for the debt and adds a way to lose money while Zac is at work.

---

## 5. Dashboards

Use one pattern for all three: a Python script reads repo files and writes one static HTML page. No server, no Node build, opens by double-click. `impeccable` fits dashboards (its "Operate" mode). `design-taste-frontend` is written for marketing sites, and its Stop hook runs a Node script with headless Chrome and a 600 second timeout. Use it for polish only.

| Dashboard | Data that already exists | Gaps |
|---|---|---|
| Fantasy football | `Fantasy-Football\dashboard\` already runs at localhost:8787 (poller, server, `static\`). `tracker\predictions.csv` (133 rows), `fixes-2026-11-10\calibration_log.csv`, `lineup_calib.csv`, `pickem_backtest_rows.csv`, `data\ff-simulator\`. | `tracker\biases.md` is empty. Weeks 2 to 5 missing from the tracker. Bad closing line (FF-2026-11-10-01). |
| Agent network and flow | `.claude\agents\*.md` front matter (name, tools, model), `AGENT-NETWORK.md`, `logs\*.md`, `logs\DECISIONS.md` status lines, `logs\qa\`, TASKS.md, session files under the Claude projects folder (the audit counted launches from those). | Logs have no common format. DECISIONS.md headers are inconsistent (one has no brackets, one entry has two status lines). True message flow only exists in session transcripts, which are large and private. |
| Trading | Nothing yet. After a watch week: the watcher's SQLite file (bars, signals, sentinel, weights), `logs\watcher.log`, and the planned `Investing\watch-week\` files. The 7-item go-live checklist is ready to show today. | No data until the watcher runs. |

**Build order**
1. Fantasy: restyle the page that exists and add an accuracy panel. Real data, in season, lowest risk.
2. Agent network: static page. Start with three panels only: open decisions by venture and age, last log entry per agent, agents with no log at all. Add flow later.
3. Trading: last. Build it against the watcher's offline demo data so it is ready when the watch week starts.

**Risks**
- This is the "cool factor" pull ME.md warns about. Three dashboards through the full new chain is days of agent work for zero revenue. Time-box each to one session.
- A good-looking trading dashboard makes paper results feel safer than they are. It must show sample size, the fee haircut, and the checklist fails on the first screen.
- The agent dashboard will mostly show red (70 open decisions, empty logs). That is useful, and it is the point.
- `design-taste-frontend` is 35 MB and untracked. Decide whether it belongs in the wkp-brain repo before the next commit.
- Standardize the log line format first, or the agent dashboard parser will break weekly.

---

## 6. Process: does the stated procedure hold up

**What holds:** the honesty rule mostly works. Logs are full of plain "NOT AVAILABLE", "untested", "not re-read", "nothing posted". Agents rarely fake results. The EP119 correction (wrong "$40M Supernova" claim caught) shows the copy gate adding value. devils-advocate rulings on the money ideas are the sharpest documents in the repo.

**The pattern that fails:** disclose and ship. Agents state the gate they skipped, then mark the job DONE. Honest reporting has become a substitute for following the process.

**Places the stated process was not followed**
1. **QA has never run.** `logs\qa\` is empty. The procedure says QA checks before Jarvis and Zac, and to run the spec through a general-purpose agent until the agents load. On 11-10 the Fantasy fixes docx and three side-business docx packages went to `D:\WKP Reports\` with no QA report. Exact order versus the lock time is UNVERIFIED.
2. **Jarvis delegation log is empty.** The rule says every inline job gets a line. The BUILD file itself says Jarvis rebuilt the Ian v2 document, and the design skills were vetted and installed on 11-10. No lines logged.
3. **Scripts gate (two full passes).** `logs\script-room.md` 11-10: "marketing-director NOT run on end card", "final not re-read by benches after last edits". Same note on 11-05.
4. **Bench bypass.** `logs\wwd-director.md` 11-07: "I drafted the sheet myself (wwd-run-sheet bench not used)". 11-09: "wwd-run-sheet bench not launched". 11-01: marketing-director wrote all copy itself, desks not launched. AGENT-NETWORK.md says do not do the other desk's job yourself.
5. **no-ai-slop gate.** 11-01 and 11-07 packages: "the skill file was not invoked", "rules applied by hand".
6. **Public posting.** EP119: 69 posts were scheduled with Opus's own copy before the approved copy file existed (TASKS.md). Caught and redone on 11-05. Captions on the live posts are still "not verified".
7. **Closed loop.** Newest weekly data file is `data\weekly-2026-10-30.md`, 11 days old. Etsy manual data stops at 8/20.
8. **Weekly rhythm.** No 11-09 Monday brief on disk. The task-observer weekly review rides on that brief. The DECISIONS.md triage and qa-auditor review are "Not Started".
9. **TASKS.md same-turn rule.** At least a dozen OPEN decisions exist only because a TASKS row was not updated when the work happened.
10. **Known defects shipped as DONE.** Godzilla final cut marked DONE with loudness about 10.7 dB under target, "NOT fixed".

**Verdict:** the procedure locked today adds two more layers on top of gates that are already skipped under time pressure. Fewer gates that always run beat more gates that get waived. I would enforce three and drop the ceremony around the rest: (1) nothing public without the copy gate, (2) every "done" claim traced by one checker, (3) every skipped step blocks DONE instead of becoming a footnote.

---

## 7. Quick wins (safe, reversible, no ask needed)

1. Move Done rows from TASKS.md into `TASKS-ARCHIVE.md`. Cuts most of the 130 KB that loads every session.
2. Repair the broken characters in TASKS.md and CLAUDE.md, fix the escape-eaten paths, and find the tool that writes them.
3. Triage DECISIONS.md: mark entries SUPERSEDED where TASKS.md already holds Zac's answer, with the evidence line. Hand Zac one short list of what is truly open.
4. Queue the two trading conflicts (Robinhood versus Alpaca, auto-execute on no reply) as the director spec requires.
5. Rewrite the stale "Current state, August 2026" block in CLAUDE.md from TASKS.md facts, and fill or delete the [FILL IN] lines in `Investing\CLAUDE.md`.
6. Fix the three-handoff contradiction in AGENT-NETWORK.md, and add a one-line standard log format every director must use.
7. Start `logs\jarvis-delegation.md` with today's inline work, and add a CySA+ row to TASKS.md.
8. Change "skipped a gate" from a footnote to a status: a job with a skipped gate reports as PARTIAL, never DONE.

---

## Ranked action list

| # | Action | Tag |
|---|---|---|
| 1 | Write the groups list and run the 3-photo test before Fri 11/13 | ZAC |
| 2 | Say yes to pull, commit, and push the 70 pending changes (decide first if the 35 MB design skill goes in the repo) | ZAC |
| 3 | Triage DECISIONS.md down to one short list, mark superseded entries | SAFE |
| 4 | 15 NOV review: pick one money line as main effort for 30 days, put WWD in maintenance mode, freeze the rest | ZAC |
| 5 | Archive Done rows out of TASKS.md and repair the broken text and paths | SAFE |
| 6 | Run the KP Payhip pre-checks Jarvis can do (file checks, draft copy through the gates). Zac does the Sheets test and screenshots | SAFE, then ZAC |
| 7 | Decide on posting the 28 finished WKD designs in the live shop before the holidays (listing fees, cap renewal) | ZAC |
| 8 | Cap the Ian trailer: simplest cut, send Ian the questions, close the dead WRENCH decisions | ZAC |
| 9 | Queue the trading conflicts, and flip "auto-execute if no reply" to "no reply means no trade" | SAFE to queue, ZAC to decide |
| 10 | Run QA once for real on one finished package (Godzilla) through a general-purpose stand-in, to prove the gate before adding more | SAFE |
| 11 | Restyle the existing fantasy dashboard first, time-boxed. Agent dashboard second. Trading dashboard last | SAFE |
| 12 | Record the CySA+ outcome, close the Surfshark disclosure question, and hand Jarvis one clean solo voice clip each for voiceprints | ZAC |
