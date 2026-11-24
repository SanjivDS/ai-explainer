# Process notes — Entropy vs Gini Impurity

**Google Drive:** [16 Entropy and Gini Impurity](https://drive.google.com/file/d/18uo3Szq3xQPllJUmH9YBMH78c7yEEE6X/view) (uploaded 11 Oct)
**Status:** delivered to Drive for review · not yet published to YouTube
**Resolution:** 3840×2160, 24 fps · **Runtime:** 3:41.7
**Built:** 28 Sep – 4 Oct (master built 4 Oct)

Build notes for `claude-liam-entropy-vs-gini`. Append-only going forward.

## Build

- **Toolkit:** brutalist.art free path (Kokoro TTS + Manim + Remotion; no paid APIs).
- **Voice:** Kokoro `am_onyx`, generated and measured first; durations drive the cut.
- **Beats:** 12 — 7 Manim (in `scenes.py`), 5 Remotion.
- **Remotion components reused from the scene library:** `BrutalistHesitantWriter`, `ClaudeComposerAsk`, `ClaudeTitleOutro`, `ClaudeVerdictArtifact`

## Status at build (from STATUS.md)

> Complete
>
> Verified 4K master and SRT/VTT captions in renders/. See _qc/DELIVERY-QC.md.
