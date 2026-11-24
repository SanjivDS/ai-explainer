# K-Means Clustering + Elbow Method — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (16.3s)

Hola. This is Liam, in for Sanjiv. Give a machine a cloud of points and ask it to find groups. What makes two points belong together? We will animate K means, move its centers by hand, and plot a real, computed elbow curve. Then we will test the tempting claim that one bend tells you the true number of groups.

## B01 · OVERVIEW (12.8s)

K means builds compact groups around moving centers. The elbow method helps compare how many centers to use, but it does not certify natural categories. Your definition of distance still decides what similarity means.

## B02 · FRAMEWORK (16.2s)

Here is the whole loop. Choose K, the number of centers. Start those centers somewhere. Assign every point to its nearest center, then move each center to the average of its assigned points. Repeat. Points can change teams when the centers move. K is your input; the algorithm does not discover that number for you.

## B03 · EXAMPLE (17.4s)

Take four points: one, two, eight, and nine. Choose two centers, initially at one and two. The first center gets point one. The other gets two, eight, and nine, so its average moves to about six point three three. Reassign, and point two changes teams. The centers settle at one point five and eight point five. Assign, average, repeat.

## B04 · OBJECTIVE (19.6s)

What is the loop trying to reduce? Inertia: add up each point's squared distance to its assigned center. A distance of one contributes one. A distance of three contributes nine. Large misses count much more. In our four-point example, every point finishes half a unit from its center, and the four squared distances sum to one. Lower inertia means a tighter fit to these data.

## B05 · ELBOW (20.9s)

Now change K. These eighteen synthetic points form three separated clouds. With one center, the recorded inertia is about one hundred forty-eight. With two, fifty-eight. With three, roughly four. After that, each extra center buys a much smaller improvement. That bend near three is the elbow: a useful tradeoff between a tighter fit and another cluster. These are computed results, not a universal threshold.

## B06 · SCALE (21.2s)

Distance is a design choice disguised as arithmetic. Watch the same four observations under two feature weightings. With one feature spanning ten units and the other only one, the split follows the larger scale. Rescale that feature and the split changes. Standardization can help when units would otherwise dominate, but it is not automatic truth. Choose features and scales that represent meaningful similarity.

## B07 · FAILURE (20.8s)

Here is a failure the elbow cannot repair. These two curved bands look like separate groups. K means with two centers cuts across them, because nearest-center regions are separated by a straight boundary in this plane. It prefers compact groups, not arbitrary shapes. Different starts can also reach different local solutions. Use careful initialization and repeated runs, then inspect what the clusters actually contain.

## B08 · DECISION (20.9s)

And sometimes there is no convincing elbow. These points are evenly spaced along a line, with no planted groups. Their inertia still falls as we add centers. The best possible inertia cannot increase when K grows; that alone proves nothing about categories. Compare nearby choices, inspect silhouette scores and stability, and ask whether the grouping helps your task. If the evidence is ambiguous, say so.

## B09 · VERDICT (20.8s)

Keep three ideas. K means alternates nearest-center assignment and averaging. Its score rewards compactness under your chosen distance. The elbow is a candidate-selection heuristic, not a truth detector. A sensible number of groups survives checks on scaling, initialization, shape, and usefulness. The question is not only whether the score got smaller. It is whether the groups earned an interpretation.

## B10 · YOUR TURN (23.2s)

Try this prompt. On a small synthetic dataset, run K means for K from one to six with repeated initializations. Plot inertia, compare silhouette scores for K above one, and show cluster assignments. Then rescale one feature and repeat. Explain whether the same K remains defensible. Look for changed memberships, unstable results, and an honest explanation when no clear elbow exists. Save the data and seed so you can reproduce the comparison.

## B11 · OUTRO (6.5s)

K-Means Clustering plus Elbow Method. Build the groups, then question the bend. Liam, in for Sanjiv.
