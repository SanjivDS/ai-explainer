# PCA — Dimensionality Reduction Explained Visually — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (20.1s)

Namaste. This is Liam, in for Sanjiv. A dataset can have hundreds of columns, yet much of its structure may lean in only a few directions. Principal component analysis, or PCA, rotates the coordinate system to find those directions, ranks them by how much variation they capture, then lets us keep only the most useful ones. Let’s make that geometry visible—and show what gets lost.

## B01 · EXECUTIVE SUMMARY (22.7s)

Here is the whole idea. PCA replaces the original features with new, mutually perpendicular axes called principal components. The first follows the direction where the centered data varies most; each next component captures the largest remaining variation while staying perpendicular to the earlier ones. Keep a few components and the data becomes smaller. The tradeoff is compression: discarded directions cannot be perfectly recovered.

## B02 · FRAMEWORK (21.2s)

The workflow has five moves. First, center every feature around zero. Second, find the longest direction through the data cloud. Third, choose the next perpendicular direction that captures the most remaining spread. Fourth, rotate every point into this new coordinate system. Fifth, keep the first k coordinates. Center, find, rotate, project, choose k. That is PCA before the matrix notation arrives.

## B03 · WORKED EXAMPLE (20.1s)

Watch one tilted cloud. In the original x and y coordinates, both numbers are needed to locate a point. Rotate the axes so PC one runs along the cloud and PC two runs across its narrow width. Now project each point onto PC one. Every dot becomes one coordinate on a line. Two dimensions have become one, while most of this cloud’s visible spread remains.

## B04 · ALGEBRA (23.6s)

The geometry has an algebraic engine. After centering the data, PCA can use eigenvectors of the covariance matrix or, commonly, singular value decomposition of the centered data matrix. The directions are the principal axes; their associated variances rank the components. Maximizing variance along the retained directions is equivalent to minimizing squared reconstruction error for this linear projection. Different route, same fitted subspace.

## B05 · PROJECTION (22.9s)

The rotation itself does not reduce dimension; it only changes coordinates. Reduction happens when we drop component columns. Keeping PC one and PC two from a ten-feature dataset gives each row two new values instead of ten. Those values are weighted combinations of the original features, not original columns selected by importance. PCA compresses directions. It does not declare two original features the winners.

## B06 · CHOOSE K (23.2s)

Each component receives an explained-variance ratio: its share of the total variance in the centered data. Stack those shares cumulatively and the curve rises toward one. Choose k where the retained information is sufficient for the downstream job—not because an elbow is automatically correct. A visualization may tolerate more loss than anomaly detection. Validate the model or task after projection; variance is not the same thing as usefulness.

## B07 · RECONSTRUCTION (23.4s)

Now reverse the projection. Lift the one-dimensional coordinates back into the original plane. The reconstructed points land on the PC-one line, not at their exact starting positions. The perpendicular gaps are the discarded information. Keeping PC two as well restores this two-dimensional toy cloud exactly, apart from numerical precision. In higher dimensions, every omitted component contributes additional squared reconstruction error.

## B08 · FALSIFIABILITY (23.1s)

PCA listens to variance, so feature units can dominate the answer. A column measured in thousands may steer PC one more than a column measured between zero and one; standardize first when the application requires equalized scales. PCA is also linear. A curved manifold can need several straight components even when one curved coordinate would describe it. And outliers can pull the axes. Inspect the data before trusting the compression.

## B09 · VERDICT (25.8s)

The verdict: PCA is a linear rotation plus projection. Center the data, find orthogonal directions ranked by variance, transform the rows, and retain only the components that survive task-based validation. It is useful for compression, visualization, denoising, and decorrelation. It is not feature selection, not automatically scale-invariant, and not guaranteed to preserve class separation or nonlinear structure. The reconstruction gaps show the price you paid.

## B10 · YOUR TURN (27.8s)

Your turn. Paste this into Claude: Given my dataset, identify numeric features, units, missing values, and outliers; propose a leakage-safe PCA pipeline; compare centered-only and standardized inputs; plot cumulative explained variance; choose candidate values of k; reconstruct the data; and evaluate the downstream task before and after PCA. Report what each component loads on, but do not treat loadings as causal effects. Check scale, reconstruction error, and task performance before accepting the compression.

## B11 · OUTRO (19.5s)

PCA: dimensionality reduction explained visually. Center the cloud. Rotate toward maximum variance. Project onto the leading components. Keep k coordinates, then measure what the discarded directions cost. PCA can reveal a compact linear structure, but the biggest variation is not always the most useful signal. This was Liam, in for Sanjiv.
