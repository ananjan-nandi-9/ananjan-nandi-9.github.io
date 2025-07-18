---
layout: project
title: Rule Augmentations for KGC
description: Simple augmentations to improve coverage and quality of rule sets for Neuro-Symbolic Knowledge Graph Completion
img: /assets/simpleaug.png
importance: 6
category: Knowledge Graphs
collaborators: Prof. Mausam, Prof. Parag Singla
paper_url: https://aclanthology.org/2023.acl-short.23/
published: true
---

### Abstract

High-quality and high-coverage rule sets are imperative to the success of Neuro-Symbolic Knowledge Graph Completion (NS-KGC) models, because they form the basis of all symbolic inferences. 

Recent literature builds neural models for generating rule sets, however, preliminary experiments show that they struggle with maintaining high coverage. In this work, we suggest three simple augmentations to existing rule sets: (1) transforming rules to their abductive forms, (2) generating equivalent rules that use inverse forms of constituent relations and (3) random walks that propose new rules. 

Finally, we prune potentially low quality rules. Experiments over four datasets and five ruleset-baseline settings suggest that these simple augmentations consistently improve results, and obtain up to 7.1 pt MRR and 8.5 pt Hits@1 gains over using rules without augmentations.
