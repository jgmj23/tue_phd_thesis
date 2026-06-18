# 006 Collect Camera-Ready Manuscripts

## Status

Partially collected; waiting on remaining manuscripts

## Goal

Collect the final camera-ready PDFs or accepted manuscript files for thesis-body publications once the user is ready to provide them.

## Context

The thesis is expected to be a compilation-style thesis. Issue `001` identified the publication set and issue `005` will ingest source text and bibliographies. The user asked to keep camera-ready manuscript collection as a separate issue that the user will handle later.

Large copyrighted paper libraries should stay out of Git unless explicitly approved. The local folder `source-materials/papers/` is ignored by Git and is the preferred drop location for PDFs or accepted manuscripts that should remain local-only.

On 2026-06-18, the user supplied six manuscript PDFs. The supplied PDFs were
normalized under `source-materials/papers/camera-ready/`. The three remaining
thesis-body manuscript PDFs are pending final versions and should stay open in
this issue.

## Allowed Files

- `source-materials/papers/`
- `source-materials/prior-writing/`
- `notes/`
- `.agents/issues/`

## Do Not Touch

- `chapters/`
- `frontmatter/`
- `appendices/`
- `references/thesis.bib`

## Expected Output

- Camera-ready or accepted manuscript files are placed in `source-materials/papers/` or another documented local-only location.
- `notes/publication-inventory.md` is updated with the file path for each supplied manuscript.
- Any manuscript that cannot be stored in Git is documented as local-only.

## Current Manuscript State

Supplied local-only PDFs:

| Publication | Local PDF |
| --- | --- |
| "Free Spectral Range Stability under Linear Thermal Tuning in a Dual-Coupled Microring Resonator" | `source-materials/papers/camera-ready/fsr-stability-dual-coupled-microring-camera-ready.pdf` |
| "Simulation-Driven Optimization of Dual-Coupled Micro-Ring Entanglement Sources for Quantum Optical Networks" | `source-materials/papers/camera-ready/dcm-entanglement-sources-quantum-networks-camera-ready.pdf` |
| "Offloading Post-Quantum Cryptography to Data Processing Units: A Performance Analysis of HQC Key Encapsulation" | `source-materials/papers/camera-ready/hqc-pqc-offload-bluefield-dpu-ieee-access-2026-published.pdf` |
| "Real-Time Post-Quantum Secured Image Pipeline on NVIDIA BlueField-3 DPU" | `source-materials/papers/camera-ready/real-time-pq-secured-image-pipeline-bluefield3-dpu-camera-ready.pdf` |
| "Exploiting Cross-QP Ordering in RDMA over Optical Fabrics" | `source-materials/papers/camera-ready/cross-qp-ordering-rdma-optical-fabrics-camera-ready.pdf` |
| "Cross-Layer Observability for Intrusion Detection in Confidential AI Training Clusters" | `source-materials/papers/camera-ready/cross-layer-observability-confidential-ai-training-clusters-camera-ready.pdf` |

Not yet supplied:

| Publication | Current note |
| --- | --- |
| "Design and Evaluation of a Heterogeneous DPU Architecture for Accelerating Post-Quantum Cryptography" | Final manuscript/PDF pending. |
| "QKD Post-Processing Offload on BlueField-3 DPUs: Towards Quantum-Secured RDMA in Datacenter Fabrics" | Final manuscript/PDF pending. |
| "Detecting Attacks in Confidential AI Training Without Payload Access: A DPU-Based Experimental Study" | Final manuscript/PDF pending. |

## Acceptance Criteria

- Each thesis-body paper has either a camera-ready/accepted manuscript file path or a clear note that it is still unavailable.
- Patent-only items remain title-only and are not expanded into manuscript text.
- Files intended to remain local-only are confirmed ignored by Git.

## Verification

Check repository status and confirm large manuscript/PDF files are not unintentionally tracked:

```sh
git status --short
git check-ignore -v source-materials/papers/*
```

## Agent Notes

Created from user instruction on 2026-06-17. This issue is intentionally waiting on the user.

2026-06-18: User supplied six PDFs in `source-materials/papers/`; filenames
were normalized under `source-materials/papers/camera-ready/` and
`notes/publication-inventory.md` was updated with supplied/pending manuscript
status. PDFs remain ignored by Git through the `source-materials/papers/`
ignore rule.

## Review Result

Pending.
