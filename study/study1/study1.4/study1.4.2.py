#coding=utf-8
#
# 图像倒数

from PIL import Image
from numpy import *
from scipy.ndimage import filters
import pylab as plb
im = array(Image.open('test1.jpg').convert('L'))
# Sobel 导数滤波器
imx = zeros(im.shape)   #对x求导
img2 = Image.fromarray(imx)

#img2.show()
filters.sobel(im,1,imx)
imy = zeros(im.shape)   #对y求导
#img2 = Image.fromarray(imy)

#img2.show()
filters.sobel(im,0,imy)
#和，，将x y求导结果合一  求反相将边置为黑色
magnitude = 255-sqrt(imx**2+imy**2)
#img2 = Image.fromarray(magnitude)
plb.gray()
plb.imshow(magnitude)
plb.show()