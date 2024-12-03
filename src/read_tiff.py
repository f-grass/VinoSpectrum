from PIL import Image
import numpy as np

def read_tiff(path):
    """
    Read tiff file with multiple bands / images and add them at third dimension.

    Args:
        path: path to image

    Returns:
        array: concatenated images at third dimension

    """

    # read image
    img = Image.open(path)

    # init list for images
    images = []

    # read each image and add it to images list
    for i in range(img.n_frames):
        img.seek(i)
        images.append(np.expand_dims(np.array(img), axis=-1))

    # concatenate image
    array = np.concatenate(images, axis=-1)

    return array

if __name__ == '__main__':
    import plotly.express as px
    from spectral import *

    img_arr = read_tiff('data/47grad_nah_TIFF/9327.TIFF')
    img = []

    img.append(img_arr[:,:,[11]])
    img.append(img_arr[:,:,[6]])
    img.append(img_arr[:,:,[0]])
    save_rgb('rgb.jpg', img_arr, [11, 6, 0])


    fig = px.imshow(np.concatenate(img, axis=-1))
    fig.show()
