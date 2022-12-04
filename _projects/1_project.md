---
layout: page
title: Neuro-Symbolic Knowledge Graph Completion
description: 'Prof. Parag Singla, Prof. Mausam'
img: assets/img/KGC.png
importance: 1
category: work
published: true
---

An early preprint of the work done in this project can be found [here]({{ site.url }}/assets/pdf/ACL_2023_NS_KGC.pdf). 

Abstract: High-quality rules are imperative to the success of Neuro-Symbolic Knowledge Graph (KG)
models because they equip the models with the desired qualities of interpretability and generalizability. Though necessary, learning logic rules is an inherently hard task. The past rule learning models in KGs have either struggled to learn rules at the scale required for large KGs or the rules learnt by such models are of poor-quality and not diverse. To address this limitation, we propose two novel ways of feeding more high-quality rules to Neuro-Symbolic Knowledge Graph reasoning models. Specifically, we augment the existing set of logic rules of a KG model by exploiting the concepts of abduction and rule inversion. Our proposed
approach is generic and is applicable to most neuro-symbolic KG models in literature. Experiments on three datasets prove that our proposed approach obtains upto 23% MR and 7% MRR gains over the base models.

Results:
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/Paper_Results.png" title="results" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Next Steps: 
+ We have found that filtering the generated rule files based on the FOIL or PCA Confidence scores can help identify the rules that are most important for model performance. 
+ We have also tested a third type of augmentation: a random-walk based rule discovery algorithm using the PCA Confidence scores. This has resulted in significant gains on a couple of datasets. 
+ Results for another baseline and the Kinship dataset will be updated soon. 