#!/usr/bin/env python3
"""
post_short.py - post or schedule one short from a LOCAL file to Facebook, Instagram or YouTube.

Runs on Zac's PC so the file never has to be on a public link. Written 2026-10-15 after the
Composio/OpusClip/VidIQ connectors proved unable to read L:\\ (see
WWD\\reports\\Social-Posting-Connector-Report.md).

STATUS: written from the platforms' documented APIs, NOT yet tested against live accounts.
Run with --dry-run first. Test with one clip before trusting it for the week.

Credentials come from Windows environment variables only. Never put a token in a file or chat.
  META_PAGE_TOKEN       long-lived Page access token for Winter Wolf's Den
  META_PAGE_ID          104052046075172 (Winter Wolf's Den page)
  META_IG_USER_ID       Instagram business/creator account id linked to that page
  YT_CLIENT_SECRETS     path to the Google OAuth client_secret .json (Desktop app type)
  YT_TOKEN_FILE         path where the YouTube sign-in token is cached (default D:\\WKP\\scratch\\yt_token.json)

Usage examples:
  python post_short.py --platform fb --clip C:\\x\\clip1.mp4 --caption "text" --when 2026-10-15T12:30-04:00
  python post_short.py --platform ig --clip C:\\x\\clip1.mp4 --caption "text"            (publishes now)
  python post_short.py --platform yt --clip C:\\x\\clip1.mp4 --title "t" --caption "desc" --when 2026-10-15T11:00-04:00
  add --dry-run to print what would happen and send nothing.

Notes:
  * Facebook Reel and YouTube support a scheduled time. Instagram's API does not: --when on ig
    makes this script WAIT until that time and then publish (PC must stay on), or use Windows
    Task Scheduler to launch it at the time with no --when.
  * Times must include a UTC offset (EDT is -04:00 until Nov 1 2026, then EST is -05:00).
"""
import argparse
import datetime as dt
import os
import sys
import time

import requests

GRAPH = "https://graph.facebook.com/v21.0"
RUPLOAD = "https://rupload.facebook.com/video-upload/v21.0"


def need(name):
    v = os.environ.get(name)
    if not v:
        sys.exit(f"Missing environment variable {name}. See the setup steps in the connector report.")
    return v


def parse_when(s):
    if not s:
        return None
    t = dt.datetime.fromisoformat(s)
    if t.tzinfo is None:
        sys.exit("--when needs a UTC offset, for example 2026-10-15T12:30-04:00")
    return t


def check(r, what):
    if not r.ok:
        sys.exit(f"{what} failed: HTTP {r.status_code} {r.text[:600]}")
    return r.json()


# ---------------------------------------------------------------- Facebook Reel
def post_facebook(clip, caption, title, when, dry):
    page_id, token = need("META_PAGE_ID"), need("META_PAGE_TOKEN")
    size = os.path.getsize(clip)
    if when:
        epoch = int(when.timestamp())
        if epoch < time.time() + 600:
            sys.exit("Facebook needs the scheduled time at least 10 minutes in the future.")
    print(f"[FB] Winter Wolf's Den page {page_id}: {os.path.basename(clip)} ({size} bytes), "
          f"{'schedule ' + when.isoformat() if when else 'publish now'}")
    if dry:
        return
    start = check(requests.post(f"{GRAPH}/{page_id}/video_reels",
                                data={"upload_phase": "start", "access_token": token}), "FB start")
    video_id = start["video_id"]
    with open(clip, "rb") as f:
        up = requests.post(f"{RUPLOAD}/{video_id}", data=f, headers={
            "Authorization": f"OAuth {token}", "offset": "0", "file_size": str(size)})
    check(up, "FB upload")
    fin = {"upload_phase": "finish", "video_id": video_id, "access_token": token,
           "description": caption, "title": title or ""}
    if when:
        fin["video_state"] = "SCHEDULED"
        fin["scheduled_publish_time"] = int(when.timestamp())
    else:
        fin["video_state"] = "PUBLISHED"
    print("[FB] done:", check(requests.post(f"{GRAPH}/{page_id}/video_reels", data=fin), "FB finish"))


