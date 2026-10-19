# Changelog

## 2026-10-19: Independent review fixes

An independent review found safety gaps on the mains side and several wrong or unverified claims. All are fixed here.

### Safety

| Was | Now | Why |
|---|---|---|
| Open board, no enclosure; inlet on "a small upright bracket" | Whole build in a closed, earthed metal enclosure (e.g. 19″ 2U case), inlet in its rear wall, grommets for the DC leads | The inlet tabs, AC lever nuts and PSU terminals carried touchable 230 VAC |
| 6.3 mm push-on receptacles for the inlet, on 2.5 mm² wire | **Fully insulated 4.8 mm** receptacles on 1.5 mm² leads | The Schurter DD11.0121.1111 has 4.8 × 0.8 mm tabs (Schurter datasheet). A 6.3 mm receptacle sits loose on them |
| Trim with "a small flat screwdriver" next to uncovered AC terminals | Insulated trimming tool, AC terminals covered (cover or polycarbonate sheet), one hand | The V.ADJ trimmers sit on the same terminal strip as L and N |
| Earth check "< 0.5 Ω" at the inlet pins with a hobby multimeter; no insulation test | ≤ 0.3 Ω at the plug pins through the cord, probes zeroed; L↔N checks; **electrician's safety test** (SNR 462638 / EN 50678) before the first plug-in; first power-on from a 30 mA RCD socket | A multimeter can't prove PE or insulation |
| JBOD 0 V earthed only through the server bond | Negative bus also bonded to PE inside the JBOD (green-yellow 2.5 mm², PE lever nut now a 5-way WAGO 221-415); "server bond before data cables, off last" | With the bond off, a 12 V fault to the server chassis would return through the SATA data cable grounds |
| No drive cooling | Two 12 V fans on fuse block position 3 (1 A), drive temperature checks (SMART 194 ≤ 45 °C) | Eight 7200 rpm drives overheat without airflow |
| "A DC short can deliver far more than 100 A", "a hard short (hundreds of amps) clears in milliseconds" | The RSP-200-12 limits a short to about 17.5–22.5 A and hiccups (105–135 %), often before the 7.5 A fuse blows; the LRS-150F-5 gives 24–31 A, which blows the 5 A fuse | Switch-mode supplies limit their current; the troubleshooting chart now says a 12 V short shows up as clicking |

### Calculations and claims

| Was | Now | Why |
|---|---|---|
| "Both headers feed the same copper planes" stated as fact | Marked unverified; commissioning measures A1 ↔ A2 | Not checked on the real backplane |
| Blown-fuse behaviour not covered | With shared planes, one blown 12 V fuse goes unnoticed, and at the next spin-up the other carries 10.16 A = 135 % of 7.5 A. Check both fuses, or use LED-indicator fuses | |
| "PWDIS is not an issue" | Holds only if the backplane makes no 3.3 V; new commissioning step D2 measures it | Not verified on the Jonsbo N3 |
| Drives see "about 12.05 V and 5.10 V" (overview) vs 11.95–12.05 / 5.05–5.10 V (calculations) | ≈ 12.0 V and 5.05 V at the spin-up peak everywhere | 12.15 − 0.159 = 11.99 V; 5.15 − 0.103 = 5.05 V |
| Commissioning expected ≈ 10 A / ≈ 3.2 A with old test drives | Expected = drives × that drive's datasheet figure, hard stop at 12.5 A, < 7.5 A per header | The HC530 figures don't apply to test drives |
| One multimeter for 12 V and 5 V minimums at once | MIN/MAX mode, one spin-up per rail | A multimeter without MIN/MAX misses the dip |
| 60 drives "over 1 kW at peak (≈ 5 A)" | ≈ 7 A at the supplies' full rating, ≈ 3 A at the real 60-drive load | The old figure mixed the two |
| "Follow NIN / SEV" | NIV/NIN cover building wiring; a self-built device is a product (NEV); plus the safety test | |
| "Cut just behind each of the two female connectors" | Cut at the male end; check the insulation says 18AWG | The old wording left no wire on the pigtails |

### Bill of materials

