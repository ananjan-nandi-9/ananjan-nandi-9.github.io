---
layout: project
title: DynaSemble
description: Dynamic ensembling approach that intelligently selects and weights models based on input characteristics
img: /assets/dynasemble.png
importance: 5
category: Machine Learning
collaborators: Prof. Mausam, Prof. Parag Singla
paper_url: https://example.com/dynasemble
published: true
---

### Abstract

We consider two popular approaches to Knowledge Graph Completion (KGC): textual models that rely on textual entity descriptions, and structure-based models that exploit the connectivity structure of the Knowledge Graph (KG). 

Preliminary experiments show that these approaches have complementary strengths: structure-based models perform exceptionally well when the gold answer is easily reachable from the query head in the KG, while textual models exploit descriptions to give good performance even when the gold answer is not easily reachable. 

In response, we propose **DynaSemble**, a novel method for learning query-dependent ensemble weights to combine these approaches by using the distributions of scores assigned by the models in the ensemble to all candidate entities. **DynaSemble** achieves state-of-the-art results on three standard KGC datasets, with up to 6.8 pt MRR and 8.3 pt Hits@1 gains over the best baseline model for the WN18RR dataset.
