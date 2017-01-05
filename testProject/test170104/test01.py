#coding=utf-8
#
# 看pylab中imshow的显示，发现棒材端面和其他地方色彩上差异还是较大
# 特殊色彩提取太过死板，现采用聚类的思想，对像素段区域进行分类（这样不仅保证
# 需要提取的特殊色彩在一类中，同时还很好的避免了特殊色彩的变化）
#
#


import matplotlib.pylab as plb
from PIL import Image
import numpy as np
import cv2
#读图，将图片转化为数组
imrgb = Image.open('test17010301.png')
im = imrgb.split()
#提取 RGB
#r = imrgb[0]
#g = imrgb[1]
#b = imrgb[2]
#print r.max()
#print imrgb.r
im[0].show()
im[1].show()
im[2].show()
#r,g,b = np.split(imrgb,3)
imgx2 = imrgb

#显示
plb.imshow(imgx2)

#暂停显示
plb.show()

'''
for i in range(10):
    print imgx2[70+i,70+i],imgx2[100+i,100+i]

print imgx2.max(),imgx2.min()
'''