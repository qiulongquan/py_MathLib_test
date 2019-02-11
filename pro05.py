#coding:utf-8
import matplotlib.pyplot as plt
import numpy as np

print '柱状图 横向柱状图 叠层柱状图 并列柱状图'
x=[10,20,15,25,30]
y=[15,25,20,30,35]
index=np.arange(5)
# plt.bar(left=index,height=x,width=0.5,color='red')   #垂直柱状图
# plt.bar(left=0,bottom=index,height=0.5,width=x,color='red',orientation='horizontal')  #横向柱状图
# plt.barh(left=0,bottom=index,height=0.5,width=x,color='red')     #横向柱状图
plt.bar(left=index,height=x,color='red',width=0.3)      #并列柱状图
# plt.bar(left=index+0.3,height=y,color='blue',width=0.3)   #并列柱状图
plt.bar(left=index,height=y,bottom=x,color='green',width=0.3)      #层叠柱状图
plt.show()