# WARRIOR KING PRODUCTIONS — CHANNEL FRAMEWORK
### Handoff Document — Session Summary

---

## 1. WHAT THIS SESSION BUILT

WKP now has three distinct video formats, a shared research methodology underneath all of them, and a pilot recommendation for the newest format. This document is the single reference point for the whole shape.

**Related files produced this session:**
- `Military-Research-Master-Prompt.md` — the shared research standard all three formats run through
- `AAR-Format-Module.md` — the AAR Commander format module, with Fort Necessity as the worked example

---

## 2. THE THREE FORMATS

### What If
*(Note: earlier drafts of this project referred to this format internally as "Watershed" — that label is retired. Use "What If" going forward.)*

Pivotal historical events or battles — Battle of the Bulge, JFK assassination — researched heavily, then projected forward to show how the present would differ if the event had gone the other way.

**New addition this session:** an "other side could have won" segment. Rules for it:
- Must be built from real capability the losing side actually had available at that moment — position, timing, assets, decisions on the table. No modern tactics transplanted backward.
- Runs through the same four-band evidence tagging as everything else, and is explicitly labeled [SPECULATIVE] on screen since it's reasoning, not research.
- Not mandatory in every episode. Only include it where the counterfactual is genuinely strong. Forcing it into episodes where it isn't earns a fabricated branch — the exact failure mode the research rules exist to prevent.
- Can use the master prompt's Causation Test in reverse: shortest defensible chain of plausible changes that flips the outcome. Shorter chain = stronger segment. Say so honestly when the chain is long and weak.

### Hidden Hinge
The battle everyone credits vs. the lesser-known engagement that actually carried the causal weight. Runs on the master prompt's Causation Test (Section 8) applied adversarially to the famous event, and the full research pass applied to the real hinge.

**Screening tip:** run the causation-only prompt variant against a candidate before committing research time. If the causal chain collapses under an adversarial pass, the idea is dead cheaply — cheaper than the five-axis score catches this specific failure mode.

### AAR Commander
A battle run through a full military After Action Review, facilitated by someone who's actually sat in that room. Full structure and rules in `AAR-Format-Module.md`. Summary of the four-question spine:

1. **What was supposed to happen** — the plan, in the commander's own documented words where preserved. Reverse-engineering intent from the outcome is forbidden.
2. **What actually happened** — phase-by-phase breakdown, tagged across four failure classes: friction, enemy action, command failure, institutional failure. Ends at the point of no return.
3. **Takeaways — Sustain / Improve** — sustain is what was right regardless of outcome; improve is period-legal fixes only, each one tagged with the echelon that actually owned it.
4. **Retrain, Refight, Verify** — three-test check (was the lesson available / was it identified / was it institutionalized) verified against the commander's next engagement. Five possible verdicts, with `LEARNED — NOT INSTITUTIONALIZED` flagged as the most common and most interesting real-world result.

**Governing rules unique to this format:**
- No invented dialogue or interior thought, ever. Participants speak only through documented statements.
- All improve items must be period-legal — achievable with the technology and doctrine actually available at the time.
- Unit of analysis is the command relationship (whoever actually owned the decisions), not a fixed military echelon — flexes from a single commander-and-host (ancient armies) to a commander across a partially-controlled mixed force (Washington at Fort Necessity).

---

## 3. HOW THE FORMATS RELATE

Each format answers a different question about the same underlying premise — what actually decided this, and could it have gone another way:

| Format | Core question |
|---|---|
| What If | Did this event redirect history, and by how much? |
| Hidden Hinge | Is the credited event even the right one? |
| AAR Commander | Did the people involved get better — or did the system refuse to let them? |

All three run through the same underlying research discipline (four-band evidence tagging, citation discipline, period-legal constraints, no manufactured balance, multi-national historiography). That shared spine is what makes this a channel identity rather than three unrelated series.

---

## 4. THE SHARED RESEARCH METHODOLOGY

Full document: `Military-Research-Master-Prompt.md`

