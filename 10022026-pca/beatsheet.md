# PCA — Dimensionality Reduction Explained Visually — Beat Sheet

**Slug:** `claude-liam-pca` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 4:33.8

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 20.1s | Remotion | ClaudeComposerAsk | Claude composer opens on Namaste, Liam; PCA visual-explanation prompt types; tilted point cloud and rotated axes preview; CENTER, ROTATE, PROJECT, CH… |
| B01 | EXECUTIVE SUMMARY | 0:20.1 | 22.7s | Manim | — | spark line: Rotate, then compress.; many-column matrix and tilted point cloud enter; PC1 and PC2 rotate onto the cloud; trailing component columns fo… |
| B02 | FRAMEWORK | 0:42.8 | 21.2s | Manim | — | spark line: Five moves, one projection.; point cloud shifts to the origin; PC1 grows along maximum spread; orthogonal PC2 appears; coordinates rotate… |
| B03 | WORKED EXAMPLE | 1:04.0 | 20.1s | Manim | — | spark line: Two coordinates become one.; deterministic tilted point cloud appears on x-y axes; PC1 and PC2 rotate into place; perpendicular guides pr… |
| B04 | ALGEBRA | 1:24.1 | 23.6s | Manim | — | spark line: The algebra finds the axes.; centered matrix Xc appears; Xc equals U Sigma V transpose builds term by term; columns of V rotate into prin… |
| B05 | PROJECTION | 1:47.7 | 22.9s | Manim | — | spark line: Rotation is not reduction.; ten original columns rotate into ten PC columns; dimension counter remains ten; eight trailing PC columns fad… |
| B06 | CHOOSE K | 2:10.6 | 23.2s | Manim | — | spark line: Choose k for the task.; component variance bars descend; cumulative curve draws toward one; three candidate k markers appear; visualizati… |
| B07 | RECONSTRUCTION | 2:33.8 | 23.4s | Manim | — | spark line: Loss has a distance.; one-dimensional scores lift back onto PC1; original points return as ghost markers; perpendicular residual segments… |
| B08 | FALSIFIABILITY | 2:57.2 | 23.1s | Manim | — | spark line: Variance can mislead.; rescaling one feature rotates PC1; standardized comparison restores balanced axes; curved data ribbon resists one… |
| B09 | VERDICT | 3:20.3 | 25.8s | Remotion | ClaudeVerdictArtifact | Claude verdict artifact opens; CENTER, ROTATE, RETAIN, VALIDATE rubric resolves; not feature selection and not scale-invariant warnings land; reconst… |
| B10 | YOUR TURN | 3:46.1 | 27.8s | Remotion | ClaudeComposerAsk | Your turn. composer opens; the PCA audit prompt types verbatim; scale, leakage, reconstruction, and task-performance checks appear; pause-and-run inv… |
| B11 | OUTRO | 4:14.0 | 19.5s | Remotion | ClaudeTitleOutro | PCA — Dimensionality Reduction Explained Visually appears poster-style; terracotta period and @sanjiv resolve; title and handle hold without subline |

8 Manim beats (code in [`scenes.py`](scenes.py)) · 4 Remotion beats.
