#!/usr/bin/env python3
"""Caesar cipher disk for Chapter 1, Section 1.1 (Foundations of Digital Trust).

Draws a two-ring Caesar cipher wheel in thesis style under a shift of k = 3. The
outer ring carries the plaintext alphabet; the inner ring carries the ciphertext
alphabet rotated by k, so reading radially inward maps each plaintext letter to
its ciphertext letter. A single mapping (A -> d) is highlighted to demonstrate
the mechanic, and the intercepted ciphertext "SDVVZRUG" is presented as a
challenge for the reader to decrypt (the plaintext is deliberately not shown).

Run:  python3 figures/chapter1/caesar_cipher.py
Output: figures/chapter1/caesar_cipher.pdf  (and .png preview)
"""
import os
import sys

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Circle, FancyArrowPatch, Rectangle

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from figures.thesis_style import apply_style, BLUE, BLUE_D, VERM, VERM_D, GREY, GREY_D, GRID, BLACK

apply_style()

# ---- parameters -----------------------------------------------------------
SHIFT = 3
PLAINTEXT = "PASSWORD"          # the answer -- deliberately NOT drawn
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CIPHERTEXT = "".join(ALPHABET[(ALPHABET.index(c) + SHIFT) % 26] for c in PLAINTEXT)

# Only one mapping (A -> d) is demonstrated on the disk; the reader decrypts
# the rest of the intercepted ciphertext themselves.
DEMO_PLAIN = "A"
DEMO_CIPHER = ALPHABET[(ALPHABET.index(DEMO_PLAIN) + SHIFT) % 26]
highlight_plain = {DEMO_PLAIN}
highlight_cipher = {DEMO_CIPHER}

# ---- geometry -------------------------------------------------------------
N = 26
step = 360.0 / N                      # angular width of one segment
half = step / 2.0
# slot i is centred at the top (90 deg) and proceeds clockwise
angles = np.array([90.0 - i * step for i in range(N)])

R_OUT_OUTER, R_OUT_INNER = 4.8, 3.8   # plaintext ring
R_IN_OUTER, R_IN_INNER = 3.8, 2.8     # ciphertext ring
r_plain_text = 4.30
r_cipher_text = 3.30

fig, ax = plt.subplots(figsize=(6.6, 7.2))

# ---- highlight wedges (worked-example letters) ----------------------------
for i, letter in enumerate(ALPHABET):
    theta = angles[i]
    t1, t2 = theta - half, theta + half
    if letter in highlight_plain:
        ax.add_patch(Wedge((0, 0), R_OUT_OUTER, t1, t2,
                           width=R_OUT_OUTER - R_OUT_INNER,
                           facecolor=BLUE, alpha=0.20, edgecolor="none", zorder=1))
    cipher_letter = ALPHABET[(i + SHIFT) % 26]
    if cipher_letter in highlight_cipher:
        ax.add_patch(Wedge((0, 0), R_IN_OUTER, t1, t2,
                           width=R_IN_OUTER - R_IN_INNER,
                           facecolor=VERM, alpha=0.20, edgecolor="none", zorder=1))

# ---- ring boundary circles ------------------------------------------------
for r in (R_OUT_OUTER, R_OUT_INNER, R_IN_INNER):
    ax.add_patch(Circle((0, 0), r, fill=False, edgecolor=GREY, lw=1.4, zorder=3))

# ---- segment dividers (spokes) --------------------------------------------
for i in range(N):
    a = np.deg2rad(angles[i] + half)
    ax.plot([R_IN_INNER * np.cos(a), R_OUT_OUTER * np.cos(a)],
            [R_IN_INNER * np.sin(a), R_OUT_OUTER * np.sin(a)],
            color=GRID, lw=0.9, zorder=2)

