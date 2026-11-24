# XGBoost - Why It Works So Well — Beat Sheet

**Slug:** `claude-liam-xgboost` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:30.0

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 16.5s | Remotion | ClaudeComposerAsk | Composer types the question; Result lists corrections, controls, and efficient search |
| B01 | EXECUTIVE SUMMARY | 0:16.5 | 12.2s | Remotion | BrutalistHesitantWriter | Writer replaces magic with controlled; Corrected overview remains legible |
| B02 | FRAMEWORK | 0:28.7 | 21.7s | Manim | B02_Scene | A feature split branches into a conditional second split; Three trees join an additive prediction chain; Loss, controls and search framework appears |
| B03 | WORKED EXAMPLE | 0:50.3 | 21.6s | Manim | B03_Scene | Four targets and baseline six appear; Residuals populate row by row; Two leaves average the residuals; Half-step updates predictions and MSE |
| B04 | CURVATURE | 1:12.0 | 22.0s | Manim | B04_Scene | Two loss curves share the tangent at zero; Their different minima are marked; Slope and curvature callouts resolve |
| B05 | REGULARIZATION | 1:34.0 | 22.6s | Manim | B05_Scene | Two leaf-score bars shrink under L2; Learning-rate half-step appears as a separate operation; Split and depth controls surround the tree |
| B06 | SYSTEMS | 1:56.6 | 24.9s | Manim | B06_Scene | Individual values move into histogram bins; A candidate split scans the bins; Missing row routes to learned default; Dependent tree rounds contrast w… |
| B07 | FALSIFIABILITY | 2:21.4 | 22.5s | Manim | B07_Scene | Training and validation curves draw over rounds; Validation minimum is marked; Tree extrapolation stays flat beyond observed range |
| B08 | VERDICT | 2:43.9 | 22.3s | Remotion | ClaudeVerdictArtifact | Verdict artifact reveals the four complementary mechanisms |
| B09 | HANDOFF | 3:06.3 | 18.9s | Remotion | ClaudeComposerAsk | Viewer prompt types; Arithmetic, validation and test rubric appears |
| B10 | OUTRO | 3:25.2 | 4.5s | Remotion | ClaudeTitleOutro | Exact title restatement with channel mascot |

6 Manim beats (code in [`scenes.py`](scenes.py)) · 5 Remotion beats.
