# ROC Curve and AUC Score, Oversimplified — Beat Sheet

**Slug:** `claude-liam-roc-curve-auc-score` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:25.0

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 19.1s | Remotion | ClaudeComposerAsk | Claude composer opens on 'Ahoj, Liam'; the ROC/AUC question types into the composer; send arms; running text reads 'sweeping the threshold…'; answere… |
| B01 | EXECUTIVE SUMMARY | 0:19.1 | 22.2s | Manim | — | spark line: 'Map first. Number second.'; a threshold slider sweeps left across two score rows; caught-positive and false-alarm counters rise together… |
| B02 | FRAMEWORK — one point per threshold | 0:41.3 | 21.2s | Manim | — | spark line: 'One threshold. One point.'; threshold cuts a vertical ranked stack; TPTPR/positives builds beside FFP/negatives; the two rates become th… |
| B03 | WORKED EXAMPLE — six ranked cases | 1:02.5 | 21.4s | Manim | — | the B02 axes remain while six scored cases appear in ranked order: P P N P N N; threshold starts above the list at ROC point (0,0); first two positiv… |
| B04 | MEANING — what the area says | 1:23.9 | 21.8s | Manim | — | spark line: 'AUC judges the ranking.'; the words 'percent correct' appear and are struck through; one positive-negative pair is drawn; the higher sco… |
| B05 | DECISION — choose an operating point | 1:45.7 | 20.4s | Manim | — | spark line: 'The curve needs a policy.'; one ROC curve appears with three candidate threshold dots; disease-screen branch enlarges the high-recall re… |
| B06 | FALSIFIABILITY — a good AUC can still fail | 2:06.1 | 23.7s | Manim | — | spark line: 'Ranking is not deployment.'; an AUC badge stays fixed at 0.89; three panels split beneath it: calibration, queue capacity, subgroup; eac… |
| B07 | VERDICT | 2:29.8 | 25.4s | Remotion | ClaudeVerdictArtifact | Claude verdict artifact opens with a compact ROC curve; threshold → point → curve sequence highlights; AUC definition lands beside a shaded area; dep… |
| B08 | HANDOFF | 2:55.2 | 21.7s | Remotion | ClaudeComposerAsk | Claude composer opens with greeting 'Your turn.'; the full experiment prompt types verbatim; running line reads 'paste this into Claude…'; three rubr… |
| B09 | OUTRO | 3:16.9 | 7.8s | Remotion | ClaudeTitleOutro | poster title restates 'ROC Curve and AUC Score, Oversimplified'; slug-seeded crisp mascot scales and waves without rotation; @Sanjiv handle holds ben… |

6 Manim beats (code in [`scenes.py`](scenes.py)) · 4 Remotion beats.
