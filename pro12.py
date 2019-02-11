#coding:utf-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime     #时间函数引入

fig=plt.figure()     #图形对象生成
start=datetime.datetime(2016,1,1)    #开始时间
stop=datetime.datetime(2017,1,1)     #终了时间
delta=datetime.timedelta(days=1)     #时间间隔 一天
dates=mpl.dates.drange(start,stop,delta)    #带入到xaxis（x轴）

y=np.arange(len(dates))     #生成y轴 yaxis
ax=plt.gca()       #gca  获得坐标轴刻度
ax.plot_date(dates,y,linestyle='-',marker='')    #用 plot_date 函数来生成有日期的坐标图形
date_format=mpl.dates.DateFormatter('%Y-%m')     #设定坐标刻度的格式
ax.xaxis.set_major_formatter(date_format)       #将坐标刻度的格式带入到x轴中

fig.autofmt_xdate()
plt.show()