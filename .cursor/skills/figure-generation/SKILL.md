---
name: figure-generation
description: Generate figures for this thesis with a consistent look. Prefer draw.io (.drawio) for diagrams, schematics, flowcharts, and conceptual figures; use matplotlib only for data-driven plots. Enforces the Okabe-Ito color palette and the Latin Modern Roman thesis font. Use whenever creating, editing, or exporting any thesis figure.
---

# Thesis Figure Generation

## Tool choice

- **Diagrams / schematics / flowcharts / conceptual figures → draw.io.** Author a `.drawio` source file and export a `.pdf`. This is the default; use it whenever possible.
- **Data-driven plots (curves, bars, scatter, heatmaps) → matplotlib.** draw.io cannot plot data. Use the shared style module `figures/thesis_style.py`.

Always keep the editable source (`.drawio` or `.py`) next to the exported asset so figures are reproducible.

## Color palette (Okabe-Ito, colorblind-safe)

Use these for categorical / discrete encodings. They are already used in `figures/chapter1/`.

| Role | Fill | Dark (stroke/text) |
|------|------|--------------------|
| Blue | `#0072B2` | `#004C77` |
| Green | `#009E73` | `#00674C` |
| Vermillion / orange | `#D55E00` | `#8A3D00` |
| Orange (light) | `#E69F00` | `#9E6B00` |
| Sky blue | `#56B4E9` | `#2C7CB0` |
| Reddish purple | `#CC79A7` | `#8E4B73` |
| Yellow accent | `#FFD966` | `#BF9000` |
| Neutral grey | `#5A5A5A` | `#333333` |
| Black | `#000000` | — |

Rules:
- Pick colors in this order: Blue, Vermillion, Green, Orange, Sky blue, Purple. Do not encode meaning with red/green alone.
- For fills behind text, use the fill color at low opacity (draw.io `fillOpacity=20`) with the full-strength stroke.
- Grid lines / minor furniture: `#DDDDDD`; secondary annotations: grey `#5A5A5A`.
- For **continuous / sequential / diverging** data, do not use this palette. Use Fabio Crameri's Scientific Colour Maps (read `~/.codex/skills/scientific-colour-maps/SKILL.md`).

## Font

The thesis body font is **Latin Modern Roman** (`lmodern`). Figures must match.

- **draw.io:** set `fontFamily=LMRoman10;` on every text-bearing style. The headless draw.io exporter matches fonts by their installed family name; the Latin Modern OTFs (`font-latin-modern` cask) register per optical size as `LMRoman10`, `LMRoman12`, etc., **not** as `Latin Modern Roman`. Using the literal string `Latin Modern Roman` silently falls back to the draw.io default sans (Helvetica), which is wrong for thesis figures. `LMRoman10` is the standard text optical size and matches the thesis body font. Verify with `fc-list | grep -i lmroman` (or install via `brew install --cask font-latin-modern`) if the export still renders sans-serif.
- **matplotlib:** `font.family: serif` (handled by `scripts/thesis_style.py`). Computer Modern shipped with most TeX installs matches `lmodern`.

## draw.io conventions

- One diagram per file. Name it after its purpose, e.g. `figures/chapter2/qkd_stack.drawio`.
- Square or content-fit `pageWidth`/`pageHeight`; turn the grid off (`grid="0"`) for clean conceptual figures.
- Stroke widths: primary shapes `strokeWidth=3`, markers/legend `strokeWidth=1.5`.
- Title text: `fontStyle=1` (bold), `fontSize` ~21 for figure-internal headings, `fontColor` = the dark variant of the related fill.
- Reference style snippet (matches `figures/chapter1/field_venn.drawio`):

```text
ellipse;html=1;fillColor=#0072B2;fillOpacity=20;strokeColor=#0072B2;strokeWidth=3;fontFamily=LMRoman10;
```

### Export to PDF (draw.io CLI)

The export tool is the draw.io desktop app's headless CLI. It is an Electron
app, so it **must run outside the restricted sandbox** (request elevated/full
permissions when running as a Cursor agent), and it needs filesystem access to
the workspace.

1. Ensure the CLI is installed (one-time). `drawio` should be on `PATH` and
   `/Applications/draw.io.app` should exist:

   ```bash
   command -v drawio || brew install --cask drawio
   ```

2. Export a cropped PDF next to the source (this is the canonical asset for
   `\includegraphics`):

   ```bash
   drawio --export --crop --format pdf --output figures/<chapter>/<name>.pdf figures/<chapter>/<name>.drawio
   ```

3. **Always render a PNG preview and visually verify** marker placement, label
   fit, and that overlaps land in the intended regions before considering the
   figure done. Delete the preview afterward (do not commit it):

   ```bash
   drawio --export --crop --format png --scale 2 --output figures/<chapter>/_preview.png figures/<chapter>/<name>.drawio
   # inspect figures/<chapter>/_preview.png, then:
   rm -f figures/<chapter>/_preview.png
   ```

Notes:
- `--crop` trims the page to the diagram bounds; always use it.
- Star/badge markers use the basic shape library (`shape=mxgraph.basic.star`),
  which the desktop/web app and CLI render correctly.
- If the user edits the `.drawio` by hand, re-run the export so the committed
  `.pdf` stays in sync with the source (the `.drawio` is the source of truth).
- Do **not** re-implement a draw.io figure in matplotlib just to get a PDF; fix
  the CLI/permissions instead.

If the `drawio` CLI is genuinely unavailable, export from the draw.io
desktop/web app (File → Export as → PDF, "Crop" enabled), keeping the same path.

## matplotlib quick start

The shared module `figures/thesis_style.py` defines the palette constants and
`apply_style()` (serif font, Okabe-Ito color cycle, clean spines/grid):

```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))  # to repo root
from figures.thesis_style import apply_style, BLUE, BLUE_D, VERM, VERM_D, GREEN, GREY

apply_style()
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(7.4, 4.8))
ax.plot(x, y, "-o", color=BLUE, mec=BLUE_D, lw=2.4)
fig.savefig("figures/<chapter>/<name>.pdf")
fig.savefig("figures/<chapter>/<name>.png", dpi=160)  # preview only
```

The canonical PDF is for `\includegraphics`; the PNG is a quick preview.

## Including in LaTeX

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=\linewidth]{figures/<chapter>/<name>.pdf}
  \caption{...}
  \label{fig:<name>}
\end{figure}
```

## Checklist

- [ ] Diagram authored in draw.io (not matplotlib) when it is not a data plot
- [ ] Colors drawn from the Okabe-Ito table; sequential/continuous uses Crameri maps
- [ ] Font is Latin Modern Roman / serif, not Helvetica
- [ ] Editable source committed alongside the exported `.pdf`
- [ ] PDF exported cropped into `figures/<chapter>/` via the draw.io CLI (run outside the sandbox)
- [ ] PNG preview rendered, visually verified, then deleted (not committed)
