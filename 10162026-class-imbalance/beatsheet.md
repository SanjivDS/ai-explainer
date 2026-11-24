# Class Imbalance — Why Accuracy Can Be Misleading — Beat Sheet

**Slug:** `claude-liam-class-imbalance` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 4:01.5

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 18.1s | Remotion | ClaudeComposerAsk | Type the experiment request; Show the baseline and rare-event question |
| B01 | OVERVIEW | 0:18.1 | 10.3s | Manim | B01_Scene | Present the correct overview directly; reveal three evaluation questions without typing or erasing. |
| B02 | BASELINE | 0:28.4 | 21.1s | Manim | B02_Scene | Build a 100-dot population; one dot represents ten cases; Identify the ten faults; Reveal 99% accuracy and zero faults found |
| B03 | COUNTS | 0:49.5 | 22.9s | Manim | B03_Scene | Draw explicit actual-row and prediction-column headers; Reveal eight hits and two misses; Reveal twenty false alarms and 970 correct normal cases |
| B04 | METRICS | 1:12.4 | 18.5s | Manim | B04_Scene | Separate actual faults from the alert queue; Draw grouped numerical fractions for recall and precision; Hold the denominators side by side |
| B05 | BALANCE | 1:31.0 | 22.8s | Manim | B05_Scene | Compare baseline and scored-rule accuracy bars; Replace with equally weighted per-class recall bars; Reveal balanced accuracy of 50% and about 89% |
| B06 | THRESHOLD | 1:53.8 | 23.8s | Manim | B06_Scene | Move threshold on a zero-to-one score scale; Update hits, false alarms, precision and recall at three thresholds; Hold all three rows for comparison |
| B07 | TRAINING | 2:17.6 | 23.5s | Manim | B07_Scene | Separate train, validation and final test; Place weighting or resampling within training; Keep original class mix at evaluation |
| B08 | UNCERTAINTY | 2:41.0 | 22.1s | Manim | B08_Scene | Show eight of ten and eighty of one hundred; Change one outcome on each side; Show ten-point versus one-point recall changes |
| B09 | VERDICT | 3:03.1 | 20.4s | Remotion | ClaudeVerdictArtifact | Reveal four evaluation checks |
| B10 | YOUR TURN | 3:23.6 | 31.4s | Remotion | ClaudeComposerAsk | Type and read complete viewer prompt; Show count and data-boundary checks |
| B11 | OUTRO | 3:55.0 | 6.3s | Remotion | ClaudeTitleOutro | Restate full title with @sanjiv |

8 Manim beats (code in [`scenes.py`](scenes.py)) · 4 Remotion beats.
