#!/usr/bin/env python

'''
Stitching sample
================

Show how to use Stitcher API from python in a simple way to stitch panoramas
or scans.
'''

# Python 2/3 compatibility
from __future__ import print_function

import os

import numpy as np
import cv2 as cv

import argparse
import sys

from read_tiff import read_tiff

modes = (cv.Stitcher_PANORAMA, cv.Stitcher_SCANS)

parser = argparse.ArgumentParser(prog='stitching.py', description='Stitching sample.')
parser.add_argument('--mode',
                    type=int, choices=modes, default=cv.Stitcher_PANORAMA,
                    help='Determines configuration of stitcher. The default is `PANORAMA` (%d), '
                         'mode suitable for creating photo panoramas. Option `SCANS` (%d) is suitable '
                         'for stitching materials under affine transformation, such as scans.' % modes)

__doc__ += '\n' + parser.format_help()

red_idx = 13
green_idx = 7
blue_idx = 1

def main():
    args = parser.parse_args()

    folder = 'data/90grad_nah_TIFF/'
    image_lst = os.listdir(folder)

    image_lst.sort()

    imgs = []
    for img_name in image_lst:

        img = read_tiff(path=folder + img_name)[:,:,[red_idx, green_idx, blue_idx]]

        imgs.append(img)

    # ![stitching]
    stitcher = cv.Stitcher.create(args.mode)
    status, pano = stitcher.stitch(imgs)

    if status != cv.Stitcher_OK:
        print("Can't stitch images, error code = %d" % status)
        print("can not process images with index ")
    # ![stitching]
    else:
        cv.imwrite(f"data/example/output_stitching.jpg", pano)

        print('Done')


if __name__ == '__main__':
    main()
    cv.destroyAllWindows()

# python src/stitching.py --mode 1