# ---- letters --------------------------------------------------------------
for i, letter in enumerate(ALPHABET):
    a = np.deg2rad(angles[i])
    # plaintext (outer, uppercase)
    pc = BLUE_D if letter in highlight_plain else BLACK
    pw = "bold" if letter in highlight_plain else "normal"
    ax.text(r_plain_text * np.cos(a), r_plain_text * np.sin(a), letter,
            ha="center", va="center", fontsize=14, color=pc, fontweight=pw, zorder=4)
    # ciphertext (inner, lowercase, rotated alphabet)
    cipher_letter = ALPHABET[(i + SHIFT) % 26]
    cc = VERM_D if cipher_letter in highlight_cipher else GREY_D
    cw = "bold" if cipher_letter in highlight_cipher else "normal"
    ax.text(r_cipher_text * np.cos(a), r_cipher_text * np.sin(a), cipher_letter.lower(),
            ha="center", va="center", fontsize=12.5, color=cc, fontweight=cw,
            style="italic", zorder=4)

# ---- centre hub -----------------------------------------------------------
ax.text(0, 1.05, "PLAINTEXT", ha="center", va="center", fontsize=12,
        color=BLUE_D, fontweight="bold", zorder=4)
ax.text(0, 0.30, "ciphertext", ha="center", va="center", fontsize=11,
        color=VERM_D, style="italic", zorder=4)
ax.text(0, -1.40, r"shift  $k = 3$", ha="center", va="center", fontsize=13,
        color=GREY_D, zorder=4)
ax.text(0, -2.05, r"e.g.  A $\rightarrow$ d", ha="center", va="center",
        fontsize=10.5, color=GREY_D, zorder=4)

# rotation-direction arrow (encrypt = +k, clockwise on this disk)
arrow = FancyArrowPatch((-0.95, -0.55), (0.95, -0.55),
                        connectionstyle="arc3,rad=-0.45",
                        arrowstyle="-|>", mutation_scale=16,
                        lw=1.6, color=GREY_D, zorder=4)
ax.add_patch(arrow)

# ---- intercepted-ciphertext challenge (as a two-row table) -----------------
# Row 1: the intercepted ciphertext (all an eavesdropper sees).
# Row 2: the decrypted message, left blank for the reader to recover.
n = len(CIPHERTEXT)
cell = 0.92
x_left = -n * cell / 2.0                     # left edge of the cell grid
y_row1_top = -4.85
xc = [x_left + (j + 0.5) * cell for j in range(n)]
y_row1 = y_row1_top - cell / 2.0
y_row2 = y_row1_top - cell - cell / 2.0

for j in range(n):
    # ciphertext cell (vermillion tint)
    ax.add_patch(Rectangle((x_left + j * cell, y_row1 - cell / 2.0), cell, cell,
                           facecolor=VERM, alpha=0.12, edgecolor=GREY, lw=1.2, zorder=2))
    ax.text(xc[j], y_row1, CIPHERTEXT[j].lower(), ha="center", va="center",
            fontsize=15, color=VERM_D, fontweight="bold", style="italic", zorder=3)
    # decrypted-message cell (blue tint, unknown)
    ax.add_patch(Rectangle((x_left + j * cell, y_row2 - cell / 2.0), cell, cell,
                           facecolor=BLUE, alpha=0.10, edgecolor=GREY, lw=1.2, zorder=2))
    ax.text(xc[j], y_row2, "?", ha="center", va="center",
            fontsize=15, color=BLUE_D, fontweight="bold", zorder=3)

ax.text(x_left - 0.25, y_row1, "intercepted\nciphertext", ha="right", va="center",
        fontsize=10, color=VERM_D, linespacing=1.2)
ax.text(x_left - 0.25, y_row2, "decrypted\nmessage", ha="right", va="center",
        fontsize=10, color=BLUE_D, linespacing=1.2)

# ---- frame ----------------------------------------------------------------
ax.set_xlim(-6.4, 6.4)
ax.set_ylim(-6.6, 5.2)
ax.set_aspect("equal")
ax.axis("off")
ax.grid(False)

fig.tight_layout(pad=0.3)
here = os.path.dirname(__file__)
fig.savefig(os.path.join(here, "caesar_cipher.pdf"))
fig.savefig(os.path.join(here, "caesar_cipher.png"), dpi=160)
print("wrote caesar_cipher.pdf /.png ;", PLAINTEXT, "->", CIPHERTEXT)
