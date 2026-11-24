# Process notes — Linear vs. Logistic Regression, Oversimplified

**Google Drive:** [03 Linear and Logistic regression](https://drive.google.com/file/d/1K_sJsQZUd6gjVJgL9WTlBuo06Ypa53eZ/view) (uploaded 4 Oct)
**Status:** delivered to Drive for review · not yet published to YouTube
**Resolution:** 3840×2160, 24 fps · **Runtime:** 3:16.6
**Built:** 24–28 Aug (master built 26 Aug)

Build notes for `claude-liam-linear-logistic-regression`. Append-only going forward.

## Build

- **Toolkit:** brutalist.art free path (Kokoro TTS + Manim + Remotion; no paid APIs).
- **Voice:** Kokoro `am_onyx`, generated and measured first; durations drive the cut.
- **Beats:** 10 — 7 Manim (in `scenes.py`), 3 Remotion.
- **Remotion components reused from the scene library:** `ClaudeComposerAsk`, `ClaudeTitleOutro`

## Status at build (from STATUS.md)

> STATUS — claude-liam-linear-logistic-regression
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
> | B07 | ✅ filled | manim | pipeline | `manim/B07.mp4` |  |
> | B08 | ✅ filled | remotion | pipeline | `media/B08.mp4` |  |
> | B09 | ✅ filled | manim | pipeline | `manim/B09.mp4` |  |
