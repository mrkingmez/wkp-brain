"""Godzilla Minus Zero sound pack builder (wwd-vfx, 2026-11-07).

Copies owned sound effects from P:\\Sounds\\Sound FX into P:\\WWD Kit\\Godzilla\\Sounds\\ with a cue
prefix, cuts one derived clip (three approaching giant steps), builds the logo start frame, and prints
ffprobe durations so the cue sheet uses real numbers. Owned files only, nothing downloaded.

Run: python make_godzilla_sound_pack.py
"""
import os
import shutil
import subprocess
import sys

SRC = "P:\\Sounds\\Sound FX\\"
DST = "P:\\WWD Kit\\Godzilla\\Sounds\\"
KIT = "P:\\WWD Kit\\Godzilla\\"
FFMPEG = "ffmpeg"

# (prefix, source path relative to SRC)
PACK = [
    # logo sting
    ("ST1 steps loop", "huge-monster-steps-looping_z1N35r4d.mp3"),
    ("ST2 stomp layer 1 blast debris", "Adobe\\Fire and Explosions\\Explosion Blast Debris Large 01.wav"),
    ("ST2 stomp layer 2 blast impact", "Adobe\\Production Elements\\Production Element Title Transition Blast Impact 01.wav"),
    ("ST2 stomp layer 3 sub rumble (use first 4 s)", "Adobe\\Drones\\Drone Production Element Imaging Deep Subsonic Rumble Bass 02.wav"),
    ("ST2 stomp layer 4 dark thud", "hit-thud-dark_GkAfpDV_.mp3"),
    ("ST2 stomp layer 5 concrete drop", "Adobe\\Impacts\\Impact Concrete Drop On Concrete Single 02.wav"),
    ("ST3 roar main dragon roars", "wild-beast-roars-dragon_zJy_cB4u.mp3"),
    ("ST3 roar layer dragon growl", "Adobe\\Horror\\Horror Dragon Growl 01.wav"),
    ("ST3 roar layer grizzly (pitch down)", "Adobe\\Animals\\Animal Mammal Carnivore Grizzly Bear Roar 02.wav"),
    ("ST3 roar layer tiger (pitch down)", "Adobe\\Animals\\Animal Mammal Carnivore Cat Tiger Roar 01.wav"),
    ("ST3 roar layer beast screech", "Adobe\\Horror\\Horror Beast Screech 01.wav"),
    ("ST4 crack 1 brick building", "Adobe\\Crashes\\Crash Brick Building 01.wav"),
    ("ST4 crack 2 rock drop", "Adobe\\Crashes\\Crash Rock Drop On Wood Debris 01.wav"),
    ("ST4 crack 3 glass crack (thin)", "Adobe\\Crashes\\Crash Glass Crack 03.wav"),
    ("ST4 crack 4 concrete smash", "Adobe\\Crashes\\Crash Concrete Smashing Through Wood Debris On Pavement Short 01.wav"),
    ("ST5 squash 1 car crushing", "Adobe\\Crashes\\Crash Car Crushing 01.wav"),
    ("ST5 squash 2 crane crush", "Adobe\\Crashes\\Crash Crane Crush Car 01.wav"),
    ("ST5 squash 3 tin crush rubble", "Adobe\\Foley\\Foley Tin Crush Rubble 01.wav"),
    ("ST5 squash 4 glass crunch", "Adobe\\Crashes\\Crash Glass Crunching On Pavement 01.wav"),
    ("ST5 squash 5 body stomp", "Adobe\\Horror\\Horror Body Stomp 03.wav"),
    ("ST6 settle debris tail", "Adobe\\Fire and Explosions\\Explosion Building Demolition Debris 02.wav"),
    # whole video
    ("VD distant bomb", "Adobe\\Fire and Explosions\\Explosion Distant Bomb 01.wav"),
    ("VD distant boom", "Adobe\\Fire and Explosions\\Explosion Distant 01.wav"),
    ("VD city sirens", "city-street-sirens-2_fyW5nW4u.mp3"),
    ("VD water surge", "Adobe\\Liquid-Water\\Liquid Water Water Splash Wave 11.wav"),
    ("VD electric sizzle", "electric-sizzle_zyuNWG4u.mp3"),
    ("VD plane flyby", "Adobe\\Transportation\\Transportation Plane Flyby 04.wav"),
    ("VD wwii machine gun", "gun-machine-gun-automatic-303-caliber-vickers-burst-close-perspective_Myp7JqE_.mp3"),
    ("VD heat ray charge", "Adobe\\Science Fiction\\Science Fiction Sci-Fi Electronic Energy Pulse Low 01.wav"),
    ("VD gravity or ray beam", "Adobe\\Science Fiction\\Science Fiction Sci-Fi Electronic Distorted Energy Beam 242.wav"),
    ("VD crowd cheer", "crowd-cheers-and-whistles_MyWbxfVu.mp3"),
    ("VD crickets", "Adobe\\Ambience_2\\Ambience Night Crickets And A Bullfrog 01.wav"),
    ("VD crowd chatter bed", "ab-f-031616-38698401_crowd-chatter-ambience-01.mp3"),
    ("VD wet rip", "Adobe\\Horror\\Horror Scary Skin Rip Wet 01.wav"),
    ("VD bone crunch", "Adobe\\Horror\\Horror Scary Bone Crunch 01.wav"),
    ("VD bone tear", "Adobe\\Horror\\Horror Scary Bone Tear Wet 02.wav"),
    ("VD smack", "punch-face-hard_f1oeQhNO.mp3"),
    ("VD rubble crash", "Adobe\\Fire and Explosions\\Explosion Building Demolition Debris 01.wav"),
    ("VD dirt dig", "Adobe\\Foley\\Foley Grass And Mud Dig With Hands Short 01.wav"),
    ("VD heartbeat slow", "heartbeat-slow_M1Vtl3VO.mp3"),
    ("VD missile whoosh", "Adobe\\Weapons\\Weapon Missile 01.wav"),
    ("VD record scratch", "record-scratch_zkkU_2VO.mp3"),
    ("VD rating hit", "Adobe\\Production Elements\\Production Element Title Transition Blast Impact 02.wav"),
    ("VD mecha whirr", "monster-whirr_zk8RqSV_.mp3"),
    ("VD mecha metal hit", "hit-metal-hard_M1WQr3Eu.mp3"),
    ("VD gong optional", "hit-metal-gong-bell-deep_M17-SnNu.mp3"),
]


