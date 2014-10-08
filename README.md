HPCDash
=======

Web dashboard for HPC job monitoring, designed for scientists.

Within any laboratory that routinely utilizes supercomputers, it can be difficult to track the progress of compute jobs. In practice, multiple scientists must coordinate the usage of compute resources within an allocation of compute time and must follow their own experiments manually using tedious daily commands. The aim of this project is to simplify the tracking computer jobs and the usage of supercomputers using a web dashboard, providing scientists with a comprehensive picture of supercomputer usage at a glance.

Examples of beautiful web dashboards can be seen from companies like [Geckoboard](https://www.geckoboard.com/), [Chartio](https://chartio.com/), or [Ducksboard](https://ducksboard.com/). Open source variants of these services exist as frameworks for software development (see [Dashing.io](http://dashing.io/), [JSPlate](https://github.com/rasmusbergpalm/jslate), [Dash-Ku](https://github.com/Anephenix/dashku), [Angular Dashboard Framework](https://github.com/sdorra/angular-dashboard-framework)). These frameworks may or may not provide the functionality needed for this projects goals. 

To expose data from supercomputers over the web, several groups have developed APIs and web applications for securely communicating with HPC resources (see [Agave API](http://agaveapi.co/), [OpenLorenz](https://github.com/hpc/OpenLorenz/), [NEWT](https://newt.nersc.gov/). Similarly, grid computing software initiatives expose APIs for HPC resources in order to facilitate a common gateway for submitting and monitoring jobs. On the smaller scale, the Pomes laboratory utilizes [a basic CPU usage tracker](https://github.com/pomeslab/sumcoresg) for job monitoring, but the functionality of these code is limited..

To summarize, the desired implementation of this web dashboard will be built using the following components:
* Dashboard framework for the UI
* Javascript charting library for dashboard widgets. 
* Real-time API calls to supercomputing resources using NEWT

Although an initial implementation above is not completed, the following points describe desired functionality of this software in the long-run.
* Differing public and private views of web dashboard, to encourage open science.
* Web-based administration to add new compute resources.
* Dashboard widget support for domain-specific scientific data visualizations (3d plots, heat maps, image data).
* Functionality for flagging erroneous or unusual data by anonymous users.

