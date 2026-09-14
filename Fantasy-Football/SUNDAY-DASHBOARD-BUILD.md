# Sunday Dashboard — Local Build Spec

## DROP LOCATION
`D:\WKP\fantasy-football\`

## EXACT PHRASE FOR CLAUDE CODE
> Read SUNDAY-DASHBOARD-BUILD.md and build it. Start with Section 2 —
> verify every MFL endpoint listed there actually returns data before
> writing any dashboard code. Report what came back, then build Phase 1
> only. Do not build Phase 2 or Phase 3 until Phase 1 runs clean
> through a full Sunday.

---

## What this is

A local web dashboard for Sunday. Runs on Zac's PC, opens in a browser
at `localhost`. Nothing public, nothing hosted, no credentials leaving
the machine.

Two jobs in one page:
1. Live IRFL matchup — am I winning, and who do I have left
2. Pick'em card tracking — which of my picks are covering right now

Plus a filtered news strip.

### Not in scope
- Phone or remote access. Layout must be built to collapse to one
  column later, but do not build tunneling, hosting, or auth now.
- The sports content venture. Unrelated, different folder.
- Anything WWD.

---

## SECTION 1 — Architecture

**One Python process.** It polls the data sources on a timer, writes
the current state to a single JSON file, and serves a static page that
reads it.

Critical: the browser must **never** trigger a data pull. Refreshing
the page reads the cached JSON only. If ten refreshes cause ten MFL
calls, the key gets throttled or shut off mid-Sunday.

```
D:\WKP\fantasy-football\dashboard\
    poller.py          polls sources on a timer, writes state.json
    server.py          serves the page and state.json on localhost
    state.json         current snapshot, overwritten each cycle
    static/
        index.html
        style.css
        app.js
```

Run on a port unlikely to collide — 8787 unless something else has it.

**Layout:** CSS grid, desktop-wide by default, with breakpoints that
collapse it to a single column on a narrow viewport. Build the
breakpoints now even though phone access is out of scope. It costs
almost nothing today and avoids a rewrite later.

**Credentials:** environment variables only, same as the existing
skills. `MFL_API_KEY` is already set. Never write a key into any file
in this folder, and never into `state.json` — that file is served to
the browser.

---

## SECTION 2 — Verify endpoints before building

Confirm each of these returns real data. Report exactly what came back.
Do not substitute a similar-looking endpoint and continue.

Base pattern, already proven working for rosters:
```
https://www44.myfantasyleague.com/2026/export?TYPE={type}&L=43094&APIKEY={key}&JSON=1
```

Check these types:

| Type | Expected | Needed for |
|---|---|---|
| `liveScoring` | Live matchup totals, players yet to play | Core panel |
| `playerScores` | Per-player live points under league scoring | Player rows |
| `injuries` | League-wide injury status | News filter |
| `playoffChances` or `standings` | Record and standing | Header |

**Also confirm MFL's polling limits.** Their developer docs state
request limits and may require a `User-Agent` header identifying the
application. Find the real number and report it. Do not guess a polling
interval — derive it from the published limit with a wide safety
margin.

**ESPN scoreboard** for real game scores and clock (no key):
```
https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard
```

**ESPN news feed** for the news strip:
```
https://www.espn.com/espn/rss/nfl/news
```
Confirm this RSS feed is still live. If it 404s, say so — do not
substitute a scraper.

**Sleeper player cache** for injury status flags. Already built in the
`fantasy-football-data` skill. Read from the existing cache file, do
not re-pull.

---

## SECTION 3 — Polling rules

**Poll only when games are live.** Check the ESPN scoreboard for game
status first. If nothing is in progress, the poller sleeps. This is the
single biggest protection on the MFL key — it cuts request volume by
roughly ninety percent across a week.

Proposed intervals, to be adjusted once the real MFL limit is known:

| Source | Games live | No games live |
|---|---|---|
| MFL live scoring | Slowest interval the published limit allows, with margin | Stopped |
| ESPN scoreboard | Every sixty seconds | Every fifteen minutes |
| ESPN news RSS | Every five minutes | Every thirty minutes |
| Sleeper player cache | Once daily | Once daily |

**Fail loudly.** If a source errors, show a visible stale-data warning
on the panel it feeds, with the timestamp of the last good pull. Never
display an old number as if it were current. Never silently retry in a
tight loop.

Every panel displays the age of its data.

---

## SECTION 4 — Panels, in build order

### PHASE 1 — Build this first, nothing else

**1. Matchup header.** My total, opponent total, and both projected
finals.

**2. Players yet to play — the most important number on the page.**
Mine and my opponent's, side by side, as counts. Down thirty with four
left is a different situation than down thirty with none left, and the
raw score does not show that.

**3. Inactive alert.** A red banner, above everything, before the one
o'clock kickoff: any player in my starting lineup ruled out or doubtful.
This is the highest-value item on the entire dashboard. A started
player who was ruled out ninety minutes before kickoff is the most
expensive routine mistake in fantasy, and it is entirely preventable.
Show it loudly and keep showing it until the slot is changed.

**4. Pick'em card panel.** Read this week's card from
`D:\WKP\fantasy-football\cards\CODENAME_Week{N} Entry.xls`. For each
pick, show my side and line, the live score from ESPN, the game clock,
and whether it is currently covering. Color-code covering, not
covering, and final.

The card is the frozen Monday baseline. It is the source of truth for
what was picked. If the file for the current week is missing, say so on
the panel — do not fall back to current lines and pretend.

**5. News strip, filtered.** Only stories mentioning a player on my
roster or my opponent's roster. Everything else goes into a small
collapsed section. An unfiltered league news feed becomes noise and
gets ignored by week three.

Label it honestly. Free feeds run behind Twitter breaking news by
minutes to a half hour. Put a line on the panel stating this is not a
first-alert source.

### PHASE 2 — After Phase 1 survives a full Sunday

**6. Defensive block, separate panel.** Eight of seventeen starters are
IDP. Their points accrue slowly — a tackle at a time — so they get
ignored next to a touchdown. Give them their own panel: tackles, sacks,
turnovers, live.

Build this to work whether or not Sleeper IDP projections turned out
usable. If projections exist, show projected versus actual. If they do
not, show actual only and label the panel as having no projection
baseline. Do not fabricate a projection to fill the column.

**7. On the field now.** Which of my players are in a live game, with
game clock and network. Tells me what to put on the TV.

**8. Bench regret.** Players I sat who are outscoring players I
started. Uncomfortable and useful — it is the raw feedback for the
accuracy log.

### PHASE 3 — Later

**9. Red zone watch.** My players inside the opponent twenty. ESPN
scoreboard carries situational data; verify it exposes this before
committing to the panel.

**10. Stat correction check.** Scores change Monday and Tuesday. Flag
any matchup whose margin was inside five points and whose score has
moved since Sunday night.

---

## SECTION 5 — Open item

The accuracy log — recording each week's lineup calls and pick'em
recommendations against what actually happened — is a separate build
and is not part of this dashboard. Bench regret in Phase 2 produces
some of the raw data for it. Do not build the log here.

Whether the existing Excel tracking sheet is actually being filled in
each week is unconfirmed. Do not build anything that assumes it has
current data in it.
