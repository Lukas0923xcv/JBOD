# 2. Bill of Materials

Everything needed for the 8-drive build, grouped by shop so each group is one order. The shops and prices are for delivery to **Bern, Switzerland**, checked October 2026.

> [!NOTE]
> Prices and stock change. Where a link only goes to a shop's home page, search the shop for the part number shown. Prices are incl. 8.1 % VAT except at Mouser, which quotes excl. VAT and adds it at checkout. Prices marked *est.* are estimates for items added after the original sourcing.

**Not included:** the Jonsbo N3 backplane (already on hand), the drives, a basic multimeter, screwdrivers, wire strippers, and a mounting board or enclosure (see [Assembly](04-assembly-guide.md#step-1-mounting)).

## Order 1: Mouser.ch (power supplies)

Free express shipping over CHF 50, shipped DDP (duties paid, no customs bill on delivery).

| ✓ | Part | Part number | Qty | Price | Notes |
|---|---|---|---|---|---|
| ☐ | 12 V supply | [Mean Well RSP-200-12](https://www.mouser.ch/ProductDetail/MEAN-WELL/RSP-200-12) | 1 | CHF 36.66 | [Datasheet](https://www.meanwell.com/Upload/PDF/RSP-200/RSP-200-SPEC.PDF) |
| ☐ | 5 V supply | [Mean Well LRS-150F-5](https://www.mouser.ch/ProductDetail/MEAN-WELL/LRS-150F-5) | 1 | CHF 18.67 | [Datasheet](https://www.meanwell.com/Upload/PDF/LRS-150F/LRS-150F-SPEC.PDF) |
| | *Scale-up only:* 12 V supply | [Mean Well RSP-500-12](https://www.mouser.ch/ProductDetail/MEAN-WELL/RSP-500-12) | – | *CHF 81.84* | Not needed for 8 drives. [Datasheet](https://www.meanwell.com/Upload/PDF/RSP-500/RSP-500-SPEC.PDF) |

**Subtotal ≈ CHF 55** (≈ CHF 60 incl. VAT)

## Order 2: Galaxus.ch / Digitec.ch (DC side and tools)

| ✓ | Part | Part number | Qty | Price | Notes |
|---|---|---|---|---|---|
| ☐ | Fuse block with negative bus | Blue Sea Systems `5026` | 1 | CHF 64.40 | 12 circuits, 100 A total, 30 A per circuit. Main studs are #10-32 (an M5 ring fits); branch screws are #8-32 (an M4 ring fits). |
| ☐ | Molex Y-cable, pre-crimped | InLine `33445` (18 AWG, 20 cm) | 2 | CHF 13.70 | Cut off the female ends to get factory-crimped pigtails. You need 2 pigtails; the second cable is a spare. |
| ☐ | Blade fuse assortment | ATO/ATC, 3–30 A | 1 box | CHF 5.50 | Must include **7.5 A** and **5 A**. You need 2 of each, plus spares. |
| ☐ | Inline blade fuse holder | ATO/ATC, for 1.0 mm² / 18 AWG wire | 2 | ~CHF 5.00 *est.* | For the two +5 V leads. |
| ☐ | Lever nuts, 3-way | WAGO `221-413` (10-pack) | 1 | CHF 8.50 | You use 6: 3 for the AC split, 1 for the 5 V split, 2 to join the fuse holders to the pigtails. |
| ☐ | Ferrule crimper + ferrules | Ratchet crimper kit with ~1200 ferrules | 1 | ~CHF 26.00 | Must cover 0.5–2.5 mm². |
| ☐ | Adhesive heat shrink | Quadrios `1904C053` (3:1 dual-wall) | 1 box | CHF 14.45 | Seals crimp barrels and splices. |
| ☐ | DC clamp meter *(recommended)* | Uni-T `UT210E` | 1 | CHF 49.50 | [Digitec](https://www.digitec.ch/de/s1/product/uni-t-ut-210e-zangenmessgeraet-5780362). Measures DC current without breaking the circuit; 2 A / 20 A / 100 A ranges. |
| | Mains power meter *(optional)* | Brennenstuhl `PM 231 E CH` | 1 | CHF 22.00 | [Digitec](https://www.digitec.ch/de/s1/product/brennenstuhl-primera-line-pm-231-e-energiekostenmessgeraet-273646). Plugs in between the wall and the cord and shows watts and power factor. |

**Subtotal ≈ CHF 138** (≈ CHF 187 with the clamp meter)

## Order 3: Distrelec.ch (mains side)

| ✓ | Part | Part number | Qty | Price | Notes |
|---|---|---|---|---|---|
| ☐ | Switched, fused C14 inlet | [Schurter `DD11.0121.1111`](https://www.distrelec.ch/en/inlet-c14-250v-schurter-dd11-0121-1111/p/16963541) | 1 | CHF 13.76 | 2-pole switch, takes a fuse drawer. Panel mount, so it needs a cutout. |
| ☐ | Fuse drawer, 2-pole | [Schurter `4301.1401`](https://www.distrelec.ch/en/fuse-drawer-schurter-4301-1401/p/14323371) | 1 | CHF 6.06 | Holds two 5×20 mm fuses. |
| ☐ | Mains fuses | 5×20 mm, **6.3 A slow-blow (T)** | 2 (+2 spare) | ~CHF 2.00 *est.* | |
| ☐ | Mains cord | [Schurter `6051.2015`](https://www.distrelec.ch/en/power-cable-ch-type-t12-plug-iec-60320-c13-5m-black-schurter-6051-2015/p/11041912) | 1 | CHF 11.34 | Swiss Typ 12 plug to C13 with V-Lock. A V-Lock plug fits a normal C14 inlet; it just won't latch. **Check the length:** the shop listing says 5 m, the original notes said 2.5 m. |
| ☐ | Flat push-on receptacles, insulated | 6.3 mm, for 1.5–2.5 mm² | 3 (+spares) | ~CHF 3.00 *est.* | For the inlet's L, N and PE tabs. |

**Subtotal ≈ CHF 36**

## Order 4: Conrad.ch (wire and terminals)

All wire is **H07V-K 2.5 mm²** (fine-stranded, rated 450/750 V), sold by the metre. One size covers the AC wiring, the DC feeds and the ground bond.

| ✓ | Part | Part number | Qty | Price | Notes |
|---|---|---|---|---|---|
| ☐ | Wire, brown | LAPP H07V-K 2.5 mm² | 1 m | ~CHF 1.15/m | AC live (L) |
| ☐ | Wire, blue | LAPP H07V-K 2.5 mm² | 1 m | ~CHF 1.15/m | AC neutral (N) |
| ☐ | Wire, green-yellow | LAPP `4520002` H07V-K 2.5 mm² | 1 m | ~CHF 1.15/m | Protective earth (PE). Use this colour for nothing else. |
| ☐ | Wire, yellow | LAPP H07V-K 2.5 mm² | 1 m | ~CHF 1.15/m | +12 V |
| ☐ | Wire, red | LAPP `4520042` H07V-K 2.5 mm² | 1 m | ~CHF 1.15/m | +5 V |
| ☐ | Wire, black | LAPP `4520012` H07V-K 2.5 mm² | 2 m | ~CHF 1.15/m | V− returns and the server ground bond |
| ☐ | Ring terminals, M5, 1.5–2.5 mm² (blue) | e.g. Klauke, DIN 46237 | 10 | ~CHF 4.00 | Fuse block main stud and negative bus stud |
| ☐ | Ring terminals, M4, 0.5–1.5 mm² (red) | e.g. Klauke, DIN 46237 | 10 | ~CHF 4.00 | 18 AWG pigtail wires to the fuse block branch screws and negative bus, and the server end of the ground bond (use a blue M4 for that one) |
| ☐ | Fork or ring terminals, 1.5–2.5 mm² (blue), sized for the PSU terminal screws | | 10 | ~CHF 4.00 | Mean Well terminal blocks use small (≈ M3.5) screws. **Check your unit** before ordering. Ferrules also work in these terminals. |

**Subtotal ≈ CHF 21**

## Total

| | Cost |
|---|---|
| Parts for the 8-drive build | **≈ CHF 250** |
| + Uni-T UT210E clamp meter | ≈ CHF 300 |
| + mains power meter | ≈ CHF 322 |

Next: [Electrical calculations](03-electrical-calculations.md)
