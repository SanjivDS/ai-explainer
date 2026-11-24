# Linear vs. Logistic Regression, Oversimplified — Beat Sheet

**Slug:** `claude-liam-linear-logistic-regression` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:16.6

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 16.4s | Remotion | ClaudeComposerAsk | Claude composer opens; greeting 'Namaste, Liam'; the comparison prompt types in; send arms; running text reads 'choosing the output…'; answered lines… |
| B01 | EXECUTIVE SUMMARY | 0:16.4 | 18.7s | Manim | — | spark line: 'Same score. Different output.'; feature chips flow into one weighted-sum box; the path forks left to a number line and right to a sigmoi… |
| B02 | FRAMEWORK — choose by target | 0:35.1 | 21.2s | Manim | — | a target card enters a two-branch decision gate; continuous branch fills with price / demand / temperature; category branch fills with churn / fraud… |
| B03 | WORKED EXAMPLE — linear regression | 0:56.3 | 19.9s | Manim | — | house-size versus price axes and observed sales draw on; a fitted line sweeps through the cloud; residual segments drop from points to the line; a ne… |
| B04 | WORKED EXAMPLE — logistic regression | 1:16.2 | 20.6s | Manim | — | binary observations appear at zero and one; a straight line crosses outside the probability band and is rejected; the line transforms into a bounded… |
| B05 | MECHANISM — losses differ | 1:36.8 | 23.6s | Manim | — | two aligned fitting panels appear; left residual lengths square into a running loss bowl; right probability chips meet observed zero/one labels; a co… |
| B06 | FALSIFIABILITY — where the shortcut breaks | 2:00.4 | 23.4s | Manim | — | four stress-test tiles fill the frame: curve, calibration, threshold, causation; a straight fit visibly misses a curved pattern; predicted 0.8 group… |
| B07 | VERDICT | 2:23.8 | 19.8s | Manim | B07_Verdict | Claude artifact page opens with the comparison; linear line highlights: 'quantity'; logistic line highlights: 'class probability'; diagnostic line fi… |
| B08 | HANDOFF | 2:43.5 | 23.4s | Remotion | ClaudeComposerAsk | Claude composer opens with 'Your turn.'; the exact prompt types in as it is read aloud; send arms; running text reads 'paste this into Claude…'; rubr… |
| B09 | OUTRO | 3:06.9 | 9.0s | Remotion | ClaudeTitleOutro | slug-seeded crisp pixel mascot enters; poster title lands: 'Linear vs. Logistic Regression.'; locked @NikBearBrown handle holds |

7 Manim beats (code in [`scenes.py`](scenes.py)) · 3 Remotion beats.
