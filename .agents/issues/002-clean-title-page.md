# 002 Clean Title Page

## Status

Done

## Goal

Turn the personalized TU/e title-page draft into a clean, compliant two-page title block that can later be reproduced in the thesis source.

## Context

Source files:

- `source-materials/university/titelblad - meyer - 2026-06-17 09.35.59 - nl.docx`
- `source-materials/university/Model_titelblad_03.doc`
- `notes/university-requirements.md`

The personalized file currently renders as three A4 pages and still includes instructional highlighted text. The model title page renders as two A4 pages.

## Allowed Files

- `source-materials/university/`
- `frontmatter/`
- `notes/university-requirements.md`
- `.agents/issues/`

## Do Not Touch

- `chapters/`
- `references/`
- `research/`

## Expected Output

- A clean record of exact title-page fields needed for the thesis.
- A list of missing user-confirmed fields.
- Eventually, a reproducible title-page source in `frontmatter/`.

## Acceptance Criteria

- Candidate name matches passport exactly.
- Birthplace and country are complete and in Dutch.
- Defense date is in Dutch and matches the approved defense date.
- Role assignments for chair, promotors, copromotors, members, and advisers are complete.
- TU/e affiliation and external-affiliation rules are followed.
- No instructional highlights or template comments remain in final title-page content.
- Rendered title block fits the intended two-page TU/e format.

## Verification

Render the title-page artifact and visually inspect every page for overflow, clipping, comments, highlights, and page count.

## Agent Notes

Resolved fields:

- Full name: Joseph Gideon Meyer.
- Working birth line: `geboren te Toronto, Ontario, Canada`.
- Defense date: dinsdag 6 oktober 2026 om 16:00 uur.
- Promotor: prof.dr.ir. I. Tafur Monroy.
- Copromotoren: dr.ir. J.J. Vegas Olmos; dr. E. Mentovich.
- Adviser: dr. V.E. Gauthier Umaña.
- Chair/voorzitter: prof.dr. O. Raz.
- Reserve member printed as `Reservelid`: prof.dr. N. Calabretta.
- Tectonic build succeeds with the current title-page source.
- Rendered title pages were visually inspected.
- Re-rendered pages 1-2 after adding the reserve member; no overflow,
  clipping, comments, or highlights were visible.

Open fields:

- None.

## Review Result

Approved for merge.
