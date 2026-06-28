# Paper Summaries (agent + author quick reference)

Last updated: 2026-06-28.

Purpose: a single place that captures, for every thesis-body paper, the
information an agent or author needs **without re-scanning the source PDF** —
real title, venue/status, full author list and affiliations, abstract, key
contributions, headline results, and the local source PDF. This is the
human/agent-readable companion to `references/my_contribution.bib` (the
machine-readable citation source consumed by LaTeX).

How the data flows in the build:

- `references/my_contribution.bib` holds the canonical bibliographic records
  (full author lists, venues, DOIs). Both the end-of-thesis **List of
  Publications** (`backmatter/publications.tex`) and each per-chapter
  **Included Publication** cover page (`\includedpaper` / `\includedpaperpending`
  in `includes.tex`) print from it via `\fullcite` / `\printbibliography`, with
  `maxbibnames=99` so every author name is shown.
- The author's name is rendered `{\textbf{\underline{J. G. Meyer}}}` wherever it
  falls in the true author order.

Source PDFs live under `source-materials/papers/camera-ready/` (gitignored,
local only). When a paper reaches camera-ready, swap `\includedpaperpending`
for `\includedpaper` in its chapter and point it at the PDF.

Author-order note: the author is **not first author** on P6 (J. S. García is
first) or P8 (A. Barreiro is first). The citations use true published order.

Title note: P1, P5, P6, P8, and P9 previously carried working titles in the
thesis that differed from the real paper titles; the thesis now uses the real
titles everywhere (bib, List of Publications, cover headings, chapter prose).

---

## P1 — Simulation-Driven Optimization of Dual-Coupled Micro-Ring Entanglement Sources for Quantum Optical Networks

- **Bib key:** `meyer2026icton` · **Chapter:** 03 (Integrated Quantum Sources) · `\includedpaper`
- **Venue / status:** 26th IEEE Int. Conf. on Transparent Optical Networks (ICTON), 2026 — Accepted
- **PDF:** `source-materials/papers/camera-ready/dcm-entanglement-sources-quantum-networks-camera-ready.pdf`
- **Authors (true order):** J. G. Meyer (corr.), A. Barreiro, A. Grebenchukov, E. Mentovich, J. A. Jaramillo-Villegas, J. J. Vegas Olmos, I. Tafur Monroy
- **Affiliations:** (1) NVIDIA, Yokneam Illit, IL; (2) Electrical Engineering, TU Eindhoven, NL; (3) Facultad de Ingenierías, Universidad Tecnológica de Pereira, CO
- **Topic:** integrated photonics / quantum sources
- **Abstract (condensed):** Dual-coupled micro-ring (DCM) resonators are a promising on-chip source of frequency-bin entangled photons, but spectral purity is highly sensitive to fabrication tolerances and thermal drift. Presents a coupled-mode-theory (CMT) **digital twin** of the DCM mapping device-level parameters (inter-ring coupling, dispersion, auxiliary-ring thermal detuning) to network-facing figures of merit (heralded purity, Schmidt number).
- **Key contributions:** the predictive CMT framework itself (not a single operating point); maps low-level physics to network metrics for pre-deployment configuration in hybrid quantum–classical WDM networks (C-band, 50 GHz channel spacing).
- **Headline results:** optimal auxiliary-cavity thermal tuning raises heralded purity by **up to 75%** at fixed brightness; reduces Schmidt number from **~1.8 to ~1.2**.

## P2 — Free Spectral Range Stability under Linear Thermal Tuning in a Dual-Coupled Microring Resonator

- **Bib key:** `meyer2026icsee` · **Chapter:** 03 (Integrated Quantum Sources) · `\includedpaper`
- **Venue / status:** IEEE Int. Conf. on Science and Electrical Engineering (ICSEE), 2026 — Presented
- **PDF:** `source-materials/papers/camera-ready/fsr-stability-dual-coupled-microring-camera-ready.pdf`
- **Authors (true order):** J. G. Meyer, A. Grebenchukov, A. Barreiro, J. A. Jaramillo-Villegas, J. J. Vegas Olmos, I. Tafur Monroy
- **Affiliations:** NVIDIA, Yokneam Illit, IL; Electrical Engineering, TU Eindhoven, NL; Universidad Tecnológica de Pereira, CO
- **Topic:** integrated photonics (TFLN), experimental device validation
- **Abstract (condensed):** Demonstrates linear thermo-optical tuning of a dual-coupled microring with very low FSR variation across nine modes, enabling thermally robust, spectrally stable operation for frequency-bin photonics, frequency combs, and co-packaged optics. Device in Thin-Film Lithium Niobate (TFLN); main/auxiliary rings 150 µm / 149 µm radius, 300 nm coupling gaps.
- **Key contributions:** first characterization of multi-mode FSR stability of a TFLN DCM under linear thermal tuning (prior work covered mode splitting / Vernier tuning but not simultaneous multi-mode thermal evolution).
- **Headline results:** **< 0.2% FSR variation** across nine modes under linear thermal tuning. Provides the experimental grounding for P1's simulation results.

