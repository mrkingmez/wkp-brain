"""Pricing for the eBay dropship venture. Pure function plus CLI.

price = ((cost + ship) * (1 + tax_buffer) + fixed_fee + target_profit) / (1 - fvf - promo)

Margin floor (locked, CLAUDE.md rule 7): net margin >= 20 percent AND net profit >= 5 dollars.
Fee rates come from data/fee-table.md. Refuses to run if that file is older than 35 days.
Simplification: fvf is applied to the item price only (free shipping built into price).

Usage:
  python pricing.py --cost 12 --ship 4 --category "Home & Garden" --target-profit 6
  python pricing.py --test
"""
import argparse
import math
import re
import sys
from datetime import date, datetime
from pathlib import Path

FEE_TABLE = Path(__file__).resolve().parent.parent / "data" / "fee-table.md"
MARGIN_FLOOR = 0.20
MIN_PROFIT = 5.00
TAX_BUFFER = 0.10  # drop to 0 once Zac has a resale certificate
MAX_FEE_AGE_DAYS = 35


class PricingError(Exception):
    pass


def load_fees(category, path=FEE_TABLE, today=None):
    """Return (fvf_rate, fixed_fee) for category. Raises PricingError if stale or missing."""
    today = today or date.today()
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError as e:
        raise PricingError(f"fee table unreadable: {e}")
    m = re.search(r"Last checked:\s*(\d{4}-\d{2}-\d{2})", text)
    if not m:
        raise PricingError("fee table has no 'Last checked: YYYY-MM-DD' date; populate it first")
    age = (today - datetime.strptime(m.group(1), "%Y-%m-%d").date()).days
    if age > MAX_FEE_AGE_DAYS:
        raise PricingError(f"fee table is {age} days old (max {MAX_FEE_AGE_DAYS}); refresh it")
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 3 and cells[0].lower() == category.lower():
            try:
                return float(cells[1]), float(cells[2])
            except ValueError:
                raise PricingError(f"bad numbers for category {category!r}")
    raise PricingError(f"category {category!r} not in fee table")


def compute(cost, ship, fvf, fixed, target_profit=MIN_PROFIT, tax_buffer=TAX_BUFFER, promo=0.0):
    """Return dict(price, net_profit, net_margin, result)."""
    if fvf + promo >= 1 - MARGIN_FLOOR:
        raise PricingError("fee rates leave no room for the margin floor")
    landed = (cost + ship) * (1 + tax_buffer)
    target_profit = max(target_profit, MIN_PROFIT)
    by_target = (landed + fixed + target_profit) / (1 - fvf - promo)
    by_margin = (landed + fixed) / (1 - fvf - promo - MARGIN_FLOOR)
    raw = max(by_target, by_margin)
    price = math.floor(raw) + 0.99
    if price < raw:
        price += 1
    # recheck after rounding; bump a dollar at a time if a rounding edge case dips under the floor
    for _ in range(5):
        net = price * (1 - fvf - promo) - fixed - landed
        margin = net / price
        if net >= MIN_PROFIT - 1e-9 and margin >= MARGIN_FLOOR - 1e-9:
            break
        price += 1
    net = price * (1 - fvf - promo) - fixed - landed
    margin = net / price
    ok = net >= MIN_PROFIT - 1e-9 and margin >= MARGIN_FLOOR - 1e-9
    return {"price": round(price, 2), "net_profit": round(net, 2),
            "net_margin": round(margin, 4), "result": "PASS" if ok else "FAIL"}


def _tests():
    cases = [
        # cost, ship, fvf, fixed, target
        (10, 4, 0.1325, 0.30, 5),
        (25, 6, 0.1325, 0.30, 8),
        (3, 2, 0.15, 0.30, 5),
        (60, 10, 0.12, 0.40, 10),
        (8, 0, 0.1325, 0.30, 5),
    ]
    for c in cases:
        r = compute(*c)
        assert r["result"] == "PASS", (c, r)
        assert r["net_profit"] >= 5 and r["net_margin"] >= 0.20, (c, r)
        assert str(r["price"]).endswith((".99",)), (c, r)
    # known value: landed 15.40; margin floor binds (net 5.11 at 23.99, 21.3 percent)
    r = compute(10, 4, 0.1325, 0.30, 5)
    assert r["price"] == 23.99, r
    # buffer matters: zero buffer must be cheaper
    assert compute(10, 4, 0.1325, 0.30, 5, tax_buffer=0)["price"] < compute(10, 4, 0.1325, 0.30, 5)["price"]
    # promo raises price
    assert compute(10, 4, 0.1325, 0.30, 5, promo=0.05)["price"] > compute(10, 4, 0.1325, 0.30, 5)["price"]
    # impossible fees rejected
    try:
        compute(10, 4, 0.9, 0.3)
        raise AssertionError("expected PricingError")
    except PricingError:
        pass
    # stale fee table refused
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "f.md"
        p.write_text("Last checked: 2020-01-01\n| a | 0.1 | 0.3 |\n", encoding="utf-8")
        try:
            load_fees("a", p)
            raise AssertionError("expected stale error")
        except PricingError:
            pass
        p.write_text(f"Last checked: {date.today()}\n| a | 0.1 | 0.3 |\n", encoding="utf-8")
        assert load_fees("a", p) == (0.1, 0.3)
    print("pricing tests: 9 checks PASS")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--test", action="store_true")
    ap.add_argument("--cost", type=float)
    ap.add_argument("--ship", type=float, default=0.0)
    ap.add_argument("--category")
    ap.add_argument("--target-profit", type=float, default=MIN_PROFIT)
    ap.add_argument("--tax-buffer", type=float, default=TAX_BUFFER)
    ap.add_argument("--promo-rate", type=float, default=0.0)
    a = ap.parse_args()
    if a.test:
        _tests()
        return 0
    if a.cost is None or not a.category:
        ap.error("--cost and --category required")
    try:
        fvf, fixed = load_fees(a.category)
        r = compute(a.cost, a.ship, fvf, fixed, a.target_profit, a.tax_buffer, a.promo_rate)
    except PricingError as e:
        print(f"REFUSED: {e}")
        return 2
    for k, v in r.items():
        print(f"{k}: {v}")
    return 0 if r["result"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
