---
name: ffmpeg-compress-video
description: Compress video for web with quality presets
tools: [ffmpeg]
tags: [video, compression, web]
difficulty: beginner
verified: true
---

# Compress Video for Web

## Problem

Video files are too large for web upload, sharing, or storage. Need to reduce size while maintaining acceptable quality.

## Solution

```bash
# Good quality, reasonable size (CRF 23)
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac -b:a 128k output.mp4
```

## How It Works

1. `-c:v libx264` - Use H.264 codec (widely compatible)
2. `-crf 23` - Quality level (18-28 typical, lower=better)
3. `-preset medium` - Encoding speed vs compression tradeoff
4. `-c:a aac -b:a 128k` - Audio: AAC at 128kbps

## Variations

### Maximum compression (smaller file, lower quality)
```bash
ffmpeg -i input.mp4 -c:v libx264 -crf 28 -preset slow -c:a aac -b:a 96k small.mp4
```

### High quality (larger file)
```bash
ffmpeg -i input.mp4 -c:v libx264 -crf 18 -preset slow -c:a aac -b:a 192k hq.mp4
```

### Resize to 720p while compressing
```bash
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -vf scale=-1:720 -c:a aac output_720p.mp4
```

### Two-pass encoding (best quality/size ratio)
```bash
ffmpeg -i input.mp4 -c:v libx264 -b:v 1M -pass 1 -f null /dev/null
ffmpeg -i input.mp4 -c:v libx264 -b:v 1M -pass 2 output.mp4
```

### Quick preview (fast, larger file)
```bash
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset ultrafast preview.mp4
```

### Strip audio (video only)
```bash
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -an silent.mp4
```

## Quality Guide

| CRF | Quality | Typical Use |
|-----|---------|-------------|
| 18 | Visually lossless | Archive |
| 23 | Good (default) | General sharing |
| 28 | Acceptable | Web streaming |
| 35 | Low | Previews only |

## Common Pitfalls

- **Container format**: Output extension determines container (.mp4, .mkv)
- **Audio sync**: Issues may occur with variable framerate sources
- **Codec support**: H.264 is safest for compatibility

## See Also

- [ffmpeg quick reference](../../clis/ffmpeg/quick.md)
- [ffmpeg-extract-thumbnail](ffmpeg-extract-thumbnail.md)
