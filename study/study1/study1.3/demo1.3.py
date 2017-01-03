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
    averageim = array(img[0], 'f')
    for im in img:
        averageim += array(im)
    averageim /= len(img)
    # 返回uint8 类型的平均图像
    return array(averageim, 'uint8')

from PIL import Image
from numpy import *
import pylab as plb
import matplotlib.pyplot as plt
#求平均的图片必须大小相同
img1 = array(Image.open('test1.jpg'))
img1.resize((300,300))
img2 = array(Image.open('test2.jpg'))
img2.resize((300,300))
img3 = array(Image.open('test3.jpg'))
img3.resize((300,300))
im = array(Image.open('test1.jpg').convert('L'),'f')
# 对图像进行反相处理
im2 = 255 - im
# 对图像像素值求平方后得到的图像
im4 = 255.0 * (im/255.0)**2

#im = Image.fromarray(im)
plb.gray()
plt.subplot(231)
plt.imshow(im)      #显示灰度图
plt.subplot(232)
plt.imshow(im2)     #显示反相图
plt.subplot(233)
plt.imshow(im4)     #显示平方后的图像

plt.subplot(235)
img5 = Image.fromarray(histeq(im))
plt.imshow(img5)    #显示均衡化的图像
plt.subplot(236)
img = (img1,img2,img3)
img6 = Image.fromarray(compute_average(img))
plt.imshow(img6)    #显示求平均后的图像

im = Image.fromarray(im)
plt.subplot(234)
#resize()需要图片对象进行调用
#显示缩小的图片
plt.imshow(im.resize((im.size[0]/2,im.size[1]/2)))
plb.show()#暂停程序


