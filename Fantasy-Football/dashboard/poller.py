"""Sunday Dashboard poller. One process: polls sources on a timer,
writes the full snapshot to state.json. The browser/server never
triggers a pull -- see server.py and SKILL doc note in the dashboard
folder README.

Run:
    python poller.py                 loop forever, live-gated polling
    python poller.py --once          single cycle, then exit (testing)
    python poller.py --once --force  single cycle, ignore the
                                      games-live gate (testing outside
                                      a live window)
"""
import argparse
import json
import os
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

import requests

import config
import espn_client
import mfl_client
import pickem_card
import player_bridge
import scoring
import sleeper_client
from team_match import match_nfl_team, match_cfb_team


def log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat()}] {msg}", flush=True)


def load_players_cache() -> dict:
    if not config.MFL_PLAYERS_CACHE.exists():
        raise SystemExit(
            f"{config.MFL_PLAYERS_CACHE} does not exist. Run the fantasy-football-data "
            f"players pull once before starting the poller -- not guessing at player names."
        )
    data = json.loads(config.MFL_PLAYERS_CACHE.read_text(encoding="utf-8"))
    return {p["id"]: p for p in data["players"]["player"]}


def get_current_week() -> int:
    """Sleeper's state endpoint is the cheapest live source of truth for
    the current NFL week -- verified working, no key, no league tie-in.
    NFL_WEEK env var is a manual override for testing a specific week;
    if both are unavailable, fail loudly rather than guessing a week
    number (a wrong week silently pulls the wrong matchup)."""
    import os
    override = os.environ.get("NFL_WEEK")
    if override:
        return int(override)
    resp = requests.get("https://api.sleeper.app/v1/state/nfl", timeout=10)
    resp.raise_for_status()
    return int(resp.json()["week"])


class Source:
    """Tracks per-source polling state: next-due time and 429 backoff."""

    def __init__(self, name: str, base_interval: int):
        self.name = name
        self.base_interval = base_interval
        self.current_interval = base_interval
        self.next_due = 0.0
        self.last_success_at: float | None = None
        self.last_error: str | None = None

    def due(self, now: float) -> bool:
        return self.base_interval > 0 and now >= self.next_due

    def record_success(self, now: float):
        self.last_success_at = now
        self.last_error = None
        self.current_interval = self.base_interval
        self.next_due = now + self.current_interval

    def record_throttle(self, now: float):
        old_interval = self.current_interval
        if old_interval == config.MFL_LIVE_POLL_SECONDS:
            # Specific, requested rule: a 429 at the standard 90s interval
            # backs off to exactly 120s, not the generic 2x doubling.
            self.current_interval = 120
        else:
            self.current_interval = min(
                old_interval * config.BACKOFF_MULTIPLIER, config.BACKOFF_CAP_SECONDS
            )
        self.last_error = "429 throttled -- backed off, not retrying immediately"
        self.next_due = now + self.current_interval
        log(f"{self.name}: {self.last_error} (interval {old_interval}s -> {self.current_interval}s)")
        log_429_event(self.name, old_interval, self.current_interval)

    def record_error(self, now: float, err: str):
        self.last_error = err
        self.next_due = now + self.current_interval
        log(f"{self.name}: error -- {err}")

    def age_seconds(self, now: float) -> float | None:
        if self.last_success_at is None:
            return None
        return now - self.last_success_at

    def meta(self, now: float) -> dict:
        age = self.age_seconds(now)
        return {
            "last_success_at": (
                datetime.fromtimestamp(self.last_success_at, tz=timezone.utc).isoformat()
                if self.last_success_at else None
            ),
            "age_seconds": age,
            "stale": age is not None and age > config.STALE_WARNING_MINUTES * 60,
            "never_succeeded": self.last_success_at is None,
            "last_error": self.last_error,
        }


def log_429_event(source_name: str, old_interval: float, new_interval: float):
    """Section-3-style honesty rule applied to rate limiting: every 429
    gets a durable, timestamped record Zac can check after Sunday,
    independent of whatever's in the scrolling console output."""
    ts = datetime.now(timezone.utc).isoformat()
    note = ""
    if old_interval == config.MFL_LIVE_POLL_SECONDS and new_interval == 120:
        note = " (auto backed off from the standard 90s interval to 120s)"
    line = f"{ts}\t{source_name}\t429 received\tinterval {old_interval}s -> {new_interval}s{note}\n"
    config.MFL_429_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(config.MFL_429_LOG, "a", encoding="utf-8") as f:
        f.write(line)


