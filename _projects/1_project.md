---
layout: page
title: Sneaking Syntax into Transformer Language Models with Tree Regularization
description: 'Prof. Christopher D. Manning'
img: assets/TR1.png
importance: 1
category: work
published: true
---

### Abstract

While compositional accounts of human language understanding are based on a hierarchical tree-like process, neural models like transformers lack a direct inductive bias for such tree structures. Introducing syntactic inductive biases could unlock more robust and data-efficient learning in transformer language models (LMs), but existing methods for incorporating such structure greatly restrict models, either limiting their expressivity or increasing inference complexity. This work instead aims to softly inject syntactic inductive biases into given transformer circuits, through a structured regularizer. We introduce TREEREG, an auxiliary loss function that converts bracketing decisions from silver parses into a set of differentiable orthogonality constraints on vector hidden states. TREEREG integrates seamlessly with the standard LM objective, requiring no architectural changes. LMs pre-trained with TreeReg on natural language corpora such as WikiText-103 achieve up to 10% lower perplexities on out-of-distribution data and up to 9.5 point improvements in syntactic generalization, requiring less than half the training data to outperform standard LMs. TreeReg still provides gains for pre-trained LLMs: Continued pre-training of Sheared Llama with TreeReg results in improved syntactic generalization, and fine-tuning on MultiNLI with TreeReg mitigates degradation of performance on adversarial NLI benchmarks by 41.2 points.

[Link to Paper](https://arxiv.org/abs/2411.18885)
