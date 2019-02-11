#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

print '散点图  股票散点图分布'
open,close=np.loadtxt('0001.csv',delimiter=',',skiprows=0,usecols=(4,6),unpack=True)
change=close-open         #收盘价-开盘价=change  算出每天的差值
yesterday=change[:-1]     #取前18天的记录（一共19天记录）
today=change[1:]          #取后18天的记录（一共19天记录）

plt.scatter(yesterday,today,s=30,c='r',marker='o',alpha=0.2)    #alpha 透明度 0.1开始到1   0.1最浅
plt.show()
