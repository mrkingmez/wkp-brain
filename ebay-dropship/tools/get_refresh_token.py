"""Swap an eBay authorization code for a refresh token and save it as a user
environment variable. Nothing secret is printed. Run it yourself in a terminal.
Reads EBAY_ENV, EBAY_CLIENT_ID, EBAY_CLIENT_SECRET from the environment."""
import base64, getpass, json, os, sys, urllib.parse, urllib.request, urllib.error

env = os.environ.get("EBAY_ENV", "PRODUCTION").upper()
cid, sec = os.environ.get("EBAY_CLIENT_ID"), os.environ.get("EBAY_CLIENT_SECRET")
if not cid or not sec:
    sys.exit("EBAY_CLIENT_ID or EBAY_CLIENT_SECRET is not set.")
host = "api.sandbox.ebay.com" if env.startswith("SAND") else "api.ebay.com"
print("Environment:", "SANDBOX" if "sandbox" in host else "PRODUCTION")

runame = input("Paste your RuName (the long name like Zachary_Ki-WKPComm-...): ").strip()
raw = getpass.getpass("Paste the full address you landed on (hidden, press Enter): ").strip()
q = urllib.parse.urlparse(raw).query or raw
code = urllib.parse.parse_qs(q).get("code", [raw])[0]  # parse_qs already URL-decodes

body = urllib.parse.urlencode({"grant_type": "authorization_code", "code": code, "redirect_uri": runame}).encode()
auth = base64.b64encode(f"{cid}:{sec}".encode()).decode()
req = urllib.request.Request(f"https://{host}/identity/v1/oauth2/token", data=body, headers={
    "Content-Type": "application/x-www-form-urlencoded", "Authorization": f"Basic {auth}"})
try:
    data = json.load(urllib.request.urlopen(req, timeout=30))
except urllib.error.HTTPError as e:
    err = json.loads(e.read().decode() or "{}")
    sys.exit(f"eBay said no (HTTP {e.code}): {err.get('error')} - {err.get('error_description')}")

rt = data.get("refresh_token")
if not rt:
    sys.exit("No refresh token came back.")

import winreg
with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_SET_VALUE) as k:
    winreg.SetValueEx(k, "EBAY_REFRESH_TOKEN", 0, winreg.REG_SZ, rt)
print("Saved EBAY_REFRESH_TOKEN. Expires in about", data.get("refresh_token_expires_in", 0) // 86400, "days.")
print("Open a new terminal for it to show up. Token was not printed.")
