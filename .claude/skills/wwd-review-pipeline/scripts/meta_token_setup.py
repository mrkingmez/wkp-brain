#!/usr/bin/env python3
"""
meta_token_setup.py - one-time: turn a short-lived Graph API Explorer token into a long-lived
Page token for Winter Wolf's Den, find the linked Instagram account id, and save all three
as Windows USER environment variables. Prints no secret.

Before running, set these in PowerShell for THIS window only (not saved anywhere):
  $env:META_APP_ID="..."        (Meta app dashboard, Settings > Basic, App ID)
  $env:META_APP_SECRET="..."    (same page, App secret, click Show)
  $env:META_SHORT_TOKEN="..."   (Graph API Explorer, Generate Access Token, with the permissions
                                 pages_show_list, pages_manage_posts, pages_read_engagement,
                                 instagram_basic, instagram_content_publish, business_management)
Then:  python meta_token_setup.py

Result: META_PAGE_TOKEN, META_PAGE_ID, META_IG_USER_ID saved with setx (open a NEW terminal to use them).
Status: written 2026-10-15 from documented endpoints, not yet run against the live app.
"""
import os
import subprocess
import sys

import requests

G = "https://graph.facebook.com/v21.0"
PAGE_NAME = "Winter Wolf's Den"


def env(n):
    v = os.environ.get(n)
    if not v:
        sys.exit(f"Set {n} in this PowerShell window first (see the top of this file).")
    return v


def get(url, **p):
    r = requests.get(url, params=p, timeout=30)
    if not r.ok:
        sys.exit(f"Request failed: HTTP {r.status_code} {r.text[:400]}")
    return r.json()


app_id, secret, short = env("META_APP_ID"), env("META_APP_SECRET"), env("META_SHORT_TOKEN")
long_user = get(f"{G}/oauth/access_token", grant_type="fb_exchange_token", client_id=app_id,
                client_secret=secret, fb_exchange_token=short)["access_token"]
pages = get(f"{G}/me/accounts", access_token=long_user, fields="id,name,access_token", limit=100)["data"]
page = next((p for p in pages if p["name"] == PAGE_NAME), None)
if not page:
    sys.exit(f"Page '{PAGE_NAME}' not in the list. Pages seen: {[p['name'] for p in pages]}")
ig = get(f"{G}/{page['id']}", access_token=page["access_token"],
         fields="instagram_business_account")
ig_id = (ig.get("instagram_business_account") or {}).get("id")
if not ig_id:
    sys.exit("No Instagram account linked to the page. Link winterwolfsden to the page in Meta Business Suite settings.")
for k, v in (("META_PAGE_TOKEN", page["access_token"]), ("META_PAGE_ID", page["id"]), ("META_IG_USER_ID", ig_id)):
    subprocess.run(["setx", k, v], check=True, capture_output=True)
print(f"Saved for page {page['id']} and Instagram {ig_id}. Open a new terminal before posting.")
