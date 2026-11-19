#!/usr/bin/env python3
"""Entry for make.fun's "Sum up 19 November's world news in one image" bounty.

The image is the entry: a TV-news infographic of Thursday 19 November 2026 -
the historic Trump-Xi-Putin trilateral at the APEC summit in Shenzhen,
Iran firing on U.S. sites in Kuwait, Hakeem Jeffries nominated as the first
Black Speaker, GTA VI's worldwide rollout, a markets snapshot at 19 Nov
00:00 UTC (Dow -561, Bitcoin $62,968), the EU's EUR45B Ukraine loan,
Cyclone Akvan bearing down on India, and Voyager 1 reaching one light-day
— plus a global ticker strip, so the page reads busy and worldwide. This
program does nothing but copy the finished picture beside it into the output
folder, so running it twice always writes the same bytes. No network, no
randomness, standard library only.
"""

import os
import shutil
from pathlib import Path

# The folder holding this file, so the copy works no matter where the
# harness starts the program from.
HERE = Path(__file__).resolve().parent

# The harness sets MAKEFUN_OUTPUT_DIR; without it, fall back to /output.
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")

# Say what landed, so a run's log shows the entry made it out. The copy
# itself is byte-for-byte, which is what keeps two runs identical.
print(f"Wrote entry.png to {OUT_DIR / 'entry.png'}")
