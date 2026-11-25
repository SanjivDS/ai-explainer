# Frictional log — Explainer: ROC Curve and AUC Score, Oversimplified

## 2026-09-09 — built with the review feedback in hand, then three rounds at the type gate

- **Drive:** [06 ROC Curve and AUC score](https://drive.google.com/file/d/1cE8CXoM1571tTQPFkmWbB59qHPDf-yz3/view) (uploaded 3 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on the ROC curve and AUC: ROC as the
map of threshold tradeoffs, AUC as ranking quality rather than deployment quality.
The worked example ranks six schematic cases `P P N P N N` and counts 8 of 9
positive–negative pairs in order (AUC 8/9 ≈ 0.89). B06 then holds that AUC fixed
while calibration, capacity and subgroup checks fail. 10 beats (6 Manim, 4
Remotion), built in Codex on 8–9 Sep.

**What I tried, and what I expected.**
- On 8 Sep I asked Codex to make it "considering all the changes that were
  mentioned", meaning the handle and footer fixes from Sanjana Rao's review the day
  before.
- [CHECK: what you expected, e.g. that building with the corrections from the start
  would mean no resubmission this time.]

**Where it resisted, and what I did next.**
- **The narration approval was inferred.** `PEDAGOGY.md` records the PASS as given
  "via the explicit instruction 'generate audio narration'", while
  `CHECKS-REPORT.md` still says GATE P is pending. I had read the narration before
  asking for the audio; the instruction was my sign-off.
- **It took several pushes to finish,** across two Codex threads: "go ahead and
  finish it" (8 Sep), "continue and finish the creation" and "complete the roc curve
  auc score video" (9 Sep).
- **The project landed in a nested folder.** It was built under
  `books/gradient-descent/youtube/roc-auc/youtube/…`, while its BUILD-PROMPT names
  `books/roc-auc/youtube/…`; that second path exists with only an empty `_qc/master`.
- **The first render stretched B04–B06** more than 3× to fill the narration.
  `scenes.py` was changed to scale every animation to the measured audio, so all six
  Manim clips are native length.
- **Facts were corrected before scripting.** "AUC is accuracy across thresholds"
  was rejected, "pick the point closest to the upper-left" was dropped as a
  universal rule, "PR-AUC is always better under imbalance" was softened to "inspect
  PR behavior too" (McDermott et al., NeurIPS 2024), and a prevalence-independence
  claim was left out.
- **Gate V: 0 blocker / 5 major,** all dispositioned after frame review: a B01
  cross-fade, the verdict card's page margin (B07), and the outro's negative space
  (B09).
- **Resolution.** The 9 Sep master was 1920×1080 (204.75 s). A 4K master (205.0 s)
  was exported on 21 Sep, the same day Sanjana told me the videos were still not in 4K.
- **The branding export failed GATE T in three rounds** (2–3 Oct). Text runs in
  B01, B03, B05 and B06 measured about 36–40 px, under the 41 px floor. It passed
  on 3 Oct.

**Outcome.** 3840×2160, 24 fps, 3:25.0, 10 beats. GATE T pass (0 FAILs, 3 Oct),
layout audit clean, 8/9 derived independently in `FACTCHECK.md`. Branding check:
410 frames at 2 fps plus 30 beat samples, no matches.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic, carrying the review feedback into the brief, the narration
  approval, the pushes to finish, and reviewing the cut.
- Codex's: the beat sheet and narration, the worked example and its derivation,
  the sources (Google ML Crash Course, scikit-learn, McDermott et al.), the
  corrections above, the Manim scenes, the build and the October fixes. Claude
  Code's: the 21 Sep 4K export.

<!-- DRAFT. Sources: README.md; brutalist.art-main and -latest copies of
     PEDAGOGY.md, CHECKS-REPORT.md, BUILD-PROMPT.md, FACTCHECK.md, SOURCES.md,
     replace_log.md, _qc/DISPOSITION.md, layout_audit.md; TYPECHECK.md (3 Oct);
     beat_sheet.json (build.at 2026-09-09 main, 2026-10-03 latest); the empty
     books/roc-auc folder in both trees; ffprobe of the 9 Sep master;
     reports/4k-audit-2026-09-24 inventory.json; reports/branding-cleanup-2026-10-02
     (roc log, repair-round2/3.log, type-debug.log, final-qc result.json);
     Codex messages 7–9 Sep, 21 Sep; Claude Code messages 21–22 Sep.
     Replace every [CHECK] and delete this comment. -->
