# Frictional log — Explainer: Tokenization - How Machines Break Down Language

## 2026-10-15 — the first Deep Dive video, and a round trip back to the older template

- **Drive:** [21 NLP-1 Tokenization](https://drive.google.com/file/d/18dn6Hh80p-udcuUEfW7L-cqLJs3FKgM4/view) (uploaded 26 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** The first video of the Deep Dive set (NLP): an
`ai-explainer` on how a sentence becomes the numbers a language model receives.
It builds a tiny byte-pair-encoding tokenizer and shows why a token is not the
same thing as a word. Rendered at native 3840×2160 on the older Confusion Matrix
template, with a Sanjiv persona in place of Liam.

**What I tried, and what I expected.**
- On 14 Oct, before the series started, I set ground rules: no typing, erasing
  or retyping animations; smaller, legible headings and body text; more
  whitespace and fewer elements at once; the older videos as the visual
  reference; no overlapping text or graphs; no beat-sheet footnote.
- I dropped Liam from the intro and outro and wrote the opening myself ("This is
  Sanjiv. Today we shall discuss…"), asking for similar intros from here on.
- I expected the new series rules to sit cleanly on top of the old template, and
  swapping Liam for my own intro to be a small change, so the focus could be on
  how text is split into tokens.

**Where it resisted, and what I did next.**
- **The footer request ran four rounds.** I asked to remove the @sanjiv footer
  (14 Oct). On 15 Oct I added that the intro should still match the older videos:
  a Claude-style text field with @sanjiv and the agenda beneath it. The intro had
  been a static Manim stand-in, so the older `ClaudeComposerAsk` was restored with
  typing switched off.
- **"No typing" made it bland.** With whole lines popping in, I said typing was
  fine; what I didn't want was the type-it, erase-it, retype-it "not this but
  that" correction. Forward-only typing went back in after my approval.
- **I had layered too many instructions, so I reset.** I asked for a re-render on
  the older template, keeping only the no-Liam persona and the overlap checks.
  The previous master and sources were archived under
  `revisions/before-template-reset/`. The reset brought the bottom-right branding
  back, so I asked once more that night (15 Oct, 23:40) to remove it. That is the
  delivered cut. The reset also restored the template's `BrutalistHesitantWriter`
  overview, and I accepted
  the delivered cut with it after requesting the changes above.
- **Frame QC caught real defects, fixed at the source.** A B07 cue missed on a
  hyphenated phrase (the cue helper now raises on missing phrases); labels went to
  a 28-point floor; accent borders became underlines, because a box read as
  overlapping text; a B02 crossfade collision became sequential fades.
- **Whitespace vs the fill quota.** My whitespace request conflicted with the
  default fill check, so B03 and B11 were declared sparse-by-design after visual
  inspection; the other checks stayed on.
- **No library scene existed**, so every body scene is in the reel's `scenes.py`.
- **Greeting.** The first cut said "Hola"; it became "Hi" and B00 was regenerated.
- **Environment.** The reel runs on the `brutalist.art-main` venv and Kokoro
  model. Direct listening wasn't available; audio was checked by transcription and
  signal metrics.

**Outcome.** 3840×2160, 24 fps, 3:07.6, 12 beats. GATE T pass, GATE V 0 blocker /
0 major, 375 half-second timeline samples and 60 beat samples reviewed, 368
footer samples clear, decoded audio unchanged from the previous master. 76-cue SRT
captions.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic, the 14 Oct series rules, the Sanjiv intro wording, the
  footer, intro, typing and template-reset requests, the approvals, and
  reviewing the final cut.
- Codex's: the beat sheet and narration, the executed BPE example and fact-check,
  the Manim scenes and bookends, each revision pass, and the frame-by-frame QC and
  fixes above.
