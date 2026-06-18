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
- Treat the thesis as a compilation-style thesis organized around Joseph G. Meyer's publication set, with original introduction, synthesis, transitions, and conclusion added around the papers.
- Use `references/thesis.bib` as the canonical thesis bibliography. Paper-specific bibliographies remain source inputs and should be merged/deduplicated rather than cited directly from separate paper projects.
- Patent-related material should be limited to title-level mention unless the user supplies approved disclosure language.
- Exclude the Optics Letters spatial-mode QKD paper and the ROSE-QKD paper/manuscript from the thesis body. Keep the ROSE-QKD patent as title-only thesis material.
- Keep `.agents/issues/*.md` and GitHub Issues synchronized explicitly. Local issue files are repository planning specs and do not create or close GitHub Issues by themselves.
- Organize the thesis as a paper-centric compilation with five narrative parts: thesis frame, quantum photonic and quantum-secured network foundations, DPU/PQC infrastructure, datacenter fabric and confidential AI security, and synthesis.
- Each paper-bearing chapter should wrap the included manuscript with descriptive, non-generic section titles.
- Use `\includepdf` (via `pdfpages`) to embed the final/accepted manuscript PDFs rather than copying raw LaTeX text.
- Wrap each paper with a pre-paper section (publication context, author contribution, relation to the thesis) and a post-paper section (discussion and transition to the next chapter).

## 2026-06-18

- Reframe Chapters 1 and 2 around "Architectures for Scalable Quantum-Resilient Communication Systems," following the Go/No-Go activity report's three pillars: high-performance PQC acceleration, scalable/topology-aware QKD architectures, and integrated photonic entanglement sources for deployable QKD.
- Keep ROSE-QKD as patent/title-level context only. It may support the scalable-QKD architecture motivation, but it is not a thesis-body paper unless approved disclosure language is later provided.
- Separate the front-frame chapters by function: Chapter 1 makes the thesis argument, scope, research questions, and paper map; Chapter 2 provides the technical background and unifying cross-layer evaluation method.
