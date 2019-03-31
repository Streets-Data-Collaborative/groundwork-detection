# Team 2 - Yellow Taxis.

Medium Article: https://medium.com/streets-data-collaborative-groundwork-team-2/91220c1f2b1

# Custom Vision 

The steps are summarized below:

1. First we extracted images from Open-Street-Cam and GoogleStreet View using the ETL [scripts](https://github.com/Streets-Data-Collaborative/groundwork-detection/tree/master/Taxis/ETL_scripts). 
2. Then trained the Custom Vision model manually directly on https://www.customvision.ai/projects and, 
3. Finally developed a script to analyze new images by calling the pre-trained model using the parameters below (see github [Custom-vision script](https://github.com/Streets-Data-Collaborative/groundwork-detection/blob/master/Taxis/CustomVisionPrediction_scripts/Cab_Counting_Neighborhoods.ipynb).
The  Custom-vision script extracts Google images based on the imported shape file. So if someone wants to use the  Custom-vision script (from step 3) on another geography, you would have to edit the script and import the appropriate shape files.
