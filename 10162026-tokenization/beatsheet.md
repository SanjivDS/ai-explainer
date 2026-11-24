# Tokenization - How Machines Break Down Language — Beat Sheet

**Slug:** `tokenization` · **Series:** Deep Dive — NLP · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:07.6

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | The Question | 0:00.0 | 16.3s | Remotion | ClaudeComposerAsk | Older template ClaudeComposerAsk with Tokenization content and Sanjiv branding. |
| B01 | The Whole Idea | 0:16.3 | 15.8s | Remotion | BrutalistHesitantWriter | Older template BrutalistHesitantWriter with Tokenization content and Sanjiv branding. |
| B02 | Choose the Pieces | 0:32.1 | 17.1s | Manim | B02_Scene | Show “cats” once. Three successive panels: whole word [cats]; characters [c][a][t][s]; illustrative subwords [cat][s]. Never show all three panels to… |
| B03 | Learn a Merge | 0:49.3 | 17.2s | Manim | B03_Scene | Toy corpus “low × 5”, “lower × 2”. Show existing character tiles; highlight adjacent l and o. Pair-count panel replaces corpus: l+o=7, o+w=7, w+e=2,… |
| B04 | Merge Again | 1:06.5 | 17.0s | Manim | B04_Scene | Tile boundaries join: [l][o][w] → [lo][w]. Then [lo][w] → [low]. Labels are whole strings throughout; use panel swaps and boundary motion, never lett… |
| B05 | Apply the Rules | 1:23.4 | 16.3s | Manim | B05_Scene | Restore text → pieces → IDs framework. Process “lower” with learned rules into [low][e][r], then IDs from the executed toy vocabulary. Label “Toy tok… |
| B06 | IDs Are Addresses | 1:39.8 | 16.0s | Manim | B06_Scene | Three token cards above three ID boxes. Arrow to a small embedding lookup table. Numeric vectors are abstract colored cells, labeled “learned vectors… |
| B07 | Break the Toy | 1:55.8 | 18.2s | Manim | B07_Scene | Show “Lower” and a distinct unknown marker for uppercase L. Next panel: “é” → UTF-8 bytes [C3][A9], labeled hexadecimal. No simultaneous character in… |
| B08 | Test the Boundary | 2:14.0 | 16.2s | Manim | B08_Scene | One comparison at a time: “lower” versus “Lower”, then “lower” versus “ lower”. Show inspection checklist: tokenizer name, exact input, pieces and ID… |
| B09 | The Takeaway | 2:30.2 | 16.4s | Remotion | ClaudeVerdictArtifact | Older template ClaudeVerdictArtifact with Tokenization content and Sanjiv branding. |
| B10 | Your Turn | 2:46.6 | 17.2s | Remotion | ClaudeComposerAsk | Older template ClaudeComposerAsk with Tokenization content and Sanjiv branding. |
| B11 | Tokenization | 3:03.9 | 3.5s | Remotion | ClaudeTitleOutro | Older template ClaudeTitleOutro with Tokenization content and Sanjiv branding. |

7 Manim beats (code in [`scenes.py`](scenes.py)) · 5 Remotion beats.
