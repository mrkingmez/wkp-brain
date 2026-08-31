> NAMING NOTE, 30 AUG 2026: "Watershed" is RETIRED. This format is now
> "What If". The methodology below is unchanged and remains authoritative.
> Only the name changed. Superseded by WKP-Channel-Framework-Handoff.md
> on naming, not on method.

# Warrior King Productions — What If SOP (v3)

### Format A (What If) + Format B (Hidden Hinge) — Corrected \& Locked

\---

## LOCKED DEFINITIONS — read this before anything else

**Format A — "What If."** A single major event that changed the world, for better or worse. Not battle-exclusive — JFK is the model case, but a battle can also be a Watershed event if it's genuinely a fork with a predictive-branch structure (e.g., "what if Midway went to Japan"). The defining feature is a **forward-looking predictive branch model** from a real historical fork.

**Format B — "Hidden Hinge."** Specifically battles/military events. Not a branching prediction — a **backward-looking causal-chain correction**. "You were taught battle X mattered because of outcome Y. Battle Z, same era, actually drove more of Y. Here's the dependency chain, and here's what happens to X if Z goes differently."

The difference that matters: **A predicts forward from an open fork. B re-traces backward through a chain that's already resolved.** Don't build A's branch-probability machinery into a B episode — B needs the causal-dependency case, not a percentage.

\---

## FORMAT A: THE PREDICTIVE MODEL METHODOLOGY

This is the actual answer to "I don't want you just telling me what you think would happen." Here's the structured process, and the spreadsheet that operationalizes it.

### Step 1 — Baseline Reconstruction

Document the real historical trajectory first, fully sourced. This is ground truth — you cannot model a divergence from a point you haven't accurately established.

### Step 2 — Variable Identification

Identify the specific causal variables active at the divergence point: political, military, economic, and personal/leadership factors. Pull these from primary sources — memos, orders, declassified cables, recorded conversations, contemporaneous reporting — not general summaries.

### Step 3 — Reference Class Forecasting

Find historical analogues: other moments where a similar leader or system faced a similar fork, and see empirically how those tended to resolve. This is the step that separates a real forecasting method from a guess — it's the core technique professional forecasters (Philip Tetlock's "superforecasters," intelligence community estimative analysis) use to outperform pure intuition: anchor your probability estimate in an actual historical base rate, not a vibe.

### Step 4 — Branch Construction

Build at least 2-3 explicit branches, each conditioned on specific named variables. Not "maybe this, maybe that" — "if variable X holds AND Y follows historical pattern, branch 1 results; if X holds but Z breaks from pattern, branch 2 results."

### Step 5 — Score It (the spreadsheet)

Open **WhatIf-Predictive-Model.xlsx**. For every variable from Step 2, score:

* **Importance (1-5):** how much this factor actually matters to the outcome
* **Confidence (1-5):** how solid the sourcing behind this factor is
* **Branch Support (1-5 per branch):** how strongly this factor points toward each branch

The sheet computes a weighted score and a normalized probability-style percentage per branch automatically. The JFK Example tab is fully worked — study it before building your own.

### Step 6 — Devil's Advocate Stress Test

Apply your existing SOP step here, specifically against the highest-scoring branch. Attack its weakest assumptions on purpose. If the branch survives, your confidence in it goes up; if it doesn't, adjust the scores and recompute.

### Step 7 — Sensitivity Check

Temporarily zero out one factor's Importance score and watch how much the percentages move. A factor that swings the result a lot is "load-bearing" — that's the single biggest uncertainty in your model, and it should be named on-screen, not hidden. This is what makes the model intellectually honest instead of just persuasive.

### Step 8 — Trace Forward with Checkpoints

Once you have your highest-probability branch, trace it forward with explicit checkpoints — your 5-year mark with up to three specific developments, then continuing outward. Keep referencing back to which Step 2 variables are driving each new development, so the audience can follow the reasoning chain, not just the narrative.

### Step 9 — State the Verdict as a Model Output, Not an Opinion

On-screen, this should read closer to "our model weights this branch at roughly 37% against two competing branches near 31% each, driven primarily by \[the load-bearing factor from Step 7]" — not "here's what probably happened." Show the machinery.

\---

## FORMAT B: THE HIDDEN HINGE WORKSHEET

