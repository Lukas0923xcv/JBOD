# DIY JBOD Power Project: Streamlined Procurement Guide (8-HDD PoC)
**Destination:** Bern, Switzerland  
**Configuration:** 8-HDD Proof of Concept (1x Jonsbo N3 Backplane, 1x Mean Well RSP-200-12, 1x Mean Well LRS-150F-5, Pre-crimped Molex Pigtails).  
**Scale-Up PSU:** Mean Well RSP-500-12 (for 30–60 drives).  
**Electrical Standard:** Swiss SEV 1011 (Typ 12/13), 230 VAC / 50 Hz, 10 A max per outlet.

---

## 1. Verified Electrical & Power Calculations (from Your Spec Sheet)

Based on the calculations in [`docs/original_calculation_sheet.md`](docs/original_calculation_sheet.md), here are the exact metrics for the **8-HDD PoC setup**:

| Rail | Per-HDD Spin-up | 8 HDDs Spin-up Load | PSU Model | PSU Rated Output | Peak Load % | Margin |
|---|---|---|---|---|---|---|
| **+12 V Rail** | 1.27 A (15.24 W) | **10.16 A (121.9 W)** | **Mean Well RSP-200-12** | 16.7 A (200.4 W) | **60.8%** | **39.2% Headroom** (Well below 75% continuous target) |
| **+5 V Rail** | 0.47 A (2.35 W) | **3.76 A (18.8 W)** | **Mean Well LRS-150F-5** | 22.0 A (110.0 W) | **17.1%** | **82.9% Headroom** (Runs cool & completely silent) |
| **Combined** | 17.59 W | **140.7 W peak** | Dual Supply | 310.4 W total | **45.3%** | **Excellent safety margin** |

### Fuse Sizing for the Dual Molex Headers (Molex A1 & Molex A2)
* **Molex A1 & A2 (+12 V pins):** Carry ~5.08 A peak spin-up each $\rightarrow$ **7.5 A or 10 A ATO/ATC blade fuse**.
* **Molex A1 & A2 (+5 V pins):** Carry ~1.88 A peak each $\rightarrow$ **5 A ATO/ATC blade fuse**.
* **Common GND & "Zum Server-GND":** Run a **6.0 mm² black wire** directly from your central GND Busbar to the server chassis / motherboard ground screw.

---

## 2. Master Sourcing Catalog (What You Actually Need to Buy)

### 2.1 Power Supplies (Mouser Switzerland)

