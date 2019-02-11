import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,10,1)
fig=plt.figure()
ax=fig.add_subplot(221)
plt.plot(x,2*x,label='example1')
ax.grid(color='g')
plt.legend()
plt.show()


ax1=fig.add_subplot(222)
plt.plot(x,2*x)
ax1.grid(color='r')
plt.show()