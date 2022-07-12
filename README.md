# Synthetic NeRF Dataset creation tool

I just put together this dataset creation tool to leverage the power of [AI葵
kwea123's](https://github.com/kwea123) [amazing pure pytorch+cuda trained with pytorch-lightning implementation\https://github.com/kwea123/ngp_pl. This tool uses the colmap2nerf script from [NVIDIA's Instant NeRF implementation] (https://github.com/NVlabs/instant-ngp)

# Usage
Have colmap installed in your system and added to your system PATH
create an images folder and add the photos you want for the dataset.
run python data_handler.py.
At the end of processing, you shoould now have an NSVF formatted dataset to train onto 
