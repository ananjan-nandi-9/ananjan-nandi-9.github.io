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

So far, we have obtained F1 Score above 0.95 for the segregation of green pixels into Farmland and Forest by using a classifier trained on a composite of LandSat, Sentinel and MODIS NDVI data, smoothened using Whittaker smoothing. Pipelines for this classification have been implemented on Google Earth Engine and TensorFlow. 

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
    LULC Map for area around Mandya, Karnataka
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/LULC_BRaw.png" title="Satellite Imagery" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/LULC_Berambadi.png" title="LULC Map" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Boundary of Berambadi forest, Karnataka
</div>

We have also obtained encouraging results for unsupervised classification of the Cropland class according to cropping intensity and seasonality by utilizing TimeSeriesKMeans to cluster the NDVI time series for the Farmland class. The cluster centers obtained with 4 clusters is displayed below. The clusters correspond to double cropping, and single cropping in the Kharif and Rabi seasons. 

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/Cropland_Clusters.png" title="Clusters" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
