# Frictional log — Explainer: Cross-Validation — Why One Train/Test Split Isn't Enough

## 2026-10-04 — computed folds, and a contrast pass across every native scene

- **Drive:** [17 Cross Validation](https://drive.google.com/file/d/1syYUyYCA-J3N2VSU8LjKkBSBBm4Hu54M/view) (uploaded 11 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on why one train/test split isn't
enough. It covers two random splits that disagree, five folds that rotate the
validation data, using CV to pick a model while the final test stays sealed, and
three failure cases: leaking preprocessing, the wrong kind of split, and what CV
cannot certify. 12 beats (7 Manim, 5 Remotion bookends), native 3840×2160. This
was the third topic built on 4 Oct, with the same notes: @sanjiv, "Liam, in for
Sanjiv", no production footers.

**What I tried, and what I expected.**
- I requested it at 19:04 on 4 Oct with just the title. Unlike K-means and
  Entropy, this build ran straight through: master at 19:23, QC finished 19:25.
- [CHECK: what you expected, e.g. that a third same-day build would go faster,
  or that the earlier contrast fixes would already be in the template.]

**Where it resisted, and what I did next.**
- **No fold scene in the library.** The search returned unrelated split/testing
  diagrams, so the folds and scores were drawn natively in Manim.
- **The experiment had to show real disagreement.** The synthetic regression
  (NumPy least squares, not scikit-learn) uses seed 7 and 140 noisy
  observations: 100 for development and 40 held back as a final test.
  - Two 80/20 splits of the same data gave RMSE 0.456 and 0.574.
  - With 5-fold CV the cubic model averaged 0.534 and the linear model 0.774.
    The cubic model was picked and scored 0.488 on the untouched final test.
- **Several claims needed tightening.**
  - The fold standard deviation (0.035) is descriptive only, not a confidence
    interval.
  - The training sets overlap across folds, and this is shown explicitly.
  - Scaling statistics are recomputed from the training rows of each fold.
  - The final 40 rows play no part in choosing the model.
  - CV does not certify an unbiased score for the model it selected, or
    performance under future shift.
  - Whether to split by group or by time depends on how the model will be used.
- **Frame review found layout and contrast defects, fixed in the scene code.**
  - Score-label spacing and the overlapping-training-set view (B02 and B04
    re-rendered).
  - The chronological boundary placement in B07 (re-rendered).
  - Diagram contrast, changed to ink outlines and open/filled class markers.
    All seven native scenes (B02–B08) were re-rendered for this before the
    final typography check passed at 19:21.

**Outcome.** 3840×2160, 24 fps, 4:05.8, 12 beats. GATE T pass (12/12), GATE V 0
blocker / 0 major on 24 frames, 492 frames at 2 fps plus 36 per-beat samples
audited with zero old-name or footer-label matches. SRT (80 cues, 0 errors) and
VTT captions included.

**What the AI tools contributed, and what I did with it.**
- Mine: [CHECK: the topic choice and its place in the series, the brief, and
  your review of the cut before the 11 Oct upload.]
- Codex's: the beat
  sheet and narration, the computed regression experiment and its fact-check,
  the Manim scenes, the build, and the frame QC and fixes listed above.

<!-- DRAFT. Sources: BUILD-LOG.md, BUILD-PROMPT.md, CHECKS-REPORT.md,
     FACTCHECK.md, SOURCES.md, SRTCHECK.md, TYPECHECK.md, _qc/DELIVERY-QC.md,
     _qc/REPORT.md, evidence/execution.txt, native-fix/time-fix/contrast-fix
     logs, beat_sheet.json (build.at 2026-10-04T19:23), the 4 Oct Codex message
     (19:04), and the repo README. Replace every [CHECK] and delete this comment. -->
