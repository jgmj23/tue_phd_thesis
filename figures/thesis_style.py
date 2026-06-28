"""Shared matplotlib style for thesis figures.

Use for data-driven plots only; author diagrams in draw.io instead.
Enforces the Okabe-Ito colorblind-safe palette and a serif font that
matches the thesis body font (Latin Modern / Computer Modern).

Usage:
    from figures.thesis_style import apply_style, BLUE, VERM, GREEN, GREY
    apply_style()
"""
from cycler import cycler
import matplotlib.pyplot as plt

# Okabe-Ito palette (fill, dark variant for strokes/text)
BLUE,   BLUE_D   = "#0072B2", "#004C77"
VERM,   VERM_D   = "#D55E00", "#8A3D00"
GREEN,  GREEN_D  = "#009E73", "#00674C"
ORANGE, ORANGE_D = "#E69F00", "#9E6B00"
SKY,    SKY_D    = "#56B4E9", "#2C7CB0"
PURPLE, PURPLE_D = "#CC79A7", "#8E4B73"
YELLOW, YELLOW_D = "#FFD966", "#BF9000"
GREY,   GREY_D   = "#5A5A5A", "#333333"
BLACK            = "#000000"

# Categorical cycle order (avoid red/green-only contrasts)
CYCLE = [BLUE, VERM, GREEN, ORANGE, SKY, PURPLE]

GRID = "#DDDDDD"


def apply_style():
    """Apply thesis-wide matplotlib rcParams."""
    plt.rcParams.update({
        "font.family": "serif",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "legend.fontsize": 9.5,
        "mathtext.default": "regular",
        "axes.prop_cycle": cycler(color=CYCLE),
        "axes.grid": True,
        "axes.grid.axis": "y",
        "grid.color": GRID,
        "grid.linestyle": "--",
        "axes.spines.top": False,
        "axes.spines.right": False,
    })
