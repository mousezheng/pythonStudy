#coding=utf-8
#
#Matplotlab学习案例
#
#左右两幅图，
#左边的图用MatPlotlib绘制一个六边形
#右边的图用Matplotlib绘制一些随机的点和线
#用户可以使用鼠标点击随机点中的三个，在控制台输出点击的坐标
#

import matplotlib.pyplot as plt
import pylab as plb
import random
#绘制左图
plt.subplot(121,axisbg='1')
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

#绘制右图
plt.subplot(122,axisbg='0')
n=3
while n>0:
    plb.plot([random.randint(20,100),random.randint(50,200)]
             ,[random.randint(20,100),random.randint(50,200)],'wo-')
    n = n-1


#接收三个随机点
x = plb.ginput(3)
for temp in x:
    print temp
#关闭坐标轴
# plb.axis('off')
plt.show()