---
layout: project
title: Rule Augmentations for KGC
description: Simple augmentations to improve coverage and quality of rule sets for Neuro-Symbolic Knowledge Graph Completion
img: /assets/simpleaug.png
importance: 5
category: Knowledge Graphs
collaborators: Prof. Mausam, Prof. Parag Singla
paper_url: https://aclanthology.org/2023.acl-short.23/
published: true
---

### Abstract

High-quality and high-coverage rule sets are imperative to the success of Neuro-Symbolic Knowledge Graph Completion (NS-KGC) models, because they form the basis of all symbolic inferences. Recent literature builds neural models for generating rule sets, however, preliminary experiments show that they struggle with maintaining high coverage.

In this work, we suggest three simple augmentations to existing rule sets:

1. **Transforming rules to their abductive forms**: Converting deductive rules into abductive reasoning patterns
2. **Generating equivalent rules using inverse relations**: Creating rules that utilize inverse forms of constituent relations  
3. **Random walks for rule proposal**: Using random walks to propose new rules and expand coverage

Finally, we prune potentially low quality rules to maintain overall rule set quality.

### Results

Experiments over four datasets and five ruleset-baseline settings suggest that these simple augmentations consistently improve results, obtaining up to **7.1 pt MRR** and **8.5 pt Hits@1** gains over using rules without augmentations.

The approach demonstrates that simple, principled augmentations can significantly enhance the performance of neuro-symbolic knowledge graph completion systems without requiring complex architectural changes.
