#!usr/bin/python
#coding:utf-8
import numpy as np

file=open('textfile1.txt','w')
c=np.random.randint(1,100,10)
str1=''
for num in c:
    print num
    str1=str1+str(num)+' '
file.write(str1)
file.close()

file=open('textfile1.txt','r')
fileline=file.read()
print '这一行的原始数据;'+fileline
list=fileline.split()  #拆分数据
print list
print type(list[0])     #打印数据类型 str类型
list=map(int,list)     #转换数据类型  str---》int
print list
print type(list[0])     #打印数据类型 int类型
list.sort()              #排序
print '排序后输出; '+str(list)
max=max(list)
print '最大值;'+str(max)
min=min(list)
print '最小值;'+str(min)
mean=np.mean(list)
print '均值;'+str(mean)