# 4. Assembly Guide

Step-by-step wiring for the 8-drive build. Parts are named as in the [bill of materials](02-bill-of-materials.md).

> [!CAUTION]
> Untested design. **Keep the mains cord unplugged for this entire guide.** Read [SAFETY.md](../SAFETY.md) first.

```mermaid
flowchart LR
    S1["1 · Mount"] --> S2["2 · Pigtails"] --> S3["3 · AC wiring<br>⚠ mains"] --> S4["4 · +12 V"] --> S5["5 · +5 V"] --> S6["6 · Grounds"] --> S7["7 · Finish"] --> C(["Commissioning"])
    classDef mains fill:#fde2e1,stroke:#b42318,color:#1b1b1a
    classDef dc fill:#eef4fb,stroke:#3f7cc0,color:#1b1b1a
    class S3 mains
    class S1,S2,S4,S5,S6,S7 dc
```

The complete wiring diagram, for reference while you work:

[![Wiring diagram](images/wiring-diagram.svg)](images/wiring-diagram.svg)

## Tools

- Wire stripper for 0.5–2.5 mm²
- Ferrule crimper (from the kit) and an insulated-terminal crimper for ring and fork terminals
- Small flat screwdriver for the PSU terminals and trimmers, and a PH2 screwdriver
- 3/8″ (≈ 9.5 mm) nut driver or spanner for the Blue Sea #10-32 studs
- Heat gun. A lighter will scorch adhesive heat shrink.
- Multimeter that reads 0.01 V

## Wire colours

| Function | Colour |
|---|---|
| AC live (L) | Brown |
| AC neutral (N) | Blue |
| Protective earth (PE) | Green-yellow, and nothing else |
| +12 V | Yellow (matches the Molex pigtail) |
| +5 V | Red (matches the Molex pigtail) |
| 0 V / ground | Black |

Use a **ferrule** on every stranded wire end that goes into a lever nut or a screw clamp, and a **ring terminal** on every wire end that goes onto a stud.

---

## Step 1: Mounting

![Board layout, top view](images/board-layout.svg)

1. Mount both supplies and the Blue Sea 5026 on an **insulating board** of about **420 × 300 mm** (plywood, phenolic or acrylic). The RSP-200-12 alone is 215 × 115 mm. Leave at least 20 mm around the supplies for airflow, and face their terminal strips toward the fuse block to keep the DC runs short.
2. The Schurter inlet is a **panel-mount** part and needs a rectangular cutout in a panel (check the DD11 datasheet for the size). A small upright bracket on the board works. **If the bracket or enclosure is metal, connect it to PE.**
3. Never run the build loose on a metal desk.

Neither supply has a 115/230 V selector switch. Both accept 88–264 VAC automatically.

## Step 2: Prepare the Molex pigtails

Cut **one** InLine 33445 Y-cable just behind each of its two female connectors, so you have two female pigtails with about 20 cm of wire each. Keep the second cable as a spare. Strip 8 mm from each wire.

![Molex pigtail pin-out and termination](images/molex-pinout.svg)

> [!WARNING]
> Not every cable maker follows the colour code. **Check with the multimeter's continuity mode** that yellow really goes to pin 1 and red to pin 4, using the pin numbers moulded into the connector. The chamfered corners only stop the plug going in upside down; they don't mark pin 1.

Label one pigtail **A1** and the other **A2**.

## Step 3: AC wiring (230 VAC)

