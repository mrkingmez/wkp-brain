"""Shared config for the Sunday Dashboard. No secrets in this file —
MFL_API_KEY comes from the environment, same convention as
fantasy-football-data SKILL.md."""
import os
from pathlib import Path

MFL_HOST = "www44"
MFL_API_HOST = "api.myfantasyleague.com"  # for non-league-specific TYPEs (injuries) — MFL's own
                                            # guidance: spreads load across servers, and league-hosted
                                            # calls to these TYPEs error with "must go to api.myfantasyleague.com"
MFL_LEAGUE_ID = "43094"
MFL_YEAR = "2026"
MFL_FRANCHISE_ID = "0012"  # Caerellius Lions
MFL_API_KEY = os.environ.get("MFL_API_KEY", "")

USER_AGENT = "WKP-Sunday-Dashboard/0.1 (kingzpotus@gmail.com)"

REPO_ROOT = Path(r"D:\WKP")
FF_ROOT = REPO_ROOT / "Fantasy-Football"
DASHBOARD_DIR = FF_ROOT / "dashboard"
CARDS_DIR = FF_ROOT / "cards"  # BLANK templates only, per Zac's naming spec (2026-09-13) -- not the real picks

# Real card locations, exact filenames per Zac (2026-09-13):
PICKUPS_DIR = Path(r"D:\Documents\Pickups 2026")
CARD_CODENAME = "Sanders"


def model_picks_docx_path(week: int) -> Path:
    return PICKUPS_DIR / f"Pickups 2026 - Week {week}.docx"


def hybrid_card_path(week: int) -> Path:
    """The card actually submitted to the league -- human + model
    combined. This is the 'assisted_card' source everywhere in this
    codebase, and what the live dashboard's pick'em panel reads."""
    return PICKUPS_DIR / f"{CARD_CODENAME}_Week{week} Entry.xls"


def control_card_path(week: int) -> Path:
    """Zac's picks, no model input. Starts Week 2 per Zac -- Week 1
    genuinely has none. Callers must check .exists() and treat a
    missing file as ABSENT, not as a card with zero picks -- those are
    different facts (no attempt made vs. an empty attempt)."""
    return PICKUPS_DIR / f"{CARD_CODENAME}_Week{week}P Entry.xls"


STATE_PATH = DASHBOARD_DIR / "state.json"
RAW_CACHE_PATH = DASHBOARD_DIR / ".raw_cache.json"  # poller-internal only; never served to the browser
MFL_429_LOG = DASHBOARD_DIR / "mfl-429-log.txt"  # every 429 MFL returns, timestamped, for a post-Sunday check
POLLER_PID_FILE = DASHBOARD_DIR / "poller.pid"  # written by poller.py's continuous-loop mode; server.py checks it

FF_DATA_SKILL_DIR = REPO_ROOT / ".claude" / "skills" / "fantasy-football-data"
MFL_PLAYERS_CACHE = FF_DATA_SKILL_DIR / "players-cache.json"
SLEEPER_PLAYERS_CACHE = FF_DATA_SKILL_DIR / "sleeper-players-cache.json"
NFL_TEAMS_CACHE = DASHBOARD_DIR / "espn-nfl-teams-cache.json"

PORT = 8787

# Verified 2026-09-12 against MFL's own api_info page: MFL does not
# publish a fixed request-per-minute number ("not fixed and will vary").
# Their concrete guidance: space requests >=1 second apart minimum,
# unregistered clients (this one) get a lower ceiling than registered
# ones, and thresholds are intentionally LOWERED during live games --
# the exact window this dashboard runs in. No client registration has
# been done for this key. These intervals are a wide-margin default
# given that, not a number MFL published -- tighten only after
# registering the client and confirming a real ceiling.
MFL_LIVE_POLL_SECONDS = int(os.environ.get("MFL_POLL_SECONDS", "90"))
MFL_IDLE_POLL_SECONDS = 0  # doc's own rule: stop entirely when nothing is live

ESPN_SCOREBOARD_LIVE_SECONDS = 60
ESPN_SCOREBOARD_IDLE_SECONDS = 15 * 60
ESPN_NEWS_LIVE_SECONDS = 5 * 60
ESPN_NEWS_IDLE_SECONDS = 30 * 60

# 429 backoff: double the relevant interval each consecutive throttle,
# capped, per MFL's own "if you get a 429, cool things down, don't
# retry immediately" guidance.
BACKOFF_MULTIPLIER = 2
BACKOFF_CAP_SECONDS = 20 * 60

STALE_WARNING_MINUTES = 15  # a panel older than this shows the stale banner
