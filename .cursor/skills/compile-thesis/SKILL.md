---
name: compile-thesis
description: >-
  Compile this LaTeX thesis to thesis.pdf with Tectonic and verify the build.
  Use after any significant change (chapter prose, figures, tables,
  bibliography, layout, or build files), and whenever the user asks to build,
  compile, rebuild, or regenerate the thesis / PDF, or when a build fails with a
  biber/biblatex version error.
---

# Compile the thesis

The author wants `thesis.pdf` kept current. Run this after every significant
change so the change is visible in the PDF.

## Command

From the repo root:

```sh
make pdf
```

This runs Tectonic with the vendored biblatex and writes `thesis.pdf`.

It expands to:

```sh
tectonic -Z search-path=tools/biblatex --keep-logs --keep-intermediates thesis.tex
```

Run with full filesystem and network access (not a restricted sandbox).
Tectonic caches fonts/packages under `~/Library/Caches/Tectonic` and may fetch
resources on first use; a sandbox that blocks writes outside the workspace
fails with `Operation not permitted` while caching fonts. When running as a
Cursor agent, request the elevated permission for this command.

## Verify the build

After building, confirm it was clean:

```sh
grep -c undefined thesis.log   # must print 0 (no undefined citations/refs)
```

- `make pdf` must exit `0`.
- `grep -c undefined thesis.log` must print `0`.

If either check fails, the build is not done — fix and rebuild.

## Do not break the bibliography setup

`make pdf` passes `-Z search-path=tools/biblatex` because Tectonic's bundled
`biblatex` is older than the system `biber`. Without the flag the build fails:

```
Found biblatex control file version ... versions are incompatible.
```

Do not remove that flag and do not edit the `biblatex` setup in `includes.tex`
to work around it. If `biber` is upgraded and the error returns, update the
vendored files in `tools/biblatex/` instead (see `tools/biblatex/README.md`).

## Notes

- A full TeX install is not present. Do not assume `latexmk`, `xelatex`, or
  `kpsewhich` exist. The `make latexmk` target is only for machines with a
  complete TeX Live installation.
- These rules also live in the repo's `AGENTS.md` (Operating Rules and
  Build And Verification).
