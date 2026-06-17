# Agent Workflow

Use one issue as the unit of work.

## Normal Flow

1. Create or choose an issue in `.agents/issues/`.
2. If creating a new issue, immediately create the matching GitHub issue with `gh issue create`.
3. Update `.agents/status.md` with the GitHub issue number/link. `Pending` is only allowed as a short-lived state before sync.
4. Start a branch named `codex/issue-NNN-short-title`.
5. Create a worktree at `.worktrees/NNN-short-title`.
6. Have one agent work only inside that issue's allowed file scope.
7. Run the issue's verification command.
8. Write a handoff note in `.agents/handoffs/NNN-short-title.md`.
9. Review into `.agents/reviews/NNN-short-title-review.md`.
10. If the issue is complete, close the matching GitHub issue with `gh issue close`.
11. Merge back to `main` only when the work is accepted and local/GitHub issue states match.

## Good New-Chat Prompt

```text
Read AGENTS.md and .agents/issues/NNN-short-title.md.
Create/use branch codex/issue-NNN-short-title and worktree .worktrees/NNN-short-title.
Work only on that issue's allowed files.
When done, run the verification command, update the issue status, sync the matching GitHub issue, and write a handoff note.
```

## Coordination Rules

- Keep this main thread as the coordinator when several issues are active.
- Use separate chats only for separate issues with non-overlapping file scopes.
- Do not run two agents on the same chapter file at the same time.
- If an issue discovers new scope, create a follow-up issue instead of expanding silently.
- When creating that follow-up issue, create the GitHub issue in the same turn and update `.agents/status.md`; do not leave the GitHub column as `Pending` before merge.
- Each agent should leave the repo in a state that another agent can inspect without guessing what happened.

## GitHub Sync Commands

Create a GitHub issue from a local issue file:

```sh
gh issue create --repo jgmj23/tue_phd_thesis \
  --title "NNN Short Title" \
  --body-file .agents/issues/NNN-short-title.md
```

Close a completed GitHub issue:

```sh
gh issue close N --repo jgmj23/tue_phd_thesis \
  --comment "Completed in COMMIT_SHA. Summary..."
```

Verify remote state:

```sh
gh issue view N --repo jgmj23/tue_phd_thesis --json state,title,url
```
