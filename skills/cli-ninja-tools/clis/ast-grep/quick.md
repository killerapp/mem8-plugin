# ast-grep (sg) Quick Reference

**Check**: `sg --version`
**Install**: `brew install ast-grep` | `cargo install ast-grep --locked` | `npm i -g @ast-grep/cli`

## Top 10 Patterns

```bash
# 1. Find console.log statements
sg --pattern 'console.log($$$)' --lang js

# 2. Find async functions
sg --pattern 'async function $NAME($$$) { $$$ }' --lang js

# 3. Find React useState
sg --pattern 'const [$STATE, $SETTER] = useState($INIT)' --lang tsx

# 4. Find imports from module
sg --pattern "import $_ from 'lodash'" --lang ts

# 5. Rewrite: var to const
sg --pattern 'var $NAME = $VALUE' --rewrite 'const $NAME = $VALUE' --lang js

# 6. Rewrite: promise to await
sg --pattern '$PROMISE.then($CB)' --rewrite 'await $PROMISE' --lang js

# 7. Find class components
sg --pattern 'class $NAME extends React.Component { $$$ }' --lang tsx

# 8. Find function calls
sg --pattern 'oldFunc($ARGS)' --lang js

# 9. Interactive mode
sg --pattern 'console.log($$$)' --interactive --lang js

# 10. Use rule file
sg scan --rule rule.yaml src/
```

## Pattern Syntax

| Pattern | Matches |
|---------|---------|
| `$VAR` | Single AST node |
| `$$$` | Zero or more nodes |
| `$_` | Single node (don't capture) |

## YAML Rule Example

```yaml
# rule.yaml
id: convert-console-to-logger
language: javascript
rule:
  pattern: console.log($MSG)
fix: logger.info($MSG)
```

```bash
# Scan with rule
sg scan --rule rule.yaml src/

# Apply fixes
sg scan --rule rule.yaml --update-all src/
```

## Essential Flags

| Flag | Purpose |
|------|---------|
| `--pattern` | Search pattern |
| `--rewrite` | Replacement |
| `--lang` | Language (js/ts/tsx/py/go/...) |
| `--interactive` | Preview changes |
| `--json` | JSON output |

## See Also

- [Full reference](reference.md)
- [AST patterns cookbook](../../recipes/code-analysis/)
