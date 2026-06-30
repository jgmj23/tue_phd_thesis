#!/usr/bin/env python3
r"""Distance-vs-secret-key-rate figure for Chapter 3, Section 3.3
("Distance Scaling and Quantum Repeaters").

Visualises the central claim of the section:
  * a direct / repeaterless QKD link decays EXPONENTIALLY with distance,
    bounded by the PLOB repeaterless capacity bound;
  * Twin-Field QKD (TF-QKD) improves the scaling to sqrt(eta), reaching
    ~800-1000 km but at very low (bits/s) rates;
  * only QUANTUM REPEATERS restore favourable (polynomial) scaling, lifting
    the achievable rate above the PLOB bound at long distance.

Real, WDM-compatible state-of-the-art demonstrations (CV-, DV- and TF-QKD)
are overlaid as scatter points.

Run:    python3 figures/chapter3/distance_keyrate.py
Output: figures/chapter3/distance_keyrate.pdf  (canonical, for \includegraphics)
        figures/chapter3/distance_keyrate.png  (preview only)

Data:   figures/chapter3/qkd_papers.csv  (self-contained, in-repo copy)

Bound math (PLOB / TF) reused from the author's earlier DCM-sota tool.
The PLOB and TF curves are fundamental capacity bounds; the repeater curve is
an ILLUSTRATIVE schematic of polynomial scaling, not a measured result.
"""
import os
import sys

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from figures.thesis_style import (
    apply_style,
    BLUE, BLUE_D, VERM, VERM_D, GREEN, GREEN_D,
    ORANGE, ORANGE_D, PURPLE, PURPLE_D, GREY, GREY_D,
)

apply_style()

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(HERE, "qkd_papers.csv")

REP_RATE = 1e9            # reference system clock (1 GHz) to express bounds in bits/s
FIBER_LOSS = 0.2         # dB/km, standard telecom single-mode fibre

# Protocol -> (fill color, edge color, marker)
PROTOCOL_STYLE = {
    "DV-QKD": (BLUE, BLUE_D, "o"),
    "CV-QKD": (PURPLE, PURPLE_D, "s"),
    "TF-QKD": (ORANGE, ORANGE_D, "^"),
}


def load_data(path):
    """Load the WDM-compatible QKD demonstrations dataset."""
    df = pd.read_csv(path)
    df["distance_km"] = pd.to_numeric(df["distance_km"], errors="coerce")
    df["key_rate_bps"] = pd.to_numeric(df["key_rate_bps"], errors="coerce")
    df = df.dropna(subset=["distance_km", "key_rate_bps", "protocol"])
    df = df[df["wdm_compatible"] == "Yes"]
    return df


def calculate_plob_bound(distances_km, fiber_loss_db_per_km=FIBER_LOSS):
    """PLOB (Pirandola-Laurenza-Ottaviani-Banchi) repeaterless bound.

    Secret-key capacity of a pure-loss channel: -log2(1 - eta) bits per use,
    with transmittance eta = 10^(-alpha L / 10). Expressed in bits/s using a
    1 GHz reference clock. Decays ~ linearly in eta, i.e. exponentially in L.
    """
    total_loss_db = fiber_loss_db_per_km * distances_km
    eta = 10 ** (-total_loss_db / 10)
    plob_bits_per_use = -np.log2(1 - eta + 1e-15)
    return plob_bits_per_use * REP_RATE


def calculate_tf_bound(distances_km, fiber_loss_db_per_km=FIBER_LOSS):
    """Twin-Field bound scaling as sqrt(eta) (single-repeater-like scaling).

    Replacing eta by sqrt(eta) effectively halves the loss exponent, which is
    what lets TF-QKD reach ~800-1000 km, albeit at very low rates.
    """
    total_loss_db = fiber_loss_db_per_km * distances_km
    eta = 10 ** (-total_loss_db / 10)
    sqrt_eta = np.sqrt(eta)
    tf_bits_per_use = -np.log2(1 - sqrt_eta + 1e-15)
    return tf_bits_per_use * REP_RATE


