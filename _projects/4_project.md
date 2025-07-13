---
layout: project
title: CTC-DRO
description: A robust optimization approach to improve the performance of worst-performing languages for multilingual speech recognition
img: /assets/language_training_analysis.png
importance: 4
category: Machine Learning
collaborators: Prof. Tatsunori Hashimoto, Prof. Dan Jurafsky, Prof. Karen Livescu
github: https://github.com/Bartelds/ctc-dro
paper_url: https://arxiv.org/abs/2407.00870
published: true
---

### Abstract

Modern deep learning models often achieve high overall performance, but consistently fail on specific subgroups. Group distributionally robust optimization (group DRO) addresses this problem by minimizing the worst-group loss, but it fails when group losses misrepresent performance differences between groups. This is common in domains like speech, where the widely used connectionist temporal classification (CTC) loss scales with input length and varies with linguistic and acoustic properties, leading to spurious differences between group losses. 

We present **CTC-DRO**, which addresses the shortcomings of the group DRO objective by smoothing the group weight update to prevent overemphasis on consistently high-loss groups, while using input length-matched batching to mitigate CTC's scaling issues. We evaluate **CTC-DRO** on the task of multilingual automatic speech recognition (ASR) across five language sets from the ML-SUPERB 2.0 benchmark. **CTC-DRO** consistently outperforms group DRO and CTC-based baseline models, reducing the worst-language error by up to 47.1% and the average error by up to 32.9%. **CTC-DRO** can be applied to ASR with minimal computational costs, and offers the potential for reducing group disparities in other domains with similar challenges.
