"""Shared ESPN scoreboard access for the accuracy tracker. Scores come
from ESPN, never nflverse -- confirmed real reason (ACCURACY-TRACKER-
BUILD.md Section 3): nflverse lags days behind, ESPN has final scores
immediately.

Real gap found and worked around while building this (2026-09-13):
ESPN's own `odds` field on a scoreboard event DISAPPEARS once the game
goes final -- confirmed by direct comparison, same week, same call:
pre-game events carry a full odds block (spread, provider, etc.),
post-game (status.type.state == 'post') events carry no odds key at
all. So ESPN cannot be the closing-line source once you actually need
it (Tuesday morning, after the games are over). Closing lines come
from nflverse's `schedules` release instead (via the nfl-data skill) --
that file is NOT subject to the same lag as `pbp`/`stats_*` since it's
lightly-processed schedule/line data, confirmed by checking it same-day
against two already-final week 1 games: both had real final scores and
a real spread_line within hours of kickoff.
"""
import requests

NFL_SCOREBOARD = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"


def week_scoreboard(season: int, week: int, seasontype: int = 2) -> dict:
    """No custom User-Agent -- see Fantasy-Football/dashboard/espn_client.py
    for why (this project's own descriptive UA gets a 403 from ESPN)."""
    resp = requests.get(NFL_SCOREBOARD, params={"seasontype": seasontype, "week": week, "dates": season}, timeout=20)
    resp.raise_for_status()
    return resp.json()


def normalize_games(scoreboard: dict) -> list[dict]:
    """Returns one dict per game:
    {game_id, away_team, home_team, away_score, home_score, kickoff,
     state ('pre'|'in'|'post'), completed, spread_home}
    spread_home follows nflverse's own documented sign convention
    (positive = home favored) so it's directly comparable to a
    nflverse closing_line value -- NOT ESPN's team-relative convention
    (which prints the favored team's own name with a negative number,
    e.g. "CIN -3.5"). Converted here, once, so nothing downstream has
    to juggle two different sign conventions.
    """
    games = []
    for event in scoreboard.get("events", []):
        comp = event["competitions"][0]
        away = next(c for c in comp["competitors"] if c["homeAway"] == "away")
        home = next(c for c in comp["competitors"] if c["homeAway"] == "home")

        spread_home = None
        odds = comp.get("odds")
        if odds:
            raw_spread = odds[0].get("spread")
            if raw_spread is not None:
                # ESPN's `spread` field is signed from the HOME team's own
                # perspective already in this endpoint (confirmed 2026-09-13:
                # CIN home, "CIN -3.5" details string, spread=-3.5 -- so
                # ESPN's raw value is negative when home is favored).
                # nflverse's convention is the opposite sign (positive =
                # home favored). Flip here so spread_home always means
                # "positive = home favored" everywhere in this codebase.
                spread_home = -raw_spread

        games.append({
            "game_id": event["id"],
            "away_team": away["team"]["abbreviation"],
            "home_team": home["team"]["abbreviation"],
            "away_score": away.get("score"),
            "home_score": home.get("score"),
            "kickoff": event.get("date"),
            "state": comp["status"]["type"]["state"],
            "completed": comp["status"]["type"]["completed"],
            "spread_home": spread_home,
        })
    return games


def find_game(games: list[dict], team_abbr: str) -> dict | None:
    for g in games:
        if team_abbr in (g["away_team"], g["home_team"]):
            return g
    return None
