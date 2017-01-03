#coding=utf-8
#
# 图片的读取和显示
from PIL import Image
import pylab as plb
#读图1
img = Image.open('test1.jpg')
#使用默认图片打开软件打开
img.show()

#灰度化
grayimg = img.convert('L')
#注意：每次只能显示一张图片，需要关闭上一张
grayimg.show()
#使用python专用的打开图片的软件
plb.imshow(img)
#防止一闪而过
plb.show()