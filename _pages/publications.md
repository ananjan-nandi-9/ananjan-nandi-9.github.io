---
layout: page
permalink: /publications/
title: publications
description: Full list of my publications in reverse chronological order. Also available on <a href="https://scholar.google.com/citations?user=I3uNMUEAAAAJ" target="_blank" rel="noopener noreferrer">Google Scholar</a>.
years: [2026, 2025, 2024, 2023] # prepend the new year here every January, or papers won't appear
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
