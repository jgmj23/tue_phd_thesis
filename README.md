# Thesis

This repository contains the source, notes, references, figures, and coordination files for the PhD thesis.

## Workflow

Work is organized by issue:

```text
Issue -> Branch -> Worktree -> Agent work -> Review -> Merge
```

`main` should stay buildable. Agents should work in issue-specific branches and worktrees, using the issue file as the source of truth for scope and acceptance criteria.

## Key Paths

- `chapters/`: thesis chapter source files.
- `frontmatter/`: abstract, acknowledgements, notation, and other front matter.
- `appendices/`: appendix source files.
- `backmatter/`: CV, publications, acknowledgements, and other closing matter.
- `references/`: bibliography and citation notes.
- `figures/source/`: editable figure sources.
- `figures/exported/`: thesis-ready figure exports.
- `tables/source/`: editable table sources.
- `tables/exported/`: thesis-ready table exports.
- `notes/`: literature notes, meeting notes, decisions, and scratch work.
- `research/`: code, notebooks, data pointers, and generated outputs.
- `source-materials/`: official requirements, advisor input, prior writing, reference exports, and other incoming materials.
- `.agents/issues/`: local issue queue for agent work.
- `.agents/status.md`: current issue-status dashboard.
- `.agents/workflow.md`: recommended agent/thread workflow.
- `.agents/handoffs/`: context left by agents when a task is paused or completed.
- `.agents/reviews/`: review notes before merging issue work.

## Issue Naming

Use numeric, stable issue identifiers:

```text
.agents/issues/001-intro-outline.md
codex/issue-001-intro-outline
.worktrees/001-intro-outline
```

Keep one active owner per issue. If two agents need the same chapter, split the work into separate issues with non-overlapping file scopes.

## Build

The thesis is built with Tectonic. Build (or rebuild) the PDF with:

```sh
make pdf
```

This writes `thesis.pdf` at the repo root. Agents are expected to run this
after every significant change so the latest content is visible in the PDF.

`make pdf` passes `-Z search-path=tools/biblatex` so Tectonic uses a vendored
`biblatex` that matches the system `biber`; without it, the build fails with a
`biblatex control file version ... incompatible` error. See
`tools/biblatex/README.md` for details and how to update it.

Run the build with normal (non-sandboxed) filesystem and network access:
Tectonic caches fonts/packages under `~/Library/Caches/Tectonic` and may fetch
resources on first use.

Alternative full-TeX build (only on machines with a complete TeX Live install,
including `latexmk`, `xelatex`, and `biber`):

```sh
make latexmk
```
