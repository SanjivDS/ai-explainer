# L2 Regularization, Oversimplified — Beat Sheet

**Slug:** `claude-liam-l2-regularization-ridge` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:12.6

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 17.0s | Remotion | ClaudeComposerAsk | Claude composer opens on cream with greeting 'Shalom, Liam'; the L2 question types into the composer; terracotta send arms; running text says 'shrink… |
| B01 | EXECUTIVE SUMMARY | 0:17.0 | 19.1s | Manim | — | spark line appears: 'Fit, with restraint.'; a balance appears with training error on the left; squared coefficient penalty lands on the right; lambda… |
| B02 | FRAMEWORK — the objective | 0:36.1 | 21.1s | Manim | — | residual-sum-of-squares term builds on the left and is labelled 'fit'; a plus sign and lambda appear in terracotta; sum of squared slope coefficients… |
| B03 | MECHANISM — why squaring shrinks | 0:57.2 | 21.8s | Manim | — | one coefficient bar doubles; its penalty tile expands from one square to four; loss contours draw around an unconstrained optimum; a circular L2 boun… |
| B04 | WORKED EXAMPLE — correlated predictors | 1:19.0 | 21.1s | Manim | — | two nearly overlapping predictor arrows feed one prediction; OLS assigns a tall positive bar to x1 and a tall negative bar to x2; sample A swaps to s… |
| B05 | DECISION — choose lambda | 1:40.1 | 20.8s | Manim | — | log-lambda axis appears from weak to strong regularization; coefficient paths shrink across the axis; cross-validation error curve draws, falls, then… |
| B06 | FALSIFIABILITY — where the shortcut breaks | 2:00.9 | 21.5s | Manim | — | three diagnostic cards enter: scale, intercept, sparsity; meter and millimeter versions of one feature produce unequal coefficient bars; standardizat… |
| B07 | VERDICT | 2:22.3 | 22.6s | Manim | — | Claude verdict artifact opens with title 'What Ridge buys'; row one reveals: large weights → charged; row two reveals: variance → reduced; row three… |
| B08 | YOUR TURN | 2:45.0 | 21.0s | Remotion | ClaudeComposerAsk | Claude composer appears with greeting 'Your turn.'; the complete demo prompt types in verbatim; running text says 'paste this into Claude…'; three ru… |
| B09 | OUTRO | 3:05.9 | 6.5s | Remotion | ClaudeTitleOutro | locked crisp-safe mascot enters by translation only; poster title appears: 'L2 Regularization.'; @Sanjiv handle resolves beneath; terracotta period h… |

7 Manim beats (code in [`scenes.py`](scenes.py)) · 3 Remotion beats.
