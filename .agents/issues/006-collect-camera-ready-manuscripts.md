# 006 Collect Camera-Ready Manuscripts

## Status

Waiting on User

## Goal

Collect the final camera-ready PDFs or accepted manuscript files for thesis-body publications once the user is ready to provide them.

## Context

The thesis is expected to be a compilation-style thesis. Issue `001` identified the publication set and issue `005` will ingest source text and bibliographies. The user asked to keep camera-ready manuscript collection as a separate issue that the user will handle later.

Large copyrighted paper libraries should stay out of Git unless explicitly approved. The local folder `source-materials/papers/` is ignored by Git and is the preferred drop location for PDFs or accepted manuscripts that should remain local-only.

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

## Review Result

Pending.
