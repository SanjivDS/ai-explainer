# Bias vs. Variance, Oversimplified — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (16.3s)

A model can fail in two opposite ways: be too simple to see the pattern, or so eager to see one that it memorizes the noise. This is Liam, in for Bear. The bias versus variance tradeoff is how you catch both mistakes before they walk into production wearing a confident score. Let us make it visible.

## B01 · EXECUTIVE SUMMARY (17.2s)

Here is the whole idea in one breath. We train on a small, messy sample, but we care about the next case we have not seen. A rigid model misses real structure. A twitchy one mistakes accidents for structure. The tradeoff is choosing enough flexibility to learn the signal, without letting the sample boss the model around.

## B02 · FRAMEWORK — two data draws (19.4s)

Bias is the model's built-in stubbornness: across many possible training sets, its average answer leans away from the real pattern. Variance is its jumpiness: swap in another reasonable sample, and its answer changes too much. Notice the difference. Bias is wrong in a repeatable direction. Variance is unstable because the data got a vote it should not have had.

## B03 · WORKED EXAMPLE — high bias (18.3s)

First failure: high bias. Imagine the real relationship bends, but you insist on fitting a ruler through it. The ruler is admirably stable. Give it a different sample and it still draws almost the same line. That is not reliability. It is a bad assumption surviving every meeting. The model underfits because it lacks the shape the job requires.

## B04 · WORKED EXAMPLE — high variance (18.8s)

Now turn the flexibility dial all the way up. The model draws a little flourish through every training point. Training error looks heroic. Then one harmless sample swap makes the whole curve lurch. That is high variance: perfect recall of yesterday's accidents, fragile guesses about tomorrow. It is overfitting, and the training score is the accomplice, not the alibi.

## B05 · MECHANISM — the validation curve (20.1s)

So how do you find the useful middle without trusting your vibes? Hold out data the model never trained on. As complexity rises, training error usually keeps falling; it has more ways to please the past. Validation error tells the part you actually care about. It falls while the model learns signal, then rises when the model starts learning noise. Choose near that valley, not at the training trophy.

## B06 · FALSIFIABILITY — the tradeoff is not a law of nature (19.3s)

One important cleanup: this is a diagnostic, not a cosmic law that every model obeys neatly. More data can steady a high-variance model. Regularization can make an over-flexible model less jumpy. Better features can let a simple model see what it missed. The tradeoff names the pressure. It does not excuse you from measuring the system you actually built.

## B07 · VERDICT (17.9s)

The verdict. Bias means your model is consistently missing the pattern. Variance means it lets the particular sample write the answer. The target is not the most complicated model, or the lowest training error. It is the model that stays useful on data it has never met. That is generalization: the only score the future agrees to pay.

## B08 · HANDOFF (19.6s)

Your turn. Paste this in: build me a tiny regression demo with one noisy dataset, then fit a straight line, a medium curve, and a very flexible curve. Show train and validation error, and let me resample the points. That prompt makes the tradeoff move instead of sit in a textbook. Watch which model changes its mind when the data changes. Then ask what intervention you would try first.

## B09 · OUTRO (9.1s)

Bias versus variance, oversimplified. Do not reward a model for remembering the room. Reward it for recognizing the next room. Liam, in for Bear.
