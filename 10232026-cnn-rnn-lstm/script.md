# CNN vs RNN vs LSTM - When and Why to Use Each — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · The Question (13.7s)

Hi. This is Sanjiv. Today we shall discuss CNNs, RNNs, and LSTMs, and when and why to use each. We will follow how they handle information, work through small examples, and turn those differences into practical choices.

## B01 · The Big Picture (14.3s)

Choose a fit for the task. Local patterns, sequence order, and memory requirements shape the decision. An LSTM is a type of recurrent network. Here, when we compare it with an RNN, we mean a basic, ungated RNN.

## B02 · Three Ways to Handle Information (14.8s)

Imagine three jobs: finding a defect in an image, following a sensor stream, and remembering an earlier event when interpreting a later reading. These suggest different ways to connect a network. The data format alone does not decide which model will work best.

## B03 · CNN: Reuse a Local Detector (15.4s)

A convolutional neural network applies the same learned filter at different locations. Each application examines a local neighborhood. Sharing weights lets a useful pattern detector work across the image. Deeper layers combine local features into larger patterns.

## B04 · A Tiny Convolution (17.1s)

Take five values: one, two, three, four, five. Apply a filter with weights one, zero, and negative one. Each three-value window produces negative two. This is the cross-correlation operation commonly called convolution in neural networks. The same filter also works along a time axis.

## B05 · When a CNN Fits (17.4s)

A CNN is a useful candidate when nearby values form recurring patterns: textures in images, or short motifs in signals. Stacking layers or using dilation expands the region each output can use. A shallow filter sees only its local window, so check the required context.

## B06 · RNN: Carry a State Forward (15.9s)

A basic recurrent neural network processes a sequence step by step. Each step combines the new input with the previous hidden state. That state is a learned summary of earlier inputs. The same update rule is reused through time, and changing the order can change the result.

## B07 · A Tiny Recurrent Update (17.7s)

In a constructed one-unit example, combine the input with half the previous state, then apply tanh. Starting from zero, inputs one, zero, zero produce states about zero point seven six two, zero point three six three, and zero point one eight zero. Earlier information influences later steps.

## B08 · Where a Basic RNN Struggles (17.5s)

Training sends gradients backward through those steps. Repeated transformations can make them shrink or grow. As a simple illustration, multiplying by one half ten times gives about one thousandth. A basic RNN can be a small baseline for short dependencies, but long-range learning can be difficult.

## B09 · LSTM: Control the Memory (17.1s)

Long short-term memory networks add a cell state and learned gates. The forget gate controls retained memory, the input gate controls new content, and the output gate controls what reaches the hidden state. This structure helps gradients travel through time, but does not guarantee perfect memory.

## B10 · One Gated Memory Update (16.8s)

Suppose the old cell value is zero point five. Retain eighty percent of it and add twenty percent of a candidate value of zero point three. The new cell value is zero point four six. These supplied numbers illustrate the calculation; a trained LSTM learns its gate values.

## B11 · When an LSTM Fits (18.5s)

Consider an LSTM when useful context must persist across many steps and recurrent processing suits the application. Sensor histories and sequence labeling are examples. The gates add parameters and computation compared with a basic RNN at the same hidden width. Test whether the added capacity earns its cost.

## B12 · Compare the Constraints (18.0s)

CNN windows can be computed in parallel within a layer. Recurrent steps depend on earlier states, which limits parallelism across time. For live prediction, prevent future information from entering the model: use causal convolutions or a forward-only recurrent design. Measure latency on the actual deployment hardware.

## B13 · Choose Through an Experiment (17.5s)

For image defects, start by testing a CNN. For a short stream, a basic RNN can establish a recurrent baseline. For delayed context, test an LSTM and a temporal CNN. Compare against a simple baseline using the same task metric, suitable validation split, and deployment budget.

## B14 · The Verdict (16.3s)

These are starting points for experiments. Temporal CNNs can compete with recurrent networks on sequence tasks, and other architectures may also fit. Choose the connections that match the problem, then let held-out results, memory use, and latency determine whether that choice holds up.

## B15 · Your Turn (17.0s)

Compare a CNN, a basic RNN, and an LSTM for my dataset. Ask about input structure, required context, available labels, and latency. Propose a baseline and a validation plan. Use this prompt with a specific task. Look for a testable recommendation tied to your constraints.

## B16 · CNN vs RNN vs LSTM (6.2s)

CNN versus RNN versus LSTM. When and why to use each. This is Sanjiv.
