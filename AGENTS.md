# Agent Instructions

This repository is organized around issue-scoped thesis work. Every agent should read this file and the relevant issue file before making changes.

## Operating Rules

- Treat `.agents/issues/*.md` as the source of truth for active work.
- Keep local issue files and GitHub Issues synchronized. When creating a new `.agents/issues/NNN-short-title.md`, also create the matching GitHub issue with `gh issue create`, then update `.agents/status.md` with the GitHub issue number/link. When marking a local issue `Done`, also close the matching GitHub issue with `gh issue close`.
- Do not treat an issue as complete, reviewed, or merged while `.agents/status.md` shows `Pending` in the GitHub column for that issue.
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

## GitHub Issue Sync

Local files under `.agents/issues/` are planning specs, not GitHub Issues.
Creating, editing, committing, or pushing those files does not automatically
create or close GitHub Issues. Agents must explicitly keep both systems aligned:

1. Create or update the local issue file.
2. Run `gh issue create --repo jgmj23/tue_phd_thesis --title "NNN Short Title" --body-file .agents/issues/NNN-short-title.md` for new issues.
3. Update `.agents/status.md` so the GitHub column links to the created issue.
4. When local status becomes `Done`, run `gh issue close N --repo jgmj23/tue_phd_thesis --comment "...completion note..."`.
5. Before pushing or calling work merged, run `gh issue list --repo jgmj23/tue_phd_thesis --state all` or `gh issue view N --json state,title,url` when relevant, and confirm local/remote states match.

## Thesis Writing Rules

- Preserve academic tone unless an issue requests exploratory drafting.
- Mark uncertain claims with `TODO:` and explain what is missing.
- Do not invent citations. Use citation keys only when they exist in `references/thesis.bib`, or mark them as `TODO: citation`.
- Use `biblatex` with `style=ieee` and `sorting=none` (numbered references, first-citation order) via the single canonical bibliography `references/thesis.bib`.
- Keep chapter files focused on thesis prose. Put planning, alternatives, and rough notes in `notes/`.
- Prefer source figures and reproducible exports where practical.
- Use descriptive, content-specific section titles in chapters rather than generic template names (e.g., "From Photonic Devices to Network Components" instead of "Chapter Motivation").
- For paper-centric chapters, preserve the accepted/camera-ready paper formatting where possible by including the final PDF using `\includepdf` from the `pdfpages` package instead of copying raw LaTeX text.
- Before each included paper, add a short thesis-formatted section with publication venue/status, author contribution, relation to the thesis questions, and why the paper belongs there.
- After each included paper, add a thesis-formatted discussion/transition section.

## Build And Verification

Use the commands documented in the active issue. If a build system has not been finalized yet, verify by checking affected files for obvious syntax, path, and citation-key issues.
