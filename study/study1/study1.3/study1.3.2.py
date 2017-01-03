#!/usr/bin/env python
#coding=utf-8
from PIL import Image
from numpy import *
import pylab as plb
im = array(Image.open('test1.jpg').convert('L'))
# 对图像进行反相处理
im2 = 255 - im
# 将图像像素值变换到100...200 区间
im3 = (100.0/255) * im + 100
# 对图像像素值求平方后得到的图像
im4 = 255.0 * (im/255.0)**2


img1 = Image.fromarray(im2)
img2 = Image.fromarray(im3)
img3 = Image.fromarray(im4)
#   一次只能显示一张图片不是很方面
# img1.show()
#img2.show()
#img3.show()
plb.gray()
plb.figure(1)
#plb.title("图像处理反相结果")
plb.imshow(img1)
plb.figure(2)
#plb.title('图像处理将图像像素值变换到100...200 区间')
plb.imshow(img2)
plb.figure(3)
#plb.title("图像处理对图像像素值求平方后得到的图像")
plb.imshow(img3)
plb.show()#暂停程序

