# L1 Regularization, Oversimplified — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (18.9s)

A model with fifty inputs is rarely a model with fifty real signals. L1 regularization does something Ridge cannot: it removes features outright. This is Liam, in for Bear. Lasso shrinks the weights, and then it sets some of them to exactly zero, making the fit and a feature-selection decision in one move. Let us see why the geometry forces that.

## B01 · EXECUTIVE SUMMARY (19.9s)

Here is the whole idea in one breath. L1 regularization adds a second bill to the fitting problem: the total absolute size of the coefficients. Paying that bill pulls every weight toward zero, and because of the shape of the penalty, some weights arrive at exactly zero. Those features drop out of the model entirely. You get a simpler model and a shortlist, from one setting.

## B02 · FRAMEWORK — the objective (19.9s)

The machinery is one objective with two jobs. Start with the prediction error on the training data. Then add lambda times the total absolute weight, every coefficient's magnitude, summed. Lambda at zero is ordinary least squares. Raise lambda and each unit of weight costs more, so the optimizer has to justify every coefficient it keeps. Same fit, now on a budget.

## B03 · MECHANISM — why exactly zero (20.1s)

Why exactly zero, and not merely small? Picture the budget as a region the solution has to stay inside. Squaring gives you a circle, smooth everywhere, so the best point almost never sits on an axis. Absolute value gives you a diamond, and a diamond has corners sitting right on the axes. The loss contours tend to meet that corner first, and at a corner one coefficient is precisely zero.

## B04 · WORKED EXAMPLE — the regularization path (16.6s)

Now sweep the penalty and watch. At a small lambda every predictor keeps a weight. Turn it up and the weakest one hits zero and leaves. Turn it further and the next one goes. This is the regularization path, and it is the honest picture of what Lasso does. Not a ranking. A sequence of removals, one threshold at a time.

## B05 · DECISION — choosing lambda (18.7s)

So which lambda? Do not eyeball it. Hold out data, sweep the penalty, and plot validation error. It falls as you cut variance, then climbs once you start deleting real signal. Take the bottom of that curve. And standardize your features first, because the penalty compares raw coefficient magnitudes, so an unscaled variable gets charged the wrong price.

## B06 · FALSIFIABILITY — where sparsity lies (20.6s)

Now the cleanup, because sparsity flatters itself. Give Lasso two correlated features and it keeps one and drops its twin, nearly arbitrarily. Resample the data and the surviving subset changes, so do not read that list as discovery. The survivors are biased too, pulled toward zero. And selected never means causal. Elastic net exists precisely because grouped predictors break this.

## B07 · VERDICT (19.6s)

The verdict. L1 regularization penalizes total absolute weight, which shrinks every coefficient and drives some of them to exactly zero. That makes it a fitting method and a feature selector at once. Choose lambda by cross-validation, standardize before you fit, and treat the selected set as one plausible subset rather than the truth. Ridge shrinks. Lasso decides.

## B08 · HANDOFF (20.0s)

Your turn. Paste this in: fit Lasso across a range of penalties on your own data, plot the regularization path, and mark where each coefficient reaches zero. Then refit on a bootstrap resample and compare which features survive. That second half is the part people skip, and it is the part that tells you whether your shortlist is a finding or an accident. Watch how much the survivor list moves.

## B09 · OUTRO (8.2s)

L1 regularization, oversimplified. Ridge makes weights small. Lasso makes choices, so audit the choices. Liam, in for Bear.
