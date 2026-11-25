# Frictional log — Explainer: Neural Networks - Forward Propagation Explained

## 2026-10-18 — the first Deep Learning video, and a run of small geometry fixes

- **Drive:** [24 DL-1 Forward Propagation](https://drive.google.com/file/d/1et1AAhBKixBxMH0R-7YwtEiE0oB_cShG/view) (uploaded 6 Nov)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** The first Deep Learning video in the Deep Dive set: a
two-input, two-hidden-unit network traced through weighted sums, ReLU and a
prediction, in column-vector notation, showing why stacked layers without an
activation collapse into one affine map. Native 3840×2160 on the older Confusion
Matrix template, Sanjiv persona, no bottom-right footer.

**What I tried, and what I expected.**
- I requested it on the morning of 18 Oct and approved the plan five minutes
  later. The build followed the Attention reel's pipeline.
- [CHECK: what you expected going in, e.g. that a single small network would be
  quicker than the NLP videos, or that Backpropagation would reuse this network.]

**Where it resisted, and what I did next.**
- **The diagrams were mathematically wrong in small ways.** The matrix brackets
  were reflected around the origin. The ReLU plot curved instead of having a
  straight corner, and its marker didn't follow the drawn line. Both were
  corrected in the scene code.
- **The overview carried the previous episode's context.** It was replaced with
  this episode's Combine / Activate / Predict labels. The older writer component
  matches single tokens only, so the misconception correction is "updates → uses",
  which keeps the approved meaning.
- **B09's header overlapped its rows.** The layout was rebuilt as explicit
  aligned rows.
- **B04's audio clipped after decoding.** The MP3 peak went over full scale by
  0.0067 (7 samples). A −2 dB gain brought it to 0.8043 without touching timing.
- **GATE T failed on B06.** The smallest text run was 35 px against the 41 px
  floor. The output parameters and arithmetic were enlarged and the note raised to
  32 pt, then B06 was re-rendered and the unchanged checker re-run.
- **GATE V flagged four MAJOR underfills**: B03 at 49%, B08 at 55%, and B11 at 47%
  in two samples, against a 55% minimum. These are the template's whitespace, so
  each was given a documented per-scene sparse-design declaration. The validators
  weren't modified, and the original findings stay in `_qc/initial-gate-v.md`.
- **One black frame in the outro.** The solid background now persists behind the
  content fade, and a full blackdetect finds no black intervals. The pre-outro
  sample hashes match the reviewed build, and the changed outro samples were
  reviewed again.
- **Sources and conventions.** The Deep Learning book page couldn't be fetched, so
  it isn't relied on. D2L uses a row-batch convention, so the episode says
  explicitly that it uses columns. The constructed numbers are executed in
  `evidence/example.py`: prediction 2.5, and −1 with the second input changed to 3.
  The collapsed affine map has effective weights (2, −3) and bias 2.
- **Audio check limits.** ASR and signal checks only, without direct listening.

**Outcome.** 3840×2160, 24 fps, 4:04.0, 14 beats. GATE T pass, GATE V 0 blocker /
0 major after the declarations, 488 timeline samples at 2 fps (25 contact sheets)
plus boundary and 15/50/85% samples reviewed, 477 footer samples clear, full
decode passed, master peak 0.6632. 98 caption cues.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic and title, and the plan approval. [CHECK: your review of the
  cut, and whether choosing a regression output (not a probability) or the
  changed-input check was your idea.]
- Codex's: the script and storyboard, the constructed network and its executed
  evidence, the source check, the Manim scenes, and the QC and repairs listed
  above.

<!-- DRAFT. Sources: BUILD-LOG.md, BUILD-PROMPT.md, CHECKS-REPORT.md,
     FACTCHECK.md, PROMPTS.md, QC-REPORT.md, SOURCES.md, STATUS.md, TYPECHECK.md
     (2026-10-18T20:09), _qc/REPORT.md, _qc/initial-gate-v.md, beat_sheet.json
     (build.at 2026-10-18T20:10), SCRIPT-AND-STORYBOARD.md,
     codex-user-messages.txt (18–19 Oct), repo README.md. Note: the README's
     "Built: 12–16 Oct" week ends before the 18 Oct request and master; the final
     verification is dated 19 Oct. Build sessions were Codex threads. Replace every
     [CHECK] and delete this comment. -->
