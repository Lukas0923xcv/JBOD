# 1. Design Overview

How the system fits together, and why it is built this way.

## The idea

A hard drive needs two supplies: **+12 V** for the spindle motor and **+5 V** for the logic board. A JBOD backplane like the Jonsbo N3 takes both through two 4-pin Molex connectors and spreads them to all its bays.

This design uses one dedicated Mean Well supply per voltage:

| Supply | Output | Role |
|---|---|---|
| **Mean Well RSP-200-12** | 12 V, 16.7 A (200 W) | Spindle power for the 8-drive build. Active PFC, universal input, 40 A cold-start inrush at 230 VAC. |
| **Mean Well LRS-150F-5** | 5 V, 22 A (110 W) | Logic power. Universal input, no active PFC, 60 A cold-start inrush at 230 VAC. |
| **Mean Well RSP-500-12** *(scale-up)* | 12 V, 41.7 A (500 W) | Replaces the RSP-200-12 for larger arrays. Adds remote on/off and remote sense. See [Scaling up](06-scaling-up.md). |

Both supplies have a voltage-adjust trimmer (marked **V.ADJ**). It is used to set the outputs slightly high, at 12.15 V and 5.15 V, so the drives still see about 12.05 V and 5.10 V after the voltage drop in the wiring.

## System diagram

```mermaid
flowchart TD
    subgraph AC ["Mains side · 230 VAC"]
        Wall["Wall outlet<br>(Swiss Typ 13)"] --> Cord["Typ 12 → C13 cord"]
        Cord --> Inlet["Schurter DD11 inlet<br>2-pole switch + 2× 6.3 A T fuses"]
        Inlet --> WL["WAGO: L"]
        Inlet --> WN["WAGO: N"]
        Inlet --> WPE["WAGO: PE"]
    end

    WL & WN & WPE --> PSU12["RSP-200-12<br>set to 12.15 V"]
    WL & WN & WPE --> PSU5["LRS-150F-5<br>set to 5.15 V"]

    subgraph DC ["DC distribution"]
        PSU12 -->|"+12 V · 2.5 mm²"| FB["Blue Sea 5026<br>fuse block (+ bus)"]
        PSU12 -->|"V− · 2.5 mm²"| NB["Blue Sea 5026<br>negative bus"]
        PSU5 -->|"V− · 2.5 mm²"| NB
        PSU5 -->|"+5 V · 2.5 mm²"| W5["WAGO: +5 V split"]

        FB -->|"7.5 A blade fuse"| A1_12["Molex A1 · +12 V"]
        FB -->|"7.5 A blade fuse"| A2_12["Molex A2 · +12 V"]
        W5 -->|"5 A inline fuse"| A1_5["Molex A1 · +5 V"]
        W5 -->|"5 A inline fuse"| A2_5["Molex A2 · +5 V"]
        NB --> A1_G["Molex A1 · 2× GND"]
        NB --> A2_G["Molex A2 · 2× GND"]
    end

    NB ===|"2.5 mm² ground bond"| Server["Host server chassis"]

    A1_12 & A1_5 & A1_G --> BP["Jonsbo N3 backplane<br>8 bays"]
    A2_12 & A2_5 & A2_G --> BP
    BP --> HDD["8× 3.5″ SATA drives"]
    BP -. "SATA data" .-> Server
```

### Why each part is there

- **Fused, switched inlet.** One switch disconnects both supplies on both poles, and the 6.3 A slow-blow fuses protect the internal AC wiring.
- **Blue Sea 5026 fuse block.** A common +12 V bus with up to 12 blade-fuse positions, plus a negative bus in the same housing. Each Molex lead gets its own fuse, so a shorted pigtail blows only its own fuse.
- **5 V fused separately.** The fuse block has a single positive bus, so it can carry only one voltage. The 5 V leads use two inline blade-fuse holders off a lever-nut split instead.
- **Both Molex headers on one backplane come from the same pair of supplies.** On the Jonsbo N3 both headers feed the same internal 12 V and 5 V copper planes, so the current splits roughly evenly between them. **Never** feed the two headers of one backplane from two different supplies: their outputs would be tied together and would fight each other.
- **Ground bond to the server.** Mean Well supplies have isolated outputs, which means their V− terminal is not connected to earth, so the JBOD's 0 V would otherwise float relative to the server. The bond wire gives the drives and the SATA controller the same 0 V reference. Then the SATA cable ground wires never have to carry an offset current, and a static or fault charge has a proper path.

## Why not an ATX power supply?

An ATX supply works. Many JBODs run on one. This design trades a little cost and effort for some specific advantages:

| | Consumer ATX PSU | This design |
|---|---|---|
| **Fault isolation** | One short trips the whole PSU, so every drive goes offline at once | A short blows only that branch's fuse |
| **Voltage tuning** | Fixed outputs | Each rail is trimmable to make up for wiring loss |
| **Wiring** | Bulky harness with unused 24-pin, PCIe and EPS cables | Only the wires you need, sized for the job |
| **Turning on** | Needs PS_ON bridged or an adapter board | Turns on with the mains switch (the RSP-500-12 also has a remote on/off input) |
| **Rail balance** | Older group-regulated units can drift on 12 V with little 5 V load. Modern DC-DC designs don't have this problem | The rails are independent supplies |
| **Cost and effort** | Cheap, plug-and-play | More parts, and you have to wire mains yourself |

## Power-on and power-off order

The drives should be spinning before the host scans for them, and the host should be shut down cleanly before the drives lose power.

```mermaid
sequenceDiagram
    autonumber
    actor You
    participant JBOD as JBOD power (inlet switch)
    participant HDD as Drives
    participant Host as Host server

    Note over You,Host: Power-on
    You->>JBOD: Switch JBOD on
    JBOD->>HDD: 12 V and 5 V applied
    Note over HDD: Spin-up surge ≈ 10 A on 12 V<br>for about 5–10 s
    You->>Host: Power on the host
    Host->>HDD: Scan the SATA bus, mount the arrays

    Note over You,Host: Power-off
    You->>Host: Shut down the OS (flushes caches, parks heads)
    Host->>Host: Powers off
    You->>JBOD: Switch JBOD off
```

If the host is already running when you switch on the JBOD, the drives appear as hot-plugged devices. That works with most HBAs and AHCI controllers that have hot-plug enabled, but powering on first is the predictable order.

Next: [Bill of materials](02-bill-of-materials.md)