## P3 — QKD Post-Processing Offload on BlueField-3 DPUs: Towards Quantum-Secured RDMA in Datacenter Fabrics

- **Bib key:** `meyer2026qkd` · **Chapter:** 04 (QKD Post-Processing on Programmable Network Hardware) · `\includedpaperpending` (PDF not yet embedded)
- **Venue / status:** IEEE Int. Conf. on Quantum Computing and Engineering (QCE / IEEE Quantum Week), Toronto, 2026 — In review
- **PDF:** `source-materials/papers/camera-ready/QKD_PostProc_DPUs.pdf` (draft)
- **Authors (true order):** J. G. Meyer (corr.), J. J. Vegas Olmos, I. Tafur Monroy
- **Affiliations:** NVIDIA, Yokneam Illit, IL; TU Eindhoven, NL
- **Topic:** QKD post-processing offload to DPU
- **Abstract (condensed):** First QKD-ready post-processing and key-injection architecture that offloads the **entire** classical pipeline (sifting, LDPC error correction, privacy amplification) onto an NVIDIA BlueField-3 DPU, running natively on the DPU's Arm Cortex-A78 cores, and injects distilled keys directly into the hardware IPsec engine. A synthetic BB84 source emulates the quantum channel with reproducible QBER for systematic hardware sweeps; classical post-processing and key injection run on real BlueField-3 hardware.
- **Key contributions:** collapses key generation and consumption into a single SmartNIC; enables line-rate encryption of RDMA traffic with zero host CPU usage; demonstrates feasibility of a quantum-secured RDMA (Q-RDMA) fabric.
- **Headline results:** sustains secure key rates **up to 0.18 Mbps at 1% QBER** with **zero host CPU utilization**; RDMA latency/throughput identical to standard MACsec, key-rotation jitter negligible.

## P4 — Offloading Post-Quantum Cryptography to Data Processing Units: A Performance Analysis of HQC Key Encapsulation

- **Bib key:** `meyer2026hqc` · **Chapter:** 05 (DPU-Accelerated PQC) · `\includedpaper`
- **Venue / status:** IEEE Access, vol. 14, pp. 53831–53845, 2026 — **Published**, DOI 10.1109/ACCESS.2026.3681219
- **PDF:** `source-materials/papers/camera-ready/hqc-pqc-offload-bluefield-dpu-ieee-access-2026-published.pdf`
- **Authors (true order):** J. Meyer (corr.), E. Mentovich, I. Tafur Monroy, J. J. Vegas Olmos
- **Affiliations:** TU Eindhoven, NL; NVIDIA, Yokneam Illit, IL
- **Topic:** PQC offload (code-based KEM) to DPU
- **Abstract (condensed):** First experimental evaluation of offloading **HQC** key encapsulation (NIST 4th-round code-based KEM) to high-capacity DPUs. Compares host x86 execution vs DPU-offloaded execution on NVIDIA BlueField-3 (400 Gbit/s) across three security levels and four server-load regimes, single- and multi-threaded. Argues architectural isolation gives predictable PQC performance under contention.
- **Headline results:** under idle, host ~22% lower latency; under moderate–heavy contention, DPU **31–34% lower latency** (advantage grows with security level). Multi-threaded DPU throughput scales near-linearly, exceeding host by **up to 2.9× (idle)** and **5.5× (heavy load)**. Determinism: host latency variance **> 34%** under heavy load vs DPU **< 0.1%** regardless of host/DPU background activity.

## P5 — GPU-Accelerated Post-Quantum Cryptography on Embedded DPU Architecture

- **Bib key:** `meyer2026heterogeneous` · **Chapter:** 05 (DPU-Accelerated PQC) · `\includedpaperpending` (PDF not yet embedded)
- **Venue / status:** IEEE Networking Letters, 2026 — In review
- **PDF:** `source-materials/papers/camera-ready/pqc_networking_letters_final.pdf` (draft)
- **Authors (true order):** J. Meyer (corr.), A. Cano Aguilera, F. Cugini, I. Tafur Monroy, J. J. Vegas Olmos
- **Affiliations:** NVIDIA, Yokneam Illit, IL; TU Eindhoven, NL; CNIT, Pisa, IT (Cugini)
- **Topic:** heterogeneous (embedded GPU) DPU PQC acceleration
- **Abstract (condensed):** First characterization of GPU-accelerated PQC on a DPU with an **embedded** GPU (NVIDIA BlueField-2 + integrated A30) where Arm cores and GPU share one memory domain, eliminating PCIe overhead and freeing Arm cores for network functions. Evaluates ML-KEM (FIPS 203) and ML-DSA (FIPS 204) across NIST levels and batch sizes 1–1000.
- **Headline results:** CPU–GPU crossover at batch **~10**; speedups **up to 46× (ML-KEM)** and **94× (ML-DSA)** over single-threaded Arm CPU; extends TLS 1.3 capacity to **~62,000 conn/s** (~12× the 8-core CPU limit) at a worst-case **14–36 ms** per-handshake latency dominated by batch-accumulation delay, not GPU processing.
- **Note:** prior thesis working title was "Design and Evaluation of a Heterogeneous DPU Architecture for Accelerating Post-Quantum Cryptography."

