# 008 Plan Thesis Section Structure

## Status

Done

## Goal

Restructure the thesis skeleton into a paper-centric, part-based outline that keeps the agreed cross-layer narrative while making the included publications the central body of the dissertation.

## Context

The current thesis skeleton uses generic chapters: introduction, background, methods, results, discussion, and conclusion. The user wants a structure closer to the Abraham Cano thesis style: a short narrative wrapper around the thesis problem, followed by chapters centered on published papers, with transitions and synthesis prose around the included papers.

Relevant inputs:

- `notes/template-analysis.md`
- `notes/publication-inventory.md`
- `source-materials/templates/abraham-cano-draft/`

The Abraham Cano draft is a local third-party reference only. Reuse its structural pattern, not its prose, figures, or publication PDFs.

## Allowed Files

- `thesis.tex`
- `chapters/`
- `notes/decisions.md`
- `notes/publication-inventory.md`
- `.agents/issues/008-plan-thesis-section-structure.md`
- `.agents/status.md`
- `.agents/handoffs/008-plan-thesis-section-structure.md`

## Do Not Touch

- `source-materials/templates/abraham-cano-draft/`
- `references/thesis.bib`
- `frontmatter/`
- `backmatter/`

## Expected Output

- `thesis.tex` uses part divisions for the thesis frame, quantum foundations, DPU/PQC infrastructure, datacenter security, and synthesis.
- Chapter files are renamed or replaced with paper-centric placeholders that identify which publications belong in each chapter.
- Each paper-centric chapter has a consistent wrapper pattern:
  - chapter motivation
  - relation to thesis research questions
  - publication context and author contribution
  - included paper placeholder
  - post-paper discussion
  - link to the next chapter
- `notes/publication-inventory.md` records the final planning structure.
- `notes/decisions.md` records the structural decision.

## Acceptance Criteria

- The thesis skeleton compiles.
- The structure remains paper-centric without copying third-party Abraham Cano prose.
- Each candidate thesis-body paper from `notes/publication-inventory.md` is assigned to a planned chapter or explicitly deferred.
- Changes stay within the allowed file scope.
- Uncertain publication statuses or claims are marked with `TODO:`.
- Relevant decisions are recorded in `notes/decisions.md`.

## Verification

```sh
make pdf
```

Also check that all chapter files referenced by `thesis.tex` exist.

## Agent Notes

Preferred structure from the user discussion:

1. Thesis frame: introduction plus background and unifying methods.
2. Quantum photonic and quantum-secured network foundations.
3. Post-quantum cryptography in programmable network infrastructure.
4. Cross-layer security in datacenter fabrics and confidential AI.
5. Cross-layer lessons and future outlook.

Paper chapters should contain placeholders for the published papers and the narrative wrapper, not full prose drafts.

Local implementation completed on branch `codex/issue-008-plan-thesis-section-structure`.

GitHub sync: created as `https://github.com/jgmj23/tue_phd_thesis/issues/8` after user approval. Closed after local status was marked `Done`.

Verification: `make pdf` passed after rerunning outside the sandbox. The first sandboxed run failed with a Tectonic runtime/network panic. The successful build produced only overfull-line warnings from long placeholder titles and table-of-contents entries.

## Review Result

Accepted.
