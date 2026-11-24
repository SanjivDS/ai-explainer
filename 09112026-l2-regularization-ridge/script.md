# L2 Regularization, Oversimplified — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (17.0s)

A regression model can fit the training data beautifully by leaning far too hard on its coefficients. L2 regularization puts a price on that swagger. This is Liam, in for Sanjiv. Ridge regression trades a little training fit for a model that is usually steadier on new data. Let us watch the trade happen.

## B01 · EXECUTIVE SUMMARY (19.1s)

Here is the whole idea in one breath. Ordinary least squares only asks how closely predictions match the training targets. Ridge adds a second bill for large coefficient values. Turning up lambda makes that bill matter more, shrinking the coefficients and often reducing sensitivity to noisy or overlapping predictors, at the cost of some bias.

## B02 · FRAMEWORK — the objective (21.1s)

The machinery is one equation. Start with residual sum of squares: the prediction mistakes. Then add lambda times the sum of every slope coefficient squared. Lambda equals zero gives ordinary least squares. A larger lambda makes big weights increasingly expensive. The optimizer still fits the data; it just has to justify every large coefficient against a quadratic cover charge.

## B03 · MECHANISM — why squaring shrinks (21.8s)

Why does the square matter? Double a coefficient and its penalty becomes four times larger. So Ridge dislikes one predictor carrying an enormous weight when several smaller weights can explain nearly the same pattern. The circular L2 budget squeezes the solution inward smoothly. It usually makes coefficients small, not exactly zero. That last distinction separates Ridge from feature-selection methods like Lasso.

## B04 · WORKED EXAMPLE — correlated predictors (21.1s)

Now the useful case. Suppose two predictors carry almost the same signal. Ordinary least squares can give one a huge positive coefficient and the other a huge negative one, while their combined prediction still looks reasonable. Change the sample slightly and those roles may flip. Ridge shrinks both, sharing the work more calmly. The prediction may barely move, but the fitted coefficients stop performing acrobatics.

## B05 · DECISION — choose lambda (20.8s)

Lambda is not a bravery setting. Too little regularization leaves the model unstable. Too much crushes useful signal and underfits. Fit a sequence of lambda values inside cross-validation, measure performance on folds the model did not train on, and choose near the validation minimum. Then evaluate once on untouched test data. Training loss alone will always lobby for less restraint.

## B06 · FALSIFIABILITY — where the shortcut breaks (21.5s)

Now the edge cases. Ridge depends on scale: without standardizing predictors, the same numerical penalty treats differently measured features unevenly. The intercept is usually left unpenalized. And if you need coefficients to become exactly zero for sparse feature selection, L2 is the wrong geometry; use an L1 method such as Lasso. Ridge is stabilization, not automatic simplification.

## B07 · VERDICT (22.6s)

The verdict. L2 regularization does not forbid complexity; it charges rent for coefficient magnitude. That small deliberate bias can buy a large reduction in variance, especially when predictors overlap or data is limited. Standardize the features, tune lambda with cross-validation, and judge the final model on untouched data. Ridge earns its keep when steadier predictions matter more than dramatic coefficients.

## B08 · YOUR TURN (21.0s)

Your turn. Paste this in: build a tiny Ridge regression demo with two strongly correlated predictors. Add a lambda slider, plot both coefficient paths, and show cross-validation error. Let me resample the training rows. Then check three things: whether the coefficients become steadier, whether validation error has a useful minimum, and whether excessive lambda visibly underfits. That is the penalty earning its name.

## B09 · OUTRO (6.5s)

L2 regularization, oversimplified. Fit the signal, charge the swagger. Liam, in for Sanjiv.