```mermaid
flowchart LR
    subgraph Inlet ["Schurter DD11 inlet"]
        IL["L"]
        IN["N"]
        IPE["PE"]
    end
    subgraph WAGO ["WAGO 221-413"]
        WL["L"]
        WN["N"]
        WPE["PE"]
    end
    subgraph LRS ["LRS-150F-5"]
        LL["L"]
        LN["N"]
        LF["FG ⏚"]
    end
    subgraph RSP ["RSP-200-12"]
        RL["L"]
        RN["N"]
        RF["FG ⏚"]
    end
    IL --> WL
    IN --> WN
    IPE --> WPE
    WL --> RL
    WL --> LL
    WN --> RN
    WN --> LN
    WPE --> RF
    WPE --> LF
    linkStyle 0,3,4 stroke:#8b4513,stroke-width:4px
    linkStyle 1,5,6 stroke:#1f6fd1,stroke-width:4px
    linkStyle 2,7,8 stroke:#2e9e3e,stroke-width:4px,stroke-dasharray:8 5
```

Brown = L, blue = N, green-yellow (dashed) = PE.

1. Fit **two 6.3 A slow-blow (T) 5×20 mm fuses** in the Schurter 4301.1401 drawer and slide it into the inlet.
2. Crimp insulated 6.3 mm push-on receptacles onto three short 2.5 mm² wires (brown, blue, green-yellow) and push them onto the inlet's **L**, **N** and **PE** tabs.
3. Put each wire into its own 3-way WAGO 221-413. From each WAGO, run one wire of the same colour to each supply:
   - brown → **L** on both supplies
   - blue → **N** on both supplies
   - green-yellow → **⏚ / FG** on both supplies
4. Tug-test every wire, then close the WAGO levers fully.
5. Fit the terminal covers on both supplies if they came with them.

## Step 4: +12 V distribution

1. Run a **yellow 2.5 mm²** wire from **RSP-200-12 V+** (fork or ring terminal) to the **positive main stud** of the Blue Sea 5026 (M5 ring terminal). Torque to the value printed on the block, about 2.7 N·m.
2. Crimp an **M4 red ring terminal** on the yellow wire of pigtail A1 and connect it to **branch 1**. Do the same with A2 on **branch 2**.
3. Insert a **7.5 A** blade fuse in positions 1 and 2. Leave all other positions empty.

## Step 5: +5 V distribution

The fuse block's bus carries only +12 V, so +5 V uses inline fuse holders:

```mermaid
flowchart LR
    P["LRS-150F-5<br>V+"] -->|"red 2.5 mm²"| W["WAGO<br>split"]
    W --> F1["5 A inline<br>fuse"] --> J1["WAGO<br>splice"] --> A1["Pigtail A1<br>pin 4 (red)"]
    W --> F2["5 A inline<br>fuse"] --> J2["WAGO<br>splice"] --> A2["Pigtail A2<br>pin 4 (red)"]
    linkStyle default stroke:#d62828,stroke-width:3px
```

1. Run a **red 2.5 mm²** wire from **LRS-150F-5 V+** to a 3-way WAGO.
2. Put one lead of each inline fuse holder into that WAGO.
3. Join each fuse holder's other lead to the red wire of one pigtail with a WAGO. One slot stays empty; close its lever anyway. A crimped butt splice under heat shrink also works.
4. Insert a **5 A** fuse in each holder.

## Step 6: Ground returns and server bond

1. Run a **black 2.5 mm²** wire from **RSP-200-12 V−** to the **negative bus stud** of the Blue Sea 5026 (M5 ring).
2. Run a **black 2.5 mm²** wire from **LRS-150F-5 V−** to the same stud.
3. Connect the **two black wires of each pigtail** (four in total) to the negative bus branch screws (M4 red rings).
4. **Server bond:** crimp a blue M4 ring onto each end of a black 2.5 mm² wire long enough to reach your server. Fit one end under a free negative bus branch screw. This end is connected to a bare-metal chassis screw on the server during [commissioning](05-commissioning-checklist.md). Scrape off paint if needed.

## Step 7: Finish

- Shrink adhesive heat shrink over every crimp barrel and splice.
- Clip on the fuse block cover.
- Strain-relieve the pigtails and the server bond wire with cable ties, so a tug on them doesn't pull on the terminals.
- Label the inlet "230 VAC".

Next: [Commissioning checklist](05-commissioning-checklist.md). Do it in full before you connect any drive.
