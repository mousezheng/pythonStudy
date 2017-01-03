#coding=utf-8
#
# 简单的一个小测试

from PIL import Image
import matplotlib.pyplot as plt
from pylab import *
from numpy import *
from scipy.cluster.vq import *
from scipy.misc import imresize

def get_class_img(im,steps,class_num):
    steps = steps # 图像被划分成steps×steps 的区域
    dx = im.shape[0] / steps
    dy = im.shape[1] / steps
    # 计算每个区域的颜色特征
    features = []
    for x in range(steps):
        for y in range(steps):
            R = mean(im[x*dx:(x+1)*dx,y*dy:(y+1)*dy,0])
            G = mean(im[x*dx:(x+1)*dx,y*dy:(y+1)*dy,1])
            B = mean(im[x*dx:(x+1)*dx,y*dy:(y+1)*dy,2])
            features.append([R,G,B])
    features = array(features,'f') # 变为数组
    # 聚类
    centroids,variance = kmeans(features,class_num)
    code,distance = vq(features,centroids)
    # 用聚类标记创建图像
    codeim = code.reshape(steps,steps)
    codeim = imresize(codeim,im.shape[:2],interp='nearest')

    return codeim

def get_class_img2(features,steps,class_num):
    steps = steps
     # 聚类
    centroids,variance = kmeans(features,class_num)
    code,distance = vq(features,centroids)
    # 用聚类标记创建图像
    codeim = code.reshape(100,100)
    codeim = imresize(codeim,im.shape[:2],interp='nearest')

    return codeim

'''
好奇怪啊，为什么聚类后的图片变小了，左右小了三分之一
--郑思林 17.1.2
已经解决，原来是步长问题，可能是python为了保证计算速度，自动将大小改了
'''
img = Image.open('section.1.1.jpg')
#print img.size
#plt.gray()
plt.subplot(221)
plt.title('original')
plt.imshow(img) #原图
plt.subplot(222)
plt.title('gray')
plt.imshow(img.convert('L'))    #灰度图
plt.subplot(223)
plt.title('class1')
array_img = array(img)
im = get_class_img(array_img,50,4)    #1
plt.imshow(im)

plt.subplot(224)
plt.title('class2')
#im2 = get_class_img2(im,100,2)          #2
#array_img = array(im2)
#plt.figure(2)
plt.imshow(img)
#print img.size
#size = ginput(4)
print size
plt.show()

im = Image.fromarray(im)
#im.save('save.jpg')