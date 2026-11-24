# Confusion Matrix — Beat Sheet

**Slug:** `claude-liam-confusion-matrix` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 2:14.5

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 14.6s | Remotion | ClaudeComposerAsk | Composer types the ask under 'Selam, Liam'; Answer lines land: four cells, two mistakes, rows and columns |
| B01 | EXECUTIVE SUMMARY | 0:14.6 | 12.5s | Remotion | BrutalistHesitantWriter | Writer types 'one accuracy score', then strikes it; 'four separate counts' types in its place; Context cards: Truth · Prediction · Mistakes |
| B02 | FRAMEWORK | 0:27.0 | 16.8s | Manim | B02_Scene | Actual axis labels the rows; Predicted axis labels the columns; Diagonal cells fill: True Positive, True Negative; Off-diagonal cells fill: False Neg… |
| B03 | WORKED EXAMPLE | 0:43.8 | 18.1s | Manim | B03_Scene | Empty matrix with 1,000 payments · 20 fraud header; TP counter lands on 15; FP counter lands on 10; FN counter lands on 5; TN counter lands on 970; C… |
| B04 | READING RATES | 1:01.9 | 18.0s | Manim | B04_Scene | Fraud row highlights; recall fraction 15/20 = 75% builds beside it; Flagged column highlights; precision fraction 15/25 = 60% builds; Honest row high… |
| B05 | FALSIFIABILITY | 1:19.9 | 19.2s | Manim | B05_Scene | Two matrices side by side: Our model vs Never flags; Accuracy bars: 98.5% and 98.0%, nearly equal; Never-flags TP cell reads 0; FN cell 20 in terraco… |
| B06 | VERDICT | 1:39.1 | 14.5s | Remotion | ClaudeVerdictArtifact | Verdict artifact reveals four reporting rules |
| B07 | HANDOFF | 1:53.6 | 15.7s | Remotion | ClaudeComposerAsk | Viewer prompt types into the composer; Checklist appears: truth axis labeled, rates from cells, majority baseline |
| B08 | OUTRO | 2:09.3 | 5.0s | Remotion | ClaudeTitleOutro | Exact title restatement with handle and slug-seeded mascot |

4 Manim beats (code in [`scenes.py`](scenes.py)) · 5 Remotion beats.
