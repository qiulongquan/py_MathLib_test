import numpy as np
import matplotlib.pyplot as plt

x=np.random.randn(200)
y=x+np.random.randn(200)*0.5

fig=plt.figure()
ax=fig.add_subplot(111)
# ax.set_xlim([])
ax.set_xticks([-1,3])
plt.scatter(x,y)
plt.show()