# Publication Inventory

Last updated: 2026-06-17.

This note records the initial publication inputs for a compilation-style thesis.
The source list is `source-materials/prior-writing/joey_publications.docx`,
with additional publication details from
`/Users/jomeyer/Documents/PhD/CV/cv/publications.tex` and project status from
`source-materials/prior-writing/project-status-index.md`.

Working assumption from the user: all listed manuscripts can be treated as
accepted for thesis-planning purposes.

## Reference Workflow

The thesis should use one canonical bibliography file,
`references/thesis.bib`.

This does not replace the reference sections inside the original papers as
published artifacts. Instead, it consolidates the BibTeX records needed by the
thesis into a single citation library so chapter text, introduction text, and
transition text can cite sources consistently. Paper-specific `.bib` files
remain source inputs and should be merged, deduplicated, and checked before
chapter drafting.

## Candidate Paper Set

| Topic | Publication | Status assumption | Local source status |
| --- | --- | --- | --- |
| DPU/PQC | "Design and Evaluation of a Heterogeneous DPU Architecture for Accelerating Post-Quantum Cryptography" | accepted | Source in `/Users/jomeyer/Documents/Projects/Pisa/NetworkingLetters/pqc_networking_letters_final.tex`; bibliography in `/Users/jomeyer/Documents/Projects/Pisa/NetworkingLetters/references.bib`. |
| DPU/PQC | "Offloading Post-Quantum Cryptography to Data Processing Units: A Performance Analysis of HQC Key Encapsulation" | accepted / published | Source in `/Users/jomeyer/Documents/Projects/HQConDPUs/Round2/HQC_on_DPUs-Resubmission-2/access.tex`; bibliography in `/Users/jomeyer/Documents/Projects/HQConDPUs/Round2/HQC_on_DPUs-Resubmission-2/references.bib`; DOI listed in CV as `10.1109/ACCESS.2026.3681219`. |
| Quantum photonics | "Free Spectral Range Stability under Linear Thermal Tuning in a Dual-Coupled Microring Resonator" | accepted | Source repository supplied by user: `https://github.com/jgmj23/ICSEE26---FSRstableDCM`. Local final PDF and presentation also found in `/Users/jomeyer/Documents/Projects/DCM/ICSEE26/`. |
| Quantum photonics | "Simulation-Driven Optimization of Dual-Coupled Micro-Ring Entanglement Sources for Quantum Networks" | accepted / invited | Source in `/Users/jomeyer/Documents/Projects/DCM/ICTON26_DCM/main.tex`; bibliography in `/Users/jomeyer/Documents/Projects/DCM/ICTON26_DCM/refs.bib`. |
| Confidential AI / DPU observability | "Intrusion Detection for Confidential AI Training Clusters: A Cross-Layer Observability Framework" | accepted / invited | Source in `/Users/jomeyer/Documents/Projects/ConfidentialCompute/agents/paperA_icton/Overleaf/1_main.tex`; bibliography in `/Users/jomeyer/Documents/Projects/ConfidentialCompute/agents/paperA_icton/Overleaf/references.bib`. |
| Optical/RDMA security | "Exploiting Cross-QP Ordering in RDMA over Optical Fabrics" | accepted / invited | Candidate latest source in `/Users/jomeyer/Documents/Projects/ICTON26_RDMA_Ordering/Paper/1_main.tex`; bibliography in `/Users/jomeyer/Documents/Projects/ICTON26_RDMA_Ordering/Paper/references.bib`. Older parallel source also exists under `icton26_rdma/`. |
| Confidential AI / DPU observability | "Detecting Attacks in Confidential AI Training Without Payload Access: A DPU-Based Experimental Study" | accepted | Draft source likely in `/Users/jomeyer/Documents/Projects/ConfidentialCompute/agents/paperB_tifs/draft/paperB_full_draft.tex`; bibliography source still needs confirmation. |
| Edge AI / DPU/PQC | "Securing Edge AI Pipelines: Offloading Image I/O and Post-Quantum Cryptography to DPUs" | in progress; assume eventual acceptance for planning | Source repository supplied by user: `https://github.com/jgmj23/EDGEAI`, branch or source label `main_ica3pp`. User noted it is not totally done yet. |
| QKD/DPU | "QKD Post-Processing Offload on BlueField-3 DPUs: Towards Quantum-Secured RDMA in Datacenter Fabrics" | accepted / submitted | Source in `/Users/jomeyer/Documents/Projects/QKD_DPU_QCE26/paper/paper.tex`; bibliography in `/Users/jomeyer/Documents/Projects/QKD_DPU_QCE26/paper/bibliography.bib`. |

## Not In Thesis Body

The following publications may remain in the CV/publication list, but the user
confirmed they should not be treated as thesis-body compilation papers:

- "Analogy of free-space quantum key distribution using spatial modes of light:
  scaling up the distance and the dimensionality," Optics Letters 50, 3297-3300
  (2025).
- ROSE-QKD as a paper/manuscript. The ROSE-QKD patent title does belong and is
  tracked under patent handling below.

## Patent Handling

The user indicated patents cannot be expanded on beyond title-level mention.
Use only titles/statuses unless the user later provides approved disclosure
language.

| Patent title | Status from publication list |
| --- | --- |
| Multi-Hybrid Cryptographic Key Exchange (MHKE) | filed |
| Computational offloading of operations necessary for Post-Quantum Cryptography on NV NICs | filed |
| Rose-QKD | filed |
| Authentication of Quantum Network | draft |

## Draft Chapter Buckets

These are planning buckets only, not final chapter titles.

1. Quantum photonic and QKD systems: DCM FSR stability, DCM entanglement-source optimization, QKD post-processing offload, and title-only ROSE-QKD patent context where permitted.
2. DPU-accelerated post-quantum and edge security: HQC on DPUs, GPU/DPU PQC acceleration, edge AI pipeline offload.
3. Secure network fabrics and confidential AI observability: optical/RDMA ordering attacks, confidential AI intrusion detection, payload-free DPU-based attack detection.

## Open Inputs

- Merge and clean project bibliographies into `references/thesis.bib`.
- Camera-ready or accepted manuscript PDFs are deferred to issue `006-collect-camera-ready-manuscripts`.
