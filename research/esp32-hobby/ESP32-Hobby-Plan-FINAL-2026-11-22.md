# ESP32 Hobby Plan FINAL

Date: 2026-11-22. For Zac. Merged from the first pass and deep passes A to D. Where they conflict, the later verified source (A, retail pages opened 2026-11-22) wins. Nothing bought, nothing signed up for.

## 1. The answer

**Buy first: Freenove ESP32-S3 CAM Super Starter Kit, FNK0083, $44.99 at store.freenove.com** (A, opened store page 2026-11-22, free standard shipping, listed in stock). Per A: 1 ESP32-S3 CAM board (8MB flash, 8MB PSRAM), 1GB card and reader, 176 items, 81 projects, 584-page tutorial (download, MicroPython and C, no paper), no soldering, 4.9 stars (21) on the store. This replaces the first pass figures (76 projects, 539 pages).

Why: one box, one tutorial, camera included, parts made to work together.

**Three things still unverified before you pay:**
1. **Box contents.** The store page text did not list breadboard, display or cable. The title says wires, modules and sensors are included. Ask Freenove support (a store reviewer says they answer daily) or read the product page photos.
2. **USB cable.** Not verified as included. Plan on a data-capable cable of your own.
3. **Ship-from and customs.** The page says you "may need to pay customs duties and VAT" and does not name the ship-from country. Ask before ordering.

Also: buy only from store.freenove.com or Amazon sold by the maker. Third-party marketplace listings showed FNK0083 at $82.99 and $130.99 (A, search snippets, not opened).

**Not a good first kit: Elegoo ESP-32 Super Starter.** Two recent US buyers (dated 08/09/2026 and 09/12/2026) report the tutorial link is dead, and one returned the kit (A). No camera either.

## 2. Cheaper and bigger options (verified prices only)

| Option | Price | Source and date | Note |
|---|---|---|---|
| Freenove ESP32-S3 CAM Basic | $31.99 | A, Freenove store, 2026-11-22 | 144 items, 60 projects, 463 pages |
| Freenove ESP32 CAM Super (non-S3) | $41.99 | A, Freenove store, 2026-11-22 | 175 items, 78 projects, 522 pages |
| Freenove ESP32 CAM Ultimate (non-S3) | $45.45 | A, Amazon, 2026-11-22 | 240 items, 122 projects, 4.6 stars (270). Older board |
| Freenove S3 CAM Ultimate | $59.99 store; $49.95 Amazon | A, 2026-11-22 | Amazon is a Black Friday price, list $59.90. 243 items, 121 projects, 828 pages. Finish Super first |
| Freenove S3 CAM board plus 1GB card | from $19.99 | A, Freenove store | Board only |
| Seeed XIAO ESP32-S3 Sense | $18.90 Seeed (first pass, read directly); $19.19 Amazon (A) | 2026-11-22 | Camera and mic. B: one forum thread reports Windows port trouble. Pick pre-soldered |
| Adafruit ESP32-S3 Feather 5477 | $17.50 | First pass, read directly | Board only, no camera |
| ESP32-CAM with MB programmer, Aideepen | $14.72 | A, Amazon | Easy camera add-on |
| Elegoo ESP-32 Super Starter | $31.44 | A, Amazon | Dead tutorial reports. Skip |
| Build-your-own bundle | about $80.79 | A, Amazon, 2026-11-22 | 6 boards, camera, 37 sensors, OLED, wires. No tutorial. Not for a first buy |

Plan from A: start with Freenove for the tutorial, add a $16 to $19 board multipack later.

## 3. Alibaba verdict

- **No ESP32 mystery box exists on Alibaba** (D). Every mystery or blind box seen was consumer gadgets (earbuds, watches, phones, unclaimed parcels). Contents are random with no parts list. Scam pattern: 1-year-old sellers, 2.4 to 3.5 scores, $5 to $20 "phone or laptop" boxes. Skip.
- **The real option is a stated-contents kit** at about $7 to $12 (D, search cards). Landed cost is the catch: de minimis is suspended for China (CRS IF12891, Aug 2026), so duty applies. D estimates a $7 kit lands near $15 to $25. Exact current duty rate NOT VERIFIED. Shipping cost and days to Georgia NOT VERIFIED (cards showed delivery Dec 18 to Feb 17). Product pages were CAPTCHA blocked.
- Clone risk, plus 5V-era parts (37-in-1 kits are built for 5V Arduino).
- **Rule: only a small sample, only AFTER a known kit works.** If you do: seller 5+ years, 4.7+ score, pay inside Alibaba checkout, order the minimum. Keyestudio (13 yrs, 4.8, $22.70 to $26.20) is the sensible one but near Elegoo money.

## 4. Day-one checklist

