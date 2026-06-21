#!/usr/bin/env python3
"""Render the three-pillar Venn diagram for the introduction.

This mirrors the editable draw.io master (field_venn.drawio) so the thesis can
build without a manual draw.io export. Coordinates use the draw.io pixel space
(origin top-left, y increasing downward); the matplotlib y-axis is inverted to
match. Re-run after editing to regenerate field_venn.pdf:

    python3 figures/chapter1/field_venn.py
"""
import os
import tempfile

os.environ.setdefault("MPLCONFIGDIR", tempfile.mkdtemp(prefix="mpl-"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "field_venn.pdf")

# Wong colour-vision-deficiency-friendly palette (approved).
SRC, SRC_T = "#0072B2", "#004C77"   # Pillar 3: integrated photonic sources
QKD, QKD_T = "#009E73", "#00674C"   # Pillar 2: topology-aware QKD architectures
PQC, PQC_T = "#D55E00", "#8A3D00"   # Pillar 1: high-performance PQC
PATENT_FILL, PATENT_EDGE = "#FFD966", "#BF9000"

R = 200.0
CIRCLES = [
    ((300, 280), SRC),   # top-left
    ((560, 280), QKD),   # top-right
    ((430, 500), PQC),   # bottom
]

TITLES = [
    ("Integrated photonic\nsources", (107, 80), SRC_T),
    ("Topology-aware QKD\narchitectures", (782, 80), QKD_T),
    ("High-performance\npost-quantum cryptography", (425, 757), PQC_T),
]

# Papers: label -> centre (draw.io coords).
PAPERS = {
    "1": (274, 190), "2": (218, 280),          # sources
    "3": (581, 187),                            # QKD
    "4": (320, 545), "5": (470, 615), "6": (555, 550),  # PQC
    "7": (400, 340), "8": (455, 340), "9": (430, 395),  # centre (RQ4)
}

# Patents: label -> centre.
PATENTS = {
    "1": (432, 535), "2": (375, 605),  # PQC pillar
    "3": (600, 290), "4": (685, 230),  # QKD pillar
}


def main():
    fig, ax = plt.subplots(figsize=(7.2, 7.2))

    for (cx, cy), colour in CIRCLES:
        ax.add_patch(Circle((cx, cy), R, facecolor=colour, alpha=0.20,
                            edgecolor="none", zorder=1))
        ax.add_patch(Circle((cx, cy), R, facecolor="none", edgecolor=colour,
                            linewidth=2.5, alpha=0.9, zorder=2))

    for text, (x, y), colour in TITLES:
        ax.text(x, y, text, ha="center", va="center", fontsize=18,
                fontweight="bold", color=colour, zorder=5)

    for label, (x, y) in PAPERS.items():
        ax.add_patch(Circle((x, y), 16, facecolor="white", edgecolor="black",
                            linewidth=1.5, zorder=4))
        ax.text(x, y, label, ha="center", va="center", fontsize=13,
                fontweight="bold", zorder=5)

    for label, (x, y) in PATENTS.items():
        ax.scatter([x], [y], marker="*", s=1400, facecolor=PATENT_FILL,
                   edgecolor=PATENT_EDGE, linewidth=1.5, zorder=4)
        ax.text(x, y - 2, label, ha="center", va="center", fontsize=10,
                fontweight="bold", color="black", zorder=5)

    # Legend (bottom-left, clear of the circles).
    lx, ly = 95, 620
    ax.add_patch(Circle((lx, ly), 11, facecolor="white", edgecolor="black",
                        linewidth=1.5, zorder=4))
    ax.text(lx + 22, ly, "Papers", ha="left", va="center", fontsize=13, zorder=5)
    ax.scatter([lx], [ly + 34], marker="*", s=420, facecolor=PATENT_FILL,
               edgecolor=PATENT_EDGE, linewidth=1.5, zorder=4)
    ax.text(lx + 22, ly + 34, "Patents", ha="left", va="center", fontsize=13,
            zorder=5)

    ax.set_xlim(0, 850)
    ax.set_ylim(810, 10)  # inverted -> draw.io-style top-left origin
    ax.set_aspect("equal")
    ax.axis("off")

    fig.savefig(OUT, bbox_inches="tight", pad_inches=0.05)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
