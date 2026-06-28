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
    2017  20     IBM Q 20 Tokyo
    2019  53     Google Sycamore (Arute et al., Nature 574, 505 (2019))
    2021  127    IBM Eagle
    2022  433    IBM Osprey
    2023  1121   IBM Condor
    2026  ~1180  Atom Computing (1,180-atom array)
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from scipy.interpolate import interp1d

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
    ("Fowler et al.", (8, 0)),
    ("Gidney & Eker\u00e5", (8, 6)),
    ("Gidney", (-6, 12)),
    ("Pinnacle", (10, 6)),
]

hw_yr = np.array([2017, 2019, 2021, 2022, 2023, 2026])
hw_q = np.array([20, 53, 127, 433, 1121, 1180])
hw_lbl = {
    2017: ("Tokyo", (8, 0)),
    2019: ("Sycamore", (8, -12)),
    2021: ("Eagle", (8, -12)),
    2022: ("Osprey", (-20, 10)),
    2023: ("Condor", (-10, 10)),
    2026: ("Atom", (8, -12))
}

# Extrapolation target
q_day_x = 2030
q_day_q = 1e4

# ---- figure ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.4, 4.8))

# Extrapolate for shading extending back to 2011 (edge of plot)
f_req = interp1d(req_yr, np.log10(req_q), fill_value="extrapolate")
f_hw = interp1d(hw_yr, np.log10(hw_q), fill_value="extrapolate")

xs_past = np.linspace(2011, 2026, 100)
req_i_past = 10**f_req(xs_past)
hw_i_past = 10**f_hw(xs_past)

# Linear extrapolation in log space to Q-Day
f_req_fut = interp1d([2026, q_day_x], np.log10([req_q[-1], q_day_q]))
f_hw_fut = interp1d([2026, q_day_x], np.log10([hw_q[-1], q_day_q]))

xs_future = np.linspace(2026, q_day_x, 100)
req_i_fut = 10**f_req_fut(xs_future)
hw_i_fut = 10**f_hw_fut(xs_future)

xs_all = np.concatenate([xs_past, xs_future])
req_all = np.concatenate([req_i_past, req_i_fut])
hw_all = np.concatenate([hw_i_past, hw_i_fut])

ax.set_yscale("log")
ax.set_ylim(10, 2e9)
ax.grid(axis="y", linestyle="--", color="#DDDDDD", zorder=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
    
ax.fill_between(xs_all, hw_all, req_all, color=GREY, alpha=0.12, zorder=1, linewidth=0)

ax.plot(req_yr, req_q, "-o", color=VERM, mfc=VERM, mec=VERM_D, mew=1.1, lw=2.4, ms=8, zorder=5, label="Required to break RSA-2048")
ax.plot(hw_yr, hw_q, "-s", color=BLUE, mfc=BLUE, mec=BLUE_D, mew=1.1, lw=2.4, ms=7, zorder=5, label="Largest quantum processors built")
ax.plot(xs_future, req_i_fut, "--", color=VERM, lw=2.4, zorder=4, alpha=0.6)
ax.plot(xs_future, hw_i_fut, "--", color=BLUE, lw=2.4, zorder=4, alpha=0.6)

# Q-Day marker
ax.axvline(q_day_x, color=GREY, ls="--", lw=1.0, zorder=2)
ax.plot([q_day_x], [q_day_q], "ko", ms=5, zorder=6)

# Labels
for (x, y, (t, off)) in zip(req_yr, req_q, req_lbl):
    ax.annotate(t, (x, y), textcoords="offset points", xytext=off, fontsize=8.5, color=VERM_D, fontweight="bold", zorder=6)
for x, y in zip(hw_yr, hw_q):
    if x in hw_lbl:
        t, off = hw_lbl[x]
        ax.annotate(t, (x, y), textcoords="offset points", xytext=off, fontsize=8.5, color=BLUE_D, fontweight="bold", zorder=6)

ax.text(2018.3, 10 ** 4.9, "The Hardware Gap", fontsize=12, fontstyle="italic", fontweight="bold", color=GREY, ha="center", va="center", zorder=3)

# Q-Day annotations
ax.annotate("RSA-2048\nbroken", (q_day_x, q_day_q), textcoords="offset points", xytext=(15, 10),
            fontsize=9.5, color="black", fontweight="bold", zorder=7,
            arrowprops=dict(arrowstyle="->", color="black", lw=1.2, relpos=0, shrinkA=0, shrinkB=4))

# Configure axes limits
ax.set_xlim(2011, 2031)

# Draw broken axis lines
import matplotlib.transforms as mtransforms
d = .02
trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
kwargs = dict(transform=trans, color='k', clip_on=False)
ax.plot((2028 - 0.2, 2028 + 0.2), (-d, d), **kwargs)
ax.plot((2028.3 - 0.2, 2028.3 + 0.2), (-d, d), **kwargs)

ax.set_yticks([1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9])
ax.set_yticklabels(["10", "100", "1K", "10K", "100K", "1M", "10M", "100M", "1B"])
ax.yaxis.set_minor_locator(mticker.NullLocator())

ax.set_xticks([2012, 2017, 2021, 2026, 2030])
ax.set_xticklabels(["2012", "2017", "2021", "2026", '"Q-Day"'])

ax.set_ylabel("Physical qubits (log scale)")
ax.set_xlabel("Year")

ax.legend(loc="upper right", fontsize=9.5, frameon=False, ncol=1, bbox_to_anchor=(0.88, 1.0))

fig.subplots_adjust(bottom=0.15)
here = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(here, "hardware_gap.pdf"))
fig.savefig(os.path.join(here, "hardware_gap.png"), dpi=160)
print("wrote hardware_gap.pdf / .png")
