# 001 Collect Thesis Inputs Handoff

## What Changed

- University source files were collected under `source-materials/university/`.
- University requirements, title-page fields, template analysis, and defense timeline notes were created.
- The publication list was copied to `source-materials/prior-writing/joey_publications.docx`.
- The project status index was copied to `source-materials/prior-writing/project-status-index.md`.
- `notes/publication-inventory.md` now records thesis-body candidate papers, excluded publications, patent handling, project/source locations, chapter-planning buckets, and reference workflow.
- Follow-up issues now cover title page cleanup, defense timeline, build skeleton, reference/prior-writing ingestion, and later camera-ready manuscript collection.

## What Remains

- Issue `005-ingest-references-and-prior-writing` should merge/deduplicate the project bibliographies into `references/thesis.bib` and classify reusable prior text.
- Issue `006-collect-camera-ready-manuscripts` is waiting on the user and should collect camera-ready PDFs or accepted manuscripts later.
- Issue `002-clean-title-page` is waiting for confirmation on whether reserve member prof.dr. N. Calabretta appears on the printed title page.

## Open Questions

- Confirm the bibliography source for the confidential-compute payload-free detection manuscript.
- Confirm how much of the not-yet-finished Edge AI paper should be used before it is finalized.

## Files Touched

- `.agents/issues/001-collect-thesis-inputs.md`
- `.agents/issues/005-ingest-references-and-prior-writing.md`
- `.agents/issues/006-collect-camera-ready-manuscripts.md`
- `.agents/status.md`
- `notes/decisions.md`
- `notes/publication-inventory.md`
- `source-materials/prior-writing/joey_publications.docx`
- `source-materials/prior-writing/project-status-index.md`

## Verification

Ran `git status --short`. Newly added tracked candidates are source metadata, notes, and issue files; large paper PDFs remain deferred to ignored `source-materials/papers/`.
