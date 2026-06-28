# Agent Instructions

This is a single-author thesis repository. Work happens directly on `main`
using a lightweight, trunk-based workflow. Every agent should read this file
before making changes.

## Workflow (lightweight, trunk-based)

- Work directly on `main`. Do not create per-task branches, worktrees, or
  GitHub issues for routine writing. `main` should always stay buildable.
- `.agents/backlog.md` is the optional, informal to-do list for what to write
  or fix next. It is a planning aid, not a tracking system — there is no
  GitHub-issue sync, no handoff notes, and no review notes to maintain.
- Commit in small, logical chunks. Don't let a week of work pile up
  uncommitted. Prefer one coherent commit per topic (e.g. "rework chapter 1
  framing", "regenerate hardware-gap figure").
- Compile after every significant change. Whenever you finish a substantive
  edit (chapter prose, figures, tables, bibliography, layout, or build files),
  run `make pdf` so the change is reflected in `thesis.pdf`. Do not end a turn
  that made significant content changes without producing an up-to-date
  `thesis.pdf`. The full procedure and gotchas are in the `compile-thesis`
  skill (`.cursor/skills/compile-thesis/`); see also `Build And Verification`.
- Prefer small, reviewable changes over broad rewrites.
- Update `notes/decisions.md` when making a substantive structural,
  terminology, citation, or workflow decision.
- Keep scratch scripts and throwaway experiments in `scratch/` (gitignored),
  not in the repo root or `figures/`.

## When to use branches (the exception, not the rule)

Only reach for a feature branch (and optionally a worktree under
`.worktrees/`) when running **multiple agents in parallel on non-overlapping
files** — for example, drafting several chapters at once. In that case use
`feature/short-title` branches, keep each agent inside its own file scope,
never run two agents on the same chapter file simultaneously, and merge back
to `main` once each piece builds cleanly. For everything else, edit `main`
directly.

## Thesis Writing Rules

- Preserve academic tone unless an issue requests exploratory drafting.
- Mark uncertain claims with `TODO:` and explain what is missing.
- Do not invent citations. Use citation keys only when they exist in `references/thesis.bib`, or mark them as `TODO: citation`.
- Use `biblatex` with `style=ieee` and `sorting=none` (numbered references, first-citation order) via the single canonical bibliography `references/thesis.bib`.
- Keep chapter files focused on thesis prose. Put planning, alternatives, and rough notes in `notes/`.
- Prefer source figures and reproducible exports where practical.
- Use descriptive, content-specific section titles in chapters rather than generic template names (e.g., "From Photonic Devices to Network Components" instead of "Chapter Motivation").
- For paper-centric chapters, preserve the accepted/camera-ready paper formatting where possible by including the final PDF using `\includepdf` from the `pdfpages` package instead of copying raw LaTeX text.
- Before each included paper, add a short thesis-formatted section with publication venue/status, author contribution, relation to the thesis questions, and why the paper belongs there.
- After each included paper, add a thesis-formatted discussion/transition section.

## Build And Verification

The thesis is built with Tectonic. The single command to (re)build the PDF is:

```sh
make pdf
```

This writes `thesis.pdf` (at the repo root) and keeps the intermediate
`.aux`/`.bcf`/`.bbl`/`.log` files. Run it after every significant change so
the author can immediately see the result in `thesis.pdf`. After building,
confirm the run was clean:

- `make pdf` exits with status `0`.
- `grep -c undefined thesis.log` reports `0` (no undefined citations/refs).

### Compile gotchas (read before debugging a failed build)

- Bibliography / `biber` version mismatch: Tectonic bundles an older
  `biblatex` than the system `biber`, which fails with
  `Found biblatex control file version ... versions are incompatible`. This is
  already solved: `make pdf` passes `-Z search-path=tools/biblatex` so Tectonic
  uses the vendored `biblatex` that matches `biber`. Do not remove that flag.
  If `biber` is later upgraded and the error returns, update
  `tools/biblatex/` (see `tools/biblatex/README.md`) rather than deleting the
  flag or editing `includes.tex`.
- Tectonic writes fonts/packages to its cache at `~/Library/Caches/Tectonic`
  and may fetch resources from the network on first use. Run the build with
  full filesystem and network access (a sandbox that blocks writes outside the
  workspace will fail with `Operation not permitted` while caching fonts).
- A full TeX install is not required and is not present; do not assume
  `latexmk`, `xelatex`, or `kpsewhich` exist. The `make latexmk` target is only
  for machines that have a complete TeX Live installation.
