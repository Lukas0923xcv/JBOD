# Test Log

This design has **not been verified yet**. These measurements are what will verify it. Copy the template below for each test session, fill it in, and commit it. If a measurement disagrees with the [calculations](03-electrical-calculations.md), note it in the "Notes" field and open an issue.

---

## Session template

**Date:**
**Who:**
**Build:** (e.g. 8 drives, RSP-200-12 + LRS-150F-5, 1× Jonsbo N3)
**Drives:** (model × count; spin-up and idle current from the datasheet. Test drives or production HC530s?)
**Ambient temperature:**

### Before power-on

| Check | Result |
|---|---|
| Electrician's safety test (PE ≤ 0.3 Ω, insulation ≥ 1 MΩ, leakage ≤ 3.5 mA): pass / fail, by whom | |
| Backplane A1 ↔ A2 planes: shared or split | |
| Backplane SATA power pins at 3.3 V (step D2): none / which | |
| Test drives' datasheet spin-up current × number of drives = expected peak | |

### No-load voltages (after trimming)

| Point | 12 V | 5 V |
|---|---|---|
| Pigtail A1 | | |
| Pigtail A2 | | |

### Under load

| Measurement | Expected | Measured |
|---|---|---|
| 12 V peak current at spin-up (both yellow pigtail wires) | drives × spin-up current (8 HC530s: ≈ 10.2 A), ≤ 11.9 A | |
| 12 V peak current, A1 / A2 separately | each < 7.5 A | |
| 12 V MIN at spin-up | ≥ 11.90 V | |
| 5 V MIN | ≥ 5.00 V | |
| 12 V idle current | drives × idle current (8 HC530s: ≈ 3.2 A) | |
| Mains power at idle (if a power meter is fitted) | | |
| RSP-200-12 case temperature after 30 min | ≤ 50 °C | |
| LRS-150F-5 case temperature after 30 min | ≤ 50 °C | |
| Hottest fuse or crimp after 30 min | ≤ 50 °C | |
| Hottest drive (SMART 194) after 30 min of reading | ≤ 45 °C | |
| SMART 199 (CRC errors) before / after | no increase | |

### Result

- [ ] Pass  - [ ] Fail

**Notes:**

---

<!-- Add completed sessions below this line, newest first. -->
