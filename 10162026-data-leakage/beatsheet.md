# Data Leakage — The ML Mistake That Gives Fake-Good Results — Beat Sheet

**Slug:** `claude-liam-data-leakage` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:57.9

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 16.9s | Remotion | ClaudeComposerAsk | Show the request for a leakage audit and reproducible noise experiment |
| B01 | OVERVIEW | 0:16.9 | 16.6s | Manim | B01_Scene | Reveal the three information boundaries directly |
| B02 | TIME | 0:33.5 | 19.2s | Manim | B02_Scene | Draw prediction-time boundary; show future resolution entering a support-ticket predictor |
| B03 | GROUPS | 0:52.7 | 21.2s | Manim | B03_Scene | Show the same customer in train and test; regroup whole customers |
| B04 | EXPERIMENT | 1:13.9 | 19.1s | Manim | B04_Scene | Reveal 300 rows, 10,000 noise features and random binary labels; split 180/120 |
| B05 | LEAK | 1:33.0 | 20.4s | Manim | B05_Scene | Show selection using all labels; trace test-label information into selected columns |
| B06 | RESULT | 1:53.4 | 22.5s | Manim | B06_Scene | Reveal measured leaky and clean scores side by side on a common scale |
| B07 | REPAIR | 2:15.9 | 23.1s | Manim | B07_Scene | Draw train-only learned transform and fixed test transform; enclose training pipeline |
| B08 | STRESS TEST | 2:39.0 | 22.9s | Manim | B08_Scene | Compare ordinary overfitting with evaluation contamination; show limits of a shuffle check |
| B09 | VERDICT | 3:01.9 | 20.7s | Remotion | ClaudeVerdictArtifact | Reveal four practical audit steps |
| B10 | YOUR TURN | 3:22.7 | 26.6s | Remotion | ClaudeComposerAsk | Show and read the complete viewer prompt |
| B11 | OUTRO | 3:49.3 | 8.4s | Remotion | ClaudeTitleOutro | Restate the full title and @sanjiv |

8 Manim beats (code in [`scenes.py`](scenes.py)) · 4 Remotion beats.
