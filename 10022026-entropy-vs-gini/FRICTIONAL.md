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
- I expected to reuse the K-means setup, and to show with real equations how the
  two impurity measures score a split and why they often select similar splits.

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
  captions and delivery QC were finished after I sent "continue" at 16:16. It most likely stopped
  at a usage limit.

**Outcome.** 3840×2160, 24 fps, 3:41.7, 12 beats. GATE T pass (12/12), GATE V 0
blocker / 0 major on 24 frames, 443 frames at 2 fps plus 36 per-beat samples
audited with zero old-name or footer-label matches. Every equation was checked in
its revealed state. SRT (80 cues, 0 errors) and VTT captions included.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic choice, the brief, and reviewing the cut before the 11 Oct
  upload.
- Codex's: the beat
  sheet and narration, the computed node and split values with their fact-check,
  the constructed disagreement case, the MathText equations, the Manim scenes,
  the build, and the frame QC and fixes listed above.
