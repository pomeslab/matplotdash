Matplotdash
=======

An analytics dashboard designed for real-time visualization of scientific data.

Analytics dashboards are ubiquitous in business and marketing analytics, made famous by the boom of software start-ups. However, these dashboard solutions are either closed-source “software as a service” solutions, or not designed with scientific visualization in mind. The aim of this project is to develop a science-agnostic web dashboard to assist computational scientists in performing routine analysis and rare event detection with arbitrary time series data sources. This software is focussed on a front-end for real-time analytics that is general and supports scientific visualizations out of the box.

A primary application for this analytics dashboard is in the discipline of high-performance computing and computational science. In this field, data is often continuously generated on the days to years timescale, but there is no solution to perform monitoring of these simulations without the use of manual and repeated re-analysis over the length of the project. For this reason, Matplotdash intends to support a number of HPC APIs (see [Agave API](http://agaveapi.co/),  [NEWT](https://newt.nersc.gov/)) in order to security expose data being generated on supercomputers in conjunction with a piece of software running concurrently with scientific simulations.

Although an initial implementation above is not completed, the following points describe desired long-term functionality.
* Public and private views of web dashboard, to encourage open science.
* Dashboard widget support for numerous data visualizations libraries (Bokeh, Lightning-Viz, Etc.)

Questions about this project should be sent to Chris Ing (ing.chris@gmail.com),@jsci
The foundation of this code will be developed with assistance from the [Mozilla Science Lab](http://www.mozillascience.org/).
