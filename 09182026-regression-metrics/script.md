# Regression Metrics: MAE, MSE, RMSE, R², and MAPE, Oversimplified — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (21.1s)

Five regression metrics can score the same predictions five different ways. This is Liam, in for Sanjiv. MAE counts ordinary misses. MSE makes large misses dominate. RMSE restores the target's units. R squared compares against a mean-prediction baseline. MAPE speaks in percentages, until zero makes that language break. Let us choose the metric by the mistake we actually care about.

## B01 · EXECUTIVE SUMMARY (22.7s)

Here is the whole idea in one breath. Every metric starts with the gap between prediction and reality, but each one values that gap differently. Absolute error is steady, squared error is harsh, root mean squared error is harsh but readable in the original units, R squared asks whether you beat a simple baseline, and percentage error asks how large the miss was relative to the truth. Metric choice is a cost decision disguised as arithmetic.

## B02 · FRAMEWORK (22.9s)

Start with residuals: actual value minus predicted value. Their signs tell direction, but most regression metrics remove the sign before averaging. MAE takes absolute values. MSE squares them. RMSE takes the square root after averaging the squares. R squared compares your total squared error with the squared error from always predicting the training-set mean. MAPE divides each absolute error by the actual value before averaging.

## B03 · WORKED EXAMPLE (20.9s)

Use one tiny example: actual values two, four, six, and eight; predictions three, five, five, and eleven. The errors have magnitudes one, one, one, and three. MAE is their average: one point five. MSE averages one, one, one, and nine, giving three. RMSE is the square root of three, about one point seven three. One large miss barely shifts MAE, but it owns most of MSE.

## B04 · COMPARE (22.0s)

Now change only the error pattern. Model A misses every case by two. Model B is exact three times and misses once by eight. Both have MAE two. But A has RMSE two, while B has RMSE four, because squaring exposes the catastrophic miss. That is not proof that RMSE is better. It proves the metrics encode different preferences: consistency versus protection from rare, expensive failures.

## B05 · R² (20.7s)

R squared changes the question. Instead of asking how many units you missed by, it asks how much squared error you removed compared with predicting the mean every time. One means perfect predictions. Zero means you merely matched that baseline. Negative values are possible: your model can be worse than the mean baseline. And R squared has no target units, so pair it with an error metric people can interpret.

## B06 · MAPE FAILURE CASE (22.7s)

MAPE looks friendly because it says percent, but the denominator is the actual value. If actual is one and you miss by one, that is one hundred percent. If actual is one hundred and you miss by one, that is one percent. At actual zero, ordinary MAPE is undefined. Near zero, tiny denominators can dominate the average, so low-valued cases receive much more weight. Use it only when zero is impossible and relative error matches the domain.

## B07 · VERDICT (26.7s)

Let us recap with Claude. Use MAE when each unit of error has roughly equal cost and you want robustness to large misses. Use MSE when large errors deserve a sharply larger penalty, especially during optimization. Report RMSE when you want that sensitivity in the target's units. Use R squared to compare against the mean baseline, not to describe error size. Use MAPE only where actual values stay meaningfully away from zero. Usually, report a pair, plus the error distribution.

## B08 · HANDOFF (27.2s)

Your turn. Paste this in: given my regression predictions, actual values, target units, and the real cost of small versus large errors, calculate MAE, MSE, RMSE, R squared, and MAPE. Show which observations dominate each metric, test what happens near actual value zero, and recommend two metrics with reasons. This prompt forces the arithmetic to meet the operating context. Check whether the answer names the R squared baseline and refuses MAPE when zero makes it invalid.

## B09 · OUTRO (10.2s)

Regression metrics: M A E, M S E, R M S E, R squared, and M A P E, oversimplified. Measure the errors your decisions can afford. Liam, in for Sanjiv.
