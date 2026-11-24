# Cross-Validation — Why One Train/Test Split Isn't Enough — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (18.7s)

Ciao. This is Liam, in for Sanjiv. You train a model, test it once, and get a reassuring score. Change the split, and the score changes. Which result should you trust? We will run a small example, rotate the validation data through five folds, and see what cross-validation can tell us. Then we will protect the evaluation from leakage and from the wrong kind of split.

## B01 · OVERVIEW (12.7s)

One split gives a partial picture. Cross-validation checks a learning procedure across several partitions. It helps compare choices, but it cannot guarantee future performance. An untouched final test still has a separate job.

## B02 · SPLIT (22.5s)

Here is a recorded synthetic regression experiment. Keep the dataset and cubic model type fixed, but refit on two different random partitions. Each uses eighty training records and twenty validation records. The first root mean squared error is about zero point four five six. The second is zero point five seven four. Lower is better. Neither number is fabricated; they reflect different training samples and different held-out examples.

## B03 · FOLDS (20.6s)

Instead of trusting one partition, divide the hundred development records into five equal folds. Train a fresh model on four folds and validate it on the fifth. Now move the validation role and start the model again. Repeat until each fold has served once. Every record is validated once and used for training four times. The separate forty-record test set stays closed throughout this development loop.

## B04 · SCORES (21.0s)

These are the five recorded validation errors for the cubic model. They run from about zero point five zero four to zero point five nine eight. Their mean is zero point five three four. You can now see variation that one split concealed. But these are not five independent experiments: the training sets overlap. Their spread is descriptive, not automatically a confidence interval for future performance.

## B05 · SELECT (21.4s)

Use the same folds to compare learning procedures. Here a linear model averages zero point seven seven four error; the cubic model averages zero point five three four. On this example, cross-validation selects the cubic model. Lock that choice, refit it on all hundred development records, and open the separate test set. Its error is zero point four eight eight. Do not tune again on that final score.

## B06 · LEAKAGE (21.4s)

Leakage can make the whole exercise look better than it is. Suppose a scaler learns its mean from all the development data before the folds are made. Validation values have already influenced training. Fit the scaler using only the training portion of each fold, then apply that fitted transform to its validation portion. Feature selection and imputation belong inside that same boundary. A pipeline helps enforce it.

## B07 · STRUCTURE (23.0s)

The split must match the prediction problem. For independent classification examples, stratification can preserve class proportions. If several records come from one patient, keep that patient together when testing generalization to new patients. For forecasting, train on earlier data and validate on later data. Randomly mixing past and future can answer the wrong question. Five neatly drawn folds do not make a bad validation design honest.

## B08 · LIMITS (23.2s)

Cross-validation is useful, not magic. Five folds and two candidate settings mean ten model fits before the final refit. More folds cost more and do not create new independent data. Searching many settings can also overfit the validation process. A separate untouched test, or an outer loop of nested cross-validation, evaluates the selection procedure more honestly. And no resampling trick guarantees performance after the real world changes.

## B09 · VERDICT (21.6s)

Keep the roles separate. Cross-validation compares choices on development data and exposes sensitivity to the partition. Preprocessing must learn only from each training fold. Group and time boundaries must reflect deployment. After selection, refit the chosen procedure and use the untouched test for a final check. One test can still be valuable. What fails is treating one convenient split as the whole story.

## B10 · YOUR TURN (31.7s)

Try this prompt. Build a reproducible five-fold cross-validation example. Keep a final test set untouched. Fit preprocessing inside each training fold, compare two model settings on identical folds, and report every validation score plus the mean. Explain whether the split should be stratified, grouped, or chronological. Refit the chosen procedure on all development data, then evaluate it once on the final test. Look for separate fit operations, disjoint indices, and a test set that never influences model selection. Save the data, split assignments, and seed so the result can be checked.

## B11 · OUTRO (7.7s)

Cross-Validation. Why One Train/Test Split Isn't Enough. Rotate the folds. Protect the test. Liam, in for Sanjiv.
