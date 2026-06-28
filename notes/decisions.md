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

## 2026-06-21

- Make the three research pillars the explicit structural backbone of the thesis:
  the three central numbered Parts are `Part I --- Quantum Key Distribution`
  (ch. 3--4, RQ2/RQ3), `Part II --- Post-Quantum Cryptography` (ch. 5--6, RQ1),
  and `Part III --- Programmable Datacenter Infrastructure` (ch. 7--8, RQ4).
  This unifies the previously parallel RQ and pillar taxonomies (pillar = Part),
  supersedes the earlier five-numbered-part scheme, and the Chapter 1 `field_venn`
  figure is relabelled to Part I/II/III to match.
- Standardize thesis figure generation via the `figure-generation` skill (`.cursor/skills/figure-generation/`): prefer draw.io (`.drawio` source + cropped PDF export) for diagrams/schematics, and matplotlib only for data plots.
- Dropped the "pillars" terminology in Chapter 1 in favor of simply calling them "Parts" (Parts I, II, and III), removing the awkward "pillars to parts" transition.
- Adopt the Okabe-Ito colorblind-safe palette for categorical figures (already in use in `figures/chapter1/`); use Crameri Scientific Colour Maps for continuous/sequential/diverging data.
- Match figure typography to the thesis body font (Latin Modern Roman / `lmodern`): serif in matplotlib, `fontFamily=Latin Modern Roman` in draw.io.
- Add `figures/thesis_style.py` as the canonical matplotlib style (palette constants + `apply_style()`).
- Reframe the three research pillars (Chapter 1 "Three Pillars" and the `field_venn` figure) as QKD, post-quantum cryptography, and programmable datacenter infrastructure (replacing the earlier PQC / topology-aware key-exchange / integrated-photonic-sources framing). The integrated photonic entanglement-source work now sits at the device layer of the QKD pillar, and the DPU/optical-fabric/observability substrate is promoted to its own infrastructure pillar. Updated `figures/chapter1/field_venn.drawio`/`.pdf` accordingly: papers/patents mapped as QKD-only (photonic sources; ROSE-QKD and quantum-network-authentication patents), QKD&cap;PQC (MHKE hybrid key-exchange patent), QKD&cap;infrastructure (QKD post-processing on DPU), PQC&cap;infrastructure (HQC/heterogeneous-DPU/edge-AI papers; PQC-offload-on-NIC patent), and infrastructure-only (RQ4 cross-layer: RDMA-over-optical-fabrics and the two confidential-AI observability papers). Final marker layout (author-adjusted in the `.drawio`): QKD-only papers 1--2; QKD&cap;infrastructure paper 3 plus two QKD-architecture patents (ROSE-QKD, quantum-network authentication); PQC&cap;infrastructure papers 4--6 plus the PQC-offload-on-NIC patent; infrastructure-only papers 7--9; QKD&cap;PQC empty; and a single multi-hybrid key-exchange patent (MHKE) at the all-three centre. The figure caption and surrounding Chapter 1 prose describe the overlaps and the single central patent rather than a populated triple centre.
