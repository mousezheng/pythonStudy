#coding=utf-8
import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('test17010302.png')
h = np.zeros((256,256,3)) #创建用于绘制直方图的全0图像

bins = np.arange(256).reshape(256,1) #直方图中各bin的顶点位置
color = [ (255,0,0),(0,255,0),(0,0,255) ] #BGR三种颜色
for ch, col in enumerate(color):
    originHist = cv2.calcHist([img],[ch],None,[256],[0,256])
    cv2.normalize(originHist, originHist,0,255*0.9,cv2.NORM_MINMAX)
    hist=np.int32(np.around(originHist))
    pts = np.column_stack((bins,hist))
    cv2.polylines(h,[pts],False,col)

h=np.flipud(h)

cv2.imshow('colorhist',h)

#plt.hist(h,range(0,255))
#plt.show()
cv2.waitKey(0)