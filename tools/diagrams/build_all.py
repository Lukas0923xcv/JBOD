"""Regenerates every SVG in docs/images/. Run: python3 tools/diagrams/build_all.py"""

import os
import runpy

HERE = os.path.dirname(os.path.abspath(__file__))
for script in ("wiring_diagram.py", "board_layout.py", "molex_pinout.py", "charts.py"):
    runpy.run_path(os.path.join(HERE, script), run_name="__main__")
