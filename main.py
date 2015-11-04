import homography

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy import misc

#Sample image
image = misc.lena()
param = (1, 2, 3)

#image_out = image_warp(image,param)

def image_warp(image, param):
    H = homography.homographyMatrix(param)
#	H_inv = numpy.linalg.inv(H)
#	result = backward_warping(image, H_inv)

image_out = image_warp(image, param)    
