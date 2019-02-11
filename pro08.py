#coding=utf-8
import  numpy as np
import matplotlib.pyplot as plt
print '正弦函数'
n=np.pi
x=np.arange(0,2*n,0.01)
y=np.sin(x)
# plt.title("正弦函数")
plt.plot(x,y)

plt.show()