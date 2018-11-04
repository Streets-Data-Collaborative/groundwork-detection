# groundwork-detection
ARGO internship project to use http://customvision.ai to detect features from US Street imager

## Why
Small improvements in "Maintenance, management of state assets and public-sector accounting", [according to a recent Economist op-ed](https://www.economist.com/leaders/2018/10/20/large-economic-gains-can-come-from-mundane-improvements-in-policy)  could lead to large economic gains for cities, states, and entire nations.

We believe that local and state governments should be capable of auditing the urban environment using common-sense digital tools and leveraging advances in machine learning, responsibly towards the next-generation of Maintenance, management of state assets and public-sector accounting.

## What
Using street view imagery, develop a computer vision model that is trained on three specific elements of urban infrastructure, namely: 
1. Detection of US street signage.
2. Road width estimates.
3. Detection and counting of Yellow Taxis on NYC streets.

## How
Use http://customvision.ai - an easy-to-use computer vision toolkit developed by Microsoft.

## When
### Week 1 - Orientation
- Read the [SQUID Story](https://www.hackster.io/argo/squid-street-quality-identification-a43367)
- Learn how to use http://customvision.ai to develop quick computer vision applications.
- Learn how to collect street view imagery at a citywide scale using [Google Street View API](https://developers.google.com/maps/documentation/streetview/intro) and [Open Street Cam - OSC](http://openstreetcam.org/) and our [OSC-ETL tools](https://github.com/Streets-Data-Collaborative/osc-tools).
- Develop and Document simple data specifications for each of the detections.
- Isolate your imagery for model training.

### Week 2 - Train & Test
- Upload training imagery to customvision interface.
- Label what you intend to detections from the uploaded imagery.
- Test the accuracy of your trained model.
- Iterate towards better precision and recall.

### Week 3 - Results
- Parse results from customvision output into a more readable format.
- Deploy your trained model to "audit" a specific geography. (For consistency, we will choose this area for you).
- Prepare blog to document your journey. What worked, What did not. Ideas for future improvement / applications etc.

## Who
ARGO project supervisor: Varun Adibhatla

CUSP Students

### Operational Roles 
- Project scribe: CUSP student who will take notes during check-in and manage the github repo (code,readme, issues)
- Project logistics: CUSP student who ensures meetings are scheduled and handles conference/video calls.
