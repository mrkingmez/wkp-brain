# ESP32 hobby: retail verification (angle A)
Date seen: 2026-11-22. Read-only. Nothing bought, nothing added to cart, no login used. Prices are what the page showed that day. Amazon prices include Black Friday deals and move daily. Shipping and tax not included unless stated.

## Pages opened vs not
- OPENED (Chrome tool, real page text): store.freenove.com FNK0083 product page and ESP32 search listing (31 results); us.elegoo.com ESP-32 Super Starter Kit page; Amazon search result pages and product pages (Elegoo ESP32 kit, Elegoo UNO R4 kit, Freenove CAM Ultimate kit, Elegoo 37-in-1).
- OPENED via WebFetch: adafruit.com/product/5325 only (QT Py ESP32-S2, $12.50, 30 in stock).
- BLOCKED: WebFetch to Freenove, Elegoo and Amazon returned 429/503. The Chrome tool got through.
- NOT CHECKED: SparkFun, Seeed store, DFRobot, Keyestudio site, Waveshare site, M5Stack, LILYGO, Espressif store, Walmart, eBay, camelcamelcamel, Keepa, Wayback. Seeed XIAO and Waveshare appear only as Amazon listings. All "not verified".
- Amazon review text was not read, only star averages and counts from search cards.

## 1. Kit table (prices seen 2026-11-22)
| Kit | SKU/ASIN | Price seen, where | Boards | Camera | Parts | Display | Breadboard | USB cable | Solder | Tutorial | Stars (count) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Freenove ESP32-S3 CAM Super Starter | FNK0083 | $44.99 store.freenove.com, free standard shipping, "may need to pay customs duties and VAT" | 1 ESP32-S3 CAM (8MB flash, 8MB PSRAM), 1GB card + reader | Y | 176 items, 81 projects | not on page text | not on page text (not verified) | not verified | no | 584 pages, downloadable/online, MicroPython + C, no paper | 4.9 (21) store |
| Freenove ESP32-S3 CAM Ultimate | store; Amazon B0BMQ2CPQN | $59.99 store; $49.95 Amazon (list $59.90, Black Friday) | 1 S3 CAM | Y | 243 items, 121 projects | not verified | not verified | not verified | no | 828 pages, Python/C/Java | 4.6 (144) Amazon |
| Freenove ESP32 (non-S3) CAM Ultimate | B0CJJJ7BCY | $45.45 Amazon | 1 ESP32 CAM (4MB flash, 8MB PSRAM) | Y | 240 items, 122 projects | not verified | not verified | not verified | no | 795 pages | 4.6 (270) |
| Freenove ESP32-S3 CAM Basic | store | $31.99 store | 1 S3 CAM | Y | 144 items, 60 projects | - | - | - | no | 463 pages | not read |
| Freenove ESP32 CAM Basic | store | $28.99 store | 1 | Y | 143 items, 58 projects | - | - | - | no | 400 pages | not read |
| Freenove ESP32 CAM Super | store | $41.99 store | 1 | Y | 175 items, 78 projects | - | - | - | no | 522 pages | not read |
| Freenove S3 CAM board + 1GB card (board only) | store | from $19.99 | 1 | Y | board | - | - | - | no | example tutorial | - |
| Freenove ESP32-S3 DEV (no camera) | store | from $14.99 | 1 | N | board | - | - | - | no | example | - |
| Freenove Media Kit ESP32-S3 | store | $34.99 or $44.99 | 1 S3 CAM | Y | screen, speaker, mic, AI voice | screen | - | - | - | - | not read |
| Freenove Touch Display CYD ESP32-S3 | store | from $21.99 | 1 | - | 2.8/3.5/4.0 in IPS touch | touch | - | - | - | LVGL | - |
| ELEGOO ESP-32 Super Starter Kit | B0FR4RGDYN | $31.44 Amazon; us.elegoo.com price NOT in page text (page shows "105 credits", $15 shipping under $50) | 1 ESP-32 WROOM, CP2102, USB-C | N | "35+ modules" incl OLED, servo, keypad; "200+ parts" claim | OLED yes | not confirmed | not verified | no | online tutorial reported dead (see flags) | Amazon 4.4 (240); us.elegoo.com 3.5 (2) |
| ELEGOO UNO R4 WiFi Super Starter (NOT ESP32) | B0GV391HB3 | $45.99 Amazon | UNO R4 (5V logic) | N | 200+ parts | - | - | - | no | online | 4.6 (67). Skip. |
| SunFounder ESP32 Ultimate Starter | B0HJ5L7XGH | $47.99 Amazon | not verified | appeared in ESP32-CAM search, not verified | - | - | - | - | - | - | 5.0 (42), thin history |
| ACEBOTT ESP32 Electronics Kit | B0FNRDSWPM | $23.99 Amazon | not verified | not verified | - | - | - | - | - | - | 4.5 (190) |
| Lonely Binary 400+ pc kit for ESP32 | B0FJ4P9SN3 | $18.99 Amazon | probably parts only (verify) | N | 400+ parts | - | - | - | - | - | 4.4 (66) |
"-" or "not verified" means the page text did not state it. The Freenove store page text did not list box contents, so breadboard and cable are not verified, though the title says wires, modules, sensors are included.

