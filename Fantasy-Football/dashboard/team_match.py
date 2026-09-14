"""Matches the free-text team names on the pick'em card (e.g. 'LA RAMS',
'New England', 'MICHIGAN') against ESPN scoreboard team objects.

Card convention (confirmed from the actual Week 1 card, and the card's
own legend row): ALL CAPS = home team; away/home is otherwise just a
city or city+nickname string, typed by hand, not a fixed code. NFL
entries use nickname to disambiguate the two LA teams and the two NY
teams (e.g. 'LA RAMS' vs 'LA CHARGERS'); every other NFL entry is just
the city. College entries are whatever short name fits the cell.

This is substring/token matching, not exact-key lookup -- it will not
be perfect on every possible spelling. Log anything it can't resolve
rather than guessing, per the honesty rule.
"""
import re


def _norm(s: str) -> str:
    return re.sub(r"[^A-Z0-9 ]", "", s.upper()).strip()


def match_nfl_team(card_text: str, nfl_teams: list[dict]) -> dict | None:
    """nfl_teams: list of ESPN team dicts (from espn_client.nfl_teams())."""
    token = _norm(card_text)
    if not token:
        return None

    # Pass 1: nickname is a whole word in the card text -- resolves the
    # LA/NY duplicate-city cases (RAMS vs CHARGERS, GIANTS vs JETS).
    words = set(token.split())
    for team in nfl_teams:
        nickname = _norm(team.get("name", ""))
        if nickname and nickname in words:
            return team

    # Pass 2: exact location match, only safe when location is unique
    # (i.e. not one of the two LA/NY teams).
    location_counts: dict[str, int] = {}
    for team in nfl_teams:
        loc = _norm(team.get("location", ""))
        location_counts[loc] = location_counts.get(loc, 0) + 1
    for team in nfl_teams:
        loc = _norm(team.get("location", ""))
        if loc and loc == token and location_counts.get(loc) == 1:
            return team

    # Pass 3: substring either direction (handles state-name franchises
    # like 'TENNESSEE' for the Titans, whose ESPN location is 'Tennessee').
    for team in nfl_teams:
        loc = _norm(team.get("location", ""))
        if loc and (loc in token or token in loc) and location_counts.get(loc) == 1:
            return team

    return None


def match_cfb_team(card_text: str, cfb_events: list[dict]) -> tuple[dict, dict] | None:
    """Returns (event, competitor_team_dict) for the first event whose
    competitor matches card_text, or None. cfb_events = espn_client
    .cfb_scoreboard()['events']."""
    token = _norm(card_text)
    if not token:
        return None
    best = None
    for event in cfb_events:
        comp = event.get("competitions", [{}])[0]
        for competitor in comp.get("competitors", []):
            team = competitor.get("team", {})
            candidates = [
                _norm(team.get("shortDisplayName", "")),
                _norm(team.get("location", "")),
                _norm(team.get("name", "")),
                _norm(team.get("nickname", "")),
            ]
            for cand in candidates:
                if not cand:
                    continue
                if cand == token or cand in token or token in cand:
                    # prefer exact/short match over a loose substring hit
                    if cand == token:
                        return event, team
                    if best is None:
                        best = (event, team)
    return best