Open the **Hidden Hinge Worksheet** tab in the same spreadsheet file. It's eight questions, not a branch model:

1. The famous battle (X) — what outcome is it credited with?
2. The overlooked battle (Z) — what actually happened?
3. What factors drove Z's outcome?
4. How does Z causally feed into the conditions that produced X?
5. If Z had gone differently — does X still happen, happen differently, or never happen?
6. What does popular history get wrong about X's actual significance?
7. What do multiple countries' historiographies say about X and Z (not just one nation's textbooks)?
8. Historical Plausibility Score (1-10) for your causal-chain claim, and why.

Answer all eight, sourced, before scripting. That's your Devil's Advocate pass built into the structure itself.

\---

## RESEARCH PROMPT — FORMAT A (updated)

```
I'm building a Format A What If episode on: \[EVENT]. This needs a real 
predictive model, not a narrative guess.

1. Reconstruct the actual historical trajectory, fully sourced, from 
   multiple countries' historiography where relevant — not just American 
   sources.
2. Identify every political, military, economic, and personal/leadership 
   variable active at the divergence point. Cite primary sources (memos, 
   orders, declassified documents, recorded conversations) wherever they 
   exist.
3. Find 2-3 reference-class analogues — other historical moments with a 
   structurally similar fork — and how they resolved.
4. Construct 2-3 explicit branches, each conditioned on named variables.
5. For each variable, propose an Importance score, Confidence score, and 
   per-branch Support score (1-5 each) I can enter into the model 
   spreadsheet, with your reasoning for each number.
6. Flag which single variable looks most load-bearing before I even run 
   the sensitivity check.
```

## RESEARCH PROMPT — FORMAT B (updated)

```
I'm building a Format B Hidden Hinge episode comparing \[FAMOUS BATTLE X] 
to \[OVERLOOKED BATTLE Z]. Answer the eight Hidden Hinge Worksheet 
questions in full, sourced from multiple countries' historiography, not 
just one national tradition. Flag anywhere historians genuinely disagree 
rather than picking a side for me.
```

\---

# MODEL RECOMMENDATIONS

Different tasks in this pipeline benefit from different model strength. Here's the actual breakdown:

|Task|Recommended Model|Why|
|-|-|-|
|Format A variable research, reference-class analysis, branch construction|**Opus** (currently Opus 5)|This is the deepest multi-step reasoning task in your whole pipeline — holding many variables, sources, and a branch structure together without losing the thread is exactly where Opus earns its cost over Sonnet.|
|Format B eight-question worksheet research|**Opus**|Same reason — causal-chain reasoning across sources is analytically demanding.|
|Scripts, captions, IG copy, shot lists|**Sonnet** (currently Sonnet 5)|Strong writing quality at much faster speed and lower cost — this is most of your day-to-day volume work.|
|Quick lookups, formatting, simple Q\&A, troubleshooting a single error message|**Haiku** (currently Haiku 4.5)|Fast and cheap for anything that doesn't need deep reasoning.|
|Bombing-mission-style production walkthroughs, SOP building|**Sonnet**, escalate to **Opus** only if a step needs genuinely hard multi-system reasoning|Sonnet handles this well; you rarely need Opus-level depth for production logistics.|

**Can I change the model, or do you have to?** You control it — there's a model selector in the chat interface, and you can switch mid-conversation. I can't switch myself mid-task, but I'll flag it when I think a step would benefit from more horsepower ("this variable-scoring pass would be stronger on Opus, want to switch before we run it?") so you know when it's worth the swap.

\---

# NEXT UP: TRADING COMPANY + SPORTS TOOL

Both are real builds, not content SOPs — worth their own dedicated pass rather than a rushed add-on here.

**Trading company SOP** — I'll need to know: what kind of trading (day trading, swing, options, a specific asset class), and whether this is research/analysis support or something touching actual trade execution (which I can't execute on your behalf, only inform).

**Sports "self-updating status" tool** — this is genuinely a different kind of build than a content SOP; it sounds like you want a live tracker (something closer to the interactive spreadsheet/artifact tools I just built for Watershed) that updates as roster/injury data changes, not a one-time writeup. I can pull live team/player data through a sports-data tool I have access to. Tell me which sport/league and what "status" should track (playoff odds, roster strength, injury impact) and I'll scope it properly next.

Want to tackle trading or sports first?

