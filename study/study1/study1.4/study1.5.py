#coding=utf-8
#
# 图像去噪小案例


'''
使用A. Chambolle（2005）在公式（11）中的计算步骤实现Rudin-Osher-Fatemi（ROF）去噪模型
输入：含有噪声的输入图像（灰度图像）、U 的初始值、TV 正则项权值、步长、停业条件
输出：去噪和去除纹理后的图像、纹理残留
'''
from numpy import *
def denoise(im,U_init,tolerance=0.1,tau=0.125,tv_weight=100):
    m,n = im.shape # 噪声图像的大小
    # 初始化
    U = U_init
    Px = im # 对偶域的x 分量
    Py = im # 对偶域的y 分量
    error = 1
    while (error > tolerance):
        Uold = U
        # 原始变量的梯度
        GradUx = roll(U,-1,axis=1)-U # 变量U 梯度的x 分量
        GradUy = roll(U,-1,axis=0)-U # 变量U 梯度的y 分量
        # 更新对偶变量
        PxNew = Px + (tau/tv_weight)*GradUx
        PyNew = Py + (tau/tv_weight)*GradUy
        NormNew = maximum(1,sqrt(PxNew**2+PyNew**2))
        Px = PxNew/NormNew # 更新x 分量（对偶）
        Py = PyNew/NormNew # 更新y 分量（对偶）
        # 更新原始变量
        RxPx = roll(Px,1,axis=1) # 对x 分量进行向右x 轴平移
        RyPy = roll(Py,1,axis=0) # 对y 分量进行向右y 轴平移
        DivP = (Px-RxPx)+(Py-RyPy) # 对偶域的散度
        U = im + tv_weight*DivP # 更新原始变量
        # 更新误差
        error = linalg.norm(U-Uold)/sqrt(n*m);
    return U,im-U # 去噪后的图像和纹理残余


from PIL import Image
from pylab import *
import matplotlib.pyplot as plt
im = array(Image.open('test3.jpg').convert('L'))
U,T = denoise(im,im)
gray()
plt.subplot(121)
imshow(im)
plt.subplot(122)
imshow(U)
axis('equal')
axis('off')
show()