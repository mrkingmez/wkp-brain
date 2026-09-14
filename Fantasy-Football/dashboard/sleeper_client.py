"""Sleeper projections pull for the dashboard's dual-projection panel.
No key, no auth -- same source verified in FF-DATA-PATCH-sleeper-espn.md."""
import requests

POSITIONS = ["QB", "RB", "WR", "TE", "K", "DEF", "DL", "LB", "DB"]


def week_projections(season: int, week: int) -> dict:
    """Returns {sleeper_player_id: stats_dict}."""
    params = [("season_type", "regular")] + [("position[]", p) for p in POSITIONS]
    resp = requests.get(f"https://api.sleeper.app/projections/nfl/{season}/{week}", params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return {p["player_id"]: p["stats"] for p in data if p.get("player_id")}
