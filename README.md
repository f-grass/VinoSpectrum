# VinoSpectrum

## Data 

- image shape (2676, 2588)
- number of bands: 14
- wavelenght
    - {0:430nm} 
    - {1:450nm} --> blue
    - {2:405nm}
    - {3:490nm}
    - {4:525nm}
    - {5:570nm}
    - {6:550nm} 
    - {7:560nm} --> green
    - {8:850nm}
    - {9:630nm}
    - {10:710nm} 
    - {11:650nm} 
    - {12:735nm}
    - {13:685nm} --> red

## Steps 

- **Step 1:**
  - We try to combine 47 degrees images with python library OpenCV  
  - We recognize problems with multiple open source tools to combine the images

- **Step 2:** We switch our data source to the 90 degrees images and combine the images with OpenCV stitching method

- **Step 3:** We transform (crop) the image to map the vineyard rows between the picture and the map 

- **Step 4:** We transform (crop) the image to map the vineyard rows

- **Step 5:** 
    - We calculate Triangular Greenness Index (TGI)
    - TGI estimates chlorophyll concentration in leaves
    - We use data from red (450nm), green (560nm) and blue (685nm) band to calculate TGI
    - TGI = GREEN - 0.39 * RED - 0.61 * BLUE

- **Step 6:**
    - We export image with colormap nipy_spectral from matplotlib
    - We map the exported image with QGIS via a 4 Point alignment to the gps map

## Result

- We learn a lot
- We had fun
- We figure out that the geographical reference while merging non-orthogonal captured images is a challenge and represents a potential for future research