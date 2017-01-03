#coding=utf-8
from scipy.misc import imresize
#import graphcut
from PIL import Image
from numpy import *
from pylab import *
def create_msr_labels(m,lasso=False):
    #""" 从用户的注释中创建用于训练的标记矩阵"""
    labels = zeros(im.shape[:2])
    # 背景
    labels[m==0] = -1
    labels[m==64] = -1
    # 前景
    if lasso:
        labels[m==255] = 1
    else:
        labels[m==128] = 1
    return labels