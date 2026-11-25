# Frictional log — Explainer: Attention - Why It Changed NLP

## 2026-10-16 — exact attention arithmetic, and a footer check that cried wolf

- **Drive:** [23 NLP-3 Attention](https://drive.google.com/file/d/1Bmz9_baTgAK8_1_6JqsUTcf3jhbN1xM0/view) (uploaded 3 Nov)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** The third NLP video in the Deep Dive set: why a fixed
summary was a bottleneck, how attention scores, weights and mixes values (query,
key, value), and what that made possible in the Transformer. Native 3840×2160 on
the older Confusion Matrix template, Sanjiv persona, no bottom-right footer.

**What I tried, and what I expected.**
- I requested the video on the evening of 16 Oct and approved the plan about 25
  minutes later, with the same series preferences as Word Embeddings.
- The previous video was used only for template props; no earlier timing or media
  was reused.
- I expected a straight run after the Tokenization revisions, with the main work
  being to fit the worked example on screen without crowding.

**Where it resisted, and what I did next.**
- **No library scene did attention arithmetic.** The scene search returned only
  generic matrix hits, so the ten teaching scenes are custom Manim and only the
  five bookend/framing scenes come from the library.
- **The overview needed a props fix.** Its property types were repaired and B01
  re-rendered.
- **Two beats were hard to follow by ear.** B05 now says the first scaled score
  separately from the two zero scores, and B07 names each output coordinate
  explicitly. Only those two audio files and their renders were regenerated; the
  values didn't change.
- **Rounding needed a caveat.** The softmax weights display as .673, .164, .164,
  which add to 1.001. The beat shows them as approximate and says the unrounded
  weights sum to one. The outputs (.836, .327) and, with the query changed,
  (.327, .836) were checked by independent assertions and spoken at two decimals.
- **The footer check failed on a false positive.** A broad crop flagged frame 00292
  at 145.5 s. Full-frame review showed the edge of a B07 explanatory note, not a
  footer; the actual footer area was empty in all 544 samples. The failure is kept
  in `footer-qc.log`, and the shared validator wasn't changed.
- **Claims were scoped, not inflated.** Attention predates the Transformer
  (Bahdanau et al., 2014/ICLR 2015). Parallel computation over positions applies to
  training, not to autoregressive generation, and no speed-up is claimed. 4²=16 →
  8²=64 counts dense pairs; it is not a universal runtime law. A heat map alone is
  not a causal explanation, but Jain & Wallace is read together with Wiegreffe &
  Pinter rather than as a blanket rejection.
- **Audio check limits.** Alignment, ASR comparison and signal levels passed with
  no clipping. Direct listening wasn't available, and ASR still misreads some
  proper names.

**Outcome.** 3840×2160, 24 fps, 4:37.5, 15 beats (11 teaching, 4 framing). GATE T
pass on all 15. 555 half-second timeline samples (28 contact sheets) and 75 beat
samples reviewed, with native-resolution spot checks. No unintended overlaps
found. Full decode passed. 104 caption cues and chapters.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic and title, the standing series preferences, and the plan
  approval. [CHECK: your review of the cut, and whether the "context, calculation,
  consequences" structure or the bottleneck-first opening was your call.]
- Codex's: the 15-beat script and storyboard, the constructed q/k/v example and its
  execution, the source check, the Manim scenes, the narration fixes, the footer
  false-positive review, and the QC above.

<!-- DRAFT. Sources: BUILD-LOG.md, BUILD-PROMPT.md, CHECKS-REPORT.md,
     FACTCHECK.md, PROMPTS.md, QC-REPORT.md, SOURCES.md, STATUS.md, TYPECHECK.md
     (2026-10-16T21:23), _qc/REPORT.md, beat_sheet.json (build.at
     2026-10-16T21:24), footer-qc.log, overview-fix.log, renders/ timestamps,
     codex-user-messages.txt (16–17 Oct), repo README.md. Note: the master file is
     dated 16 Oct but QC-REPORT and the delivery entry are dated 17 Oct. Build
     sessions were Codex threads. Replace every [CHECK] and delete this comment. -->
