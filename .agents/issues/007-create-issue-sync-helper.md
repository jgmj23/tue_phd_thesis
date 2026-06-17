# 007 Create Issue Sync Helper

## Status

Open

## Goal

Create a reusable helper, and possibly a Codex skill, that keeps local `.agents/issues/*.md`, `.agents/status.md`, and GitHub Issues synchronized.

## Context

Issue `006` was created locally but did not appear on GitHub until `gh issue create` was run manually. The repository workflow now requires explicit sync, but a helper would reduce future mistakes.

Potential implementation options:

- A repo-local script such as `scripts/sync-github-issues`.
- A Codex skill for issue creation/sync workflows, created under the user's Codex skills directory if approved.
- Both: a deterministic repo-local script plus a skill that tells agents when and how to run it.

If creating a Codex skill, follow the `skill-creator` skill instructions, ask where to create the skill, and validate the generated skill before marking this issue complete.

## Allowed Files

- `AGENTS.md`
- `.agents/`
- `scripts/`
- `notes/`

## Do Not Touch

- `chapters/`
- `frontmatter/`
- `appendices/`
- `references/thesis.bib`

## Expected Output

- A documented command or skill workflow that creates missing GitHub issues from local issue files.
- The helper updates `.agents/status.md` with GitHub issue links.
- The helper can close GitHub issues when local issues are marked `Done`, or clearly documents that closing remains manual.

## Acceptance Criteria

- Running the helper on an already-synced repo is idempotent.
- New local issues are created on GitHub and linked in `.agents/status.md`.
- The workflow handles GitHub authentication/network failures clearly.
- The helper does not create duplicate GitHub issues for existing local issues.

## Verification

Run the helper in dry-run mode if implemented, or on a test issue if safe:

```sh
git status --short
```

## Agent Notes

Created after user requested that issue sync happen automatically and suggested a possible skill for issue creation.

## Review Result

Pending.
