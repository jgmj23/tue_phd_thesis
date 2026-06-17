# Decisions

Record thesis and workflow decisions here so future agents can understand why the repository is shaped this way.

## 2026-06-17

- Use issue-scoped work as the primary workflow: issue, branch, worktree, agent work, review, merge.
- Keep `main` stable and buildable.
- Store local issue definitions in `.agents/issues/`.
- Store local worktrees under `.worktrees/`, ignored by Git.
- Store official TU/e regulations, title-page models, and related institutional source material in `source-materials/university/`.
- Do not create the LaTeX build skeleton until the TU/e/department template situation is clear; the current official inputs are regulations and Word title-page templates, not a LaTeX class.
- Use the Abraham Cano draft only as a local third-party LaTeX reference; do not track its thesis prose, figures, or publication PDFs as this repository's source.
- Adopt the template's 170 mm x 240 mm print geometry for the initial thesis skeleton.
