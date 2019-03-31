# Custom Vision 

The steps are summarized below:

1. First we extracted images from Open-Street-Cam and GoogleStreet View using the ETL [scripts](https://github.com/Streets-Data-Collaborative/groundwork-detection/tree/master/Taxis/ETL_scripts). 
2. Then trained the Custom Vision model manually directly on https://www.customvision.ai/projects and, 
3. Finally developed a script to analyze new images by calling the pre-trained model using the parameters below (see github [Custom-vision script](https://github.com/Streets-Data-Collaborative/groundwork-detection/blob/master/Taxis/CustomVisionPrediction_scripts/Cab_Counting_Neighborhoods.ipynb).
The  Custom-vision script extracts Google images based on the imported shape file. So if someone wants to use the  Custom-vision script (from step 3) on another geography, you would have to edit the script and import the appropriate shape files.

## Custom Vision parameters
Prediction_Key = 'd523a599e7f845e6b0af872a5cfa4698'
Content_Type = 'application/octet-stream'
__PRED_URL__ = 'https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/' \
  + 'Prediction/6f366357-d7dc-4b0e-a6fe-e61984f90bad/image?iterationId=473dfffd-c1d0-4bca-b679-a6b47620c5ad'


# More about Custom Vision ...

If you want to create your own Custom Vision model, you can train your own model using the indications below:

- [**CustomVisionPrediction_ image.ipynb**](https://github.com/Streets-Data-Collaborative/groundwork-detection/blob/master/Taxis/CustomVisionPrediction_scripts/CustomVisionPrediction_%20image.ipynb) detects objects using Custom Vision API, returns the Custom Vision prediction result in json format.

---

- [**CustomVisionPrediction_folder.ipynb**](https://github.com/Streets-Data-Collaborative/groundwork-detection/blob/master/Taxis/CustomVisionPrediction_scripts/CustomVisionPrediction_folder.ipynb) detects objects using Custom Vision API, returns the Custom Vision prediction result in json format, and counts the number of target objects for all PNG images in a single folder directory.

### Parameters:
- folder: folder path.
- Prediction_Key: refer to customvision.ai/projects - Performance - Prediction URL - Prediction-Key.
- Content_Type: default set as 'application/octet-stream' for image file prediction.
- projectId: refer to customvision.ai/projects - projectId.
- prediction_probability_threshold: Above this prediction probability threshold, we decide to detect the object as a target.

### Reference:
- CustomVision documents: https://southcentralus.dev.cognitive.microsoft.com/docs/services/450e4ba4d72542e889d93fd7b8e960de/operations/5a6264bc40d86a0ef8b2c290
