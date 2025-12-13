# ffmpeg Quick Reference

**Check**: `ffmpeg -version`
**Install**: `brew install ffmpeg` | `apt install ffmpeg` | `scoop install ffmpeg`

## Top 10 Patterns

```bash
# 1. Compress video for web (H.264, reasonable quality)
ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset medium -c:a aac output.mp4

# 2. Extract audio from video
ffmpeg -i video.mp4 -vn -acodec mp3 audio.mp3

# 3. Extract thumbnail at specific time
ffmpeg -i video.mp4 -ss 00:00:05 -vframes 1 thumbnail.jpg

# 4. Convert format
ffmpeg -i input.mov -c:v libx264 -c:a aac output.mp4

# 5. Resize video (720p)
ffmpeg -i input.mp4 -vf scale=-1:720 -c:a copy output_720p.mp4

# 6. Create GIF from video
ffmpeg -i video.mp4 -vf "fps=10,scale=480:-1" -t 5 output.gif

# 7. Trim video (start to duration)
ffmpeg -i input.mp4 -ss 00:01:00 -t 00:00:30 -c copy clip.mp4

# 8. Concatenate videos
ffmpeg -f concat -i list.txt -c copy output.mp4
# list.txt: file 'video1.mp4'\nfile 'video2.mp4'

# 9. Extract frames as images
ffmpeg -i video.mp4 -vf fps=1 frame_%04d.png

# 10. Add watermark
ffmpeg -i video.mp4 -i logo.png -filter_complex "overlay=10:10" output.mp4
```

## Essential Flags

| Flag | Purpose |
|------|---------|
| `-i` | Input file |
| `-c:v` | Video codec |
| `-c:a` | Audio codec |
| `-crf` | Quality (0-51, lower=better) |
| `-preset` | Speed vs compression |
| `-ss` | Start time |
| `-t` | Duration |
| `-vf` | Video filter |
| `-vn` | No video |
| `-an` | No audio |

## Quality Presets (CRF)

| CRF | Quality | Use Case |
|-----|---------|----------|
| 18 | Visually lossless | Archive |
| 23 | Good (default) | General |
| 28 | Okay | Web streaming |
| 35+ | Low | Previews |

## See Also

- [Full reference](reference.md)
- [Media recipes](../../recipes/media/)
