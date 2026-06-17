# 004 Create Thesis Build Skeleton

## Status

Ready for Review

## Goal

Create the initial LaTeX thesis entry point and build workflow once the correct TU/e template constraints are known.

## Context

Available inputs now include official regulations, Word title-page templates, and the local Abraham Cano draft LaTeX template.

## Allowed Files

- `thesis.tex`
- `Makefile`
- `frontmatter/`
- `chapters/`
- `appendices/`
- `references/`
- `figures/`
- `tables/`
- `notes/`
- `.agents/issues/`

## Do Not Touch

- `source-materials/university/`
- `source-materials/templates/abraham-cano-draft/`

## Expected Output

- `thesis.tex` entry point.
- Minimal chapter/frontmatter includes.
- Bibliography hook.
- Build command in `Makefile`.
- Placeholder files only where useful.

## Acceptance Criteria

- Build command is documented.
- Generated outputs are ignored unless intentionally stored as milestones.
- Front matter can later reproduce the approved TU/e title page.
- No university-specific formatting is guessed if a template is still missing.

## Verification

Run the selected build command once a TeX distribution/template is available.

## Agent Notes

Created initial thesis skeleton:

- `thesis.tex`
- `includes.tex`
- `Makefile`
- `frontmatter/titlepage.tex`
- `frontmatter/summary.tex`
- chapter placeholders
- `backmatter/`
- `references/thesis.bib`

The external template indicates 170 mm x 240 mm or 170 mm x 245 mm print pages; this skeleton adopts 170 mm x 240 mm for now.

Tectonic is available locally and is now the default `make pdf` path. `latexmk`, `xelatex`, and `biber` are not installed on `PATH`, so `make latexmk` is reserved for a fuller TeX installation.

Verification performed:

- `make pdf` completed successfully with Tectonic.
- `thesis.pdf` was produced.
- PDF page size is 170 mm x 240 mm.
- Rendered title pages were visually inspected.
- Remaining log warnings are expected until the bibliography is ingested: BibTeX fallback and empty bibliography.

## Review Result

Pending review.
