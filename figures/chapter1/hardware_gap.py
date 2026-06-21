#!/usr/bin/env python3
"""Hardware-gap figure for Chapter 1, Section 1.2.2 (The Hardware Gap).

Dual-trend ("scissor") chart contrasting the falling resource estimate for
factoring RSA-2048 against the rising size of the largest demonstrated
gate-model quantum processors. The shaded region between the two trends is the
"hardware gap".

Run:  python3 figures/chapter1/hardware_gap.py
Output: figures/chapter1/hardware_gap.pdf  (and .png preview)

Data / sources:
  Required physical qubits to factor RSA-2048 (fault-tolerant estimates):
    2012  ~1e9   Fowler et al., Phys. Rev. A 86, 032324 (2012)
    2019  2e7    Gidney & Ekera, Quantum 5, 433 (2021) ("20 million noisy qubits")
    2025  1e6    Gidney, arXiv:2505.15917 ("< 1 million noisy qubits")
    2026  ~9.8e4 Webster et al. (Pinnacle), arXiv:2602.11457 ("< 100k qubits")
  Largest demonstrated gate-model processors (noisy physical qubits):
    2001  7      IBM NMR, Shor factoring of 15
    2017  20     IBM Q 20 Tokyo
    2019  53     Google Sycamore (Arute et al., Nature 574, 505 (2019))
    2021  127    IBM Eagle
    2022  433    IBM Osprey
    2023  1121   IBM Condor (1,180-atom array, Atom Computing, same year)
    2026  ~1180  largest counts remain ~10^3 (field pivoted to fidelity/logical)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.patches import FancyArrowPatch

# Okabe-Ito palette, consistent with figures/chapter1/field_venn.drawio
BLUE, BLUE_D = "#0072B2", "#004C77"     # achieved hardware
VERM, VERM_D = "#D55E00", "#8A3D00"     # required to break RSA-2048
GREY = "#5A5A5A"

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "mathtext.default": "regular",
})

# ---- data -----------------------------------------------------------------
req_yr = np.array([2012, 2019, 2025, 2026])
req_q = np.array([1e9, 2e7, 1e6, 9.8e4])
req_lbl = [
    ("$\\sim$1 billion (Fowler et al.)", (8, 8)),
    ("20 M (Gidney & Eker\u00e5)", (8, 9)),
    ("$<$1 M (Gidney)", (-6, 12)),
    ("$<$100 K (Pinnacle)", (10, 6)),
]

hw_yr = np.array([2001, 2017, 2019, 2021, 2022, 2023, 2026])
hw_q = np.array([7, 20, 53, 127, 433, 1121, 1180])
hw_lbl = {2001: ("7 (Shor on NMR)", (8, -16)),
          2021: ("127 (Eagle)", (-10, -18)),
          2023: ("1,121 (Condor)", (-6, 9))}

# ---- figure ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.4, 4.8))

ax.set_yscale("log")
ax.set_ylim(2, 4e9)
ax.set_xlim(2000, 2028)
ax.set_yticks([1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9])
ax.set_yticklabels(["1", "10", "100", "1K", "10K", "100K", "1M", "10M", "100M", "1B"])
ax.yaxis.set_minor_locator(mticker.NullLocator())
ax.set_xticks([2001, 2007, 2013, 2019, 2025])
ax.grid(axis="y", linestyle="--", color="#DDDDDD", zorder=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)

# shaded "hardware gap" between the two trends (2012 -> 2026)
xs = np.linspace(2012, 2026, 200)
req_i = 10 ** np.interp(xs, req_yr, np.log10(req_q))
hw_i = 10 ** np.interp(xs, hw_yr, np.log10(hw_q))
ax.fill_between(xs, hw_i, req_i, color=GREY, alpha=0.12, zorder=1, linewidth=0)
ax.text(2016.3, 10 ** 4.0, "Hardware gap", fontsize=12, fontstyle="italic",
        fontweight="bold", color=GREY, ha="center", va="center", rotation=-18, zorder=3)

# required trend (falling)
ax.plot(req_yr, req_q, "-o", color=VERM, mfc=VERM, mec=VERM_D, mew=1.1,
        lw=2.4, ms=8, zorder=5, label="Required to break RSA-2048")
for (x, y, (t, off)) in zip(req_yr, req_q, req_lbl):
    ax.annotate(t, (x, y), textcoords="offset points", xytext=off,
                fontsize=8.5, color=VERM_D, fontweight="bold", zorder=6)

# achieved trend (rising)
ax.plot(hw_yr, hw_q, "-s", color=BLUE, mfc=BLUE, mec=BLUE_D, mew=1.1,
        lw=2.4, ms=7, zorder=5, label="Largest quantum processors built")
for x, y in zip(hw_yr, hw_q):
    if x in hw_lbl:
        t, off = hw_lbl[x]
        ax.annotate(t, (x, y), textcoords="offset points", xytext=off,
                    fontsize=8.5, color=BLUE_D, fontweight="bold", zorder=6)

# "today" marker + explicit gap arrow at 2026
ax.axvline(2026, color=GREY, ls=(0, (2, 3)), lw=1.0, zorder=2)
ax.text(2026, 2.6e9, "today", fontsize=8.5, color=GREY, ha="center",
        va="bottom", fontstyle="italic")
arr = FancyArrowPatch((2026.8, 1180), (2026.8, 9.8e4), arrowstyle="<->",
                      mutation_scale=12, color=GREY, lw=1.8, zorder=6)
ax.add_patch(arr)

ax.set_ylabel("Physical qubits (log scale)")
ax.set_xlabel("Year")
ax.legend(loc="center left", fontsize=9.5, frameon=False,
          bbox_to_anchor=(0.02, 0.62), ncol=1)

plt.tight_layout()
here = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(here, "hardware_gap.pdf"))
fig.savefig(os.path.join(here, "hardware_gap.png"), dpi=160)
print("wrote hardware_gap.pdf / .png")
