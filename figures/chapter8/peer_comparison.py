#!/usr/bin/env python3
"""Per-node peer-comparison figure for Chapter 8 (Infrastructure Defence).

Illustrates the chapter's detection intuition: the operator sees each
confidential node only through its DPU-observable metadata, but across the
cluster those per-node signals share the same training rhythm. A compromised
node stands out simply because its structural signal leaves the envelope its
peers still obey, no payload inspection required.

Layout: three node icons side by side, each with its DPU-observed egress
telemetry sparkline directly above it. Healthy peers stay inside the shared
expected envelope; the flagged (rightmost) node's trace breaks out (here, data
exfiltration filling the quiet inter-collective gaps).

The node glyphs reproduce a server-rack icon in the thesis palette (healthy in
blue with a hard hat, flagged in vermillion with small horns); each body colour
matches its sparkline. The traces are synthetic and illustrative, not measured.

Run:  python3 figures/chapter8/peer_comparison.py
Output: figures/chapter8/peer_comparison.pdf  (and .png preview)
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, FancyBboxPatch, Circle
from matplotlib.colors import to_rgb
from matplotlib.lines import Line2D
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from figures.thesis_style import (  # noqa: E402
    apply_style, BLUE, BLUE_D, VERM, VERM_D, GREEN, GREY, GREY_D,
)

apply_style()
HERE = os.path.dirname(os.path.abspath(__file__))

NODES = ["Node A", "Node B", "Node C"]
BAD = 2                                    # compromised node (rightmost)
N_ITER = 4
PPI = 160
t = np.linspace(0, N_ITER, N_ITER * PPI, endpoint=False)
phase = t % 1.0

HEALTHY = dict(body=BLUE, stroke=BLUE_D, led=GREEN, icon=BLUE_D)
FLAGGED = dict(body=VERM, stroke=VERM_D, led=VERM_D, icon=VERM_D)


def egress_template(p):
    return (0.06
            + 0.42 * np.exp(-((p - 0.60) / 0.045) ** 2)
            + 1.00 * np.exp(-((p - 0.80) / 0.050) ** 2))


def smooth(x, w=13):
    return np.convolve(x, np.ones(w) / w, mode="same")


def load_icon_halves(path):
    """Split the two-glyph icon PNG at its central gap and crop each half."""
    im = plt.imread(path)                        # (H, W, 4), float 0..1
    w = im.shape[1]
    col = im[..., 3].sum(axis=0)                 # per-column alpha mass
    lo, hi = int(w * 0.30), int(w * 0.70)
    split = lo + int(np.argmin(col[lo:hi]))

    def crop(sub):
        a = sub[..., 3]
        ys, xs = np.where(a > 0.05)
        return sub[ys.min():ys.max() + 1, xs.min():xs.max() + 1]

    return crop(im[:, :split]), crop(im[:, split:])


def tint(icon, color):
    """Recolour a glyph to a solid palette colour, preserving its alpha."""
    r, g, b = to_rgb(color)
    out = np.empty_like(icon)
    out[..., 0], out[..., 1], out[..., 2] = r, g, b
    out[..., 3] = icon[..., 3]
    return out


_worker, _devil = load_icon_halves(os.path.join(HERE, "node_icons_src.png"))
WORKER = tint(_worker, HEALTHY["icon"])
DEVIL = tint(_devil, FLAGGED["icon"])


def draw_node_icon(ax, flagged):
    """Server-rack body (SVG-style 128x128 coords, y-down) plus its glyph."""
    c = FLAGGED if flagged else HEALTHY
    ax.add_patch(FancyBboxPatch((20, 50), 88, 60,
                 boxstyle="round,pad=0,rounding_size=6",
                 fc=c["body"], ec=c["stroke"], lw=2.0, alpha=0.9, zorder=2))
    for yy in (70, 90):                          # rack seams
        ax.plot([28, 100], [yy, yy], color=c["stroke"], lw=1.4, zorder=3)
    for yy in (60, 80, 100):                     # status LEDs
        ax.add_patch(Circle((35, yy), 3, fc=c["led"], ec="none", zorder=4))
    for yy in (56, 76, 96):                      # vents
        ax.add_patch(FancyBboxPatch((70, yy), 20, 4,
                     boxstyle="round,pad=0,rounding_size=2",
                     fc=c["stroke"], ec="none", zorder=3))
    # glyph sitting on top of the server (OffsetImage never distorts aspect;
    # a single zoom keeps both glyphs at their true relative sizes)
    icon = DEVIL if flagged else WORKER
    oi = OffsetImage(icon, zoom=0.62, interpolation="antialiased")
    ab = AnnotationBbox(oi, (64, 49), xycoords="data", frameon=False,
                        box_alignment=(0.5, 0.0), pad=0.0, zorder=6,
                        annotation_clip=False)
    ax.add_artist(ab)


base = egress_template(phase)
env_hi = base * 1.18 + 0.08
env_lo = np.clip(base * 0.82 - 0.08, 0.0, None)

# ---- figure scaffold ------------------------------------------------------
fig = plt.figure(figsize=(7.4, 3.5))
gs = fig.add_gridspec(2, len(NODES), height_ratios=[0.52, 0.48],
                      hspace=0.42, wspace=0.14,
                      left=0.075, right=0.985, top=0.80, bottom=0.07)

fig.text(0.5, 0.955, "Operator observability plane",
         ha="center", va="center", fontsize=11, fontweight="bold", color=GREY_D)

for i, name in enumerate(NODES):
    bad = (i == BAD)
    rng = np.random.default_rng(100 + i)

    jit = 0.015 * rng.standard_normal()
    amp = 1.0 + 0.04 * rng.standard_normal()
    y = egress_template((t + jit) % 1.0) * amp
    y = y * (1 + 0.05 * rng.standard_normal(t.size)) + 0.015 * rng.standard_normal(t.size)
    y = np.clip(y, 0.0, None)
    if bad:
        gap = ((phase > 0.05) & (phase < 0.55)).astype(float)
        y = y + smooth(0.34 * gap, 13)

    line_c = VERM if bad else BLUE

    # ---- sparkline (on top) ----------------------------------------------
    axs = fig.add_subplot(gs[0, i])
    axs.fill_between(t, env_lo, env_hi, color=GREY, alpha=0.16, lw=0, zorder=1)
    if bad:
        out = y > env_hi
        axs.fill_between(t, env_hi, y, where=out, color=VERM, alpha=0.30,
                         interpolate=True, lw=0, zorder=2)
    axs.plot(t, y, color=line_c, lw=1.5 if bad else 1.2, zorder=4)
    axs.set_ylim(0, 1.34)
    axs.set_xlim(0, N_ITER)
    axs.set_xticks([])
    axs.set_yticks([])
    for s in ("top", "right", "left", "bottom"):
        axs.spines[s].set_visible(False)
    if i == 0:
        axs.set_ylabel("egress rate\n(normalized)", fontsize=8.5, color=GREY_D)

    # ---- node icon (below) -----------------------------------------------
    axn = fig.add_subplot(gs[1, i])
    axn.set_xlim(0, 128)
    axn.set_ylim(168, 0)               # y-down; room below icon for labels
    axn.set_aspect("equal")
    axn.axis("off")
    draw_node_icon(axn, bad)
    label_c = VERM_D if bad else GREY_D
    axn.text(64, 138, name, ha="center", va="center",
             fontsize=11, fontweight="bold", color=label_c)
    axn.text(64, 158, "TEE + BlueField DPU", ha="center", va="center",
             fontsize=8.0, color=GREY_D)

# ---- shared legend --------------------------------------------------------
handles = [
    Line2D([0], [0], color=BLUE, lw=1.6, label="Healthy node"),
    Line2D([0], [0], color=VERM, lw=1.8, label="Flagged node"),
    Patch(facecolor=GREY, alpha=0.16, label="Shared expected envelope"),
]
fig.legend(handles=handles, loc="upper center", ncol=3, frameon=False,
           fontsize=9.0, bbox_to_anchor=(0.5, 0.915))

here = os.path.dirname(os.path.abspath(__file__))
fig.savefig(os.path.join(here, "peer_comparison.pdf"))
fig.savefig(os.path.join(here, "peer_comparison.png"), dpi=160)
print("wrote peer_comparison.pdf / .png")