def repeater_schematic(distances_km, segment_km=100.0):
    """ILLUSTRATIVE quantum-repeater curve with polynomial scaling.

    Model: a chain of fixed-length (segment_km) elementary links. Each link sits
    at a fixed transmittance, so the per-link rate is constant; stitching N = L /
    segment_km links via entanglement swapping reduces the end-to-end rate only
    polynomially (here ~ 1/N). The result stays far above the exponentially
    decaying PLOB bound at long distance. This is a schematic, not a measurement.
    """
    seg_rate = calculate_plob_bound(np.array([segment_km]))[0]
    n_segments = np.maximum(distances_km / segment_km, 1.0)
    return seg_rate / n_segments


def main():
    df = load_data(DATA_FILE)

    fig, ax = plt.subplots(figsize=(7.0, 4.6))
    ax.set_yscale("log")

    max_dist = max(df["distance_km"].max() * 1.1, 1100)
    distances = np.linspace(1, max_dist, 600)

    plob = calculate_plob_bound(distances)
    tf = calculate_tf_bound(distances)
    rep = repeater_schematic(distances)

    y_top = 1e10
    y_bottom = 1e-1

    # Repeater-accessible region: above the PLOB repeaterless bound.
    ax.fill_between(distances, plob, y_top, color=GREEN, alpha=0.05,
                    linewidth=0, zorder=0)

    # Fundamental bounds.
    ax.plot(distances, plob, ls="--", color=GREY, lw=2.0, zorder=2,
            label="PLOB repeaterless bound")
    ax.plot(distances, tf, ls="--", color=VERM, lw=2.0, zorder=2,
            label=r"TF-QKD bound ($\sqrt{\eta}$)")

    # Illustrative repeater scaling (clearly labelled as schematic).
    rep_mask = distances >= 100.0
    ax.plot(distances[rep_mask], rep[rep_mask], ls="-.", color=GREEN_D, lw=2.0,
            zorder=2, label="Repeater scaling (illustrative)")

    # Real demonstrations.
    for protocol, (fill, edge, marker) in PROTOCOL_STYLE.items():
        subset = df[df["protocol"] == protocol]
        if subset.empty:
            continue
        ax.scatter(subset["distance_km"], subset["key_rate_bps"],
                   c=fill, marker=marker, s=95, alpha=0.9,
                   edgecolors=edge, linewidths=1.2, zorder=5)

    ax.set_xlim(0, max_dist)
    ax.set_ylim(y_bottom, y_top)
    ax.set_xlabel("Transmission distance (km)")
    ax.set_ylabel("Secret key rate (bits/s)")
    ax.grid(True, which="major", axis="both")

    # Bound-equation annotation box.
    ax.text(
        0.015, 0.035,
        r"$R_{\mathrm{PLOB}} \leq -\log_2(1-\eta)$" + "\n"
        r"$R_{\mathrm{TF}} \leq -\log_2(1-\sqrt{\eta})$" + "\n"
        r"$\eta = 10^{-\alpha L/10}$,  $\alpha = 0.2$ dB/km",
        transform=ax.transAxes, fontsize=8.5, va="bottom", ha="left",
        bbox=dict(boxstyle="round,pad=0.45", facecolor="white",
                  edgecolor=GREY, alpha=0.92),
    )

    # Legend: protocol markers + bound lines.
    marker_handles = [
        Line2D([0], [0], marker=m, color="w", markerfacecolor=fill,
               markeredgecolor=edge, markeredgewidth=1.1, markersize=8, label=p)
        for p, (fill, edge, m) in PROTOCOL_STYLE.items()
    ]
    line_handles = [
        Line2D([0], [0], ls="--", color=GREY, lw=2.0,
               label="PLOB repeaterless bound"),
        Line2D([0], [0], ls="--", color=VERM, lw=2.0,
               label=r"TF-QKD bound ($\sqrt{\eta}$)"),
        Line2D([0], [0], ls="-.", color=GREEN_D, lw=2.0,
               label="Repeater scaling (illustrative)"),
    ]
    ax.legend(handles=marker_handles + line_handles, loc="upper right",
              frameon=True, framealpha=0.95, fontsize=8.5, ncol=1)

    fig.subplots_adjust(bottom=0.13, left=0.115, right=0.97, top=0.97)
    fig.savefig(os.path.join(HERE, "distance_keyrate.pdf"))
    fig.savefig(os.path.join(HERE, "distance_keyrate.png"), dpi=160)
    print("wrote distance_keyrate.pdf / .png  ({} demonstrations)".format(len(df)))


if __name__ == "__main__":
    main()
