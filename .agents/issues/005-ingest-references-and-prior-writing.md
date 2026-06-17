# 005 Ingest References And Prior Writing

## Status

Ready

## Goal

Bring in the citation library and existing scientific writing so agents can start chapter planning without inventing claims or citations.

## Context

The repo currently has official university requirements but not the thesis bibliography, prior papers, proposal text, or chapter drafts.

## Allowed Files

- `source-materials/references/`
- `source-materials/prior-writing/`
- `references/`
- `notes/literature/`
- `.agents/issues/`

## Do Not Touch

- `chapters/`
- `frontmatter/`

## Expected Output

- `references/thesis.bib` or a documented path to the exported bibliography.
- Notes identifying existing drafts and reusable prior text.
- Follow-up issues for chapter outlines and literature synthesis.

## Acceptance Criteria

- Citation keys are available before chapter drafting begins.
- Prior writing is classified by source and reuse status.
- Any copied/adapted text is traceable back to its source.
- Follow-up chapter issues include citation/source context.

## Verification

Check that citation files parse and that source-material paths are documented.

## Agent Notes

Initial publication-list and project-index inputs are available:

- `source-materials/prior-writing/joey_publications.docx`
- `source-materials/prior-writing/project-status-index.md`
- `notes/publication-inventory.md`

The publication inventory identifies candidate paper sources and bibliographies in local project folders:

- HQC/PQC DPU paper: `/Users/jomeyer/Documents/Projects/HQConDPUs/Round2/HQC_on_DPUs-Resubmission-2/`
- GPU/DPU PQC paper: `/Users/jomeyer/Documents/Projects/Pisa/NetworkingLetters/`
- DCM ICTON paper: `/Users/jomeyer/Documents/Projects/DCM/ICTON26_DCM/`
- DCM ICSEE paper: source repository supplied by user at `https://github.com/jgmj23/ICSEE26---FSRstableDCM`; `/Users/jomeyer/Documents/Projects/DCM/ICSEE26/` has PDF/presentation.
- Confidential-compute ICTON paper: `/Users/jomeyer/Documents/Projects/ConfidentialCompute/agents/paperA_icton/Overleaf/`
- Confidential-compute payload-free detection manuscript: likely `/Users/jomeyer/Documents/Projects/ConfidentialCompute/agents/paperB_tifs/draft/`
- RDMA/optical ordering paper: likely latest source in `/Users/jomeyer/Documents/Projects/ICTON26_RDMA_Ordering/Paper/`
- Edge AI paper: source repository supplied by user at `https://github.com/jgmj23/EDGEAI`, branch or source label `main_ica3pp`; user noted it is not totally done yet.
- QKD DPU paper: `/Users/jomeyer/Documents/Projects/QKD_DPU_QCE26/paper/`

User stated all listed papers can be assumed accepted for planning purposes.
Patent material should be title-only unless approved disclosure language is supplied.
User clarified that the Optics Letters paper and the ROSE-QKD paper do not belong in the thesis body; the ROSE-QKD patent title does belong.
Camera-ready and accepted manuscript PDFs are deferred to issue `006-collect-camera-ready-manuscripts`.

## Review Result

Pending.
