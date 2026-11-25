# Frictional log — Explainer: Random Forest: Why Multiple Trees Beat One, Oversimplified

## 2026-09-17 — six collisions, a late 4K pass, and an old handle

- **Drive:** [10 Random Forest](https://drive.google.com/file/d/1gLkiVEkccH0L2TDKMHB4-bQ9JYxOsz84/view) (uploaded 4 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on why a forest usually varies less
than one tree: bootstrap samples and random feature subsets make the trees
differ, and averaging less-correlated errors reduces variance. The worked
average is (0.9 + 0.8 + 0.2 + 0.7 + 0.4) / 5 = 0.60, which is class A under an
illustrative 0.50 cutoff. 10 beats: 6 Manim and 4 Remotion bookends.

**What I tried, and what I expected.**
- I asked for "Random Forest - Why multiple trees beat one" late on 17 Sep and
  approved the narration within about ten minutes.
- [CHECK: what you expected, e.g. that reusing the decision-tree layout would
  carry over cleanly.]

**Where it resisted, and what I did next.**
- **The title overclaims, so the script hedges.** "Beat one" is explained as a
  common variance-reduction advantage, not a guarantee. Identical trees are said
  not to help. Voting isn't treated as universal (scikit-learn averages class
  probabilities). Out-of-bag scoring is presented as one evaluation option.
- **I found six layout collisions in the first cut.** In three messages I
  reported problems at 0:23 (the one-tree diagram against T1-L-R), 0:42
  (training rows outside its box), 1:07 (feature X/Y outside the box), 1:14
  (text against the boxes below), 2:11 (correlated error merged with the L/R
  nodes) and 2:17 (the weak-signal and more-compute boxes running into
  correlated error). Spacing was revised and all six timestamps were checked
  again before the 17 Sep master.
- **The type checker the skill names wasn't there**, so the type-lock was done
  by inspecting the 1080p render.
- **It was left out of the first 4K batch.** The 17 Sep master was 1920×1080
  and wasn't part of the 21 Sep rebuild. On 24 Sep I asked for a check on the
  4K files Claude Code had produced, and for the remaining videos to be
  continued. All six scenes were rebuilt natively. The final export was blocked
  twice (GATE T failing on 5 beats, then 1). The fixes were the forest/table
  layout, wider root labels, and replacing the B03 footer arrow with a colon
  after a small-glyph crop. The sparse B07 recap card was recorded as
  deliberate, with the check itself left on.
- **The old handle came back.** On 2 Oct, OCR found `@NikBearBrown` on the
  closing frame of the 4K master, even though the 17 Sep QC report said none
  appeared. The cleanup set the channel handle explicitly instead of relying
  on template defaults, switched to `@sanjiv`, and redrew accent text in ink.
  A Whisper search of the narration found only "bearish", which is unrelated
  and was left in.

**Outcome.** 3840×2160, 24 fps, 3:34.6, 10 beats. GATE T pass (2 Oct, 0
FAILs), GATE V 0 blocker / 0 major. Branding QC: 429 frames at 2 fps plus 30
beat samples, with no flags.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic request, the narration approval, the six timestamped layout
  reports, and asking for the 4K work to be checked and finished. [CHECK: why
  this topic this week, and your review of the final cut.]
- Claude's: [CHECK: the 17 Sep build and the 24–27 Sep 4K continuation are
  Codex threads. Confirm which tool to credit.] The beat sheet, the worked
  average and the wording limits, the Manim scenes, the collision fixes, the
  native 4K rebuild, and the handle repair with OCR checks.

<!-- DRAFT. Sources: brutalist.art-main and -latest copies of BUILD-PROMPT.md,
     STATUS.md, TYPECHECK.md, FACTCHECK.md, SOURCES.md, PEDAGOGY.md,
     _qc/REPORT.md, BUILD-LOG.md, scenes.py / scenes.py.pre-qc-fix diff,
     beat_sheet.json (build.at 2026-10-02T12:24); reports/4k-audit-2026-09-24
     (README.md, random-forest-*final*.log); reports/branding-cleanup-2026-10-02
     (README.md, baseline-findings.json, final-qc result.json);
     video-resolution-inventory.md; Codex messages 17–24 Sep.
     Replace every [CHECK] and delete this comment. -->
