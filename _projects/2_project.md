---
layout: page
title: Land Use-Land Cover Map Generation
description: Prof. Aaditeshwar Seth
img: assets/img/LULC_India.png
importance: 2
category: work
published: true
---

This project is related to the generation of Land Use-Land Cover maps from satellite time series data. The aim is to use temporal data to do finer-grained LULC classification on top of existing spatial classifers such as Dynamic World from Google. Adding temporal data should help in separation of classes such as Farmland and Forest from areas in which greenery is identified, and segregation of Farmland based on crop seasonality and intensity. 

So far, I have obtained F1 Score above 0.95 for the segregation of green pixels into Farmland and Forest by using a classifier trained on a composite of LandSat, Sentinel and MODIS NDVI data, smoothened using Whittaker smoothing. Pipelines for this classification have been implemented on Google Earth Engine and TensorFlow. 

Have a look at the results below:

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/LULC_Raw.png" title="Satellite Imagery" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/LULC_Mandya.png" title="LULC Map" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    LULC Map for area around Mandya, 
</div>

You can also put regular text between your rows of images.
Say you wanted to write a little bit about your project before you posted the rest of the images.
You describe how you toiled, sweated, *bled* for your project, and then... you reveal its glory in the next row of images.


<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    You can also have artistically styled 2/3 + 1/3 images, like these.
</div>


The code is simple.
Just wrap your images with `<div class="col-sm">` and place them inside `<div class="row">` (read more about the <a href="https://getbootstrap.com/docs/4.4/layout/grid/">Bootstrap Grid</a> system).
To make images responsive, add `img-fluid` class to each; for rounded corners and shadows use `rounded` and `z-depth-1` classes.
Here's the code for the last row of images above:

{% raw %}
```html
<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/6.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-4 mt-3 mt-md-0">
        {% include figure.html path="assets/img/11.jpg" title="example image" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
```
{% endraw %}
