"""Small shared math so the engine and the scorecard compute a trade the same way."""


def net_at(entry_raw, exit_raw, shares, bps, fee_bps, sell_reg_bps):
    """Net P and L of one round trip if slippage were `bps` each side. Same formula the engine uses at close."""
    fe = entry_raw * (1 + bps / 1e4)
    fx = exit_raw * (1 - bps / 1e4)
    fee_open = shares * fe * fee_bps / 1e4
    fee_close = shares * fx * (fee_bps + sell_reg_bps) / 1e4
    return (fx - fe) * shares - fee_open - fee_close


def bdays_between(a, b):
    """Weekdays in [a, b). Holidays are not modeled."""
    import datetime as dt
    n, d = 0, a
    while d < b:
        if d.weekday() < 5:
            n += 1
        d += dt.timedelta(days=1)
    return n
