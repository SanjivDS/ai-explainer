# Process notes — ROC Curve and AUC Score, Oversimplified

**Google Drive:** [06 ROC Curve and AUC score](https://drive.google.com/file/d/1cE8CXoM1571tTQPFkmWbB59qHPDf-yz3/view) (uploaded 3 Oct)
**Status:** delivered to Drive for review
**Resolution:** 3840×2160, 24 fps · **Runtime:** 3:25.0
**Built:** 7–13 Sep (master built 9 Sep)

Build notes for `claude-liam-roc-curve-auc-score`. Append-only going forward.

## Build

- **Toolkit:** brutalist.art free path (Kokoro TTS + Manim + Remotion; no paid APIs).
- **Voice:** Kokoro `am_onyx`, generated and measured first; durations drive the cut.
- **Beats:** 10 — 6 Manim (in `scenes.py`), 4 Remotion.
- **Remotion components reused from the scene library:** `ClaudeComposerAsk`, `ClaudeTitleOutro`, `ClaudeVerdictArtifact`

## Status at build (from STATUS.md)

> STATUS — claude-liam-roc-curve-auc-score
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
> | B07 | ✅ filled | remotion | pipeline | `media/B07.mp4` |  |
> | B08 | ✅ filled | remotion | pipeline | `media/B08.mp4` |  |
> | B09 | ✅ filled | remotion | pipeline | `media/B09.mp4` |  |
