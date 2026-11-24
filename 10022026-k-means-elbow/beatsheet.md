# K-Means Clustering + Elbow Method — Beat Sheet

**Slug:** `claude-liam-k-means-elbow` · **Series:** Foundational (Data Science) · **Voice:** Kokoro `am_onyx`
**Master:** 3840×2160, 24 fps · 3:37.0

Generated from [`beat_sheet.json`](beat_sheet.json), the source of truth. Durations are the measured
Kokoro narration (`actual_duration_s`); start times are cumulative narration and can differ from the
master by beat padding.

| # | Act | Start | Dur | Lane | Pattern / scene | What's on screen |
|---|---|---|---|---|---|---|
| B00 | ASK | 0:00.0 | 16.3s | Remotion | ClaudeComposerAsk | Composer asks for the computed walkthrough; Answer previews assignment, centroids, elbow and failure cases |
| B01 | OVERVIEW | 0:16.3 | 12.8s | Remotion | BrutalistHesitantWriter | Writer replaces natural with compact; Corrected overview holds |
| B02 | FRAMEWORK | 0:29.1 | 16.2s | Manim | B02_Scene | Choose K and initial centers; Assign points to centers; Move centers to their means and repeat |
| B03 | EXAMPLE | 0:45.3 | 17.4s | Manim | B03_Scene | Show points 1, 2, 8, 9 and centers 1, 2; Center moves to 6.33; Point 2 switches; centers settle at 1.5 and 8.5 |
| B04 | OBJECTIVE | 1:02.8 | 19.6s | Manim | B04_Scene | Compare distances 1 and 3; Grow squares of area 1 and 9; Show four half-unit residuals and total inertia 1 |
| B05 | ELBOW | 1:22.4 | 20.9s | Manim | B05_Scene | Draw recorded inertia curve for K 1 through 6; Highlight bend at K 3; Show diminishing gains beyond the bend |
| B06 | SCALE | 1:43.4 | 21.2s | Manim | B06_Scene | Show original four observations and nearest-center memberships; Rescale one feature; Reveal changed memberships |
| B07 | FAILURE | 2:04.6 | 20.8s | Manim | B07_Scene | Show two synthetic curved bands; Reveal computed two-center split; Compare shape-based grouping with nearest-center grouping |
| B08 | DECISION | 2:25.4 | 20.9s | Manim | B08_Scene | Draw uniform-data inertia curve; Show evenly spaced points with no planted groups; Reveal silhouette, stability and usefulness checks |
| B09 | VERDICT | 2:46.2 | 20.8s | Remotion | ClaudeVerdictArtifact | Verdict artifact reveals the three key lessons |
| B10 | YOUR TURN | 3:07.0 | 23.2s | Remotion | ClaudeComposerAsk | Type and read the reproducible viewer experiment; Show checklist for interpreting the result |
| B11 | OUTRO | 3:30.2 | 6.5s | Remotion | ClaudeTitleOutro | Restate title and hold @sanjiv |

7 Manim beats (code in [`scenes.py`](scenes.py)) · 5 Remotion beats.
