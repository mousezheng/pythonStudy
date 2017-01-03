#coding=utf-8
#
# 速度是相当慢，运行需谨慎
#
from PIL import Image
from pylab import *
# 读取图像到数组中
im = array(Image.open('test.png').convert('L'))
# 新建一个图像
figure()
# 不使用颜色信息
gray()
# 在原点的左上角显示轮廓图像
contour(im, origin='image')
figure()
# 显示出条形图，128根
hist(im,128)
show()
axis('equal')
axis('off')