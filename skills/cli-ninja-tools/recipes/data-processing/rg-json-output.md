---
name: rg-json-output
description: Use ripgrep JSON output for structured search result processing
tools: [rg, jq]
tags: [search, json, code-analysis]
difficulty: intermediate
verified: true
---

# Structured Search with ripgrep + jq

## Problem

Need search results in a structured format for further processing, reporting, or integration with other tools.

## Solution

```bash
# Get matches as JSON, extract file paths
rg 'TODO' --json | jq -r 'select(.type == "match") | .data.path.text'
```

## How It Works

1. `rg 'pattern' --json` - Output as JSON lines (one per event)
2. `select(.type == "match")` - Filter to only match events (not summary/context)
3. `.data.path.text` - Extract the file path

## Variations

### Get file, line number, and match text
```bash
rg 'TODO:(.*)' --json | jq -r '
  select(.type == "match") |
  "\(.data.path.text):\(.data.line_number): \(.data.lines.text)"
'
```

### Count matches by file
```bash
rg 'TODO' --json | jq -s '
  [.[] | select(.type == "match") | .data.path.text] |
  group_by(.) | map({file: .[0], count: length}) |
  sort_by(-.count)
'
```

### Extract to structured JSON report
```bash
rg 'TODO|FIXME|HACK' --json | jq -s '[
  .[] | select(.type == "match") | {
    file: .data.path.text,
    line: .data.line_number,
    match: .data.lines.text | gsub("^\\s+|\\s+$"; "")
  }
]'
```

### Find files with most matches
```bash
rg 'console\.log' --json --type js | jq -s '
  [.[] | select(.type == "match") | .data.path.text] |
  group_by(.) | map({file: .[0], count: length}) |
  sort_by(-.count) | .[0:10]
'
```

### Export to CSV
```bash
rg 'TODO' --json | jq -r '
  select(.type == "match") |
  [.data.path.text, .data.line_number, .data.lines.text] | @csv
' > todos.csv
```

## Common Pitfalls

- **JSON lines**: Each line is separate JSON, use `jq -s` to slurp into array
- **Event types**: Filter for "match" type, ignore "begin", "end", "summary"
- **Large output**: Add `| head -100` to limit during testing

## See Also

- [rg quick reference](../../clis/rg/quick.md)
- [jq quick reference](../../clis/jq/quick.md)
