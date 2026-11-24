# Gradient Descent, Oversimplified — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · ASK (13.8s)

Every neural network you have ever heard of learns the same humble way: by rolling downhill. This is Sanjiv, in for Bear. No magic, no wall of calculus, just a ball, a slope, and one knob that people constantly get wrong. Let us take it apart.

## B01 · EXECUTIVE SUMMARY (16.1s)

Here is the whole idea in one breath. A model has millions of knobs. Turn them wrong and its mistakes pile up into a single number we call the loss. Gradient descent just nudges every knob in the direction that makes that number smaller — again, and again, and again. Everything after this is detail.

## B02 · FRAMEWORK — the landscape (15.2s)

Picture all those knobs as one landscape. Every point is a setting; the height is the loss — how badly the model misses. Training means one thing: find the low ground. But you can't see the whole map. It lives in a thousand dimensions, so you never get to just look and point at the bottom.

## B03 · MECHANISM — the step (worked example) (14.0s)

So you do the only thing fog allows. Feel the slope under your feet, and step downhill. Measure the slope, take a small step against it, then look again. That is the whole algorithm. The ball never knows where the bottom is — it only knows which way is down, right here.

## B04 · MECHANISM — the gradient (15.6s)

That slope has a name: the gradient. It is simply the direction the ground rises fastest — so we walk the exact opposite way. Steep slope, a big informative step; nearly flat, tiny steps. The gradient is a compass. It never tells you the destination, only the next honest direction.

## B05 · THE KNOB — learning rate (15.8s)

Now the knob everyone fights with: the learning rate — how far you step each time. Too timid, and you crawl for a thousand steps and never arrive. Too greedy, and you leap clean over the valley and bounce up the far wall — the loss explodes instead of shrinking. The craft is a step that is brave, but not reckless.

## B06 · WHERE IT BITES — local minima (16.7s)

Here is where the tidy story cracks. Downhill only ever finds the nearest bottom — not the lowest. Land in a shallow dip and you will sit there, slope zero, convinced you are done, while a deeper valley waits one ridge over. Real training fights this with momentum and randomness. Gradient descent is relentless, not wise.

## B07 · VERDICT (16.4s)

Let us recap with Claude. Loss is one number for how wrong you are. The gradient points downhill. The learning rate sets your stride. Repeat until the ground goes flat. One line to keep: gradient descent does not find the best answer — it finds the nearest one, fast. That is why the setup around it matters as much as the math.

## B08 · HANDOFF (16.7s)

Your turn. Paste this in: ask Claude to run gradient descent by hand on five points and a single weight, printing the loss and the gradient at every step. Watching one number crawl toward zero, step by step, is the moment it stops being a metaphor. Then break it on purpose — crank the learning rate, and watch it fly apart.

## B09 · OUTRO (6.4s)

Gradient descent, oversimplified. If the ball finally makes sense, subscribe. Sanjiv, in for Bear.
