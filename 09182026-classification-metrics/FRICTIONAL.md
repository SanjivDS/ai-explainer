# Frictional log — Explainer: Accuracy vs Precision vs Recall vs F1 Score, Oversimplified

## 2026-09-17 — three metrics became four, then 1080p became 4K

- **Drive:** [08 Classification metrics](https://drive.google.com/file/d/1Y-0sd9OI7SUd32rAUSPhtWtXfXqAmdKI/view) (uploaded 3 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on four classification metrics
read from one confusion matrix: accuracy counts every correct decision,
precision audits false alarms, recall audits misses, and F1 balances the two.
The worked example (TP=6, TN=88, FP=2, FN=4) gives 94% accuracy next to 60%
recall. 10 beats: 6 Manim body beats and 4 Remotion bookends, with Kokoro
`am_onyx` narration as "Liam, in for Sanjiv".

**What I tried, and what I expected.**
- I asked for "Precision vs Recall vs F-1 score" (17 Sep) and approved the
  narration with "Verdict: Pass".
- [CHECK: what you expected going in, e.g. that the three-metric version
  would be enough, or why you decided to add accuracy after approving it.]

**Where it resisted, and what I did next.**
- **The scope changed after the narration gate.** About 50 minutes after
  approving it, I asked for accuracy to be added alongside precision, recall and
  F1. The narration, fact-check and title were redone and I approved the
  four-metric version with a second "Verdict: PASS".
- **A Manim info footer sat in the bottom left.** I asked for it to be removed
  the same afternoon. The 17 Sep type-lock records no beat footer or diagnostic
  overlay in the master.
- **The type checker the skill names wasn't there.** `scripts/type_check.py` was
  missing from that toolkit checkout, so the type-lock was done by inspecting
  rendered frames instead.
- **No STATUS file.** On 18 Sep I asked where the status.md was. None existed, so
  one was made.
- **It was rendered at 1080p.** The 17 Sep master was 1920×1080. On 21 Sep Sanjana's review said none of the videos were 4K and asked me to use the latest
  version of Brutalist. All ten beats were rebuilt at native 3840×2160 that
  morning, and the 1080p file was kept as an archive. The same day I forked the
  upstream toolkit and moved the books into `brutalist.art-latest`. Later that
  day Sanjana said again that the videos still weren't 4K. The 24 Sep 4K audit
  confirmed 3840×2160 streams with ffprobe, and noted this proves the encoded
  size, not how the video was rendered.
- **The branding cleanup was blocked by the type gate (2–3 Oct).** The handle
  went from `@Sanjiv` to `@sanjiv` and review labels were switched off. The final
  export was then blocked three times (GATE T failing on 6, 6, then 4 beats).
  A debug crop found text runs in B01 and B06 below the 41 px floor at 4K. The
  fix went into the scene code: a minimum text size, terracotta text redrawn in
  ink, a darker accent, and pale card borders. The narration didn't change.

**Outcome.** 3840×2160, 24 fps, 3:34.4, 10 beats. GATE T pass (10 beats, 0
FAILs, 3 Oct), GATE V 0 blocker / 0 major. Branding QC: 429 frames at 2 fps
plus 30 beat samples, with no old-name or production-label OCR matches.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic, the decision to add accuracy, the footer-removal request,
  both narration approvals, passing on Sanjana's 4K feedback, and reviewing the
  cut.
- Codex's: the beat sheet and narration, the fact-check against Google for Developers
  and scikit-learn with the arithmetic worked out, the Manim scenes, the 4K
  rebuild, the type-gate fixes, and frame-level QC.

<!-- DRAFT. Sources: brutalist.art-main and brutalist.art-latest copies of
     BUILD-PROMPT.md, STATUS.md, TYPECHECK.md, FACTCHECK.md, PEDAGOGY.md,
     SOURCES.md, _qc/REPORT.md, scenes.py diff, beat_sheet.json (build.at
     2026-10-03T10:34); reports/4k-audit-2026-09-24/README.md;
     reports/branding-cleanup-2026-10-02 (README, claude-liam-precision-recall-f1.log,
     type-debug.log, final-qc result.json); Codex messages 17–21 Sep.
     Replace every [CHECK] and delete this comment. -->
