"""eBay Sell/Buy API client for the dropship venture.

Credentials come ONLY from environment variables (see .env.example):
  EBAY_ENV (sandbox|production, default sandbox), EBAY_CLIENT_ID, EBAY_CLIENT_SECRET, EBAY_REFRESH_TOKEN

Every module fails to SKIP with a logged reason; nothing here raises out of the CLI.
Every write accepts dry_run and logs to logs/api-YYYY-MM-DD.log with no tokens or buyer PII.

NOTE: endpoint paths and scopes below are written from knowledge of the eBay REST APIs and have
NOT been verified against live developer docs (doc pages were not machine-readable at build time).
Verify against developer.ebay.com before the first real call.

Usage:
  python ebay_api.py --check --dry-run       # smoke test every module
"""
import argparse
import base64
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
except ImportError:  # module isolation: missing dependency is a SKIP, not a crash
    requests = None

LOG_DIR = Path(__file__).resolve().parent.parent / "logs"
HOSTS = {"sandbox": "https://api.sandbox.ebay.com", "production": "https://api.ebay.com"}
SELL_SCOPES = ("https://api.ebay.com/oauth/api_scope/sell.inventory "
               "https://api.ebay.com/oauth/api_scope/sell.account "
               "https://api.ebay.com/oauth/api_scope/sell.fulfillment")
BROWSE_SCOPE = "https://api.ebay.com/oauth/api_scope"

OK, SKIP = "OK", "SKIP"
_SECRET_KEYS = {"authorization", "access_token", "refresh_token", "client_secret"}
_PII_KEYS = {"buyer", "shippingaddress", "shipto", "fullname", "email", "phone", "addressline1",
             "addressline2", "postalcode"}


def host():
    return HOSTS.get(os.environ.get("EBAY_ENV", "sandbox").lower(), HOSTS["sandbox"])


def _scrub(obj):
    if isinstance(obj, dict):
        return {k: ("[REDACTED]" if k.lower() in _SECRET_KEYS | _PII_KEYS else _scrub(v))
                for k, v in obj.items()}
    if isinstance(obj, list):
        return [_scrub(x) for x in obj]
    return obj


