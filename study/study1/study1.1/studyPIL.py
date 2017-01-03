#coding=utf-8
#用于记录学习PIL的测试用例
import Image
import pylab as plb
pil_im = Image.open('test2.jpg')

# 灰度化

pil_im = pil_im.convert('L')
plb.imshow(pil_im)
plb.show()
# 另存图片
'''
from PIL import Image
import os
filelist = ['F:/myPythonWork/PIL/test1.jpg'];
for infile in filelist:
    outfile = 'outfile' + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print "cannot convert", infile
'''

# 截取 按照 左上右下 的方式截取图片的一部分，

box = (20,20,150,150)
region = pil_im.crop(box)
#将截取的图片旋转
region = region.transpose(Image.ROTATE_180)
#将图片放回原图的原处
pil_im.paste(region,box)
plb.imshow(pil_im)
plb.show()


# 修改图片的尺寸
'''
pil_im = pil_im.resize((700,700))
# 旋转图片
pil_im = pil_im.rotate(45)
pil_im.show()
'''

