# Process notes — Transformers - Encoder, Decoder & Self-Attention

**Google Drive:** [27 LLM-1 Transformers](https://drive.google.com/file/d/1gQySl8qB8U3hszwgTdC9jUZFXjiJ_ou2/view) (uploaded 20 Nov)
**Status:** delivered to Drive for review
**Resolution:** 3840×2160, 24 fps · **Runtime:** 5:09.9
**Built:** 19–25 Oct (master built 21 Oct)

Build notes for `transformers`. Append-only going forward.

## Build

- **Toolkit:** brutalist.art free path (Kokoro TTS + Manim + Remotion; no paid APIs).
- **Voice:** Kokoro `am_onyx`, generated and measured first; durations drive the cut.
- **Beats:** 17 — 12 Manim (in `scenes.py`), 5 Remotion.
- **Remotion components reused from the scene library:** `BrutalistHesitantWriter`, `ClaudeComposerAsk`, `ClaudeTitleOutro`, `ClaudeVerdictArtifact`

## Status at build (from STATUS.md)

> Complete
>
> All 17 scenes rendered and verified. Final master: 3840×2160, 24 fps, 309.875 seconds. Sidecar captions contain 110 ordered cues.
>
> Older Claude template retained; Sanjiv introduction and outro, composer chip/agenda and centered closing handle retained; no recurring bottom-right footer.
>
> Type, frame, sharpness, full-decode, caption, audio-signal, footer and executable-example checks passed. All 620 timeline samples were visually reviewed. No outstanding major or blocking visual findings. Audio review used ASR/alignment and signal checks, without direct listening.
>
> Deliverables are in renders/. Nothing published.
