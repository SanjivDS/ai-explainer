# Entropy vs Gini Impurity — Beat Sheet

**Slug:** `claude-liam-entropy-vs-gini` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:41.7

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 16.5s | Remotion | ClaudeComposerAsk | Type the comparison request; Preview node scores, weighted splits and disagreement |
| B01 | OVERVIEW | 0:16.5 | 11.4s | Remotion | BrutalistHesitantWriter | Replace identical with different in the overview; Hold the corrected claim |
| B02 | FRAMEWORK | 0:27.9 | 19.5s | Manim | B02_Scene | Reveal four A dots and one B dot; Transform into pure and balanced nodes |
| B03 | GINI | 0:47.4 | 22.3s | Manim | B03_Scene | Build a five-by-five grid of ordered label pairs; Highlight the eight disagreements; Reveal structured formula and computed 0.32 |
| B04 | ENTROPY | 1:09.7 | 22.9s | Manim | B04_Scene | Reveal probability bars and surprisal values; Weight each surprise; reveal structured entropy formula; Show computed 0.722 bits |
| B05 | CURVES | 1:32.6 | 19.5s | Manim | B05_Scene | Trace entropy and doubled-Gini curves; Move a probability marker through pure, skewed and balanced states; Label normalization and maxima |
| B06 | WEIGHTS | 1:52.1 | 18.8s | Manim | B06_Scene | Partition ten label dots into four and six; Reveal child weights and impurities; Combine into weighted score and parent reduction |
| B07 | DISAGREEMENT | 2:10.9 | 21.6s | Manim | B07_Scene | Reveal both candidate partitions of the same parent; Compute the two weighted Gini scores and winner; Reveal entropy scores and the reversed winner |
| B08 | LIMITS | 2:32.5 | 22.1s | Manim | B08_Scene | Show a pure training leaf; Send mixed held-out labels into it; Reveal validation and tree-size controls |
| B09 | VERDICT | 2:54.6 | 19.2s | Remotion | ClaudeVerdictArtifact | Reveal the summary artifact |
| B10 | YOUR TURN | 3:13.8 | 21.8s | Remotion | ClaudeComposerAsk | Type and read the reproducible comparison task; Reveal arithmetic-checking guidance |
| B11 | OUTRO | 3:35.6 | 5.9s | Remotion | ClaudeTitleOutro | Hold title and @sanjiv |

7 Manim beats (code in [`scenes.py`](scenes.py)) · 5 Remotion beats.
