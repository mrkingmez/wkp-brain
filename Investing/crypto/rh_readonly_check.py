"""Robinhood Crypto API READ-ONLY check. GET requests only, never places or cancels an order.
Keys are read from user env vars RH_CRYPTO_API_KEY and RH_CRYPTO_PRIVATE_KEY (base64 Ed25519 seed). Never printed.
Auth per docs.robinhood.com/crypto/trading: message = api_key + timestamp + path + method + body,
Ed25519 signature base64, headers x-api-key, x-signature, x-timestamp (timestamp valid 30 s)."""
import base64, json, os, subprocess, sys, time, urllib.request, urllib.error
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

def user_env(name):
    v = os.environ.get(name)
    if v: return v
    out = subprocess.run(["powershell","-NoProfile","-Command",f"[Environment]::GetEnvironmentVariable('{name}','User')"],capture_output=True,text=True).stdout.strip()
    return out

API_KEY = user_env("RH_CRYPTO_API_KEY"); PRIV = user_env("RH_CRYPTO_PRIVATE_KEY")
if not API_KEY or not PRIV:
    print(f"MISSING: apiKeyLen={len(API_KEY)} privKeyLen={len(PRIV)}"); sys.exit(2)
sk = Ed25519PrivateKey.from_private_bytes(base64.b64decode(PRIV))
BASE = "https://trading.robinhood.com"

def get(path):
    ts = str(int(time.time()))
    msg = f"{API_KEY}{ts}{path}GET".encode()
    sig = base64.b64encode(sk.sign(msg)).decode()
    req = urllib.request.Request(BASE+path, headers={"x-api-key":API_KEY,"x-signature":sig,"x-timestamp":ts,"Content-Type":"application/json; charset=utf-8"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, (e.read().decode()[:300])

s, acct = get("/api/v1/crypto/trading/accounts/")
print("account status:", s, (acct.get("status") if isinstance(acct, dict) else acct))
s2, bba = get("/api/v1/crypto/marketdata/best_bid_ask/?symbol=BTC-USD")
print("best_bid_ask BTC-USD:", s2, (bba if not isinstance(bba, dict) else bba.get("results")))
