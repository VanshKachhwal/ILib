# ILib
This repository contains the development code for the ILib package

## Package installation:
1. Open the command prompt
2. Run `pip install git+https://github.com/VanshKachhwal/ILib` in the cmd prompt

## Various Functions:
* **To Remove Background:**

  Copy the path where the photos are present (Only photos must be present in the respective folder) - `input_path` ; specify where you want the images with background removed to get stored - `output_path` ; the background color to set in form of color_channels eg. - `(255,255,255)`, model type 0 or 1 - 0 is general,  1 is landscape (faster) ; threshold (between 0 and 1) to define the degree of accurate background cuts (more the threshold more will be the time taken) and then execute the following code -
  ```python
  from ILib.BackgroundModule import remove_background
  remove_background(r'input_path', r'output_path', color_channels, model, threshold)
  ##default :- color_channels - (255,255,255),  model - 0, threshold - 0.1
  ```
* **To Auto-Align Images:**

  Copy the path where the photos are present (Only photos must be present in the respective folder) - `input_path` ; specify where you want the images with background removed to get stored - `output_path` ; min_face_detection_confidence ; min_pose_detection_confidence and then execute the following code -
  ```python
  from ILib.AutoAlignerModule import auto_align
  auto_align(r'input_path', r'output_path', min_face_detection_confidence, min_pose_detection_confidence)
  ##default :- min_face_detection_confidence - 0.5, min_pose_detection_confidence - 0,5
  ```
* **To Create Collage:**

  Copy the path where the photos are present (Only photos must be present in the respective folder) - `input_path` ; specify the final collage file name with the required extension ; width ; height and then execute the following code -
  ```python
  from ILib.CollageModule import make_collage
  make_collage(r'input_path', 'file_name', width, height)
  ```


