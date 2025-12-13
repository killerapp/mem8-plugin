---
name: docker-cleanup-all
description: Clean all Docker resources - containers, images, volumes, networks
tools: [docker]
tags: [docker, cleanup, devops]
difficulty: beginner
verified: true
---

# Docker Full Cleanup

## Problem

Docker accumulates unused containers, images, volumes, and networks over time, consuming disk space.

## Solution

```bash
# Nuclear option - remove everything unused
docker system prune -a --volumes -f
```

## How It Works

1. `docker system prune` - Remove unused data
2. `-a` - Remove all unused images (not just dangling)
3. `--volumes` - Also remove unused volumes
4. `-f` - Force, no confirmation prompt

## Variations

### Step by step (more control)
```bash
# Stop all containers
docker stop $(docker ps -aq)

# Remove all containers
docker rm $(docker ps -aq)

# Remove all images
docker rmi $(docker images -q)

# Remove all volumes
docker volume rm $(docker volume ls -q)

# Remove all networks (except defaults)
docker network rm $(docker network ls -q)
```

### Clean only old/unused
```bash
# Remove containers stopped >24h ago
docker container prune --filter "until=24h" -f

# Remove images older than 7 days
docker image prune -a --filter "until=168h" -f
```

### Show what would be removed (dry run)
```bash
# Preview before pruning
docker system df -v
```

### Clean builder cache
```bash
docker builder prune -a -f
```

### Check space before/after
```bash
echo "Before:" && docker system df
docker system prune -a --volumes -f
echo "After:" && docker system df
```

## Common Pitfalls

- **Data loss**: `--volumes` will delete persistent data
- **Running containers**: Won't remove containers that are running
- **Named volumes**: Consider if you need to preserve any

## See Also

- [docker-stats-json](docker-stats-json.md)
