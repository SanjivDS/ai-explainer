# Frictional log — Explainer: Linear vs. Logistic Regression, Oversimplified

## 2026-08-26 — built in Codex to match the first two

- **Drive:** [03 Linear and Logistic regression](https://drive.google.com/file/d/1K_sJsQZUd6gjVJgL9WTlBuo06Ypa53eZ/view) (uploaded 4 Oct)
- **Report:** [REPORT.md](REPORT.md)

**What I was working on.** An `ai-explainer` on linear vs. logistic regression:
one weighted score that becomes either an unbounded number or, through a sigmoid,
a probability, with the target type deciding which. A house-price line with
residuals, a worked point mapped to 0.73 and thresholded, squared loss vs. log loss,
and a stress test (nonlinearity, calibration, threshold costs, causal overreach).
10 beats (7 Manim, 3 Remotion).

**What I tried, and what I expected.**
- I asked Codex for "a video just like the last one we created" and approved the
  narration with "Verdict: PASS" on 26 Aug.
- The same day I asked where the code should go on GitHub, since the advice was to
  upload the generation code, not the video, and set up my own repo with one folder
  per video.
- [CHECK: what you expected, e.g. that a third video in the same template would be
  quick now that the setup worked.]

**Where it resisted, and what I did next.**
- **Two beats ran in extreme slow motion.** At assembly, B05 was stretched from a
  6.8 s clip into a 23.6 s beat (3.5×) and B06 from 7.4 s into 23.4 s (3.2×);
  `replace_log.md` flagged both for longer renders. [CHECK: whether these were
  re-rendered at full length; `replace_log.md` is unchanged in the latest tree.]
- **The Codex limit.** I hit the Codex limit during 26–30 Aug while working on this
  video, on top of the Claude limit from the week before. I submitted a renewal
  request explaining how the tool limits had affected my output.
- **Claims were hedged in the fact-check.** OLS and log loss are described as what
  fitting "commonly" uses, 0.5 is labelled an example threshold, logistic regression
  is called a classifier despite its name, and "coefficients prove causation" is
  marked WRONG and rejected on screen. `$420k` and 0.73 are labelled illustrative.
- **The handle was wrong.** Sanjana Rao's 7 Sep review found @NikBearBrown on this
  video, L1 and L2. It was recompiled that day, still at 1920×1080. The 2 Oct audit
  still found an "NBB" monogram in the closing frame, which was replaced with the
  star motif. [CHECK: confirm this feedback came from Sanjana Rao before keeping it.]
- **Resolution.** The 24 Sep audit found the 7 Sep copies at 1920×1080 (196.4 s).
  4K masters (196.6 s) had been exported on 21 Sep, the same day Sanjana told me the
  videos were still not in 4K. [CHECK: what Sanjana's screenshot showed, if you know
  which file she reviewed.]
- **The type gate blocked the branding export once** (one beat failed, 2 Oct).
  B02 was re-rendered in a retry and the gate passed.

**Outcome.** 3840×2160, 24 fps, 3:16.6, 10 beats. GATE T pass (0 FAILs, 2 Oct),
Gate V 0 blocker / 0 major, layout audit clean. Branding check: 393 frames at 2 fps
plus 30 beat samples, no old-name, NBB or production-footer matches.

**What the AI tools contributed, and what I did with it.**
- Mine: [CHECK: the topic, asking for the same format as the earlier videos, the
  narration approval, the GitHub layout, and your review of the cut.]
- Codex's: the beat sheet and narration, the sources (scikit-learn Linear Models,
  Stanford CS109 and STATS 202, *ISL*) and fact-check, the Manim scenes and build,
  and the 7 Sep and 2 Oct fixes. Claude Code's: the 21 Sep 4K export.

<!-- DRAFT. Sources: README.md; brutalist.art-main and -latest copies of
     PEDAGOGY.md (VERDICT 2026-08-26), FACTCHECK.md, SOURCES.md, PROMPTS.md,
     CHECKS-REPORT.md, replace_log.md, layout_audit.md, _qc/REPORT.md;
     TYPECHECK.md (2 Oct); beat_sheet.json (build.at 2026-09-07 main,
     2026-10-02 latest); reports/4k-audit-2026-09-24 inventory.json;
     reports/branding-cleanup-2026-10-02 (README, baseline-findings.json,
     linear logs, final-qc result.json); archive/pre-sanjiv-cleanup file dates;
     Codex messages 26 Aug, 7 Sep, 21 Sep, 2 Oct, 16 Nov; Claude Code messages
     21–22 Sep. Replace every [CHECK] and delete this comment. -->