def probe(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return None


def main():
    os.makedirs(DST, exist_ok=True)
    bad = 0
    for prefix, rel in PACK:
        s = SRC + rel
        if not os.path.exists(s):
            print("MISSING", s)
            bad += 1
            continue
        d = DST + prefix + " - " + os.path.basename(rel)
        shutil.copy2(s, d)

    # derived: three approaching steps from the loop (steps land at about 0.95, 1.8, 2.7 s)
    steps = SRC + "huge-monster-steps-looping_z1N35r4d.mp3"
    out = DST + "ST1b three approaching steps (cut 0.75 to 3.35 s of huge-monster-steps-looping).wav"
    subprocess.run([FFMPEG, "-v", "error", "-y", "-ss", "0.75", "-to", "3.35", "-i", steps,
                    "-af", "afade=t=in:d=0.03,afade=t=out:st=2.3:d=0.3", out], check=True)

    # start frame: logo on solid black, 1920x1080 (the logo PNG has alpha)
    from PIL import Image
    logo = Image.open("L:\\Winter Wolfs Den review show\\Pictures\\logo.png").convert("RGBA")
    bg = Image.new("RGBA", logo.size, (0, 0, 0, 255))
    bg.alpha_composite(logo)
    bg.convert("RGB").save(KIT + "Godzilla Logo - Black Start Frame.png")

    for f in sorted(os.listdir(DST)):
        print("%7.2f s  %s" % (probe(DST + f) or -1, f))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
