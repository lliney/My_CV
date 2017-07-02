import urllib
from urllib import request
import numpy as np

#fname = input()  # read file name from stdin
f = urllib.request.urlopen("https://stepic.org/media/attachments/lesson/16462/boston_houses.csv")  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with
c=data.shape
y=np.ones(int(c[0]))
y=y.reshape(y.size,1)
#print(y)
for i in range(int(c[0])):
    y[i]=y[i]*data[i,0]
    data[i,0]=1
#Отримали масив У та масив data 1 стовбець якого 1
x=data
z1=x.T
z=np.dot(z1,x)
z=np.linalg.matrix_power(z,-1)
z=np.dot(z,z1)
data=(np.dot(z,y))
data=data.ravel()
for i in data:
    print(i, end=' ')