## P6 — Real-Time Post-Quantum Secured Image Pipeline on NVIDIA BlueField-3 DPU

- **Bib key:** `meyer2026edgeai` · **Chapter:** 06 (Post-Quantum Security for Edge AI Pipelines) · `\includedpaper`
- **Venue / status:** IEEE Int. Conf. on Algorithms and Architectures for Parallel Processing (ICA3PP), 2026 — In review
- **PDF:** `source-materials/papers/camera-ready/real-time-pq-secured-image-pipeline-bluefield3-dpu-camera-ready.pdf` (`EDGEAI.pdf` is a near-identical earlier copy of the same paper)
- **Authors (true order):** **J. S. García (1st)**, J. G. Meyer (2nd), I. Tafur Monroy, J. J. Vegas Olmos, S. Kosta
- **Affiliations:** Dept. of Electronic Systems, Aalborg University, Copenhagen, DK (García, Kosta); NVIDIA, Yokneam Illit, IL; TU Eindhoven, NL
- **Topic:** edge-AI secure image pipeline offload to DPU
- **Abstract (condensed):** Edge-AI pipelines must decode, preprocess, validate — and now (with PQC) authenticate and decrypt — every frame. Conventional host-CPU or GPU paths incur overhead or steal SM capacity, and expose decrypted frames in the host trust domain. Proposes terminating frames at network ingress on the DPU's general-purpose cores (authenticate, decrypt, preprocess), then transferring an inference-ready tensor to the GPU, preserving GPU SMs and isolating key material/plaintext from the host. Implemented on BlueField-3, using ML-KEM/ML-DSA.
- **Headline results:** on a single Arm core the secure receive path sustains **1080p at 85 fps (JPEG)** and **98 fps (TIFF)**; per-frame PQC stage consumes only **23%** of the 30-fps budget for a raw 1080p payload.
- **Note:** prior thesis working title was "Securing Edge AI Pipelines: Offloading Image I/O and Post-Quantum Cryptography to DPUs." Author is **second** author.

## P7 — Exploiting Cross-QP Ordering in RDMA over Optical Fabrics

- **Bib key:** `meyer2026rdma` · **Chapter:** 07 (Ordering, Timing, and Optical Fabric Attacks) · `\includedpaper`
- **Venue / status:** 26th IEEE Int. Conf. on Transparent Optical Networks (ICTON), 2026 — Accepted
- **PDF:** `source-materials/papers/camera-ready/cross-qp-ordering-rdma-optical-fabrics-camera-ready.pdf`
- **Authors (true order):** J. Meyer, I. Tafur-Monroy, J. J. Vegas Olmos
- **Affiliations:** Electrical Engineering, TU Eindhoven, NL; NVIDIA, Yokneam Illit, IL
- **Topic:** RDMA/RoCEv2 cross-QP ordering attack via optical-layer timing
- **Abstract (condensed):** InfiniBand/RoCEv2 guarantees message ordering within a single Queue Pair (QP) but not across QPs; high-performance apps multiplex many QPs and assume cross-QP delivery stays ~FIFO. Quantifies how much timing perturbation moves the common case into one where applications observe stale data, and argues the optical physical layer (compromised ROADM, inline delay line, malicious OCS schedule) is the most plausible injection site.
- **Headline results:** a production-class ConnectX-7 RoCEv2 pair already shows **42 stale reads / 100,000 iterations** at 1,024-byte payload in a flag/data handoff. On a software-RoCE (RXE) testbed, a single Gaussian-jittered `netem` egress rule drives corruption from **0.03% (0 delay)** to **41.93% at 50 µs** mean delay, approaching a 50% asymptote past 200 µs — exploitable with sub-millisecond timing control on one ECMP path.

## P8 — Cross-Layer Observability for Intrusion Detection in Confidential AI Training Clusters

