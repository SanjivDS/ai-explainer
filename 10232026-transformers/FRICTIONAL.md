# Frictional log — Explainer: Transformers - Encoder, Decoder & Self-Attention

## 2026-10-21 — the full architecture, a missing math module, and a rounding catch

- **Drive:** [27 LLM-1 Transformers](https://drive.google.com/file/d/1gQySl8qB8U3hszwgTdC9jUZFXjiJ_ou2/view) (uploaded 20 Nov)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** The first Transformers & LLMs video in the Deep Dive
set: the original encoder-decoder Transformer, with self-attention traced
through Q/K/V, multi-head merge, residuals, the causal mask, cross-attention and
the generation loop, then decoder-only models compared with the original two-stack
design. Native 3840×2160 on the older Claude template, Sanjiv persona, no
bottom-right footer and no beat-sheet footnote.

**What I tried, and what I expected.**
- I requested it on the morning of 21 Oct and approved the plan half an hour
  later. The worked example is a constructed three-token attention calculation,
  executed locally in `evidence/example.py`.
- I expected much of the Attention video to carry over, so the focus could be on
  how the encoder, the decoder and self-attention fit together, including the
  masked self-attention a decoder uses to predict the next token.

**Where it resisted, and what I did next.**
- **The math renderer was missing again.** Minutes after approval,
  `generate_math.py` failed with `No module named 'matplotlib.mathtext'`. The
  temporary Matplotlib folder made for Word Embeddings was still on disk, but the
  `brutalist.art-main` venv couldn't import from it. Matplotlib was reinstalled
  into `/private/tmp/transformers-math-deps`, which needed an escalated permission,
  and `build.sh` now points there. The config cache reuses `/private/tmp/cnn-mpl`.
- **A rounding error was caught before approval.** The first output coordinate
  rounds to 1.604, not 1.605. All assertions now pass, and the weighted sum uses
  the unrounded weights, with displayed values labeled as rounded.
- **Frame review found nine things to fix before final assembly:**
  - The cross-attention label sat on the diagonal connector.
  - The multi-head outputs didn't visibly route into the concatenation.
  - The short arrowheads were too small, with endpoint buffers too long.
  - The shifted input and target positions didn't line up, so they were placed
    with explicit coordinates.
  - Masked cells now say "block", so a zero attention weight isn't confused with
    a zero score. Pale fills that lowered contrast were removed.
  - The generation-loop return path was incomplete.
  - Crossing noun-token motion was replaced with a separated fade/swap.
  - The causal invariant is now shown next to the executed unmasked output.
  - The outro narration got clearer pauses.
- **Architecture claims were pinned to the paper.** The original post-norm block
  is labeled as such. The causal input is shifted, so a position sees itself but
  not future inputs. In cross-attention, Q comes from the decoder and K/V from the
  encoder. Teacher-forced parallel training is kept distinct from generation. No
  fixed linguistic roles are claimed for heads, and no memory or speed claims are
  made beyond the quadratic pair count.
- **Whitespace vs GATE V.** The progressive encoder block and the older verdict
  card keep deliberate whitespace, documented per beat. The validators are
  unchanged.
- **Audio check limits.** Local ASR, alignment and signal checks only, with no
  direct listening. ASR still misrecognizes "Sanjiv" and the short outro.

**Outcome.** 3840×2160, 24 fps, 5:09.9, 17 beats (12 teaching, 5 template
bookends). GATE T pass on all 17; GATE V 0 blocker / 0 major (34 samples);
sharpness pass (median Laplacian variance 369.4). All 620 timeline frames (31
contact sheets) and 85 beat samples reviewed. Full decode passed, no black
intervals, 609 footer samples clear, master peak 0.6557. 110 caption cues.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic and title, and the plan approval. [CHECK: your review of the
  cut, and whether the decoder-only family comparison was your idea.]
- Codex's: the script and storyboard, the constructed attention and mask-invariance
  example and its execution, the source check against Vaswani et al. and D2L, the
  dependency workaround, the Manim scenes, and the QC and repairs above.

<!-- DRAFT. Sources: BUILD-PROMPT.md, CHECKS-REPORT.md, FACTCHECK.md, PROMPTS.md,
     PLAN.json, SHARPNESS.md, SOURCES.md, STATUS.md, TYPECHECK.md
     (2026-10-21T17:57), _qc/REPORT.md, _qc/REVIEW-NOTES.md,
     SCRIPT-AND-STORYBOARD.md, beat_sheet.json (build.at 2026-10-21T17:57),
     build.sh, codex-user-messages.txt (21 Oct, incl. the 12:14 Guardian review
     excerpt), repo README.md. No BUILD-LOG.md in this folder; the dependency
     failure is known only from the Guardian excerpt, which is cut off before the
     reinstall result. Build sessions were Codex threads. Replace every [CHECK]
     and delete this comment. -->
