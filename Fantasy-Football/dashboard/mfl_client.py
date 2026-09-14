"""Thin MFL export-API client. Verified 2026-09-12 against the real
league (www44, league 43094):

- liveScoring, playerScores, standings -> league host (www44), need L=
- injuries -> api.myfantasyleague.com, NO L= param (league-hosted call
  errors: "Invalid request. This API request must go to
  api.myfantasyleague.com"; passing L= there redirects back to www44
  in a loop). Works with or without APIKEY; sent anyway for the
  registration-credit MFL mentions.
- playoffChances is NOT a valid TYPE (confirmed via MFL's own error
  message listing every valid TYPE) -- standings is what Section 2's
  "playoffChances or standings" actually resolves to.

No fixed rate limit is published. MFL's api_info page: limits "are not
fixed and will vary", unregistered clients get a lower ceiling than
registered ones, thresholds are intentionally LOWERED during live
games, and a 429 means "cool down, don't retry immediately." This
client raises Mfl429 on a 429 so the poller can back off per source
instead of hammering it.
"""
import requests

from config import MFL_HOST, MFL_API_HOST, MFL_LEAGUE_ID, MFL_YEAR, MFL_API_KEY, USER_AGENT


class Mfl429(Exception):
    pass


class MflError(Exception):
    pass


def _get(host: str, type_: str, extra: dict | None = None, timeout: int = 20) -> dict:
    params = {"TYPE": type_, "YEAR": MFL_YEAR, "JSON": "1"}
    if extra:
        params.update(extra)
    if MFL_API_KEY:
        params["APIKEY"] = MFL_API_KEY
    url = f"https://{host}.myfantasyleague.com/{MFL_YEAR}/export" if not host.startswith("api") \
        else f"https://{host}/{MFL_YEAR}/export"
    resp = requests.get(url, params=params, headers={"User-Agent": USER_AGENT}, timeout=timeout)
    if resp.status_code == 429:
        raise Mfl429(f"429 from {type_}")
    resp.raise_for_status()
    data = resp.json()
    if "error" in data:
        raise MflError(f"{type_}: {data['error'].get('$t', data['error'])}")
    return data


def live_scoring(week: int) -> dict:
    return _get(MFL_HOST, "liveScoring", {"L": MFL_LEAGUE_ID, "W": str(week)})


def player_scores(week: int) -> dict:
    return _get(MFL_HOST, "playerScores", {"L": MFL_LEAGUE_ID, "W": str(week)})


def standings() -> dict:
    return _get(MFL_HOST, "standings", {"L": MFL_LEAGUE_ID})


def injuries() -> dict:
    # Confirmed: no L= param -- this is a global, non-league-specific export.
    return _get(MFL_API_HOST, "injuries")


def rosters(franchise: str) -> dict:
    return _get(MFL_HOST, "rosters", {"L": MFL_LEAGUE_ID, "FRANCHISE": franchise})


def projected_scores(week: int) -> dict:
    """Not in the build doc's Section 2 list, but Phase 1 panel 1
    ('both projected finals') needs it and it doesn't exist anywhere
    else -- verified 2026-09-12 as a real, working TYPE alongside the
    others rather than assumed from the doc."""
    return _get(MFL_HOST, "projectedScores", {"L": MFL_LEAGUE_ID, "W": str(week)})
