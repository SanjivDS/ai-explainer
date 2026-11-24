# Frictional log — Explainer: Confusion Matrix

## 2026-10-04 — a short 4K explainer, built on the existing series template

- **Video:** not yet on YouTube
- **Drive:** [18 Confusion Matrix](https://drive.google.com/file/d/1O1R9GoWIcBpjxbi-4Tt_ECdLuVIzReTY/view) (uploaded 13 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** A short `ai-explainer` (target 2:00–2:30) on the
confusion matrix: one score replaced by four counts, so the two kinds of
mistake become visible and every rate is read from a row or a column. Rendered
at native 3840×2160 and built from the same template as the rest of the
foundational series, with the master in `renders/` and the generation files in
`books/`.

**What I tried, and what I expected.**
- I expected to reuse the existing scene library for the matrix itself.
- [CHECK: what you expected going in, e.g. that the setup from the earlier
  4K re-renders would carry over unchanged, or that a 2-minute video would be
  quicker than the 4-minute ones.]

**Where it resisted, and what I did next.**
- **No confusion-matrix component existed.** `./art scenes` returned a miss
  (logged), so the four body beats were drawn in Manim and only the bookends came
  from the library.
- **The build environment wasn't the one I thought.** The default `python3` had
  neither Manim nor Kokoro, so the build ran on the `brutalist.art-main` venv
  (Manim 0.18.1, the version used for XGBoost). There is no LaTeX on the machine
  either, so the fractions are drawn as real fraction layouts, not `a/b` text.
- **The @sanjiv outro depended on an uncommitted change.** The `handle` prop on
  `ClaudeTitleOutro` existed only in the main checkout, so it had to be applied
  to the worktree by hand before the outro would render.
- **The app quit mid-build** (4 Oct, ~17:49) and the build was resumed from where
  it stopped.
- **Both quality gates failed on the first pass, and were fixed in the scene code
  rather than waived.**
  - Terracotta accent text measured 2.74:1 on the cream background, below the
    4.5:1 floor. All text went to ink, and the accent became a tint and an
    underline.
  - A latent failure: the terracotta *outline* also read as accent text. B02/B03
    had only passed because the sampled frames came before the outline appeared.
    Replaced with a 28% tint between the cell fill and the text.
  - The `@sanjiv` handle, the headers and a B04 row label sat outside the 5%
    title-safe area (a blocker).
  - Label collisions in B02, B03 and B05, and the B04 rate table ran off frame.
- **Two facts needed correcting while scripting.** The false-positive rate is
  10/980 = 1.02%, so it is shown as "≈ 1%" and spoken as "about one percent".
  The never-flag model's precision is 0/0, undefined, so it is left out rather
  than shown as 0%.
- **Matrix layout isn't universal.** scikit-learn puts truth on the rows, while R's
  `caret` puts predictions on the rows. That became the on-screen caution "read
  the axis labels before you read a cell."

**Outcome.** 3840×2160, 24 fps, 2:14.5, 9 beats. GATE T pass, GATE V 0 blocker /
0 major, 269 frames reviewed at 2 fps plus 27 per-beat samples. SRT and VTT
captions included.

**What the AI tools contributed, and what I did with it.**
- Mine: [CHECK: the topic choice and its place in the series, the brief (short,
  4K, renders/books layout), the fraud-detection framing if that was yours, and
  your review of the cut.]
- Claude's: the beat sheet and narration from that brief, the constructed
  fraud example and its fact-check, the Manim scenes, the build, and the frame-by-frame
  QC and fixes listed above.

<!-- DRAFT. Sources: BUILD-LOG.md, BUILD-PROMPT.md, CHECKS-REPORT.md,
     FACTCHECK.md, SOURCES.md, _qc/VISUAL-REVIEW.md, beat_sheet.json (build.at
     2026-10-04T20:37), the 4 Oct Claude Code session, and the Drive listing.
     Replace every [CHECK] and delete this comment. -->
