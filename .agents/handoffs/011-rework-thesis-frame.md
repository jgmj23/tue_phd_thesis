# Handoff: 011 Rework Thesis Frame

Date: 2026-06-18

Branch: `codex/issue-011-rework-thesis-frame`

GitHub issue: https://github.com/jgmj23/tue_phd_thesis/issues/11

## Summary

Reworked the thesis front frame so Chapters 1 and 2 follow the Go/No-Go
activity report framing:

- overarching theme: architectures for scalable quantum-resilient communication
  systems;
- three research pillars: high-performance PQC acceleration,
  scalable/topology-aware QKD architectures, and integrated photonic
  entanglement sources for deployable QKD;
- ROSE-QKD remains patent/title-level context only and is not a thesis-body
  paper.

## Files Changed

- `chapters/01-introduction.tex`
- `chapters/02-background.tex`
- `notes/publication-inventory.md`
- `notes/decisions.md`
- `.agents/issues/011-rework-thesis-frame.md`
- `.agents/status.md`
- `.agents/handoffs/011-rework-thesis-frame.md`
- `source-materials/prior-writing/activity-report-2025-2026-joey.doc`
- `source-materials/prior-writing/activity-report-2025-2026-joey.txt`

## Verification

`make pdf` passed outside the sandbox. The initial sandboxed build failed with
the known Tectonic runtime panic before compilation. The successful build
produced only overfull-line warnings, including minor warnings in the new
Chapter 1 and Chapter 2 front-frame text and several existing warnings in later
chapters.

## Notes

The new text intentionally avoids adding citation commands until
`references/thesis.bib` is merged and cleaned. Two broad background claims are
marked `TODO: citation`.

The Go/No-Go activity report used for the Chapter 1--2 framing is now copied
into `source-materials/prior-writing/` in both original `.doc` form and a
plain-text extraction for search.
