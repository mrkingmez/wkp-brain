---
name: reference-name-search-limits
description: What works and what does not for business-name / trademark conflict flags from this agent (no page fetch, USPTO and GA SOS not live-queryable)
metadata:
  type: reference
---

Name-conflict runs (first one 2026-11-10, photo restore + transcription names, output `research\ventures\brand-kits\clearance-name-flags.md`):
- No page-fetch tool here. USPTO tmsearch and GA SOS ecorp cannot be queried live, mark both NOT AVAILABLE.
- Usable substitutes: WebSearch hits on markinton.com, trademark.justia.com, gleanmark.com, ttabvue.uspto.gov; restrict GA entities with allowed_domains ecorp.sos.ga.gov / bizapedia.com. Mirrors are not authoritative, tell Zac to confirm in TSDR.
- WebSearch ignores exact-phrase quotes, so "no hits" is not "no conflict".
- Known result: PROOFED is registered (reg 6783849) for proofreading and used for transcript proofreading, so any "Proofed" transcription name is a CONFLICT.
