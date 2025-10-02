
2. set up worktree for implementation:
2a. create a new worktree using the mem8 CLI: `mem8 worktree create 123 BRANCH_NAME`

3. determine required data:

branch name
path to plan file (use relative path only)
launch prompt
command to run

**IMPORTANT PATH USAGE:**
- The thoughts/ directory is synced between the main repo and worktrees
- Always use ONLY the relative path starting with `thoughts/shared/...` without any directory prefix
- Example: `thoughts/shared/plans/fix-mcp-keepalive-proper.md` (not the full absolute path)
- This works because thoughts are synced and accessible from the worktree

3a. confirm with the user by sending a message to the Human

```
based on the input, I plan to create a worktree with the following details:

worktree path: ~/wt/mem8/123
branch name: BRANCH_NAME
path to plan file: $FILEPATH
launch prompt:

    /implement_plan at $FILEPATH and when you are done implementing and all tests pass, read ./claude/commands/commit.md and create a commit, then read ./claude/commands/describe_pr.md and create a PR, then add a comment to the GitHub issue with the PR link

command to run:

    mem8 dashboard -w ~/wt/mem8/123 "/implement_plan at $FILEPATH and when you are done implementing and all tests pass, read ./claude/commands/commit.md and create a commit, then read ./claude/commands/describe_pr.md and create a PR, then add a comment to the Linear ticket with the PR link"
```

incorporate any user feedback then:

4. launch implementation session: `mem8 dashboard -w ~/wt/mem8/123 "/implement_plan at $FILEPATH and when you are done implementing and all tests pass, read ./claude/commands/commit.md and create a commit, then read ./claude/commands/describe_pr.md and create a PR, then add a comment to the Linear ticket with the PR link"`
