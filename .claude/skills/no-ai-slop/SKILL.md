---
name: no-ai-slop
description: >
  Content-quality gate for anything WKP publishes publicly - social posts,
  video titles/descriptions, sponsor reads, Etsy listings, thumbnails,
  pinned comments, emails to sponsors/press, any copy a stranger will read.
  Enforces Zac's two writing rules - no em dashes, nothing generic - and
  strips the broader patterns that read as AI-written. Run this on a draft
  before it ships, not after. Trigger on "going public," "before we post
  this," "ready to publish," "final copy," or when handing off any
  social/sponsor/listing copy for approval. NOT for internal notes, TASKS.md,
  memory files, or anything Zac reads but nobody else does.
---

# No AI Slop

A pass-before-you-ship checklist. Every piece of public-facing WKP copy runs
through this - sponsor reads, social posts, video descriptions, Etsy
listings, thumbnails, pinned comments, sponsor emails. Internal files (TASKS,
memory, logs, decisions) are exempt - this is for anything a stranger reads.

## Rule 1 - No em dashes. Zero. Ever.

Zac's standing writing rule, first locked for Shattered Empire
(2026-07-24), now general to everything public. Find every `—` (em dash)
and every double-hyphen `--` used as a dash, and rewrite the sentence
without one. Do not just swap it for a comma if a comma changes the meaning
- actually restructure the sentence. Usual fixes:

- Split into two sentences.
- Use a comma if the clause is genuinely a light aside.
- Use a colon if what follows is an explanation or a list.
- Use parentheses if it's a true aside that could be cut.
- Just rewrite it as one clean sentence.

Search for the character literally before declaring a draft clean - do not
eyeball it, em dashes hide easily in a wall of text.

## Rule 2 - Nothing generic

If a sentence could sit unchanged in literally any other channel's video, any
other brand's Etsy listing, or any other podcast's sponsor read, it's
generic - cut it or make it specific to WKP/WWD. Concretely:

- **Name real things.** The actual movie, the actual character, the actual
  product feature, the actual number. Not "an iconic scene" - the scene.
  Not "great deals" - the actual price or offer.
- **Cut throat-clearing.** No "In today's world," "Let's dive in," "Without
  further ado," "At the end of the day." Start where the actual content
  starts.
- **Cut AI tells.** Banned words/phrases unless a real person would actually
  say them out loud: *elevate, unlock, game-changer, testament to, boundaries
  (as in "pushing boundaries"), unleash, dive into, delve into, in the realm
  of, when it comes to, it's important to note, whether you're X or Y, not
  just X but Y, seamless(ly), robust, cutting-edge, ever-evolving, tapestry,
  journey (unless it's an actual trip).*
- **Cut the rhetorical-question hook** ("Ever wonder why...?") unless the
  actual hosts would actually open that way on camera - check against how
  they actually talk, not how ad copy usually opens.
- **Kill hedge-everything language.** "Might," "could potentially," "in some
  ways" - say the thing.
- **Sound like the actual people.** WWD copy should sound like Zac/KingZ and
  Matt/Winter Wolf specifically - buddy-cop, opinionated, nerd-culture
  fluent - not like a brand voice guide's idea of "casual and fun." If a line
  could be read by any YouTuber on any channel, it's not specific enough yet.

## How to run it

1. Read the full draft once for content, not editing yet.
2. Search literally for `—` and `--` - fix every hit per Rule 1.
3. Re-read line by line against the Rule 2 list - cut/replace every generic
   phrase or banned word.
4. Read it out loud (or imagine it read out loud for a sponsor read/video
   script) - if it doesn't sound like a real person talking, it's still
   slop.
5. Note what you changed in one line when you hand it back, so whoever
   asked can see the delta rather than re-diffing the whole thing.
6. If the piece has a paired `.docx` (per root CLAUDE.md's output-document
   rule), regenerate it from the cleaned `.md` so the two never drift -
   `python D:\WKP\.claude\skills\no-ai-slop\scripts\md_to_docx.py <in.md>
   <out.docx>`. It's a light converter (headers, bold/italic/code, quotes,
   bullets, rules) - good enough for these working docs, not a full
   CommonMark parser.

## Do not

- Skip this for something small - a pinned comment or pinned reply is still
  public.
- Apply this to internal files (TASKS.md, memory, decision logs, agent
  reports). Those are working documents, not public copy.
- Soften a real claim's accuracy while cutting generic language - Rule 2 is
  about specificity and voice, not about adding hype. Cutting slop should
  never make a claim less true.
