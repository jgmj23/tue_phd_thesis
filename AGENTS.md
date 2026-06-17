# Agent Instructions

This repository is organized around issue-scoped thesis work. Every agent should read this file and the relevant issue file before making changes.

## Operating Rules

- Treat `.agents/issues/*.md` as the source of truth for active work.
- Work on one issue at a time.
- Keep changes within the issue's allowed file scope.
- Do not edit files listed under `Do Not Touch` in the issue.
- Leave unrelated cleanup for a separate issue.
- Prefer small, reviewable changes over broad rewrites.
- Update `notes/decisions.md` when making a substantive structural, terminology, citation, or workflow decision.
- Add a handoff note in `.agents/handoffs/` when work is paused or completed.
- Add review notes in `.agents/reviews/` before merging back to `main`.

## Branch And Worktree Convention

For issue `NNN-short-title`:

```text
Branch:   codex/issue-NNN-short-title
Worktree: .worktrees/NNN-short-title
Issue:    .agents/issues/NNN-short-title.md
```

`main` should remain stable and buildable.

## Thesis Writing Rules

- Preserve academic tone unless an issue requests exploratory drafting.
- Mark uncertain claims with `TODO:` and explain what is missing.
- Do not invent citations. Use citation keys only when they exist in `references/thesis.bib`, or mark them as `TODO: citation`.
- Keep chapter files focused on thesis prose. Put planning, alternatives, and rough notes in `notes/`.
- Prefer source figures and reproducible exports where practical.

## Build And Verification

Use the commands documented in the active issue. If a build system has not been finalized yet, verify by checking affected files for obvious syntax, path, and citation-key issues.

