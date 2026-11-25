# Frictional log — Explainer: Bias vs. Variance, Oversimplified

## 2026-08-24 — the second explainer, moved to Codex after the usage limit

- **Drive:** [02 Bias Variance tradeoff](https://drive.google.com/file/d/1y1Nk4S24TQ_2nRiNhHrATZcOxkUHeyur/view) (uploaded 3 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on the bias–variance tradeoff: a
rigid line that underfits, a flexible curve that chases every point, and a
validation curve that shows where the useful middle is, closed with the caution
that this is a diagnostic, not a law every model obeys. 10 beats (6 Manim, 4
Remotion). All curves are schematic; no numbers appear on screen.

**What I tried, and what I expected.**
- I started it in Claude Code on 17 Aug ("What is Bias vs Variance tradeoff"), in
  the session that had already hit the usage limit. The run kept stopping ("Try
  again", "Continue from where you left off").
- On 23 Aug I moved to Codex, told it the gradient-descent video already existed
  and the setup was ready, but the tokens had run out on this second video.
- With Claude at its limit (18–23 Aug), I carried on in Codex and Cursor, and kept
  working with both through 30 Aug.
- I expected to build on the first video's format while making the difference
  between underfitting and overfitting easy to understand. I also needed to see
  whether production could continue in Codex and Cursor after the Claude limit.

**Where it resisted, and what I did next.**
- **The work restarted from scratch in a new tool.** Sources were consulted on
  23 Aug and the master compiled on 24 Aug. The layout audit found 0 overlaps and
  Gate V reported 0 blocker / 0 major.
- **The sign-off is thin.** `PEDAGOGY.md` reads `VERDICT: PASS` with the reviewer
  and date left blank; my "done, proceed" in Codex on 23 Aug is the only matching
  message. [CHECK: confirm that you reviewed the narration before audio.]
- **Scope was tightened in the sources.** "Bias" means prediction bias, not
  societal bias; the decomposition is scoped to squared-loss regression; validation
  is shown as the selection holdout, kept separate from a final test.
- **The handle changed after review.** On 7 Sep I asked for Sanjana Rao's fixes
  (@Sanjiv, "Liam, in for Sanjiv") on this older video too. It was recompiled that
  day at 1920×1080. [CHECK: confirm this feedback came from Sanjana Rao before keeping it.]
- **It wasn't 4K.** The 24 Sep audit found all three full-length copies beside the
  project at 1920×1080 (176.4 s). A 4K copy (176.6 s) had been exported on 21 Sep
  in the Claude Code session that followed the "not in 4K" feedback.
- **The type gate blocked the refresh twice.** A typography refresh in late
  September failed GATE T on two beats (B01 curve fragments read as small text, B02
  accent contrast), so no refreshed final was claimed and the 21 Sep master stayed.
  The 2 Oct branding pass hit the same gate: B01 had two text runs about 37 px tall,
  under the 41 px floor, and the final export was refused. B02 was re-rendered in a
  retry and the gate passed.

**Outcome.** 3840×2160, 24 fps, 2:56.6, 10 beats. GATE T pass (0 FAILs, 2 Oct),
Gate V 0 blocker / 0 major, layout audit clean. Branding check: 353 frames at 2 fps
plus 30 beat samples, no old-name or production-footer matches.

**What the AI tools contributed, and what I did with it.**
- Mine: studying the concept, moving the work to Codex and Cursor, reviewing the
  drafts and requesting changes. [CHECK: confirm the topic choice and the narration
  sign-off.]
- Codex's: the beat sheet and narration, the sources (Stanford STATS 202,
  scikit-learn's underfitting/overfitting example, *The Elements of Statistical
  Learning*) and scope notes, the Manim scenes, the build, and the 7 Sep and 2 Oct
  fixes. Claude Code's: the 21 Sep 4K export.

<!-- DRAFT. Sources: README.md; brutalist.art-main and -latest copies of
     PEDAGOGY.md, SOURCES.md, FACTCHECK.md, CHECKS-REPORT.md, layout_audit.md,
     _qc/REPORT.md (identical in both trees); TYPECHECK.md (2 Oct); beat_sheet.json
     (build.at 2026-09-07 main, 2026-10-02 latest); reports/4k-audit-2026-09-24
     (README, inventory.json, bias-variance-final.log);
     reports/branding-cleanup-2026-10-02 (bias logs, type-debug.log, final-qc
     result.json); archive/pre-sanjiv-cleanup/renders file dates; Claude Code
     messages 17 Aug and 21 Sep; Codex messages 23 Aug, 7 Sep, 2 Oct, 16 Nov.
     Replace every [CHECK] and delete this comment. -->
