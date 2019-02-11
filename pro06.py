#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

print '直方图'
x=np.random.randn(1000)+2
y=np.random.randn(1000)+4
plt.hist2d(x,y,bins=100)     #2-D 直方图
plt.show()
