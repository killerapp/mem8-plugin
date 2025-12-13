# CLI Ninja Patterns for AI-Powered ETL

Advanced command patterns that transform AI agents into CLI power users. Each pattern includes the problem, solution, and explanation.

## Table of Contents
- [JSON Processing with jq](#json-processing-with-jq)
- [YAML Processing with yq](#yaml-processing-with-yq)
- [Text Transformation with sd](#text-transformation-with-sd)
- [Code Search with ripgrep](#code-search-with-ripgrep)
- [AST-Based Refactoring with ast-grep](#ast-based-refactoring-with-ast-grep)
- [File Discovery with fd](#file-discovery-with-fd)
- [Pipeline Patterns](#pipeline-patterns)
- [Batch Processing](#batch-processing)

---

## JSON Processing with jq

### Extract nested values
```bash
# Get all user names from API response
curl -s https://api.example.com/users | jq -r '.data[].name'

# Get specific field with fallback
jq -r '.config.timeout // 30' config.json
```

### Transform structure
```bash
# Reshape API response to simpler format
jq '{users: [.data[] | {id, name, email}]}' response.json

# Flatten nested arrays
jq '[.results[].items[]]' nested.json
```

### Filter and select
```bash
# Find items matching condition
jq '.items[] | select(.status == "active")' data.json

# Multiple conditions
jq '.users[] | select(.age > 21 and .verified == true)' users.json

# Exclude null values
jq '.items[] | select(.email != null)' data.json
```

### Aggregate and compute
```bash
# Sum values
jq '[.transactions[].amount] | add' ledger.json

# Group by key
jq 'group_by(.category) | map({category: .[0].category, count: length})' items.json

# Unique values
jq '[.tags[]] | unique' posts.json
```

### Merge and combine
```bash
# Merge two JSON files
jq -s '.[0] * .[1]' base.json override.json

# Combine arrays from multiple files
jq -s '[.[].items[]]' file1.json file2.json file3.json
```

### Format conversion
```bash
# JSON to CSV
jq -r '.users[] | [.id, .name, .email] | @csv' users.json

# JSON to TSV
jq -r '.users[] | [.id, .name, .email] | @tsv' users.json

# Compact JSON (remove whitespace)
jq -c '.' pretty.json > compact.json
```

---

## YAML Processing with yq

### Read and extract
```bash
# Get value from YAML
yq '.spec.replicas' deployment.yaml

# Get all container images
yq '.spec.template.spec.containers[].image' deployment.yaml
```

### Modify in place
```bash
# Update a value
yq -i '.spec.replicas = 3' deployment.yaml

# Add a new field
yq -i '.metadata.annotations.updated = "2024-01-01"' deployment.yaml

# Delete a field
yq -i 'del(.spec.template.spec.containers[0].resources)' deployment.yaml
```

### Convert formats
```bash
# YAML to JSON
yq -o=json '.' config.yaml > config.json

# JSON to YAML
yq -P '.' config.json > config.yaml

# Multiple YAML docs to JSON array
yq -o=json -s '.' multi-doc.yaml
```

### Merge YAML files
```bash
# Merge with override (second file wins)
yq eval-all '. as $item ireduce ({}; . * $item)' base.yaml override.yaml

# Merge specific paths
yq '.spec.containers += load("sidecar.yaml").containers' deployment.yaml
```

---

## Text Transformation with sd

### Basic replacement
```bash
# Replace string (no escaping needed unlike sed)
sd 'old_text' 'new_text' file.txt

# Replace with capture groups
sd 'Hello (\w+)' 'Hi $1' file.txt

# Replace in-place
sd -i 'foo' 'bar' *.txt
```

### Common refactoring patterns
```bash
# Rename function calls
sd 'oldFunction\(' 'newFunction(' src/*.js

# Update import paths
sd "from 'old-module'" "from 'new-module'" src/**/*.ts

# Convert string quotes
sd "'" '"' file.js
```

### Multiline patterns
```bash
# Replace multiline block (use -s for string mode)
sd -s 'TODO: old task\nneeds work' 'DONE: completed' notes.md
```

---

## Code Search with ripgrep

### Basic search patterns
```bash
# Search with context
rg 'function.*async' -A 3 -B 1

# Search specific file types
rg 'import.*React' --type ts

# Exclude directories
rg 'TODO' --glob '!node_modules' --glob '!dist'
```

### Advanced patterns
```bash
# Find function definitions
rg '^(export\s+)?(async\s+)?function\s+\w+' --type js

# Find class with specific method
rg -U 'class \w+.*\n.*constructor' --type ts

# Count matches per file
rg 'console\.log' --count --type js
```

### Output formats for processing
```bash
# JSON output for further processing
rg 'TODO' --json | jq -r 'select(.type == "match") | .data.path.text'

# Just filenames
rg -l 'deprecated' --type py

# With line numbers for editing
rg -n 'FIXME' src/
```

### Search and replace (with confirmation)
```bash
# Preview changes
rg 'oldName' --files-with-matches | xargs -I {} sh -c 'echo "=== {} ==="; sd -p "oldName" "newName" {}'

# Apply changes
rg 'oldName' -l | xargs sd -i 'oldName' 'newName'
```

---

## AST-Based Refactoring with ast-grep

### Find patterns
```bash
# Find console.log statements
ast-grep --pattern 'console.log($$$)' --lang js

# Find async functions
ast-grep --pattern 'async function $NAME($$$) { $$$ }' --lang js

# Find React useState hooks
ast-grep --pattern 'const [$STATE, $SETTER] = useState($INIT)' --lang tsx
```

### Rewrite patterns
```bash
# Convert var to const
ast-grep --pattern 'var $NAME = $VALUE' --rewrite 'const $NAME = $VALUE' --lang js

# Add await to promise calls
ast-grep --pattern '$PROMISE.then($CALLBACK)' \
  --rewrite 'await $PROMISE' --lang js

# Convert class to functional component
ast-grep --pattern 'class $NAME extends React.Component { $$$ }' \
  --rewrite 'function $NAME(props) { $$$ }' --lang tsx
```

### Use YAML rules for complex transforms
```yaml
# rule.yaml
id: convert-console-to-logger
language: javascript
rule:
  pattern: console.log($MSG)
fix: logger.info($MSG)
```

```bash
ast-grep scan --rule rule.yaml src/
ast-grep scan --rule rule.yaml --update-all src/  # Apply fixes
```

### Find unused variables
```bash
# Find declared but unused
ast-grep --pattern 'const $VAR = $_' --lang ts | \
  while read line; do
    var=$(echo "$line" | grep -oP 'const \K\w+')
    count=$(rg -c "\b$var\b" --type ts | awk -F: '{sum+=$2} END {print sum}')
    [ "$count" -eq 1 ] && echo "Unused: $var in $line"
  done
```

---

## File Discovery with fd

### Find by pattern
```bash
# Find all TypeScript files
fd -e ts -e tsx

# Find specific filename
fd -g 'package.json'

# Find with regex
fd '.*\.test\.(js|ts)$'
```

### Find and execute
```bash
# Delete all .pyc files
fd -e pyc -x rm {}

# Format all Python files
fd -e py -x black {}

# Run tests for changed files
fd -e test.ts --changed-within 1h -x npx jest {}
```

### Find by attributes
```bash
# Find large files
fd --size +10m

# Find recently modified
fd --changed-within 24h

# Find empty directories
fd --type d --empty
```

---

## Pipeline Patterns

### JSON API to CSV report
```bash
curl -s https://api.example.com/orders | \
  jq -r '.orders[] | [.id, .customer, .total, .status] | @csv' | \
  tee orders.csv | \
  head -20
```

### Find and summarize code patterns
```bash
# Count TODO comments by file
rg -c 'TODO|FIXME|HACK' --type py | \
  sort -t: -k2 -rn | \
  head -10
```

### Batch file renaming
```bash
# Rename with pattern
fd -e jpg | while read f; do
  new=$(echo "$f" | sd '(\d{4})(\d{2})(\d{2})' '$1-$2-$3')
  mv "$f" "$new"
done
```

### Config validation pipeline
```bash
# Validate all YAML configs
fd -e yaml -e yml | while read f; do
  if ! yq '.' "$f" > /dev/null 2>&1; then
    echo "Invalid: $f"
  fi
done
```

### Git diff to structured data
```bash
# Changed files as JSON
git diff --name-status HEAD~5 | \
  awk '{print "{\"status\":\"" $1 "\",\"file\":\"" $2 "\"}"}' | \
  jq -s '.'
```

---

## Batch Processing

### Parallel execution
```bash
# Process files in parallel (4 jobs)
fd -e json | parallel -j4 'jq ".count" {} > {.}.count'

# With progress bar
fd -e csv | parallel --bar 'csvstat {} > {.}.stats'
```

### Chunked processing
```bash
# Process large file in chunks
split -l 10000 large.json chunk_
for f in chunk_*; do
  jq -c '.[] | select(.valid)' "$f" >> filtered.json
done
rm chunk_*
```

### Error handling in pipelines
```bash
# Continue on error, log failures
fd -e yaml | while read f; do
  if ! yq '.spec.replicas' "$f" 2>/dev/null; then
    echo "$f" >> failed.log
  fi
done
```

### Atomic file updates
```bash
# Safe in-place update (write to temp, then move)
for f in *.json; do
  jq '.updated = now' "$f" > "$f.tmp" && mv "$f.tmp" "$f"
done
```

---

## Quick Reference: Common One-Liners

```bash
# Pretty print JSON
cat file.json | jq '.'

# Extract all URLs from file
rg -o 'https?://[^\s"<>]+' file.txt

# Find largest directories
du -sh */ | sort -rh | head -10

# Watch file for changes and run command
watchexec -e py 'pytest'

# Compare two JSON files
diff <(jq -S '.' a.json) <(jq -S '.' b.json)

# Find duplicate files by content
fd -t f -x md5sum {} | sort | uniq -d -w32

# Convert all PNG to JPG
fd -e png -x convert {} {.}.jpg

# Kill process by port
lsof -ti:3000 | xargs kill -9

# Monitor log file with highlighting
tail -f app.log | rg --passthru 'ERROR|WARN'

# Generate random password
openssl rand -base64 32 | tr -d '/+=' | head -c 16
```
