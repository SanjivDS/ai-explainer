# Feature Scaling: Standardization vs Normalization, Oversimplified — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (19.8s)

Ahoj. This is Liam, in for Sanjiv. Imagine one feature measured in dollars and another measured as a fraction. A model that uses distance, gradients, or penalties can treat the larger numbers as more important even when they are not. Feature scaling fixes the units. But standardization and normalization do it differently, and choosing blindly can create a new problem.

## B01 · EXECUTIVE SUMMARY (22.0s)

Here is the whole idea. Scaling does not add information; it changes the coordinate system so numerical magnitude does not win by accident. Standardization expresses values in standard-deviation units around the mean. Min–max scaling maps the observed training range into a fixed interval, usually zero to one. Neither is universally better. The model, distribution, outliers, and deployment range decide.

## B02 · WHY SCALE (22.7s)

Why can units matter? In nearest neighbors, a thousand-dollar difference can overwhelm a small but meaningful ratio because distance sees the raw numbers. In gradient-based models, uneven scales can make optimization crawl along a narrow valley. With regularization, coefficient penalties also interact with feature scale. Tree splits mostly compare order and thresholds, so ordinary decision trees usually need scaling far less.

## B03 · STANDARDIZATION (21.6s)

Standardization subtracts the training mean, then divides by the training standard deviation. Take ten, twenty, and thirty. Their mean is twenty; using the population standard deviation, about eight point one six, they become roughly minus one point two two, zero, and plus one point two two. The center moves to zero and one unit now means one training-set standard deviation. The shape is not forced to become normal.

## B04 · MIN-MAX NORMALIZATION (19.3s)

Min–max scaling subtracts the training minimum and divides by the training range. The same ten, twenty, and thirty become zero, zero point five, and one. That bounded interval is useful when a model or interface expects a known range. But the endpoints are set by extremes. Add an outlier at one hundred, and the original three values compress near the bottom.

## B05 · COMPARE (22.7s)

The tradeoff is clearer side by side. Standardization has no fixed bounds and remains sensitive to outliers because the mean and standard deviation move. Min–max guarantees the chosen range for the training observations, but it is even more hostage to extreme endpoints. New values can fall below zero or above one unless you clip them. If outliers dominate, consider a robust scaler instead of pretending either default is safe.

## B06 · LEAKAGE AND NAMING (23.2s)

Two practical traps matter more than the formula. First, split before fitting the scaler. Learn the mean, deviation, minimum, or maximum from training data only, then reuse those stored values on validation, test, and production inputs. A pipeline makes that discipline easier. Second, names vary: here normalization means min–max scaling, while scikit-learn's Normalizer rescales each sample to unit norm. Always inspect the exact operation.

## B07 · VERDICT (22.5s)

The verdict: scale when the model cares about distances, gradients, variance, or comparable penalties. Standardize when centered, standard-deviation units fit the job. Use min–max scaling when a fixed training range is useful and extremes are trustworthy. Trees often do not need either. Whatever you choose, fit it inside the training pipeline, validate the whole model, and remember that scaling changes geometry—not the underlying signal.

## B08 · HANDOFF (26.6s)

Your turn. Paste this into Claude: Given my dataset, model, and train-validation split, compare no scaling, StandardScaler, MinMaxScaler, and RobustScaler inside leakage-safe pipelines. Explain which model behaviors make scaling relevant, report cross-validated performance and convergence time, inspect transformed ranges and outliers, and recommend one option with caveats. Look for a justified choice, not an automatic winner, then run the same comparison on your own data.

## B09 · TITLE RESTATE (21.3s)

Feature scaling: standardization versus normalization, oversimplified. Standardization centers values and measures deviation from the mean. Min–max normalization anchors values to the training endpoints. Both can be distorted by outliers. Some models need scaling; trees often do not. Split first, fit the scaler on training data, and reuse it everywhere else. This was Liam, in for Sanjiv.
