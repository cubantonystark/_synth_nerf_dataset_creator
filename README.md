# Synthetic NeRF Dataset creation tool
(preliminary writeup) I will add more as time allows.

Feel free to use and enhance. i wrote this in a couple hours and some of the code might not be pythonic enough. You are more than welcome to contribute to this effort.<br>
<br>
I will add compatibility results shortly.<br>

I just put together this dataset creation tool to leverage the power of [AI葵
kwea123's](https://github.com/kwea123) [amazing pure pytorch+cuda trained with pytorch-lightning implementation](https://github.com/kwea123/ngp_pl). This tool uses the colmap2nerf script from [NVIDIA's Instant NeRF implementation](https://github.com/NVlabs/instant-ngp)

# Usage
Have colmap installed in your system and added to your system PATH.<br>
create an images folder and add the photos you want for the dataset.,br>
run python data_handler.py.<br>
At the end of processing, you should now have an NSVF formatted dataset to train onto the implementation.<br>
The tool works for both JPEG and PNG file formats.

# Acknowlegments
[AI葵, kwea123](https://github.com/kwea123) for his amazing work in the instant NeRF field.<br>
[NVIDIA Research Projects](https://github.com/NVlabs) for their breakthroughs in this field.
