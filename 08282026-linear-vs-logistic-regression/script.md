# Linear vs. Logistic Regression, Oversimplified — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (16.4s)

Linear regression and logistic regression share a skeleton, then answer different questions. One predicts an amount. The other predicts a probability. This is Liam, in for Bear. The confusing name hides a clean design choice: keep the weighted sum, then change what happens at the output. Let us make that fork visible.

## B01 · EXECUTIVE SUMMARY (18.7s)

Here is the whole idea in one breath. Both methods combine inputs using learned weights. Linear regression leaves that score as a number, useful for quantities like price or temperature. Logistic regression bends the score through an S-shaped function, turning it into a probability for a class such as yes or no. Same engine room; different dashboard.

## B02 · FRAMEWORK — choose by target (21.2s)

Start with the target, not the algorithm menu. If the answer can naturally keep moving along a number line, you have a regression target: tomorrow's demand, a house price, a temperature. If the answer is membership in a category, you have classification: churn or stay, fraud or legitimate. Logistic regression models the probability of that category, then a separate threshold can turn probability into a decision.

## B03 · WORKED EXAMPLE — linear regression (19.9s)

Take house size and price. Plot the sales, fit a line, then use that line to estimate a new home's price. The vertical gaps are residuals, and ordinary least squares chooses coefficients that minimize the sum of their squares. That is the contract: predict a quantity and pay heavily for large misses. The line can output any real number, including foolish ones outside the data range.

## B04 · WORKED EXAMPLE — logistic regression (20.6s)

Now change the target to whether a customer churns. A straight line is awkward: probabilities should not wander below zero or above one. Logistic regression keeps the weighted score, then sends it through the sigmoid. Low scores squeeze toward zero, high scores toward one, and the middle stays sensitive. The result is a probability estimate; a threshold, such as one half, creates the class label.

## B05 · MECHANISM — losses differ (23.6s)

The output change also changes the fitting objective. Linear regression usually minimizes squared residuals: distance from each observed number to the predicted number. Logistic regression fits class probabilities by maximizing likelihood, equivalently minimizing log loss. Confidently assigning low probability to what actually happened is punished hard. That is why logistic regression is not merely linear regression with answers clipped between zero and one.

## B06 · FALSIFIABILITY — where the shortcut breaks (23.4s)

Now the cleanup. A straight relationship can miss curves, interactions, and changing variance. Logistic probabilities can be badly calibrated, and a one-half threshold may be wrong when false positives and false negatives have different costs. Both models can extrapolate badly, inherit biased data, and mistake association for causation. Their simplicity is a feature only when diagnostics and held-out data say the assumptions are useful.

## B07 · VERDICT (19.8s)

The verdict. Linear regression predicts a continuous quantity by fitting a weighted sum, commonly with squared error. Logistic regression uses a weighted sum to model class probability through a logistic link, commonly with log loss. Choose by the target and the decision you need. Then test residuals, calibration, thresholds, and performance on data the model never saw.

## B08 · HANDOFF (23.4s)

Your turn. Paste this in: take one dataset with a continuous target and one with a binary target. Fit linear regression to the first and logistic regression to the second. Visualize predictions, residuals, probabilities, and a movable decision threshold. Then audit four things: target type, loss, extrapolation, and calibration. This prompt turns the names into observable behavior. Look for where each model becomes confidently wrong, not merely where it fits.

## B09 · OUTRO (9.0s)

Linear versus logistic regression, oversimplified. Do not choose from the name. Choose from the target, then interrogate the mistakes. Liam, in for Bear.
