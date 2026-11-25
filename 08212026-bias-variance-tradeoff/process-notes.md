# Process notes — Bias vs. Variance, Oversimplified

**Google Drive:** [02 Bias Variance tradeoff](https://drive.google.com/file/d/1y1Nk4S24TQ_2nRiNhHrATZcOxkUHeyur/view) (uploaded 3 Oct)
**Status:** delivered to Drive for review
**Resolution:** 3840×2160, 24 fps · **Runtime:** 2:56.6
**Built:** 17–23 Aug (master built 24 Aug)

Build notes for `claude-liam-bias-variance-tradeoff`. Append-only going forward.

## Build

- **Toolkit:** brutalist.art free path (Kokoro TTS + Manim + Remotion; no paid APIs).
- **Voice:** Kokoro `am_onyx`, generated and measured first; durations drive the cut.
- **Beats:** 10 — 6 Manim (in `scenes.py`), 4 Remotion.
- **Remotion components reused from the scene library:** `ClaudeComposerAsk`, `ClaudeTitleOutro`, `ClaudeVerdictArtifact`

## Status at build (from STATUS.md)

> STATUS — claude-liam-bias-variance-tradeoff
>
> 10/10 beats filled. Derived from beat_sheet.json — edit the sheet, not this file.
>
> | beat | status | fill method | who | slot | suggested prompt / search |
> |---|---|---|---|---|---|
> | B00 | ✅ filled | remotion | pipeline | `media/B00.mp4` |  |
> | B01 | ✅ filled | manim | pipeline | `manim/B01.mp4` |  |
> | B02 | ✅ filled | manim | pipeline | `manim/B02.mp4` |  |
> | B03 | ✅ filled | manim | pipeline | `manim/B03.mp4` |  |
> | B04 | ✅ filled | manim | pipeline | `manim/B04.mp4` |  |
> | B05 | ✅ filled | manim | pipeline | `manim/B05.mp4` |  |
> | B06 | ✅ filled | manim | pipeline | `manim/B06.mp4` |  |
> | B07 | ✅ filled | remotion | pipeline | `manim/B07.mp4` |  |
> | B08 | ✅ filled | remotion | pipeline | `media/B08.mp4` |  |
> | B09 | ✅ filled | remotion | pipeline | `manim/B09.mp4` |  |
