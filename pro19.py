#coding =utf-8
import matplotlib.pyplot as plt
import numpy as np

# r=np.arange(1,6,1)
r=np.empty(9)      #empty  是创建一个大小为9的空数组
r.fill(5)          #fill   是填充这个数组全部都是数字  5

# pi=[0,np.pi/2,np.pi,3*np.pi/2,2*np.pi]
pi=[0,np.pi/4,np.pi/2,3*np.pi/4,np.pi,5*np.pi/4,3*np.pi/2,7*np.pi/4,2*np.pi]     #8边型的图形
ax=plt.subplot(111,projection='polar')
ax.plot(pi,r,color='r',linewidth='5')
plt.show()