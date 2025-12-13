---
name: docker-stats-json
description: Get Docker container stats in JSON format for processing
tools: [docker, jq]
tags: [docker, monitoring, json]
difficulty: intermediate
verified: true
---

# Docker Stats as JSON

## Problem

Need container resource usage (CPU, memory, network) in a structured format for monitoring or alerting.

## Solution

```bash
# Get stats for all containers as JSON
docker stats --no-stream --format '{{json .}}' | jq -s '.'
```

## How It Works

1. `docker stats` - Show container resource usage
2. `--no-stream` - Single snapshot (not continuous)
3. `--format '{{json .}}'` - Output as JSON
4. `jq -s '.'` - Collect into array

## Variations

### Get specific fields
```bash
docker stats --no-stream --format '{{json .}}' | jq '{
  name: .Name,
  cpu: .CPUPerc,
  mem: .MemUsage,
  net: .NetIO
}'
```

### Find high CPU containers (>50%)
```bash
docker stats --no-stream --format '{{json .}}' | jq '
  select((.CPUPerc | gsub("%"; "") | tonumber) > 50)
'
```

### Memory usage sorted
```bash
docker stats --no-stream --format '{{json .}}' | jq -s '
  sort_by(.MemPerc | gsub("%"; "") | tonumber) | reverse
'
```

### Export to CSV
```bash
docker stats --no-stream --format '{{.Name}},{{.CPUPerc}},{{.MemUsage}}' > stats.csv
```

### Continuous monitoring to file
```bash
while true; do
  docker stats --no-stream --format '{{json .}}' | \
    jq -c '{time: now | todate, stats: .}' >> docker-stats.jsonl
  sleep 60
done
```

### Alert on high memory
```bash
docker stats --no-stream --format '{{json .}}' | jq -r '
  select((.MemPerc | gsub("%"; "") | tonumber) > 80) |
  "ALERT: \(.Name) using \(.MemPerc) memory"
'
```

## Common Pitfalls

- **Percentage parsing**: Values include `%`, need to strip for math
- **No containers**: Returns empty if no containers running
- **Format escaping**: Use single quotes around Go template

## See Also

- [jq quick reference](../../clis/jq/quick.md)
- [docker-cleanup-all](docker-cleanup-all.md)
