"""IRFL scoring function -- Section 3 of FF-SCORING-RULES.md.

One function, all positions, driven entirely by league-scoring-rules.json
(built from Section 1, cross-checked 2026-09-13 against the live MFL
TYPE=rules/allRules exports -- zero point-value disagreements found).

Used for:
1. Sleeper projections -> a real IRFL projection for lineup decisions.
2. Sleeper weekly actuals -> same math, so projected vs. actual compares
   under identical rules.
3. Dashboard live scoring -- for projections/post-game analysis only.
   MFL's own liveScoring export is authoritative during games; this
   function does not second-guess it.

NEVER read pts_ppr/pts_half_ppr/pts_std for any position -- those are
Sleeper's own default format and materially disagree with the IRFL's
real rules (verified: Fred Warner at 7.23 projected tackles scored
pts_ppr 0.5; under these rules the same projection is ~7 points).

Every rule with no confident Sleeper field mapping is logged rather
than silently skipped or guessed at -- see the 'low'/'unscorable'
confidence entries in league-scoring-rules.json. Their notes explain
the specific gap; this function surfaces them at call time via the
`unscored` list on the result rather than folding them into the total.
"""
import json
from dataclasses import dataclass, field
from pathlib import Path

RULES_PATH = Path(__file__).parent / "league-scoring-rules.json"


@dataclass
class ScoreResult:
    total: float
    breakdown: dict = field(default_factory=dict)   # rule -> points contributed
    unscored: list = field(default_factory=list)     # rules this call could not score, with why
    low_confidence_used: list = field(default_factory=list)  # rules scored using an unconfirmed field


class DuplicateFieldMapping(Exception):
    pass


def load_rules(path: Path = RULES_PATH) -> list[dict]:
    """Guard added 2026-09-13: 'idp_def_td' is a combined Sleeper bucket
    that can plausibly represent an interception-return TD, a defensive
    fumble-recovery TD, or a blocked-kick-return TD -- MFL pays 6 points
    for every one of those under a different rule (#IR/#DR/#BF/#MF/#BP).
    Mapping the same Sleeper field to more than one of those rules would
    silently double- (or triple-) count a single real touchdown. This
    check makes that impossible rather than relying on nobody ever doing
    it by accident: any non-null sleeper_field claimed by more than one
    rule aborts the load."""
    data = json.loads(path.read_text(encoding="utf-8"))
    rules = data["rules"]

    claims: dict[str, list[str]] = {}
    for r in rules:
        sfield = r.get("sleeper_field")
        if sfield:
            claims.setdefault(sfield, []).append(r["rule"])
    duplicates = {f: names for f, names in claims.items() if len(names) > 1}
    if duplicates:
        raise DuplicateFieldMapping(
            "One or more Sleeper fields are mapped to multiple rules -- this would double-count "
            f"real events. Fix league-scoring-rules.json before scoring anything: {duplicates}"
        )

    return rules


def describe_gaps(rules: list[dict] | None = None) -> list[dict]:
    """The unscorable/low-confidence rule list is static -- identical on
    every score_player() call regardless of which player was scored.
    Call this once to see the full gap list rather than re-reading it
    off every individual player's result.unscored."""
    if rules is None:
        rules = load_rules()
    return [
        {"rule": r["rule"], "mfl_event": r["mfl_event"], "confidence": r["sleeper_field_confidence"],
         "note": r.get("note", "")}
        for r in rules if r["sleeper_field_confidence"] in ("low", "unscorable")
    ]


