---
layout: page
permalink: /publications/
title: publications
description: Full list of my publications in reverse chronological order. Also available on Google Scholar.
years: [2026, 2025, 2024, 2023]
nav: true
nav_order: 1
---

<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
