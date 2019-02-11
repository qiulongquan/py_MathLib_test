#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# y=np.linspace(-10,100,10)
# x=y**2
print  '折线图'
date,open=np.loadtxt('0002.csv',delimiter=',',converters={0:mdates.strpdate2num('%Y/%m/%d')},skiprows=0,usecols=(0,1),unpack= True)

print date
plt.plot_date(date,open,linestyle='-',c='r',alpha=0.3,marker='o')
plt.show()