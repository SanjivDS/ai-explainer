# Frictional log — Explainer: Gradient Descent, Oversimplified

## 2026-08-12 — the first explainer, built without LaTeX and corrected in the 4K pass

- **Drive:** [01 Gradient Descent](https://drive.google.com/file/d/1jo-3nv1LZTZu02BW7VScrk4BU5uQyJfw/view) (uploaded 3 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** My first `ai-explainer`, from the prompt "What is
gradient descent?": loss as the height of a landscape, the gradient as the local
slope, the learning rate as the step, and where the method stops being reliable.
10 beats (6 Manim, 4 Remotion bookends), narrated by Kokoro `am_onyx` as "Liam, in
for Sanjiv". It was built in Claude Code right after the toolkit setup on 10 Aug.

**What I tried, and what I expected.**
- I asked whether I could start without installing LaTeX/MacTeX and add it later
  only if it became necessary. The build went ahead without it: every Manim label
  is plain Pango `Text`.
- I expected to study the concept and use the toolkit to produce a clear
  explainer, then review the draft and request changes to the explanations and
  visuals.

**Where it resisted, and what I did next.**
- **Text collided with the graph.** The first layout audit (12 Aug) logged 3
  errors, the labels "you are here", "low loss" and "you can't see the bottom"
  sitting on a curve, plus one label outside the safe area. I spotted the overlap
  on playback, asked whether missing LaTeX was the cause, and asked for every label
  to be kept clear of the lines. The
  August audit on disk still shows the 3 errors; the label and margin corrections
  that are documented came in the September 4K pass.
- **I hit the Claude usage limit** on 14 Aug, right after asking for that fix
  ("when will it reset").
- **The handle changed after review.** On 7 Sep, after Sanjana Rao's feedback on
  the later videos, I asked for the same fix here (@Sanjiv, "Liam, in for
  Sanjiv"). It was recompiled that day, still at 1920×1080.
- **It wasn't 4K.** The 24 Sep audit found both full-length copies at 1920×1080
  (146.9 s); only the review slate was 3840×2160.
- **The 4K pass found factual problems in the narration.** The recap said "the
  gradient points downhill" while B04 showed it pointing toward steepest increase,
  and B06/B07 promised the method "finds the nearest" minimum. Exact rewrites for
  B00, B01, B02, B06 and B07 were proposed in `SCRIPT-CORRECTIONS.md` (also dropping
  "every neural network", "millions of knobs" and "a thousand dimensions"). I
  approved them on 27 Sep and the five beats were re-voiced in the same voice.
- **Re-voicing hit a hidden field.** B01/B02/B06 carried a beat-level
  `engine=manim`, which the audio script reads as the TTS engine and skips; it was
  set to `kokoro`. (Copied from this sheet, it had muted an L1 reel on 4 Sep.)
- **Final-frame QC caught two more defects.** The B04 "steep" label overflowed the
  left edge (moved inside the margin), and the outro had inherited an unrelated
  default subtitle, "bot vs bot, season one". The shared `ClaudeTitleOutro` now
  hardcoded @NikBearBrown and a mascot, so a project-local outro keeps @Sanjiv; the
  compiler still logs that as a skin advisory.

**Outcome.** 3840×2160, 24 fps, 2:33.5, 10 beats. GATE T pass (0 FAILs), final-frame
QC 0 blocker / 0 major, 2 Oct branding OCR check clean (307 frames + 30 samples).
Fact-check PASS on the corrected claims (Goodfellow et al., *Deep Learning* §4.3
and ch. 8). No SRT/VTT captions in `renders/`.

**What the AI tools contributed, and what I did with it.**
- Mine: the topic, studying the concept, the original August narration approval,
  spotting the label overlap on playback, directing changes, approving the five
  narration corrections before the 27 Sep export, and reviewing the video.
- Claude Code's (Aug): the beat sheet and narration, the Manim scenes and the first
  build. Codex's (Sep–Oct): the 4K rebuild, the fact review and proposed
  corrections, the re-voicing, and the frame-QC and branding fixes above.
