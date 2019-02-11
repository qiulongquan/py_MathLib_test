#coding:utf-8
import matplotlib.pyplot as plt
#饼状图  阴影饼状图
labels='a','b','c','d','d'
faces=[10,20,30,30,10]

explode=[0,0,0,0.2,0.2]
plt.axes(aspect=1)
plt.pie(x=faces,labels=labels,autopct='%.0f%%',explode=explode,shadow=True)

plt.show()