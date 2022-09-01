# CarBodyDamageDetection : Detect Exterior Car Damage Using YOLOv5
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Uu7XuWf09z-H2PDv93WywyVxCX3K4ef4?usp=sharing)

This project detects damage on the car body using the state-of-the-art [YOLOv5](https://github.com/ultralytics/yolov5) algorithm. 

## Project Steps
  1. Dataset of 100 images is collected.
  2. VOTT is used to add images annotations.
  3. Labels .txt files are generated.
  4. Dataset is splitted 9:1 for train and test.
  5. Model YOLOv5x is trained on the dataset.

## Repo Content
  1. Custom Labeled Dataset
  2. Train Notebook
  3. YOLOv5 .yaml File

## Train YOLOv5 on Custom Data
You can train YOLOv5 on your custom images through these steps:

  1. Place all the dataset images in one folder.
  2. Download [VOTT](https://github.com/microsoft/VoTT).
  3. Follow the [Annotations README.md](https://github.com/DohaElHady/CarBodyDamageDetection/blob/main/Annotations/README.md).
  4. Set the dataset structure in [Dataset README.md](https://github.com/DohaElHady/CarBodyDamageDetection/blob/main/Dataset/README.md).
  5. Upload file to either Github or Google Drive.
  6. Clone the file to the Notebook.
  7. Run "CarBodyDamageDetection-YOLOv5.ipynb".
  8. Best model will be avilable at "/content/yolov5/runs/train/exp(i)/weights/best.pt".
  
