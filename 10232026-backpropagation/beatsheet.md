# Backpropagation - How Neural Networks Actually Learn — Beat Sheet

**Slug:** `backpropagation` · **Series:** Deep Dive — Deep Learning · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 4:31.3

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | The Question | 0:00.0 | 14.8s | Remotion | ClaudeComposerAsk | ClaudeComposerAsk: Hi, Sanjiv. Composer request and agenda: Predict, Trace Gradients, Update. Retain folder chip and agenda; no corner footer. |
| B01 | The Big Picture | 0:14.8 | 15.6s | Remotion | BrutalistHesitantWriter | Older-template overview: correct guesses to calculates in “Backpropagation guesses how each parameter affects loss.” Context cards: Loss, Gradients,… |
| B02 | Bring Back the Network | 0:30.5 | 15.8s | Manim | B02_Scene | Reuse two-input, two-hidden-unit network. Reveal x=(2,1), z=(1,-0.5), h=(1,0), prediction=2.5 along its route. Parameter values supplied in companion… |
| B03 | Give the Prediction a Target | 0:46.2 | 14.9s | Manim | B03_Scene | Prediction 2.5 and target 1 enter half-squared-error block. Reveal L=½(ŷ−y)²=1.125. Label one constructed training example. |
| B04 | Start at the Loss | 1:01.2 | 16.6s | Manim | B04_Scene | Plot local loss curve with point ŷ=2.5 and slope 1.5. Display ∂L/∂ŷ=ŷ−y=1.5; separate gradient from loss label. |
| B05 | The Chain Rule | 1:17.7 | 17.7s | Manim | B05_Scene | Three nodes parameter → intermediate → loss. Animate backward arrows and reveal ∂L/∂w=(∂L/∂u)(∂u/∂w). One equation at a time. |
| B06 | Gradients at the Output | 1:35.5 | 17.2s | Manim | B06_Scene | Use v=(2,-1), c=0.5 to avoid layer-index clutter. Show ŷ=v₁h₁+v₂h₂+c. Reveal gradients v₁:1.5, v₂:0, c:1.5 sequentially. |
| B07 | Pass Through ReLU | 1:52.7 | 18.2s | Manim | B07_Scene | Backward sensitivities into h: (3,-1.5). ReLU gates at z=(1,-0.5) yield dz=(3,0). Gate labels positive slope 1, negative slope 0. |
| B08 | Reach the Earlier Weights | 2:10.9 | 18.2s | Manim | B08_Scene | Focus first unit only. ∂L/∂w₁₁=3×2=6; ∂L/∂w₁₂=3×1=3; ∂L/∂b₁=3. Then muted second-unit zero gradients. |
| B09 | The Optimizer Takes a Step | 2:29.1 | 20.6s | Manim | B09_Scene | Freeze computed gradients, then reveal θnew=θ−0.05∇L. Focus w₁₁:0.5−0.05×6=0.2. Updated parameters in separate panel, no new-value reuse during backw… |
| B10 | Run Forward Again | 2:49.7 | 19.2s | Manim | B10_Scene | Recompute with updated parameters: z=(0.1,-0.5), h=(0.1,0), output=.6175. Compare loss1.125→.073153125, displayed0.0732. Label one example, one step. |
| B11 | Check the Gradient | 3:08.8 | 21.2s | Manim | B11_Scene | Show central difference [L(w+ε)−L(w−ε)]/(2ε), ε=10⁻⁶. Analytic6 and numerical≈6. Real companion output excerpt; no fabricated terminal. |
| B12 | From One Step to Learning | 3:30.1 | 20.0s | Manim | B12_Scene | Training loop around minibatch: forward → loss → backward → update. Separate held-out evaluation panel. Brief learning-rate large-step caution, no in… |
| B13 | The Verdict | 3:50.1 | 18.2s | Remotion | ClaudeVerdictArtifact | Claude verdict artifact, four concise lines: Predict; Measure loss; Trace gradients; Update parameters. |
| B14 | Your Turn | 4:08.3 | 17.8s | Remotion | ClaudeComposerAsk | ClaudeComposerAsk prompt verbatim with folder chip and task lines: Use supplied parameters; Check all gradients; Recompute loss. |
| B15 | Backpropagation - How Neural Networks Actually Learn | 4:26.1 | 4.9s | Remotion | ClaudeTitleOutro | Older title outro, centered @sanjiv and crisp mascot. Solid cream background during title fade. |

11 Manim beats (code in [`scenes.py`](scenes.py)) · 5 Remotion beats.
