#!/usr/bin/env python3
r"""Spontaneous four-wave mixing (SFWM) resonance-comb figure for Chapter 3,
Section 3.2 ("Nonlinear Optics and Four-Wave Mixing").

Visualises how a microring source produces frequency-bin entangled pairs:
  * the ring supports a comb of resonances spaced by the free spectral range
    (FSR);
  * a continuous-wave pump sits on the central resonance (omega_p);
  * SFWM annihilates two pump photons and creates a signal (omega_s) and an
    idler (omega_i) photon on resonances placed SYMMETRICALLY about the pump,
    enforcing energy conservation  omega_s + omega_i = 2 omega_p;
  * the phase-matching / dispersion envelope sets how many symmetric bin pairs
    receive appreciable gain, i.e. the dimensionality of the frequency-bin
    entangled state.

Run:    python3 figures/chapter3/sfwm_comb.py
Output: figures/chapter3/sfwm_comb.pdf  (canonical, for \includegraphics)
        figures/chapter3/sfwm_comb.png  (preview only)
"""
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from figures.thesis_style import (
    apply_style, BLUE, BLUE_D, ORANGE, ORANGE_D, GREEN, GREEN_D, GREY, GREY_D,
)

apply_style()

HERE = os.path.dirname(os.path.abspath(__file__))

N_SIDE = 4              # resonances on each side of the pump
FSR = 1.0               # free spectral range (frequency axis is in FSR units)
LINEWIDTH = 0.10        # resonance HWHM in FSR units (high-Q -> narrow)
ENV_WIDTH = 2.6         # phase-matching envelope half-width in FSR units


def lorentzian(x, x0, gamma):
    return gamma**2 / ((x - x0) ** 2 + gamma**2)


def main():
    orders = np.arange(-N_SIDE, N_SIDE + 1)
    centers = orders * FSR

    x = np.linspace(-(N_SIDE + 0.6), N_SIDE + 0.6, 4000)

    # Phase-matching / SFWM-gain envelopes for different dispersion engineering.
    envelope1 = np.exp(-(x ** 2) / (2 * (ENV_WIDTH * 0.5) ** 2))
    envelope2 = np.exp(-(x ** 2) / (2 * ENV_WIDTH ** 2))
    envelope3 = np.exp(-(x ** 2) / (2 * (ENV_WIDTH * 1.5) ** 2))

    # Resonance comb, each peak weighted by the envelope2 at its center (as before).
    comb = np.zeros_like(x)
    for c in centers:
        comb += np.exp(-(c ** 2) / (2 * ENV_WIDTH ** 2)) * lorentzian(x, c, LINEWIDTH)

    fig, ax = plt.subplots(figsize=(7.4, 4.2))

    # Dispersion / phase-matching envelopes.
    ax.plot(x, envelope1, ls="--", color=GREY, lw=1.2, zorder=2, alpha=0.5)
    ax.plot(x, envelope2, ls="--", color=GREY, lw=1.8, zorder=2)
    ax.plot(x, envelope3, ls="--", color=GREY, lw=1.2, zorder=2, alpha=0.5)
    ax.fill_between(x, 0, envelope2, color=GREY, alpha=0.06, zorder=0)
    ax.text(N_SIDE + 0.55, 1.20,
            r"phase-matching" "\n" r"envelopes ($\Delta k$)", color=GREY_D, fontsize=9, style="italic",
            ha="right", va="bottom")

    # Colour map: pump (centre), signal (+ orders, green), idler (- orders, orange).
    def peak_color(n):
        if n == 0:
            return BLUE, BLUE_D
        return (GREEN, GREEN_D) if n > 0 else (ORANGE, ORANGE_D)

    for n, c in zip(orders, centers):
        single = np.exp(-(c ** 2) / (2 * ENV_WIDTH ** 2)) * lorentzian(x, c, LINEWIDTH)
        fill, edge = peak_color(n)
        ax.fill_between(x, 0, single, color=fill, alpha=0.85, linewidth=0, zorder=3)
        ax.plot(x, single, color=edge, lw=1.0, zorder=4)

    # Pump label.
    ax.annotate(r"pump $\omega_p$", xy=(0, 1.0), xytext=(0, 1.17),
                ha="center", va="bottom", color=BLUE_D, fontsize=11,
                arrowprops=dict(arrowstyle="-", color=BLUE_D, lw=1.2))

    # Signal / idler bin labels (first pair).
    ax.text(1.0, np.exp(-1 / (2 * ENV_WIDTH ** 2)) + 0.05, r"signal $\omega_s$",
            color=GREEN_D, fontsize=10.5, ha="center", va="bottom")
    ax.text(-1.0, np.exp(-1 / (2 * ENV_WIDTH ** 2)) + 0.05, r"idler $\omega_i$",
            color=ORANGE_D, fontsize=10.5, ha="center", va="bottom")

    # FSR spacing annotation between two adjacent resonances on the right.
    y_fsr = 0.30
    ax.annotate("", xy=(3.0, y_fsr), xytext=(2.0, y_fsr),
                arrowprops=dict(arrowstyle="<->", color=GREY_D, lw=1.3))
    ax.text(2.5, y_fsr + 0.03, "FSR", ha="center", va="bottom",
            color=GREY_D, fontsize=10)

    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(0, 1.32)
    ax.set_xlabel(r"Frequency detuning from pump  (units of FSR)")
    ax.set_ylabel("Cavity resonance / emission (a.u.)")
    ax.set_yticks([])
    ax.set_xticks(orders)
    ax.grid(False)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)

    fig.subplots_adjust(bottom=0.15, left=0.06, right=0.985, top=0.97)
    fig.savefig(os.path.join(HERE, "sfwm_comb.pdf"))
    fig.savefig(os.path.join(HERE, "sfwm_comb.png"), dpi=160)
    print("wrote sfwm_comb.pdf / .png")


if __name__ == "__main__":
    main()
