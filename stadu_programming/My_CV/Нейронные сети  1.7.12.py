import math
import  numpy as np
x=np.array([[1,60],
            [1,50],
            [1,75]])
y=np.array([[10],
            [7],
            [12]])
z1=x.T
print(z1.shape)
z=np.dot(z1,x)
print(z.shape)
z=np.linalg.matrix_power(z,-1)
print(z.shape)
z=np.dot(z,z1)
print(z.shape)
print(np.dot(z,y))