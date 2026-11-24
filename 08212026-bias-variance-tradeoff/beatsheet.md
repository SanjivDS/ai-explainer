# Bias vs. Variance, Oversimplified — Beat Sheet

**Slug:** `claude-liam-bias-variance-tradeoff` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 2:56.6

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 16.3s | Remotion | ClaudeComposerAsk | Claude composer on cream; greeting 'Bonjour, Liam'; the ask types into the composer; terracotta send arms; running text says 'testing the fit…'; thre… |
| B01 | EXECUTIVE SUMMARY | 0:16.3 | 17.2s | Manim | — | spark line: 'Learn signal, not noise.'; training dots appear with a smooth hidden trend line; a rigid straight fit misses the curve on the left; a ja… |
| B02 | FRAMEWORK — two data draws | 0:33.5 | 19.4s | Manim | — | two equal panels appear: 'bias' and 'variance'; three sample datasets cycle beneath a fixed smooth truth; left: three rigid fits stay similarly and v… |
| B03 | WORKED EXAMPLE — high bias | 0:52.9 | 18.3s | Manim | — | curved truth line draws behind scattered observations; a straight ruler-fit sweeps across, missing both ends; sample A changes to sample B; ruler bar… |
| B04 | WORKED EXAMPLE — high variance | 1:11.2 | 18.8s | Manim | — | same observations return with a smooth hidden trend; a wavy fit threads exactly through every training dot; training badge ticks to 'perfect fit' in… |
| B05 | MECHANISM — the validation curve | 1:30.0 | 20.1s | Manim | — | horizontal axis types in: 'model flexibility'; training-error curve descends steadily in soft ink; validation curve descends, bottoms out, then rises… |
| B06 | FALSIFIABILITY — the tradeoff is not a law of nature | 1:50.1 | 19.3s | Manim | — | a balance labelled 'bias / variance' appears, then gets stamped 'diagnostic'; three levers enter: 'more data', 'regularization', 'better features'; m… |
| B07 | VERDICT | 2:09.4 | 17.9s | Remotion | ClaudeVerdictArtifact | Claude artifact page opens with a four-line verdict; bias line highlights: 'consistently misses'; variance line highlights: 'sample writes the answer… |
| B08 | HANDOFF | 2:27.4 | 19.6s | Remotion | ClaudeComposerAsk | Claude composer opens with greeting 'Your turn.'; the suggested prompt types in full; send arms terracotta; running text says 'paste this into Claude… |
| B09 | OUTRO | 2:46.9 | 9.1s | Remotion | ClaudeTitleOutro | pixel mascot enters on the cream Claude title card; poster title lands: 'Bias vs. Variance.'; @NikBearBrown handle holds beneath |

6 Manim beats (code in [`scenes.py`](scenes.py)) · 4 Remotion beats.