Tutorial notes from the pages: Freenove ships a 584 page PDF per kit. A store reviewer says support answers daily and that the MicroPython tutorial does not cover the Wi-Fi camera stream, only the C/Arduino one does. Two Elegoo US reviewers (dated 08/09/2026 and 09/12/2026) say the Elegoo ESP-32 kit tutorial URL is dead and one returned the kit.

## 2. Verdict
Best single start for a beginner who wants a camera: Freenove FNK0083, $44.99 direct (store lists in stock), or Freenove ESP32 CAM Ultimate B0CJJJ7BCY $45.45 on Amazon (more projects, older non-S3 board). Amazon's S3 Ultimate at $49.95 is a Black Friday price, list $59.90. Elegoo ESP32 at $31.44 has no camera and a reportedly dead tutorial. Not a good first kit until that is fixed.

## 3. Build-your-own bundle (Amazon prices seen 2026-11-22, link pattern amazon.com/dp/ASIN)
| Part | Item | Price | Notes |
|---|---|---|---|
| 3 x ESP32-S3 DevKitC-1 N16R8 | AITRIP 3PCS | $18.99 (4.2, 38) | ASIN not captured. Alternate Hosyond 3Pack N16R8 $18.99 (4.4, 154). hiBCTR 3-pack $19.79 has only 5 reviews |
| 3 x ESP32 WROOM | ELEGOO 3PCS ESP-WROOM-32 USB-C | $16.14 (4.7, 576) | best-reviewed multipack seen. Hosyond 3Pack $12.79 (4.6, 169) |
| 3 x tiny C3 | Seeed XIAO ESP32C3 3-pack | $16.99 (4.9, 107) | genuine Seeed; XIAO ESP32S3 3-pack $21.59 (4.6, 95) |
| Camera | ESP32-CAM OV2640 1pc | $11.99 (4.1, 269) | B07WCFGMTF, needs a USB programmer. Aideepen ESP32-CAM-MB $14.72 (4.0, 84) B0FLP81B44 includes one. Easiest: Seeed XIAO ESP32-S3 Sense with camera and mic $19.19 (4.4, 394) |
| Sensors | ELEGOO 37-in-1 | $31.44 (4.7, 2.5K) | B01MG49ZQ5. Cheaper unbranded 37-in-1 $15.19 (4.2, 20) B0DC6J2RKP; Keyestudio 37 $24.99 to $32 (4.5) |
| OLED | ELEGOO 0.96 in SSD1306 I2C 3-pack | $8.49 (4.7, 279) | B0FSRQG23K |
| Breadboard + wires | 830+400 breadboards and jumper kit | $9.99 (4.5, 155) | B09VKYLYN7; ELEGOO 120 Dupont wires B01EV70C78 |

Cheapest sensible total: 18.99 + 16.14 + 11.99 + 15.19 + 8.49 + 9.99 = about $80.79 (6 boards, camera, 37 sensors, OLED, wires). Better-quality swap (Elegoo 37-in-1, Seeed S3 Sense instead of ESP32-CAM): about $109. Compare Freenove FNK0083 $44.99 for 1 board, camera, 81 guided projects. Suggestion: start with the Freenove kit for the tutorial, add a $16 to $19 board multipack later.

3.3V check (general knowledge, not from the pages): ESP32 GPIO is 3.3V and not 5V tolerant. The 37-in-1 modules are sold for 5V Arduino. Many run fine at 3.3V (buttons, LEDs, DHT11, DS18B20, analog pots), relay modules need 5V for the coil, and 5V outputs such as an HC-SR04 echo must be level-shifted. Not verified per module, check each datasheet. SSD1306 OLED is fine at 3.3V I2C. ESP32-CAM wants a solid 5V supply on its 5V pin.

## 4. Risk flags
- Price gouging (search snippets, last-resort source, not opened): FNK0083 at $82.99 and $130.99 from third-party marketplace listings versus $44.99 official. Elegoo ESP32 kit at $90 on a marketplace versus $31.44 Amazon. Buy from store.freenove.com or Amazon sold by the maker.
- Generic N16R8 multipacks (AITRIP, Hosyond, hiBCTR, Lonely Binary) are clones of Espressif's DevKitC-1. Watch for wrong variant (one listing was N8R2 at $8.99 under a similar title), dual USB-C confusion (use the UART port to flash first), and 5-star scores with 2 to 14 ratings.
- No-name ESP32-CAM at $11.99 often has no USB board and weak antenna.
- Elegoo ESP-32 kit: dead tutorial reported by two recent buyers.
- Amazon prices are Black Friday deals and may jump. SunFounder and ACEBOTT ESP32 kits have thin review history.
- Slow China shipping: Freenove says "may need to pay customs duties and VAT" and does not state the ship-from country, so not verified. AliExpress and eBay not opened.

## 5. Not verified
Adafruit/SparkFun/Seeed/DFRobot/Keyestudio/Waveshare/M5Stack/LILYGO/Espressif store prices, Walmart, eBay, price history, Amazon review text, Freenove box contents, Elegoo US price on its own site, full Elegoo kit contents.
