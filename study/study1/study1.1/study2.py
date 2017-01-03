#coding=utf-8

import pylab as plb
import numpy as np

img = plb.imread('test.png')
#plb.imshow(img)
#将图片转换为数组
Im = plb.array(img)
print Im.shape,Im.dtype

#对图像反相处理
im2 = 255 - Im

#将图像像素值变换到100...200区间
im3 = (100.0/255) * Im + 100

#对图像像素求平方后得到图像
im4 = 255.0 * (Im/255.0)**2

#img2 = plb.
plb.imshow(im2)
plb.title('test')
plb.show()