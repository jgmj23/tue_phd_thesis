# Publication Inventory

Last updated: 2026-06-28.

This note records the initial publication inputs for a compilation-style thesis.
The source list is `source-materials/prior-writing/joey_publications.docx`,
with additional publication details from
`/Users/jomeyer/Documents/PhD/CV/cv/publications.tex`, project status from
`source-materials/prior-writing/project-status-index.md`, and the Year 1
activity report copied from
`/Users/jomeyer/Documents/PhD/Admin/Activity report - Joey.doc`.

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

## Local Prior-Writing Sources

| Source | Local file | Use |
| --- | --- | --- |
| Publication list | `source-materials/prior-writing/joey_publications.docx` | Initial candidate publication inventory. |
| Project status index | `source-materials/prior-writing/project-status-index.md` | Source paths and project-status notes. |
| Activity report, February 1st 2025--February 1st 2026 | `source-materials/prior-writing/activity-report-2025-2026-joey.doc`; searchable extraction in `source-materials/prior-writing/activity-report-2025-2026-joey.txt` | Go/No-Go framing for the thesis theme, research pillars, and Chapter 1--2 structure. |

## Candidate Paper Set

| Topic | Publication | Status assumption | Local source status |
| --- | --- | --- | --- |
| DPU/PQC | "Design and Evaluation of a Heterogeneous DPU Architecture for Accelerating Post-Quantum Cryptography" | in review (IEEE Networking Letters) | Source in `/Users/jomeyer/Documents/Projects/Pisa/NetworkingLetters/pqc_networking_letters_final.tex`; bibliography in `/Users/jomeyer/Documents/Projects/Pisa/NetworkingLetters/references.bib`. |
| DPU/PQC | "Offloading Post-Quantum Cryptography to Data Processing Units: A Performance Analysis of HQC Key Encapsulation" | accepted / published | Source in `/Users/jomeyer/Documents/Projects/HQConDPUs/Round2/HQC_on_DPUs-Resubmission-2/access.tex`; bibliography in `/Users/jomeyer/Documents/Projects/HQConDPUs/Round2/HQC_on_DPUs-Resubmission-2/references.bib`; DOI listed in CV as `10.1109/ACCESS.2026.3681219`. |
| Quantum photonics | "Free Spectral Range Stability under Linear Thermal Tuning in a Dual-Coupled Microring Resonator" | accepted | Source repository supplied by user: `https://github.com/jgmj23/ICSEE26---FSRstableDCM`. Local final PDF and presentation also found in `/Users/jomeyer/Documents/Projects/DCM/ICSEE26/`. |
| Quantum photonics | "Simulation-Driven Optimization of Dual-Coupled Micro-Ring Entanglement Sources for Quantum Networks" | accepted / invited | Source in `/Users/jomeyer/Documents/Projects/DCM/ICTON26_DCM/main.tex`; bibliography in `/Users/jomeyer/Documents/Projects/DCM/ICTON26_DCM/refs.bib`. |
| Confidential AI / DPU observability | "Intrusion Detection for Confidential AI Training Clusters: A Cross-Layer Observability Framework" | accepted / invited | Source in `/Users/jomeyer/Documents/Projects/ConfidentialCompute/agents/paperA_icton/Overleaf/1_main.tex`; bibliography in `/Users/jomeyer/Documents/Projects/ConfidentialCompute/agents/paperA_icton/Overleaf/references.bib`. |
| Optical/RDMA security | "Exploiting Cross-QP Ordering in RDMA over Optical Fabrics" | accepted / invited | Candidate latest source in `/Users/jomeyer/Documents/Projects/ICTON26_RDMA_Ordering/Paper/1_main.tex`; bibliography in `/Users/jomeyer/Documents/Projects/ICTON26_RDMA_Ordering/Paper/references.bib`. Older parallel source also exists under `icton26_rdma/`. |
| Confidential AI / DPU observability | "Detecting Attacks in Confidential AI Training Without Payload Access: A DPU-Based Experimental Study" | in review (IEEE TIFS) | Draft source likely in `/Users/jomeyer/Documents/Projects/ConfidentialCompute/agents/paperB_tifs/draft/paperB_full_draft.tex`; bibliography source still needs confirmation. |
| Edge AI / DPU/PQC | "Securing Edge AI Pipelines: Offloading Image I/O and Post-Quantum Cryptography to DPUs" | in review (ICA3PP) | Source repository supplied by user: `https://github.com/jgmj23/EDGEAI`, branch or source label `main_ica3pp`. |
| QKD/DPU | "QKD Post-Processing Offload on BlueField-3 DPUs: Towards Quantum-Secured RDMA in Datacenter Fabrics" | in review (IEEE Quantum Week / QCE, Toronto) | Source in `/Users/jomeyer/Documents/Projects/QKD_DPU_QCE26/paper/paper.tex`; bibliography in `/Users/jomeyer/Documents/Projects/QKD_DPU_QCE26/paper/bibliography.bib`. |

