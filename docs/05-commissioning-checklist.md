# 5. Commissioning Checklist

Print this and tick each box. **Stop at the first failure** and fix it before you go on. Record your readings in the [test log](test-log.md).

> [!CAUTION]
> The cord stays **unplugged** for parts A and B. Read [SAFETY.md](../SAFETY.md) first.

## A. Visual check (unplugged)

- [ ] No loose copper strands near any terminal
- [ ] Every ferrule and ring terminal crimped tight. Tug-test each wire.
- [ ] Stud nuts and terminal screws tight
- [ ] Colours match the [assembly guide](04-assembly-guide.md#wire-colours): brown L, blue N, green-yellow PE
- [ ] Fuses fitted: 2 × 6.3 A T in the inlet, 2 × 7.5 A in the fuse block, 2 × 5 A inline
- [ ] **No drives and no backplane connected**

## B. Resistance checks (unplugged, multimeter in Ω mode)

| ✓ | Measure between | Expect | Reading |
|---|---|---|---|
| ☐ | Inlet PE pin ↔ RSP-200-12 metal case | < 0.5 Ω | |
| ☐ | Inlet PE pin ↔ LRS-150F-5 metal case | < 0.5 Ω | |
| ☐ | Inlet PE pin ↔ metal bracket or enclosure (if any) | < 0.5 Ω | |
| ☐ | Inlet L pin ↔ PE pin (switch **on**) | open / very high | |
| ☐ | Inlet N pin ↔ PE pin (switch **on**) | open / very high | |
| ☐ | Pigtail A1: pin 1 (12 V) ↔ pin 2 (GND) | not a short (it will charge slowly through the PSU) | |
| ☐ | Pigtail A1: pin 4 (5 V) ↔ pin 2 (GND) | not a short | |
| ☐ | Pigtail A2: same two checks | not a short | |

## C. First power-on, no load

- [ ] Plug in the cord and switch the inlet **on**
- [ ] Both green **DC-OK** LEDs light
  - If not: switch off, unplug, and check the inlet fuses and the AC wiring
- [ ] No smell, no noise other than a faint whine, nothing gets warm

## D. Trim the voltages (no load)

Measure at the **pigtail connector** with the multimeter in DC V:

| ✓ | Rail | Probe on pins | Turn trimmer | Target | Reading |
|---|---|---|---|---|---|
| ☐ | +12 V, A1 | 1 (+) and 2 (−) | **V.ADJ** on RSP-200-12 | **12.15 V** | |
| ☐ | +12 V, A2 | 1 and 2 | (no adjustment, check only) | 12.15 V ± 0.02 | |
| ☐ | +5 V, A1 | 4 (+) and 3 (−) | **V.ADJ** on LRS-150F-5 | **5.15 V** | |
| ☐ | +5 V, A2 | 4 and 3 | (no adjustment, check only) | 5.15 V ± 0.02 | |

- [ ] Switch off, **unplug**, and wait 1 minute until both LEDs are dark

## E. First spin-up (8 test drives)

1. [ ] Plug both pigtails into the backplane's **A1** and **A2** headers
2. [ ] Insert the test drives
3. [ ] Connect the **server bond wire** to the server chassis. The server can stay off for this test.
4. [ ] Set the clamp meter to **DC A, 20 A range** and **zero it** (press ZERO with the jaws closed and away from wires). Clamp it around the **yellow 2.5 mm² wire from the RSP-200-12 to the fuse block**. That one wire carries the whole 12 V load.
5. [ ] Put the multimeter on a spare drive's power connector, or on the back of pigtail A1 pins 1–2
6. [ ] Plug in and switch on, then watch:

| ✓ | Check | Expect | Reading |
|---|---|---|---|
| ☐ | 12 V current during spin-up (highest reading) | ≈ 10 A, must stay below 16.7 A | |
| ☐ | 12 V lowest voltage during spin-up | ≥ 11.90 V | |
| ☐ | 5 V voltage | ≥ 5.00 V | |
| ☐ | 12 V current after ~15 s (idle) | ≈ 3–3.5 A | |
| ☐ | All drives spin up (listen, or check the activity LEDs) | 8 / 8 | |
| ☐ | PSU case temperature after 30 min | warm to the touch, not hot | |

The meter updates only a few times per second, so it may read slightly below the true spin-up peak.

## F. Host test

1. [ ] Connect SATA data cables to the host
2. [ ] Power on in order: **JBOD first**, wait ~15 s, then the host (see [power-on order](01-design-overview.md#power-on-and-power-off-order))
3. [ ] All 8 drives detected, and SMART shows no new CRC errors (`smartctl -A /dev/sdX`, attribute 199)

✅ **Commissioning complete.** Fill in the [test log](test-log.md).
