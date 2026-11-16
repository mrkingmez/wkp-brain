# DFS process from Zac's friend, part 1 of 3 (received 2026-11-13)

Source: Zac's friend (an experienced DK player), relayed by Zac in chat. Parts 2 and 3 not received yet. Saved as written, lightly trimmed. Do not build from it until all three parts are in, unless Zac says go.

## Part 1: DK NFL Early-slate process

1. **Portfolio, not one perfect lineup.** Treat the slate like an investment mix. Safe chalk is the base, mid-owned plays fill the middle, a few low-owned darts give the upside. They do not trust sim scores or rankings much. They trust relative position ranks and players whose scores move together (QB plus his receivers, bring-backs).
2. **Chalk pool, then require it.** Take the top 6 RBs, top 6 WRs and top 6 TEs by projected ownership, then add any top-6 by projection who are not already in, position by position. Every lineup needs at least 5 players from that pool. That keeps the floor high enough to clear cash lines and the remaining spots are where they take shots.
3. **QB rules.** No QB under $5,000. A low-owned QB must pass a gate: confirmed starter, Vegas implied team total of 21 or more, a top-12 ceiling at the position, and an opponent defense outside the top 8. Gate-passing low-owned QBs keep paying (Stroud and Love in Week 9). Misses come from too many chalk QBs that fail the gate.
4. **Stack rules.** Pair the QB with his receivers, but never play 3 or more bring-back players from the opponent in the main stack. Control team exposure through stack size and per-player caps, not by forcing anyone in.
5. **Do not force players.** Use caps and broad minimums, not locks. Let the pool do the work.
6. **Timing.** Submit a rough backup set early on Sunday. Recheck the pool when inactives and updated projections land around 11:30 AM ET, do the final build about an hour before lock, then stop. No endless rebuilding.
7. **Review every week.** After the slate compare projected and actual ownership, see which low-owned plays hit, and check how far the lineups were from the cash line. Ownership projections have been fine. QB choice is where the money is won or lost.

## What our current tools have and lack (Jarvis, 2026-11-13, from reading `dfs_optimize.py`)

Have:
- Salary-cap optimizer built on a simulation (4,000 simulated slates), cash mode (best average) and GPP mode (best 90th percentile), optional QB stack flag, drops OUT and IR players, reads a DK salary file.
- Odds pulls (for implied team totals), nflverse data, injury files, a Week 10 simulation, DFS study notes in `reports\Fixes-2026-11-10-DFS.md`.

Lack (needed to follow this process):
- **Projected ownership** for every player. No source wired in. This drives the chalk pool and the low-owned QB gate.
- A **chalk pool and "at least 5 from the pool"** constraint.
- **QB gate** checks: confirmed starter (partly from injury data), implied total of 21 or more (computable from our odds pull), top-12 ceiling (computable from the sim), opponent defense rank outside the top 8 (needs a defense ranking source).
- **Portfolio output**: many lineups with per-player and per-team exposure caps, a max of 2 bring-backs, and no forced players.
- **Review loop**: projected versus actual ownership, which low-owned plays hit, distance from the cash line. Needs a tracker.
- The friend does not trust sim scores much; ours is a sim. Use the sim for ceilings and correlation, use his rules for structure, and measure which one does better over weeks.

## Questions for the friend (via Zac), to settle before building
1. Which source gives the projected ownership, and what does it cost?
2. Which projection source defines "top 6 by projection"?
3. How many lineups per slate, entry fees, and are they cash games, GPPs or both?
4. The numbers for per-player caps, team exposure caps and stack size.
5. Where do the defense ranks and "top-12 ceiling" come from?
6. Does "Early slate" mean the Sunday 1 PM games only?

Parts 2 and 3: pending.

---

## Part 3 (received 2026-11-13): data sources and contest rules, from the friend

- The projections file Zac received costs the friend $297 a month. The friend's rule: the first $300 of profit each month pays that bill. He did not start there. He started with free trials.
- **Daily Fantasy Fuel (dailyfantasyfuel.com):** his go-to. Lightweight, solid projections and ownership, no simulations, has an optimizer. Good for cash style games like DK double-ups. 7-day free trial that he says allows downloading projections and ownership. Good base for building our own sims.
- **DFS Army:** good data, tools and information, "a really good optimizer", best package under $100 a month. He is not sure a free trial exists.
- **Volume and contests:** about 30 lineups on NFL, each different, to cover the process in part 1. As many single-entry and 3 to 5 max-entry contests as possible, then fill the rest with cheap 20-max contests. NEVER a contest with more than 20 max entries. Avoid any contest with an entry fee over $3 (the friend says professionals are barred from small-fee contests under $3, not verified by us).

### Checked by Jarvis on the vendors' own pages, 2026-11-13 (page text only)
- Daily Fantasy Fuel: Monthly $29.99, 6 months $134.99. "Try free for 7 days" on both plans. Credit card required: NOT STATED. Auto-renew: NOT STATED. Projection download: mentioned, file format NOT STATED. Ownership export: NOT STATED. Refunds: NOT STATED. Has DK and FanDuel optimizers with stacking controls and 1-click export to DK.
- DFS Army: no free trial stated (a "Free Month" link with no terms shown). Listed prices per month: LITE, Core-4 and All Football $69.99, VIP $99.99, VIP and Player Props $119.99. All memberships auto-renew, cancel anytime. Optimizer builds 3 to 300 lineups with exposure controls. Research Station is a downloadable Excel or Sheets file. CSV and ownership export: NOT STATED.
- Zac signs up himself. Agents never create accounts, enter payment details or enter lineups.
