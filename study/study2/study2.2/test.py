#coding=utf-8
import sift
from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters

imname = 'test1.jpg'
im1 = array(Image.open(imname).convert('L'))
sift.process_image(imname,'test1.sift')
l1,d1 = sift.read_features_from_file('test1.sift')
figure()
gray()
sift.plot_features(im1,l1,circle=True)
show()