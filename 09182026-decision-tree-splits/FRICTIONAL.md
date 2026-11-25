# Frictional log — Explainer: Decision Trees: How Splits Actually Work, Oversimplified

## 2026-09-18 — dotted guides that ran through the nodes

- **Drive:** [09 Decision Tree](https://drive.google.com/file/d/1ObfLER35dWIxFoyfZmbZwT9woN8qdirV/view) (uploaded 3 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on how a classification tree picks
a split: score candidate (feature, threshold) pairs by the weighted Gini
impurity of the children, and keep the best one. The worked example is a
six-row dataset. Threshold 2.5 leaves weighted impurity 0.25, and threshold 3.5
splits it perfectly (0, a decrease of 0.5). 10 beats: 6 Manim and 4 Remotion
bookends.

**What I tried, and what I expected.**
- I asked for "Decision Trees (How Splits Actually Work)" on 17 Sep and approved
  the narration that evening.
- [CHECK: what you expected, e.g. that a tree diagram would be simple to lay
  out after the metrics video, or that one review pass would be enough.]

**Where it resisted, and what I did next.**
- **The wording had to be narrowed while scripting.** The script doesn't say a
  tree "asks the most useful question". It says a splitter scores candidates
  under a criterion. Midpoint thresholds are credited specifically to
  scikit-learn's exact best-split search. "Information gain" isn't used loosely;
  the example names Gini impurity decrease. Greediness is described as local
  only.
- **The type checker the skill names wasn't there.** `scripts/type_check.py`
  was missing, so the equivalent checks were done by hand on the 1080p render
  and documented in TYPECHECK.md.
- **Lines and nodes overlapped at 0:21 and 0:25.** I reported it on 18 Sep, then
  pushed back on the first answer: "is it meant for the dotted lines to overlap
  with the nodes?" In the fix, all five dotted threshold guides sit between
  neighbouring sample nodes, and the sample row clears before the LEFT/RIGHT
  branch arrows appear.
- **No STATUS file.** I asked for one on 18 Sep, along with the random forest
  video's.
- **It was rendered at 1080p.** After Sanjana's 21 Sep note that nothing was in
  4K, all ten beats were rebuilt at native 3840×2160 that morning. QC covered 402
  frames at 2 fps across 17 contact sheets, and the 0:21/0:25 fix was checked
  again. Sanjana said again that afternoon that the videos still weren't 4K.
  The 24 Sep audit confirmed the 3840×2160
  stream with ffprobe.
- **The branding cleanup was blocked by the type gate (2 Oct).** The final
  export failed GATE T twice (5 beats each time). A debug crop found one text
  run in B02, 38 px tall against a 41 px floor. The scene diff shows the arrow
  in the B02 footer ("LOWER CHILD IMPURITY → LARGER DECREASE") replaced with a
  colon, terracotta text redrawn in ink, a darker accent, and `@sanjiv`
  replacing `@Sanjiv`.

**Outcome.** 3840×2160, 24 fps, 3:21.1, 10 beats. GATE T pass (2 Oct, 0
FAILs), GATE V 0 blocker / 0 major. Branding QC: 402 frames at 2 fps plus 30
beat samples, with no flags.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic request, the narration approval, the timestamped overlap
  report and the follow-up when the first fix didn't satisfy me. [CHECK: why
  this topic this week, and anything else you reviewed.]
- Claude's: [CHECK: the session records for this build and the 21 Sep 4K
  rebuild are Codex threads. Confirm which tool to credit.] The beat sheet, the
  six-row example and its arithmetic, the source-scoped wording, the Manim
  scenes, the overlap fix, the 4K rebuild and the type-gate repair.

<!-- DRAFT. Sources: brutalist.art-main and -latest copies of BUILD-PROMPT.md,
     STATUS.md, TYPECHECK.md, FACTCHECK.md, SOURCES.md, PEDAGOGY.md,
     _qc/REPORT.md, scenes.py diff, beat_sheet.json (build.at
     2026-10-02T23:45); reports/4k-audit-2026-09-24/README.md;
     reports/branding-cleanup-2026-10-02 (claude-liam-decision-tree-splits*.log,
     type-debug.log, type-debug-repair.log, final-qc result.json); Codex
     messages 17–21 Sep. Replace every [CHECK] and delete this comment. -->
