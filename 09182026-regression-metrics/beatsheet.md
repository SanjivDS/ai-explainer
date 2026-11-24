# Regression Metrics: MAE, MSE, RMSE, R², and MAPE, Oversimplified — Beat Sheet

**Slug:** `claude-liam-regression-metrics` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:37.5

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 21.1s | Remotion | ClaudeComposerAsk | Claude composer opens on 'Kumusta, Liam'; the five-metric comparison prompt types into the composer; send arms; running text reads 'measuring the mis… |
| B01 | EXECUTIVE SUMMARY | 0:21.1 | 22.7s | Manim | — | spark line: 'One residual. Five lenses.'; one prediction-to-actual gap appears as a residual; the residual branches into absolute, squared, rooted, b… |
| B02 | FRAMEWORK | 0:43.8 | 22.9s | Manim | — | spark line: 'Residuals come first.'; actual and predicted dots connect into signed residual arrows; absolute and square transforms animate side by si… |
| B03 | WORKED EXAMPLE | 1:06.8 | 20.9s | Manim | — | four actual/prediction pairs enter as vertical columns; residual magnitudes 1, 1, 1, 3 draw between each pair; MAE tray averages 1+1+1+3 into 1.5; MS… |
| B04 | COMPARE | 1:27.7 | 22.0s | Manim | — | two model lanes appear: A errors [2,2,2,2], B errors [0,0,0,8]; both MAE counters meet at 2; RMSE counters split to 2 versus 4; B's single 8 expands… |
| B05 | R² | 1:49.7 | 20.7s | Manim | — | spark line: 'Beat the baseline.'; mean-only baseline residual bars establish total squared error; model residual bars shrink and the removed fraction… |
| B06 | MAPE FAILURE CASE | 2:10.4 | 22.7s | Manim | — | equal absolute misses of 1 appear over actuals 1 and 100; percentage labels diverge to 100% and 1%; actual value approaches zero and the ratio meter… |
| B07 | VERDICT | 2:33.2 | 26.7s | Remotion | ClaudeVerdictArtifact | Claude verdict artifact opens with a metric-to-cost matrix; MAE and RMSE rows highlight their error-cost assumptions; R² row moves beside the mean ba… |
| B08 | HANDOFF | 2:59.9 | 27.2s | Remotion | ClaudeComposerAsk | Claude composer opens on 'Your turn.'; the full evaluation prompt types verbatim; running text reads 'testing metric assumptions…'; checklist lands:… |
| B09 | OUTRO | 3:27.1 | 10.2s | Remotion | ClaudeTitleOutro | poster title restates the episode title; title-safe poster frame settles; @sanjiv handle holds beneath the title |

6 Manim beats (code in [`scenes.py`](scenes.py)) · 4 Remotion beats.
