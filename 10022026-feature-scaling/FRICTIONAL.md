# Frictional log — Explainer: Feature Scaling: Standardization vs Normalization, Oversimplified

## 2026-10-02 — 1080p first, then native 4K and an old handle

- **Drive:** [13 Feature Scaling](https://drive.google.com/file/d/1ULEnffn0oWHuYXTpswzNwxXW9NhhDNae/view) (uploaded 4 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on standardization versus min–max
scaling. The values 10, 20, 30 map to about −1.22, 0, +1.22 (population standard
deviation ≈ 8.16) and to 0, 0.5, 1 respectively. The video also covers why
scaling matters for distance, gradient and PCA models, and why the scaler must
be fitted on training data only. 10 beats: 6 Manim and 4 Remotion bookends.

**What I tried, and what I expected.**
- I asked for "Feature Scaling — Standardization vs Normalization" on 18 Sep
  and approved the narration within about ten minutes.
- [CHECK: what you expected, e.g. that a worked-numbers video would need fewer
  layout fixes than the tree videos.]

**Where it resisted, and what I did next.**
- **"Normalization" means two different things.** The video uses it for min–max
  scaling only and names scikit-learn's sample-wise `Normalizer` as a separate
  operation. Standardization is described as centering and rescaling, not as
  making data normal. Min–max is described as bounding only the training range,
  since new values can fall outside it.
- **Collisions in the first cut.** QC found brief graphic collisions in B01, B03
  and B04. They were fixed and the 1080p master was regenerated (443 frames
  checked).
- **The first master was 1080p.** On 21 Sep the PM asked for 4K. In the 24–27
  Sep 4K continuation, all six scenes were rebuilt natively. The final export
  was blocked three times (GATE T failing on 5, 2, then 1 beat). The fixes were
  terracotta arrows and outlines redrawn in ink for contrast, and the
  raw-data card moved in from the left margin. The B07 recap's inset card was
  recorded as deliberate (`sparse_by_design`) instead of switching the check
  off.
- **Duplicate files with different resolutions.** The 1 Oct inventory still
  listed a 1920×1080 copy beside the project and the 3840×2160 master in
  `renders/`. This was part of why I asked which files were really 4K.
- **The old handle came back.** On 2 Oct, OCR found `@NikBearBrown` on the
  closing frame of the 4K master, though the 18 Sep QC had reported only
  `@Sanjiv`. The cleanup set the handle explicitly instead of relying on
  template defaults, switched to `@sanjiv`, and turned review labels off.

**Outcome.** 3840×2160, 24 fps, 3:41.8, 10 beats. GATE T pass (2 Oct, 0
FAILs), GATE V 0 blocker / 0 major. Branding QC: 444 frames at 2 fps plus 30
beat samples, with no flags.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic request, the narration approval, passing on the PM's 4K
  feedback, and the 2 Oct request to remove the old handle and footers.
  [CHECK: why this topic this week, and your review of the cut.]
- Claude's: [CHECK: the 18 Sep build and the 4K continuation are Codex
  threads. Confirm which tool to credit.] The beat sheet and the terminology
  limits, the worked z-score and min–max values, the Manim scenes, the
  collision and contrast fixes, the native 4K rebuild, and the handle repair.

<!-- DRAFT. Sources: brutalist.art-main and -latest copies of BUILD-PROMPT.md,
     STATUS.md, TYPECHECK.md, FACTCHECK.md, SOURCES.md, PEDAGOGY.md,
     _qc/REPORT.md, BUILD-LOG.md, scenes.py / scenes.py.pre-qc-fix diff,
     beat_sheet.json (build.at 2026-10-02T11:58); reports/4k-audit-2026-09-24
     (README.md, feature-*final*.log); reports/branding-cleanup-2026-10-02
     (README.md, baseline-findings.json, final-qc result.json);
     video-resolution-inventory.md; Codex messages 18 Sep – 2 Oct. Note: the
     repo README gives "Built 28 Sep – 2 Oct", but the first build is dated
     18 Sep. Replace every [CHECK] and delete this comment. -->
