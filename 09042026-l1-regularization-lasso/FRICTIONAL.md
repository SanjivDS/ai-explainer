# Frictional log — Explainer: L1 Regularization, Oversimplified

## 2026-09-04 — two L1 projects, placeholder slates in the submission, and an NBB mark

- **Drive:** [04 L1 Regularization (Lasso)](https://drive.google.com/file/d/1zC_kkxJUv7AXVCOCVGzKKL6VLvD-8gjm/view) (uploaded 3 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on Lasso: why a penalty on total
absolute weight drives some coefficients to exactly zero while the squared penalty
only shrinks them. The diamond-vs-circle geometry, a regularization path, choosing
lambda by cross-validation, and the edge cases (correlated twins, unstable picks,
shrinkage bias, not causation). 10 beats (8 Manim, 2 Remotion), the sibling of the
L2 reel. Built in Claude Code; I signed the narration verdict on 4 Sep before audio.

**What I tried, and what I expected.**
- The 4 Sep session stopped partway ("Continue from where you left off", "Try
  again") and I re-ran the command. Two L1 projects were built that morning: this
  one (`claude-liam-l1-regularization-lasso`) and a standalone
  `claude-liam-l1-regularization`. [CHECK: whether the second one was intended, and
  which one you submitted first.]
- [CHECK: what you expected going in, e.g. that Claude Code would now finish a
  video in one run.]

**Where it resisted, and what I did next.**
- **"Can't hear narration."** I reported this on 4 Sep. The standalone copy's
  BUILD-LOG traces it to a field copied from the gradient-descent sheet
  (beat-level `engine: manim`), which made the audio script skip B01–B06; only 4 of
  10 beats were voiced until it was set to `kokoro`.
- **Three drafted lines were softened in the fact-check.** Loss contours "always"
  hit a corner became "tend to meet that corner first"; Lasso picks a correlated
  feature "at random" became "nearly arbitrarily"; a Lasso-vs-Ridge accuracy line
  was dropped for lack of a source.
- **The handle was wrong.** Sanjana Rao's 7 Sep review found @NikBearBrown on this
  video, L2 and Linear/Logistic. It was recompiled that day.
- **"Missing media throughout."** Her 8 Sep review rejected this video. B01–B07 in
  the submitted cut were pipeline placeholder slates. The Manim scenes were
  re-rendered from `scenes.py`, restored to their slots, the 1920×1080 master was
  recompiled with 10/10 slots filled, and the mid-beat frames were inspected.
- **It wasn't 4K.** The 24 Sep audit found both full-length copies at 1920×1080
  (183.0 s); only the review slate was 3840×2160.
- **The native 4K rebuild (25 Sep)** re-rendered all eight Manim scenes with ink
  labels for contrast. The B02/B06 underfill during progressive reveals was recorded
  as sparse by design, with the checks left on.
- **An NBB mark survived the handle fix.** The B09 outro drew a terracotta "NBB"
  monogram. The 2 Oct branding audit found it in the closing frame and it was
  replaced with the star motif.

**Outcome.** 3840×2160, 24 fps, 3:03.2, 10 beats. GATE T pass (0 FAILs, 2 Oct),
Gate V 0 blocker / 0 major, strict layout audit 0 errors across 15 snapshots.
Branding check: 367 frames at 2 fps plus 30 beat samples, no matches.

**What the AI tools contributed, and what I did with it.**
- Mine: [CHECK: the topic and pairing it with L2, the 4 Sep narration sign-off,
  reporting the missing narration, passing on Sanjana's two reviews, and your review
  of the cut.]
- Claude Code's (4 Sep): the beat sheet, narration, sources (Tibshirani 1996,
  *ESL* §3.4 and §7.10, Zou & Hastie 2005), fact-check, Manim scenes and first
  build. Codex's: the 7–8 Sep fixes, the 25 Sep 4K rebuild and the 2 Oct branding
  cleanup.

<!-- DRAFT. Sources: README.md; brutalist.art-main and -latest copies of
     PEDAGOGY.md, FACTCHECK.md, SOURCES.md, PROMPTS.md, CHECKS-REPORT.md,
     _qc/REPORT.md (the 8 Sep repair note is only in the main copy); latest
     BUILD-LOG.md, TYPECHECK.md, layout_audit.md; beat_sheet.json (build.at
     2026-09-08 main, 2026-10-02 latest); books/l1-regularization BUILD-LOG.md;
     reports/4k-audit-2026-09-24 (README, inventory.json, lasso logs);
     reports/branding-cleanup-2026-10-02 (README, baseline-findings.json,
     final-qc result.json); Claude Code messages 4 Sep and 21 Sep; Codex
     messages 7–8 Sep. Replace every [CHECK] and delete this comment. -->
