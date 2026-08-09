---
description: WKP memory protocol. Read past learnings at session start, write new ones as they happen, keep everything inside the repo and in git.
---

# WKP Memory

Memory lives **inside this repo** at `memory/`. All paths below are relative to
the repo root (`D:\WKP` on the main Windows machine, a different absolute path
on the Pi later — which is exactly why nothing here is hardcoded).

## Structure

```
memory/
├── MEMORY.md            # Index. Read every session.
├── me.md                # Pointer to the real ME.md — never a second profile
├── topics/
│   └── <topic>.md       # Detailed entries by topic
└── projects/
    └── <venture>.md     # Operational learnings scoped to one venture
```

## Why the index is named MEMORY.md

Claude Code has its own native memory feature. Left alone, it writes an index
called `MEMORY.md` plus flat topic files into
`C:\Users\<user>\.claude\projects\D--WKP\memory\` — outside the repo, invisible
to git, stranded on one machine.

That folder is now a **directory junction** pointing at `D:\WKP\memory\`. Native
writes land in the repo automatically. Matching its index filename means the
native system and this protocol share one index instead of fighting over two.

Never "fix" this by writing to the `C:\Users\...` path directly. It is the same
folder. Write to `memory/`.

---

## CRITICAL: memory vs. CLAUDE.md routing

This rule is what keeps the system from rotting. Get it wrong and it recreates
the unmerged-patch-file decay that killed the first Second Brain.

**Goes in a venture CLAUDE.md** — things Zac decided on purpose:
- Strategy, positioning, pricing, priority order
- Locked creative rules and formats
- Project status, canon, cast, plot structure
- Workflows he asked for by name

**Goes in memory** — things Claude figured out:
- Tool behavior, bugs, workarounds, error fixes
- "We tried X, it broke because Y, do Z instead"
- Hardware and environment facts about a specific machine
- Working patterns noticed in passing

**Goes in LOCAL-PATHS.md** — machine-specific file locations. Never memory.

**When it belongs somewhere other than memory, say so out loud in the same
turn.** Do not silently file a decision into memory. Name the file that needs
updating. Never let changes accumulate to be merged later.

---

## Agent-Initiated Actions (Claude runs these — the user does not ask)

### `load` — session start

1. Read `memory/MEMORY.md`
2. Follow pointers to any topic files relevant to the work at hand
3. If working inside a venture folder, check `memory/projects/<venture>.md`
4. Hold that context. Do not recite it back unless asked.

Files are small. Read them directly. Only spawn a background agent if `topics/`
grows past roughly ten files:

```
Task(subagent_type="general-purpose", run_in_background=true, prompt="""
Memory load. Read memory/MEMORY.md and any relevant topic files.
Return a brief context summary for the main agent.
""")
```

### `save` — persist a learning

1. Pick an existing topic where one fits. Do not invent a new topic for
   something that belongs in an old one.
2. Append to `memory/topics/<topic>.md`:
   ```markdown
   ## <Short title> [YYYY-MM-DD]
   <What happened, why, and what to do instead. 1-3 sentences.>
   ```
3. Add or update the pointer line in `memory/MEMORY.md`:
   ```markdown
   - [<Short title>](topics/<topic>.md) — <one-line summary>
   ```
4. Prompt Zac to commit and push at a natural stopping point. Memory that is
   not pushed does not exist on any other machine.

### `recall` — retrieve context

Grep `memory/MEMORY.md`, follow the pointers, read the matching topic files,
return only what bears on the question. Can block if needed immediately.

---

## User Commands

- `/mem show` — list `memory/`, print `MEMORY.md`, show the first lines of each
  topic file
- `/mem forget <topic>` — delete the topic file and its index line. Confirm with
  Zac first. Git history still holds it.

## When to save

- Zac says "remember", "note that", "this is always", "don't forget"
- A non-trivial problem gets solved, especially a tool bug or environment fix
- A working preference surfaces that is not already written down
- A pattern shows up across more than one session

## When to recall

- Starting unfamiliar work in a venture
- Stuck on something that smells previously hit
- Zac asks "do you remember", "didn't we try this", "what happened with"

## Principles

- **Repo-local**: memory lives in git, never only in a home directory
- **One index**: `MEMORY.md`, shared with Claude Code's native memory
- **Categorized**: everything gets a topic, no dumping ground
- **Atomic**: one `##` block is one memory
- **Routed**: decisions to CLAUDE.md, paths to LOCAL-PATHS.md, learnings here
- **Editable**: plain markdown, Zac can open and fix any of it