DISAGREEMENT_THRESHOLD_PCT = 30.0


def build_matchup_panel(live: dict, proj: dict, players: dict, sleeper_proj: dict | None,
                         rules: list[dict] | None = None) -> dict:
    """Two independently-sourced projected finals, side by side:
    - mfl_projected_final: MFL's own TYPE=projectedScores export.
    - irfl_scoring_projected_final: Sleeper's raw projected component
      stats (pass_yd, idp_tkl_solo, etc.), run through scoring.py's
      score_player() under the real IRFL rules from
      FF-SCORING-RULES.md. Never reads Sleeper's pts_ppr.
    Requires the MFL<->Sleeper player bridge (player_bridge.py) to look
    up each starter's Sleeper projection; a starter with no bridge
    match is skipped from the IRFL-scoring total and listed under
    'unbridged_players' so the gap is visible, not silently absorbed
    into a slightly-low number.
    """
    matchups = live["liveScoring"]["matchup"]
    proj_by_id = {}
    for p in proj.get("projectedScores", {}).get("playerScore", []):
        try:
            proj_by_id[p["id"]] = float(p["score"])
        except (TypeError, ValueError):
            proj_by_id[p["id"]] = 0.0  # MFL sends "" for some players (e.g. no projection available)

    mine, opp = None, None
    for m in matchups:
        ids = [f["id"] for f in m["franchise"]]
        if config.MFL_FRANCHISE_ID in ids:
            fr_by_id = {f["id"]: f for f in m["franchise"]}
            mine = fr_by_id[config.MFL_FRANCHISE_ID]
            opp_id = [i for i in ids if i != config.MFL_FRANCHISE_ID][0]
            opp = fr_by_id[opp_id]
            opp["id"] = opp_id
            break

    if mine is None:
        return {"error": f"Franchise {config.MFL_FRANCHISE_ID} not found in this week's liveScoring matchups."}

    genuine_disagreements = []
    missing_data = []
    unbridged = []
    approx_kicker_ids = []

    def irfl_score_for(mfl_id: str, position: str | None) -> float | None:
        if sleeper_proj is None:
            return None
        sleeper_id = player_bridge.mfl_to_sleeper(mfl_id)
        if sleeper_id is None:
            unbridged.append(mfl_id)
            return None
        stats = sleeper_proj.get(sleeper_id)
        if stats is None:
            return 0.0  # bridged fine, Sleeper just has no projection row for them this week
        if position == "PK":
            approx_kicker_ids.append(mfl_id)
            return scoring.score_kicker_approx(stats, rules).total
        return scoring.score_player(stats, rules).total

    def side(fr, side_label: str):
        starters = fr["players"]["player"]
        mfl_projected_final = 0.0
        irfl_projected_final = 0.0
        for p in starters:
            try:
                actual = float(p["score"])
            except (TypeError, ValueError):
                actual = 0.0
            not_started = p.get("gameSecondsRemaining") == "3600"
            player_info = players.get(p["id"], {})
            position = player_info.get("position")

            mfl_val = proj_by_id.get(p["id"], 0.0)
            irfl_val = irfl_score_for(p["id"], position)

            if not_started:
                mfl_projected_final += mfl_val
                irfl_projected_final += irfl_val if irfl_val is not None else mfl_val  # fall back rather than understate
            else:
                mfl_projected_final += actual
                irfl_projected_final += actual

            if not_started and irfl_val is not None:
                denom = max(abs(mfl_val), abs(irfl_val), 0.01)
                pct_diff = abs(mfl_val - irfl_val) / denom * 100
                if pct_diff > DISAGREEMENT_THRESHOLD_PCT:
                    entry = {
                        "side": side_label,
                        "player_id": p["id"],
                        "name": player_info.get("name", f"Unknown ({p['id']})"),
                        "position": position,
                        "mfl_projected": round(mfl_val, 2),
                        "irfl_scoring_projected": round(irfl_val, 2),
                        "pct_diff": round(pct_diff, 1),
                    }
                    if mfl_val == 0.0 or irfl_val == 0.0:
                        entry["reason"] = (
                            "MFL has no projection for this player" if mfl_val == 0.0
                            else "Sleeper has no component projection for this player this week"
                        )
                        missing_data.append(entry)
                    else:
                        genuine_disagreements.append(entry)

        return {
            "franchise_id": fr["id"],
            "score": float(fr["score"]),
            "players_yet_to_play": int(fr.get("playersYetToPlay", -1)),
            "players_currently_playing": int(fr.get("playersCurrentlyPlaying", -1)),
            "mfl_projected_final": round(mfl_projected_final, 2),
            "irfl_scoring_projected_final": round(irfl_projected_final, 2),
            # kept for backward compat with anything still reading the old key
            "projected_final": round(mfl_projected_final, 2),
        }

    result = {"mine": side(mine, "mine"), "opponent": side(opp, "opponent")}
    genuine_disagreements.sort(key=lambda d: d["pct_diff"], reverse=True)
    missing_data.sort(key=lambda d: d["pct_diff"], reverse=True)
    result["genuine_disagreements"] = genuine_disagreements
    result["missing_data"] = missing_data
    result["disagreement_threshold_pct"] = DISAGREEMENT_THRESHOLD_PCT
    if unbridged:
        result["unbridged_players"] = sorted(set(unbridged))
    if approx_kicker_ids:
        result["kicker_scoring_note"] = (
            "IRFL-scoring figures for kicker(s) "
            f"{', '.join(sorted(set(approx_kicker_ids)))} are APPROXIMATE -- Sleeper only exposes "
            "banded field-goal-made counts, not exact distance, so field goals are priced at their "
            "band's midpoint rather than the real kick length. Do not treat as league-verified."
        )
    return result