## Camera-Ready / Accepted Manuscript Files

Manuscript PDFs are local-only thesis inputs. They live under
`source-materials/papers/`, which is ignored by Git.

| Publication | Manuscript status | Local PDF |
| --- | --- | --- |
| "Free Spectral Range Stability under Linear Thermal Tuning in a Dual-Coupled Microring Resonator" | supplied 2026-06-18; camera-ready PDF | `source-materials/papers/camera-ready/fsr-stability-dual-coupled-microring-camera-ready.pdf` |
| "Simulation-Driven Optimization of Dual-Coupled Micro-Ring Entanglement Sources for Quantum Optical Networks" | supplied 2026-06-18; camera-ready PDF | `source-materials/papers/camera-ready/dcm-entanglement-sources-quantum-networks-camera-ready.pdf` |
| "Offloading Post-Quantum Cryptography to Data Processing Units: A Performance Analysis of HQC Key Encapsulation" | supplied 2026-06-18; published IEEE Access PDF | `source-materials/papers/camera-ready/hqc-pqc-offload-bluefield-dpu-ieee-access-2026-published.pdf` |
| "Real-Time Post-Quantum Secured Image Pipeline on NVIDIA BlueField-3 DPU" | supplied 2026-06-18; accepted/camera-ready manuscript PDF | `source-materials/papers/camera-ready/real-time-pq-secured-image-pipeline-bluefield3-dpu-camera-ready.pdf` |
| "Exploiting Cross-QP Ordering in RDMA over Optical Fabrics" | supplied 2026-06-18; camera-ready PDF | `source-materials/papers/camera-ready/cross-qp-ordering-rdma-optical-fabrics-camera-ready.pdf` |
| "Cross-Layer Observability for Intrusion Detection in Confidential AI Training Clusters" | supplied 2026-06-18; camera-ready PDF | `source-materials/papers/camera-ready/cross-layer-observability-confidential-ai-training-clusters-camera-ready.pdf` |
| "QKD Post-Processing Offload on BlueField-3 DPUs: Towards Quantum-Secured RDMA in Datacenter Fabrics" | supplied 2026-06-28; in review at IEEE Quantum Week (QCE, Toronto); draft PDF | `source-materials/papers/camera-ready/QKD_PostProc_DPUs.pdf` |
| "Detecting Attacks in Confidential AI Training Without Payload Access: A DPU-Based Experimental Study" | supplied 2026-06-28; in review at IEEE TIFS; draft PDF | `source-materials/papers/camera-ready/Conf_Compute_TIFS.pdf` |
| "Securing Edge AI Pipelines: Offloading Image I/O and Post-Quantum Cryptography to DPUs" | supplied 2026-06-28; in review at ICA3PP; draft PDF | `source-materials/papers/camera-ready/EDGEAI.pdf` |
| "Design and Evaluation of a Heterogeneous DPU Architecture for Accelerating Post-Quantum Cryptography" | in review at IEEE Networking Letters; draft PDF not yet in `camera-ready/` folder (user noted a draft is attached) | TODO: drop draft PDF into `source-materials/papers/camera-ready/` |

