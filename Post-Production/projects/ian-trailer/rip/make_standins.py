from PIL import Image, ImageDraw, ImageFont
import os
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "standin")
os.makedirs(d, exist_ok=True)
f = ImageFont.truetype("arial.ttf", 150)
s = ImageFont.truetype("arial.ttf", 48)
for name, base in (("W1a", 120), ("W1b", 70)):
    im = Image.new("RGB", (1920, 1080), (base,) * 3)
    dr = ImageDraw.Draw(im)
    for x in range(-1080, 1920, 120):
        dr.line((x, 0, x + 1080, 1080), fill=(base + 25,) * 3, width=6)
    dr.rectangle((40, 40, 1880, 1040), outline=(235, 235, 235), width=8)
    dr.text((960, 480), name, font=f, fill=(245, 245, 245), anchor="mm")
    dr.text((960, 640), "STAND-IN, not the real art", font=s, fill=(245, 245, 245), anchor="mm")
    dr.ellipse((200, 200, 360, 360), fill=(230, 230, 230))
    im.save(os.path.join(d, name + "-standin.png"))