def build_inactive_alert(live: dict, injuries_data: dict, players: dict) -> dict:
    matchups = live["liveScoring"]["matchup"]
    my_starters = []
    for m in matchups:
        for f in m["franchise"]:
            if f["id"] == config.MFL_FRANCHISE_ID:
                my_starters = [p["id"] for p in f["players"]["player"]]

    injury_by_id = {i["id"]: i for i in injuries_data.get("injuries", {}).get("injury", [])}
    flagged_statuses = {"OUT", "DOUBTFUL", "QUESTIONABLE", "IR", "RETIRED"}

    alerts = []
    for pid in my_starters:
        inj = injury_by_id.get(pid)
        if inj and inj.get("status", "").upper() in flagged_statuses:
            p = players.get(pid, {})
            alerts.append({
                "player_id": pid,
                "name": p.get("name", f"Unknown ({pid})"),
                "position": p.get("position"),
                "team": p.get("team"),
                "status": inj.get("status"),
                "details": inj.get("details"),
            })
    return {"alerts": alerts}


def _event_status(comp: dict, competitor: dict, other: dict) -> dict:
    """Shared status-dict shape for both NFL and CFB events. Real bug
    fixed here 2026-09-13: the old NCAA-specific branch built a status
    dict with only 'status'/'clock' -- no scores at all -- so every
    college game's ATS 'covering' computation silently used 0-0 no
    matter the real score. This is the one place either league builds
    a status dict now, so that gap can't reopen for one league and not
    the other."""
    status_type = comp["status"]["type"]
    return {
        "status": status_type["description"],
        "state": status_type["state"],           # 'pre' | 'in' | 'post'
        "completed": status_type["completed"],
        "clock": comp["status"].get("displayClock"),
        "period": comp["status"].get("period"),
        # "10:22 - 2nd" / "Final" / "9/13 - 8:20 PM EDT" -- one clean
        # string for every state, straight from ESPN, no assembly needed.
        "short_detail": status_type.get("shortDetail") or status_type.get("description"),
        "abbr": competitor["team"]["abbreviation"],
        "my_team_score": competitor.get("score"),
        "other_team_score": other.get("score"),
        "other_abbr": other["team"]["abbreviation"],
    }


def _nfl_status(nfl_events: list, team_abbr: str) -> dict | None:
    for event in nfl_events:
        comp = event["competitions"][0]
        for competitor in comp["competitors"]:
            if competitor["team"]["abbreviation"] == team_abbr:
                other = next(c for c in comp["competitors"] if c is not competitor)
                return _event_status(comp, competitor, other)
    return None


def _cfb_status(match: tuple) -> dict | None:
    if match is None:
        return None
    event, team = match
    comp = event["competitions"][0]
    competitor = next(c for c in comp["competitors"] if c["team"]["abbreviation"] == team["abbreviation"])
    other = next(c for c in comp["competitors"] if c is not competitor)
    return _event_status(comp, competitor, other)


