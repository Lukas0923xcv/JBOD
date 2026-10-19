# 2. Bill of Materials

Everything needed for the 8-drive build, grouped by shop so each group is one order. The shops and prices are for delivery to **Bern, Switzerland**, checked October 2026.

> [!NOTE]
> Prices and stock change. Where a link only goes to a shop's home page, search the shop for the part number shown. Prices are incl. 8.1 % VAT except at Mouser, which quotes excl. VAT and adds it at checkout. **Each price is the line total for the quantity shown.** Prices marked *est.* are estimates for items added after the original sourcing.

**Not included:** the Jonsbo N3 backplane (already on hand), the drives, a ≈ 420 × 300 mm insulating mounting board (plywood, phenolic or acrylic, see [Assembly](04-assembly-guide.md#step-1-enclosure-and-mounting)), and these tools:

- multimeter that reads 0.01 V and has a **MIN/MAX** (or "peak hold") mode
- screwdrivers (small flat and PH2)
- wire stripper for 0.5–2.5 mm²
- ratchet crimper for insulated ring, fork and flat push-on terminals (red/blue)
- 3/8″ (≈ 9.5 mm) nut driver or spanner
- heat gun
- drill and a way to cut the inlet cutout in the enclosure (jigsaw with metal blade, nibbler or step drill and file)
- optional: IR thermometer for the temperature checks

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
| ☐ | Fuse block with negative bus | Blue Sea Systems `5026` | 1 | CHF 64.40 | 12 circuits, 100 A total, 30 A per circuit, 32 V DC. Main studs are #10-32 (an M5 ring fits); branch screws are #8-32 (an M4 ring fits). Includes the cover. |
| ☐ | Molex Y-cable, pre-crimped | InLine `33445` (18 AWG, 20 cm) | 2 | CHF 13.70 | Cut off the male end to get two factory-crimped female pigtails. You need 2 pigtails; the second cable is a spare. **Must be the Y type with two separate legs, and the insulation must be printed "18AWG".** Thinner wire is not protected by the 7.5 A fuse. |
| ☐ | Blade fuse assortment | ATO/ATC, 3–30 A | 1 box | CHF 5.50 | Must include **7.5 A** and **5 A**. You need 2 of each, plus spares. |
| ☐ | Blade fuses, 1 A | ATO/ATC 1 A (black) | 1 pack | ~CHF 3.00 *est.* | For the fan circuit. Not in most assortments. |
| ☐ | Inline blade fuse holder | ATO/ATC, for 1.0 mm² / 18 AWG wire | 2 | ~CHF 5.00 *est.* | For the two +5 V leads. |
| ☐ | Lever nuts, 3-way | WAGO `221-413` (10-pack) | 1 | CHF 8.50 | You use 7: L and N splits (2), the 5 V split (1), the fuse holder splices (2) and the fan splices (2). |
| ☐ | Lever nuts, 5-way | WAGO `221-415` (pack) | 1 | ~CHF 9.00 *est.* | The PE split: inlet, both supplies, the enclosure and the 0 V–PE bond. |
| ☐ | Ferrule crimper + ferrules | Ratchet crimper kit with ~1200 ferrules | 1 | ~CHF 26.00 | Must cover 0.25–2.5 mm². |
| ☐ | Adhesive heat shrink | Quadrios `1904C053` (3:1 dual-wall) | 1 box | CHF 14.45 | Seals crimp barrels and splices. |
| ☐ | Trimming tool, insulated | Plastic or ceramic trimmer screwdriver set | 1 | ~CHF 6.00 *est.* | For the V.ADJ trimmers, which sit next to live AC terminals. **Don't use a metal screwdriver.** |
| ☐ | DC clamp meter *(recommended)* | Uni-T `UT210E` | 1 | CHF 49.50 | [Digitec](https://www.digitec.ch/de/s1/product/uni-t-ut-210e-zangenmessgeraet-5780362). Measures DC current without breaking the circuit (20 A and 100 A DC ranges, 17 mm jaw). |
| | Blade fuses with "blown" LED *(optional)* | ATO 7.5 A and 5 A, LED indicator | 2 + 2 | ~CHF 8.00 *est.* | The LED lights when the fuse has blown, so a blown fuse doesn't go unnoticed. See [design overview](01-design-overview.md#why-each-part-is-there). |
| | Mains power meter *(optional)* | Brennenstuhl `PM 231 E CH` | 1 | CHF 22.00 | [Digitec](https://www.digitec.ch/de/s1/product/brennenstuhl-primera-line-pm-231-e-energiekostenmessgeraet-273646). Plugs in between the wall and the cord and shows watts and power factor. |

**Subtotal ≈ CHF 156** (≈ CHF 205 with the clamp meter)

## Order 3: Distrelec.ch (mains side)

| ✓ | Part | Part number | Qty | Price | Notes |
|---|---|---|---|---|---|
| ☐ | Switched, fused C14 inlet | [Schurter `DD11.0121.1111`](https://www.distrelec.ch/en/inlet-c14-250v-schurter-dd11-0121-1111/p/16963541) | 1 | CHF 13.76 | 2-pole switch, takes a 2-pole fuse drawer. **Quick-connect tabs are 4.8 × 0.8 mm.** Panel mount: it goes in the enclosure's rear wall (check the cutout and panel thickness in the [DD11 datasheet](https://www.schurter.com/en/datasheet/typ_dd11.pdf)). |
| ☐ | Fuse drawer, 2-pole | [Schurter `4301.1401`](https://www.distrelec.ch/en/fuse-drawer-schurter-4301-1401/p/14323371) | 1 | CHF 6.06 | Holds two 5×20 mm fuses. |
| ☐ | Mains fuses | 5×20 mm, **6.3 A slow-blow (T)** | 2 (+2 spare) | ~CHF 2.00 *est.* | |
| ☐ | Mains cord | [Schurter `6051.2015`](https://www.distrelec.ch/en/power-cable-ch-type-t12-plug-iec-60320-c13-5m-black-schurter-6051-2015/p/11041912) | 1 | CHF 11.34 | Swiss Typ 12 plug to C13 with V-Lock. A V-Lock plug fits a normal C14 inlet; it just won't latch. **Check the length:** the shop listing says 5 m, the original notes said 2.5 m. A cord up to 5 m keeps the earth resistance within the 0.3 Ω test limit. |
| ☐ | Flat push-on receptacles, **fully insulated, 4.8 mm** | 4.8 × 0.8 mm, for 0.5–1.5 mm² (red) | 3 (+spares) | ~CHF 3.00 *est.* | For the inlet's L, N and PE tabs. **Not 6.3 mm:** a 6.3 mm receptacle sits loose on a 4.8 mm tab. |

**Subtotal ≈ CHF 36**

## Order 4: Conrad.ch (wire, terminals and fittings)

Main wire is **H07V-K 2.5 mm²** (fine-stranded, rated 450/750 V), sold by the metre. The short leads from the inlet to the WAGOs are **1.5 mm²** to fit the 4.8 mm receptacles. Behind a 6.3 A fuse that is plenty.

| ✓ | Part | Part number | Qty | Price | Notes |
|---|---|---|---|---|---|
| ☐ | Wire, brown | LAPP H07V-K 2.5 mm² | 1 m | ~CHF 1.15 | AC live (L), WAGO to supplies |
| ☐ | Wire, blue | LAPP H07V-K 2.5 mm² | 1 m | ~CHF 1.15 | AC neutral (N), WAGO to supplies |
| ☐ | Wire, green-yellow | LAPP `4520002` H07V-K 2.5 mm² | 2 m | ~CHF 2.30 | Protective earth (PE) to the supplies and the enclosure, and the 0 V–PE bond. Use this colour for nothing else. |
| ☐ | Wire, brown, blue, green-yellow | H07V-K **1.5 mm²** | 1 m each | ~CHF 2.40 *est.* | Inlet to WAGO leads |
| ☐ | Wire, yellow | LAPP H07V-K 2.5 mm² | 1 m | ~CHF 1.15 | +12 V |
| ☐ | Wire, red | LAPP `4520042` H07V-K 2.5 mm² | 1 m | ~CHF 1.15 | +5 V |
| ☐ | Wire, black | LAPP `4520012` H07V-K 2.5 mm² | 2 m | ~CHF 2.30 | V− returns and the server ground bond. Buy more if your server is further than about 1 m away. |
| ☐ | Wire, yellow and black | H05V-K 0.75 mm² | 1 m each | ~CHF 1.20 *est.* | Fan leads, fuse block to fan splices |
| ☐ | Ring terminals, M5, 1.5–2.5 mm² (blue) | e.g. Klauke, DIN 46237 | 10 | ~CHF 4.00 | Fuse block + stud (from the RSP-200-12) and − stud (from both supplies) |
| ☐ | Ring terminals, M4, 0.5–1.5 mm² (red) | e.g. Klauke, DIN 46237 | 10 | ~CHF 4.00 | 18 AWG pigtail wires and 0.75 mm² fan leads to the fuse block branch screws and negative bus |
| ☐ | Ring terminals, M4, 1.5–2.5 mm² (blue) | e.g. Klauke, DIN 46237 | 6 | ~CHF 3.00 | Both ends of the server ground bond, the bus end of the 0 V–PE bond, and the enclosure earth point |
| ☐ | Fork or ring terminals, 1.5–2.5 mm² (blue), sized for the PSU terminal screws | | 10 | ~CHF 4.00 | Mean Well terminal blocks use small (≈ M3.5) screws. **Check your unit** before ordering. Ferrules also work in these terminals. |
| ☐ | Mounting hardware | M3/M4 screws, nylon standoffs, serrated washers | 1 set | ~CHF 8.00 *est.* | Supplies and fuse block to the board, board into the enclosure, earth point (serrated washer bites through paint) |
| ☐ | Cable grommets / cable glands | for 6–10 mm openings | 4 | ~CHF 4.00 *est.* | Where the pigtails, fan leads and server bond leave the enclosure |
| ☐ | Cable ties and adhesive tie mounts | | 1 pack | ~CHF 4.00 *est.* | Strain relief |
| ☐ | Insulating sheet | Polycarbonate, 1 mm, A5 | 1 | ~CHF 5.00 *est.* | Covers the supplies' AC terminals while you trim with the lid open |

**Subtotal ≈ CHF 49**

## Order 5: Enclosure and fans (any shop)

| ✓ | Part | Part number | Qty | Price | Notes |
|---|---|---|---|---|---|
| ☐ | Enclosure, metal, vented | e.g. empty 19″ 2U case, ≥ 430 × 320 mm inside | 1 | ~CHF 80 *est.* | Takes the 420 × 300 mm board. 2U (≈ 88 mm inside) clears the 50 mm tall RSP-200-12. Needs vent holes, a removable lid and a flat rear panel for the inlet. It **must be earthed**. |
| ☐ | Fans, 120 mm, 12 V | 3-pin, ≤ 0.3 A each | 2 | ~CHF 20 *est.* | Cool the drives. Skip them if the backplane sits in a case with fans you can wire to this circuit. |

**Subtotal ≈ CHF 100**

## Total

| | Cost |
|---|---|
| Parts for the 8-drive build | **≈ CHF 400** |
| + Uni-T UT210E clamp meter | ≈ CHF 450 |
| + mains power meter | ≈ CHF 470 |

The enclosure and fans account for most of the increase over the earlier ≈ CHF 250 estimate. Don't skip the enclosure.

Next: [Electrical calculations](03-electrical-calculations.md)
