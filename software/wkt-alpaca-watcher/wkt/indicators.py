"""Pure-python indicators on a list of bars (dicts with o, h, l, c, v). No pandas needed.
Each function returns a list the same length as the input. None means UNKNOWN (not enough data)."""
import math


def finite(x):
    return x is not None and isinstance(x, (int, float)) and math.isfinite(x)


def ema(vals, n):
    a = 2.0 / (n + 1)
    out, prev = [], None
    for v in vals:
        prev = v if prev is None else a * v + (1 - a) * prev
        out.append(prev)
    return out


def _wilder(vals, n):
    a = 1.0 / n
    out, prev = [], None
    for v in vals:
        if v is None:
            out.append(None)
            continue
        prev = v if prev is None else a * v + (1 - a) * prev
        out.append(prev)
    return out


def rsi(close, n=14):
    d = [None] + [close[i] - close[i - 1] for i in range(1, len(close))]
    up = _wilder([None if x is None else max(x, 0.0) for x in d], n)
    dn = _wilder([None if x is None else max(-x, 0.0) for x in d], n)
    out = []
    for u, w in zip(up, dn):
        if u is None:
            out.append(None)
        elif w == 0:
            out.append(100.0 if u > 0 else 50.0)
        else:
            out.append(100 - 100 / (1 + u / w))
    return out


def true_range(bars):
    tr = []
    for i, b in enumerate(bars):
        if i == 0:
            tr.append(b["h"] - b["l"])
        else:
            pc = bars[i - 1]["c"]
            tr.append(max(b["h"] - b["l"], abs(b["h"] - pc), abs(b["l"] - pc)))
    return tr


def atr(bars, n=14):
    return _wilder(true_range(bars), n)


def rolling(vals, n, fn):
    return [fn(vals[i - n + 1:i + 1]) if i >= n - 1 else None for i in range(len(vals))]


def _std(xs):
    m = sum(xs) / len(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def bollinger(close, n=20, k=2.0):
    mid = rolling(close, n, lambda x: sum(x) / len(x))
    sd = rolling(close, n, _std)
    lo = [None if m is None else m - k * s for m, s in zip(mid, sd)]
    return lo


def macd_hist(close, f=12, s=26, sig=9):
    line = [a - b for a, b in zip(ema(close, f), ema(close, s))]
    signal = ema(line, sig)
    return [a - b for a, b in zip(line, signal)]


def stochastic(bars, n=14, d=3):
    lo = rolling([b["l"] for b in bars], n, min)
    hi = rolling([b["h"] for b in bars], n, max)
    k = []
    for b, l, h in zip(bars, lo, hi):
        if l is None:
            k.append(None)
        elif h == l:
            k.append(50.0)
        else:
            k.append(100.0 * (b["c"] - l) / (h - l))
    dd = [None if i < n - 1 + d - 1 else sum(k[i - d + 1:i + 1]) / d for i in range(len(k))]
    return k, dd


def adx(bars, n=14):
    pdm, mdm = [0.0], [0.0]
    for i in range(1, len(bars)):
        up = bars[i]["h"] - bars[i - 1]["h"]
        dn = -(bars[i]["l"] - bars[i - 1]["l"])
        pdm.append(up if (up > dn and up > 0) else 0.0)
        mdm.append(dn if (dn > up and dn > 0) else 0.0)
    a = atr(bars, n)
    ps, ms = _wilder(pdm, n), _wilder(mdm, n)
    dx = []
    for x, y, z in zip(ps, ms, a):
        if not z:
            dx.append(0.0)
            continue
        pdi, mdi = 100 * x / z, 100 * y / z
        dx.append(0.0 if pdi + mdi == 0 else 100 * abs(pdi - mdi) / (pdi + mdi))
    return _wilder(dx, n)


def enrich(bars, atr_period=14):
    """Series needed by scoring. All lists aligned to bars."""
    close = [b["c"] for b in bars]
    vol = [b["v"] for b in bars]
    k, d = stochastic(bars)
    vavg = rolling(vol, 20, lambda x: sum(x) / len(x))
    hi = [b["h"] for b in bars]
    hi20 = [None] + [max(hi[i - 20:i]) if i >= 20 else None for i in range(1, len(bars))]
    return {
        "ema20": ema(close, 20), "ema50": ema(close, 50), "rsi": rsi(close), "atr": atr(bars, atr_period),
        "bb_lo": bollinger(close), "macd_hist": macd_hist(close), "stoch_k": k, "stoch_d": d,
        "adx": adx(bars), "vol_ratio": [None if (a is None or a == 0) else v / a for v, a in zip(vol, vavg)],
        "hi20": hi20,
    }
