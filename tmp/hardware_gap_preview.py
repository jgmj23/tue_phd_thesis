import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/mpl")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

# Okabe-Ito palette (matches field_venn.drawio)
BLUE = "#0072B2"
BLUE_D = "#004C77"
VERM = "#D55E00"
VERM_D = "#8A3D00"

labels = ["IBM Condor\n(superconducting)", "Neutral-atom\narrays",
          "Next-gen qLDPC\nprojection", "Noisy estimate\n(2025)",
          "Original estimate\n(2019)"]
values = [1121, 1000, 100000, 1000000, 20000000]
toplabels = ["1,121", "~1,000", "<100K", "<1M", "~20M"]
colors = [BLUE, BLUE, VERM, VERM, VERM]
edges = [BLUE_D, BLUE_D, VERM_D, VERM_D, VERM_D]
x = [0, 1, 2.6, 3.6, 4.6]

fig, ax = plt.subplots(figsize=(8.2, 5.0))
ax.bar(x, values, width=0.7, color=colors, edgecolor=edges, linewidth=1.3, alpha=0.9, zorder=3)
ax.set_yscale("log")
ax.set_ylim(100, 2e8)
ax.set_xlim(-0.6, 5.3)

for xi, v, t in zip(x, values, toplabels):
    ax.text(xi, v * 1.25, t, ha="center", va="bottom", fontsize=10, fontweight="bold",
            color=BLUE_D if v < 1e4 else VERM_D)

ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=9)
ax.set_ylabel("Physical qubits (log scale)", fontsize=12)
ax.set_yticks([1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8])
ax.set_yticklabels(["100", "1K", "10K", "100K", "1M", "10M", "100M"])
ax.grid(axis="y", linestyle="--", color="#DDDDDD", zorder=0)

# group labels (below the x tick labels)
ax.annotate("Achieved (2026)", xy=(0.5, 0), xytext=(0.5, -0.17),
            xycoords=("data", "axes fraction"), ha="center",
            fontsize=11, fontweight="bold", color=BLUE_D)
ax.annotate("Required to break RSA-2048", xy=(3.6, 0), xytext=(3.6, -0.17),
            xycoords=("data", "axes fraction"), ha="center",
            fontsize=11, fontweight="bold", color=VERM_D)

# gap arrow
arr = FancyArrowPatch((1.8, 1000), (1.8, 100000), arrowstyle="<->", mutation_scale=14,
                      color="#444444", lw=2, zorder=4)
ax.add_patch(arr)
ax.text(1.8, 9000, "Hardware gap\n~10$^2$–10$^4$×", ha="center", va="center",
        fontsize=10, fontweight="bold", color="#444444")
ax.axhline(1000, xmin=0.27, xmax=0.45, color=BLUE, ls=(0, (6, 4)), lw=1.5)

for s in ["top", "right"]:
    ax.spines[s].set_visible(False)

plt.subplots_adjust(bottom=0.22)
out = os.path.join(os.path.dirname(__file__), "hardware_gap_preview.png")
plt.savefig(out, dpi=150)
print(out)
