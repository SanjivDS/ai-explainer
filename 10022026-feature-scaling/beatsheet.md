# Feature Scaling: Standardization vs Normalization, Oversimplified — Beat Sheet

**Slug:** `claude-liam-feature-scaling` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:41.8

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 19.8s | Remotion | ClaudeComposerAsk | Claude composer opens on 'Ahoj, Liam'; the feature-scaling comparison prompt types in; a dollar-scale column towers over a fractional column; answer… |
| B01 | EXECUTIVE SUMMARY | 0:19.8 | 22.0s | Manim | — | spark line: 'Change units, not information.'; two unequal feature axes distort a circular neighborhood; axes rescale and the intended neighborhood be… |
| B02 | WHY SCALE | 0:41.8 | 22.7s | Manim | — | spark line: 'Units change the geometry.'; a KNN distance ruler is dominated by the large-scale feature; a gradient zigzags through an elongated loss… |
| B03 | STANDARDIZATION | 1:04.5 | 21.6s | Manim | — | spark line: 'Center. Then scale.'; formula z = (x − mean) / standard deviation writes on; 10, 20, 30 settle on a number line and mean 20 is marked; s… |
| B04 | MIN-MAX NORMALIZATION | 1:26.1 | 19.3s | Manim | — | spark line: 'Anchor to the endpoints.'; formula (x − min) / (max − min) writes on; 10, 20, 30 map evenly to 0, 0.5, 1; an outlier at 100 extends the… |
| B05 | COMPARE | 1:45.4 | 22.7s | Manim | — | spark line: 'Both defaults can bend.'; standardization panel shows an unbounded axis centered at zero; min–max panel shows the training interval lock… |
| B06 | LEAKAGE AND NAMING | 2:08.0 | 23.2s | Manim | — | spark line: 'Fit train. Reuse everywhere.'; raw data splits into train and test before the scaler; training data fits scaler parameters; test data ca… |
| B07 | VERDICT | 2:31.3 | 22.5s | Remotion | ClaudeVerdictArtifact | verdict artifact opens as a scaler selection receipt; model sensitivity check appears first; standardize and min–max choices resolve with their assum… |
| B08 | HANDOFF | 2:53.7 | 26.6s | Remotion | ClaudeComposerAsk | handoff composer opens with 'Your turn.'; the exact spoken scaler-comparison prompt types in; four leakage-safe pipelines preview side by side; perfo… |
| B09 | TITLE RESTATE | 3:20.4 | 21.3s | Remotion | ClaudeTitleOutro | unequal axes contract into a balanced title lockup; standardization and min–max formulas settle beneath; fit train / transform rest rule locks on; 'L… |

6 Manim beats (code in [`scenes.py`](scenes.py)) · 4 Remotion beats.