1. **Tutorial version check first (10 minutes).** Download the kit code. Search it for `ledcSetup`, `ledcAttachPin`, `timerBegin`. Hits mean it was written for core 2.x (B, Espressif migration guide). Install the ESP32 core version the kit tutorial states. If it states none, use 3.3.13 (C: last 3.x release; 4.0.0 is days old and its breaking changes were not read). Core 2.0.17 is the common fix for old code (B). Kit code on 3.x is NOT VERIFIED for Freenove.
2. **Board package:** "esp32 by Espressif Systems," not "Arduino ESP32 Boards."
3. **Data-capable USB cable.** Charge-only cables are the top "no COM port" cause. Swap cable and port first.
4. **Drivers.** Check Device Manager for a COM port. Identify the small USB chip (CH340, CP210x, CH343) and install that driver.
5. **Power.** Use a PC port or a 5V 1A charger. Unplug USB before moving wires.
6. **20-minute timebox.** If upload fails for 20 minutes: new cable, new port, then stop and park it.
7. **Camera brownout fix (B):** short data cable, a different port or powered hub, a stable 5V supply. A loose ribbon cable gives "camera init failed." Camera heat and focus are NOT VERIFIED, so do not leave it enclosed and unattended.
8. Write one line: board, core version, IDE version, port, cable.

## 5. Parts that grow (dollar figures are estimates from C, not retrieved prices)

- **Phase 1, the kit itself, $44.99 (verified).** C also suggests a multimeter and 2 data cables (about $10 to $15, estimate).
- **Phase 2, about $20 (estimate):** servo SG90, capacitive soil sensor, PIR, WS2812B stick, resistors, capacitor, 5V 2A charger.
- **Phase 3, about $30 (estimate):** second board as a dedicated node, TFT or e-paper, I2S mic and amp, stepper, MPU6050. Buy a soldering iron only here.

Rule: one new part per project.

## 6. Twelve projects, quick-win order (from C; links are pages C fetched)

1. OLED hello and I2C scanner: https://randomnerdtutorials.com/esp32-ssd1306-oled-display-arduino-ide/ (2019 page, some comments report library-version failures)
2. BME280 readout on the OLED: https://randomnerdtutorials.com/esp32-bme280-arduino-ide-pressure-temperature-humidity/ (updated 2026)
3. Camera live stream on home Wi-Fi: https://randomnerdtutorials.com/esp32-cam-video-streaming-web-server-camera-home-assistant/ (written for ESP32-CAM, adapt pins for S3). A notes the Freenove MicroPython tutorial does not cover the Wi-Fi stream, only the C/Arduino one does
4. Desk clock and weather: https://randomnerdtutorials.com/esp32-http-get-post-arduino/ (2020, HTTP only; weather API terms NOT verified)
5. NeoPixel mood lamp: no verified link
6. Plant monitor: no verified link, use an ADC1 pin
7. Motion snapshot to SD: https://randomnerdtutorials.com/esp32-cam-pir-motion-detector-photo-capture/ (comments report wrong schematic and false triggers)
8. Servo desk toy: https://randomnerdtutorials.com/esp32-servo-motor-web-server-arduino-ide/ (library friction on 3.x)
9. Sensor logger to a local web page: no verified link
10. Time-lapse: no verified link
11. Desk status display from a script on your own PC: no verified link, API terms NOT verified
12. Sci-fi door sensor with sound, or a Blender enclosure: no verified link, I2S code must be 3.x-ready

Fall back to the kit's own 81 projects whenever a web tutorial breaks.

## 7. Safety and gotchas

- ESP32 pins are 3.3V and not 5V tolerant. Check every module. The HC-SR04 echo needs a divider; relay coils need 5V (A and C, general knowledge, per-module NOT VERIFIED).
- No mains. Low-voltage loads only. Do not drive relays or motors straight from a pin (B).
- Home Wi-Fi only, no port forwarding, change default passwords, keep Wi-Fi passwords out of shared code (C).
- Camera privacy: the stock stream sketch is plain HTTP with no password (C). Point it at a shelf, unplug it when guests visit, tell your wife where it points.
- Clone boards can arrive dead or with weak regulators (B, 2022 forum, mixed reports).

## 8. Not verified

- Freenove box contents, cable, breadboard, display, ship-from country, live customs charges.
- Whether the Freenove code compiles on core 3.x.
- Core 4.0.0 breaking changes.
- Alibaba shipping cost and days, current duty rate, Trade Assurance terms, product pages.
- Reddit, Amazon review text, esp32.com (not reachable).
- Camera heat and focus; clone chip genuineness.
- I2C addresses and 5V needs per module (datasheet memory).
- Elegoo US store price (not in page text; the $35.99 in the first pass was a snippet).
- Weather and sports API terms.

**Three follow-ups you could choose:**
1. Email Freenove support the three open questions (contents, cable, ship-from). Zac sends it; nothing is sent from here.
2. A free check of the downloaded Freenove tutorial code for ledcSetup, ledcAttachPin and timerBegin, plus the stated core version.
3. A Wokwi free simulator trial so you can try code before the box arrives (free-tier limits NOT VERIFIED).
