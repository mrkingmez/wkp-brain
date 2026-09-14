"""Parses the weekly pick'em card (.xls).

Confirmed layout:
  col 0 = EC marker cell (next to the favored team) -- marked with
          literal 'X' text, confirmed on the real submitted Week 1
          card (row 21, Jacksonville).
  col 1 = FAVORED team name (ALL CAPS if that team is the home team)
  col 2 = SPREAD (number), OR a section-header string like
          'NFL ( 9 September)' / 'NCAA ( 12 September)' /
          'Monday Night Tie Breaker ( 14 September)' when cols 1 and 3
          are both blank on that row
  col 3 = UNDERDOG team name
  col 4 = second EC marker column -- confirmed always blank on every
          real card checked so far; carried through in case a future
          week's template actually uses it.

PICK MARKING -- RESOLVED 2026-09-13 (was decision FF-2026-09-12-01,
now closed). Zac confirmed: picks are marked by FILLED CELL BACKGROUND
COLOR on the favored (col 1) or underdog (col 3) cell, not by text.
Verified directly against the real submitted Week 1 card
(Sanders_Week1 Entry.xls): all 20 picks (19 games + the Monday-night
tiebreaker) showed exactly one of col1/col3 filled, zero rows with
zero or multiple fills.

CORRECTED 2026-09-13 (same day, Zac's follow-up): the two colors found
on the real card are not "inconsistent tooling" -- they're meaningful.
Green (RGB confirmed as (0, 128, 128) on the actual file -- Zac's own
word for it is "green", carried through as this codebase's label even
though it reads as teal in RGB) marks a picked-but-ungraded cell. Zac
then RECOLORS that same cell red (RGB (221, 8, 6)) by hand once he's
decided the pick lost. So: any fill still identifies the pick (team
identification was already correct and needed no rework), but the
SPECIFIC color is also captured as Zac's own outcome hint -- and it is
explicitly NOT authoritative. ESPN's score is what grades a pick
(here and everywhere else in this codebase); the color is compared
against that real result only to catch a discrepancy. Real one found
immediately on the actual card: SEATTLE is marked red (Zac's-loss) but
the real result was an exact push (SEA won by 3, the spread was 3) --
not a loss. Surfaced, not silently trusted either way.

Color matching is done by RGB, not by xlrd's raw palette index --
palette indices are workbook-local and are not guaranteed to mean the
same color in a different week's file, even though the same actual
colors are almost certainly reused.
"""
import re
from pathlib import Path

import xlrd

SECTION_RE = re.compile(r"^(NFL|NCAA|Monday Night Tie ?Breaker)\s*\(\s*([^)]+)\)", re.I)

# RGB -> Zac's own outcome-hint label. Confirmed against the real Week 1
# card. Any other non-default fill color found is reported as
# "unknown_color" rather than guessed at -- these are the only two
# colors actually observed and confirmed by Zac so far.
FILL_COLOR_HINTS = {
    (0, 128, 128): "ungraded",   # Zac's "green" -- picked, not yet graded by hand
    (221, 8, 6): "loss",         # Zac recolors here by hand once he's decided the pick lost
}


def find_current_week_card(cards_dir: Path, codename: str, week: int) -> Path | None:
    candidate = cards_dir / f"{codename}_Week{week} Entry.xls"
    if candidate.exists():
        return candidate
    # loose fallback: any file matching the week number, in case the
    # codename changes -- report what was found, don't guess further.
    matches = list(cards_dir.glob(f"*Week{week}*Entry.xls"))
    return matches[0] if matches else None


def _cell_fill(sheet, xf_list, colour_map, row: int, col: int) -> tuple[bool, tuple | None, str | None]:
    """Returns (is_filled, rgb, color_hint)."""
    xf_index = sheet.cell_xf_index(row, col)
    pci = xf_list[xf_index].background.pattern_colour_index
    if pci in (None, 64, 65):
        return False, None, None
    rgb = colour_map.get(pci)
    hint = FILL_COLOR_HINTS.get(rgb, "unknown_color")
    return True, rgb, hint


def _resolve_pick(favored: str, underdog: str, fav_fill: tuple, dog_fill: tuple) -> dict:
    fav_filled, fav_rgb, fav_hint = fav_fill
    dog_filled, dog_rgb, dog_hint = dog_fill
    if fav_filled and dog_filled:
        return {"pick": "ambiguous", "pick_team": None, "pick_color_rgb": None, "pick_outcome_hint": None}
    if fav_filled:
        return {"pick": "favored", "pick_team": favored, "pick_color_rgb": fav_rgb, "pick_outcome_hint": fav_hint}
    if dog_filled:
        return {"pick": "underdog", "pick_team": underdog, "pick_color_rgb": dog_rgb, "pick_outcome_hint": dog_hint}
    return {"pick": None, "pick_team": None, "pick_color_rgb": None, "pick_outcome_hint": None}


