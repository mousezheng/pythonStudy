#coding=utf-8
#
# NumPy小案例
#输出六张图，分别是
# 原图的灰度图，反相处理结果，像素求平方处理结果
# 原图缩放一倍，图片直方图均衡化，图像平均

# 对一幅灰度图像进行直方图均衡化
def histeq(im,nbr_bins=256):
    # 计算图像的直方图
    imhist,bins = histogram(im.flatten(),nbr_bins,normed=True)
    cdf = imhist.cumsum() # cumulative distribution function
    cdf = 255 * cdf / cdf[-1] # 归一化
    # 使用累积分布函数的线性插值，计算新的像素值
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape)

#计算图像列表的平均图像
def compute_average(img):
# 打开第一幅图像，将其存储在浮点型数组中
    averageim = array(img, 'f')
    averageim /= len(img)
    # 返回uint8 类型的平均图像
    return array(averageim, 'uint8')

from PIL import Image
from numpy import *
import pylab as plb
import matplotlib.pyplot as plt

im = array(Image.open('test1.jpg').convert('L'))
# 对图像进行反相处理
im2 = 255 - im
# 对图像像素值求平方后得到的图像
im4 = 255.0 * (im/255.0)**2

im = Image.fromarray(im)

plt.subplot(231,im)
plt.subplot(232,im2)
plt.subplot(233,im4)
plt.subplot(234,im.resize((im.size[0]/2,im.size[1]/2)))
plt.subplot(235,average(im))
plt.subplot(236,histeq(im))
plb.show()#暂停程序


