#coding=utf-8
#
# 在图像间寻找对应点
'''
Harris 角点检测器仅仅能够检测出图像中的兴趣点，但是没有给出通过比较图像间
的兴趣点来寻找匹配角点的方法。我们需要在每个点上加入描述子信息，并给出一
个比较这些描述子的方法。
兴趣点描述子是分配给兴趣点的一个向量，描述该点附近的图像的表观信息。描述
子越好，寻找到的对应点越好。我们用对应点或者点的对应来描述相同物体和场景
点在不同图像上形成的像素点。
'''

from PIL import Image
from numpy import *
from pylab import *
import harris




im1 = array(Image.open('test1.jpg').convert('L'))
im2 = array(Image.open('test1.jpg').convert('L'))
wid = 5
harrisim = harris.compute_harris_response(im1,wid)
filtered_coords1 = harris.get_harris_points(harrisim,wid+1)
d1 = harris.get_descriptors(im1,filtered_coords1,wid)
harrisim = harris.compute_harris_response(im2,wid)
filtered_coords2 = harris.get_harris_points(harrisim,wid+1)
d2 = harris.get_descriptors(im2,filtered_coords2,wid)
print 'starting matching'

matches = harris.match_twosided(d1,d2,2)
figure()
gray()
harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches)
show()
