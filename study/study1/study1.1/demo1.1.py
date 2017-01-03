#coding=utf-8
#使用PIL类库中常见的方法制作一个小案例
#
#读取一张图片，将图片中一部分进行旋转，
#然后整体旋转，最后显示并存储在C盘中
#

from PIL import Image
import pylab as plb
import os

#存储图片
def saveImg(img,type):

    try:
        img.save('C:/test/testr.' + type)
    except IOError:
        return False
    return True




img = Image.open('test1.jpg')
#转化为二值图像
grayImg = img.convert('L')
'''
#显示 默认图片浏览器
grayImg.show()
'''
#设置缩略图
# imgchange1 = grayImg.thumbnail((100,100))
box = (20,20,130,130)
imgchange2 = img.crop(box)
imgchange2 = imgchange2.transpose(Image.ROTATE_180)
grayImg.paste(imgchange2,box)#注意返回值不是图片或者矩阵类型
#显示为灰色 注意：不加的话会显示伪彩色，一种特殊的彩色
plb.gray()
#显示 python专用图片浏览器
plb.figure('demo')  #设置窗口信息
plb.title('demo1')
plb.imshow(grayImg)
#防止一闪而过
plb.show()
if saveImg(grayImg,'jpg'):
    print 'ok'

