# Frictional log — Explainer: Backpropagation - How Neural Networks Actually Learn

## 2026-10-19 — every gradient checked twice, and a mascot in the way of the handle

- **Drive:** [25 DL-2 Backpropagation](https://drive.google.com/file/d/1f_kycoVZQ6QvMcogdwsCwsxiOYfV-FSs/view) (uploaded 10 Nov)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** The second Deep Learning video, picking up the Forward
Propagation network: add a target, trace the calculation backward with the chain
rule, and take one gradient-descent step. Native 3840×2160 on the older Confusion
Matrix template, Sanjiv persona, no bottom-right footer.

**What I tried, and what I expected.**
- I requested it on 19 Oct and approved the plan three minutes later. The plan
  reused the older Claude bookends and the Forward Propagation typography.
- The plan targeted about 5–6 minutes. The measured narration came to 4:31.
- I expected that reusing the forward network would make this one quicker, so
  the focus could be on how gradients are computed backward and used to update
  the weights.

**Where it resisted, and what I did next.**
- **The maths had to be provable, not just plausible.** All nine analytic
  gradients were checked against central finite differences (ε = 1e-6), with a
  maximum absolute error of 2.1 × 10⁻¹⁰. The example uses target 1, learning rate
  0.05 and a simultaneous update, and it evaluates ReLU away from zero, its
  non-differentiable point. Prediction 2.5 → 0.6175, loss 1.125 → 0.073153125,
  displayed as 0.0732.
- **Scope was stated, not implied.** This is one constructed example and one
  update. The zero gradient through the inactive ReLU applies to this input, not to
  the unit permanently. Nothing is claimed for arbitrary learning rates.
- **Frame review found four collisions.** The chain-rule arrows touched the
  equation, the output and hidden-weight derivative rows were crowded, the final
  ReLU gradient sat on its note, and the training-loop arrowheads were too small.
  All four were fixed in the scene code.
- **The outro mascot ran into the centered @sanjiv handle.** The shared
  `ClaudeTitleOutro` component got an optional `mascotGap` prop. This reel uses
  100; other reels keep the default.
- **B07's number was ambiguous when spoken.** The narration now says "negative
  zero point five". That beat was regenerated and realigned, and ASR confirmed the
  number.
- **Whitespace vs GATE V.** The progressive reveals (network, derivatives, ReLU,
  finite differences) and the overview, verdict and outro bookends are
  intentionally sparse. Each is documented in the beat sheet, and no thresholds
  were relaxed.
- **The build leans on temporary folders.** `build.sh` points `PYTHONPATH` at
  `/private/tmp/embeddings-math-deps`, the Matplotlib install made for Word
  Embeddings, and sets `MPLCONFIGDIR=/private/tmp/backprop-mpl`. A rebuild after
  those folders are cleared would need them recreated.
- **Audio check limits.** All source peaks are below full scale, and the master
  peak is 0.6433. ASR review only, with no direct listening.

**Outcome.** 3840×2160, 24 fps, 4:31.3, 16 beats. GATE T pass on all 16; GATE V 0
blocker / 0 major (32 samples); sharpness pass (median Laplacian variance 281.5;
lowest B15 at 63%). 543 timeline frames (28 contact sheets) and 80 beat samples
reviewed. Full decode passed, no black intervals, 532 footer samples clear. 105
caption cues.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic and title, and the plan approval. [CHECK: your review of the
  cut, and whether continuing the forward-propagation network was your request.]
- Codex's: the script and storyboard, the gradient derivations and the
  finite-difference check, the Manim scenes, the `mascotGap` change, the narration
  fix, and the QC above.

<!-- DRAFT. Sources: BUILD-LOG.md, CHECKS-REPORT.md, FACTCHECK.md, PROMPTS.md,
     PLAN.json, QC-REPORT.md, SHARPNESS.md, SOURCES.md, STATUS.md, TYPECHECK.md
     (2026-10-19T18:33), _qc/REPORT.md, SCRIPT-AND-STORYBOARD.md, beat_sheet.json
     (build.at 2026-10-19T18:38), build.sh, codex-user-messages.txt (19 Oct),
     repo README.md. No BUILD-PROMPT.md in this folder. Build sessions were Codex
     threads. Replace every [CHECK] and delete this comment. -->
