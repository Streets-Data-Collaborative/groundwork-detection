# Custom Vision Prediction
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
