#coding=utf-8
#
# 使用python对文件夹下面的图片进行读取
#
import os

def getAllImages(path):
   return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')|f.endswith('.txt')]

print getAllImages("D:\\test")