import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,10)
plt.plot(x,2*x)
ax=plt.gca()

ax.locator_params('y',nbins=20)
plt.show()