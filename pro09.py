#coding=utf:8
import numpy as np
import matplotlib.pyplot as plt

print 'subplot 使用方法 在一个页面中画4个小图'
x=np.arange(1,100)
fig=plt.figure()
ax1=fig.add_subplot(221)
ax1.plot(x,x)

ax2=fig.add_subplot(222)
ax2.plot(x,-x)

ax3=fig.add_subplot(223)
ax3.plot(x,x*x)

ax4=fig.add_subplot(224)
ax4.plot(x,np.log(x))
