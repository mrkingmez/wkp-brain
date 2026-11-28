import hashlib
import json
import math
import os

import yaml

REQUIRED = [
    "cluster.min_insiders", "cluster.watch_min_insiders", "cluster.window_days", "cluster.count_roles", "cluster.exclude_entity_owners", "cluster.exclude_fund_issuers", "cluster.max_filing_lag_business_days",
    "timing.accepted_tz", "timing.premarket_entry_cutoff_et",
    "filing.transaction_codes_kept", "filing.exclude_10b5_1", "filing.offering_min_owners", "filing.offering_keywords",
    "classify.entity_words", "classify.fund_issuer_words", "classify.fund_issuer_phrases", "classify.fund_sic_codes", "classify.ceo_regex", "classify.cfo_regex",
    "classify.tiny_base_usd", "classify.pct_change_uninformative_over",
    "sec.allowed_hosts", "sec.max_requests_per_second", "sec.retries", "sec.backoff_seconds", "sec.timeout_seconds",
    "sec.max_response_bytes", "sec.max_filings_per_run", "sec.lookback_days", "sec.user_agent_env",
    "forward.benchmark", "forward.benchmarks", "forward.feed", "forward.horizons", "forward.haircut_bps", "forward.pass_haircut_bps",
    "forward.zac_extra_trading_days", "forward.cost_floor_bps", "forward.fill_window_minutes", "forward.min_price", "forward.min_avg_dollar_volume",
    "primary_test.registered_on", "primary_test.population", "primary_test.ledger", "primary_test.horizon_trading_days", "primary_test.cost",
    "primary_test.metric", "primary_test.benchmarks", "primary_test.adoption",
    "isolation.writes_to_watcher", "isolation.feeds_watcher_score", "isolation.adoption",
    "kill_criteria.K1.at_counted", "kill_criteria.K1.mean_at_or_below", "kill_criteria.K1.median_at_or_below", "kill_criteria.K2.at_qualifying",
    "kill_criteria.K2.unfilled_share_over", "kill_criteria.K3.at_filled", "kill_criteria.K3.median_round_trip_cost_over",
    "kill_criteria.K4.months_after_first_counted_day", "kill_criteria.K4.counted_under", "kill_criteria.K7.resets_at_or_over", "kill_criteria.K7.before_counted",
    "freeze.counted_signals_from_et",
    "forward.liquidity_lookback_days", "forward.missing_best_case_over_pct", "forward.position_usd", "forward.min_listing_age_trading_days", "forward.listing_history_calendar_days", "forward.min_counted_for_verdict", "forward.watcher_dir",
]


def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    validate(cfg)
    return cfg


