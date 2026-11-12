# Setting the eBay Keys as Windows Environment Variables

Written 2026-10-11. Nothing in this guide contains a real key. Never paste a key into a Claude chat, a file in the repo, or a note.

## Rules
- Do this in a normal PowerShell window you open yourself. Do NOT use the `!` prefix inside Claude Code, because anything it prints lands in the conversation.
- The method below uses a hidden prompt. What you type is not shown on screen, and it is not saved in PowerShell history.
- Start with sandbox. Sandbox keys and production keys are different keysets. Use EBAY_ENV=sandbox with sandbox keys until Zac says to switch.

## Step 1: Get the values (in your browser, not in Claude)
1. Go to `developer.ebay.com` and sign in.
2. Open your account menu and click **Application Keys**.
3. Under **Sandbox**, find your App ID (Client ID) and Cert ID (Client Secret). Keep this page open.
4. For the refresh token, on the same page click **User Tokens** next to the sandbox keyset, sign in with a sandbox test seller, and agree. The scopes must include sell.inventory, sell.account and sell.fulfillment. Copy the Refresh Token (not the short access token).

## Step 2: Open PowerShell
1. Click Start. Type `PowerShell`. Click **Windows PowerShell**. A blue window opens.

## Step 3: Set each variable
Do these one block at a time. After you press Enter, you get a prompt. Paste the value (right-click pastes) and press Enter. Nothing appears on screen. That is normal.

Client ID:
```
$s = Read-Host "EBAY_CLIENT_ID" -AsSecureString; $v = [Runtime.InteropServices.Marshal]::PtrToStringBSTR([Runtime.InteropServices.Marshal]::SecureStringToBSTR($s)); setx EBAY_CLIENT_ID $v | Out-Null; $v = $null; $s = $null
```

Client Secret:
```
$s = Read-Host "EBAY_CLIENT_SECRET" -AsSecureString; $v = [Runtime.InteropServices.Marshal]::PtrToStringBSTR([Runtime.InteropServices.Marshal]::SecureStringToBSTR($s)); setx EBAY_CLIENT_SECRET $v | Out-Null; $v = $null; $s = $null
```

Refresh Token:
```
$s = Read-Host "EBAY_REFRESH_TOKEN" -AsSecureString; $v = [Runtime.InteropServices.Marshal]::PtrToStringBSTR([Runtime.InteropServices.Marshal]::SecureStringToBSTR($s)); setx EBAY_REFRESH_TOKEN $v | Out-Null; $v = $null; $s = $null
```

Environment (not secret, so a plain command is fine):
```
setx EBAY_ENV sandbox
```

## Step 4: Check without showing the values
1. Close the PowerShell window. Setx only affects windows opened after it runs.
2. Open a new PowerShell window.
3. Paste this. It prints lengths only, never the values:
```
"ID: " + $env:EBAY_CLIENT_ID.Length; "SECRET: " + $env:EBAY_CLIENT_SECRET.Length; "TOKEN: " + $env:EBAY_REFRESH_TOKEN.Length; "ENV: " + $env:EBAY_ENV
```
4. Every number should be bigger than 0, and ENV should say `sandbox`. A length of 0 or an empty line means that variable did not save. Repeat its block from Step 3.
5. Watch the TOKEN number. Setx cuts values off at 1024 characters. If your token is longer than that, setx keeps only the first 1024, and the token is broken. If TOKEN is exactly 1024, use the fallback below.

## Fallback for a long refresh token
This has no length limit and also keeps the value off the command line:
```
$s = Read-Host "EBAY_REFRESH_TOKEN" -AsSecureString; $v = [Runtime.InteropServices.Marshal]::PtrToStringBSTR([Runtime.InteropServices.Marshal]::SecureStringToBSTR($s)); [Environment]::SetEnvironmentVariable("EBAY_REFRESH_TOKEN", $v, "User"); $v = $null; $s = $null
```
Then repeat Step 4.

## Step 5: Restart Claude Code
Claude Code only sees the variables if you start it after Step 3. Close it and open it again. Then ask Claude to run `ebay_api.py --check --dry-run`. Auth should say OK instead of SKIP. The check only reports OK or SKIP and never prints a key.

## To remove one
```
[Environment]::SetEnvironmentVariable("EBAY_CLIENT_SECRET", $null, "User")
```
Change the name for the one you want gone.

## Good to know
- These variables are saved for your Windows user only. Anyone who can log in as you on this machine can read them.
- On the second machine, repeat this guide. Never copy keys between machines through the repo, chat or email.
- If a key ever leaks (pasted in a chat, committed), go back to the developer page and regenerate it right away.
- Production comes later: new keyset, new refresh token, and `setx EBAY_ENV production`.
