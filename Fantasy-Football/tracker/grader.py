"""Accuracy tracker grader -- Section 3 & 4 of ACCURACY-TRACKER-BUILD.md.

Run: python grader.py <season> <week>

Scores come from ESPN (never nflverse -- nflverse lags days, ESPN has
final scores immediately, per Section 3). Closing lines come from
nflverse's `schedules` release via the nfl-data skill -- confirmed
necessary because ESPN's own odds field disappears once a game goes
final (see espn_games.py's module docstring for how this was verified).

INTEGRITY: this module writes ONLY the post-game columns
(graded_at, away_score, home_score, closing_line, result_su, result_ats).
Before writing anything back, every pre-game column of every row is
diffed against what was just read from disk; if a single character of
any pre-game field would change, the whole run aborts and writes
nothing. That is the closest a flat CSV rewrite can get to Section 2's
'grader reads, computes, and writes graded rows to a separate pass
rather than rewriting history in place' -- a true separate-file design
was considered and rejected because Section 2's own column list has
the post-game fields living in the SAME row as the pre-game ones; this
keeps that shape while making the append-only guarantee load-bearing
in code, not just in intent.

Refuses to grade any row logged after its own game's kickoff, per
Section 2, and says so loudly rather than silently skipping it.
"""
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).parent))
import espn_games

TRACKER_DIR = Path(__file__).parent
PREDICTIONS_CSV = TRACKER_DIR / "predictions.csv"
NFLVERSE_SCHEDULES = Path(r"D:\WKP\data\nfl\schedules\games.parquet")

# Real, fully-enumerated mismatch between ESPN's team abbreviations
# (used everywhere else in this codebase) and nflverse's (used only in
# schedules.parquet for the closing line). Verified 2026-09-13 by
# diffing all 32 codes from a live pull of both sources -- these are
# the ONLY two that differ; every other code matches exactly.
ESPN_TO_NFLVERSE_ABBR = {"LAR": "LA", "WSH": "WAS"}


def _nflverse_abbr(espn_abbr: str) -> str:
    return ESPN_TO_NFLVERSE_ABBR.get(espn_abbr, espn_abbr)

PRE_GAME_COLUMNS = [
    "logged_at", "season", "week", "game_id", "away_team", "home_team",
    "source", "pick_su", "pick_ats", "line_used", "line_source", "confidence", "on_card",
]
POST_GAME_COLUMNS = ["graded_at", "away_score", "home_score", "closing_line", "result_su", "result_ats"]