Key mechanisms all three formats draw on:

- **Four-band evidence tagging:** [ESTABLISHED] / [SUPPORTED] / [CONTESTED] / [SPECULATIVE] — replaces false-precision confidence percentages
- **Claim-type source matching** — source authority depends on what's being claimed (a soldier's diary has authority over ground conditions, not command intent), not a fixed source hierarchy
- **Battlefield Reconstruction** with its own four-tag system: [SOURCED] / [COMPUTED] / [INFERRED] / [UNKNOWN] — the section most prone to fabrication, so "unknown" showing up often is a sign of honesty, not a gap
- **Causation Test** — adversarial pass against inflated causal claims; core engine for Hidden Hinge and the What If reverse-branch
- **Citation discipline** — top-priority rule; unverifiable citations get flagged "attribution uncertain" rather than invented
- **Multi-national historiography required** — no defaulting to Anglophone/American academic sources alone
- **No modern moral framework imposed on historical actors**
- **Scope scaling** — depth matches the engagement's actual significance, not a fixed template length

---

## 5. AAR COMMANDER — PILOT RECOMMENDATION

**Recommended pilot: the Hannibal arc — Trebia (218 BC) → Lake Trasimene (217 BC) → Cannae (216 BC)**

Rationale:
- Same commander across all three, refining the same core idea (draw in, envelop, destroy) with increasing sophistication — this runs the Q4 verification test three times *within a single pilot*, without needing a second episode to prove the format works
- Strong documented reasoning on both sides via Polybius (closer to contemporary) and Livy (later, more moralizing) — good material for the format's bias-flagging rules
- Avoids the weak point of going earlier than this: pre-Greek battle accounts (Sumerian, Egyptian, Assyrian) are largely royal propaganda with little preserved command reasoning, which would push Q1 mostly into [UNKNOWN]/[SPECULATIVE] and make for a weak pilot

**Natural follow-on episode:** did Rome learn from Cannae? Scipio at Zama (202 BC) explicitly studied Hannibal's methods before beating him with them — institutional learning at the losing side's level, verified against the man who taught the lesson.

**Open structural question flagged, not yet resolved:** the Zama case is a different shape than the format's current unit-of-analysis rule (same commander, learn/didn't-learn). Zama is same *institution*, different *commander*, studying an *enemy's* method rather than reviewing their own failure. Worth deciding whether this is a variant of AAR Commander or a distinct sub-format before it comes up again — it will, once the channel moves forward in time and command relationships become more institutional (national armies, general staffs) rather than individual.

---

## 6. STANDING PILOT FROM EARLIER SESSIONS (for chronology context)

Note from prior work in this project: **Fort Necessity (July 1754, George Washington)** was previously identified as the AAR Commander pilot, with **Monongahela (1755)** as its verification engagement — same command-relationship structure (Washington across a mixed, partially-controlled force), same three-test learn/didn't-learn arc, already fully worked out in `AAR-Format-Module.md`.

**This creates a sequencing decision to make:** the chronological-arc idea (start in BC, move forward, document tactical evolution) argues for Hannibal first. The prior groundwork argues for Fort Necessity, since it's already fully scoped as a worked example in the format module. Both are strong; this hasn't been decided yet and is worth resolving before locking a production calendar.

---

## 7. OPEN ITEMS / NOT YET DECIDED

- **Pilot sequencing:** Hannibal (per chronological-arc logic, this session) vs. Fort Necessity (already fully worked out as the format module's example, from earlier sessions)
- **What If "other side wins" segment:** confirmed as conditional/not-mandatory, but no formal criteria yet for what makes a counterfactual "strong enough to earn it" — worth defining before the first episode that includes it
- **Zama-type cases:** institutional-learning-from-an-enemy is structurally different from the current AAR Commander unit-of-analysis rule; not yet resolved whether it's a variant or a new sub-format
- **Channel bible:** proposed but not yet built — a single document stating all three formats side by side with shared rules, for future reference. Still on the table whenever you want it.
