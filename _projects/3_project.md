---
layout: project
title: Roleplay-doh
description: A framework enabling domain experts to create realistic LLM-simulated patients for medical training
img: /assets/rpdteaser-clean.png
importance: 3
category: Healthcare AI
collaborators: Prof. Diyi Yang, Prof. Emma Brunskill
github: https://github.com/SALT-NLP/roleplay-doh
paper_url: https://arxiv.org/abs/2407.00870
published: true
---

### Abstract

Recent works leverage LLMs to roleplay realistic social scenarios, aiding novices in practicing their social skills. However, simulating sensitive interactions, such as in mental health, is challenging. Privacy concerns restrict data access, and collecting expert feedback, although vital, is laborious. 

To address this, we develop **Roleplay-doh**, a novel human-LLM collaboration pipeline that elicits qualitative feedback from a domain-expert, which is transformed into a set of principles, or natural language rules, that govern an LLM-prompted roleplay. We apply this pipeline to enable senior mental health supporters to create customized AI patients for simulated practice partners for novice counselors. After uncovering issues in GPT-4 simulations not adhering to expert-defined principles, we also introduce a novel principle-adherence prompting pipeline which shows 30% improvements in response quality and principle following for the downstream task. 

Via a user study with 25 counseling experts, we demonstrate that the pipeline makes it easy and effective to create AI patients that more faithfully resemble real patients, as judged by creators and third-party counselors.