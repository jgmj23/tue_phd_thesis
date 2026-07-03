#!/usr/bin/env python3
r"""Dual-coupled microring (DCM) source figure for Chapter 3,
Section 3.3 ("Microring Entanglement Sources").

Two stacked panels, each pairing a small ring schematic with its transmission
spectrum:

  (a) Single microring: a main ring side-coupled to a bus waveguide produces an
      evenly spaced comb of resonance notches (transmission T_a). A pump on one
      resonance seeds signal/idler pairs on the symmetric resonances; three
      consecutive comb lines are labelled I (idler), k (k-th line), S (signal).

  (b) Dual-coupled microring: an auxiliary ring (tuned by a micro-heater,
      detuning Delta) is coupled to the main ring with strength kappa. The extra
      cavity reshapes the response -- the main-ring resonances split / are
      reshaped (T_a) and the auxiliary comb (T_b, dashed) interferes with them,
      giving the two control knobs (kappa, Delta) that map device physics to
      network-facing metrics.

Run:    python3 figures/chapter3/dcm_source.py
Output: figures/chapter3/dcm_source.pdf  (canonical, for \includegraphics)
        figures/chapter3/dcm_source.png  (preview only)
"""
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Circle, FancyArrowPatch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from figures.thesis_style import (
    apply_style, BLUE, BLUE_D, SKY, SKY_D, GREY, GREY_D,
)

apply_style()

HERE = os.path.dirname(os.path.abspath(__file__))

N_SIDE = 4                 # comb lines on each side of centre
FSR = 1.0                  # free spectral range (frequency axis in FSR units)
WIDTH = 0.055              # resonance HWHM in FSR units (high-Q -> narrow)
DEPTH = 0.92               # notch depth
SPLIT = 0.14               # main-ring mode splitting from inter-ring coupling
DETUNE = 0.32              # auxiliary-ring detuning (Delta) in FSR units


def lorentz(x, x0, w):
    return 1.0 / (1.0 + ((x - x0) / w) ** 2)


def single_transmission(x, centers):
    dips = np.zeros_like(x)
    for c in centers:
        dips += DEPTH * lorentz(x, c, WIDTH)
    return 1.0 - np.clip(dips, 0, DEPTH)


def dual_transmission(x, centers):
    """Main-ring transmission with each resonance split into a doublet."""
    dips = np.zeros_like(x)
    for c in centers:
        dips += 0.55 * lorentz(x, c - SPLIT, WIDTH * 0.85)
        dips += 0.55 * lorentz(x, c + SPLIT, WIDTH * 0.85)
    return 1.0 - np.clip(dips, 0, 0.92)


def aux_transmission(x, centers):
    """Auxiliary-ring comb, detuned by Delta (shallower, dashed)."""
    dips = np.zeros_like(x)
    for c in centers:
        dips += 0.6 * lorentz(x, c + DETUNE, WIDTH * 1.1)
    return 1.0 - np.clip(dips, 0, 0.7)


# ---------------------------------------------------------------------------
# Ring schematics (drawn on equal-aspect axes with data coords in [0, 1]).
# ---------------------------------------------------------------------------
def bus_with_ports(ax, y):
    ax.plot([0.04, 0.96], [y, y], color=GREY, lw=3.0, solid_capstyle="round",
            zorder=1)
    ax.add_patch(FancyArrowPatch((0.0, y), (0.06, y), arrowstyle="-|>",
                 mutation_scale=11, color=BLUE_D, lw=2.0, zorder=2))
    ax.add_patch(FancyArrowPatch((0.94, y), (1.0, y), arrowstyle="-|>",
                 mutation_scale=11, color=GREEN if False else BLUE_D, lw=2.0,
                 zorder=2))
    ax.text(0.02, y - 0.05, r"$\omega_p$", color=BLUE_D, fontsize=10,
            ha="left", va="top")
    ax.text(0.98, y - 0.05, r"$\omega_s,\omega_i$", color=BLUE_D, fontsize=10,
            ha="right", va="top")


def draw_single_ring(ax):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    y_bus = 0.16
    r = 0.30
    cy = y_bus + r
    ax.add_patch(Circle((0.5, cy), r, facecolor="none", edgecolor=BLUE_D,
                 lw=3.2, zorder=2))
    bus_with_ports(ax, y_bus)
    ax.text(0.5, cy, "main\nring", color=BLUE_D, fontsize=9.5, ha="center",
            va="center")


