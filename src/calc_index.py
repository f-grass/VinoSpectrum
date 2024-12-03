import os
from read_tiff import read_tiff
from PIL import Image
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt


def show_tgi_idx():
    folder = 'data/90grad_nah_TIFF/'
    image_lst = os.listdir(folder)

    image_lst.sort()

    red_idx = 13
    green_idx = 7
    blue_idx = 1


    for img_name in image_lst[20:25]:
        img = read_tiff(path=folder + img_name)
        idx_arr = img[:,:,green_idx] - 0.39 * img[:,:,red_idx] - 0.61 * img[:,:,blue_idx]

        fig = px.imshow(idx_arr)
        fig.show()

def calc_tgi_from_combined():
    img = np.array(Image.open("data/90_degrees_combined_rgb_cropped.jpg"))
    idx_arr = img[:, :, 1] - 0.39 * img[:, :, 0] - 0.61 * img[:, :, 2]


    fig = plt.imshow(idx_arr, cmap='nipy_spectral')
    cbar = plt.colorbar(fig)
    plt.axis('off')
    plt.savefig( 'data/90_degrees_application_map.png', dpi=300)
    plt.show()

if __name__ == '__main__':
    calc_tgi_from_combined()