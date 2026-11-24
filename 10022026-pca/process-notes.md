# Process notes — PCA — Dimensionality Reduction Explained Visually

**Google Drive:** [14 Principal Component Analysis](https://drive.google.com/file/d/16tIVinbuyIlWZ_eBwJOxiCWnSBcP4Yp4/view) (uploaded 4 Oct)
**Status:** delivered to Drive for review · not yet published to YouTube
**Resolution:** 3840×2160, 24 fps · **Runtime:** 4:33.8
**Built:** 28 Sep – 4 Oct (master built 2 Oct)

Build notes for `claude-liam-pca`. Append-only going forward.

## Build

- **Toolkit:** brutalist.art free path (Kokoro TTS + Manim + Remotion; no paid APIs).
- **Voice:** Kokoro `am_onyx`, generated and measured first; durations drive the cut.
- **Beats:** 12 — 8 Manim (in `scenes.py`), 4 Remotion.
- **Remotion components reused from the scene library:** `ClaudeComposerAsk`, `ClaudeTitleOutro`, `ClaudeVerdictArtifact`

## Status at build (from STATUS.md)

> Status — PCA
>
> Status: COMPLETE — READY FOR HUMAN REVIEW
>
> - Narration: 12 beats, generated and measured with free local Kokoro audio
> - Pedagogy gate: PASS (approved 2026-09-21)
> - Fact-check: complete from primary and official references
> - Visuals: complete (8 native Manim beats and 4 Claude-style Remotion bookends)
> - Final master: `claude-liam-pca.mp4`
> - Runtime: 273.48 seconds (4:33.48)
> - Resolution: 1920×1080
> - Typecheck: PASS
> - Visual QC: PASS — 547 sampled frames at 2 fps across 22 contact sheets
> - Full decode: PASS
> - Publishing: not performed
>
> Ready for review and upload by the authorized reviewer.

**Note:** this STATUS.md predates the 4K re-render; the master on disk was re-probed at 3840×2160.
