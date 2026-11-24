# Word Embeddings - Word2Vec, GloVe & Semantic Similarity — Beat Sheet

**Slug:** `word-embeddings` · **Series:** Deep Dive — NLP · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:57.3

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | The Question | 0:00.0 | 16.3s | Remotion | ClaudeComposerAsk | Claude intro types the episode prompt; agenda: Context, Learning, Similarity. |
| B01 | The Whole Idea | 0:16.3 | 18.4s | Remotion | BrutalistHesitantWriter | Older-template writer changes “store definitions” to “encode usage patterns”; three cards: Context, Vectors, Similarity. |
| B02 | An ID Is Not an Embedding | 0:34.7 | 15.4s | Manim | B02_Scene | A categorical lookup selects one row of a matrix. Label example coordinates as illustrative; no meaningful numeric ID distances. |
| B03 | Context Supplies the Signal | 0:50.1 | 16.4s | Manim | B03_Scene | Highlight exact executed corpus windows; accumulate cat and dog rows side by side. Disclosure: toy corpus; radius one. |
| B04 | Word2Vec: Two Prediction Tasks | 1:06.5 | 17.2s | Manim | B04_Scene | Use the sentence “the cat eats food”; separate CBOW and skip-gram arrow diagrams. Context → target, then target → context. Sequential transitions, no… |
| B05 | Learning From Prediction | 1:23.7 | 19.5s | Manim | B05_Scene | Positive pair cat/eats beside sampled contrast cat/road; show parameter update schematically, without invented loss values. Label: schematic training… |
| B06 | GloVe: Count Before Fitting | 1:43.2 | 18.8s | Manim | B06_Scene | Build the exact toy co-occurrence matrix; highlight nonzero cells. Reveal structured equation: word–context dot product + biases approximates log cou… |
| B07 | Different Routes, Related Evidence | 2:02.0 | 20.3s | Manim | B07_Scene | Side-by-side pipelines from one corpus: prediction examples → Word2Vec; count matrix → GloVe. Both end at learned vector tables; no fabricated perfor… |
| B08 | Cosine Compares Directions | 2:22.3 | 16.9s | Manim | B08_Scene | Plot A=(1,2), B=(2,4) on fixed axes; structured fraction, calculated cosine=1. Explicit constructed-vector label. |
| B09 | Compute, Do Not Guess | 2:39.2 | 16.9s | Manim | B09_Scene | Exact evidence: A·C=4, norms=√5, cosine=0.8. Then D=(-2,1) gives zero. Stage equation and arrows separately; avoid label collisions. |
| B10 | Similarity Has Limits | 2:56.1 | 18.5s | Manim | B10_Scene | Show hot/cold as a qualitative context illustration, without an invented score. Then two bank sentences point to one static vector; clearly distingui… |
| B11 | The Verdict | 3:14.6 | 19.7s | Remotion | ClaudeVerdictArtifact | Claude verdict artifact: Name the model; Compute in original space; Inspect neighbors; Test the task. No recurring footer. |
| B12 | Your Turn | 3:34.3 | 18.1s | Remotion | ClaudeComposerAsk | Claude composer types the exact prompt; output checklist includes model named, code executed, missing words handled. Folder @sanjiv retained. |
| B13 | Word Embeddings | 3:52.4 | 4.7s | Remotion | ClaudeTitleOutro | Older-template title card and mascot, @sanjiv handle; no Liam. |

9 Manim beats (code in [`scenes.py`](scenes.py)) · 5 Remotion beats.
