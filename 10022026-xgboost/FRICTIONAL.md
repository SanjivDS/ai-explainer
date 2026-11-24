# Frictional log — Explainer: XGBoost - Why It Works So Well

## 2026-10-02 — 4K from the start, but under the wrong name

- **Video:** not yet on YouTube
- **Drive:** [12 XGBoost](https://drive.google.com/file/d/1UhfocwQahh-rv4pjjGX2geiqFicUd0oQ/view) (uploaded 4 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on one boosting round, using a
constructed four-row example. The targets 2, 4, 8, 10 have mean 6, giving
residuals −4, −2, 2, 4. The split x ≤ 2 gives leaf corrections −3 and +3, and a
learning rate of 0.5 takes training MSE from 10 to 3.25. With λ = 2 the leaves
shrink to ±1.5. The arithmetic was run in `evidence/example.py`. 11 beats: 6
Manim and 5 Remotion.

**What I tried, and what I expected.**
- I asked for "XGBoost - why it works so well" "rendered in 4k" (28 Sep). This
  was the first video where 4K was part of the request.
- [CHECK: what you expected, e.g. that saying 4K up front would avoid the
  re-render cycle of the earlier videos.]

**Where it resisted, and what I did next.**
- **No library scene for the mechanism.** The scene search found the shared
  bookends but nothing for XGBoost, so B02–B07 were written as local Manim
  scenes.
- **The first build used the wrong identity.** The build log records "default
  skill identity, Liam in for Bear". On 29 Sep I asked for `@sanjiv` and "Liam,
  in for Sanjiv". The B00/B08/B10 narration, word alignment and captions were
  regenerated, all 11 scenes were re-rendered at native 4K, and 420 frames were
  checked again.
- **The type gate failed on the first pass** (6 beats). The native source
  citations and channel bug were 38 px tall against a 41 px floor, so they were
  raised from 25 to 29 points.
- **Smaller bugs before the final:**
  - A Manim attribute name collided with the Scene's internal duration state,
    so the clips didn't hold to the measured audio.
  - The same-slope caption overlapped the chart and was moved below the axes.
  - The B05 leaf-score numerals touched the heading. They were separated
    without changing the 2:1 bar ratio.
  - Line keys were added to the training/validation legend.
  - Explicit pauses were added with `pad_audio.py`.
- **Too many files with the same name.** On 1 Oct I asked which of the archive
  1080p, slate and plain MP4 files were the 4K ones. The inventory shows the
  XGBoost slate was 1920×1080 and the `renders/` master 3840×2160.
- **Branding cleanup (2 Oct).** OCR found no old handle. The video was
  re-exported with production labels off and checked frame by frame.

**Outcome.** 3840×2160, 24 fps, 3:30.0, 11 beats. GATE T pass (11 beats, 0
FAILs), GATE V 0 blocker / 0 major. Branding QC: 420 frames at 2 fps plus 33
beat samples, with no flags. SRT and VTT captions included. The loss curves
and the extrapolation beat are labelled as conceptual, with no benchmark claims.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic and the 4K requirement, the identity correction, and the
  question about which files were really 4K. [CHECK: why this topic this week,
  and your review of the cut.]
- Claude's: [CHECK: the session record for this build is a Codex thread.
  Confirm which tool to credit.] The beat sheet, the constructed example and
  its executed check, the fact-check against Chen & Guestrin and the XGBoost
  docs, the Manim scenes, the rebrand re-render, the type and layout fixes, and
  frame-level QC.

<!-- DRAFT. Sources: brutalist.art-latest/books/xgboost/.../claude-liam-xgboost:
     BUILD-LOG.md, BUILD-PROMPT.md, PROMPTS.md, README.md, STATUS.md,
     FACTCHECK.md, SOURCES.md, TYPECHECK.md, _qc/VISUAL-REVIEW.md,
     _qc/REPORT.md, type-check.log, final-build.log, rebrand-*.log,
     beat_sheet.json (build.at 2026-10-02T12:22); video-resolution-inventory.md;
     reports/branding-cleanup-2026-10-02 (baseline-findings.json, final-qc
     result.json); Codex messages 28 Sep – 2 Oct.
     Replace every [CHECK] and delete this comment. -->
