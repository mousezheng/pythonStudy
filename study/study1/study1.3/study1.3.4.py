#coding=utf-8
#直方图的均衡化
'''
直方图均衡化是指将一幅
图像的灰度直方图变平，使变换后的图像中每个灰度值的分布概率都相同。在对图
像做进一步处理之前，直方图均衡化通常是对图像灰度值进行归一化的一个非常好
的方法，并且可以增强图像的对比度。
在这种情况下，直方图均衡化的变换函数是图像中像素值的累积分布函数（cumulative
distribution function，简写为cdf，将像素值的范围映射到目标范围的归一化操作）。
'''

def histeq(im,nbr_bins=256):
# 对一幅灰度图像进行直方图均衡化
    # 计算图像的直方图
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum() # cumulative distribution function
    cdf = 255 * cdf / cdf[-1] # 归一化
    # 使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape)

from PIL import Image
from numpy import *
import pylab as plb
img = Image.open('test1.jpg')
im = array(Image.open('test1.jpg').convert('L'),'f')
img1 = Image.fromarray(im)
#plb.figure(1)
#plb.imshow(im)
img1.show()
#plb.figure(3)
#plb.imshow(histeq(im))
img1 = Image.fromarray(histeq(im))
img1.show()
'''
plb.figure(2)
plb.imshow(im)
#看起来更均匀，色彩变更变大了
#直方图均衡化后图像的对比度增强了，原先图像灰色区域的细节变得清晰。
pil_im = Image.fromarray(uint8(im))
plb.figure(4)
plb.imshow(pil_im)
'''
plb.show()