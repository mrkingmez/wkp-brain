import datetime as _dt
import hashlib
import json
import math

import yaml

REQUIRED = [
    "feed", "timeframe", "scan_interval_seconds", "bars_lookback_days", "symbols", "market_gauge",
    "paper_book.starting_equity", "paper_book.haircut_bps_each_side", "paper_book.fee_bps_each_side",
    "paper_book.sell_reg_fee_bps", "paper_book.max_gap_atr",
    "rules.min_score_to_trade", "rules.risk_per_trade_pct", "rules.max_position_pct",
    "rules.atr_stop_multiple", "rules.atr_period", "rules.reward_multiple", "rules.time_stop_sessions",
    "rules.daily_kill_switch_pct", "rules.watch_days", "rules.hot_score", "rules.max_open_positions",
    "filters.min_bars", "filters.min_price", "filters.min_avg_dollar_volume_1h", "filters.max_stale_days",
    "scoring.base", "scoring.pullback", "scoring.mean_reversion", "scoring.breakout",
    "session_bars.regular_hours_only", "session_bars.first_bar_start_hour_et", "session_bars.last_bar_start_hour_et",
    "counting.min_score", "fills.session_open_fill_hour_et",
    "zac_ledger.enabled", "zac_ledger.max_pending_sessions",
    "scorecard.haircut_views_bps", "scorecard.pass_haircut_bps", "scorecard.sizing_view_equity",
    "end_rule.last_day", "end_rule.close_open_at_last_close",
    "pdt.enforce", "pdt.max_day_trades_rolling", "pdt.window_trading_days", "pdt.max_day_trades_per_month",
    "regime.daily_lookback_days", "regime.sma_fast", "regime.sma_slow", "regime.slope_days", "regime.atr_period",
    "regime.vol_median_days", "regime.vol_ratio_volatile", "regime.breadth_min_up", "regime.min_breadth_symbols",
    "sizing.max_loss_per_trade_pct", "sizing.max_loss_per_week_pct",
    "sizing.step_up.enabled", "sizing.step_up.risk_pct", "sizing.step_up.min_score", "sizing.step_up.regime",
    "sizing.step_up.min_counted_trades", "sizing.step_up.expectancy_haircut_bps",
    "sizing.step_up.no_kill_trading_days", "sizing.step_up.max_open_positions_below",
]


def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    validate(cfg)
    return cfg


def config_hash(cfg):
    """Short fingerprint of the PARSED config (comments and spacing do not change it, any value does).
    It goes on every log line. A different hash means a different experiment: counts restart."""
    blob = json.dumps(cfg, sort_keys=True, default=str, separators=(",", ":"))
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def _num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v)


def validate(cfg):
    for dotted in REQUIRED:
        cur = cfg
        for part in dotted.split("."):
            if not isinstance(cur, dict) or part not in cur or cur[part] is None:
                raise ValueError("config missing required key: " + dotted)
            cur = cur[part]
    ld = cfg["end_rule"]["last_day"]
    try:
        if not isinstance(ld, str) or _dt.date.fromisoformat(ld).isoformat() != ld:
            raise ValueError
    except ValueError:
        raise ValueError('end_rule.last_day must be a quoted date written YYYY-MM-DD')
    r = cfg["rules"]
    for k in ("min_score_to_trade", "max_position_pct", "atr_stop_multiple", "reward_multiple", "daily_kill_switch_pct", "hot_score"):
        if not _num(r[k]) or r[k] <= 0:
            raise ValueError("rules.%s must be a positive number" % k)
    if not isinstance(r["max_open_positions"], int) or r["max_open_positions"] < 1 or r["max_position_pct"] > 100:
        raise ValueError("bad max_open_positions or max_position_pct")
    for k in ("starting_equity", "haircut_bps_each_side", "fee_bps_each_side", "sell_reg_fee_bps"):
        if not _num(cfg["paper_book"][k]) or cfg["paper_book"][k] < 0:
            raise ValueError("paper_book.%s must be a finite non-negative number" % k)
    if cfg["paper_book"]["starting_equity"] <= 0:
        raise ValueError("paper_book.starting_equity must be positive")
    if cfg["feed"] != "iex":
        raise ValueError("feed must be iex (SIP is denied on this account)")
    if cfg["market_gauge"] not in cfg["symbols"]:
        raise ValueError("market_gauge must be in symbols")
    if not _num(cfg["counting"]["min_score"]) or cfg["counting"]["min_score"] < r["min_score_to_trade"]:
        raise ValueError("counting.min_score must be a number at or above rules.min_score_to_trade")
    sbars = cfg["session_bars"]
    if not isinstance(sbars["regular_hours_only"], bool) or not all(isinstance(sbars[k], int) and 0 <= sbars[k] <= 23 for k in ("first_bar_start_hour_et", "last_bar_start_hour_et"))             or sbars["first_bar_start_hour_et"] > sbars["last_bar_start_hour_et"]:
        raise ValueError("bad session_bars settings")
    fh = cfg["fills"]["session_open_fill_hour_et"]
    if not isinstance(fh, int) or isinstance(fh, bool) or not sbars["first_bar_start_hour_et"] <= fh <= sbars["last_bar_start_hour_et"]:
        raise ValueError("fills.session_open_fill_hour_et must be a whole hour inside the session bar hours")
    gap = cfg["zac_ledger"].get("max_gap_atr")
    if gap is not None and (not _num(gap) or gap <= 0):
        raise ValueError("zac_ledger.max_gap_atr must be null or a positive number")
    mps = cfg["zac_ledger"]["max_pending_sessions"]
    if not isinstance(mps, int) or isinstance(mps, bool) or mps < 1:
        raise ValueError("zac_ledger.max_pending_sessions must be a whole number of 1 or more")
    views = cfg["scorecard"]["haircut_views_bps"]
    if not isinstance(views, list) or not views or not all(_num(v) and v >= 0 for v in views):
        raise ValueError("scorecard.haircut_views_bps must be a non-empty list of non-negative numbers")
    if cfg["scorecard"]["pass_haircut_bps"] not in views:
        raise ValueError("scorecard.pass_haircut_bps must be one of the haircut views")
    su = cfg["sizing"]["step_up"]
    if su["expectancy_haircut_bps"] not in views:
        raise ValueError("sizing.step_up.expectancy_haircut_bps must be one of the haircut views")
    if not isinstance(su["enabled"], bool):
        raise ValueError("sizing.step_up.enabled must be true or false")
    for k in ("max_loss_per_trade_pct", "max_loss_per_week_pct"):
        if not _num(cfg["sizing"][k]) or cfg["sizing"][k] <= 0:
            raise ValueError("sizing.%s must be a positive number" % k)
    if not _num(su["risk_pct"]) or not isinstance(su["min_counted_trades"], int) or su["min_counted_trades"] < 1 or su["regime"] not in ("UPTREND_CALM", "UPTREND_VOLATILE", "RANGE", "DOWNTREND_CALM", "DOWNTREND_VOLATILE") or not _num(su["min_score"]) or su["min_score"] < cfg["rules"]["min_score_to_trade"]:
        raise ValueError("bad sizing.step_up settings")
    if su["risk_pct"] > cfg["sizing"]["max_loss_per_trade_pct"]:
        raise ValueError("sizing.step_up.risk_pct is above the hard max loss per trade")
    if not _num(cfg["scorecard"]["sizing_view_equity"]) or cfg["scorecard"]["sizing_view_equity"] <= 0:
        raise ValueError("scorecard.sizing_view_equity must be positive")
    return cfg