def config_hash(cfg):
    """Fingerprint of the PARSED config: comments and spacing do not change it, any value does."""
    blob = json.dumps(cfg, sort_keys=True, default=str, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def _num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def f_horizons(cfg):
    h = cfg.get("forward", {}).get("horizons")
    return h if isinstance(h, list) else []


def validate(cfg):
    if not isinstance(cfg, dict):
        raise ValueError("config is not a mapping")
    for dotted in REQUIRED:
        cur = cfg
        for part in dotted.split("."):
            if not isinstance(cur, dict) or part not in cur or cur[part] is None:
                raise ValueError("config missing required key: " + dotted)
            cur = cur[part]
    c = cfg["cluster"]
    if not isinstance(c["min_insiders"], int) or c["min_insiders"] < 2:
        raise ValueError("cluster.min_insiders must be an integer of 2 or more")
    if not isinstance(c["watch_min_insiders"], int) or not (2 <= c["watch_min_insiders"] < c["min_insiders"]):
        raise ValueError("cluster.watch_min_insiders must be an integer from 2 up to min_insiders minus 1")
    if not isinstance(c["window_days"], int) or c["window_days"] < 1:
        raise ValueError("cluster.window_days must be a positive integer")
    for k in ("exclude_entity_owners", "exclude_fund_issuers"):
        if not isinstance(c[k], bool):
            raise ValueError("cluster.%s must be true or false" % k)
    if not isinstance(c["count_roles"], list) or not c["count_roles"] or not set(c["count_roles"]) <= {"officer", "director"}:
        raise ValueError("cluster.count_roles must be a non-empty list of officer and director only (10 percent owner and Other never count)")
    if cfg["filing"]["transaction_codes_kept"] != ["P"]:
        raise ValueError("filing.transaction_codes_kept must be exactly [P] (open-market purchases only)")
    if not isinstance(c["max_filing_lag_business_days"], int) or c["max_filing_lag_business_days"] < 0:
        raise ValueError("cluster.max_filing_lag_business_days must be a non-negative integer")
    try:
        from zoneinfo import ZoneInfo
        ZoneInfo(cfg["timing"]["accepted_tz"])
        hh, mm = str(cfg["timing"]["premarket_entry_cutoff_et"]).split(":")
        if not (0 <= int(hh) and 0 <= int(mm) <= 59 and (int(hh), int(mm)) < (9, 30)):
            raise ValueError("cutoff must be before the 09:30 open")
    except Exception as e:
        raise ValueError("timing block invalid: %s" % type(e).__name__)
    iso = cfg["isolation"]
    if iso["writes_to_watcher"] is not False or iso["feeds_watcher_score"] is not False \
            or iso["adoption"] != "a_pass_is_a_request_to_zac_for_a_locked_rule_change_never_automatic":
        raise ValueError("isolation: writes_to_watcher and feeds_watcher_score must be false and adoption must stay a request to Zac (ruling 8)")
    kc = cfg["kill_criteria"]
    if not all(k in kc for k in ("K1", "K2", "K3", "K4", "K5", "K6", "K7")):
        raise ValueError("kill_criteria must hold K1 to K7")
    for dotted in ("K1.at_counted", "K2.at_qualifying", "K3.at_filled", "K4.months_after_first_counted_day", "K4.counted_under", "K7.resets_at_or_over", "K7.before_counted"):
        a, b = dotted.split(".")
        if not isinstance(kc[a][b], int) or kc[a][b] < 1:
            raise ValueError("kill_criteria.%s must be a positive integer" % dotted)
    if not (0 < kc["K2"]["unfilled_share_over"] < 1) or not _num(kc["K3"]["median_round_trip_cost_over"]) or kc["K3"]["median_round_trip_cost_over"] <= 0:
        raise ValueError("kill_criteria K2 share must be between 0 and 1 and K3 cost must be positive")
    try:
        import datetime as _dt
        _dt.datetime.fromisoformat(str(cfg["freeze"]["counted_signals_from_et"]))
    except ValueError:
        raise ValueError("freeze.counted_signals_from_et must be an ISO date-time like 2026-11-28T00:00:00")
    pt = cfg["primary_test"]
    if pt["ledger"] != "zac" or pt["population"] != "officer_and_director_clusters" or pt["metric"] != "mean_excess_net_of_cost" \
            or pt["benchmarks"] != "both_spy_and_iwm" or pt["cost"] != "larger_of_floor_and_measured_half_spread_each_side" \
            or pt["adoption"] != "a_pass_is_a_request_to_zac_never_automatic":
        raise ValueError("primary_test must keep the registered definition (zac ledger, officer and director clusters, mean excess net of cost, both benchmarks, adoption by request only)")
    if not isinstance(pt["horizon_trading_days"], int) or pt["horizon_trading_days"] not in f_horizons(cfg):
        raise ValueError("primary_test.horizon_trading_days must be exactly one of forward.horizons")
    fi = cfg["filing"]
    if not isinstance(fi["exclude_10b5_1"], bool):
        raise ValueError("filing.exclude_10b5_1 must be true or false")
    if not isinstance(fi["offering_min_owners"], int) or fi["offering_min_owners"] < 2:
        raise ValueError("filing.offering_min_owners must be an integer of 2 or more")
    if not isinstance(fi["offering_keywords"], list) or not all(isinstance(k, str) and k.strip() for k in fi["offering_keywords"]):
        raise ValueError("filing.offering_keywords must be a list of words")
    s = cfg["sec"]
    if not _num(s["max_requests_per_second"]) or s["max_requests_per_second"] <= 0:
        raise ValueError("sec.max_requests_per_second must be a positive number")
    for k in ("retries", "max_filings_per_run", "lookback_days", "max_response_bytes"):
        if not isinstance(s[k], int) or s[k] < 0:
            raise ValueError("sec.%s must be a non-negative integer" % k)
    f = cfg["forward"]
    if not isinstance(f["benchmarks"], list) or sorted(f["benchmarks"]) != ["IWM", "SPY"]:
        raise ValueError("forward.benchmarks must be exactly SPY and IWM (ruling 6: the primary pass needs both)")
    if f["feed"] != "iex":
        raise ValueError("forward.feed must be iex")
    if not isinstance(f["horizons"], list) or not f["horizons"] or not all(isinstance(h, int) and h >= 1 for h in f["horizons"]):
        raise ValueError("forward.horizons must be a list of positive integers")
    if not isinstance(f["haircut_bps"], list) or not f["haircut_bps"] or not all(_num(v) and v >= 0 for v in f["haircut_bps"]):
        raise ValueError("forward.haircut_bps must be a list of non-negative numbers")
    if f["pass_haircut_bps"] not in f["haircut_bps"]:
        raise ValueError("forward.pass_haircut_bps must be one of forward.haircut_bps")
    for k in ("min_listing_age_trading_days", "listing_history_calendar_days"):
        if not isinstance(f[k], int) or f[k] < 1:
            raise ValueError("forward.%s must be a positive integer" % k)
    if not _num(f["position_usd"]) or f["position_usd"] <= 0:
        raise ValueError("forward.position_usd must be a positive number")
    if not _num(f["cost_floor_bps"]) or f["cost_floor_bps"] < 30:
        raise ValueError("forward.cost_floor_bps must be a number of 30 or more (ruling 5: never below the stock ruling stress level)")
    if not isinstance(f["fill_window_minutes"], int) or f["fill_window_minutes"] < 1:
        raise ValueError("forward.fill_window_minutes must be a positive integer")
    if not isinstance(f["zac_extra_trading_days"], int) or f["zac_extra_trading_days"] < 0:
        raise ValueError("forward.zac_extra_trading_days must be a non-negative integer")
    return cfg


def flatten(cfg, prefix=""):
    out = {}
    for k, v in cfg.items():
        key = prefix + k
        if isinstance(v, dict):
            out.update(flatten(v, key + "."))
        else:
            out[key] = v
    return out


def changed_keys(old, new):
    a, b = flatten(old), flatten(new)
    return sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))


