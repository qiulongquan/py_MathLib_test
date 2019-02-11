#coding=utf:8
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,10,1)
y=x*x

plt.plot(x,y)
plt.text(5,5,"this is a comment",family='fantast',size=20,color='g',style='italic',weight='black',alpha=0.3)
#内容是中文还是会出现问题。用英文就可以了
plt.show()