def _pick_side_state(game_state: str | None, covering: str | None, side: str) -> str:
    """side is 'favored' or 'underdog'. Vocabulary: 'upcoming' before
    kickoff, 'covering'/'not_covering' while live, 'won'/'lost' once
    final. No 'push' -- this league has none (Zac, 2026-09-13: an exact
    margin-equals-spread result goes to the underdog, not a refund;
    already documented in Fantasy-Football/CLAUDE.md's pick'em section
    as "Underdog wins ties", which this codebase had not honored until
    now). `covering` (computed in enrich(), below) never returns "push"
    anymore -- see that function for the tie-goes-to-underdog logic."""
    if game_state is None or covering is None:
        return "unknown"
    if game_state == "pre":
        return "upcoming"
    is_final = game_state == "post"
    side_is_covering = covering == side
    if is_final:
        return "won" if side_is_covering else "lost"
    return "covering" if side_is_covering else "not_covering"


def build_pickem_panel(week: int, nfl_scoreboard: dict, cfb_scoreboard_data: dict, nfl_teams: list) -> dict:
    # Real submitted card (hybrid: human + model), per Zac's spec
    # 2026-09-13 -- D:\Documents\Pickups 2026\Sanders_Week{N} Entry.xls.
    # config.CARDS_DIR now holds BLANK templates only and is never read
    # for live tracking.
    path = config.hybrid_card_path(week)
    if not path.exists():
        return {"card_found": False, "message": f"No hybrid card found for week {week} at {path}."}

    card = pickem_card.read_card(path)

    nfl_events = nfl_scoreboard.get("events", [])
    cfb_events = cfb_scoreboard_data.get("events", [])

    def enrich(g: dict, is_nfl: bool) -> dict:
        fav_status, dog_status = None, None
        if is_nfl:
            fav_team = match_nfl_team(g["favored"], nfl_teams)
            dog_team = match_nfl_team(g["underdog"], nfl_teams)
            fav_status = _nfl_status(nfl_events, fav_team["abbreviation"]) if fav_team else None
            dog_status = _nfl_status(nfl_events, dog_team["abbreviation"]) if dog_team else None
        else:
            fav_status = _cfb_status(match_cfb_team(g["favored"], cfb_events))
            dog_status = _cfb_status(match_cfb_team(g["underdog"], cfb_events))

        covering = None
        if fav_status and dog_status and g["spread"] is not None:
            try:
                fav_pts = float(fav_status.get("my_team_score") or 0)
                dog_pts = float(dog_status.get("my_team_score") or 0)
                margin = fav_pts - dog_pts
                # No push in this league (Zac, 2026-09-13): an exact
                # margin == spread result goes to the underdog, not a
                # refund. Already favorite-relative here (margin is
                # fav_pts - dog_pts), so the tie case falls straight
                # into "underdog" with no separate favorite/home
                # conflation to account for -- unlike grader.py's
                # home/away-relative version, which needed explicit
                # case analysis for the same rule.
                covering = "favored" if margin > g["spread"] else "underdog"
            except (TypeError, ValueError):
                covering = None

        game_state = fav_status["state"] if fav_status else (dog_status["state"] if dog_status else None)
        favored_state = _pick_side_state(game_state, covering, "favored")
        underdog_state = _pick_side_state(game_state, covering, "underdog")

        if g["pick"] == "favored":
            pick_state = favored_state
        elif g["pick"] == "underdog":
            pick_state = underdog_state
        else:
            pick_state = None

        # Zac's hand-applied color is NEVER authoritative -- ESPN's score
        # is what grades a pick, everywhere in this codebase. The color
        # is only ever compared against that real result to catch a
        # disagreement, per Zac's explicit instruction 2026-09-13.
        #
        # No "push" state exists anymore (ties go to the underdog, see
        # _pick_side_state), so the only two possible ESPN-graded states
        # for a decided pick are "won"/"lost" -- a mismatch is now just
        # color says "loss" but ESPN says "won". Re-checked SEATTLE
        # under the corrected rule: SEA (favorite) exact-tied the 3.0
        # spread, and ties go to the underdog, so SEA's pick is now
        # graded "lost" -- which MATCHES Zac's red mark. The discrepancy
        # that existed under the old (incorrect) push-based grading is
        # gone, but not because the pick became a win -- it's because
        # the correct grade and the hand mark now agree it's a loss.
        color_discrepancy = None
        if g["pick_outcome_hint"] == "loss" and pick_state == "won":
            color_discrepancy = {
                "pick_team": g["pick_team"],
                "color_says": "loss",
                "espn_says": pick_state,
            }

        # Display fields computed here, not in the browser -- state.json
        # stays self-describing and app.js stays a thin renderer.
        pick_line = -g["spread"] if g["pick"] == "favored" else g["spread"]
        pick_display = f"{g['pick_team']} {pick_line:+g}" if g["pick_team"] and g["spread"] is not None else g["pick_team"]

        game_display, leader_abbr, clock_display = None, None, None
        if fav_status or dog_status:
            fa = fav_status["abbr"] if fav_status else "?"
            da = dog_status["abbr"] if dog_status else "?"
            fs = fav_status.get("my_team_score") if fav_status else None
            ds = dog_status.get("my_team_score") if dog_status else None
            game_display = f"{fa} {fs if fs is not None else '-'} - {da} {ds if ds is not None else '-'}"
            clock_display = (fav_status or dog_status)["short_detail"]
            try:
                fs_n, ds_n = float(fs), float(ds)
                if fs_n > ds_n:
                    leader_abbr = fa
                elif ds_n > fs_n:
                    leader_abbr = da
            except (TypeError, ValueError):
                pass

        verdict_map = {
            "upcoming": "NOT_STARTED", "unknown": "NOT_STARTED",
            "covering": "WINNING", "not_covering": "LOSING",
            "won": "WON", "lost": "LOST",
        }
        verdict = verdict_map.get(pick_state, "NOT_STARTED")

        return {
            **g,
            "favored_live": fav_status,
            "underdog_live": dog_status,
            "currently_covering": covering,
            "favored_state": favored_state,
            "underdog_state": underdog_state,
            "pick_state": pick_state,
            "color_discrepancy": color_discrepancy,
            "match_found": bool(fav_status or dog_status),
            "pick_display": pick_display,
            "game_display": game_display,
            "leader_abbr": leader_abbr,
            "clock_display": clock_display,
            "verdict": verdict,
        }

    enriched_games = [enrich(g, g["section"] == "NFL") for g in card["games"]]

    # The Monday-night tiebreaker game is one of the real 20 ATS picks
    # (real bug fixed 2026-09-13: it was never enriched with live status
    # at all before, and the card record silently excluded it, undercounting
    # every week's total by one game). Always NFL -- the tiebreaker is
    # Monday Night Football by rule.
    enriched_tiebreaker = enrich(card["tiebreaker"], is_nfl=True) if card["tiebreaker"] else None
    record_input = enriched_games + ([enriched_tiebreaker] if enriched_tiebreaker else [])
    discrepancies = [g["color_discrepancy"] for g in record_input if g["color_discrepancy"]]

    return {
        "card_found": True,
        "source_file": card["source_file"],
        "ats_pick_marking_confirmed": card["ats_pick_marking_confirmed"],
        "ats_pick_note": card["ats_pick_note"],
        "no_picks_detected": card["no_picks_detected"],
        "eliminator_pick": card["eliminator_pick"],
        "tiebreaker": enriched_tiebreaker,
        "games": enriched_games,
        "record": build_card_record(record_input),
        "color_discrepancies": discrepancies,
    }


