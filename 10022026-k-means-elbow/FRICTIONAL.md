# Frictional log — Explainer: K-Means Clustering + Elbow Method

## 2026-10-04 — the first new topic built after the @sanjiv cleanup

- **Drive:** [15 K-means](https://drive.google.com/file/d/1BWyKhEJ6ffVvrmtkRAOiQy40ESrOBWa5/view) (uploaded 4 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on K-means: assign each point to
its nearest center, move each center to the mean of its points, repeat. Then plot
a computed elbow curve and test the tempting claim that one bend gives the true
number of groups. 12 beats (7 Manim, 5 Remotion bookends), native 3840×2160.
It was the first new topic after the 2–3 Oct cleanup of 15 masters, which put
@sanjiv on every video and removed the beat-sheet footers. Sanjana Rao had asked
for both of those in September.

**What I tried, and what I expected.**
- I asked for it on 4 Oct at 00:38 "remembering all the notes so far (4k,
  footer note removal, etc)". So 4K, @sanjiv, "Liam, in for Sanjiv" and no
  footer labels were part of the brief from the start, not fixes afterwards.
- I expected that carrying the earlier notes forward (4K, the handle, no
  footers) would mean no branding fixes this time, so I could focus on how
  K-means groups points and how the elbow method guides the choice of k.

**Where it resisted, and what I did next.**
- **No clustering scene existed.** The library search found nothing specific to
  clustering, so all seven teaching beats (B02–B08) were written natively in
  Manim.
- **Every number had to be computed, not typed.** The examples come from a
  deterministic NumPy Lloyd implementation (seed 42, 100 restarts), not from
  scikit-learn. The four-point example settles at centers 1.5 and 8.5 with
  inertia 1. The 18-point elbow curve runs 148.08 → 58.08 → 4.08 for K = 1–3.
- **The elbow claim needed qualifying.** The fact check notes that the *best
  achievable* inertia cannot rise with K, but individual local fits need not
  fall every time. It also treats the elbow as a heuristic. B08 uses uniform
  data with no planted groups as a computed counterexample, and B06 (feature
  scaling) and B07 (curved bands) show two more ways it fails.
- **Frame review sent three scenes back.** Fixed in source before delivery:
  - the elbow highlight spread into the axis, and the elbow demo didn't show the
    actual 18-point cloud, so both were added to B05;
  - a crowded comparison heading;
  - the summary card (B09) was missing its brand label.

  B05 and B07 were re-rendered in the fix passes and B09 was rebuilt in Remotion.
- **The run stopped after the master.** The master was compiled at 01:02. The
  captions, SRT check and delivery QC were only finished after I sent "continue"
  at 10:19. It most likely stopped
  at a usage limit.
- **The outro name could not be confirmed by ASR alone.** The opening transcribed
  as "Liam, in for Sanjiv", but the small ASR model garbled the closing name. The
  source narration and preserved audio were used to confirm it instead.

**Outcome.** 3840×2160, 24 fps, 3:37.0, 12 beats. GATE T pass (12/12), GATE V 0
blocker / 0 major on 24 frames, 434 frames at 2 fps plus 36 per-beat samples
audited with zero old-name or footer-label matches. SRT (77 cues, 0 errors) and
VTT captions included.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic choice, the brief carrying the 4K, footer and branding notes
  forward, and reviewing the cut before the 4 Oct Drive upload.
- Codex's: the beat
  sheet and narration, the computed clustering examples and their fact-check,
  the Manim scenes, the build, and the frame QC and fixes listed above.
