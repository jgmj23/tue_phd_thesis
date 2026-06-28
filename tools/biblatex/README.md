# Vendored biblatex (for Tectonic builds)

This directory contains a flattened copy of `biblatex` and the `biblatex-ieee`
style so that Tectonic can use a `biblatex` version that matches the system
`biber`.

## Why this exists

Tectonic ships its own (older) `biblatex` but shells out to whatever `biber`
is installed on the machine. The Homebrew `biber` (2.21) is newer than
Tectonic's bundled `biblatex` (3.17), so a plain `tectonic thesis.tex` fails
with:

```
ERROR - Error: Found biblatex control file version 3.8, expected version 3.11.
This means that your biber (2.21) and biblatex (3.17) versions are incompatible.
```

Pointing Tectonic at this directory with `-Z search-path=tools/biblatex`
(done automatically by `make pdf`) makes it load `biblatex` 3.21, which writes
a control file (`.bcf`) version 3.11 that `biber` 2.21 understands.

## Contents / provenance

- `biblatex` 3.21 runtime files (`.sty`, `.def`, `.bbx`, `.cbx`, `.lbx`, `.dbx`),
  from CTAN `macros/latex/contrib/biblatex` (release dated 2025-07-10).
- `biblatex-ieee` style files (`ieee*.bbx`, `ieee*.cbx`, `magyar-ieee.lbx`),
  from CTAN `macros/latex/contrib/biblatex-contrib/biblatex-ieee`
  (release dated 2025-08-01).

All files are flattened into this single directory (no `bbx/`, `cbx/`, `lbx/`
subfolders) because `biblatex` loads style and locale files by basename and
Tectonic's `search-path` is matched by filename.

## Updating

If you upgrade `biber` and the version mismatch returns, replace these files
with a `biblatex` release matching the new `biber` (see the compatibility
matrix in the biblatex manual), keeping the flat layout. Confirm the version
with:

```sh
grep abx@version tools/biblatex/biblatex.sty
biber --version
```
