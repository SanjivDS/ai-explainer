# Frictional log — Explainer: Word Embeddings - Word2Vec, GloVe & Semantic Similarity

## 2026-10-16 — structured math without a math renderer in the venv

- **Drive:** [22 NLP-2 WordEmbeddings](https://drive.google.com/file/d/1-1OwFdY2SjeuR-celejEz5cXTD9uOZHL/view) (uploaded 29 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** The second NLP video in the Deep Dive set: how words
become vectors, how Word2Vec (CBOW, skip-gram) and GloVe learn them, how cosine
similarity is calculated, and where "similar" misleads. Native 3840×2160 on the
older Confusion Matrix template, with the Sanjiv persona.

**What I tried, and what I expected.**
- This was the first video built from the saved series preferences that came out
  of Tokenization: Sanjiv persona, no bottom-right footer, intro and handoff folder
  chips and the closing handle kept, every text/line/figure overlap checked. I
  requested it late on 15 Oct and approved the plan five minutes later.
- I expected that with the series preferences saved, this video would need no
  template corrections, leaving the focus on how words become vectors that
  capture meaning.

**Where it resisted, and what I did next.**
- **The equations needed a renderer the venv didn't have.** The cosine and GloVe
  formulas are typeset as structured math (Matplotlib mathtext → SVG), but the
  `brutalist.art-main` venv had no Matplotlib. It was installed into a temporary
  folder (`/private/tmp/embeddings-math-deps`) and added to the path. Matplotlib
  also couldn't write its config or font cache in my home folder, and the first
  attempt failed with a traceback. One expression, `\frac45`, was rewritten as `\frac{4}{5}`. The
  seven equation SVGs are now bundled in `math/`, so a rebuild only needs Manim.
- **The model names needed pronunciation fixes.** An episode-local wrapper normalizes how
  Word2Vec and GloVe are spoken. The written script and captions keep the
  canonical names.
- **GATE T failed first and passed after three repairs:** matrix size, accent
  contrast and an intro label. In the final frame review the GloVe matrix text was
  enlarged, its equation moved off the table, the background boxes behind the
  equation SVGs removed, and selected diagram accents darkened.
- **No trained outputs were faked.** The toy corpus and vectors are constructed
  and labeled on screen, and every number is executed in `evidence/example.py`.
  Cat and dog each get eats=1 and likes=1 (radius-one windows, no cross-sentence
  pairs). A=(1,2) and C=(2,1) give 4/5 = 0.8, and D=(−2,1) is perpendicular to A.
  The zero-vector cosine is undefined and the code rejects it. All cosines use the
  original vectors, because a 2-D projection need not preserve them.
- **Qualifications, not slogans.** Close vectors need not be synonyms
  (hot/cold, with no invented score). Negative sampling is one training option, not
  the definition of Word2Vec. Corpus stereotypes are not claimed to be fixed by one
  intervention.
- **Audio check limits.** Checked by ASR and peak levels, with no clipping.
  Direct listening wasn't available, and ASR is unreliable on names and single
  vector letters.

**Outcome.** 3840×2160, 24 fps, 3:57.3 (the plan estimated about 4–5 minutes), 14
beats. GATE T pass, GATE V 0 blocker / 0 major, 475 half-second timeline samples
across 24 contact sheets plus 70 beat samples reviewed, full decode passed. 86
caption cues and chapters.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic and title, the Word2Vec-vs-GloVe framing, the series
  preferences carried over from Tokenization, the plan approval, and reviewing
  the cut.
- Codex's: the script and storyboard, the constructed corpus and its executed
  evidence, the fact-check against the Mikolov, Pennington, Nguyen, Peters and
  Bolukbasi papers, the Manim scenes, the math workaround, and the QC and fixes
  above.
