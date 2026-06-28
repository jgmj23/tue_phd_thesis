#!/usr/bin/env python3
"""Q-Day expert-likelihood figure for Chapter 1, Section 1.2.1 (Q-Day).

Redraws, in thesis style, the averaged expert likelihood estimates for a
quantum computer able to break RSA-2048 within 24 hours, as a function of the
time horizon. Two interpretations of the survey responses (optimistic and
pessimistic) bound a shaded uncertainty band.

Run:  python3 figures/chapter1/qday_timeline.py
Output: figures/chapter1/qday_timeline.pdf  (and .png preview)

Data / source:
  Mosca & Piani, "Quantum Threat Timeline Report 2025",
  Global Risk Institute / evolutionQ (2026). Averaged likelihood that a CRQC
  can break RSA-2048 in 24 hours, by horizon:
       5y   10y   15y   20y   30y
  opt  15%   49%   70%   86%   93%
  pess  5%   28%   51%   69%   81%
  (The 25-year horizon was not explicitly surveyed, so 20y and 30y are
  connected directly.)
"""
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from figures.thesis_style import apply_style, VERM, VERM_D, BLUE, BLUE_D, GREY

apply_style()

# ---- data -----------------------------------------------------------------
years = np.array([5, 10, 15, 20, 30])
optimistic = np.array([15, 49, 70, 86, 93])
pessimistic = np.array([5, 28, 51, 69, 81])

# ---- figure ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.0, 4.4))

ax.fill_between(years, pessimistic, optimistic, color=GREY, alpha=0.12,
                linewidth=0, zorder=1)

ax.plot(years, optimistic, "-v", color=VERM, mfc=VERM, mec=VERM_D, mew=1.1,
        lw=2.4, ms=8, zorder=5, label="Optimistic interpretation")
ax.plot(years, pessimistic, "-s", color=BLUE, mfc=BLUE, mec=BLUE_D, mew=1.1,
        lw=2.4, ms=7, zorder=5, label="Pessimistic interpretation")

# value labels
for x, y in zip(years, optimistic):
    ax.annotate(f"{y}%", (x, y), textcoords="offset points", xytext=(0, 9),
                ha="center", fontsize=8.5, color=VERM_D, fontweight="bold",
                zorder=6)
for x, y in zip(years, pessimistic):
    # keep the lowest label off the x-axis by placing it to the side
    if y < 10:
        xytext, ha = (12, -4), "left"
    else:
        xytext, ha = (0, -15), "center"
    ax.annotate(f"{y}%", (x, y), textcoords="offset points", xytext=xytext,
                ha=ha, fontsize=8.5, color=BLUE_D, fontweight="bold",
                zorder=6)

# even-odds reference line
ax.axhline(50, color=GREY, ls=":", lw=1.0, zorder=2)
ax.annotate("even odds", (5.2, 50), textcoords="offset points", xytext=(0, 4),
            fontsize=8.5, fontstyle="italic", color=GREY, zorder=3)

ax.set_xlim(3.5, 31.5)
ax.set_ylim(0, 100)
ax.set_xticks([5, 10, 15, 20, 25, 30])
ax.set_xticklabels(["5", "10", "15", "20", "25", "30"])
ax.yaxis.set_major_formatter(mticker.PercentFormatter(decimals=0))
ax.set_xlabel("Threat horizon (years from now)")
ax.set_ylabel("Average expert likelihood")

ax.legend(loc="lower right", fontsize=9.5, frameon=False)

fig.subplots_adjust(bottom=0.15, left=0.12, right=0.97, top=0.96)
here = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(here, "qday_timeline.pdf"))
fig.savefig(os.path.join(here, "qday_timeline.png"), dpi=160)
print("wrote qday_timeline.pdf / .png")
