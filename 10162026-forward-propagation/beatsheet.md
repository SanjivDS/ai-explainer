# Neural Networks - Forward Propagation Explained — Beat Sheet

**Slug:** `forward-propagation` · **Series:** Deep Dive — Deep Learning · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 4:04.0

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | The Question | 0:00.0 | 15.6s | Remotion | ClaudeComposerAsk | Claude composer: Hi, Sanjiv; type the request, then reveal agenda: Inputs, Hidden Layer, Prediction. |
| B01 | The Big Picture | 0:15.6 | 12.3s | Remotion | BrutalistHesitantWriter | Hesitant writer corrects “updates” to “uses” in “A forward pass updates the current weights.” Final statement remains on screen. |
| B02 | The Route Through a Network | 0:28.0 | 17.8s | Manim | B02_Scene | Draw two input nodes, two hidden nodes and one output; highlight stages in order. Park weight/bias parameters in a separate fixed panel. |
| B03 | One Unit, One Calculation | 0:45.8 | 18.4s | Manim | B03_Scene | Focus first hidden unit; show x=(2,1), weights=(0.5,-1), bias=1. Reveal products 1 and -1, sum 0, then bias gives 1. |
| B04 | The Other Hidden Unit | 1:04.1 | 18.5s | Manim | B04_Scene | Move focus to second unit; weights=(-1,1), bias=0.5. Products -2 and 1 collect into -1; bias produces -0.5. Compare preactivations 1 and -0.5. |
| B05 | Apply the Activation | 1:22.6 | 18.5s | Manim | B05_Scene | Draw ReLU curve; trace -0.5 to 0, then 1 to 1. Replace preactivation vector with hidden activation vector (1,0), keeping labels distinct. |
| B06 | From Hidden Values to Prediction | 1:41.1 | 19.2s | Manim | B06_Scene | Show output weights=(2,-1), bias=0.5; calculate 2×1-1×0+0.5=2.5. Label linear regression output, constructed example. |
| B07 | A Layer in Matrix Form | 2:00.3 | 20.0s | Manim | B07_Scene | Typeset column-vector convention z=Wx+b and a=ReLU(z); show W 2×2, x 2×1, b 2×1; highlight one row at a time then result (1,-0.5). |
| B08 | Why the Activation Matters | 2:20.3 | 20.3s | Manim | B08_Scene | Reveal affine-composition identity W2(W1x+b1)+b2=(W2W1)x+(W2b1+b2) in stages. Beside it, contrast straight mapping with a simple ReLU kink, never a t… |
| B09 | Change One Input | 2:40.6 | 18.7s | Manim | B09_Scene | Keep all parameter values locked; change x=(2,1) to (2,3). Recompute z=(-1,1.5), h=(0,1.5), output=-1. Compare original 2.5 and changed -1 for ≥2 sec… |
| B10 | Where Learning Fits | 2:59.3 | 19.9s | Manim | B10_Scene | Forward route → prediction → loss; separate backward gradient route → optimizer update. Hold parameters fixed during forward, change only at optimize… |
| B11 | The Verdict | 3:19.2 | 19.4s | Remotion | ClaudeVerdictArtifact | Claude verdict artifact reveals four concise lines: Multiply, Add bias, Activate, Repeat; no equation wall. |
| B12 | Your Turn | 3:38.6 | 20.2s | Remotion | ClaudeComposerAsk | Claude composer types prompt; @sanjiv folder chip and task lines below. Actual example parameters supplied in companion evidence/example.py. |
| B13 | Neural Networks - Forward Propagation Explained | 3:58.8 | 4.9s | Remotion | ClaudeTitleOutro | Older-template title outro with centered @sanjiv and crisp mascot; no recurring corner footer. |

9 Manim beats (code in [`scenes.py`](scenes.py)) · 5 Remotion beats.
