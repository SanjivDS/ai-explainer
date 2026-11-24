# Process notes — Regression Metrics: MAE, MSE, RMSE, R², and MAPE, Oversimplified

**Google Drive:** [07 Regression metrics](https://drive.google.com/file/d/101egQCDPU8kCuz3jkgSu-RqlZuBC40Hd/view) (uploaded 3 Oct)
**Status:** delivered to Drive for review · not yet published to YouTube
**Resolution:** 3840×2160, 24 fps · **Runtime:** 3:37.5
**Built:** 14–20 Sep (master built 3 Oct)

Build notes for `claude-liam-regression-metrics`. Append-only going forward.

## Build

- **Toolkit:** brutalist.art free path (Kokoro TTS + Manim + Remotion; no paid APIs).
- **Voice:** Kokoro `am_onyx`, generated and measured first; durations drive the cut.
- **Beats:** 10 — 6 Manim (in `scenes.py`), 4 Remotion.
- **Remotion components reused from the scene library:** `ClaudeComposerAsk`, `ClaudeTitleOutro`, `ClaudeVerdictArtifact`

## Status at build (from STATUS.md)

> STATUS — claude-liam-regression-metrics
>
> 4K rebuild
>
> Status: COMPLETE — 4K MASTER READY FOR GOOGLE DRIVE REVIEW
>
> All ten source beats and the final delivery master have been verified at
> 3840×2160. The previous delivery master was assembled at a lower resolution;
> it is retained as `claude-liam-regression-metrics-1080p-archive.mp4`.
>
> - 4K master: `claude-liam-regression-metrics-4k.mp4`
> - Runtime: 217.34 seconds
> - Frame rate: 24 fps
> - Video/audio: H.264 + AAC
> - Full decode: PASS
> - Visual QC: PASS — 435 frames sampled at 2 fps across 18 sheets
> - Publishing: not performed
>
> 10/10 beats filled. Derived from beat_sheet.json — edit the sheet, not this file.
>
> | beat | status | fill method | who | slot | suggested prompt / search |
> |---|---|---|---|---|---|
> | B00 | ✅ filled | remotion | pipeline | `media/B00.mp4` |  |
> | B01 | ✅ filled | ai-video-prompt | human | `manim/B01.mp4` | Here is the whole idea in one breath. Every metric starts with the gap between prediction  |
> | B02 | ✅ filled | ai-video-prompt | human | `manim/B02.mp4` | Start with residuals: actual value minus predicted value. Their signs tell direction, but  |
> | B03 | ✅ filled | ai-video-prompt | human | `manim/B03.mp4` | Use one tiny example: actual values two, four, six, and eight; predictions three, five, fi |
> | B04 | ✅ filled | ai-video-prompt | human | `manim/B04.mp4` | Now change only the error pattern. Model A misses every case by two. Model B is exact thre |
> | B05 | ✅ filled | ai-video-prompt | human | `manim/B05.mp4` | R squared changes the question. Instead of asking how many units you missed by, it asks ho |
> | B06 | ✅ filled | ai-video-prompt | human | `manim/B06.mp4` | MAPE looks friendly because it says percent, but the denominator is the actual value. If a |
> | B07 | ✅ filled | remotion | pipeline | `media/B07.mp4` |  |
> | B08 | ✅ filled | remotion | pipeline | `media/B08.mp4` |  |
> | B09 | ✅ filled | remotion | pipeline | `media/B09.mp4` |  |
