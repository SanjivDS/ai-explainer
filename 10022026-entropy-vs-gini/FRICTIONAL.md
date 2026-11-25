# Frictional log — Explainer: Entropy vs Gini Impurity

## 2026-10-04 — structured equations, and a split where the two criteria disagree

- **Drive:** [16 Entropy and Gini Impurity](https://drive.google.com/file/d/18uo3Szq3xQPllJUmH9YBMH78c7yEEE6X/view) (uploaded 11 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on the two ways a decision tree
scores how mixed a node is. It calculates Gini and entropy on the same examples,
traces their curves, and finds a case where they pick different best splits.
12 beats (7 Manim, 5 Remotion bookends), native 3840×2160, built on 4 Oct with the
same carried-forward notes as K-means: @sanjiv, "Liam, in for Sanjiv", no
production footers.

**What I tried, and what I expected.**
- I requested it at 13:20 on 4 Oct with just the title, relying on the notes
  already given in that session.
- [CHECK: what you expected, e.g. that this would reuse the K-means setup
  unchanged, or whether you knew going in that it needed real equations.]

**Where it resisted, and what I did next.**
- **No matching scene in the library.** The candidates were unrelated decision
  diagrams, so the impurity arithmetic was drawn natively in Manim.
- **The equations needed a structured math renderer.** In August I had
  asked to work without MacTeX for now, so the six equations (Gini, the worked
  Gini value, entropy, the worked entropy value, the weighted children and the
  reduction) were rendered as MathText SVG. That used matplotlib 3.9.4 installed
  in an isolated temporary folder (`/private/tmp/entropy-mathdeps`). The SVGs are
  kept in `math/`, and BUILD-PROMPT records the install, because a rebuild will
  need it again.
- **Finding a real disagreement took a constructed case.** Both candidate
  splits had to come from the same parent. Split A wins on Gini (0.3125 vs 0.3333),
  and split B wins on entropy (0.689 vs 0.704). The candidate features are saved in
  `evidence/` to show both splits can actually be made.
- **Three facts needed careful wording.**
  - Gini is read as the chance that two draws *with replacement* disagree. The
    majority-vote error (0.20) is a different quantity and is labelled separately.
  - Gini is doubled only in the curve-comparison beat, and labelled there.
  - Entropy is in base 2. A pure training leaf is shown not to imply held-out
    accuracy.
- **Frame review found four defects, fixed in the scene code.**
  - Formula annotation spacing.
  - Clearance under the training-leaf heading.
  - Probability-bar contrast.
  - Score-label contrast.

  B03, B04 and B08 were re-rendered, then B04 and B07 again for contrast.
- **The run stopped after the master.** The master was compiled at 13:38, and the
  captions and delivery QC were finished after I sent "continue" at 16:16.
  [CHECK: why it stopped.]

**Outcome.** 3840×2160, 24 fps, 3:41.7, 12 beats. GATE T pass (12/12), GATE V 0
blocker / 0 major on 24 frames, 443 frames at 2 fps plus 36 per-beat samples
audited with zero old-name or footer-label matches. Every equation was checked in
its revealed state. SRT (80 cues, 0 errors) and VTT captions included.

**What the AI tools contributed, and what I did with it.**
- Mine: [CHECK: the topic choice and its place in the series, the brief, and your review of the cut before the 11 Oct upload.]
- The agent's (this build ran in a Codex session, per my message log): the beat
  sheet and narration, the computed node and split values with their fact-check,
  the constructed disagreement case, the MathText equations, the Manim scenes,
  the build, and the frame QC and fixes listed above.

<!-- DRAFT. Sources: BUILD-LOG.md, BUILD-PROMPT.md, CHECKS-REPORT.md,
     FACTCHECK.md, SOURCES.md, SRTCHECK.md, TYPECHECK.md, _qc/DELIVERY-QC.md,
     _qc/REPORT.md, evidence/execution.txt, make_math.py, math-deps.log,
     native-fix/contrast-fix logs, beat_sheet.json (build.at 2026-10-04T13:38),
     the 4 Oct Codex messages (13:20, 16:16), the 12 Aug Claude Code message on
     MacTeX, and the repo README. Replace every [CHECK] and delete this comment. -->
