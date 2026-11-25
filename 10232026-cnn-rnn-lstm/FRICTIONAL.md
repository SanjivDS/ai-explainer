# Frictional log — Explainer: CNN vs RNN vs LSTM - When and Why to Use Each

## 2026-10-20 — a comparison that refuses to name a winner

- **Drive:** [26 DL-3 CNN vs RNN vs LSTM](https://drive.google.com/file/d/1RxkUe1leAyT9_OjvVmeXjtJTeAIthLAo/view) (uploaded 12 Nov)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** The third Deep Learning video: local patterns (CNN),
carried sequence state (basic RNN) and gated memory (LSTM), and how to choose
between them for a task. Native 3840×2160 on the older Confusion Matrix template,
Sanjiv persona, no bottom-right footer.

**What I tried, and what I expected.**
- I requested it on the evening of 19 Oct and approved the plan the next morning.
  The plan targeted about 5–6 minutes; the measured narration came to 4:31.8.
- I expected to compare the three architectures by their strengths and
  suitability for different tasks, which meant studying all three closely.

**Where it resisted, and what I did next.**
- **The template's overview writer can't correct a phrase.** The older hesitant
  writer matches single words, not phrases, so the opening misconception was
  shortened to "Choose a winner." Its one correction then lands on the approved
  sentence "Choose a fit for the task." The narration didn't change.
- **Scene fixes.** The time-dependency arrows were enlarged within their gaps.
  The experimental-choice scene now transitions into a train / held-out-evaluation
  schematic.
- **Whitespace vs GATE V.** The lower space in B03, B05 and B10 and in the older
  verdict card is deliberate. It is documented per beat, without changing
  validator thresholds.
- **Editorial safeguards for a comparison video.** An LSTM is a kind of RNN, so
  "RNN" here means a basic, ungated RNN. CNNs aren't limited to images: temporal
  CNNs (Bai et al.) are credible sequence candidates from one historical study,
  not a universal ranking. 0.5¹⁰ is an illustrative scalar product, not a full RNN
  derivative. A same-width LSTM has more parameters because it has four affine
  transforms to the RNN's one. Parallelism is stated as a dependency fact, not a
  measured speed-up. Live prediction must not see future inputs. The suggested
  applications are labeled as starting points to validate on held-out data. No
  training benchmark was run.
- **The build leans on temporary folders.** `build.sh` points `PYTHONPATH` at
  `/private/tmp/embeddings-math-deps`, the Matplotlib install made for Word
  Embeddings, and sets `MPLCONFIGDIR=/private/tmp/cnn-mpl`; `build.sh` regenerates
  the equation SVGs with Matplotlib from that folder on every run.
- **Audio check limits.** Local ASR and decoded levels only. ASR spells LSTM and
  Sanjiv inconsistently and normalizes spoken numbers, and there was no direct
  listening.

**Outcome.** 3840×2160, 24 fps, 4:31.8, 17 beats. GATE T pass on all 17; GATE V 0
blocker / 0 major (34 samples); sharpness pass (median Laplacian variance 244.9).
544 timeline samples at 2 fps (28 contact sheets) plus 85 beat samples reviewed,
with no collisions, clipping or mascot/handle overlap. Full decode passed, 530
footer samples clear, master peak 0.6293. All 720 narration words are in 94 caption
cues.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic and title, framing it as choosing a fit for the task rather
  than a ranking, the closing viewer task (input structure, context, labels,
  latency), the plan approval, and reviewing the cut.
- Codex's: the script and storyboard, the constructed examples and their executed
  assertions, the source check against D2L and Bai et al., the Manim scenes, and
  the QC and fixes above.
