# Process notes — Tokenization - How Machines Break Down Language

**Google Drive:** [21 NLP-1 Tokenization](https://drive.google.com/file/d/18dn6Hh80p-udcuUEfW7L-cqLJs3FKgM4/view) (uploaded 26 Oct)
**Status:** delivered to Drive for review
**Resolution:** 3840×2160, 24 fps · **Runtime:** 3:07.6
**Built:** 12–18 Oct (master built 15 Oct)

Build notes for `tokenization`. Append-only going forward.

## Build

- **Toolkit:** brutalist.art free path (Kokoro TTS + Manim + Remotion; no paid APIs).
- **Voice:** Kokoro `am_onyx`, generated and measured first; durations drive the cut.
- **Beats:** 12 — 7 Manim (in `scenes.py`), 5 Remotion.
- **Remotion components reused from the scene library:** `BrutalistHesitantWriter`, `ClaudeComposerAsk`, `ClaudeTitleOutro`, `ClaudeVerdictArtifact`

## Status at build (from STATUS.md)

> Status
>
> Completed: Recurring bottom-right @sanjiv footer removed from native diagrams, overview, and verdict. Intro and handoff folder chips and closing title-card handle retained. Existing older-template animation and composition preserved. Typography and final-frame gates passed; intentional empty corner space documented. Verified no residual footer ink in 368 half-second samples. Decoded audio identical to template-with-footer master; full video decode passed. Refreshed 375 timeline and 60 beat samples; inspected 12 full beat midpoints. Master remains 3840×2160, 187.625 seconds.
