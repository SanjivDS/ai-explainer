# CNN vs RNN vs LSTM - When and Why to Use Each — Beat Sheet

**Slug:** `cnn-rnn-lstm` · **Series:** Deep Dive — Deep Learning · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 4:31.8

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | The Question | 0:00.0 | 13.7s | Remotion | ClaudeComposerAsk | ClaudeComposerAsk: Hi, Sanjiv. Composer request and agenda: Predict, Trace Gradients, Update. Retain folder chip and agenda; no corner footer. |
| B01 | The Big Picture | 0:13.7 | 14.3s | Remotion | BrutalistHesitantWriter | Older-template overview: correct guesses to calculates in “Backpropagation guesses how each parameter affects loss.” Context cards: Loss, Gradients,… |
| B02 | Three Ways to Handle Information | 0:28.0 | 14.8s | Manim | B02_Scene | Reveal image grid, ordered signal, and delayed cue separately, then align them. No accuracy bars. |
| B03 | CNN: Reuse a Local Detector | 0:42.9 | 15.4s | Manim | B03_Scene | Slide one highlighted 3-by-3 kernel across a small image; build feature-map cells. Show shared weights once. |
| B04 | A Tiny Convolution | 0:58.3 | 17.1s | Manim | B04_Scene | Animate a width-three window over [1,2,3,4,5], with filter [1,0,-1], producing [-2,-2,-2]. Label constructed example, stride one, no padding. |
| B05 | When a CNN Fits | 1:15.4 | 17.4s | Manim | B05_Scene | Image defects and waveform motifs, sequentially. Expand receptive-field brackets across stacked layers. |
| B06 | RNN: Carry a State Forward | 1:32.8 | 15.9s | Manim | B06_Scene | Unroll three recurrent cells; reuse one weight label. State travels above input nodes; arrows avoid labels. |
| B07 | A Tiny Recurrent Update | 1:48.7 | 17.7s | Manim | B07_Scene | Reveal h_t=tanh(x_t+0.5h_previous), h0=0. Input [1,0,0]; states approximately [.762,.363,.180]. Each state replaces the previous highlight. |
| B08 | Where a Basic RNN Struggles | 2:06.4 | 17.5s | Manim | B08_Scene | Backward gradient arrows through a long chain; illustrative factors 0.5 repeated ten times. Label illustration, not measured benchmark. |
| B09 | LSTM: Control the Memory | 2:24.0 | 17.1s | Manim | B09_Scene | Show cell-state path, then forget/input/output gates one at a time. Separate hidden-state output below. |
| B10 | One Gated Memory Update | 2:41.0 | 16.8s | Manim | B10_Scene | Show c_new=f*c_old+i*g, then 0.8*0.5+0.2*0.3=0.46. Gates labeled supplied illustrative values; output gate shown only after calculation. |
| B11 | When an LSTM Fits | 2:57.9 | 18.5s | Manim | B11_Scene | Delayed cue moves along timeline to later decision; show state and bounded-memory icon. No claim that delay alone selects winner. |
| B12 | Compare the Constraints | 3:16.3 | 18.0s | Manim | B12_Scene | Three sparse comparison rows revealed independently: locality; recurrent state; gated state. Parallel-window illustration versus step dependency. |
| B13 | Choose Through an Experiment | 3:34.3 | 17.5s | Manim | B13_Scene | Three scenario cards sequentially: image defect→CNN candidate; short stream→basic RNN baseline; delayed context→LSTM candidate. Then validation split… |
| B14 | The Verdict | 3:51.8 | 16.3s | Remotion | ClaudeVerdictArtifact | Claude verdict artifact, four concise lines: Predict; Measure loss; Trace gradients; Update parameters. |
| B15 | Your Turn | 4:08.2 | 17.0s | Remotion | ClaudeComposerAsk | ClaudeComposerAsk prompt verbatim with folder chip and task lines: Use supplied parameters; Check all gradients; Recompute loss. |
| B16 | CNN vs RNN vs LSTM | 4:25.2 | 6.2s | Remotion | ClaudeTitleOutro | Older title outro, centered @sanjiv and crisp mascot. Solid cream background during title fade. |

12 Manim beats (code in [`scenes.py`](scenes.py)) · 5 Remotion beats.
