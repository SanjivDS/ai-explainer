# Frictional log — Explainer: Data Leakage — The ML Mistake That Gives Fake-Good Results

## 2026-10-12 — built on the revised Class Imbalance layout

- **Drive:** [20 Data Leakage](https://drive.google.com/file/d/1PCTPrwN19P6th_XSMKgxNwcklbTDwdXM/view) (uploaded 20 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on three boundaries that leakage
crosses: prediction time, groups, and preprocessing. In the middle is a measured
noise experiment where a leaky pipeline looks far better than chance. 12 beats
(8 Manim, 4 Remotion bookends), native 3840×2160.

**What I tried, and what I expected.**
- I asked for it at 19:13 on 12 Oct, in the same message where I approved the
  revised Class Imbalance cut ("better, thank you"). So it was built to that
  treatment from the start:
  - direct reveals, with no type/erase/retype;
  - 42/30/28/44 type sizes;
  - generous whitespace, @sanjiv, and no production footers.

  The authoring check notes that this preference replaced the skill's default
  hesitant-writer overview.
- I expected that reusing the approved Class Imbalance layout would avoid a
  second round of layout feedback, leaving the focus on how leakage makes
  results look better than they are.

**Where it resisted, and what I did next.**
- **No leakage scene in the library.** The search returned unrelated product
  diagrams, so the boundaries were drawn natively in Manim. Layout previews were
  checked before the full 4K render.
- **The headline numbers had to be measured, not asserted.**
  - The setup: seed 42, 300 rows, 10,000 independent Gaussian noise features,
    random labels, split 180/120, with the top 25 features chosen by
    correlation.
  - Choosing features with all the labels gave 95/120 = 79.2%. Choosing them
    from the training rows only gave 62/120 = 51.7%.
  - Both runs used the same classifier and the same split, with no seed
    search. Chance-level is the expected result, not exactly 50%.
- **The classifier name had to stay honest.** It is ridge regression on ±1
  labels with a zero threshold, not logistic regression. The narration calls it
  a simple linear classifier, and `evidence/` gives the exact method.
- **Several claims needed qualifying.**
  - Applying a fixed, train-fitted transform to held-out data is required, not
    leakage.
  - Customer overlap counts as leakage for the stated task of predicting *new*
    customers.
  - A strong held-out score alone doesn't prove leakage.
  - A label-shuffle check can't rule out every kind of leakage.
  - The support-ticket and customer diagrams are labelled as constructed
    examples.
- **GATE T failed on the first pass.** At 19:23, terracotta accent text
  (#D97757) measured 2.74:1 on cream in B02, B03, B05 and B06, against the 4.5:1
  floor. The flagged annotations and bars went to dark ink, and terracotta stayed
  only on the population dots and brand elements. The four scenes were
  re-rendered without shrinking the type, and the gate passed at 19:26.
- **The run stopped after the master.** The master was compiled at 19:28 on 12 Oct.
  The captions, SRT check and delivery QC were finished on 13 Oct after I sent
  "continue" at 10:00. It most likely stopped
  at a usage limit.
- Boopesh Mohanraj's review came after Class Imbalance.

**Outcome.** 3840×2160, 24 fps, 3:57.9, 12 beats. GATE T pass (12/12, after the
contrast fix), GATE V 0 blocker / 0 major on 24 frames. 476 frames at 2 fps plus
36 per-beat samples and 24 start/end boundary samples were audited, with zero
old-name or footer-label matches. SRT (77 cues, 0 errors) and VTT captions
included, plus STATUS.md.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic choice, the request to build on the approved Class Imbalance
  treatment, and reviewing the cut before the 20 Oct upload.
- Codex's: the beat
  sheet and narration, the noise experiment and its fact-check, the Manim
  scenes, the build, the contrast fix and the frame QC listed above.
