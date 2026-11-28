"""Locked risk rules as small pure functions. All numbers come from cfg['rules'] and cfg['sizing']."""
import datetime as dt
import math

from .stats import bdays_between


def risk_pct_for(score, cfg):
    tiers = sorted(((float(k), float(v)) for k, v in cfg["rules"]["risk_per_trade_pct"].items()), reverse=True)
    for floor, pct in tiers:
        if score >= floor:
            return pct
    return 0.0


def loss_limit_hit(start_equity, equity, pct):
    """True when equity is down `pct` percent or more from start_equity. UNKNOWN inputs fail closed."""
    if start_equity is None or start_equity <= 0 or equity is None:
        return True  # UNKNOWN counts as FAIL
    loss_pct = round((start_equity - equity) / start_equity * 100.0, 9)
    return loss_pct >= float(pct)


def kill_switch_tripped(day_start_equity, equity, cfg):
    """True when the day's loss is at or beyond the kill switch percent."""
    return loss_limit_hit(day_start_equity, equity, cfg["rules"]["daily_kill_switch_pct"])


def weekly_limit_hit(week_start_equity, equity, cfg):
    return loss_limit_hit(week_start_equity, equity, cfg["sizing"]["max_loss_per_week_pct"])


def gate_reason(score, weekday_abbr, cfg):
    """Score-based block for a new trade, or None. Monday only at hot_score or higher."""
    R = cfg["rules"]
    if score is None:
        return "UNKNOWN score"
    if score < R["min_score_to_trade"]:
        return "score %.1f under %s, no trade" % (score, R["min_score_to_trade"])
    if weekday_abbr in R["watch_days"] and score < R["hot_score"]:
        return "watch day (%s): needs score %s or higher, got %.1f" % (weekday_abbr, R["hot_score"], score)
    return None


def size_shares(equity, cash, entry_price, atr_value, score, cfg, risk_pct=None, fractional=False):
    """Whole shares (or fractional for the small-account view). Returns (shares, details).
    25 percent position cap, cash and the hard max loss per trade all bind. risk_pct overrides the tier (step-up)."""
    R = cfg["rules"]
    pct = risk_pct_for(score, cfg) if risk_pct is None else float(risk_pct)
    pct = min(pct, float(cfg["sizing"]["max_loss_per_trade_pct"]))
    risk_usd = equity * pct / 100.0
    risk_per_share = R["atr_stop_multiple"] * atr_value
    if pct <= 0 or risk_per_share <= 0 or entry_price <= 0 or equity <= 0:
        return 0, {"why": "no size (risk pct, atr, price or equity unusable)", "risk_pct": pct}
    by_risk = risk_usd / risk_per_share
    by_cap = equity * R["max_position_pct"] / 100.0 / entry_price
    by_cash = max(cash, 0.0) / entry_price
    raw = min(by_risk, by_cap, by_cash)
    shares = raw if fractional else int(math.floor(raw))
    binding = min((by_risk, "risk"), (by_cap, "position cap"), (by_cash, "cash"))[1]
    return shares, {"risk_pct": pct, "risk_usd": round(risk_usd, 2), "risk_per_share": round(risk_per_share, 4),
                    "by_risk": round(by_risk, 4), "by_cap": round(by_cap, 4), "by_cash": round(by_cash, 4),
                    "binding": binding}


def step_up_check(cfg, score, regime_tag, open_positions, nets_at_expectancy_bps, last_kill_date, today):
    """Capped step-up of the risk percent. OFF unless sizing.step_up.enabled is true.
    Returns (risk_pct or None, list of reasons). All conditions must hold, UNKNOWN regime is FAIL.
    nets_at_expectancy_bps: net P and L of closed Zac-ledger trades under the current config, at the configured haircut."""
    su = cfg["sizing"]["step_up"]
    if not su["enabled"]:
        return None, ["step-up is OFF in config"]
    why = []
    if score is None or score < su["min_score"]:
        why.append("score under %s" % su["min_score"])
    if regime_tag != su["regime"]:
        why.append("regime %s is not %s" % (regime_tag, su["regime"]))
    n = len(nets_at_expectancy_bps)
    if n < su["min_counted_trades"]:
        why.append("only %d counted Zac-ledger trades, need %d" % (n, su["min_counted_trades"]))
    elif sum(nets_at_expectancy_bps) / n <= 0:
        why.append("Zac-ledger expectancy at %s bps is not positive" % su["expectancy_haircut_bps"])
    if last_kill_date:
        kd = dt.date.fromisoformat(last_kill_date)
        if bdays_between(kd, today) < su["no_kill_trading_days"]:
            why.append("kill switch within the last %d trading days" % su["no_kill_trading_days"])
    if open_positions >= su["max_open_positions_below"]:
        why.append("%d open positions, need fewer than %d" % (open_positions, su["max_open_positions_below"]))
    if why:
        return None, why
    return float(su["risk_pct"]), ["step-up conditions all met"]


def pdt_block(day_trade_dates, today, cfg, open_entry_dates=()):
    """Conservative pattern day trader guard. day_trade_dates: ISO ET dates of past same-day round trips.
    open_entry_dates: ISO ET dates of entries still open. An entry opened on `today` could be exited the same session,
    so it counts as a potential day trade against both limits (change 4, S4 fix: the ledger can never exceed the limit).
    Returns a reason string if a new entry should be refused, else None. Rule text NOT confirmed (see plan)."""
    P = cfg["pdt"]
    if not P["enforce"]:
        return None
    ds = [dt.date.fromisoformat(x) for x in day_trade_dates]
    ds += [dt.date.fromisoformat(x) for x in open_entry_dates if dt.date.fromisoformat(x) == today]
    rolling = sum(1 for d in ds if d <= today and bdays_between(d, today) < P["window_trading_days"])
    if rolling >= P["max_day_trades_rolling"]:
        return "PDT guard: %d day trades in the last %d trading days (limit %d)" % (rolling, P["window_trading_days"], P["max_day_trades_rolling"])
    month = sum(1 for d in ds if (d.year, d.month) == (today.year, today.month))
    if month >= P["max_day_trades_per_month"]:
        return "PDT guard: %d day trades this calendar month (limit %d)" % (month, P["max_day_trades_per_month"])
    return None
