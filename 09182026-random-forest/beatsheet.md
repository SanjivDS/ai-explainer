# Random Forest: Why Multiple Trees Beat One, Oversimplified — Beat Sheet

**Slug:** `claude-liam-random-forest` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:34.6

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 19.9s | Remotion | ClaudeComposerAsk | Claude composer opens on 'Bula, Liam'; the forest-mechanics prompt types into the composer; send arms; running text reads 'growing diverse trees…'; a… |
| B01 | EXECUTIVE SUMMARY | 0:19.9 | 20.6s | Manim | — | spark line: 'Different mistakes. Steadier average.'; one dataset produces one tall, twitching tree; small data perturbations split into several diffe… |
| B02 | FRAMEWORK | 0:40.5 | 22.3s | Manim | — | spark line: 'Perturb. Grow. Combine.'; training table fans into bootstrap row bags; each bag enters a tree with a different feature subset at its nod… |
| B03 | TREE INSTABILITY | 1:02.8 | 20.1s | Manim | — | two nearly identical training tables appear side by side; a few rows change or disappear in the second table; root winner flips from feature X to fea… |
| B04 | DIVERSITY ENGINE | 1:22.9 | 21.5s | Manim | — | one row table shuffles into three bootstrap bags with repeats and omissions; three feature decks expose different subsets at their root nodes; three… |
| B05 | WORKED EXAMPLE | 1:44.4 | 21.2s | Manim | — | five tree cards reveal class-A probabilities 0.9, 0.8, 0.2, 0.7, 0.4; the 0.2 prediction separates as the dissenting tree; all five values enter an a… |
| B06 | FALSIFIABILITY | 2:05.6 | 21.6s | Manim | — | ten look-alike trees make the same wrong prediction in lockstep; correlation gauge rises and the average stays wrong; weak-signal feature cards feed… |
| B07 | VERDICT | 2:27.2 | 22.6s | Remotion | ClaudeVerdictArtifact | verdict artifact opens as a forest receipt; perturb rows and restrict features check on; grow diverse, competent trees checks on; average predictions… |
| B08 | HANDOFF | 2:49.8 | 27.0s | Remotion | ClaudeComposerAsk | handoff composer opens with 'Your turn.'; the exact spoken comparison prompt types into the composer; tree-count, feature-subset, and leaf-size sweep… |
| B09 | TITLE RESTATE | 3:16.7 | 17.7s | Remotion | ClaudeTitleOutro | one tree multiplies into a forest behind the title; resample / randomize / average labels settle beneath; different prediction needles converge into… |

6 Manim beats (code in [`scenes.py`](scenes.py)) · 4 Remotion beats.