| Role | Part Number & Product | Shop Link | Price (CHF) | Stock | Datasheet | Spec Confirmation |
|---|---|---|---|---|---|---|
| **12 V PoC (16.7 A)** | **Mean Well RSP-200-12** (200.4 W, 12 V / 16.7 A, Active PFC, Universal AC) | [Mouser CH — RSP-200-12](https://www.mouser.ch/ProductDetail/MEAN-WELL/RSP-200-12) | **CHF 36.66** excl. VAT | In Stock | [RSP-200 PDF](https://www.meanwell.com/Upload/PDF/RSP-200/RSP-200-SPEC.PDF) | Confirmed: 10.0–13.2 V adj., active PFC, 16.7 A continuous. Universal 88–264 VAC input. |
| **5 V Logic (22 A)** | **Mean Well LRS-150F-5** (110 W, 5 V / 22 A, Full Range AC Input) | [Mouser CH — LRS-150F-5](https://www.mouser.ch/ProductDetail/MEAN-WELL/LRS-150F-5) | **CHF 18.67** excl. VAT | In Stock (>190) | [LRS-150F PDF](https://www.meanwell.com/Upload/PDF/LRS-150F/LRS-150F-SPEC.PDF) | Confirmed: Trimpot adjusts 4.5–5.5 V (trim to **5.15 V**). |
| *12 V Scale-Up (41.7 A)* | **Mean Well RSP-500-12** (500.4 W, 12 V / 41.7 A, Remote ON/OFF) | [Mouser CH — RSP-500-12](https://www.mouser.ch/ProductDetail/MEAN-WELL/RSP-500-12) | *CHF 81.84* | In Stock | [RSP-500 PDF](https://www.meanwell.com/Upload/PDF/RSP-500/RSP-500-SPEC.PDF) | Confirmed: Powers 30 drives at 75% load (375 W). Active PFC, remote ON/OFF control. |

---

### 2.2 DC Distribution, Protection & Pigtails (Galaxus.ch & Distrelec)

| Item | Part Number & Product | Shop Link | Price (CHF/EUR) | Stock | Spec Confirmation |
|---|---|---|---|---|---|
| **Fuse Block with Negative Bus** | **Blue Sea Systems 5026** (ST Blade Fuse Block 12-Circuit with Negative Bus & Cover) | [Galaxus.ch](https://www.galaxus.ch) | **CHF 64.40** | In Stock | 100 A total rating, 30 A per circuit, M5 main studs, M4 branch screws, clear cover. |
| **Pre-Crimped Molex Cables** | **InLine 33445** (Molex 4-Pin Y-Cable, 18 AWG, 20 cm) — *Order 2x* | [Galaxus.ch InLine 33445](https://www.galaxus.ch) | **CHF 6.85** incl. VAT | In Stock | Cut in half to yield 2 ready-to-wire female Molex pigtails with factory-crimped pins. |
| **Blade Fuses (Assortment)** | **Standard Blade Fuses** (ATO/ATC, 3 A to 30 A) | [Galaxus / Reichelt](https://www.galaxus.ch) | **~CHF 5.50** | In Stock | Insert 2x 7.5 A fuses on 12 V lines and 2x 5 A fuses on 5 V lines. |
| **WAGO 221 Lever Nuts (3-way)** | **WAGO 221-413** (Compact 3-conductor, 10-pack) | [Galaxus — WAGO 221-413](https://www.galaxus.ch) | **CHF 8.50** | In Stock | For AC mains splitting (Live, Neutral, PE) and 5 V rail branching. |
| **Ferrule Crimper Kit** | **Ratchet Ferrule Crimper + 1200 Ferrules** | [Galaxus Ferrule Kit](https://www.galaxus.ch) | **~CHF 26.00** | In Stock | Square ferrule profile for clean contact in WAGO nuts and screw terminals. |
| **Adhesive Heat Shrink** | **Quadrios 1904C053** (3:1 Dual-Wall Heat Shrink with Glue, 100 pcs) | [Galaxus — Quadrios](https://www.galaxus.ch) | **CHF 14.45** | In Stock | Dual-wall heat shrink with hot-melt adhesive for terminal insulation. |

---

### 2.3 Wiring & Terminals (Conrad.ch & Distrelec)

| Item | Part Number & Product | Shop Link | Price (CHF) | Stock | Spec Confirmation |
|---|---|---|---|---|---|
| **6.0 mm² Wire (Main DC & GND)** | **LAPP 4520014** (H07V-K 6.0 mm² Black, Meterware) | [Conrad.ch](https://www.conrad.ch) | **CHF 1.95 / m** | In Stock | Class 5 fine-stranded copper, >50 A rating. Buy 3 m black. |
| **2.5 mm² Wire (12V, 5V, PE)** | **LAPP 4520042 (Red), 4520012 (Blk), 4520002 (GN/YE)** | [Conrad.ch Meterware](https://www.conrad.ch) | **CHF 1.15 / m** | In Stock | 2.5 mm² rated 24 A. Green/Yellow for PE chassis bonding. |
| **Ring Terminals (M4/M5)** | **Klauke 6504 (M4/6mm²), 6304 (M4/2.5mm²), 6505 (M5/6mm²)** | [Conrad.ch](https://www.conrad.ch) | **~CHF 11.50** | In Stock | M4 for Mean Well terminals; M5 for Blue Sea fuse block studs. |
| **IEC C14 Switched/Fused Inlet** | **Schurter DD11.0121.1111** + Fusedrawer 4301.1401 + Fuses | [Distrelec CH](https://www.distrelec.ch) | **CHF ~22.00** | In Stock | Swiss-made panel-mount inlet with built-in 2-pole DPST switch. |
| **Swiss Typ 12 to C13 Cable** | **Schurter 6051.2015** (V-Lock, 2.5 m) | [Distrelec CH](https://www.distrelec.ch) | **CHF 11.34** | In Stock | Molded Swiss plug, mechanical V-Lock latch. |
| **DC Clamp Meter (1 mA Resolution)** | **Uni-T UT210E** True RMS Mini Clamp Meter | [Digitec.ch](https://www.digitec.ch) | **CHF 49.50** | In Stock | Non-invasively measures 1.27 A spin-up surge and 0.25 A idle currents per conductor. |
