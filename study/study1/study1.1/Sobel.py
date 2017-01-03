# coding=utf-8

import pylab as plb
from numpy import *
from scipy.ndimage import filters

im = array(plb.imread('test1.png'))
# Sobel 导数滤波器
imx = zeros(im.shape)
filters.sobel(im,1,imx)
imy = zeros(im.shape)
filters.sobel(im,0,imy)
magnitude = sqrt(imx**2+imy**2)

plb.imshow(imy)
plb.show()