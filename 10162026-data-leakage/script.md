# Data Leakage — The ML Mistake That Gives Fake-Good Results — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (16.9s)

Ciao. This is Liam, in for Sanjiv. A model can earn a great test score by using information it would never have in practice. That mistake is data leakage. We will trace three ways information sneaks across a boundary, then run a noise-only experiment whose impressive score disappears when we fix the workflow.

## B01 · OVERVIEW (16.6s)

Data leakage gives a model an unfair preview. Ask three questions: was this information available when the prediction was made? Did held-out data influence training choices? And are the supposedly separate examples actually connected? A high score is only useful if the evaluation matches the real task.

## B02 · TIME (19.2s)

Imagine predicting whether a support ticket will escalate, at the moment it arrives. The opening message is available then. The resolution code is written after the ticket closes. If that later field enters the model, it can reveal the outcome. A random train-test split does not remove this shortcut. Keep only features that would genuinely be available at the prediction time.

## B03 · GROUPS (21.2s)

Now imagine predicting outcomes for new customers. A customer has several tickets. Split individual rows randomly, and that same customer can appear in both training and test data. The model may exploit familiarity instead of generalizing to new customers. Keep each customer together when that is the task. For future predictions, also respect time. The right boundary depends on what deployment will ask.

## B04 · EXPERIMENT (19.1s)

Here is our reproducible experiment. Generate three hundred rows, ten thousand random features, and independent random binary labels. There is no planted predictive signal. Reserve one hundred twenty rows for evaluation and use one hundred eighty for training. The model will use just twenty-five features. The crucial question is which rows get to influence that choice.

## B05 · LEAK (20.4s)

In the leaky workflow, select the twenty-five features most correlated with the labels across all three hundred rows. Then train a simple linear classifier using only the training rows. That last step looks correct. But the evaluation labels already helped choose the features. With so many random columns, selection can discover accidental patterns in the very answers we claim to have held out.

## B06 · RESULT (22.5s)

On those same one hundred twenty evaluation rows, the leaky workflow gets ninety-five correct: seventy-nine point two percent. Repeat feature selection using training rows only, with the same split and classifier, and it gets sixty-two correct: fifty-one point seven percent. These are measured results from one seeded synthetic run, not universal scores. Near-chance performance is the honest expectation for this noise-only task.

## B07 · REPAIR (23.1s)

The repair is to put every learned preparation step inside the training boundary. Learn imputation values, scaling statistics, and feature choices from training data. Apply those fixed choices to held-out data without fitting again. In cross-validation, repeat that process separately inside every training fold. A pipeline helps enforce this order, but it cannot recognize a future-only feature or choose the right customer split for you.

## B08 · STRESS TEST (22.9s)

A good score alone does not prove leakage. Ordinary overfitting can happen with a clean split: a model memorizes training noise and performs poorly on held-out data. Leakage instead compromises what the evaluation is allowed to know. Shuffling labels and rerunning the entire workflow can expose suspicious performance, but passing that check does not certify the dataset. Audit timestamps, duplicated entities, and every learned step too.

## B09 · VERDICT (20.7s)

Define exactly what is being predicted and when. Split according to the people, devices, or time periods that must remain unseen. Keep learned preprocessing inside training folds. Use validation data to make choices, then evaluate the fixed workflow on an untouched final test. If you repeatedly change the model after reading that final score, the test has become part of development.

## B10 · YOUR TURN (26.6s)

Try this prompt. Audit a machine learning workflow for data leakage. Define the prediction time and the unit being predicted. List when each feature becomes available. Check for overlapping entities across splits. Fit preprocessing inside each training fold. Protect a final test set. Propose one reproducible leakage check. Look for explicit timestamps, a justified split, and a clear separation between fitting and applying transformations. Run the proposed check; do not accept a reassuring checklist as proof.

## B11 · OUTRO (8.4s)

Data Leakage. The machine learning mistake that gives fake-good results. Protect the boundary before trusting the score. Liam, in for Sanjiv.
