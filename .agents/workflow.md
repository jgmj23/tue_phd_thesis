# Agent Workflow

This thesis uses a **lightweight, trunk-based** workflow. See `AGENTS.md` for
the authoritative rules; this file is a short companion.

## Normal flow

1. Pick the next thing to work on (optionally from `.agents/backlog.md`).
2. Edit directly on `main`.
3. Run `make pdf` after any substantive change and confirm the build is clean.
4. Commit in small, logical chunks with a clear message.
5. Record substantive structural/terminology/citation/workflow decisions in
   `notes/decisions.md`.

No GitHub-issue sync, no per-task branches, no handoff/review notes are
required for routine writing.

## Parallel work (exception)

Only when several agents work at once on **non-overlapping files** (e.g.
different chapters), use short-lived `feature/short-title` branches and merge
back to `main` when each piece builds. Never run two agents on the same
chapter file simultaneously.

## History

The earlier issue-based workflow (numbered issues, GitHub sync, worktrees,
handoffs, reviews) is archived under `.agents/` for reference:
`issues/`, `handoffs/`, `reviews/`, and `status.md`. These are a historical
record of work done through June 2026 and are no longer actively maintained.
