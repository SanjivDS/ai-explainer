# Decision Trees: How Splits Actually Work, Oversimplified — Beat Sheet

**Slug:** `claude-liam-decision-tree-splits` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:21.1

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 18.8s | Remotion | ClaudeComposerAsk | Claude composer opens on 'Merhaba, Liam'; the split-mechanics prompt types into the composer; send arms; running text reads 'testing thresholds…'; an… |
| B01 | EXECUTIVE SUMMARY | 0:18.8 | 18.8s | Manim | — | spark line: 'Score. Split. Repeat.'; one mixed node of labeled rows appears; several candidate cut lines sweep across the rows; the cleanest local di… |
| B02 | FRAMEWORK | 0:37.5 | 19.8s | Manim | — | spark line: 'Purity is the scoreboard.'; Gini = 1 − Σ p² builds term by term; a pure six-of-one-class node resolves to Gini 0; a three-and-three mixe… |
| B03 | CANDIDATES | 0:57.3 | 21.2s | Manim | — | six labeled samples sort along a number line: 1A 2A 3A 4B 5B 6B; five midpoint ticks appear between distinct adjacent values; a threshold sweeps from… |
| B04 | WORKED EXAMPLE | 1:18.6 | 18.4s | Manim | — | the parent's 3A/3B proportions calculate to Gini 0.5; threshold 2.5 cuts the sorted row into AA and ABBB; left Gini resolves to 0; right Gini resolve… |
| B05 | WINNING SPLIT | 1:37.0 | 20.4s | Manim | — | threshold 3.5 cuts AAA from BBB; both children turn pure and each Gini counter falls to 0; weighted child impurity resolves to 0; decrease rises to 0… |
| B06 | FALSIFIABILITY | 1:57.4 | 21.3s | Manim | — | a greedy badge locks onto the best immediate root split; an unsearched alternate root previews a different downstream tree; the greedy tree grows unt… |
| B07 | VERDICT | 2:18.7 | 22.6s | Remotion | ClaudeVerdictArtifact | verdict artifact opens as a five-step split receipt; enumerate and partition steps check on; score and weight steps check on; choose and recurse lock… |
| B08 | HANDOFF | 2:41.3 | 23.7s | Remotion | ClaudeComposerAsk | handoff composer opens with 'Your turn.'; the exact spoken prompt types into the composer; a threshold ledger and two-level tree preview appear; rubr… |
| B09 | TITLE RESTATE | 3:05.0 | 15.9s | Remotion | ClaudeTitleOutro | title assembles around one root node and two branches; test / score / choose / repeat labels settle along the branches; the winning threshold 3.5 lan… |

6 Manim beats (code in [`scenes.py`](scenes.py)) · 4 Remotion beats.
