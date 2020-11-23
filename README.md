# ELEC498Capstone
Currently uses 2 models:
  - YOLO - Extracting bird subimages
  - Custom Tensorflow model - Classify `goose` and `not goose`
## Instructions
  - Download the weights from https://pjreddie.com/media/files/yolov3.weights
  - Move the file (`yolov3.weights`) to `config/`
  - Run `model.ipynb` using Jupyter.
## Dependancies
  - Matplotlib
  - OpenCV
  - Tensorflow (GPU is preferred)
##### YOLO Bounding box detection on goose.
![YOLO Bounding box detection on goose](https://i.imgur.com/4f4BXGA.jpg)