def build_card_record(enriched_games: list) -> dict:
    """RESOLVED 2026-09-13 (was decision FF-2026-09-12-01): picks are
    marked by fill color, read directly by pickem_card.py, so each
    game's real 'pick'/'pick_team' fields are trustworthy now -- this
    reports Zac's ACTUAL running record, not a favorite-side reference.
    A game whose pick state is None or 'ambiguous' (zero or multiple
    filled cells -- confirmed zero such rows on the real Week 1 card,
    but a future week's card could still have one) is counted as
    undecided/unknown rather than guessed."""
    total = len(enriched_games)
    won = lost = undecided = unknown_pick = 0

    for g in enriched_games:
        if g["pick"] == "favored":
            state = g["favored_state"]
        elif g["pick"] == "underdog":
            state = g["underdog_state"]
        else:
            unknown_pick += 1
            continue

        # No "push" state possible anymore (Zac, 2026-09-13: no push in
        # this league, ties go to the underdog) -- won/lost/undecided only.
        if state == "won":
            won += 1
        elif state == "lost":
            lost += 1
        else:  # upcoming, covering, not_covering, unknown
            undecided += 1

    return {
        "pick_side_known": True,
        "note": "Real record -- picks read from filled cell color on the submitted card.",
        "record": {
            "won": won, "lost": lost,
            "undecided": undecided, "unknown_pick": unknown_pick, "total": total,
        },
    }


