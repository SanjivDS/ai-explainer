# Frictional log — Explainer: Class Imbalance — Why Accuracy Can Be Misleading

## 2026-10-12 — built, then rebuilt the same day after my layout feedback

- **Drive:** [19 Class Imbalance](https://drive.google.com/file/d/1g1HXzkdhFJaQWYIdChWK52f3ai-48P9B/view) (uploaded 16 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on why 99% accuracy can mean a
model finds none of the rare cases. It uses 990 normal records and 10 faults, a
confusion table, recall and precision, balanced accuracy, moving the threshold,
where resampling is allowed to happen, and how much one miss moves the recall on a small
sample. 12 beats, native 3840×2160.

**What I tried, and what I expected.**
- On 12 Oct at 00:32 I asked for three things explicitly: render in 4K; make the
  heading, subheading and body text different sizes so that no
  words/figures/lines overlap; and add a STATUS.md file.
- [CHECK: what you expected, e.g. that separate type sizes alone would make the
  frames feel uncluttered.]

**Where it resisted, and what I did next.**
- **The first pass met the brief but not my taste.** It used a heading 54 /
  subtitle 36 / body 30 / key-value 52 type scale in separate layout bands, and
  the layouts were previewed before the 4K render. The first master was compiled
  at 12:33, after I sent "continue" at 12:30. [CHECK: why the run had stopped
  after ~00:48.] At 12:40 I wrote back that the older videos were better.
  - I didn't like the type-backspace-retype overview.
  - Even with different sizes, a few frames looked cluttered. The headings,
    subheadings and text could be smaller and still legible.
- **At 19:00 I asked for a re-render with those changes.** The first master was
  archived (`archive/class-imbalance-before-layout-revision`).
  - The hesitant-writer overview (B01) was removed entirely and replaced with
    a direct reveal of three questions, now drawn in Manim. That leaves 8 Manim
    and 4 Remotion beats.
  - Typing was turned off in both composer scenes (B00 and B10).
  - Type went from 54/36/30/52 to 42/30/28/44 Manim points.
  - Headings were shortened, a redundant training caption was dropped, and
    number morphs became brief fades.
  - Narration and evidence were kept, so the runtime stayed at 241.5 s. B00–B08
    and B10 were re-rendered. At 19:13 I replied "better, thank you."
- **The numbers needed care.**
  - The always-normal baseline scores 99% accuracy, 0% recall and 50%
    balanced accuracy. Its precision is undefined (no alerts), so no value is
    shown.
  - At threshold 0.5 the counts are TP 8, FN 2, FP 20, TN 970, giving recall
    80% and precision 28.6%. At 0.8 recall and precision are both 50%. At 0.2
    recall is 90% and precision 9.1%.
  - Precision isn't monotonic in general, so the narration says it falls
    "here".
  - Turning one hit into a miss moves recall 10 points at 8/10 but 1 point at
    80/100. This is labelled as a sensitivity illustration, not a confidence
    interval.
- [CHECK: if Boopesh Mohanraj's review (around 19–23 Oct) covered this video, add
  what he asked for. No written record of it was found on disk.]

**Outcome.** 3840×2160, 24 fps, 4:01.5, 12 beats. GATE T pass (12/12), GATE V 0
blocker / 0 major on 24 frames, all eight native scenes pass the collision and
safe-margin checks, and 483 frames at 2 fps plus 36 per-beat samples were audited with
zero old-name or footer-label matches. SRT (80 cues, 0 errors) and VTT captions
included, plus STATUS.md.

**What the AI tools contributed, and what I did with it.**
- Mine: the three-point brief, the layout feedback that drove the rebuild, and
  approving the revised cut. [CHECK: the topic choice and its place in the
  series, and anything you changed between the 12 Oct master and the 16 Oct
  upload.]
- Codex's: the beat
  sheet and narration, the constructed 1,000-record example and its fact-check,
  the Manim scenes and layout checks, both builds, and the revision listed above.

<!-- DRAFT. Sources: BUILD-LOG.md, BUILD-PROMPT.md, CHECKS-REPORT.md,
     FACTCHECK.md, PROMPTS.md, SOURCES.md, SRTCHECK.md, STATUS.md, TYPECHECK.md,
     _qc/DELIVERY-QC.md, _qc/REVIEW-FIXES.md, _qc/layout/*.json, final-build.log,
     archive/class-imbalance-before-layout-revision (STATUS.md, master 12:33),
     beat_sheet.json (build.at 2026-10-12T19:09), the 12 Oct Codex messages
     (00:32, 12:30, 12:40, 19:00, 19:13), and the repo README.
     Replace every [CHECK] and delete this comment. -->
