# Frictional log — Explainer: PCA — Dimensionality Reduction Explained Visually

## 2026-10-02 — finished at 1080p the morning 4K became the rule

- **Drive:** [14 Principal Component Analysis](https://drive.google.com/file/d/16tIVinbuyIlWZ_eBwJOxiCWnSBcP4Yp4/view) (uploaded 4 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on PCA as rotation plus projection:
center the data, find orthogonal directions ranked by variance, project, choose
k, reconstruct, and validate. One deterministic point cloud carries through
every step. The failure beat separates scale, nonlinear shape and outliers.
12 beats: 8 Manim and 4 Remotion bookends. At 4:33.8 it is the longest in the
set.

**What I tried, and what I expected.**
- I asked for "PCA - Dimensionality Reduction Explained Visually" on 20 Sep and
  approved the narration the next morning. The 1920×1080 master was finished at
  10:18 on 21 Sep. At 10:25 I passed on Sanjana's note that none of the videos
  were in 4K.
- [CHECK: what you expected, e.g. whether you knew 1080p would be rejected.]

**Where it resisted, and what I did next.**
- **The claims had to be narrowed.** The script doesn't say PCA "selects the
  most important features". It builds new components from weighted
  combinations of features. No fixed explained-variance threshold is given.
  Centering is kept separate from standardization, and the point cloud is
  labelled as a teaching toy, not measured data.
- **The first cut had generic bookend text.** QC replaced the generic B09
  verdict with a PCA-specific center/rotate/retain/validate artifact, and
  replaced the generic B11 subline. It also raised the B05 footer clear of the
  wordmark.
- **The type checker the skill names wasn't there**, so the checks were done
  by hand during a 547-frame visual audit.
- **The native 4K rebuild was blocked by the type gate (24–27 Sep).** All eight
  Manim scenes were rebuilt at 3840×2160, and the final export was blocked twice
  (GATE T failing on 7 beats, then 2). The fixes:
  - higher text contrast
  - the SVD equation and its cards made smaller to fit the margins
  - the explained-variance bars moved
  - "2D → 1D" changed to "2D TO 1D"
  - in the outlier panel, the empty ellipse was replaced with schematic points,
    because in pixel inspection it looked like an overlapping label
- **Branding cleanup (2 Oct).** OCR found no old handle. The scenes were
  re-rendered with `@sanjiv` and accent text in ink, and review labels were
  switched off for the final export.

**Outcome.** 3840×2160, 24 fps, 4:33.8, 12 beats. GATE T pass (2 Oct, 0
FAILs), GATE V 0 blocker / 0 major. Branding QC: 548 frames at 2 fps plus 36
beat samples, with no flags.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic request, the narration approval, and passing on Sanjana's 4K
  feedback. [CHECK: why this topic this week, and your review of the 4K cut.]
- Claude's: [CHECK: the 20–21 Sep build and the 4K continuation are Codex
  threads. Confirm which tool to credit.] The beat sheet and the wording
  limits, the point-cloud Manim scenes, the bookend corrections, the native 4K
  rebuild and its layout fixes, and frame-level QC.

<!-- DRAFT. Sources: brutalist.art-main and -latest copies of BUILD-PROMPT.md,
     STATUS.md, TYPECHECK.md, FACTCHECK.md, SOURCES.md, PEDAGOGY.md,
     _qc/REPORT.md, scenes.py / scenes.py.pre-qc-fix diff, beat_sheet.json
     (build.at 2026-10-02T12:18); reports/4k-audit-2026-09-24 (README.md,
     pca-*final*.log); reports/branding-cleanup-2026-10-02 (baseline-findings.json,
     final-qc result.json); Codex messages 20–21 Sep. Note: the repo README
     gives "Built 28 Sep – 2 Oct", but the first build is dated 20–21 Sep.
     Replace every [CHECK] and delete this comment. -->
