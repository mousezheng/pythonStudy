#coding=utf-8
#
#学习NumPy测试
#

import Image
import numpy as np

arrayIm = np.array(Image.open('test1.jpg'))
#直接访问其 i = 12,j = 12,中第二通道的值
# print arrayIm[12,12,2]
