# Abraham Cano Draft Template Analysis

Template copied locally to:

`source-materials/templates/abraham-cano-draft/`

The template is ignored by Git because it is a third-party thesis draft with prose, figures, and publication PDFs. Reusable structure has been adapted into this repository instead.

## Useful Parts

- `main.tex`: book-class thesis entry point with front matter, chapters, back matter, bibliography, list of acronyms, publications, acknowledgements, and CV.
- `includes.tex`: package set and print geometry.
- `front/titlepage_formal.tex`: custom LaTeX rendering of the TU/e Word title-page format.
- `README.txt`: print-size guidance and notes that the official TU/e title page is only available as Word.

## Adopted

- Page geometry: 170 mm x 240 mm, with margins from the template.
- Book-class, two-sided structure.
- Front matter, main matter, and back matter split.
- Custom LaTeX title-page approach based on the TU/e Word model.
- `biblatex`/`biber` bibliography workflow.

## Not Adopted Yet

- Glossaries/acronym build workflow.
- Publication-PDF inclusion workflow.
- Full package list from the template, which contains duplicates and project-specific packages.
- Chapter prose, figures, and publication PDFs.

## Local Tooling Gap

This machine currently has Tectonic at `/opt/homebrew/bin/tectonic`. It does not have `latexmk`, `xelatex`, or `biber` on `PATH`, so `make pdf` uses Tectonic by default and `make latexmk` is reserved for a fuller TeX installation.

`make pdf` now builds `thesis.pdf` successfully. The only expected log warnings are the BibTeX fallback warning and empty bibliography warning, both of which should be revisited after the bibliography is ingested.
