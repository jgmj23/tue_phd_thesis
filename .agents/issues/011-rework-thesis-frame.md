# 011 Rework Thesis Frame

## Status

Done

## Goal

Revise Chapters 1 and 2 so the front matter frames the thesis around
architectures for scalable quantum-resilient communication systems, using the
three research pillars from the 2026 Go/No-Go activity report.

## Context

The current Chapter 1 and Chapter 2 files contain generic TODO placeholders.
The user's Go/No-Go activity report identifies the overarching research theme
as "Architectures for Scalable Quantum-Resilient Communication Systems" and
organizes the work into three pillars:

- high-performance post-quantum cryptographic acceleration;
- scalable and topology-aware QKD architectures;
- integrated photonic entanglement sources for deployable QKD.

ROSE-QKD should remain patent/title-level context only and must not become a
thesis-body paper.

## Allowed Files

- `chapters/01-introduction.tex`
- `chapters/02-background.tex`
- `notes/decisions.md`
- `notes/publication-inventory.md`
- `source-materials/prior-writing/activity-report-2025-2026-joey.doc`
- `source-materials/prior-writing/activity-report-2025-2026-joey.txt`
- `.agents/issues/011-rework-thesis-frame.md`
- `.agents/status.md`
- `.agents/handoffs/011-rework-thesis-frame.md`
- `.agents/reviews/011-rework-thesis-frame-review.md`

## Do Not Touch

- `references/thesis.bib`
- `frontmatter/`
- `backmatter/`
- `chapters/03-integrated-quantum-sources.tex`
- `chapters/04-qkd-post-processing-dpu.tex`
- `chapters/05-dpu-accelerated-pqc.tex`
- `chapters/06-edge-ai-pipelines.tex`
- `chapters/07-rdma-optical-fabrics.tex`
- `chapters/08-confidential-ai-observability.tex`
- `chapters/09-cross-layer-lessons.tex`
- `source-materials/templates/abraham-cano-draft/`

## Expected Output

- Chapter 1 has concrete, descriptive section headings that introduce the
  thesis claim, scope, research context, research pillars, research questions,
  contributions, and dissertation organization.
- Chapter 2 introduces the technical background needed for the paper-centric
  chapters: PQC deployment constraints, programmable network infrastructure,
  QKD network architecture, integrated photonic sources, and cross-layer
  evaluation.
- ROSE-QKD is mentioned only as patent/title-level context unless approved
  disclosure language is later provided.
- Planning notes reflect the updated front-frame structure.

## Acceptance Criteria

- The thesis builds successfully with `make pdf`, or a narrower syntax check is
  documented if the build environment is unavailable.
- Changes stay within the allowed file scope.
- No invented citations are added. Citation placeholders, if needed, are marked
  as `TODO: citation`.
- Substantive structural decisions are recorded in `notes/decisions.md`.

## Verification

```sh
make pdf
```

## Agent Notes

Implemented on branch `codex/issue-011-rework-thesis-frame`.

Chapter 1 now frames the dissertation as an architecture problem for scalable
quantum-resilient communication systems, adds concrete scope, research
questions, research pillars, and dissertation organization.

Chapter 2 now provides the technical scaffolding for the paper-centric chapters:
PQC deployment constraints, DPU/SmartNIC offload, scalable QKD architectures,
integrated photonic sources, and cross-layer architecture evaluation.

ROSE-QKD is explicitly kept as patent/title-level context only.

After the Chapter 1--2 reframe, the activity report source was copied into the
repository source materials as
`source-materials/prior-writing/activity-report-2025-2026-joey.doc`, with a
plain-text extraction at
`source-materials/prior-writing/activity-report-2025-2026-joey.txt` for search
and future agent use.

Verification: `make pdf` passed outside the sandbox after the sandboxed
Tectonic run failed with the known runtime panic. The successful build produced
only overfull-line warnings, mostly from existing long headings and placeholder
sections.
