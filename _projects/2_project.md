---
layout: page
title: h4rm3l
description: A dynamic benchmark of composable jailbreak attacks for systematically evaluating LLM safety
img: assets/benchmark_plot.jpg
importance: 2
category: AI Safety
collaborators: Prof. Christopher D. Manning, Prof. Dan Jurafsky
paper_url: https://mdoumbouya.github.io/h4rm3l/
published: true
---

### Abstract

The safety of Large Language Models (LLMs) remains a critical concern due to a lack of adequate benchmarks for systematically evaluating their ability to resist generating harmful content. Previous efforts towards automated red teaming involve static or templated sets of illicit requests and adversarial prompts which have limited utility given jailbreak attacks' evolving and composable nature. We propose a novel dynamic benchmark of composable jailbreak attacks to move beyond static datasets and taxonomies of attacks and harms. Our approach consists of three components collectively called h4rm3l: (1) a domain-specific language that formally expresses jailbreak attacks as compositions of parameterized prompt transformation primitives, (2) bandit-based few-shot program synthesis algorithms that generate novel attacks optimized to penetrate the safety filters of a target black box LLM, and (3) open-source automated red-teaming software employing the previous two components. We use h4rm3l to generate a dataset of 2656 successful novel jailbreak attacks targeting 6 state-of-the-art (SOTA) open-source and proprietary LLMs. Several of our synthesized attacks are more effective than previously reported ones, with Attack Success Rates exceeding 90% on SOTA closed language models such as claude-3-haiku and GPT4-o. By generating datasets of jailbreak attacks in a unified formal representation, h4rm3l enables reproducible benchmarking and automated red-teaming, contributes to understanding LLM safety limitations, and supports the development of robust defenses in an increasingly LLM-integrated world.

[Link to Paper](https://mdoumbouya.github.io/h4rm3l/)
