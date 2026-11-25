# Process notes — Bagging vs Boosting, Oversimplified

**Google Drive:** [11 Bagging vs Boosting](https://drive.google.com/file/d/1o1UzJG3bI9W0kGY2dShmkr5m3hsmNTAS/view) (uploaded 3 Oct)
**Status:** delivered to Drive for review
**Resolution:** 3840×2160, 24 fps · **Runtime:** 4:10.0
**Built:** 28 Sep – 4 Oct (master built 2 Oct)

Build notes for `claude-liam-bagging-vs-boosting`. Append-only going forward.

## Build

- **Toolkit:** brutalist.art free path (Kokoro TTS + Manim + Remotion; no paid APIs).
- **Voice:** Kokoro `am_onyx`, generated and measured first; durations drive the cut.
- **Beats:** 11 — 7 Manim (in `scenes.py`), 4 Remotion.
- **Remotion components reused from the scene library:** `ClaudeComposerAsk`, `ClaudeTitleOutro`, `ClaudeVerdictArtifact`

## Status at build (from STATUS.md)

> Status — Bagging vs Boosting
>
> Status: COMPLETE — READY FOR REVIEW
>
> - Narration drafted: 11 beats
> - Pedagogy gate: PASS (approved 2026-09-18)
> - Fact-check: ready for narration review
> - Audio: generated and duration-bound for all 11 beats
> - Visuals: 11/11 beats filled
> - Master: `claude-liam-bagging-vs-boosting.mp4`
> - Runtime: 04:09.820
> - Resolution: 1920×1080
> - Captions: SRT and WebVTT included
> - Visual QC: PASS at 2 fps (500 inspected frames)
> - Typecheck: PASS
> - Publishing: not performed
>
> Next action: human review. Publishing was not performed.

**Note:** this STATUS.md predates the 4K re-render; the master on disk was re-probed at 3840×2160.
