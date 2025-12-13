---
name: ffmpeg-extract-thumbnail
description: Extract frame from video as thumbnail image
tools: [ffmpeg]
tags: [video, thumbnail, image]
difficulty: beginner
verified: true
---

# Extract Video Thumbnail

## Problem

Need to generate a thumbnail/preview image from a video file.

## Solution

```bash
# Extract frame at 5 seconds
ffmpeg -i video.mp4 -ss 00:00:05 -vframes 1 thumbnail.jpg
```

## How It Works

1. `-ss 00:00:05` - Seek to 5 seconds (before -i for fast seeking)
2. `-vframes 1` - Extract exactly 1 frame
3. Output format determined by extension (.jpg, .png)

## Variations

### Extract at specific timestamp
```bash
ffmpeg -ss 00:01:30 -i video.mp4 -vframes 1 thumbnail.jpg
```

### Extract and resize
```bash
ffmpeg -i video.mp4 -ss 00:00:05 -vframes 1 -vf scale=320:-1 thumb_small.jpg
```

### Higher quality JPEG
```bash
ffmpeg -i video.mp4 -ss 00:00:05 -vframes 1 -q:v 2 thumbnail.jpg
```

### PNG for transparency/lossless
```bash
ffmpeg -i video.mp4 -ss 00:00:05 -vframes 1 thumbnail.png
```

### Extract multiple frames (1 per second)
```bash
ffmpeg -i video.mp4 -vf fps=1 frame_%04d.jpg
```

### Extract from middle of video
```bash
# Get duration, extract at 50%
duration=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 video.mp4)
middle=$(echo "$duration / 2" | bc)
ffmpeg -ss $middle -i video.mp4 -vframes 1 thumbnail.jpg
```

### Batch extract from multiple videos
```bash
for video in *.mp4; do
  ffmpeg -ss 00:00:05 -i "$video" -vframes 1 "${video%.mp4}_thumb.jpg"
done
```

### Create thumbnail grid/montage
```bash
ffmpeg -i video.mp4 -vf "select='not(mod(n,100))',scale=160:-1,tile=4x4" -frames:v 1 grid.jpg
```

## Common Pitfalls

- **-ss position**: Put BEFORE -i for fast seeking, AFTER for accurate seeking
- **Black frames**: First few seconds might be black, seek further in
- **Aspect ratio**: Use `scale=WIDTH:-1` to maintain aspect ratio

## See Also

- [ffmpeg quick reference](../../clis/ffmpeg/quick.md)
- [ffmpeg-compress-video](ffmpeg-compress-video.md)
