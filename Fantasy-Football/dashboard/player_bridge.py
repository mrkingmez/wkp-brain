"""MFL <-> Sleeper player ID bridge.

Solves the gap flagged in FF-DATA-PATCH-sleeper-espn.md: "MFL player IDs
and Sleeper player IDs are different numbering systems... nothing joins
them out of the box." That patch proposed cross-referencing third-party
IDs first, falling back to name+position+team matching. Verified
2026-09-13 that path #1 actually works: MFL's players export with
`&DETAILS=1` carries a real `espn_id` field, and Sleeper's player
objects carry the same `espn_id` -- confirmed identical for Fred
Warner (3138826 on both sides) before trusting this for real.

Per that same patch: "Do not silently drop players that fail to match.
Write unmatched players to a unmatched.log and surface the count."
"""
import json
from pathlib import Path

SKILL_DIR = Path(r"D:\WKP\.claude\skills\fantasy-football-data")
MFL_DETAILS_CACHE = SKILL_DIR / "players-cache-details.json"
SLEEPER_CACHE = SKILL_DIR / "sleeper-players-cache.json"
UNMATCHED_LOG = Path(__file__).parent / "unmatched.log"

_bridge_cache = None


def _normalize_id(v) -> str | None:
    if v in (None, "", 0, "0"):
        return None
    return str(v).strip()


def build_bridge() -> dict:
    """Returns {mfl_id: sleeper_id}. Cached in-process; call again after
    re-pulling either source cache to rebuild."""
    global _bridge_cache
    if _bridge_cache is not None:
        return _bridge_cache

    if not MFL_DETAILS_CACHE.exists():
        raise SystemExit(f"{MFL_DETAILS_CACHE} missing -- pull MFL TYPE=players&DETAILS=1 first.")
    if not SLEEPER_CACHE.exists():
        raise SystemExit(f"{SLEEPER_CACHE} missing -- pull Sleeper v1/players/nfl first.")

    mfl_players = json.loads(MFL_DETAILS_CACHE.read_text(encoding="utf-8"))["players"]["player"]
    sleeper_players = json.loads(SLEEPER_CACHE.read_text(encoding="utf-8"))

    # Index Sleeper players by espn_id and rotowire_id for O(1) lookup.
    sleeper_by_espn, sleeper_by_rotowire = {}, {}
    for sid, p in sleeper_players.items():
        eid = _normalize_id(p.get("espn_id"))
        if eid:
            sleeper_by_espn[eid] = sid
        rid = _normalize_id(p.get("rotowire_id"))
        if rid:
            sleeper_by_rotowire[rid] = sid

    bridge, unmatched = {}, []
    for mp in mfl_players:
        mfl_id = mp["id"]
        eid = _normalize_id(mp.get("espn_id"))
        rid = _normalize_id(mp.get("rotowire_id"))

        sleeper_id = sleeper_by_espn.get(eid) if eid else None
        match_method = "espn_id" if sleeper_id else None
        if sleeper_id is None and rid:
            sleeper_id = sleeper_by_rotowire.get(rid)
            match_method = "rotowire_id" if sleeper_id else None

        if sleeper_id:
            bridge[mfl_id] = sleeper_id
        else:
            unmatched.append({"mfl_id": mfl_id, "name": mp.get("name"), "team": mp.get("team"),
                               "position": mp.get("position"), "espn_id": mp.get("espn_id")})

    if unmatched:
        UNMATCHED_LOG.write_text(
            f"{len(unmatched)} MFL players did not match a Sleeper player via espn_id or rotowire_id.\n"
            f"Name-matching fallback is NOT implemented -- these are simply unbridged.\n\n" +
            "\n".join(f"{u['mfl_id']}\t{u['name']}\t{u['team']}\t{u['position']}\tespn_id={u['espn_id']}"
                       for u in unmatched),
            encoding="utf-8",
        )

    print(f"Player bridge built: {len(bridge)} matched, {len(unmatched)} unmatched "
          f"(see {UNMATCHED_LOG} if > 0).")

    _bridge_cache = bridge
    return bridge


def mfl_to_sleeper(mfl_id: str) -> str | None:
    return build_bridge().get(mfl_id)