def read_card(path: Path) -> dict:
    wb = xlrd.open_workbook(str(path), formatting_info=True)
    sheet = wb.sheet_by_index(0)
    xf_list = wb.xf_list
    colour_map = wb.colour_map

    games = []
    tiebreaker = None
    section = None
    section_date = None

    for r in range(sheet.nrows):
        col0 = str(sheet.cell_value(r, 0)).strip()
        col1 = str(sheet.cell_value(r, 1)).strip()
        col2_raw = sheet.cell_value(r, 2)
        col2 = str(col2_raw).strip()
        col3 = str(sheet.cell_value(r, 3)).strip()
        col4 = str(sheet.cell_value(r, 4)).strip() if sheet.ncols > 4 else ""

        m = SECTION_RE.match(col2) if col2 and not col1 and not col3 else None
        if m:
            section = m.group(1).upper().replace("TIE BREAKER", "TIE BREAKER")
            section_date = m.group(2).strip()
            continue

        if section and section.startswith("MONDAY"):
            # Tiebreaker section has TWO col1+col3-populated rows, not one:
            # the game itself (favored/spread/underdog, same shape as a
            # regular game row), then a second row below it holding the
            # predicted final score for each team in col1/col3 (confirmed
            # against the real submitted card 2026-09-13 -- e.g. '24.0' /
            # '19.0' for Kansas City / Denver, NOT a single combined total
            # in some other column as the blank template's structure alone
            # suggested). Real bug caught here: an earlier version treated
            # ANY col1+col3 row in this section as a fresh tiebreaker game,
            # so the score-prediction row silently clobbered the real one.
            if col1 and col3 and tiebreaker is None:
                fav_fill = _cell_fill(sheet, xf_list, colour_map, r, 1)
                dog_fill = _cell_fill(sheet, xf_list, colour_map, r, 3)
                tiebreaker = {
                    "favored": col1,
                    "spread": _to_float(col2_raw),
                    "underdog": col3,
                    "home_is_favored": col1.isupper(),
                    "row": r,
                    "predicted_favored_score": None,
                    "predicted_underdog_score": None,
                    **_resolve_pick(col1, col3, fav_fill, dog_fill),
                }
            elif col1 and col3 and tiebreaker is not None:
                tiebreaker["predicted_favored_score"] = _to_float(col1)
                tiebreaker["predicted_underdog_score"] = _to_float(col3)
            continue

        if col1 and col3 and section in ("NFL", "NCAA"):
            fav_fill = _cell_fill(sheet, xf_list, colour_map, r, 1)
            dog_fill = _cell_fill(sheet, xf_list, colour_map, r, 3)
            games.append({
                "section": section,
                "section_date": section_date,
                "favored": col1,
                "spread": _to_float(col2_raw),
                "underdog": col3,
                "home_is_favored": col1.isupper(),
                "ec_marked": col0.strip().upper() == "X" or col4.strip().upper() == "X",
                "row": r,
                **_resolve_pick(col1, col3, fav_fill, dog_fill),
            })

    all_rows = games + ([tiebreaker] if tiebreaker else [])
    zero_filled = [g for g in all_rows if g["pick"] is None]
    multi_filled = [g for g in all_rows if g["pick"] == "ambiguous"]
    any_ec_marked = any(g["ec_marked"] for g in games)

    return {
        "source_file": str(path),
        "games": games,
        "tiebreaker": tiebreaker,
        "ats_pick_marking_confirmed": True,
        "ats_pick_note": "Picks marked by filled cell color on the favored/underdog cell -- resolved 2026-09-13.",
        "picks_parsed": sum(1 for g in all_rows if g["pick"] in ("favored", "underdog")),
        "rows_total": len(all_rows),
        "zero_filled_rows": [{"favored": g["favored"], "underdog": g["underdog"], "row": g["row"]} for g in zero_filled],
        "multi_filled_rows": [{"favored": g["favored"], "underdog": g["underdog"], "row": g["row"]} for g in multi_filled],
        "eliminator_pick": next((g for g in games if g["ec_marked"]), None),
        "no_picks_detected": not any_ec_marked and not any(g["pick"] for g in all_rows),
    }


def _to_float(v) -> float | None:
    try:
        return float(v)
    except (TypeError, ValueError):
        return None
