#coding=utf-8
#
#Scipy聚类包
from PIL import Image
from numpy import *
from pylab import *
from scipy.cluster.vq import *
class1 = 1.5 * randn(100,2)
class2 = randn(100,2) + array([5,5])
#生成两类二维正态分布数据。
features = vstack((class1,class2))
#用k=2 对这些数据进行聚类
centroids,variance = kmeans(features,2)
#用SciPy 包中的矢量量化函数对每个数据点进行归类：
code,distance = vq(features,centroids)

#画出这些数据点及最终的聚类中心
figure()
ndx = where(code==0)[0]
plot(features[ndx,0],features[ndx,1],'*')
ndx = where(code==1)[0]
plot(features[ndx,0],features[ndx,1],'r.')
plot(centroids[:,0],centroids[:,1],'go')
axis('off')
show()
'''
结果：一个对二维数据用K-means 进行聚类的示例。类中心标记为绿色大圆环，预测出的
类分别标记为蓝色星号和红色点。
'''
