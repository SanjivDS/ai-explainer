# Frictional log — Explainer: Bagging vs Boosting, Oversimplified

## 2026-10-02 — five rounds on one loss-curve label

- **Drive:** [11 Bagging vs Boosting](https://drive.google.com/file/d/1o1UzJG3bI9W0kGY2dShmkr5m3hsmNTAS/view) (uploaded 3 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` contrasting two ensemble
strategies. Bagging trains on bootstrap samples independently and then votes or
averages. Boosting trains in sequence, with AdaBoost reweighting the missed rows
and gradient boosting adding loss-reducing corrections. The noise stress test
shows how both can fail. 11 beats: 7 Manim and 4 Remotion bookends.

**What I tried, and what I expected.**
- I asked for "Bagging vs Boosting" on 18 Sep and approved the narration a few
  minutes later.
- [CHECK: what you expected, e.g. that a side-by-side comparison would lay out
  more easily than the tree videos.]

**Where it resisted, and what I did next.**
- **The usual slogans had to go.** "Bagging reduces variance, boosting reduces
  bias" is stated as a tendency, not a rule. AdaBoost's reweighting is kept
  separate from gradient boosting's corrections. The script doesn't claim that
  boosting always overfits noise or that bagging prevents overfitting.
- **My timestamp review found three collisions (19 Sep).** At 1:55 the circles
  around dots 3 and 7 covered their numbers. At 2:24 "memory" overlapped the
  bagging bars, so I asked for the Memory and Tuning cards to sit below. At 2:45
  "train loss" overlapped its curve.
- **The 2:45 labels took five messages.** I asked for smaller labels with train
  loss under its curve, then reported it was "still overlapping", then asked for
  both labels aligned vertically before the three boxes, and finally to keep
  train loss and move validation loss up to the end of the red curve. The
  master was rebuilt that night at 1920×1080 and 500 frames were checked.
- **The first master was 1080p.** On 21 Sep Sanjana asked for 4K. The 24–27 Sep
  4K continuation rebuilt all seven scenes natively. The final export was
  blocked twice (GATE T failing on 7 beats, then 2) and fixed by raising
  card/text contrast and redrawing the B02/B07 diagram strokes in ink,
  including the train-loss curve. The narration didn't change.
- **The teaching footer ran into the handle (2 Oct).** In the branding cleanup,
  the footer notes in B03 and B05 touched the `@sanjiv` row, so they were moved
  up. The handle changed from `@Sanjiv` to `@sanjiv`, and review labels were
  switched off for the final export.

**Outcome.** 3840×2160, 24 fps, 4:10.0, 11 beats. GATE T pass (2 Oct, 0
FAILs), GATE V 0 blocker / 0 major. Branding QC: 500 frames at 2 fps plus 33
beat samples, with no flags.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic request, the narration approval, and the timestamped layout
  review, including the exact label placement I wanted at 2:45. [CHECK: why
  this topic this week, and your review of the 4K cut.]
- Claude's: [CHECK: the 18–19 Sep build and the 4K continuation are Codex
  threads. Confirm which tool to credit.] The beat sheet and the hedged
  wording, the Manim mechanism diagrams, each label revision, the 4K rebuild,
  and the footer and handle fixes.

<!-- DRAFT. Sources: brutalist.art-main and -latest copies of BUILD-PROMPT.md,
     STATUS.md, TYPECHECK.md, FACTCHECK.md, SOURCES.md, PEDAGOGY.md,
     _qc/REPORT.md, BUILD-LOG.md, scenes.py / scenes.py.pre-qc-fix diff,
     beat_sheet.json (build.at 2026-10-02T23:01); reports/4k-audit-2026-09-24
     (README.md, bagging-vs-boosting-*final*.log);
     reports/branding-cleanup-2026-10-02 (fixes.json, final-qc result.json);
     Codex messages 18–21 Sep. Note: the repo README gives "Built 28 Sep – 2 Oct",
     but the records show the first build on 18–19 Sep.
     Replace every [CHECK] and delete this comment. -->
