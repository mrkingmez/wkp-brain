"""Accuracy tracker logger -- Section 1 & 2 of ACCURACY-TRACKER-BUILD.md.

Writes prediction rows for the three Phase 1 sources (model,
assisted_card, control_card). Lineups (source D) are explicitly out of
scope until Phase 4.

THE INTEGRITY RULE (Section 2): predictions.csv is append-only in
practice. This module only ever appends new rows with blank post-game
columns. It never rewrites an existing row -- that's grader.py's job,
and even there only the post-game columns move.

SIGN CONVENTION (decided here, since the build doc doesn't pin one):
`line_used` and `closing_line` are both stored using nflverse's
documented convention -- positive = home team favored by that many
points, negative = away team favored. Confirmed against nflverse's own
schedules data dictionary and cross-checked against ESPN's odds for
all 14 pending week 1 games (exact sign+magnitude match on every one)
before this was trusted. Every prediction is normalized to this
convention at write time, in this one file, so nothing downstream has
to reason about favorite/underdog framing at all -- grading is always
just "home_score - away_score vs. the signed line."

SECTION 6 DISCIPLINE: the control card (and, later, the gut lineup) is
accepted as loose plain text -- a list of team names, nothing else.
Zac is never asked to type a spread, a line, or a game id. Those come
from the real card / ESPN schedule automatically.
"""
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "dashboard"))
import team_match  # noqa: E402 -- reused from the dashboard build, already tested
import pickem_card  # noqa: E402
import docx_picks  # noqa: E402
import config as dashboard_config  # noqa: E402 -- real card paths live here (2026-09-13 spec)

import espn_games

TRACKER_DIR = Path(__file__).parent
PREDICTIONS_CSV = TRACKER_DIR / "predictions.csv"
CARDS_DIR = TRACKER_DIR.parent / "cards"  # BLANK templates only -- see dashboard_config for real card paths

COLUMNS = [
    "logged_at", "season", "week", "game_id", "away_team", "home_team",
    "source", "pick_su", "pick_ats", "line_used", "line_source", "confidence", "on_card",
    "graded_at", "away_score", "home_score", "closing_line", "result_su", "result_ats",
]