class ConfigChangeError(RuntimeError):
    pass


def record_config(cfg, history_path, today, reason=None, allow_multi=False):
    """Learning-loop hook. Appends a dated record to config-history.jsonl when the hash is new.
    A new hash resets this scanner's counts (outputs are counted per hash). ONE value may change per run:
    a change of several values is refused unless a written reason is given with allow_multi.
    Returns (hash, changed_keys_list, is_new)."""
    h = config_hash(cfg)
    last = None
    if os.path.exists(history_path):
        with open(history_path, "r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                try:
                    last = json.loads(line)
                except ValueError:
                    continue
    if last and last.get("config_hash") == h:
        return h, [], False
    keys = changed_keys(last["config"], cfg) if last and isinstance(last.get("config"), dict) else []
    if last and len(keys) > 1 and not (allow_multi and reason):
        raise ConfigChangeError("%d config values changed at once (%s). One change per run: revert all but one, "
                                "or rerun with --allow-multi-change and --reason \"why\"." % (len(keys), ", ".join(keys[:6])))
    rec = {"config_hash": h, "previous_hash": last.get("config_hash") if last else None, "date": today,
           "changed_keys": keys, "reason": reason, "counts_reset": True, "config": cfg}
    with open(history_path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, sort_keys=True, default=str) + "\n")
    return h, keys, True