# ---------------------------------------------------------------- Instagram Reel
def post_instagram(clip, caption, when, dry):
    ig_id, token = need("META_IG_USER_ID"), need("META_PAGE_TOKEN")
    size = os.path.getsize(clip)
    print(f"[IG] account {ig_id}: {os.path.basename(clip)} ({size} bytes), "
          f"{'wait until ' + when.isoformat() + ' then publish' if when else 'publish now'}")
    if dry:
        return
    cont = check(requests.post(f"{GRAPH}/{ig_id}/media", data={
        "media_type": "REELS", "upload_type": "resumable", "caption": caption,
        "share_to_feed": "true", "access_token": token}), "IG container")
    cid, uri = cont["id"], cont["uri"]
    with open(clip, "rb") as f:
        up = requests.post(uri, data=f, headers={
            "Authorization": f"OAuth {token}", "offset": "0", "file_size": str(size)})
    check(up, "IG upload")
    for _ in range(60):  # wait for Instagram to finish processing (up to ~5 min)
        st = check(requests.get(f"{GRAPH}/{cid}", params={
            "fields": "status_code", "access_token": token}), "IG status")
        if st.get("status_code") == "FINISHED":
            break
        if st.get("status_code") == "ERROR":
            sys.exit(f"IG processing error: {st}")
        time.sleep(5)
    else:
        sys.exit("IG processing did not finish in 5 minutes.")
    if when:
        wait = (when - dt.datetime.now(dt.timezone.utc)).total_seconds()
        if wait > 0:
            print(f"[IG] uploaded and processed, waiting {int(wait)}s until {when.isoformat()}")
            time.sleep(wait)
    pub = check(requests.post(f"{GRAPH}/{ig_id}/media_publish", data={
        "creation_id": cid, "access_token": token}), "IG publish")
    print("[IG] done:", pub)


# ---------------------------------------------------------------- YouTube Short
def post_youtube(clip, title, caption, when, dry):
    print(f"[YT] {os.path.basename(clip)}: '{title}', "
          f"{'schedule ' + when.isoformat() if when else 'publish now (public)'}")
    if dry:
        return
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload

    scopes = ["https://www.googleapis.com/auth/youtube.upload"]
    token_file = os.environ.get("YT_TOKEN_FILE", r"D:\WKP\scratch\yt_token.json")
    creds = None
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(need("YT_CLIENT_SECRETS"), scopes)
            creds = flow.run_local_server(port=0)  # opens a browser: sign in as the channel owner
        with open(token_file, "w") as f:
            f.write(creds.to_json())
    yt = build("youtube", "v3", credentials=creds)
    status = {"selfDeclaredMadeForKids": False}
    if when:
        status["privacyStatus"] = "private"
        status["publishAt"] = when.astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    else:
        status["privacyStatus"] = "public"
    body = {"snippet": {"title": title, "description": caption, "categoryId": "24"}, "status": status}
    req = yt.videos().insert(part="snippet,status", body=body,
                             media_body=MediaFileUpload(clip, chunksize=-1, resumable=True))
    resp = None
    while resp is None:
        _, resp = req.next_chunk()
    print("[YT] done: https://youtu.be/" + resp["id"])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--platform", required=True, choices=["fb", "ig", "yt"])
    ap.add_argument("--clip", required=True)
    ap.add_argument("--caption", required=True, help="Caption (fb, ig) or description (yt)")
    ap.add_argument("--title", default="", help="Required for yt")
    ap.add_argument("--when", help="ISO time with UTC offset, e.g. 2026-10-15T12:30-04:00")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    if not os.path.isfile(a.clip):
        sys.exit(f"Clip not found: {a.clip}")
    when = parse_when(a.when)
    if a.platform == "fb":
        post_facebook(a.clip, a.caption, a.title, when, a.dry_run)
    elif a.platform == "ig":
        post_instagram(a.clip, a.caption, when, a.dry_run)
    else:
        if not a.title:
            sys.exit("--title is required for YouTube")
        post_youtube(a.clip, a.title, a.caption, when, a.dry_run)


if __name__ == "__main__":
    main()