def _read_all_rows() -> list[dict]:
    if not PREDICTIONS_CSV.exists():
        return []
    with open(PREDICTIONS_CSV, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _write_all_rows(rows: list[dict], columns: list[str]):
    with open(PREDICTIONS_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        writer.writerows(rows)


def _closing_line_for(season: int, week: int, away_team: str, home_team: str) -> float | None:
    """REAL BUG CAUGHT HERE 2026-09-13: schedules.parquet holds every
    season nflverse has ever published (7500+ rows) in one file, and
    team abbreviations repeat every year. An early version of this
    function matched on team codes alone and silently returned a 2008
    meeting of these same two teams instead of the 2026 one -- exactly
    the kind of silent corruption this build was warned about. season
    and week are now mandatory filters, not optional context."""
    if not NFLVERSE_SCHEDULES.exists():
        return None
    df = pd.read_parquet(NFLVERSE_SCHEDULES)
    nv_away, nv_home = _nflverse_abbr(away_team), _nflverse_abbr(home_team)
    match = df[(df["season"] == season) & (df["week"] == week) &
               (df["away_team"] == nv_away) & (df["home_team"] == nv_home)]
    if match.empty or pd.isna(match.iloc[0]["spread_line"]):
        return None
    if len(match) > 1:
        raise RuntimeError(
            f"Ambiguous closing-line match: {len(match)} rows for season {season} week {week} "
            f"{away_team}@{home_team} -- refusing to guess which one is real."
        )
    return float(match.iloc[0]["spread_line"])


def grade_week(season: int, week: int) -> dict:
    rows = _read_all_rows()
    original_pre_game = {i: {c: r.get(c, "") for c in PRE_GAME_COLUMNS} for i, r in enumerate(rows)}

    scoreboard = espn_games.week_scoreboard(season, week)
    games = espn_games.normalize_games(scoreboard)
    games_by_id = {g["game_id"]: g for g in games}

    now = datetime.now(timezone.utc)
    graded, refused, skipped_incomplete = 0, [], 0

    for i, row in enumerate(rows):
        if str(row["season"]) != str(season) or str(row["week"]) != str(week):
            continue
        if row.get("result_su") or row.get("result_ats"):
            continue  # already graded -- never re-touch a graded row

        game = games_by_id.get(row["game_id"])
        if game is None:
            refused.append(f"REFUSED row {i}: game_id {row['game_id']} not found on this week's ESPN scoreboard")
            continue

        logged_at = datetime.fromisoformat(row["logged_at"])
        kickoff = datetime.fromisoformat(game["kickoff"].replace("Z", "+00:00")) if game["kickoff"] else None
        if kickoff and logged_at >= kickoff:
            refused.append(
                f"REFUSED row {i} ({row['away_team']}@{row['home_team']}, {row['source']}): "
                f"logged_at {row['logged_at']} is at or after kickoff {game['kickoff']} -- integrity violation, not graded"
            )
            continue

        if not game["completed"]:
            skipped_incomplete += 1
            continue

        away_score, home_score = float(game["away_score"]), float(game["home_score"])
        margin = home_score - away_score  # nflverse convention: positive = home won by that much

        # Straight up. Ties count as incorrect (Section 3), unless Zac
        # says otherwise -- no override mechanism built since none was
        # asked for.
        result_su = ""
        if row.get("pick_su"):
            if margin == 0:
                result_su = "incorrect"
            else:
                winner = game["home_team"] if margin > 0 else game["away_team"]
                result_su = "correct" if row["pick_su"] == winner else "incorrect"

        # Against the spread. line_used is signed in nflverse's
        # convention (positive = home favored) -- see logger.py's
        # module docstring for why that convention was chosen.
        #
        # RULE CORRECTION 2026-09-13 (Zac): this league has NO push.
        # When the final margin lands exactly on the spread, the
        # UNDERDOG wins the pick -- not a refund. This also matches
        # Fantasy-Football/CLAUDE.md's own pick'em section, which
        # already documented "Underdog wins ties" -- a rule this
        # grader had not been honoring until now (real process gap:
        # that line was sitting in the venture's own CLAUDE.md the
        # whole time this was built).
        #
        # An exact tie is NOT symmetric under "margin > line" the way
        # push-exclusion made it look -- which side wins a tie depends
        # on who's the favorite, not just home/away. Verified by
        # explicit case analysis before trusting this (both directions,
        # not just the case that happened to be on the real Week 1
        # card): line=+3 (home favored), margin=+3 tie -> home is
        # favorite -> home LOSES the tie, away/dog wins. line=-3 (away
        # favored, home is the dog), margin=-3 tie -> home is the dog
        # -> home WINS the tie. So home_wins_tie = NOT favorite_is_home,
        # not a constant.
        #
        # line == 0 (a true pick'em game, no favorite/underdog at all)
        # has no underdog for an exact tie to fall to -- flagged rather
        # than guessed at either direction.
        result_ats = ""
        if row.get("pick_ats") and row.get("line_used") not in ("", None):
            line = float(row["line_used"])
            picked_home = row["pick_ats"] == game["home_team"]

            if margin == line:
                if line == 0:
                    result_ats = "unresolved_pickem_tie"
                else:
                    favorite_is_home = line > 0
                    home_wins_tie = not favorite_is_home
                    covered = home_wins_tie if picked_home else not home_wins_tie
                    result_ats = "correct" if covered else "incorrect"
            else:
                home_covered = margin > line
                covered = home_covered if picked_home else not home_covered
                result_ats = "correct" if covered else "incorrect"

        closing_line = _closing_line_for(season, week, row["away_team"], row["home_team"])

        row["graded_at"] = now.isoformat()
        row["away_score"] = away_score
        row["home_score"] = home_score
        row["closing_line"] = closing_line if closing_line is not None else ""
        row["result_su"] = result_su
        row["result_ats"] = result_ats
        graded += 1

    # Integrity check: no pre-game field may have changed for ANY row,
    # not just the ones we touched. If this trips, abort and write
    # nothing -- a corrupted history is worse than a late report.
    for i, row in enumerate(rows):
        for col in PRE_GAME_COLUMNS:
            if row.get(col, "") != original_pre_game[i][col]:
                raise RuntimeError(
                    f"INTEGRITY ABORT: row {i} column '{col}' changed from "
                    f"{original_pre_game[i][col]!r} to {row.get(col, '')!r}. "
                    f"Nothing was written. This must never happen -- investigate before re-running."
                )

    if rows:
        _write_all_rows(rows, PRE_GAME_COLUMNS + POST_GAME_COLUMNS)

    for r in refused:
        print(r)

    return {"graded": graded, "refused": len(refused), "skipped_incomplete": skipped_incomplete}


def _pct(correct: int, total: int) -> str:
    return f"{100 * correct / total:.1f}%" if total else "n/a (0 graded)"


# ATS break-even, recomputed 2026-09-13 for this league's no-push rule
# (Zac: "underdog wins ties, no refunds"). The standard 52.4% figure
# assumes -110/-110 odds with pushes refunded and EXCLUDED from the
# win-rate denominator; that ratio is a pure function of the vig and
# does not depend on push frequency (verified algebraically: q cancels
# out of the break-even equation when pushes are refunded/excluded).
#
# In THIS format, a game that would have pushed instead ALWAYS resolves
# underdog-wins/favorite-loses -- never refunded, never excluded. Modeled
# as: a bettor is on the favorite vs. underdog roughly 50/50 specifically
# among the games that land exactly on the number (a neutral assumption;
# there's no reason to think anyone can predict which games will push).
# Each of those games then carries a -5-unit expected value (half win
# +100, half lose -110) instead of the 0 EV it had when refunded, which
# nudges the required win rate on the OTHER (non-tie) games up slightly
# to compensate:
#   p = [110 + 5q/(1-q)] / 210
# q (per-game push probability) sourced from Action Network's 2014-2023
# NFL ATS data: favorite covers 47%, favorite-wins-no-cover 16%,
# underdog wins 34%, push ~3% (100-47-16-34). At q=0.03: p = 52.455%,
# a ~0.07-point nudge over the standard 52.4% -- small because pushes
# are themselves rare, not because the correction is wrong.
ATS_BREAKEVEN_PCT = 52.5


def _fmt_pct(v: float) -> str:
    return f"{v:g}%"


def favorite_baseline(season: int, week: int) -> tuple[int, int]:
    """'Always pick the favorite' computed from the SAME graded games
    this week, not a historical constant (Section 4's explicit rule)."""
    rows = [r for r in _read_all_rows()
            if str(r["season"]) == str(season) and str(r["week"]) == str(week) and r.get("result_su")]
    seen_games = {}
    for r in rows:
        seen_games[r["game_id"]] = r  # any source's row carries the same away/home/scores
    correct, total = 0, 0
    for r in seen_games.values():
        if r.get("line_used") in ("", None) or r.get("away_score") in ("", None):
            continue
        line = float(r["line_used"])
        if line == 0:
            continue  # pick 'em game, no favorite
        favorite_is_home = line > 0
        margin = float(r["home_score"]) - float(r["away_score"])
        favorite_won = (margin > 0) == favorite_is_home
        total += 1
        correct += int(favorite_won)
    return correct, total


def summarize(season: int, week: int):
    rows = [r for r in _read_all_rows() if str(r["season"]) == str(season) and str(r["week"]) == str(week)]
    print(f"\n=== Accuracy summary: season {season} week {week} ===\n")

    for source in ("model", "assisted_card", "control_card"):
        srows = [r for r in rows if r["source"] == source and r.get("result_ats")]
        su_rows = [r for r in rows if r["source"] == source and r.get("result_su")]

        su_correct = sum(1 for r in su_rows if r["result_su"] == "correct")
        su_total = sum(1 for r in su_rows if r["result_su"] in ("correct", "incorrect"))

        ats_correct = sum(1 for r in srows if r["result_ats"] == "correct")
        ats_unresolved_tie = sum(1 for r in srows if r["result_ats"] == "unresolved_pickem_tie")
        ats_total = sum(1 for r in srows if r["result_ats"] in ("correct", "incorrect"))  # no push in this league

        print(f"-- {source} --")
        print(f"  Straight up: {su_correct}/{su_total} = {_pct(su_correct, su_total)}")
        tie_note = f", {ats_unresolved_tie} unresolved pick'em tie(s) excluded" if ats_unresolved_tie else ""
        print(f"  Against the spread: {ats_correct}/{ats_total} = {_pct(ats_correct, ats_total)} "
              f"(baseline {_fmt_pct(ATS_BREAKEVEN_PCT)} -- this league has no push, ties go to the "
              f"underdog{tie_note})")

    fav_correct, fav_total = favorite_baseline(season, week)
    print(f"\n  Favorite-picks-every-game baseline (this week's games): "
          f"{fav_correct}/{fav_total} = {_pct(fav_correct, fav_total)}")

    total_graded = sum(1 for r in rows if r.get("result_su") or r.get("result_ats"))
    print(f"\nGames graded this run: {total_graded}")
    if total_graded < 150:
        print(f"Sample size note: {total_graded} graded games is well under the ~150 threshold where a "
              f"percentage means anything. Treat every number above as a direction, not a verdict.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: python grader.py <season> <week>")
    season, week = int(sys.argv[1]), int(sys.argv[2])
    result = grade_week(season, week)
    print(f"Graded {result['graded']} rows, refused {result['refused']}, "
          f"{result['skipped_incomplete']} not yet final.")
    summarize(season, week)
