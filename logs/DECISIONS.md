# Decision Queue

Agents append. Zac clears. Nothing else writes.



**Blocked:** what cannot proceed

**Options:** A / B / C

**Recommendation:** which and why

**Status:** OPEN | DECIDED: <answer>

---

## [WWD-2026-08-20-01] 2026-08-20 | WWD | No devils-advocate agent exists to review WWD packages before ship

**Blocked:** WWD director protocol requires handing every draft to a
devils-advocate agent with the format spec path before anything ships. That
agent type does not exist in this environment's available roster (only claude,
claude-code-guide, Explore, general-purpose, Plan, statusline-setup,
wwd-director). Not a one-off, this will recur on every future WWD package,
review, and script unless resolved.

**Options:**
A. Build a proper devils-advocate agent definition (.claude/agents/) so future
   runs get a real, purpose-built adversarial reviewer.
B. Standardize on using general-purpose with an explicit adversarial-review
   prompt as the permanent substitute, and update WWD/CLAUDE.md's hard rule to
   say so plainly instead of naming an agent that doesn't exist.
C. Leave it ad hoc, each director run decides in the moment (current state,
   not sustainable, inconsistent review quality).

**Recommendation:** A. This session's stand-in (general-purpose, briefed
adversarially) caught four real issues (em dashes in internal notes, an
unverifiable host attribution, two chapter-title inconsistencies, one
cherry-picked stat), so the review step has proven value. A dedicated agent
definition would make that review consistent run to run instead of depending
on how well each director happens to brief a generic substitute.

**Status:** DECIDED: Option A. devils-advocate.md created in .claude/agents/ 20 AUG. Needs its two exit tests run before trusting.

---

## [SYS-01] 2026-08-19 | SYSTEM | Agent files arriving HTML-escaped
**Issue:** All 4 agent .md files written with &#x20; instead of
spaces and backslash-escaped markdown (\#, \*, \-). Fixed manually
in VS Code. wwd-director hit this twice.
**Suspected cause:** content copied from rendered view rather than
raw code block.
**Next time:** use the code block copy button, then verify with
`type <file>` before trusting it.
**Status:** OPEN - watch for recurrence