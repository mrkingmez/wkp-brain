# Tailscale Setup Guide: Connecting Your Second Machine

Written 2026-10-10 for Zac. Main Desktop (Windows 11 Home) plus the new second machine.

## What Tailscale does, in plain words
It puts both computers on one private network, as if they were in the same room, even when they are at different places. Nothing is opened to the public internet. Only devices signed into YOUR account can see each other.

## Before you start
- You need about 20 minutes and both machines powered on, with internet.
- You need an account to sign in with. Your Gmail (kingzpotus@gmail.com) works: Tailscale has no passwords of its own, it uses a "Sign in with Google" button.
- This guide assumes the second machine is also Windows. If it is a Mac or Linux box, the steps are the same except the install file in Part 2.

## Part 1: Main Desktop (do this first)
1. Open your web browser and go to `tailscale.com`.
2. Click **Get Started**.
3. Click **Sign up with Google**. Pick kingzpotus@gmail.com. Click **Continue** on any permission screen.
4. If it asks Business or Personal, click **Personal use**.
5. On the "Let's add your first device" page, click **Windows**.
6. Click the download button. Open the downloaded file from your Downloads folder. Click **Yes** if Windows asks permission.
7. Click through the installer with the default choices. Click **Install**, then **Finish**.
8. A sign-in window opens in your browser. Click **Sign in with Google**, pick the same Gmail account, click **Connect**.
9. Look at the bottom-right of your screen (the system tray, near the clock). You may need to click the small up arrow. A Tailscale icon should be there.
10. Right-click the icon. At the top you should see your computer name and a number starting with `100.`. Write that number down. This is the Main Desktop's private address.

## Part 2: Second Machine
1. On the second machine, open the browser and go to `tailscale.com/download`.
2. Click **Windows** and download the installer. Run it and click through with the defaults.
3. When the sign-in window opens, click **Sign in with Google**.
4. **Use the exact same Gmail account as Part 1.** A different account makes a separate network and the two machines will not see each other. This is the number one mistake.
5. Click **Connect**.
6. Right-click the Tailscale icon in the bottom-right. Write down this machine's `100.` number too.

## Part 3: Check that they can see each other
1. On your phone or either computer, go to `login.tailscale.com/admin/machines`. Sign in with Google.
2. You should see both machines listed with a green dot. If one is missing or gray, see Troubleshooting.
3. On the Main Desktop, click the Start menu, type `cmd`, press Enter.
4. In the black window type `ping ` (with a space) followed by the second machine's `100.` number, then press Enter.
5. Four lines starting with "Reply from" means it works. "Request timed out" means it does not yet.
6. Repeat from the second machine, pinging the Main Desktop's number.

## Part 4: Set up the second machine for WKP work
Do not copy the repo over Tailscale. GitHub is the source of truth.
1. Install Git for Windows, Python 3.12 and Claude Code on the second machine.
2. Sign Claude Code into your Claude account.
3. Clone the repo from GitHub (`wkp-brain`) to a folder you choose. On the main machine it is `D:\WKP`. The second machine does not have to match.
4. Open `LOCAL-PATHS.md` in the repo. Add a new section for the second machine with its own paths (repo, scratch, python, ffmpeg). This file is per-machine and must never be copied from the Main Desktop. The file already has a `## MACHINE:` section layout for exactly this.
5. Add any tokens or keys (like the Hugging Face token) on the second machine yourself, as environment variables. Never copy them into a file in the repo.
6. Commit and push the `LOCAL-PATHS.md` change so the Main Desktop sees it.

## Part 5: Moving big files between the two machines
Raw video and media do not live in GitHub. Two easy options:
- **Send a file:** in File Explorer, right-click a file and look for **Send with Tailscale** (the feature is called Taildrop). Pick the other machine. The file lands in the other machine's Downloads folder. Good for single files. If the option is missing, check it is turned on in the Tailscale menu on both machines.
- **Shared drive:** on the machine that has the files, right-click the folder, **Properties**, **Sharing**, **Share**. Give your Windows user access. From the other machine, open File Explorer and type `\\100.x.x.x` (the first machine's Tailscale number) in the address bar. Use this for the `L:` media drive.

Note: Windows 11 **Home** cannot be controlled through Remote Desktop (it can only connect out, not be connected into). If you want to see the Main Desktop's screen from the second machine, ask Claude for a separate guide on a Home-compatible option before buying anything.

## Part 6: Keep it running
1. Right-click the Tailscale icon. Make sure **Run unattended** (or "Start on login") is on, so it comes back after a reboot.
2. Do not turn on **Funnel** or share your machines with other people. Neither is needed here and both make the private network less private.
3. If a machine sleeps, it drops off. Set the second machine to never sleep while plugged in: Settings, System, Power, Screen and sleep.

## Troubleshooting
- **Second machine does not show in the admin page:** you signed in with a different account. Right-click the icon, **Log out**, sign in again with the right Gmail.
- **Ping times out but both show green:** Windows Firewall may be blocking pings. On the machine being pinged, open Start, type `Windows Defender Firewall`, click **Allow an app or feature**, and make sure **Tailscale** is checked. Try again.
- **Icon missing:** click the small up arrow near the clock. If it is still missing, open Start and type `Tailscale`.
- **Gray dot:** that machine is asleep, off, or Tailscale is not running.

## What I could not verify
- Tailscale's free plan limits change. Check `tailscale.com/pricing` for the current free Personal plan before relying on it.
- Exact button labels in the Windows app change between versions. If a label here does not match, tell Claude what you see on screen and it will adjust the step.