def draw_dual_ring(ax):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect("equal")
    ax.axis("off")
    y_bus = 0.10
    r_main = 0.235
    cy_main = y_bus + r_main
    r_aux = 0.20
    cy_aux = cy_main + r_main + r_aux

    # main ring (tangent to the bus waveguide)
    ax.add_patch(Circle((0.5, cy_main), r_main, facecolor="none",
                 edgecolor=BLUE_D, lw=3.2, zorder=2))
    bus_with_ports(ax, y_bus)
    ax.text(0.5, cy_main, "main", color=BLUE_D, fontsize=9, ha="center",
            va="center")

    # auxiliary ring (tangent to the main ring)
    ax.add_patch(Circle((0.5, cy_aux), r_aux, facecolor="none",
                 edgecolor=SKY_D, lw=3.2, zorder=2))
    ax.text(0.5, cy_aux, "aux", color=SKY_D, fontsize=9, ha="center",
            va="center")


def main():
    orders = np.arange(-N_SIDE, N_SIDE + 1)
    centers = orders * FSR
    x = np.linspace(-(N_SIDE + 0.5), N_SIDE + 0.5, 6000)

    fig = plt.figure(figsize=(7.4, 5.0))
    gs = GridSpec(2, 2, width_ratios=[1.0, 3.4], height_ratios=[1, 1],
                  wspace=0.34, hspace=0.32, left=0.02, right=0.985,
                  bottom=0.11, top=0.93)

    ax_s_ring = fig.add_subplot(gs[0, 0])
    ax_s_spec = fig.add_subplot(gs[0, 1])
    ax_d_ring = fig.add_subplot(gs[1, 0])
    ax_d_spec = fig.add_subplot(gs[1, 1])

    # ---- Panel (a): single ring --------------------------------------------
    draw_single_ring(ax_s_ring)
    Ta = single_transmission(x, centers)
    ax_s_spec.plot(x, Ta, color=BLUE, lw=2.0, zorder=3, label=r"$T_a$")
    _style_spec(ax_s_spec, orders, show_xlabel=False)
    ax_s_spec.legend(loc="lower right", frameon=False, handlelength=1.6)

    # label three consecutive comb lines I / k / S
    for xc, lab in [(-1, "I"), (0, r"$k$"), (1, "S")]:
        ax_s_spec.annotate(lab, xy=(xc, 0.02), xytext=(xc, -0.13),
                           ha="center", va="top", fontsize=11, color=GREY_D,
                           annotation_clip=False)

    # ---- Panel (b): dual-coupled ring --------------------------------------
    draw_dual_ring(ax_d_ring)
    Ta_d = dual_transmission(x, centers)
    Tb_d = aux_transmission(x, centers)
    ax_d_spec.plot(x, Tb_d, color=SKY, lw=1.6, ls="--", zorder=2,
                   label=r"$T_b$ (aux)")
    ax_d_spec.plot(x, Ta_d, color=BLUE, lw=2.0, zorder=3, label=r"$T_a$ (main)")
    _style_spec(ax_d_spec, orders, show_xlabel=True)
    ax_d_spec.legend(loc="lower right", frameon=False, handlelength=1.8,
                     ncol=2, columnspacing=1.2)

    # panel letters
    fig.text(0.015, 0.955, "(a)", fontsize=13, fontweight="bold",
             color=GREY_D)
    fig.text(0.015, 0.475, "(b)", fontsize=13, fontweight="bold",
             color=GREY_D)

    fig.savefig(os.path.join(HERE, "dcm_source.pdf"))
    fig.savefig(os.path.join(HERE, "dcm_source.png"), dpi=160)
    print("wrote dcm_source.pdf / .png")


def _style_spec(ax, orders, show_xlabel):
    ax.set_xlim(-(N_SIDE + 0.5), N_SIDE + 0.5)
    ax.set_ylim(0, 1.12)
    ax.set_xticks(orders)
    ax.set_yticks([0, 1])
    ax.set_ylabel("Transmission")
    ax.grid(False)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    if show_xlabel:
        ax.set_xlabel(r"Frequency detuning from pump  (units of FSR)")
    else:
        ax.set_xticklabels([])


if __name__ == "__main__":
    main()
