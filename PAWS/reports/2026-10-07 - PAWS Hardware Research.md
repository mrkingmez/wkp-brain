# PAWS Hardware Research: Scout Two-Screen Build

Date: 2026-10-07. Research only. Nothing ordered. Prices are from search snapshots checked 2026-10-07 and are NOT yet verified against live product pages. Treat every price as approximate until a BOM pass confirms it.

## Bottom line

Zac's spec (clear screen for the character, bigger touch screen for functions, brain, storage, battery, SD plus microSD reader, USB-A and USB-C) does not fit the Waveshare ESP32-S3-Touch-LCD-1.69 that was locked earlier. That board has four free pins and one USB port, which is the whole PAWS-007 problem. The spec as written points to a Raspberry Pi class brain. That makes this a platform change, not a parts add-on. Queued as PAWS-008 for Zac's call.

If Zac approves the Pi path, PAWS-007 (SD vs audio pin fight) disappears: a Pi has plenty of GPIO, and the SD reader arrives over USB, not over the pins.

## Proposed parts, by job

**1. Clear screen for Scout: Waveshare 1.51 inch Transparent OLED (SKU 22545)**
- 128 by 64 pixels, SPI or I2C, light blue only. Monochrome. Scout would be blue pixel art floating in glass, not a color character.
- Price seen: about $39.14 (Robotshop US), $28.56 (Robotshop Canada, 1 left), about 14.91 pounds (Waveshare UK store). No US price found on Waveshare's own site.
- Open question for Zac: blue-only, 1.51 inches is small. Larger or color transparent panels were not researched yet. If Scout needs color, that is a separate search.
- Design note: a transparent OLED only lights pixels. Whatever sits behind it shows through, so it needs a dark or printed backdrop, not a bright screen behind it.

**2. Larger touch screen: Raspberry Pi Touch Display 2**
- 5 inch at $40 list, 7 inch at $60 list (both 720 by 1280, capacitive, DSI connector). Resellers seen at $51 for the 5 inch. 7 inch seen at about 57.60 pounds (Pi Hut) and about $70 (Little Bird, converted).
- Needs a Pi with a DSI port. The Pi Zero family has none, so Zero 2 W is out for this screen.
- Not the same as the Adafruit listing seen on Jameco ($251.95), which looks like a bad or stale price. Ignore.

**3. Brain: Raspberry Pi 5 (4GB)**
- List about $110 after the April 2026 memory-driven increases, street seen from $96 to $153. Prices are moving every few months.
- Gives USB-A host, USB-C, DSI, full GPIO, microSD boot. Pi Zero 2 W (about $28 to $35 street) is cheaper but cannot drive the Touch Display 2.
- Cheaper Pi 5 sizes and the Pi 4 were not priced. Worth a follow-up since this is the biggest line item.

**4. Storage: microSD card for the Pi, plus the card reader below for user cards**
- Not priced this pass. Needs three suppliers per SOURCING rules. Target: A2-rated 64GB or 128GB.

**5. Battery: Waveshare UPS HAT (E) plus four 21700 cells**
- HAT about $32.99 plus about $8 shipping direct (Liliputing), $44.99 on Amazon. Fits Pi 5, 4, 3.
- Cells are NOT included. Liliputing put a full 20000 mAh set around $30. Needs its own sourcing and a note on shipping lithium cells.
- Alternative cheaper board, UPS HAT (B) on 18650 cells, about 25 pounds, but low stock. PiSugar3 was about $39.99 including its battery, but it targets the Pi Zero, so it does not match the Pi 5 path.

**6. SD plus microSD plus USB-A plus USB-C: no bare module exists**
Searches found only finished hubs, no OEM board with all five. Best matches:
- ProMaster 4041: SD slot, microSD slot, three USB-A 3.0, HDMI, USB-C with pass-through charging. Listed at $39.95. Closest to the whole ask, and it fits the earlier rule of using an existing certified dock instead of custom silicon.
- Hama 00200140: three USB-A, SD and microSD, USB 3.2 Gen 1. Aluminum housing.
- StarTech HB31C3ASDMB: three USB-A plus SD only. microSD needs an adapter, so it misses the spec.
- DIY split: Waveshare 4 Port USB HUB HAT ($8.99, USB 2.0 only, Zero-sized) plus a UGREEN CM387 style SD plus TF reader. Cheapest, but USB 2.0 speed and more enclosure work.
- Caveat: several of these hubs advertise UHS-II but run the card slots at UHS-I. Fine for Scout's read-only scan, flag if speed ever matters.

## Rough cost, before microSD, shipping, enclosure, cables

- Low end (5 inch screen, cheapest transparent OLED, one hub): about $282.
- High end (7 inch screen, US OLED price): about $312.
- That is the Pi 5 at $110, screen at $40 to $60, OLED at $28.56 to $39.14, UPS HAT at $32.99, cells at about $30, ProMaster hub at $39.95. Bigger than the ESP32 plan by a wide margin. Fine for a prototype, hard for a consumer price point.

## What breaks or changes if Zac goes this way

- The two Waveshare ESP32-S3 boards already ordered stay useful for Taskagotchi (Build 1) and as a cheap secondary. They do not run Scout as now specced.
- Enclosure grows: two screens, a Pi, a battery pack with four 21700 cells, a hub. ENCLOSURE.md needs a rewrite.
- Child-safety hard blockers still apply: no microphone, no LLM, no cloud or data collection on anything a person under 18 touches. A Pi runs a full OS that can do all of that, so the software has to be locked down on purpose. FIRMWARE and EDUCATION work stays gated.
- Android companion app plan is unaffected.

## What is not done

- BOM rows not added to `hardware\PAWS-BOM.xlsx`. The three-supplier price and link verification is not finished for any part above, and the SOURCING rule says no row until it is. Next pass should do that.
- microSD card, 21700 cells, color or larger transparent panels, and cheaper Pi sizes still need research.

## Decision needed

PAWS-008 in `decisions\DECISIONS.md`: move Scout to a Pi 5 based two-screen build (this report), or stay on the Waveshare ESP32 board and drop the bigger screen, USB-A, and full SD/microSD reader from v1.

## Sources

- https://robotshop.com/products/waveshare-151inch-transparent-oled-128x64-spi-i2c-light-blue-display
- https://raspberrypi.com/products/touch-display-2
- https://thepihut.com/products/raspberry-pi-touch-display-2
- https://www.techspot.com/news/111165-raspberry-pi-prices-soar-amid-ai-memory-shortage.html
- https://www.gigazine.net/gsc_news/en/20260402-raspberry-pi-price-increases
- https://thepihut.com/products/21700-ups-hat-e-for-raspberry-pi-5-4-3
- https://www.cnx-software.com/?p=134868
- https://www.cnx-software.com/2025/01/06/pisugar3-is-a-low-cost-raspberry-pi-ups-module-with-rtc-hardware-battery-protection-and-power-management-features/
- https://avlgear.com/products/promaster-4041-usb-c-card-reader-and-hub-for-sd-and-micro-sd
- https://www.waveshare.com/product/usb-hub-hat.htm