def _card_team_names(week: int) -> set[str]:
    """The set of team-name strings (as typed on the card) appearing in
    this week's pick'em card -- used only to flag on_card in the full
    scoreboard, not to identify a pick side. Reads the real hybrid
    card, not the blank templates in config.CARDS_DIR."""
    path = config.hybrid_card_path(week)
    if not path.exists():
        return set()
    card = pickem_card.read_card(path)
    names = set()
    for g in card["games"]:
        names.add(g["favored"])
        names.add(g["underdog"])
    if card.get("tiebreaker"):
        names.add(card["tiebreaker"]["favored"])
        names.add(card["tiebreaker"]["underdog"])
    return names


def build_full_scoreboard_panel(week: int, nfl_scoreboard: dict, cfb_scoreboard_data: dict, nfl_teams: list) -> dict:
    """Every game currently IN PROGRESS across both pro and college,
    regardless of whether it's on the card -- with score, clock, and an
    on_card flag so card games stand out. Complements the pick'em panel
    (which only shows the ~20 card games); this shows everything live."""
    card_names = _card_team_names(week)
    on_card_abbrs = set()
    for name in card_names:
        t = match_nfl_team(name, nfl_teams)
        if t:
            on_card_abbrs.add(t["abbreviation"])

    def nfl_row(event):
        comp = event["competitions"][0]
        away = next(c for c in comp["competitors"] if c["homeAway"] == "away")
        home = next(c for c in comp["competitors"] if c["homeAway"] == "home")
        return {
            "league": "NFL",
            "away_team": away["team"]["abbreviation"], "away_score": away.get("score"),
            "home_team": home["team"]["abbreviation"], "home_score": home.get("score"),
            "clock": comp["status"].get("displayClock"),
            "status": comp["status"]["type"]["description"],
            "on_card": away["team"]["abbreviation"] in on_card_abbrs or home["team"]["abbreviation"] in on_card_abbrs,
        }

    def cfb_row(event):
        comp = event["competitions"][0]
        away = next(c for c in comp["competitors"] if c["homeAway"] == "away")
        home = next(c for c in comp["competitors"] if c["homeAway"] == "home")
        # CFB on_card check: card text is loose (e.g. 'Oklahoma'), so
        # match by substring against the card's own team-name strings
        # rather than requiring an exact abbreviation match.
        away_name = away["team"].get("shortDisplayName", "")
        home_name = home["team"].get("shortDisplayName", "")
        on_card = any(
            n.upper() in away_name.upper() or away_name.upper() in n.upper()
            or n.upper() in home_name.upper() or home_name.upper() in n.upper()
            for n in card_names
        )
        return {
            "league": "CFB",
            "away_team": away_name, "away_score": away.get("score"),
            "home_team": home_name, "home_score": home.get("score"),
            "clock": comp["status"].get("displayClock"),
            "status": comp["status"]["type"]["description"],
            "on_card": on_card,
        }

    nfl_live = [nfl_row(e) for e in nfl_scoreboard.get("events", [])
                if e["competitions"][0]["status"]["type"]["state"] == "in"]
    cfb_live = [cfb_row(e) for e in cfb_scoreboard_data.get("events", [])
                if e["competitions"][0]["status"]["type"]["state"] == "in"]

    games = sorted(nfl_live + cfb_live, key=lambda g: not g["on_card"])  # on_card games first
    return {"games": games, "live_count": len(games)}


def build_news_panel(headlines: list, players: dict, live: dict) -> dict:
    matchups = live.get("liveScoring", {}).get("matchup", []) if live else []
    roster_ids = set()
    for m in matchups:
        ids = [f["id"] for f in m["franchise"]]
        if config.MFL_FRANCHISE_ID in ids:
            for f in m["franchise"]:
                for p in f["players"]["player"]:
                    roster_ids.add(p["id"])
            break
    roster_names = {players[pid]["name"].split(",")[0].strip().lower() for pid in roster_ids if pid in players}

    relevant, other = [], []
    for h in headlines:
        title_lower = h["title"].lower()
        if any(name and name in title_lower for name in roster_names):
            relevant.append(h)
        else:
            other.append(h)

    return {
        "delay_notice": "Free RSS feed -- runs minutes to a half hour behind Twitter/X breaking news. Not a first-alert source.",
        "relevant": relevant,
        "other_collapsed": other,
    }


