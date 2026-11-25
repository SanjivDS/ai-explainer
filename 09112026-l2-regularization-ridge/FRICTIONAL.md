# Frictional log — Explainer: L2 Regularization, Oversimplified

## 2026-09-07 — the handle and footer fixes from the first review

- **Drive:** [05 L2 Regularization (Ridge)](https://drive.google.com/file/d/1unnRYOgMgLQZLoWg2eSKY3bMP52zreza/view) (uploaded 3 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on Ridge: a squared-weight penalty
added to least squares, with lambda as the dial that trades a little bias for less
variance. Doubling a coefficient quadruples its penalty, correlated predictors go
from unstable opposite weights to stable moderate ones, lambda is chosen by
cross-validation, and three diagnostics close it (standardize, leave the intercept
unpenalized, Ridge approaches zero where Lasso reaches it). 10 beats (7 Manim, 3
Remotion), built in Codex.

**What I tried, and what I expected.**
- I first asked Codex for "overfitting and underfitting", then switched to L2 in
  the same thread on 4 Sep. I switched so it would sit next to L1 as a pair,
  which made the comparison between the two penalties easier to follow.
- I approved the narration with "Verdict: PASS" on 4 Sep and the first cut was
  compiled that day.
- I expected to reuse the L1 structure and focus on how Ridge shrinks coefficients,
  generally without setting them exactly to zero.

**Where it resisted, and what I did next.**
- **The first review came back with two fixes.** Sanjana Rao's 7 Sep email: all
  three videos she had (L1, L2, Linear/Logistic) showed "@NikBearBrown", and this one
  had a footer in the bottom left, "B00 GRAPHIC VIDEO 0.0s + 16.7s", that had to go.
  She then clarified the narrator line should be "Liam, in for Sanjiv" and the
  handle under the Claude dialogue box "@Sanjiv". I asked Codex to correct the three
  videos one by one, and this one was recompiled that day at 1920×1080.
- **Claims were hedged in the sources.** Ridge "usually" improves stability rather
  than promising lower test error, the intercept is "usually" unpenalized as a
  standard formulation, and every path and curve is labelled schematic.
- **Resolution.** The 24 Sep audit found the 7 Sep copies and the slate at
  1920×1080 (192.4 s). A 4K master (192.6 s) had been exported on 21 Sep, the same
  day Sanjana told me the videos were still not in 4K.
- **Production footers were still showing in some videos.** On 2 Oct I reported
  footer notes with beat-sheet info on the bottom left and asked for every video to
  be checked one by one. The cleanup's baseline audit flagged no footer or
  old-handle text in this video. The cleanup
  exported in final mode, with review labels off, which drops the beat, status and
  timecode overlays.
- **The type gate blocked that export once** (two beats failed on 2 Oct); after
  the fix GATE T passed and the master was exported the same night.

**Outcome.** 3840×2160, 24 fps, 3:12.6, 10 beats (9 SHOW, 1 title-card outro).
GATE T pass (0 FAILs, 2 Oct), Gate V 0 blocker / 0 major, layout audit clean.
Branding check: 385 frames at 2 fps plus 30 beat samples, no old-name or
production-footer matches.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic switch, the narration approval, passing Sanjana's feedback
  through and asking for the fixes one video at a time, reporting the returning
  footers, and reviewing the cut.
- Codex's: the beat sheet and narration, the sources (scikit-learn Ridge, Stanford
  STATS 202), fact-check, Manim scenes and build, and the 7 Sep and 2 Oct fixes.
  Claude Code's: the 21 Sep 4K export.
