# Cross-Validation — Why One Train/Test Split Isn't Enough — Beat Sheet

**Slug:** `claude-liam-cross-validation` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 4:05.8

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 18.7s | Remotion | ClaudeComposerAsk | Type the reproducible comparison request; Preview rotating folds and leakage checks |
| B01 | OVERVIEW | 0:18.7 | 12.7s | Remotion | BrutalistHesitantWriter | Replace complete with partial; Hold the corrected overview |
| B02 | SPLIT | 0:31.4 | 22.5s | Manim | B02_Scene | Reveal two recorded 80/20 partitions; Grow RMSE bars to 0.456 and 0.574 |
| B03 | FOLDS | 0:53.9 | 20.6s | Manim | B03_Scene | Build a five-by-five fold matrix; Move held-out role across rows with fresh fit labels; Keep final test separate |
| B04 | SCORES | 1:14.5 | 21.0s | Manim | B04_Scene | Reveal all five computed scores; Draw the mean; Show overlapping training sets and distinguish spread from confidence |
| B05 | SELECT | 1:35.5 | 21.4s | Manim | B05_Scene | Compare linear and cubic CV means; Select cubic and refit on all development records; Open final test and reveal 0.488 RMSE |
| B06 | LEAKAGE | 1:56.9 | 21.4s | Manim | B06_Scene | Show incorrect preprocessing across the fold boundary; Remove leaking arrow; Fit scaler inside training and apply it to validation |
| B07 | STRUCTURE | 2:18.3 | 23.0s | Manim | B07_Scene | Preserve class counts across folds; Keep patient records together; Move chronological boundary forward |
| B08 | LIMITS | 2:41.3 | 23.2s | Manim | B08_Scene | Count ten fits for two candidates and five folds; Place tuning inside outer evaluation; Move future-data marker beyond the observed sample |
| B09 | VERDICT | 3:04.5 | 21.6s | Remotion | ClaudeVerdictArtifact | Reveal role-specific summary |
| B10 | YOUR TURN | 3:26.1 | 31.7s | Remotion | ClaudeComposerAsk | Read the complete viewer experiment while typed; Show checks for data separation |
| B11 | OUTRO | 3:57.8 | 7.7s | Remotion | ClaudeTitleOutro | Restate full title and hold @sanjiv |

7 Manim beats (code in [`scenes.py`](scenes.py)) · 5 Remotion beats.