def atomic_write_json(path: Path, obj: dict):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, indent=2), encoding="utf-8")
    tmp.replace(path)


def run_cycle(week: int, players: dict, sources: dict, force: bool) -> dict:
    now = time.time()
    raw = {}
    if config.RAW_CACHE_PATH.exists():
        try:
            raw = json.loads(config.RAW_CACHE_PATH.read_text(encoding="utf-8"))
        except Exception:
            raw = {}

    # ESPN scoreboard always polls (it's what decides whether MFL polls at all)
    if force or sources["espn_scoreboard"].due(now):
        try:
            raw["espn_scoreboard"] = espn_client.nfl_scoreboard()
            sources["espn_scoreboard"].record_success(now)
        except Exception as e:
            sources["espn_scoreboard"].record_error(now, str(e))

    games_live = force or (raw.get("espn_scoreboard") and espn_client.any_game_live(raw["espn_scoreboard"]))

    # re-derive intervals based on live/idle state
    sources["espn_scoreboard"].base_interval = (
        config.ESPN_SCOREBOARD_LIVE_SECONDS if games_live else config.ESPN_SCOREBOARD_IDLE_SECONDS
    )
    sources["espn_news"].base_interval = (
        config.ESPN_NEWS_LIVE_SECONDS if games_live else config.ESPN_NEWS_IDLE_SECONDS
    )
    for name in ("mfl_live_scoring", "mfl_injuries", "mfl_standings", "mfl_projected"):
        sources[name].base_interval = config.MFL_LIVE_POLL_SECONDS if games_live else config.MFL_IDLE_POLL_SECONDS

    if force or sources["espn_news"].due(now):
        try:
            raw["espn_news"] = espn_client.news_headlines()
            sources["espn_news"].record_success(now)
        except Exception as e:
            sources["espn_news"].record_error(now, str(e))

    if not config.NFL_TEAMS_CACHE.exists() or force:
        try:
            raw["nfl_teams"] = espn_client.nfl_teams()
            config.NFL_TEAMS_CACHE.write_text(json.dumps(raw["nfl_teams"]), encoding="utf-8")
        except Exception as e:
            log(f"nfl_teams fetch failed: {e}")
    if "nfl_teams" not in raw and config.NFL_TEAMS_CACHE.exists():
        raw["nfl_teams"] = json.loads(config.NFL_TEAMS_CACHE.read_text(encoding="utf-8"))

    # Sleeper projections -- fetched once per process (cached in .raw_cache.json
    # across cycles, same as nfl_teams), not on the 90s live-poll cadence.
    # Feeds the dual-projection comparison in build_matchup_panel.
    if "sleeper_proj" not in raw or force:
        try:
            raw["sleeper_proj"] = sleeper_client.week_projections(int(config.MFL_YEAR), week)
        except Exception as e:
            log(f"sleeper projections fetch failed: {e}")

    if games_live:
        if force or sources["mfl_live_scoring"].due(now):
            try:
                raw["mfl_live_scoring"] = mfl_client.live_scoring(week)
                sources["mfl_live_scoring"].record_success(now)
            except mfl_client.Mfl429:
                sources["mfl_live_scoring"].record_throttle(now)
            except Exception as e:
                sources["mfl_live_scoring"].record_error(now, str(e))

        if force or sources["mfl_projected"].due(now):
            try:
                raw["mfl_projected"] = mfl_client.projected_scores(week)
                sources["mfl_projected"].record_success(now)
            except mfl_client.Mfl429:
                sources["mfl_projected"].record_throttle(now)
            except Exception as e:
                sources["mfl_projected"].record_error(now, str(e))

        if force or sources["mfl_injuries"].due(now):
            try:
                raw["mfl_injuries"] = mfl_client.injuries()
                sources["mfl_injuries"].record_success(now)
            except mfl_client.Mfl429:
                sources["mfl_injuries"].record_throttle(now)
            except Exception as e:
                sources["mfl_injuries"].record_error(now, str(e))

        if force or sources["mfl_standings"].due(now):
            try:
                raw["mfl_standings"] = mfl_client.standings()
                sources["mfl_standings"].record_success(now)
            except mfl_client.Mfl429:
                sources["mfl_standings"].record_throttle(now)
            except Exception as e:
                sources["mfl_standings"].record_error(now, str(e))
    else:
        log("no games live -- MFL polling stopped for this cycle")

    sources["espn_cfb_scoreboard"].base_interval = (
        config.ESPN_SCOREBOARD_LIVE_SECONDS if games_live else config.ESPN_SCOREBOARD_IDLE_SECONDS
    )
    if force or sources["espn_cfb_scoreboard"].due(now):
        try:
            raw["espn_cfb_scoreboard"] = espn_client.cfb_scoreboard()
            sources["espn_cfb_scoreboard"].record_success(now)
        except Exception as e:
            sources["espn_cfb_scoreboard"].record_error(now, str(e))
    cfb = raw.get("espn_cfb_scoreboard", {"events": []})

    panels = {}

    if "mfl_live_scoring" in raw and "mfl_projected" in raw:
        panels["matchup"] = build_matchup_panel(
            raw["mfl_live_scoring"], raw["mfl_projected"], players, raw.get("sleeper_proj")
        )
    elif "mfl_live_scoring" in raw:
        panels["matchup"] = {"note": "projectedScores not yet pulled this cycle"}
    else:
        panels["matchup"] = {"error": "No liveScoring data yet."}

    if "mfl_live_scoring" in raw and "mfl_injuries" in raw:
        panels["inactive_alert"] = build_inactive_alert(raw["mfl_live_scoring"], raw["mfl_injuries"], players)
    else:
        panels["inactive_alert"] = {"alerts": [], "note": "Waiting on liveScoring and/or injuries data."}

    panels["pickem"] = build_pickem_panel(
        week, raw.get("espn_scoreboard", {"events": []}), cfb, raw.get("nfl_teams", [])
    )

    panels["full_scoreboard"] = build_full_scoreboard_panel(
        week, raw.get("espn_scoreboard", {"events": []}), cfb, raw.get("nfl_teams", [])
    )

    panels["news"] = build_news_panel(
        raw.get("espn_news", []), players, raw.get("mfl_live_scoring", {"liveScoring": {"matchup": []}})
    )

    atomic_write_json(config.RAW_CACHE_PATH, raw)

    state_out = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "week": week,
        "games_live": bool(games_live),
        "franchise_id": config.MFL_FRANCHISE_ID,
        "sources": {name: src.meta(now) for name, src in sources.items()},
        "panels": panels,
    }
    return state_out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--force", action="store_true", help="ignore the games-live gate (testing)")
    args = parser.parse_args()

    config.DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)
    players = load_players_cache()

    sources = {
        "espn_scoreboard": Source("espn_scoreboard", config.ESPN_SCOREBOARD_IDLE_SECONDS),
        "espn_cfb_scoreboard": Source("espn_cfb_scoreboard", config.ESPN_SCOREBOARD_IDLE_SECONDS),
        "espn_news": Source("espn_news", config.ESPN_NEWS_IDLE_SECONDS),
        "mfl_live_scoring": Source("mfl_live_scoring", config.MFL_LIVE_POLL_SECONDS),
        "mfl_projected": Source("mfl_projected", config.MFL_LIVE_POLL_SECONDS),
        "mfl_injuries": Source("mfl_injuries", config.MFL_LIVE_POLL_SECONDS),
        "mfl_standings": Source("mfl_standings", config.MFL_LIVE_POLL_SECONDS),
    }

    try:
        week = get_current_week()
    except Exception as e:
        log(f"Could not determine current week from Sleeper: {e}. Set NFL_WEEK env var to override.")
        sys.exit(1)

    log(f"Sunday Dashboard poller starting -- week {week}, franchise {config.MFL_FRANCHISE_ID}")

    if args.once:
        state = run_cycle(week, players, sources, force=args.force)
        atomic_write_json(config.STATE_PATH, state)
        log(f"wrote {config.STATE_PATH}")
        return

    # Continuous-loop mode only -- lets server.py (or Zac, by hand) tell
    # whether a poller is actually running before assuming state.json is
    # live. Removed on clean exit; a stale file (process gone) is
    # detected by PID check, not by the file's mere existence.
    config.POLLER_PID_FILE.write_text(str(os.getpid()), encoding="utf-8")
    try:
        while True:
            try:
                state = run_cycle(week, players, sources, force=False)
                atomic_write_json(config.STATE_PATH, state)
            except Exception:
                log("unhandled error in poll cycle:\n" + traceback.format_exc())
            time.sleep(10)
    finally:
        if config.POLLER_PID_FILE.exists():
            config.POLLER_PID_FILE.unlink()


if __name__ == "__main__":
    main()
