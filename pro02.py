#!usr/bin/python
#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

x=np.random.randn(10)
y=-x+np.random.randn(10)*0.5
strx=''
stry=''
f=open ('textfile2.txt','w')
for numx in x:
    strx = strx + str(numx) + ' '
f.write(strx+'\n')
for numy in y:
    stry=stry+str(numy)+' '
f.write(stry)
f.close()

# x=np.arange(0,100,10)
# y=np.arange(0,-100,-10)

f=open('textfile2.txt','r')
filelinex=f.readline()
fsplitx=filelinex.split()
fileliney=f.readline()
fsplity=fileliney.split()

plt.scatter(fsplitx,fsplity)
plt.show()