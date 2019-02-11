#coding:utf-8
import numpy as np
import  matplotlib.pyplot as plt

x=np.arange(1,100,1)
y1=np.log(x)
y2=x*x

fig=plt.figure()
ax1=fig.add_subplot(111)
ax1.plot(x,y1)
ax1.set_ylabel('Y1')   #设定 y轴的label
ax2=ax1.twinx()     #通过ax1生成一个相同的ax2   也就是说在生成一个y轴
ax2.plot(x,y2,'r')     #设定第二个y轴
ax2.set_ylabel('Y2')    #设定y2的标签
ax1.set_xlabel('compare Y1 and Y2')     #设定x轴的标签
plt.show()