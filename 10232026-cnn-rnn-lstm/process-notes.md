# Process notes — CNN vs RNN vs LSTM - When and Why to Use Each

**Google Drive:** [26 DL-3 CNN vs RNN vs LSTM](https://drive.google.com/file/d/1RxkUe1leAyT9_OjvVmeXjtJTeAIthLAo/view) (uploaded 12 Nov)
**Status:** delivered to Drive for review · not yet published to YouTube
**Resolution:** 3840×2160, 24 fps · **Runtime:** 4:31.8
**Built:** 19–23 Oct (master built 20 Oct)

Build notes for `cnn-rnn-lstm`. Append-only going forward.

## Build

- **Toolkit:** brutalist.art free path (Kokoro TTS + Manim + Remotion; no paid APIs).
- **Voice:** Kokoro `am_onyx`, generated and measured first; durations drive the cut.
- **Beats:** 17 — 12 Manim (in `scenes.py`), 5 Remotion.
- **Remotion components reused from the scene library:** `BrutalistHesitantWriter`, `ClaudeComposerAsk`, `ClaudeTitleOutro`, `ClaudeVerdictArtifact`

## Status at build (from STATUS.md)

> Complete — local review copy
>
> 2026-10-20. Approved episode rendered and visually reviewed.
>
> - Video: renders/cnn-rnn-lstm.mp4 — 4:32, 3840×2160, 24 fps
> - Captions: renders/cnn-rnn-lstm.srt
> - Runnable examples: renders/cnn-rnn-lstm-example.py
> - Chapters and SHA256SUMS alongside video
> - Typography, final-frame, sharpness, decode, footer, caption and peak checks passed
> - No publishing performed
>
> Audio was reviewed through ASR and signal checks, not direct listening. See _qc/REPORT.md.
