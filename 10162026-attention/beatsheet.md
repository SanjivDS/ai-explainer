# Attention - Why It Changed NLP — Beat Sheet

**Slug:** `attention` · **Series:** Deep Dive — NLP · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 4:37.5

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | The Question | 0:00.0 | 18.2s | Remotion | ClaudeComposerAsk | Claude composer intro, greeting Hi, Sanjiv; prompt then three-line agenda: Context, Calculation, Consequences. |
| B01 | The Whole Idea | 0:18.2 | 16.9s | Remotion | BrutalistHesitantWriter | Older hesitant-writer overview: Attention supplies fixed context. Correct fixed to input-dependent; three cards: Score, Weight, Mix. |
| B02 | One Summary Is a Bottleneck | 0:35.1 | 19.3s | Manim | — | Simple encoder-decoder schematic: four source states collapse into one summary; decoder repeatedly reads it. Replace with accessible source-state row. |
| B03 | Context Can Change Each Step | 0:54.5 | 17.8s | Manim | — | Two successive decoder queries point to the same source states with different illustrative weights. No learned language alignment claimed. |
| B04 | Query, Key, Value | 1:12.2 | 19.2s | Manim | — | Three vector roles revealed separately; query compares with keys, resulting weights multiply values. Show learned projection paths from input represe… |
| B05 | Compute the Scores | 1:31.4 | 16.9s | Manim | — | Constructed example: q=(1,0), keys=(2,0),(0,2),(0,0), d_k=2. Dot products 2,0,0 then divide by sqrt(2). |
| B06 | Scores Become Weights | 1:48.4 | 19.0s | Manim | — | Stable softmax computation; bars labeled .673,.164,.164, with rounded-values note. Exact weights retained in evidence. |
| B07 | Mix the Values | 2:07.4 | 22.5s | Manim | — | Values=(1,0),(0,1),(1,1); weighted sum gives (.836,.327). Then q=(0,1), weights swap and output=(.327,.836). Sequential stages, no crowded combined t… |
| B08 | Self-Attention and Cross-Attention | 2:29.8 | 17.9s | Manim | — | Side-by-side provenance diagrams: same sequence supplies Q,K,V versus decoder supplies Q and encoder supplies K,V. No complete architecture on this f… |
| B09 | Why the Transformer Mattered | 2:47.8 | 24.5s | Manim | — | Recurrent chain vs direct allowed attention links; parallel training positions then separate autoregressive output steps. Historical label: Transform… |
| B10 | Structure Still Matters | 3:12.2 | 21.8s | Manim | — | Three uncluttered stages: positional information; causal triangular mask; two heads whose outputs concatenate and project. Show context-appropriate i… |
| B11 | Power Has Limits | 3:34.0 | 19.6s | Manim | — | Dense 4×4 to 8×8 score grid, counts16→64; separate attention-map inspection panel tagged not a causal explanation by itself. |
| B12 | The Verdict | 3:53.6 | 20.4s | Remotion | ClaudeVerdictArtifact | Claude artifact with four short lines: Scores compare; weights normalize; values mix; architecture enables context exchange. |
| B13 | Your Turn | 4:14.0 | 18.2s | Remotion | ClaudeComposerAsk | Claude composer prompt read aloud; folder @sanjiv retained, bottom-right footer absent. |
| B14 | Attention - Why It Changed NLP | 4:32.2 | 5.1s | Remotion | ClaudeTitleOutro | Older title restatement with mascot and centered @sanjiv. |

10 Manim beats (code in [`scenes.py`](scenes.py)) · 5 Remotion beats.
