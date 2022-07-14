# Synthetic NeRF dataset creation tool

 This tool was created to leverage the power of [AI葵 (kwea123)](https://github.com/kwea123)'s Lightning fast [NeRF](https://github.com/kwea123/ngp_pl). It uses the `colmap2nerf` script from [NVIDIA's Instant NeRF](https://github.com/NVlabs/instant-ngp) implementation and [COLMAP](https://colmap.github.io/index.html) to produce a Synthetic NeRF dataset formated like the those in [Facebook Research NSVF Synthetic NeRF datasets](https://github.com/facebookresearch/NSVF#dataset).<br><br>
 Feel free to use, and enhance. I wrote this in a few free hours and some of the code might not be pythonic enough. You are more than welcome to contribute to this effort.<br>

### :book: Dataset structure<br>
```bash
<dataset_name>
|-- bbox.txt         # bounding-box file
|-- intrinsics.txt   # 4x4 camera intrinsics
|-- rgb
    |-- 0.png        # target image for each view
    |-- 1.png
    ...
|-- pose
    |-- 0.txt        # camera pose for each view (4x4 matrices)
    |-- 1.txt
    ...
```

The resulting ``bbox.txt`` file contains a line describing the initial bounding box and voxel size:

```bash
x_min = -7.500 y_min = -7.500 z_min = -7.500 x_max = 8.500 y_max = 8.500 z_max = 8.500 initial_voxel_size = 0.4
```
 I hardcoded those values by referencing [NVIDIA's Instant NeRF](https://github.com/NVlabs/instant-ngp)'s rendering GUI. You are more than welcome to change them to fit your needs.<br><br>
 The datasets are split with view indices. For example, "``train (0..100)``, ``valid (100..200)`` and ``test (200..400)``" mean the first 100 views for training, 100-199th views for validation, and 200-399th views for testing.
<br>
### Required libraries
tqdm, halo, Pillow, json, opencv-python, argparse, pathlib, numpy
### :computer: Usage
- Have [Colmap](https://colmap.github.io/index.html) installed in your system and added to your system PATH.<br>
- Create an images folder and add the photos you want for the dataset.<br>
- Run ``python dataset.py``<br>
- The tool will convert .JPG files to .PNG format and also resize to a standard 800 x 800. This is done for ease of use and avoid potential errors when training.<br>
- At the end of processing, you should now have an [NSVF style](https://github.com/facebookresearch/NSVF) formatted dataset to train with [NGP_PL](https://github.com/kwea123/ngp_pl).<br>

### :tv: The video below shows the tool in action

https://user-images.githubusercontent.com/6027881/178971425-6d593d58-52ae-46c7-bfd1-57e4ba4c2344.mp4


### :grey_exclamation: Changelog

- Standarized image output and size.
- Added randomization to test and validation sets.
- Removed redundant code.

### :hammer: To Do

- Create GUI
- Add funtionality to prepare datasets for colorless and colorized mesh extraction

### :+1: Acknowledgments
[AI葵, kwea123](https://github.com/kwea123) for the amazing work in the instant NeRF field.<br>
[NVIDIA Research Projects](https://github.com/NVlabs) for their breakthroughs in this field.<br>
[Meta -Formerly Facebook- Research](https://github.com/facebookresearch)
