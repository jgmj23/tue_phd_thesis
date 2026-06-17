# 001 Collect Thesis Inputs

## Status

Done

## Goal

Collect and classify the initial files needed to set up the thesis build, structure, citation library, and first writing issues.

## Context

The repository has just been scaffolded around an issue-based workflow. The next step is to add official requirements, existing drafts, references, research artifacts, and advisor guidance.

## Allowed Files

- `source-materials/`
- `references/`
- `notes/`
- `README.md`
- `AGENTS.md`
- `.agents/issues/`

## Do Not Touch

- `chapters/`
- `frontmatter/`
- `appendices/`

## Expected Output

- Source files are placed in the appropriate `source-materials/` subfolders.
- Important constraints are summarized in `notes/decisions.md`.
- Follow-up writing, build-system, citation, and figure issues are created as needed.

## Acceptance Criteria

- Official thesis requirements are identifiable.
- Existing writing and advisor feedback are separated from generated drafts.
- Citation sources are identified and stored or documented.
- Large copyrighted paper libraries are kept out of Git unless explicitly approved.
- The next 3-5 concrete thesis issues are clear.

## Verification

Check repository status and confirm newly added files are either tracked intentionally or ignored intentionally:

```sh
git status --short
```

## Agent Notes

Received and copied initial university files into `source-materials/university/`:

- `Info-Package-PhD-april-2024.pdf`
- `Regulations-2021.pdf`
- `Model_titelblad_03.doc`
- `titelblad - meyer - 2026-06-17 09.35.59 - nl.docx`

Extracted text from both PDFs. Rendered both title-page Word files for visual inspection. Created `notes/university-requirements.md` and follow-up issues `002` through `005`.

Received user confirmations and committee details on 2026-06-17:

- Defense date confirmed as 2026-10-06 16:00.
- 5-month Hora Finita graduation-phase/committee approval step confirmed complete.
- Candidate name confirmed as Joseph Gideon Meyer.
- Birthplace supplied as Toronto, Ontario, Canada.
- Committee roles supplied from Hora Finita approval email.

Copied external Abraham Cano draft template locally to `source-materials/templates/abraham-cano-draft/`; it is ignored by Git.

Received publication-list input on 2026-06-17:

- Copied `/Users/jomeyer/Documents/PhD/CV/joey_publications.docx` to `source-materials/prior-writing/joey_publications.docx`.
- Copied `/Users/jomeyer/Documents/Projects/PROJECT_STATUS.md` to `source-materials/prior-writing/project-status-index.md`.
- Created `notes/publication-inventory.md` with the initial paper/patent inventory, project source paths, draft chapter buckets, and reference workflow.
- User stated this is expected to be a compilation-style thesis built mainly from about 10 publications plus introduction, transitions, and synthesis.
- User stated all listed papers can be assumed accepted for planning purposes.
- User stated patents cannot be expanded beyond title-level mention.
- User clarified the Edge AI paper source is `https://github.com/jgmj23/EDGEAI`, branch or source label `main_ica3pp`, and that it is not totally done yet.
- User clarified the ICSEE FSR-stability paper source is `https://github.com/jgmj23/ICSEE26---FSRstableDCM`.
- User clarified the Optics Letters paper and the ROSE-QKD paper do not belong in the thesis body; the ROSE-QKD patent does belong.
- User asked to keep camera-ready manuscripts as a separate issue that the user will handle later.
- Project sources were identified under `/Users/jomeyer/Documents/Projects/`, including HQConDPUs, Pisa, DCM, ConfidentialCompute, ICTON26_RDMA_Ordering, QKD_DPU_QCE26, and Rose_QKD.

## Review Result

Approved on 2026-06-17. Issue inputs are collected and classified; remaining work is split into follow-up issues.