- Added: enclosure, fans, 1 A blade fuses, WAGO 221-415, 4.8 mm receptacles, 1.5 mm² and 0.75 mm² wire, insulated trimming tool, mounting hardware, grommets, cable ties, polycarbonate sheet, optional LED-indicator fuses. Tools needed but not supplied are now listed.
- Prices are now stated as line totals. New total **≈ CHF 400** (≈ CHF 450 with the clamp meter); the enclosure and fans account for most of the increase.

### Calculator and diagrams

- `tools/jbod_power.py`: validates its inputs (it used to crash on `--headers 0`, `--bays 0`, `--spinup-12v 0` and accept negative drive counts); never suggests a fuse above 10 A for the 18 AWG pigtails (it used to suggest 15 A for 2.5 A drives); explains the 5 A choice on +5 V; shows the one-blown-fuse case; new `--stagger` and `--extra-12v` options.
- The charts now take their figures from the calculator instead of typed-in numbers.
- Wiring diagram: 0 V–PE bond, fan circuit on fuse position 3, 1.5 mm² inlet leads, enclosure note. Board layout: inlet in the enclosure wall.

## 2026-10-19: Production drive recorded

- The production drive is the **WD Ultrastar DC HC530 14 TB SATA** (`WUH721414ALE6L4`). Its datasheet startup currents (1.27 A at 12 V, 0.47 A at 5 V) are exactly the figures the design already used, so no sizing changes.
- Corrected the note that "helium drives often list 1.8–2.0 A": the HC530 is a helium drive at 1.27 A. The real risk is **old test drives**, which often draw 2–2.8 A at spin-up.
- Commissioning now asks you to check the test drives' spin-up current, or to start with 4 drives.
- Explained that the label's "12VDC 0.57A" is running current, not spin-up.
- Documented Power Disable (PWDIS) on enterprise drives, and added it to the troubleshooting flowchart.

## 2026-10-19: Diagrams

### New diagrams (`docs/images/`, generated by `tools/diagrams/`)

- **Wiring diagram**: every wire of the 8-drive build in its real colour, from the mains inlet to the backplane, with fuse colours and the server ground bond. Shown in the README, the design overview and the assembly guide.
- **Board layout**: to-scale top view with footprints, airflow clearances and dimensions.
- **Molex pin-out**: what each pigtail wire carries, where it lands and how it is protected.
- **Spin-up current chart**: 12 V current over time against the RSP-200-12 rating and the 75 % target.
- **Voltage budget chart**: where each millivolt goes between the trimmer and the drive, for both rails.

The charts follow the viewer's light/dark setting. The wiring diagrams always use a light background so the wire colours read correctly.

### Reworked Mermaid diagrams

- AC wiring and +5 V distribution now draw each link in its wire colour.
- The ASCII-art diagrams (ground bond, +5 V split) are replaced with Mermaid.
- New: build-order strip (assembly), step strip with mains-on steps highlighted (commissioning), "what protects what" chain (design overview), troubleshooting flowchart (commissioning), and topologies for 24 and 60 drives (scaling up).

### Corrections found while drawing

| Was | Now | Why |
|---|---|---|
| 300 × 200 mm mounting board | ≈ 420 × 300 mm | The RSP-200-12 alone is 215 × 115 mm, and the three main parts plus clearances don't fit on 300 × 200 |
| "Pin 1 is at the chamfered corner" | Use the moulded pin numbers | The chamfered corners on a 4-pin Molex are keying only; they don't mark pin 1 |
| Server bond on the negative bus **stud** (M5 ring) | On a free negative bus branch screw (blue M4 ring at both ends) | Simpler, matches the diagram, and keeps the stud for the two supply returns. Blue M4 rings added to the BOM |

## 2026-10-19: Documentation overhaul

### Structure

- Docs are now numbered in reading order (`docs/01-…` to `docs/06-…`), and the README is a short landing page with a reading path.
- **Removed** `jbod_power_parts_list.md` and `jbod_power_procurement_guide.md` from the repo root. Both duplicated the procurement guide, and their links pointed to a local `file:///c:/…` path. The bill of materials is now in one place: [`docs/02-bill-of-materials.md`](docs/02-bill-of-materials.md).
- The full liability disclaimer moved from the README into [`SAFETY.md`](SAFETY.md), alongside practical safety rules.
- **New:** [`docs/05-commissioning-checklist.md`](docs/05-commissioning-checklist.md), a printable step-by-step checklist with spaces for readings.
- **New:** [`docs/test-log.md`](docs/test-log.md), a template for recording measurements so the design can be verified.
- **New:** [`docs/06-scaling-up.md`](docs/06-scaling-up.md), split out of the calculations doc and expanded.
- **New:** [`tools/jbod_power.py`](tools/jbod_power.py), a calculator for load, PSU utilisation and fuse sizing for any drive count.
- The original worksheet moved to `docs/reference/` with a warning listing its known errors.

