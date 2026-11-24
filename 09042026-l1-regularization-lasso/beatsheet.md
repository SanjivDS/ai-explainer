# L1 Regularization, Oversimplified — Beat Sheet

**Slug:** `claude-liam-l1-regularization-lasso` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:03.2

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 18.9s | Remotion | ClaudeComposerAsk | Claude composer opens; greeting 'Ciao, Liam'; the ask types in: why does L1 zero coefficients out; send arms; running text reads 'pricing the weights… |
| B01 | EXECUTIVE SUMMARY | 0:18.9 | 19.9s | Manim | — | spark line: 'Shrink some. Zero others.'; five coefficient bars grow to their unpenalised lengths; every bar shortens as the penalty is applied; two b… |
| B02 | FRAMEWORK — the objective | 0:38.7 | 19.9s | Manim | — | spark line: 'One score. Two jobs.'; DATA FIT card appears — squared error; plus sign, then the L1 PENALTY card — lambda × total absolute weight; arro… |
| B03 | MECHANISM — why exactly zero | 0:58.6 | 20.1s | Manim | — | spark line: 'The corner is everything.'; two headers set the comparison: L1 absolute value vs L2 squared value; the L1 diamond and the L2 circle draw… |
| B04 | WORKED EXAMPLE — the regularization path | 1:18.7 | 16.6s | Manim | — | spark line: 'Watch them drop out.'; axes draw on; four named coefficients label the left margin; four paths trace downward as the penalty grows; terr… |
| B05 | DECISION — choosing lambda | 1:35.3 | 18.7s | Manim | — | spark line: 'Tune it. Don't guess.'; axes draw on with a rotated 'validation error' label; the U-shaped validation curve traces out; terracotta dot m… |
| B06 | FALSIFIABILITY — where sparsity lies | 1:54.0 | 20.6s | Manim | — | spark line: 'Where sparsity lies.'; CORRELATED TWINS tile: keeps one, drops its twin; UNSTABLE PICKS tile: resample, get a new subset; SHRINKAGE BIAS… |
| B07 | VERDICT | 2:14.6 | 19.6s | Manim | — | artifact board opens: 'Shrink, then select'; SHRINK row fills: every weight pulled toward zero; SELECT row fills: some weights land exactly on zero;… |
| B08 | HANDOFF | 2:34.2 | 20.0s | Remotion | ClaudeComposerAsk | Claude composer opens with 'Your turn.'; the exact prompt types in as it is read aloud; send arms; running text reads 'paste this into Claude…'; rubr… |
| B09 | OUTRO | 2:54.2 | 8.2s | Manim | — | dark field and the terracotta NBB mark land; poster title restates: 'L1 Regularization.'; locked @NikBearBrown handle holds |

8 Manim beats (code in [`scenes.py`](scenes.py)) · 2 Remotion beats.
