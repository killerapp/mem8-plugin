# PR Description Template

Use this template when describing pull requests. Copy this template to `thoughts/shared/prs/{pr_number}_description.md` and fill it out.

## What problem does this solve?

Describe the problem or need that this PR addresses. Link to any relevant issues.

## What changes were made?

### User-facing changes
- List any changes that affect end users
- Include new features, UI changes, behavior changes
- Note any breaking changes prominently

### Implementation details
- Describe the technical approach taken
- Highlight any architectural decisions
- Mention any new dependencies or tools added

## How to verify it

### Automated verification
- [ ] Unit tests pass: `npm test` / `pytest` / etc.
- [ ] Linting passes: `npm run lint` / `ruff check` / etc.
- [ ] Build succeeds: `npm run build` / `make build` / etc.
- [ ] Integration tests pass (if applicable)

### Manual verification
- [ ] Feature works as expected in development environment
- [ ] Edge cases have been tested
- [ ] Performance is acceptable
- [ ] Documentation is updated (if needed)

## Breaking changes

List any breaking changes and migration steps required.

## Changelog entry

Write a concise changelog entry for this change:

```
- Added/Fixed/Changed: Brief description of the change
```

## Additional context

Any additional context, screenshots, or information that reviewers should know.