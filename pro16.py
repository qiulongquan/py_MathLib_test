import numpy as np
import matplotlib.pyplot as plt

count=1000
N=np.random.rand(count)
x=np.random.rand(count)
y=np.random.rand(count)
color=np.random.rand(count)
area=np.pi*(20*np.random.rand(count)**2)

plt.scatter(x,y,s=area,c=color,alpha=0.5)
plt.show()