def _ensure_csv():
    if not PREDICTIONS_CSV.exists():
        with open(PREDICTIONS_CSV, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(COLUMNS)


def _append_rows(rows: list[dict]):
    """The only function in this module allowed to touch the file.
    Appends only -- opens in 'a' mode, never 'w' or 'r+'."""
    _ensure_csv()
    with open(PREDICTIONS_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        for row in rows:
            full = {c: row.get(c, "") for c in COLUMNS}
            writer.writerow(full)


def _refuse_if_past_kickoff(game: dict, now: datetime) -> str | None:
    """Returns an error string if this game has already kicked off,
    else None. Section 2: 'Refuse to grade any row whose logged_at is
    after kickoff and log that refusal loudly' -- applied here at
    LOGGING time too, since a pick written after kickoff is exactly as
    worthless as one graded from a late-written row, and catching it
    at write time is strictly better than catching it later."""
    kickoff_str = game.get("kickoff")
    if not kickoff_str:
        return None
    kickoff = datetime.fromisoformat(kickoff_str.replace("Z", "+00:00"))
    if now >= kickoff:
        return f"REFUSED: {game['away_team']} @ {game['home_team']} already kicked off ({kickoff_str})"
    return None


def log_model_picks(season: int, week: int, picks: list[dict], on_card_games: set[str] | None = None) -> dict:
    """picks: [{team, side_of_game ('away'|'home' not required -- team
    name is enough), pick_su (team name or None), pick_ats (team name),
    line_used (signed, home-favored-positive), confidence (0-1)}, ...]

    Section 1A: every pro game, whether or not it's on the card. The
    actual pick-generation model is out of scope for this build --
    this function only logs whatever picks are handed to it, against
    the real ESPN schedule, with the same integrity checks as every
    other source.

    on_card_games: set of team abbreviations from this week's real
    pick'em card, used to set on_card. Optional -- if not given,
    on_card is left blank rather than guessed.
    """
    now = datetime.now(timezone.utc)
    scoreboard = espn_games.week_scoreboard(season, week)
    games = espn_games.normalize_games(scoreboard)

    rows, refusals = [], []
    for pick in picks:
        game = espn_games.find_game(games, pick["team"])
        if game is None:
            refusals.append(f"REFUSED: no ESPN game found for team '{pick['team']}' in {season} week {week}")
            continue
        err = _refuse_if_past_kickoff(game, now)
        if err:
            refusals.append(err)
            continue

        on_card = None
        if on_card_games is not None:
            on_card = game["away_team"] in on_card_games or game["home_team"] in on_card_games

        rows.append({
            "logged_at": now.isoformat(),
            "season": season, "week": week, "game_id": game["game_id"],
            "away_team": game["away_team"], "home_team": game["home_team"],
            "source": "model",
            "pick_su": pick.get("pick_su", ""),
            "pick_ats": pick.get("pick_ats", ""),
            "line_used": pick.get("line_used", ""),
            "line_source": pick.get("line_source", "model_only"),
            "confidence": pick.get("confidence", ""),
            "on_card": on_card if on_card is not None else "",
        })

    if refusals:
        for r in refusals:
            print(r)

    # De-dupe against already-logged model picks for this game+week so a
    # re-run doesn't double-log (append-only means no overwrite, so this
    # check has to happen before appending).
    existing = _load_existing_keys(season, week, "model")
    rows = [r for r in rows if (r["game_id"], r["source"]) not in existing]

    _append_rows(rows)
    return {"logged": len(rows), "refused": refusals}


def _load_existing_keys(season: int, week: int, source: str) -> set[tuple[str, str]]:
    if not PREDICTIONS_CSV.exists():
        return set()
    keys = set()
    with open(PREDICTIONS_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if str(row["season"]) == str(season) and str(row["week"]) == str(week) and row["source"] == source:
                keys.add((row["game_id"], row["source"]))
    return keys


def _parse_loose_team_list(text: str) -> list[str]:
    """Section 6: 'Accept the control card as plain text pasted into a
    file. Parse loosely. Do not make Zac format anything.' One team
    name per non-empty line. Leading/trailing whitespace and blank
    lines are ignored; nothing else is required."""
    return [line.strip() for line in text.splitlines() if line.strip()]


def log_card_picks_from_text(season: int, week: int, source: str, picks_text: str) -> dict:
    """FALLBACK path -- kept for a week where a real card file isn't
    ready yet, or for manual override. The normal path for real weeks
    is now log_hybrid_card() / log_control_card(), which read the real
    fill-color-marked .xls files directly (decision FF-2026-09-12-01
    resolved 2026-09-13: picks are marked by cell fill color, confirmed
    against the real submitted Week 1 card -- 20/20 parsed cleanly, zero
    ambiguous rows).

    source: 'assisted_card' or 'control_card'. picks_text: plain text,
    one team name per line, in the same order Zac picked them -- matched
    against this week's BLANK template card in cards\\ (favored/spread/
    underdog only; this path never reads real pick marks from a file).
    Lines don't need to match the card's exact spelling; team_match.py's
    substring matching (already proven against the real card) resolves
    it to a real ESPN team and the card's real spread.

    pick_su is left blank -- a plain team-name list is an ATS pick list
    by construction (this is a spread pool), and inventing a straight-up
    winner from that would be exactly the silent-corruption risk this
    build is trying to avoid. If Zac wants to log SU picks too, prefix a
    line with 'SU:' and it's captured as pick_su on the matching game
    instead of being forced to equal pick_ats.
    """
    assert source in ("assisted_card", "control_card")

    import pickem_card
    card_path = pickem_card.find_current_week_card(CARDS_DIR, _guess_codename(week), week)
    if card_path is None:
        return {"logged": 0, "refused": [f"REFUSED: no pick'em card found for week {week}"]}
    card = pickem_card.read_card(card_path)

    now = datetime.now(timezone.utc)
    scoreboard = espn_games.week_scoreboard(season, week)
    espn_games_list = espn_games.normalize_games(scoreboard)

    teams_named = _parse_loose_team_list(picks_text)
    su_overrides = {}
    ats_picks = []
    for line in teams_named:
        if line.upper().startswith("SU:"):
            su_overrides[line[3:].strip()] = True
        else:
            ats_picks.append(line)

    nfl_teams_cache_path = Path(__file__).parent.parent / "dashboard" / "espn-nfl-teams-cache.json"
    import json
    nfl_teams = json.loads(nfl_teams_cache_path.read_text(encoding="utf-8")) if nfl_teams_cache_path.exists() else []

    rows, refusals = [], []
    for team_text in ats_picks:
        matched_team = team_match.match_nfl_team(team_text, nfl_teams)
        if matched_team is None:
            refusals.append(f"REFUSED: could not match '{team_text}' to an NFL team -- not guessing, skipped")
            continue
        abbr = matched_team["abbreviation"]
        game = espn_games.find_game(espn_games_list, abbr)
        if game is None:
            refusals.append(f"REFUSED: '{team_text}' matched {abbr} but no ESPN game found this week")
            continue
        err = _refuse_if_past_kickoff(game, now)
        if err:
            refusals.append(err)
            continue

        card_game = next(
            (g for g in card["games"] if team_text.strip().upper() in (g["favored"].upper(), g["underdog"].upper())
             or abbr == team_text.strip().upper()),
            None,
        )
        line_used = ""
        if card_game and card_game["spread"] is not None:
            fav_is_home = card_game["home_is_favored"]
            fav_abbr = None
            fav_match = team_match.match_nfl_team(card_game["favored"], nfl_teams)
            if fav_match:
                fav_abbr = fav_match["abbreviation"]
            if fav_abbr == game["home_team"]:
                line_used = card_game["spread"]        # home favored -> positive, matches our convention directly
            elif fav_abbr == game["away_team"]:
                line_used = -card_game["spread"]        # away favored -> negative
            else:
                refusals.append(f"REFUSED to set line_used for {team_text}: favored-team match ambiguous")

        su_pick = ""
        for su_name, _ in su_overrides.items():
            if team_match.match_nfl_team(su_name, nfl_teams) and \
               team_match.match_nfl_team(su_name, nfl_teams)["abbreviation"] == abbr:
                su_pick = abbr

        rows.append({
            "logged_at": now.isoformat(),
            "season": season, "week": week, "game_id": game["game_id"],
            "away_team": game["away_team"], "home_team": game["home_team"],
            "source": source,
            "pick_su": su_pick,
            "pick_ats": abbr,
            "line_used": line_used,
            "line_source": "monday_card",
            "confidence": "",
            "on_card": True,
        })

    if refusals:
        for r in refusals:
            print(r)

    existing = _load_existing_keys(season, week, source)
    rows = [r for r in rows if (r["game_id"], r["source"]) not in existing]

    _append_rows(rows)
    return {"logged": len(rows), "refused": refusals}


def _guess_codename(week: int) -> str:
    matches = list(CARDS_DIR.glob(f"*Week{week}*Entry.xls"))
    if not matches:
        return "CODENAME"
    return matches[0].name.split("_Week")[0]


def _game_line_used(card_game: dict) -> float | str:
    """nflverse convention (positive = home favored) from a card game's
    favored/spread/home_is_favored fields. Same value regardless of
    which side was picked -- line_used describes the GAME, not the pick;
    the grader compares pick_ats against home_team to decide who needed
    to cover which way."""
    if card_game.get("spread") is None:
        return ""
    return card_game["spread"] if card_game["home_is_favored"] else -card_game["spread"]


def _all_card_rows(card: dict) -> list[dict]:
    rows = list(card["games"])
    if card.get("tiebreaker"):
        rows.append(card["tiebreaker"])
    return rows


def _log_xls_card(season: int, week: int, source: str, path: Path, nfl_teams: list) -> dict:
    """Shared real-file logging path for both the hybrid (assisted_card)
    and control card -- both are the same .xls shape, both marked by
    fill color, both read via pickem_card.read_card().

    Real gap caught 2026-09-13 (same class of bug as log_model_from_docx
    originally had): 4 of the real card's 20 picks are NCAA games
    (Oklahoma, Army, Boise State, Ohio State) -- NFL-only team matching
    silently refused every one of them as 'not an NFL team'. Both
    leagues are tried now."""
    import espn_client  # dashboard module, already on sys.path

    card = pickem_card.read_card(path)
    now = datetime.now(timezone.utc)
    scoreboard = espn_games.week_scoreboard(season, week)
    espn_games_list = espn_games.normalize_games(scoreboard)
    cfb_events = espn_client.cfb_scoreboard().get("events", [])

    rows, refusals = [], []
    for card_game in _all_card_rows(card):
        if card_game["pick"] not in ("favored", "underdog"):
            refusals.append(
                f"SKIPPED {card_game['favored']} vs {card_game['underdog']}: "
                f"pick state is '{card_game['pick']}' (zero or multiple filled cells), not logging a guess."
            )
            continue

        pick_team_text = card_game["pick_team"]
        nfl_match = team_match.match_nfl_team(pick_team_text, nfl_teams)

        if nfl_match:
            abbr = nfl_match["abbreviation"]
            game = espn_games.find_game(espn_games_list, abbr)
            if game is None:
                refusals.append(f"REFUSED: '{pick_team_text}' matched {abbr} but no ESPN game found this week")
                continue
            game_id, away_team, home_team, kickoff = game["game_id"], game["away_team"], game["home_team"], game["kickoff"]
        else:
            cfb_match = team_match.match_cfb_team(pick_team_text, cfb_events)
            if cfb_match is None:
                refusals.append(f"REFUSED: could not match '{pick_team_text}' to an NFL or CFB team -- not guessing, skipped")
                continue
            event, team = cfb_match
            comp = event["competitions"][0]
            away_c = next(c for c in comp["competitors"] if c["homeAway"] == "away")
            home_c = next(c for c in comp["competitors"] if c["homeAway"] == "home")
            abbr = team["abbreviation"]
            game_id = event["id"]
            away_team = away_c["team"]["abbreviation"]
            home_team = home_c["team"]["abbreviation"]
            kickoff = event.get("date")

        if kickoff:
            kickoff_dt = datetime.fromisoformat(kickoff.replace("Z", "+00:00"))
            if now >= kickoff_dt:
                refusals.append(f"REFUSED: {away_team}@{home_team} already kicked off ({kickoff})")
                continue

        rows.append({
            "logged_at": now.isoformat(),
            "season": season, "week": week, "game_id": game_id,
            "away_team": away_team, "home_team": home_team,
            "source": source,
            "pick_su": "",
            "pick_ats": abbr,
            "line_used": _game_line_used(card_game),
            "line_source": "monday_card",
            "confidence": "",
            "on_card": True,
        })

    if refusals:
        for r in refusals:
            print(r)

    existing = _load_existing_keys(season, week, source)
    rows = [r for r in rows if (r["game_id"], r["source"]) not in existing]
    _append_rows(rows)

    return {
        "status": "logged",
        "logged": len(rows),
        "refused": refusals,
        "picks_parsed": card["picks_parsed"],
        "rows_total": card["rows_total"],
        "zero_filled_rows": card["zero_filled_rows"],
        "multi_filled_rows": card["multi_filled_rows"],
    }


def _load_nfl_teams() -> list:
    import json
    cache = dashboard_config.NFL_TEAMS_CACHE
    if not cache.exists():
        raise SystemExit(f"{cache} missing -- run the dashboard poller at least once first (it fetches this).")
    return json.loads(cache.read_text(encoding="utf-8"))


def log_hybrid_card(season: int, week: int) -> dict:
    """The real card submitted to the league: 'Sanders_Week{N} Entry.xls'
    in D:\\Documents\\Pickups 2026\\. This is the 'assisted_card' source.
    Picks are read from real fill-color marks -- see pickem_card.py."""
    path = dashboard_config.hybrid_card_path(week)
    if not path.exists():
        return {"status": "absent", "logged": 0, "message": f"No hybrid card found at {path}"}
    return _log_xls_card(season, week, "assisted_card", path, _load_nfl_teams())


def log_control_card(season: int, week: int) -> dict:
    """Zac's picks, no model input: 'Sanders_Week{N}P Entry.xls'. Starts
    Week 2 per Zac -- Week 1 genuinely has none. A missing file is
    reported as status='absent' (no attempt was made), which is a
    different fact from a card that exists with zero picks parsed --
    callers must not conflate the two."""
    path = dashboard_config.control_card_path(week)
    if not path.exists():
        return {"status": "absent", "logged": 0, "message": f"No control card for week {week} (expected {path})"}
    return _log_xls_card(season, week, "control_card", path, _load_nfl_teams())


def log_model_from_docx(season: int, week: int) -> dict:
    """The pure-model source: 'Pickups 2026 - Week {N}.docx'. Parses
    only the ATS picks section (docx_picks.py) -- the straight-up-
    winners tier list and IRFL lineup writeup in the same doc are not
    parsed here. Cross-references the hybrid card (if present) for the
    on_card flag.

    Real gap caught testing this 2026-09-13: the doc's 20 ATS picks are
    NOT all NFL -- 4 of them (Oklahoma/Michigan, Army/South Florida,
    Boise State/Memphis, Texas/Ohio State) are college games, and the
    first version of this function only tried NFL team matching,
    silently crashing on the first CFB pick. Both leagues are resolved
    here now, exactly like every other dual-league path in this
    codebase (dashboard's pick'em/full-scoreboard panels)."""
    path = dashboard_config.model_picks_docx_path(week)
    if not path.exists():
        return {"status": "absent", "logged": 0, "message": f"No model picks doc found at {path}"}

    import espn_client  # dashboard module, already on sys.path

    nfl_teams = _load_nfl_teams()
    doc_picks = docx_picks.parse_model_ats_picks(path)
    nfl_scoreboard = espn_games.week_scoreboard(season, week)
    nfl_games = espn_games.normalize_games(nfl_scoreboard)
    cfb_events = espn_client.cfb_scoreboard().get("events", [])

    on_card_games = None
    hybrid_path = dashboard_config.hybrid_card_path(week)
    if hybrid_path.exists():
        hybrid_card = pickem_card.read_card(hybrid_path)
        on_card_games = set()
        for g in _all_card_rows(hybrid_card):
            for name in (g["favored"], g["underdog"]):
                m = team_match.match_nfl_team(name, nfl_teams)
                if m:
                    on_card_games.add(m["abbreviation"])

    now = datetime.now(timezone.utc)
    rows, refusals, unmatched = [], [], []

    for p in doc_picks:
        nfl_match = team_match.match_nfl_team(p["pick_team"], nfl_teams)
        nfl_home = team_match.match_nfl_team(p["home"], nfl_teams)

        if nfl_match and nfl_home:
            abbr, home_abbr = nfl_match["abbreviation"], nfl_home["abbreviation"]
            game = espn_games.find_game(nfl_games, abbr)
            if game is None:
                refusals.append(f"REFUSED: {abbr} matched NFL but no ESPN game found this week")
                continue
            game_id, away_team, home_team, kickoff = game["game_id"], game["away_team"], game["home_team"], game["kickoff"]
        else:
            cfb_match = team_match.match_cfb_team(p["pick_team"], cfb_events)
            if cfb_match is None:
                unmatched.append(p["raw_text"])
                continue
            event, team = cfb_match
            comp = event["competitions"][0]
            away_c = next(c for c in comp["competitors"] if c["homeAway"] == "away")
            home_c = next(c for c in comp["competitors"] if c["homeAway"] == "home")
            abbr = team["abbreviation"]
            home_abbr = home_c["team"]["abbreviation"]
            game_id = event["id"]
            away_team = away_c["team"]["abbreviation"]
            home_team = home_c["team"]["abbreviation"]
            kickoff = event.get("date")

        if kickoff:
            kickoff_dt = datetime.fromisoformat(kickoff.replace("Z", "+00:00"))
            if now >= kickoff_dt:
                refusals.append(f"REFUSED: {away_team}@{home_team} already kicked off ({kickoff})")
                continue

        pick_is_home = abbr == home_abbr
        # pick_line is signed from the PICKED team's own perspective
        # (standard betting convention: negative = favored). Flip to
        # nflverse's home-favored-positive convention -- see
        # docx_picks.py's docstring for the worked examples.
        line_used = -p["pick_line"] if pick_is_home else p["pick_line"]

        on_card = None
        if on_card_games is not None:
            on_card = abbr in on_card_games or home_abbr in on_card_games

        rows.append({
            "logged_at": now.isoformat(),
            "season": season, "week": week, "game_id": game_id,
            "away_team": away_team, "home_team": home_team,
            "source": "model",
            "pick_su": "",
            "pick_ats": abbr,
            "line_used": line_used,
            "line_source": "model_only",
            "confidence": "",
            "on_card": on_card if on_card is not None else "",
        })

    if refusals:
        for r in refusals:
            print(r)
    if unmatched:
        for u in unmatched:
            print(f"REFUSED: could not match a team (NFL or CFB) in this model pick line -- {u}")

    existing = _load_existing_keys(season, week, "model")
    rows = [r for r in rows if (r["game_id"], r["source"]) not in existing]
    _append_rows(rows)

    return {
        "status": "logged",
        "logged": len(rows),
        "refused": refusals,
        "unmatched": unmatched,
        "docx_picks_found": len(doc_picks),
    }