def score_player(stats: dict, rules: list[dict] | None = None) -> ScoreResult:
    """stats: a Sleeper per-player stat dict (from a projections or
    actuals payload -- same shape either way, that's the point).
    Returns points computed strictly from Section 1's rules, never from
    Sleeper's own pts_ppr/pts_half_ppr/pts_std fields (this function
    never reads those keys at all)."""
    if rules is None:
        rules = load_rules()

    result = ScoreResult(total=0.0)

    for r in rules:
        rule_name = r["rule"]
        confidence = r["sleeper_field_confidence"]
        sfield = r.get("sleeper_field")

        if confidence == "unscorable" or sfield is None:
            result.unscored.append({
                "rule": rule_name,
                "mfl_event": r["mfl_event"],
                "reason": r.get("note", "no Sleeper field mapping"),
                "candidates": r.get("sleeper_field_candidates", []),
            })
            continue

        raw = stats.get(sfield)
        if raw is None:
            # Field mapped but absent from this player's stat line --
            # normal (e.g. a WR has no pass_yd key at all). Not an error,
            # not logged as unscored; just contributes zero.
            continue

        try:
            raw = float(raw)
        except (TypeError, ValueError):
            continue  # Sleeper sometimes sends "" for a genuinely absent stat

        if raw == 0:
            continue

        pts = raw * r["points"] if r["unit"] in ("per_yard", "per_yard_of_length") else raw * r["points"]
        # per_event and per_yard both reduce to raw * points -- MFL's
        # multiplier notation ("*6", "*.04") is a straight linear rate
        # in every rule this function scores (sacks are pre-converted to
        # 3/full-sack in the rules file; see that rule's note).

        result.breakdown[rule_name] = result.breakdown.get(rule_name, 0.0) + pts
        result.total += pts

        if confidence in ("low", "high"):
            result.low_confidence_used.append({
                "rule": rule_name,
                "sleeper_field": sfield,
                "confidence": confidence,
                "points_contributed": pts,
            })

    result.total = round(result.total, 3)
    return result


def score_kicker_approx(stats: dict, rules: list[dict] | None = None) -> ScoreResult:
    """Kicker scoring needs its own path: the two FG rules
    (0-30 flat / 31-99 per-yard) can't be driven by the generic
    per-field loop above because Sleeper only gives banded FG-made
    COUNTS, not exact yardage per kick, and the bands don't align with
    the league's 30-yard cutoff. This produces an EXPLICIT approximation
    using band midpoints, flagged as such -- per FF-SCORING-RULES.md's
    own instruction to label kicker output as approximate rather than
    presenting it at the same confidence as other positions."""
    if rules is None:
        rules = load_rules()
    result = score_player(stats, [r for r in rules if r["category"] != "kicking"] +
                           [r for r in rules if r["mfl_event"] == "EP"])

    # Band midpoints for the made-FG counts Sleeper actually exposes.
    # Every kick in a band is scored at the band's midpoint, not its
    # real distance -- this is the approximation.
    band_midpoints_and_points = [
        ("fgm_0_19", 10, 3.0),     # entirely inside the flat-3 band
        ("fgm_20_29", 25, 3.0),    # entirely inside the flat-3 band
        ("fgm_30_39", 35, None),   # STRADDLES the 30/31 cutoff -- see note below
        ("fgm_40_49", 45, None),
        ("fgm_50_59", 55, None),
        ("fgm_60p", 65, None),
    ]
    fg_note = (
        "Kicker score is APPROXIMATE. Sleeper's fgm_30_39 band mixes real "
        "30-yarders (flat 3 pts here) with 31-39 yarders (0.1/yd = 3.1-3.9 "
        "pts here) -- there is no way to split them from banded counts "
        "alone. Every FG at or above 30 yards is priced at its band "
        "midpoint under the per-yard rule (e.g. a 30-39 make scores as "
        "if it were a 35-yarder = 3.5 pts) rather than the real distance. "
        "Do not treat this kicker total as league-verified; label it "
        "approximate wherever it's shown."
    )
    result.unscored.append({"rule": "Field goal distance bands", "mfl_event": "FG", "reason": fg_note, "candidates": []})

    for field_name, midpoint, flat_pts in band_midpoints_and_points:
        count = stats.get(field_name)
        if not count:
            continue
        count = float(count)
        pts_each = flat_pts if flat_pts is not None else midpoint * 0.1
        pts = count * pts_each
        result.breakdown[f"FG ({field_name}, approx @ {midpoint}yd)"] = pts
        result.total += pts
        result.low_confidence_used.append({
            "rule": "Field goal (banded approximation)",
            "sleeper_field": field_name,
            "confidence": "low",
            "points_contributed": pts,
        })

    result.total = round(result.total, 3)
    return result
