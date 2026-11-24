# Attention - Why It Changed NLP — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · The Question (18.2s)

Hi. This is Sanjiv. Today we shall discuss attention, and why it changed natural language processing. Embeddings give us vectors. Attention lets those vectors draw information from other positions. Let us follow that exchange, calculate a tiny example, and see what changed when the Transformer put attention at its center.

## B01 · The Whole Idea (16.9s)

Attention builds input-dependent context. It scores possible sources of information, turns those scores into weights, and combines what those sources carry. That operation helped language models connect distant positions and made a different kind of sequence architecture practical.

## B02 · One Summary Is a Bottleneck (19.3s)

Start with a basic encoder-decoder translation model. The encoder compresses the source into one fixed-length vector, and the decoder generates the translation from it. That puts pressure on a single summary. The attention approach explored by Bahdanau and colleagues lets the decoder consult different source states as it produces different output words.

## B03 · Context Can Change Each Step (17.8s)

The source states stay available. At each decoding step, a new set of weights creates a new context vector. One step can draw more from one region; another step can draw more from another. These weights are a schematic illustration, not a measured translation alignment. The important change is repeated access to the source.

## B04 · Query, Key, Value (19.2s)

For the dot-product attention used in Transformers, three roles make the operation easier to follow. A query is compared with keys to produce scores. Values supply the vectors that will be mixed. In self-attention, all three come from the same sequence through learned projections. They are numeric representations, not literal questions, labels, or definitions.

## B05 · Compute the Scores (16.9s)

Here is a deliberately constructed example with two-dimensional keys. Our query is one, zero. Its dot products with the three keys are two, zero, and zero. Divide by the square root of two, because the key dimension is two. The first scaled score is about one point four one. The other two scores are zero.

## B06 · Scores Become Weights (19.0s)

Softmax exponentiates the scores and divides each result by their total. Our first source receives about sixty-seven percent of the weight; the other two receive about sixteen percent each. The unrounded weights sum to one. This is a distribution for mixing information, not a probability that a word is true or that an interpretation is correct.

## B07 · Mix the Values (22.5s)

Now apply those weights to the values. Multiplying and adding gives approximately zero point eight four for the first coordinate, and zero point three three for the second. Change only the query to zero and one, and the second key receives the largest score. The output becomes about zero point three three for the first coordinate, and zero point eight four for the second. Same keys and values; a different query produces a different mixture.

## B08 · Self-Attention and Cross-Attention (17.9s)

The names describe where the vectors come from. Self-attention relates positions within one sequence. Cross-attention takes queries from one sequence and keys and values from another, as when a decoder consults an encoder. Both use the same score, weight, and mix pattern. The distinction is the source of the information.

## B09 · Why the Transformer Mattered (24.5s)

Attention existed before the Transformer. The 2017 Transformer removed recurrence from its sequence-processing architecture. Allowed positions could interact directly through attention, and training could compute many positions in parallel. That shortened information paths and suited matrix-based hardware. Autoregressive generation still produces each new token using the preceding tokens; parallel training does not mean the whole answer appears in one step.

## B10 · Structure Still Matters (21.8s)

Attention needs surrounding structure. Position information helps represent order. A causal mask blocks access to future positions when predicting the next token. Multiple heads use different learned projections and combine their results. Heads can learn different patterns, but they are not assigned fixed jobs like grammar or meaning. Feed-forward layers and residual connections also remain part of a Transformer.

## B11 · Power Has Limits (19.6s)

There are costs and cautions. Doubling the sequence length quadruples the number of query-key pairs in dense full attention. And a bright cell in an attention map is not, by itself, proof of why the whole model answered as it did. Attention can be useful evidence to investigate, but explanations require tests of the model, not just a persuasive heat map.

## B12 · The Verdict (20.4s)

The change was a flexible way to exchange information across a sequence. Scores determine weights, weights mix values, and the surrounding architecture learns how to use that mixture. Attention helped move natural language processing beyond a single compressed summary and became a central building block of the Transformer. Follow the calculation before trusting the metaphor.

## B13 · Your Turn (18.2s)

Try this prompt: Implement our three-key attention example in Python. Print the scaled scores, softmax weights, and weighted values. Change the query and verify the result. Ask for the arithmetic, not just a diagram. Check that the weights sum to one, and keep the example clearly labeled as constructed rather than learned from language.

## B14 · Attention - Why It Changed NLP (5.1s)

Attention. Why it changed natural language processing. This is Sanjiv.
