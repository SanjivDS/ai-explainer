# Transformers - Encoder, Decoder & Self-Attention — Narration script

Voice: Kokoro `am_onyx` (local, free). Verbatim from `narration_text` in [`beat_sheet.json`](beat_sheet.json).

## B00 · The Question (14.2s)

Hi. This is Sanjiv. Today we shall discuss Transformers: encoders, decoders, and self-attention. We will follow a sentence through the architecture, calculate a tiny attention example, and see how a decoder produces its next token.

## B01 · The Big Picture (18.7s)

Tokens work in context. A Transformer updates each token's representation using information from other allowed positions. Encoders and decoders use this machinery differently. To understand the architecture, track two things: where the information comes from, and which positions each token is allowed to see.

## B02 · The Architecture Map (18.8s)

Start with the original encoder-decoder design. The encoder reads a source sequence and produces contextual representations. The decoder uses the target prefix and those source representations to predict the next target token. This is one Transformer arrangement; we will also distinguish encoder-only and decoder-only models.

## B03 · Give Tokens Position (20.0s)

Text first becomes tokens, then embedding vectors. The model also needs information about position. Otherwise, unrestricted self-attention by itself does not know which token came first. The original Transformer adds positional encodings to embeddings. Other designs supply position information differently, but order must enter the computation somehow.

## B04 · Self-Attention Connects a Sequence (18.1s)

In self-attention, queries, keys, and values come from the same sequence of representations through learned projections. A query is compared with keys to produce scores. Those scores become weights over the values. Each output mixes information from allowed positions, including its own position when the mask permits it.

## B05 · Calculate Attention Weights (19.2s)

Here is a constructed example with two-dimensional queries and keys. Our query is one, zero. Its dot products with the three keys are one, zero, and one. Divide by the square root of two, then apply softmax. The resulting weights are approximately zero point four zero one, zero point one nine eight, and zero point four zero one.

## B06 · Mix the Values (19.1s)

Now use those weights to combine three value vectors. Our supplied values are one, zero; zero, two; and three, one. The weighted sum is approximately one point six zero four, zero point seven nine seven. This is a new representation, not a selected word. These numbers illustrate arithmetic, not a trained model's behavior.

## B07 · Why Multiple Heads (19.0s)

A multi-head layer repeats attention with different learned projections. Each head can form a different mixture. The head outputs are concatenated and projected back into the model's representation space. Do not assume one head always handles grammar and another always handles meaning; those neat labels are not guaranteed by the architecture.

## B08 · Inside an Encoder Block (21.6s)

An encoder block contains more than attention. In the original arrangement, a residual connection and normalization follow self-attention. A feed-forward network then transforms each position separately, followed by another residual connection and normalization. Stacking these blocks repeatedly updates the representations. Normalization placement varies across Transformer designs.

## B09 · The Decoder Cannot Peek (17.5s)

For next-token prediction, the decoder must not see the answer through later target positions. Its self-attention uses a causal mask. A position can attend to itself and earlier positions in the shifted input, but not later ones. Masked scores are excluded before softmax, so their attention weights become zero.

## B10 · Cross-Attention Reads the Source (19.4s)

In an encoder-decoder Transformer, another attention layer connects the two streams. Its queries come from decoder states, while its keys and values come from encoder outputs. That is cross-attention. The decoder can consult the source while building its target sequence. Self-attention connects positions within a stream; cross-attention connects different streams.

## B11 · Training and Generation (17.6s)

During training, the target sequence is already known. With shifted inputs and a causal mask, many target positions can be processed together without revealing their future answers. During ordinary autoregressive generation, the next token is not known yet. Predict a distribution, choose a token, append it, and repeat.

## B12 · Three Transformer Families (21.6s)

Encoder-only models build contextual representations that can support classification or token labeling. Decoder-only models use causal self-attention for next-token prediction without a separate encoder. Encoder-decoder models connect a source sequence to a generated target through cross-attention. The name Transformer describes a family, not one fixed wiring diagram.

## B13 · Check the Mask (18.4s)

We can test the information boundary. Keep our supplied queries and keys fixed, and change only a future value vector. With the causal mask, earlier attention outputs must stay unchanged. Without that mask, they can change. This small test checks our attention implementation; it does not establish the quality of a trained language model.

## B14 · The Verdict (22.5s)

Self-attention mixes information across allowed positions. Position information supplies order. Encoder and decoder blocks organize these operations, and masks control access to context. Follow the information flow and the large diagram becomes easier to read. Attention is a central component; the complete Transformer also needs projections, feed-forward layers, residual paths, and normalization.

## B15 · Your Turn (19.0s)

Build a tiny scaled dot-product attention example with three tokens. Show the queries, keys, values, softmax weights, and output. Add a causal mask and verify that changing a future value cannot affect earlier outputs. Use this prompt to reproduce the calculation. Ask for runnable code and inspect the test, not just the diagram.

## B16 · Transformers (5.0s)

Transformers. Encoder. Decoder. And self-attention. This is Sanjiv.
