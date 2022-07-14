# Synthetic NeRF Dataset creation tool
(Preliminary writeup) - I will add more as time allows.

 I just put tool to leverage the power of [AI葵kwea123's](https://github.com/kwea123) amazing pure [pytorch+cuda trained with pytorch-lightning implementation](https://github.com/kwea123/ngp_pl).<br>
 This tool uses the colmap2nerf script from [NVIDIA's Instant NeRF](https://github.com/NVlabs/instant-ngp) implementation and produces a Synthetic NeRF dataset formated like the ones in [Facebook Research NSVF Synthetic NeRF datasets](https://github.com/facebookresearch/NSVF#dataset).<br>
 Feel free to use and enhance. I wrote this in a couple hours and some of the code might not be pythonic enough. You are more than welcome to contribute to this effort. I will add compatibility results shortly.<br>

### Dataset structure<br>
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

where the ``bbox.txt`` file contains a line describing the initial bounding box and voxel size:

```bash
x_min = -7.500 y_min = -7.500 z_min = -7.500 x_max = 8.500 y_max = 8.500 z_max = 8.500 initial_voxel_size = 0.4
```
 I hardcoded those values by referencing [NVIDIA's Instant NeRF](https://github.com/NVlabs/instant-ngp)'s rendering GUI. You are more than welcome to change them to fit your needs.<br><br>
 The datasets are split with view indices. For example, "``train (0..100)``, ``valid (100..200)`` and ``test (200..400)``" mean the first 100 views for training, 100-199th views for validation, and 200-399th views for testing.
<br>
## Usage
- Have [Colmap](https://colmap.github.io/index.html) installed in your system and added to your system PATH.<br>
- Create an images folder and add the photos you want for the dataset.<br>
- Run python dataset.py.<br>
- The tool will convert .JPG files to .PNG format and also resize to a standard 800 x 800. This is done for ease of use and potential processiung issues later.<br>
- At the end of processing, you should now have an [NSVF](https://github.com/facebookresearch/NSVF) style formatted dataset to train onto the implementation.<br>

<iframe width="560" height="315" src="https://www.youtube.com/embed/XutC0lIkWqg?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Acknowledgments
[AI葵, kwea123](https://github.com/kwea123) for his amazing work in the instant NeRF field.<br>
[NVIDIA Research Projects](https://github.com/NVlabs) for their breakthroughs in this field.<br>
[Meta -Formerly Facebook- Research](https://github.com/facebookresearch)
