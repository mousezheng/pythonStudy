#coding=utf-8
#
#Scipy聚类包
from PIL import Image
from pylab import *
from numpy import *
from scipy.cluster.vq import *
from scipy.misc import imresize

steps = 150 # 图像被划分成steps×steps 的区域
im = array(Image.open('2.jpg'))

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
centroids,variance = kmeans(features,4)
code,distance = vq(features,centroids)
# 用聚类标记创建图像
codeim = code.reshape(steps,steps)
codeim = imresize(codeim,im.shape[:2],interp='nearest')

figure()
gray()
imshow(im)
figure()
imshow(codeim)
show()