# coding=utf-8
#from PIL import Image

#pip_im = Image.open('')

import pylab as plb
import numpy as np
import cv2
#设置点
x = [0,500]
y = [0,500]

x1 = [10,10,210,210,410,410]
y1 = [10,110,110,310,310,410]


#使用红色形状标记绘制这些点，作为坐标轴的左下和右上
'''
#plb.plot(x,y,'r*')
# 绘制六边形，
plb.plot([110,310],[10,10])
#带有圆圈标记的绿线
plb.plot([110,10],[10,210],'go-')
plb.plot([10,110],[210,410])
#带有正方形标记的黑色点线
plb.plot([110,310],[410,410],'ks:')
plb.plot([310,410],[410,210])
#带红色星状虚线
plb.plot([410,310],[210,10],'r*--')

# 添加标题，显示绘制的图像
plb.title('six')
'''

#关闭坐标轴
'''
#plb.axis('off')
#新建一个图像
plb.figure()
#不使用颜色信息
gray()
#对齐
#plb.axis('equal')
'''

#绘制轮廓及其直方图
'''
#  读图
img = plb.imread('test1.png')
#显示
plb.imshow(img)

#新建窗口
plb.figure()
plb.gray()

plb.hist(img.flatten(),20)
'''
x = [100,100,400,400]
y = [200,500,200,500]
plb.plot(x,y) # 默认为蓝色实线
plb.plot(x,y,'r*') # 红色星状标记
plb.plot(x,y,'go-') # 带有圆圈标记的绿线
plb.plot(x,y,'ks:') # 带有正方形标记的黑色虚线
#交互式1，，得到用户点击的坐标
#  读图
img = plb.imread('test.png')

plb.imshow(img)
#plb.figure()
plb.plot(100,100,'*')
#x = plb.ginput(3)


#plb.axis('off')

print x
plb.show()
