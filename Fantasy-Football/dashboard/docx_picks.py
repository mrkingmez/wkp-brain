"""Parses the model's ATS picks out of the weekly
'Pickups 2026 - Week {N}.docx' -- the pure-model source, no human
input, per Zac's naming spec (2026-09-13).

Only Section 1 ("PICK'EM - AGAINST THE SPREAD") is parsed. The doc also
carries a straight-up-winners tier list (Locks/Solid/Lean/Coin flip)
and a full IRFL lineup writeup -- both real, both present, neither
parsed here. Scope: this file makes the ATS picks (the ones that map
directly onto predictions.csv's schema) readable; the other two
sections are a follow-up, not silently dropped -- see
parse_model_ats_picks()'s docstring.

Real format, confirmed against Week 1 (20/20 lines matched cleanly):
    "{Away} at {Home}. Card {..}, mkt {..} ({..}). PICK: {Team} {+/-N} (...)."
"""
import re
from pathlib import Path

import docx

PICK_LINE_RE = re.compile(
    r"^(.+?) at (.+?)\.\s.*?PICK:\s*([A-Za-z.' ]+?)\s+([+-]\d+(?:\.\d+)?)\s*\("
)


def parse_model_ats_picks(path: Path) -> list[dict]:
    """Returns [{away, home, pick_team, pick_line}], one per game.
    pick_line is signed FROM THE PICKED TEAM'S OWN PERSPECTIVE (matches
    how the doc itself writes it, e.g. 'Seattle -3' or 'Denver +3') --
    NOT yet converted to this codebase's home-favored-positive
    convention. Callers (logger.py) do that conversion once they know
    home/away, the same place every other pick source does it.

    Only matches lines under the 'PICK'EM - AGAINST THE SPREAD' heading
    in practice (that's the only place this exact sentence shape
    appears in the real doc), but this does not check headings
    explicitly -- if a future week's doc uses this sentence pattern
    elsewhere, it would be picked up too. Report the count found;
    20 is the expected number for a normal week.
    """
    document = docx.Document(str(path))
    picks = []
    for para in document.paragraphs:
        text = para.text.strip()
        if not text or "PICK:" not in text:
            continue
        m = PICK_LINE_RE.search(text)
        if not m:
            continue
        away, home, team, line = m.groups()
        picks.append({
            "away": away.strip(),
            "home": home.strip(),
            "pick_team": team.strip(),
            "pick_line": float(line),
            "raw_text": text,
        })
    return picks
