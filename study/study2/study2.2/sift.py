#coding=utf-8
#
#SIFT 尺寸不变特征变换

'''
SIFT 特征包括兴趣点检测器和描述
子。SIFT 描述子具有非常强的稳健性，这在很大程度上也是SIFT 特征能够成功和
流行的主要原因。自从SIFT 特征的出现，许多其他本质上使用相同描述子的方法
也相继出现。现在，SIFT 描述符经常和许多不同的兴趣点检测器相结合使用（有些
情况下是区域检测器），有时甚至在整幅图像上密集地使用。SIFT 特征对于尺度、
旋转和亮度都具有不变性，因此，它可以用于三维视角和噪声的可靠匹配。你可以
在http://en.wikipedia.org/wiki/Scale-invariant_feature_transform 获得SIFT 特征的简
要介绍。
'''
from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters
import os
def process_image(imagename,resultname,params="--edge-thresh 10 --peak-thresh 5"):
#""" 处理一幅图像，然后将结果保存在文件中"""
    if imagename[-3:] != 'pgm':
        # 创建一个pgm 文件
        im = Image.open(imagename).convert('L')
        im.save('tmp.pgm')
        imagename = 'tmp.pgm'
    cmmd = str("sift "+imagename+" --output="+resultname+
         " "+params)
    os.system(cmmd)
    print 'processed', imagename, 'to', resultname


def read_features_from_file(filename):
# 读取特征属性值，然后将其以矩阵的形式返回
    f = loadtxt(filename)
    return f[:,:4],f[:,4:] # 特征位置，描述子

def write_features_to_file(filename,locs,desc):
    # 将特征位置和描述子保存到文件中
    savetxt(filename,hstack((locs,desc)))

def plot_features(im,locs,circle=False):
    """ 显示带有特征的图像
    输入：im（数组图像），locs（每个特征的行、列、尺度和朝向）"""
    def draw_circle(c,r):
        t = arange(0,1.01,.01)*2*pi
        x = r*cos(t) + c[0]
        y = r*sin(t) + c[1]
        plot(x,y,'b',linewidth=2)
        imshow(im)
    if circle:
        for p in locs:
            draw_circle(p[:2],p[2])
    else:
        plot(locs[:,0],locs[:,1],'ob')
    axis('off')

def match(desc1,desc2):
    """ 对于第一幅图像中的每个描述子，选取其在第二幅图像中的匹配
    输入：desc1（第一幅图像中的描述子），desc2（第二幅图像中的描述子）"""
    desc1 = array([d/linalg.norm(d) for d in desc1])
    desc2 = array([d/linalg.norm(d) for d in desc2])
    dist_ratio = 0.6
    desc1_size = desc1.shape
    matchscores = zeros((desc1_size[0],1),'int')
    desc2t = desc2.T # 预先计算矩阵转置
    for i in range(desc1_size[0]):
        dotprods = dot(desc1[i,:],desc2t) # 向量点乘
        dotprods = 0.9999*dotprods
        # 反余弦和反排序，返回第二幅图像中特征的索引
        indx = argsort(arccos(dotprods))
        # 检查最近邻的角度是否小于dist_ratio 乘以第二近邻的角度
        if arccos(dotprods)[indx[0]] < dist_ratio * arccos(dotprods)[indx[1]]:
            matchscores[i] = int(indx[0])
    return matchscores

def match_twosided(desc1,desc2):
    """ 双向对称版本的match()"""
    matches_12 = match(desc1,desc2)
    matches_21 = match(desc2,desc1)
    ndx_12 = matches_12.nonzero()[0]
    # 去除不对称的匹配
    for n in ndx_12:
        if matches_21[int(matches_12[n])] != n:
            matches_12[n] = 0
    return matches_12