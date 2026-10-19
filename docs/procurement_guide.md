# JBOD Power Project: Procurement & Sourcing Guide

Complete Bill of Materials (BOM), verified manufacturer part numbers, Swiss/EU vendor links, pricing, and purchasing groups for the 8-HDD benchtop setup (and RSP-500-12 scale-up).

---

## 1. Verified Bill of Materials (8-HDD Proof of Concept)

### Group 1: Power Supplies (Mouser Switzerland)
*Dispatched from authorized distribution. Free FedEx Express on orders > CHF 50.–. DDP terms (direct Swiss VAT, zero post-delivery customs fees).*

| Component | Manufacturer Part Number (MPN) | Vendor / Purchase Link | Qty | Price (CHF) | Spec Notes |
|---|---|---|---|---|---|
| **12 V Main PSU** | `RSP-200-12` | [Mouser CH — RSP-200-12](https://www.mouser.ch/ProductDetail/MEAN-WELL/RSP-200-12) | 1 | **CHF 36.66** | 200.4 W, 12 V / 16.7 A. Active PFC. Universal 88-264 VAC input. |
| **5 V Logic PSU** | `LRS-150F-5` | [Mouser CH — LRS-150F-5](https://www.mouser.ch/ProductDetail/MEAN-WELL/LRS-150F-5) | 1 | **CHF 18.67** | 110 W, 5 V / 22 A. Full-range AC input. Output adjusts 4.5–5.5 V (set to 5.15 V). |
| *Scale-Up 12 V PSU* | `RSP-500-12` | [Mouser CH — RSP-500-12](https://www.mouser.ch/ProductDetail/MEAN-WELL/RSP-500-12) | *Optional* | *CHF 81.84* | 500.4 W, 12 V / 41.7 A. Active PFC, remote ON/OFF, powers 30 drives. |

---

### Group 2: DC Protection, Wiring & Connectors (Galaxus / Digitec CH)
*Domestic Swiss shipping (Wohlen AG warehouse). Free delivery in Switzerland. 8.1% Swiss MWST included.*

| Component | Manufacturer Part Number (MPN) | Vendor / Purchase Link | Qty | Price (CHF) | Spec Notes |
|---|---|---|---|---|---|
| **DC Fuse Block with Negative Bus** | Blue Sea Systems `5026` | [Galaxus — Blue Sea 5026](https://www.galaxus.ch) | 1 | **CHF 64.40** | 12 circuits, 100 A total rating, 30 A per branch. M5 main studs, M4 branch screws, clear insulating cover. |
| **Pre-Crimped Molex Y-Cables** | InLine `33445` (18 AWG, 20 cm) | [Galaxus — InLine 33445](https://www.galaxus.ch) | 2 | **CHF 13.70** (pair) | Cut in half to yield two factory-crimped female LP4 pigtails with clean pins. |
| **ATO/ATC Blade Fuse Assortment** | Standard Auto Blade Fuses (3A–30A) | [Galaxus / Reichelt](https://www.galaxus.ch) | 1 box | **CHF 5.50** | Fast-acting zinc alloy blade fuses. Use 2x 7.5 A on 12 V lines and 2x 5 A on 5 V lines. |
| **WAGO 221 Lever Nuts (3-way)** | WAGO `221-413` (Compact 3-conductor) | [Galaxus — WAGO 221-413 (10-pack)](https://www.galaxus.ch) | 1 pack | **CHF 8.50** | Rated 450 V / 32 A. Handles all AC mains splitting and 5 V rail splitting safely. |
| **Ferrule Crimper Kit** | Hex/Square Ratchet Crimper + 1200 Ferrules | [Galaxus Ferrule Kit](https://www.galaxus.ch) | 1 kit | **~CHF 26.00** | Provides neat square ferrule ends on fine-stranded wire for WAGO clamps and screw terminals. |
| **Adhesive Heat Shrink Assortment** | Quadrios `1904C053` (3:1 dual-wall) | [Galaxus — Quadrios Heat Shrink](https://www.galaxus.ch) | 1 box | **CHF 14.45** | Dual-wall polyolefin with internal hot-melt adhesive for insulating ring terminal shanks. |

---

### Group 3: Mains Side Hardware (Distrelec Switzerland)
*Dispatched from Nänikon (ZH) warehouse. Domestic Swiss invoicing.*

| Component | Manufacturer Part Number (MPN) | Vendor / Purchase Link | Qty | Price (CHF) | Spec Notes |
|---|---|---|---|---|---|
| **Switched/Fused IEC C14 Inlet** | Schurter `DD11.0121.1111` | [Distrelec — Schurter DD11](https://www.distrelec.ch/en/inlet-c14-250v-schurter-dd11-0121-1111/p/16963541) | 1 | **CHF 13.76** | Swiss-made panel-mount inlet with built-in 2-pole DPST switch and dual fuseholder. |
| **2-Pole Fusedrawer** | Schurter `4301.1401` | [Distrelec — Schurter 4301.1401](https://www.distrelec.ch/en/fuse-drawer-schurter-4301-1401/p/14323371) | 1 | **CHF 6.06** | Required drawer for DD11 inlet. Holds two 5x20 mm slow-blow fuses (6.3 A or 10 A). |
| **Swiss Typ 12 to C13 Cable** | Schurter `6051.2015` (V-Lock, 2.5 m) | [Distrelec — Schurter 6051.2015](https://www.distrelec.ch/en/power-cable-ch-type-t12-plug-iec-60320-c13-5m-black-schurter-6051-2015/p/11041912) | 1 | **CHF 11.34** | SEV-approved molded Swiss 3-pin plug to C13 with anti-disconnect mechanical V-Lock latch. |

---

### Group 4: Cut-to-Length Wire & Ring Terminals (Conrad Switzerland)
*Wire cut to exact meter lengths from Swiss stock.*

| Component | Manufacturer Part Number (MPN) | Vendor / Purchase Link | Qty | Price (CHF) | Spec Notes |
|---|---|---|---|---|---|
| **6.0 mm² Wire (DC & Server GND)** | LAPP `4520014` (H07V-K 6 mm² Black) | [Conrad — LAPP 6 mm² Meterware](https://www.conrad.ch/de/p/lapp-4520014-litze-h07v-k-1-x-6-mm-schwarz-meterware-603120.html) | 3 m | **CHF 5.85** | Class 5 fine-stranded copper. Central negative feed and server chassis ground bonding. |
| **2.5 mm² Wire (12V, 5V, PE)** | LAPP `4520042` (Red), `4520012` (Blk), `4520002` (GN/YE) | [Conrad — LAPP 2.5 mm² Meterware](https://www.conrad.ch) | 2 m each | **CHF 6.90** | Class 5 copper. Red = +5V, Black = 12V/GND, Green/Yellow = Protective Earth. |
| **M3.5 / M4 Ring Terminals** | Klauke `6504` (6 mm²) & `6304` (2.5 mm²) | [Conrad — Klauke Ring Terminals](https://www.conrad.ch) | 10-packs | **~CHF 8.00** | DIN 46237 insulated crimp terminals for Mean Well PSU screw terminal blocks. |
| **M5 Ring Terminals** | Klauke `6505` (6 mm² / M5 stud hole) | [Conrad — Klauke M5 Terminals](https://www.conrad.ch) | 5 pcs | **~CHF 3.50** | Bolts 6 mm² wires securely onto the Blue Sea 5026 positive and negative studs. |

---

### Group 5: Recommended Diagnostic Gear

| Component | Manufacturer Part Number (MPN) | Vendor / Purchase Link | Qty | Price (CHF) | Spec Notes |
|---|---|---|---|---|---|
| **Mini DC Clamp Meter (1 mA Resolution)** | Uni-T `UT210E` True RMS | [Digitec — Uni-T UT210E](https://www.digitec.ch/de/s1/product/uni-t-ut-210e-zangenmessgeraet-5780362) | 1 | **CHF 49.50** | **Essential diagnostic tool.** Dedicated 2.000 A DC range with 1 mA resolution non-invasively measures 1.27 A spin-up surges and 0.25 A idle currents without breaking wires. |
| **Mains Power Monitor (Swiss T13)** | Brennenstuhl Primera-Line `PM 231 E CH` | [Digitec — Brennenstuhl PM 231 E](https://www.digitec.ch/de/s1/product/brennenstuhl-primera-line-pm-231-e-energiekostenmessgeraet-273646) | 1 | **CHF 22.00** | Plugs between wall and Schurter cable. Measures active watts (W), apparent power (VA), and power factor. |

---

## 2. Order Packaging Strategy (Bern, Switzerland)

* **Package 1 (Galaxus.ch / Digitec.ch):** Blue Sea 5026, Molex Y-cables, WAGO 221 nuts, blade fuses, ferrule kit, heat shrink, and Uni-T UT210E clamp meter.  
  *Subtotal: ~CHF 182.– (Free shipping, next-day Swiss Post).*
* **Package 2 (Mouser.ch):** Mean Well RSP-200-12 (CHF 36.66) + Mean Well LRS-150F-5 (CHF 18.67).  
  *Subtotal: ~CHF 55.33 (Free FedEx Express, DDP customs clearance).*
* **Package 3 (Distrelec.ch):** Schurter DD11 inlet, fusedrawer 4301.1401, Swiss V-Lock cable, 5x20 mm 6.3 A fuses.  
  *Subtotal: ~CHF 33.– (Dispatched from Nänikon ZH).*
* **Package 4 (Conrad.ch):** LAPP H07V-K wire cut to length by the meter (6 mm², 2.5 mm²), Klauke ring terminals.  
  *Subtotal: ~CHF 24.– (Domestic Swiss delivery).*

**Total PoC Build Cost:** **~CHF 295.–** (or **~CHF 345.–** including the UT210E clamp meter).