- **Bib key:** `meyer2026intrusion` · **Chapter:** 08 (Observability for Confidential AI Infrastructure) · `\includedpaper`
- **Venue / status:** 26th IEEE Int. Conf. on Transparent Optical Networks (ICTON), 2026 — Accepted
- **PDF:** `source-materials/papers/camera-ready/cross-layer-observability-confidential-ai-training-clusters-camera-ready.pdf`
- **Authors (true order):** **A. Barreiro (1st, corr.)**, J. G. Meyer (2nd), D. C. Lawo, I. Tafur Monroy, J. J. Vegas Olmos
- **Affiliations:** Electrical Engineering, TU Eindhoven, NL; NVIDIA, Yokneam Illit, IL
- **Topic:** intrusion-detection framework for confidential AI training
- **Abstract (condensed):** Confidential computing + end-to-end encryption on east–west RDMA links make payload DPI infeasible and constrain host-based IDS via kernel bypass and enclave isolation. Presents a systematic IDS framework: maps **thirteen attacks** into **three detectability tiers** based on visibility across a three-layer signal surface (network, infrastructure, workload) that survives encryption and TEE boundaries. Introduces **defensive inversion** (repurposing side-channel-style signals as anomaly-detection features) and outlines a cross-layer DPU-based monitoring architecture.
- **Note:** prior thesis working title was "Intrusion Detection for Confidential AI Training Clusters: A Cross-Layer Observability Framework." Author is **second** author. Closely related to P9 (same problem space, different paper).

## P9 — Obscured, But Not Blind: Systematizing Observability in Confidential AI Training Clusters

- **Bib key:** `meyer2026detecting` · **Chapter:** 08 (Observability for Confidential AI Infrastructure) · `\includedpaperpending` (PDF not yet embedded)
- **Venue / status:** IEEE Transactions on Information Forensics and Security (TIFS), 2026 — In review
- **PDF:** `source-materials/papers/camera-ready/Conf_Compute_TIFS.pdf` (draft)
- **Authors (true order):** J. G. Meyer (corr.), I. Tafur Monroy, J. J. Vegas Olmos
- **Affiliations:** Electrical Engineering, TU Eindhoven, NL; NVIDIA, Yokneam Illit, IL
- **Topic:** systematization + experimental study of observability limits in confidential AI clusters
- **Abstract (condensed):** Hardware isolation (NVIDIA H100 CC, Intel TDX, AMD SEV-SNP) and end-to-end encryption blind traditional IDS, but the field lacks a systematic account of what observability *remains*. Systematizes the metadata that survives encryption and the TEE boundary across three layers (network, infrastructure, workload); for each layer establishes, from first principles and prior work, the footprint an attack is predicted to leave, and validates with worked-example measurements from two testbeds (a GPU training cluster and a DPU testbed). Defines theoretical limits of metadata-only detection (covert-channel noise floor; attacks that leave no footprint by design).
- **Headline results:** resource attacks (RDMA flooding, bandwidth squatting) remain visible from the architecturally isolated **DPU vantage** (validated under IPsec); training-disruption attacks surface as outliers in collective timing. Closes with a research agenda and design guidance for cross-layer, DPU-vantage IDS.
- **Note:** prior thesis working title was "Detecting Attacks in Confidential AI Training Without Payload Access: A DPU-Based Experimental Study." This is the journal-length companion to P8.

---

## Patents (title-level only)

Per `notes/publication-inventory.md`, patents are tracked at title level only and
cannot be expanded beyond title/status without approved disclosure language.
They are listed (numbered I1–I4) in the end-of-thesis List of Publications, and
are also mentioned at title level in the relevant chapters' "Contribution and
Articles" sections: the PQC-offload patent in Ch 5, and MHKE / ROSE-QKD / the
quantum-node authentication patent in Ch 4.

| Bib key | Title | Status |
| --- | --- | --- |
| `meyer-patent-mhke` | Multi-Hybrid Cryptographic Key Exchange (MHKE) | filed |
| `meyer-patent-pqcoffload` | Computational Offloading of Operations Necessary for Post-Quantum Cryptography on Network Interface Cards | filed |
| `meyer-patent-roseqkd` | ROSE-QKD: Receiver-Only, Semi-Honest Emitter Quantum Key Distribution | filed |
| `meyer-patent-qnetauth` | Capability-Based Authentication of Quantum Nodes via Statistical Analysis | draft (application) |

## Open follow-ups

- Replace the four `\includedpaperpending` placeholders (P3, P5, P9 — and P6 if a
  newer camera-ready arrives) with `\includedpaper` once camera-ready PDFs land.
- Confirm final venue/status wording at submission time (P3 QCE, P5 Networking
  Letters, P6 ICA3PP, P9 TIFS are all in review as of this note).
- The author's specific per-paper contribution paragraphs in chapters 05–08 are
  still `TODO`; fill from the contribution statements once finalized.