## Not In Thesis Body

The following publications may remain in the CV/publication list, but the user
confirmed they should not be treated as thesis-body compilation papers:

- "Analogy of free-space quantum key distribution using spatial modes of light:
  scaling up the distance and the dimensionality," Optics Letters 50, 3297-3300
  (2025).
- ROSE-QKD as a paper/manuscript. The ROSE-QKD patent title does belong and is
  tracked under patent handling below. It may be mentioned as title-level
  context for scalable QKD architecture, but it is not a thesis-body paper.

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

## Planned Paper-Centric Thesis Structure

This structure keeps the thesis paper-centric while grouping related papers
inside a broader cross-layer narrative. Paper chapters should use a consistent
wrapper: chapter motivation, relation to research questions, publication
context and author contribution, included paper, post-paper discussion, and
link to the next chapter.

| Part | Chapter | Included papers |
| --- | --- | --- |
| Thesis Frame | Introduction | No included paper. Frames quantum-resilient communication as an architecture problem, states scope, research questions, research pillars, contributions, and dissertation organization. |
| Thesis Frame | Background and Unifying Concepts | No included paper. Establishes shared background for PQC deployment, programmable network infrastructure, scalable QKD architectures, integrated photonic sources, and cross-layer architecture evaluation. |
| Quantum Photonic and Quantum-Secured Network Foundations | Integrated Quantum Sources for Quantum Networks | "Free Spectral Range Stability under Linear Thermal Tuning in a Dual-Coupled Microring Resonator"; "Simulation-Driven Optimization of Dual-Coupled Micro-Ring Entanglement Sources for Quantum Networks". |
| Quantum Photonic and Quantum-Secured Network Foundations | QKD Post-Processing on Programmable Network Hardware | "QKD Post-Processing Offload on BlueField-3 DPUs: Towards Quantum-Secured RDMA in Datacenter Fabrics". |
| Post-Quantum Cryptography in Programmable Network Infrastructure | DPU-Accelerated Post-Quantum Cryptography | "Offloading Post-Quantum Cryptography to Data Processing Units: A Performance Analysis of HQC Key Encapsulation"; "Design and Evaluation of a Heterogeneous DPU Architecture for Accelerating Post-Quantum Cryptography". |
| Post-Quantum Cryptography in Programmable Network Infrastructure | Post-Quantum Security for Edge AI Pipelines | "Securing Edge AI Pipelines: Offloading Image I/O and Post-Quantum Cryptography to DPUs". TODO: confirm final acceptance/source state before thesis inclusion. |
| Cross-Layer Security in Datacenter Fabrics and Confidential AI | Ordering, Timing, and Optical Fabric Attacks | "Exploiting Cross-QP Ordering in RDMA over Optical Fabrics". |
| Cross-Layer Security in Datacenter Fabrics and Confidential AI | Observability for Confidential AI Infrastructure | "Intrusion Detection for Confidential AI Training Clusters: A Cross-Layer Observability Framework"; "Detecting Attacks in Confidential AI Training Without Payload Access: A DPU-Based Experimental Study". TODO: confirm bibliography source for the second paper. |
| Synthesis | Cross-Layer Lessons and Future Outlook | No included paper. Synthesizes the thesis-level claims, limitations, and future work. |

## Open Inputs

- Merge and clean project bibliographies into `references/thesis.bib` (ongoing;
  references are added as chapters are drafted).
- Drop the Heterogeneous DPU / PQC (IEEE Networking Letters) draft PDF into
  `source-materials/papers/camera-ready/`; it is the only thesis-body
  manuscript still missing a local file.
- Note: the three confidential-AI/QKD/edge manuscripts dropped on 2026-06-28
  are in-review drafts, not camera-ready. Replace them with camera-ready
  versions once accepted.
