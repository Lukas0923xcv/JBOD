# DIY JBOD Power Project: Parts List (Finalized for 8-HDD PoC)

> [!NOTE]
> **Complete Procurement Guide & Direct Shop Links:**  
> See the companion file [`jbod_power_procurement_guide.md`](file:///c:/work/antigravity/ai/jbod_power_procurement_guide.md) for full distributor carts, exact part numbers, pricing delivered to Bern, and wiring instructions.

---

## 1. Project Decisions & Status for the 8-HDD Proof of Concept (PoC)

1. **Test Scope:** 1x Jonsbo N3 Backplane (8 bays, 2x Molex), 8x 3.5" SATA HDDs.
2. **Backplanes:** Already on hand (2x Jonsbo N3 backplanes from AliExpress).
3. **Data / HBA:** No HBA or SAS expander needed for this power spin-up test.
4. **12 V PSU:** **Mean Well LRS-200-12** (12 V / 17 A, 204 W, 1U profile).
   - Peak spin-up load: $8 \times 1.27\text{ A} = \mathbf{10.16\text{ A}}\ (121.9\text{ W})$, running at **59.6% rated load**.
   - Trimmer `SVR1` tuned to **12.15 V**.
   - ⚠️ **Red slide switch set to 230 V!**
5. **5 V PSU:** **Mean Well LRS-150F-5** (5 V / 22 A, 110 W).
   - Peak logic load: $8 \times 0.47\text{ A} = \mathbf{3.76\text{ A}}\ (18.8\text{ W})$, running at **17.1% load**.
   - Trimmer `VR1` tuned to **5.15 V** (datasheet range 4.5–5.5 V).
6. **Molex Pigtails:** **Pre-crimped InLine 33445** (18 AWG Y-cables, Galaxus) cut into factory-stamped pigtails. Open-barrel crimper omitted.
7. **Fusing:**
   - 12 V lines: **2x 7.5 A (or 10 A) fast-acting ATO/ATC blade fuses**.
   - 5 V lines: **2x 5 A fast-acting ATO/ATC blade fuses**.
8. **AC & DC Distribution:**
   - AC branching: **WAGO 221-413 (3-conductor lever nuts)** for Live, Neutral, and PE.
   - 5 V branching: **WAGO 221-413 lever nut** branching PSU 5 V to both Molex leads.
   - Ground Bus: Handled directly on the **Blue Sea 5026 negative bus**. Separate 150 A copper busbar deferred to 40–60 drive scale-up.
   - Inrush sequencing relay: Omitted for 8-drive test.

---

## 2. Master Sourcing Table (Grouped by Distributor)

| Item | Model / Part Number | Distributor | Qty | Approx. Price (CHF) | Status / Notes |
|---|---|---|---|---|---|
| **12 V Main PSU** | Mean Well `LRS-200-12` | [Mouser CH](https://www.mouser.ch/ProductDetail/MEAN-WELL/LRS-200-12) | 1 | CHF 26.50 | In Stock. 12V / 17A. Set switch to 230V. |
| **5 V Logic PSU** | Mean Well `LRS-150F-5` | [Mouser CH](https://www.mouser.ch/ProductDetail/MEAN-WELL/LRS-150F-5) | 1 | CHF 18.67 | In Stock. 5V / 22A. Tune to 5.15V. |
| **DC Fuse Block with Neg Bus** | Blue Sea Systems `5026` | [Galaxus.ch](https://www.galaxus.ch) | 1 | CHF 64.40 | In Stock. 12 circuits, 100A rated, M5 studs. |
| **Pre-Crimped Molex Y-Cables** | InLine `33445` (18 AWG, 20 cm) | [Galaxus.ch](https://www.galaxus.ch) | 2 | CHF 13.70 | In Stock. Cut in half to make 2 pigtails. |
| **Blade Fuses Assortment** | Standard Auto Blade Fuses | [Galaxus.ch](https://www.galaxus.ch) | 1 box | CHF 5.50 | In Stock. 5A & 7.5A/10A fuses used. |
| **WAGO 221-413 Lever Nuts** | WAGO `221-413` (10-pack) | [Galaxus.ch](https://www.galaxus.ch) | 1 pack | CHF 8.50 | In Stock. For all AC & 5V branching. |
| **Ferrule Crimper Kit** | Hex/Square Crimper + 1200 Ferrules | [Galaxus.ch](https://www.galaxus.ch) | 1 kit | CHF 26.00 | In Stock. Budget tool + ferrule assortment. |
| **Adhesive Heat Shrink** | Quadrios `1904C053` (3:1 dual-wall) | [Galaxus.ch](https://www.galaxus.ch) | 1 box | CHF 14.45 | In Stock. Weatherproof adhesive seal. |
| **Switched/Fused IEC C14 Inlet** | Schurter `DD11.0121.1111` | [Distrelec CH](https://www.distrelec.ch) | 1 | CHF 13.76 | In Stock. Swiss-made DPST switched inlet. |
| **2-Pole Fusedrawer** | Schurter `4301.1401` | [Distrelec CH](https://www.distrelec.ch) | 1 | CHF 6.06 | In Stock. Drawer for DD11 with 2x 6.3A fuses. |
| **Swiss Typ 12 to C13 Cable** | Schurter `6051.2015` (V-Lock, 2.5 m) | [Distrelec CH](https://www.distrelec.ch) | 1 | CHF 11.34 | In Stock. Molded Swiss plug with V-Lock. |
| **6.0 mm² Wire (DC & Server GND)**| LAPP `4520014` (H07V-K Black) | [Conrad.ch](https://www.conrad.ch) | 3 m | CHF 5.85 | In Stock. Meterware. Central ground bonding. |
| **2.5 mm² Wire (12V, 5V, PE)** | LAPP `4520042` (Red), `4520012`, `4520002`| [Conrad.ch](https://www.conrad.ch) | 6 m | CHF 6.90 | In Stock. Meterware. Branch power & PE. |
| **Ring Terminals M4 & M5** | Klauke `6504`, `6304`, `6505` | [Conrad.ch](https://www.conrad.ch) | packs | CHF 11.50 | In Stock. DIN 46237 insulated crimp lugs. |
| **DC Clamp Meter (1 mA Res)** | Uni-T `UT210E` True RMS | [Digitec.ch](https://www.digitec.ch) | 1 | CHF 49.50 | In Stock. Non-invasive spin-up current measurement. |

---

## 3. Scale-Up Additions (40–60 Drives Target)

When moving from the 8-HDD PoC to the 40–60 HDD production enclosure:
1. **12 V Supplies:** Upgrade to 2x **Mean Well PSP-600-12** (active current sharing & remote ON/OFF) or 2x **LRS-600-12** (split into 2 isolated 30-drive loops).
2. **Busbars:** Add the **Blue Sea Systems 2301 (150 A)** copper busbars for high-current paralleling.
3. **Data Subsystem:** Add the **Broadcom SAS 9300-8i / 9400-8i** HBA and **Intel RES2SV240** / **Adaptec AEC-82885T** SAS expander cards with active cooling.
4. **Mains Inrush:** Add the **Finder 80.11 ON-delay relay** to stagger 12 V power activation 2 seconds after the 5 V rail to prevent domestic circuit breaker nuisance trips.
