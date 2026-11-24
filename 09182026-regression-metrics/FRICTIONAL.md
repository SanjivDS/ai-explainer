# Frictional log — Explainer: Regression Metrics: MAE, MSE, RMSE, R², and MAPE, Oversimplified

## 2026-10-03 — built at 1080p, first in line for the 4K re-render

- **Video:** not yet on YouTube
- **Drive:** [07 Regression metrics](https://drive.google.com/file/d/101egQCDPU8kCuz3jkgSu-RqlZuBC40Hd/view) (uploaded 3 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on five regression metrics as
different lenses on the same residuals. One worked dataset (actuals 2, 4, 6, 8;
predictions 3, 5, 5, 11) gives MAE 1.5, MSE 3 and RMSE √3. Two error sets,
[2,2,2,2] and [0,0,0,8], share MAE 2 but have RMSE 2 and 4. R² is measured
against the mean baseline and can go negative, and MAPE breaks at or near zero.
10 beats (6 Manim, 4 Remotion), built in Codex on 15 Sep.

**What I tried, and what I expected.**
- I asked Codex for the video on 15 Sep and approved the narration the same day
  ("Verdict: PASS approving narration").
- [CHECK: what you expected, e.g. that a fact-heavy topic with formulas would need
  more checking than the earlier ones.]

**Where it resisted, and what I did next.**
- **One claim in the draft was wrong.** It called ordinary MAPE asymmetric for
  equal over- and under-predictions, which is not true when the actual value is
  fixed. The beat now shows the supported problem instead: equal misses get very
  different weights when actual values differ in size (a miss of 1 at 1 vs. at 100).
- **The type checker wasn't there.** `scripts/type_check.py` was missing from the
  toolkit checkout on 15 Sep, so the type-lock check was done by inspecting rendered
  1920×1080 frames and source sizes.
- **It wasn't 4K.** The 15 Sep master was assembled below 4K. After Sanjana Rao's
  21 Sep note that none of the videos were in 4K, I asked Codex to re-render them
  one by one, starting with this one. Every source beat was re-rendered at native
  3840×2160 with no upscaling (217.34 s), 435 frames were reviewed across 18
  contact sheets, and the old file was kept as `-1080p-archive`. Later that day I
  was told the videos were still not in 4K. [CHECK: what the PM's screenshot
  showed, if you know which file she reviewed.]
- **Too many copies.** The folder ended up with `-1080p-archive`, `-4k`, `-slate`
  (1920×1080, 225 s) and a plain master. On 1 Oct I asked which ones were 4K.
- **The branding export was refused twice over.** On 2–3 Oct the final was blocked
  once for a missing `SHOTLIST.md` (GATE F), and GATE T failed in rounds flagging
  up to four beats, including B06 text runs about 38 px tall against the 41 px
  floor. It passed on 3 Oct, and the superseded copies were moved to
  `archive/pre-sanjiv-cleanup/`.

**Outcome.** 3840×2160, 24 fps, 3:37.5, 10 beats. GATE T pass (0 FAILs, 3 Oct),
Gate V 0 blocker / 0 major, arithmetic checked in `FACTCHECK.md`. The layout audit
keeps one warning (a ✦ mark just outside the safe area at 1.3 s). Branding check:
435 frames at 2 fps plus 30 beat samples, no matches.

**What the AI tools contributed, and what I did with it.**
- Mine: [CHECK: the topic and the five metrics chosen, the narration approval,
  choosing this video to start the 4K re-renders, and your review of the cut.]
- Codex's: the beat sheet and narration, the worked examples and their arithmetic,
  the fact-check against scikit-learn's documentation and the MAPE correction, the
  Manim scenes, the 1080p build, the 21 Sep 4K rebuild and the October cleanup.

<!-- DRAFT. Sources: README.md; brutalist.art-main and -latest copies of
     PEDAGOGY.md (VERDICT 2026-09-15), FACTCHECK.md, SOURCES.md, BUILD-PROMPT.md,
     TYPECHECK.md (15 Sep manual / 3 Oct GATE T), STATUS.md (4K rebuild),
     _qc/REPORT.md (21 Sep note in main), layout_audit.md, PROMPTS.md;
     beat_sheet.json (build.at 2026-09-21 main, 2026-10-03 latest);
     reports/4k-audit-2026-09-24 inventory.json; reports/branding-cleanup-2026-10-02
     (regression log, type-debug.log, final-qc result.json);
     reports/video-resolution-inventory.md; Codex messages 15 Sep, 21 Sep, 1 Oct.
     Replace every [CHECK] and delete this comment. -->
