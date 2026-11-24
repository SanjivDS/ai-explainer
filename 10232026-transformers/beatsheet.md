# Transformers - Encoder, Decoder & Self-Attention — Beat Sheet

**Slug:** `transformers` · **Series:** Deep Dive — Transformers & LLMs · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 5:09.9

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | The Question | 0:00.0 | 14.2s | Remotion | ClaudeComposerAsk | ClaudeComposerAsk: Hi, Sanjiv. Agenda below @sanjiv: Self-Attention / Encoder & Decoder / Generate a Token. |
| B01 | The Big Picture | 0:14.2 | 18.7s | Remotion | BrutalistHesitantWriter | Older hesitant writer: ‘Tokens work alone.’ Replace single word ‘alone’ with ‘in context’. Final: Tokens work in context. Context cards: Read / Conne… |
| B02 | The Architecture Map | 0:32.9 | 18.8s | Manim | B02_Scene | Source tokens → encoder stack → contextual vectors. Separate target-prefix → decoder → next-token distribution. Draw cross-attention connection only… |
| B03 | Give Tokens Position | 0:51.7 | 20.0s | Manim | B03_Scene | Three token chips ‘cats / chase / birds’ become vector columns. Position tags attach. Reverse noun positions while preserving token identities. |
| B04 | Self-Attention Connects a Sequence | 1:11.6 | 18.1s | Manim | B04_Scene | Three token vectors project into Q/K/V lanes. Select one query; draw score connections to keys, then weighted value arrows back to output. Label sche… |
| B05 | Calculate Attention Weights | 1:29.7 | 19.2s | Manim | B05_Scene | Typeset q=(1,0), keys=(1,0),(0,1),(1,1); dot products [1,0,1]; divide by sqrt(2); softmax weights [.401,.198,.401]. Reveal in stages, replacing score… |
| B06 | Mix the Values | 1:48.9 | 19.1s | Manim | B06_Scene | Weights connect to values (1,0),(0,2),(3,1). Weighted contributions accumulate to output approximately (1.604,.797). Full attention formula revealed… |
| B07 | Why Multiple Heads | 2:08.0 | 19.0s | Manim | B07_Scene | Two parallel attention heads with separate projection blocks merge by concatenation then output projection. Avoid semantic-role labels for heads. |
| B08 | Inside an Encoder Block | 2:26.9 | 21.6s | Manim | B08_Scene | Progressive stack: self-attention → Add & Norm → feed-forward → Add & Norm. Residual bypasses routed outside boxes. Label original post-norm arrangem… |
| B09 | The Decoder Cannot Peek | 2:48.5 | 17.5s | Manim | B09_Scene | Target input [START,I,see] aligned to targets [I,see,cats]. Lower-triangular attention mask revealed; future positions blocked before softmax. |
| B10 | Cross-Attention Reads the Source | 3:06.0 | 19.4s | Manim | B10_Scene | Decoder queries point to encoder keys and values in separate lanes. Compare self vs cross provenance with minimal labels. |
| B11 | Training and Generation | 3:25.4 | 17.6s | Manim | B11_Scene | Training: shifted input positions processed together under triangular mask. Replace with generation loop prefix → distribution → chosen token → exten… |
| B12 | Three Transformer Families | 3:43.0 | 21.6s | Manim | B12_Scene | Encoder-only / decoder-only / encoder-decoder schematics progressively highlighted, then held side by side for ≥2 seconds. No product/version claims. |
| B13 | Check the Mask | 4:04.5 | 18.4s | Manim | B13_Scene | Execute toy causal attention: change third value massively; compare earlier outputs unchanged under mask versus changed without mask. Label fixed Q/K… |
| B14 | The Verdict | 4:22.9 | 22.5s | Remotion | ClaudeVerdictArtifact | ClaudeVerdictArtifact: Context through attention / Position matters / Masks control access / Architecture defines information flow. |
| B15 | Your Turn | 4:45.5 | 19.0s | Remotion | ClaudeComposerAsk | ClaudeComposerAsk with exact spoken prompt, @sanjiv chip and task lines; no corner footer. |
| B16 | Transformers | 5:04.5 | 5.0s | Remotion | ClaudeTitleOutro | ClaudeTitleOutro exact title; centered @sanjiv, mascotGap100, no recurring footer. |

12 Manim beats (code in [`scenes.py`](scenes.py)) · 5 Remotion beats.
