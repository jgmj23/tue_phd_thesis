# Agent Workflow

Use one issue as the unit of work.

## Normal Flow

1. Create or choose an issue in `.agents/issues/`.
2. Start a branch named `codex/issue-NNN-short-title`.
3. Create a worktree at `.worktrees/NNN-short-title`.
4. Have one agent work only inside that issue's allowed file scope.
5. Run the issue's verification command.
6. Write a handoff note in `.agents/handoffs/NNN-short-title.md`.
7. Review into `.agents/reviews/NNN-short-title-review.md`.
8. Merge back to `main` only when the work is accepted.

## Good New-Chat Prompt

```text
Read AGENTS.md and .agents/issues/NNN-short-title.md.
Create/use branch codex/issue-NNN-short-title and worktree .worktrees/NNN-short-title.
Work only on that issue's allowed files.
When done, run the verification command, update the issue status, and write a handoff note.
```

## Coordination Rules

- Keep this main thread as the coordinator when several issues are active.
- Use separate chats only for separate issues with non-overlapping file scopes.
- Do not run two agents on the same chapter file at the same time.
- If an issue discovers new scope, create a follow-up issue instead of expanding silently.
- Each agent should leave the repo in a state that another agent can inspect without guessing what happened.

