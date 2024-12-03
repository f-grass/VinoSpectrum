import os
from spectral import *
from read_tiff import read_tiff

input_folder = "data/47grad_nah_TIFF"
output_folder = "data/rgb_47_nah"
files = os.listdir(path=input_folder)

i = 0
for file in files:
    i += 1
    array = read_tiff(path=input_folder + "/" + file)

    save_rgb(f'{output_folder}/{file[:-5]}.jpg', array, [11, 6, 0])
    print(f"save {i}/{len(files)}")



