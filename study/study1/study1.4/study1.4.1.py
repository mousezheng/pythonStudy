#coding=utf-8
#
# 图像模糊

#高斯模糊
'''
高斯模糊通常是其他图像处理操作的一部分，比如图像插值操作、兴趣点计算以及
很多其他应用。
'''
from PIL import Image
from numpy import *
import pylab as plb
from scipy.ndimage import filters
import matplotlib.pyplot as plt
im = array(Image.open('test1.jpg').convert('L'))
#随着第二个参数的增大模糊程度也逐渐增大
plb.gray()
for i in range(4):
    im2 = filters.gaussian_filter(im,i*2)
    plt.subplot(2,2,i)
    plt.title(i)
    plb.imshow(im2)
plb.show()
