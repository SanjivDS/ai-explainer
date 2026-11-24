# Accuracy vs Precision vs Recall vs F1 Score, Oversimplified — Beat Sheet

**Slug:** `claude-liam-precision-recall-f1` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:34.4

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 20.3s | Remotion | ClaudeComposerAsk | Claude composer opens on 'Sawubona, Liam'; the four-metric comparison prompt types into the composer; send arms; running text reads 'counting false a… |
| B01 | EXECUTIVE SUMMARY | 0:20.3 | 20.8s | Manim | — | spark line: 'Same predictions. Different questions.'; a confusion matrix assembles and all four cells feed an accuracy lens; predicted-positive colum… |
| B02 | FRAMEWORK | 0:41.1 | 22.5s | Manim | — | two-by-two confusion matrix draws from actual and predicted axes; TP, FP, FN, and TN cells receive plain-language labels; accuracy highlights TP plus… |
| B03 | WORKED EXAMPLE | 1:03.6 | 21.5s | Manim | — | one hundred cases collapse into confusion-matrix counts; cells settle at TP 6, FP 2, FN 4, and TN 88; accuracy computes (6+88)/100 = 0.94; precision… |
| B04 | THRESHOLD TRADEOFF | 1:25.1 | 21.6s | Manim | — | ranked prediction scores appear beneath a movable threshold; threshold slides lower and more predictions enter the positive set; recall steps upward… |
| B05 | ACCURACY TRAP | 1:46.7 | 20.6s | Manim | — | accuracy 94% expands into a dominant headline; the 88 true negatives visibly supply most correct decisions; four missed positives enlarge beside reca… |
| B06 | FALSIFIABILITY | 2:07.2 | 22.6s | Manim | — | two confusion matrices share TP, FP, and FN but have different TN counts; both produce the same F1 while the TN cells visibly diverge; an equal-weigh… |
| B07 | VERDICT | 2:29.9 | 20.6s | Remotion | ClaudeVerdictArtifact | verdict artifact opens with four metric decisions; accuracy receives 'balanced classes and costs'; precision receives 'false alarms expensive'; recal… |
| B08 | HANDOFF | 2:50.5 | 23.4s | Remotion | ClaudeComposerAsk | handoff artifact opens with four required inputs; true labels, scores, positive class, and error costs check on; the exact spoken prompt types into t… |
| B09 | TITLE RESTATE | 3:13.9 | 20.3s | Remotion | ClaudeTitleOutro | title words enter one at a time: ACCURACY / PRECISION / RECALL / F1; trust / coverage / balance labels settle beneath; cost and threshold rails conve… |

6 Manim beats (code in [`scenes.py`](scenes.py)) · 4 Remotion beats.
