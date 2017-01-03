#coding=utf-8
#
# 形态学：对象计数

'''
形态学（或数学形态学）是度量和分析基本形状的图像处理方法的基本框架与集合。
形态学通常用于处理二值图像，但是也能够用于灰度图像。二值图像是指图像的每
个像素只能取两个值，通常是0 和1。二值图像通常是，在计算物体的数目，或者
度量其大小时，对一幅图像进行阈值化后的结果。你可以从http://en.wikipedia.org/
wiki/Mathematical_morphology 大体了解形态学及其处理图像的方式。
'''
from PIL import Image
from numpy import *
from scipy.ndimage import measurements,morphology
import pylab as plb
# 载入图像，然后使用阈值化操作，以保证处理的图像为二值图像
im = array(Image.open('test3.png').convert('L'))
im = 1*(im<225)#暂时还不太清楚其所以然，0.0
labels, nbr_objects = measurements.label(im)
print "Number of objects:", nbr_objects


'''
imgLabels = Image.fromarray(labels)
imgLabels.show()
'''
#形态学的开操作，iterations=5进行五次
im_open = morphology.binary_opening(im,ones((2,2)),iterations=5)
labels_open, nbr_objects_open = measurements.label(im_open)
print "Number of objects:", nbr_objects_open
plb.gray()

plb.title('counter = ' + str(nbr_objects_open))
plb.imshow(labels_open)
plb.show()