def log(event, **fields):
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        path = LOG_DIR / f"api-{datetime.now():%Y-%m-%d}.log"
        line = f"{datetime.now():%H:%M:%S} {event} {json.dumps(_scrub(fields), default=str)}\n"
        with open(path, "a", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        pass


def skip(module, reason):
    log("SKIP", module=module, reason=reason)
    return {"status": SKIP, "module": module, "reason": reason}


# ---------------------------------------------------------------- auth
def auth_token(scopes=SELL_SCOPES, grant="refresh"):
    """Return (token, None) or (None, skip_dict)."""
    if requests is None:
        return None, skip("auth", "requests not installed")
    cid, sec = os.environ.get("EBAY_CLIENT_ID"), os.environ.get("EBAY_CLIENT_SECRET")
    if not cid or not sec:
        return None, skip("auth", "EBAY_CLIENT_ID / EBAY_CLIENT_SECRET not set")
    basic = base64.b64encode(f"{cid}:{sec}".encode()).decode()
    if grant == "refresh":
        rt = os.environ.get("EBAY_REFRESH_TOKEN")
        if not rt:
            return None, skip("auth", "EBAY_REFRESH_TOKEN not set")
        data = {"grant_type": "refresh_token", "refresh_token": rt, "scope": scopes}
    else:
        data = {"grant_type": "client_credentials", "scope": scopes}
    try:
        r = requests.post(f"{host()}/identity/v1/oauth2/token", data=data, timeout=20,
                          headers={"Authorization": f"Basic {basic}",
                                   "Content-Type": "application/x-www-form-urlencoded"})
        if r.status_code != 200:
            return None, skip("auth", f"token endpoint returned HTTP {r.status_code}")
        log("auth", result="token obtained", grant=grant)
        return r.json()["access_token"], None
    except Exception as e:
        return None, skip("auth", f"{type(e).__name__}")


def _call(module, method, path, token, dry_run=False, write=False, **kw):
    if write and dry_run:
        log("DRY-RUN", module=module, method=method, path=path, body=kw.get("json"))
        return {"status": OK, "module": module, "dry_run": True, "would": f"{method} {path}"}
    try:
        r = requests.request(method, f"{host()}{path}", timeout=30,
                             headers={"Authorization": f"Bearer {token}",
                                      "Content-Type": "application/json",
                                      "Content-Language": "en-US"}, **kw)
        if write:
            log("WRITE", module=module, method=method, path=path, http=r.status_code)
        if r.status_code >= 400:
            return skip(module, f"HTTP {r.status_code} on {method} {path}")
        body = r.json() if r.content else {}
        return {"status": OK, "module": module, "data": body}
    except Exception as e:
        return skip(module, f"{type(e).__name__}")


def _need_token(module, scopes=SELL_SCOPES, grant="refresh"):
    token, err = auth_token(scopes, grant)
    if err:
        return None, skip(module, f"no token ({err['reason']})")
    return token, None


# ---------------------------------------------------------------- inventory
def inventory_create_item(sku, item, dry_run=False):
    """item: inventory item payload (product, availability, condition)."""
    if dry_run:
        return _call("inventory", "PUT", f"/sell/inventory/v1/inventory_item/{sku}", None,
                     dry_run=True, write=True, json=item)
    t, e = _need_token("inventory")
    return e or _call("inventory", "PUT", f"/sell/inventory/v1/inventory_item/{sku}", t,
                      write=True, json=item)


def inventory_create_offer(offer, dry_run=False):
    if dry_run:
        return _call("inventory", "POST", "/sell/inventory/v1/offer", None, dry_run=True,
                     write=True, json=offer)
    t, e = _need_token("inventory")
    return e or _call("inventory", "POST", "/sell/inventory/v1/offer", t, write=True, json=offer)


def inventory_publish_offer(offer_id, dry_run=False):
    """Only call with an approved queue ID (or after graduation, inside caps)."""
    path = f"/sell/inventory/v1/offer/{offer_id}/publish"
    if dry_run:
        return _call("inventory", "POST", path, None, dry_run=True, write=True)
    t, e = _need_token("inventory")
    return e or _call("inventory", "POST", path, t, write=True)


def inventory_withdraw_offer(offer_id, dry_run=False):
    path = f"/sell/inventory/v1/offer/{offer_id}/withdraw"
    if dry_run:
        return _call("inventory", "POST", path, None, dry_run=True, write=True)
    t, e = _need_token("inventory")
    return e or _call("inventory", "POST", path, t, write=True)


def inventory_update_price_quantity(requests_payload, dry_run=False):
    """Bulk update. Payload: {"requests": [{"sku":..., "shipToLocationAvailability": {"quantity": n},
    "offers": [{"offerId":..., "availableQuantity": n, "price": {"value": "x", "currency": "USD"}}]}]}"""
    path = "/sell/inventory/v1/bulk_update_price_quantity"
    if dry_run:
        return _call("inventory", "POST", path, None, dry_run=True, write=True,
                     json=requests_payload)
    t, e = _need_token("inventory")
    return e or _call("inventory", "POST", path, t, write=True, json=requests_payload)


def inventory_update_quantity(sku, offer_id, qty, dry_run=False):
    return inventory_update_price_quantity(
        {"requests": [{"sku": sku, "shipToLocationAvailability": {"quantity": qty},
                       "offers": [{"offerId": offer_id, "availableQuantity": qty}]}]}, dry_run)


def inventory_update_price(sku, offer_id, price, dry_run=False):
    return inventory_update_price_quantity(
        {"requests": [{"sku": sku, "offers": [{"offerId": offer_id,
                       "price": {"value": f"{price:.2f}", "currency": "USD"}}]}]}, dry_run)


# ---------------------------------------------------------------- orders
def orders_get(limit=50):
    t, e = _need_token("orders")
    if e:
        return e
    return _call("orders", "GET", f"/sell/fulfillment/v1/order?limit={limit}"
                 "&filter=orderfulfillmentstatus:%7BNOT_STARTED%7CIN_PROGRESS%7D", t)


def orders_upload_tracking(order_id, line_item_id, carrier, tracking, dry_run=False):
    path = f"/sell/fulfillment/v1/order/{order_id}/shipping_fulfillment"
    body = {"lineItems": [{"lineItemId": line_item_id, "quantity": 1}],
            "shippedDate": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "shippingCarrierCode": carrier, "trackingNumber": tracking}
    if dry_run:
        return _call("orders", "POST", path, None, dry_run=True, write=True, json=body)
    t, e = _need_token("orders")
    return e or _call("orders", "POST", path, t, write=True, json=body)


# ---------------------------------------------------------------- browse
def browse_search(query, limit=25):
    t, e = _need_token("browse", BROWSE_SCOPE, grant="client")
    if e:
        return e
    from urllib.parse import quote
    return _call("browse", "GET", f"/buy/browse/v1/item_summary/search?q={quote(query)}&limit={limit}", t)


# ---------------------------------------------------------------- CLI
def check(dry_run=True):
    results = [
        ("auth", lambda: (lambda tk: tk[1] or {"status": OK, "module": "auth"})(auth_token())),
        ("inventory", lambda: inventory_create_item("TEST-SKU", {"availability": {
            "shipToLocationAvailability": {"quantity": 1}}}, dry_run=True)),
        ("orders", lambda: orders_upload_tracking("TEST-ORDER", "TEST-LINE", "USPS", "9400TEST",
                                                   dry_run=True)),
        ("browse", lambda: browse_search("test")),
    ]
    out = []
    for name, fn in results:
        try:
            r = fn()
        except Exception as e:  # last-resort isolation
            r = skip(name, f"unexpected {type(e).__name__}")
        print(f"{name:10s} {r['status']:5s} {r.get('reason', r.get('would', ''))}")
        out.append(r)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if a.check:
        check(a.dry_run)
        sys.exit(0)
    ap.print_help()