### Corrections

| Was | Now | Why |
|---|---|---|
| RSP-500-12 powers "30 drives at 75 % load" | 24 drives at 75 % (30 drives = 91 %) | 30 × 1.27 A = 38.1 A of 41.7 A |
| RSP-200-12 "10 drives" at 75 % | 9 drives (10 = 76 %) | 10 × 1.27 A = 12.7 A of 16.7 A |
| LRS-150F-5 "36 drives" at 75 % | 35 drives | 36 × 0.47 A = 16.9 A of 22 A = 77 % |
| LRS-150F-5 "with active PFC" | No active PFC | The LRS series has no PFC; only the RSP supplies do |
| Clamp meter on the "2.000 A range" to measure a ~10 A surge | 20 A range, clamped on the single PSU-to-fuse-block feed wire | 10 A would overrange a 2 A range |
| "Total ~CHF 295, or ~345 with the clamp meter" | ≈ CHF 250, ≈ CHF 300 with the clamp meter | The CHF 295 figure already included the meter |
| Drives receive "exactly 5.00 V and 12.00 V" (README) vs "12.05 V / 5.05 V" (calculations) | One set of figures: ≈ 11.95–12.05 V and ≈ 5.05–5.10 V | The two documents contradicted each other |
| Trim "at the PSU terminals" (README) vs at the Molex (checklist) | Trim at the Molex pigtail, no load | Made consistent |
| +12 V wire listed as **black** | Yellow for +12 V, red for +5 V, black only for ground | Black on a positive rail is a wiring mistake waiting to happen |
| AC wiring used black/blue wire that wasn't in the BOM | Brown L / blue N / green-yellow PE, all in the BOM | IEC colours; BOM matches the guide |
| 5 V "ATO fuses" in the BOM but "inline fuse holders" in the wiring guide, with no holders listed | Inline blade fuse holders added to the BOM | BOM matched to the guide |
| Faston receptacles for the inlet used but not listed | Added to the BOM | |
| 8 mm socket for "M5" studs | 3/8″ nut driver; studs are #10-32 (M5 ring fits), branch screws #8-32 (M4 ring fits) | Blue Sea 5026 uses imperial hardware |
| "7.5 A or 10 A" 12 V fuse | 7.5 A | One answer; 7.5 A is the smallest rating with ≥ 1.25× margin |
| "6.3 A or 10 A" inlet fuses | 6.3 A T | One answer |
| "Order 2 Y-cables, cut to make 2 pigtails" | One Y-cable gives both pigtails; the second is a spare | Each Y-cable has two female ends |
| "Heat gun or lighter" | Heat gun | A lighter scorches adhesive heat shrink |
| "Industrial PSUs are rated for 100 % continuous duty" alongside a 75 % derating rule | The derating rule only | Contradictory |
| ATX comparison claimed all ATX PSUs need dummy loads and sag below spec | Balanced comparison | Only true of older group-regulated units |
| Server ground bond "prevents ground loops" | Establishes a common 0 V reference for isolated Mean Well outputs | More accurate |

### Design changes

- **6 mm² wire dropped for the 8-drive build.** All DC feeds, returns and the server bond now use 2.5 mm² (rated about 24 A; the largest current here is 10.2 A). That means one wire size, fewer terminal types, and no oversized ring terminals on the small PSU terminal blocks. 6 mm² comes back in the 24-drive scale-up, where the 12 V feed carries about 30 A.
- Added a pigtail pin-out continuity check, and a PE continuity check for metal brackets or enclosures.

### Still to verify (needs the datasheets or the real parts)

- Voltage-adjust range of the RSP-200-12 and RSP-500-12 (sources disagree between ±10 % and 10.0–13.2 V). Not critical, since the trim target of 12.15 V is within either range.
- PSU terminal screw size, which decides the fork/ring terminal size.
- Length of the Schurter 6051.2015 cord (2.5 m or 5 m).
- Panel cutout size of the Schurter DD11.
