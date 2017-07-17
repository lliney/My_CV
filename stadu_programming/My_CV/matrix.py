import math
import  numpy as np
a=np.array([[1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]])
b=np.array([[1,2,3],
            [5,6,7],
            [9,10,11],
            [4,8,12]])
c=np.array([[3,0,0],
            [0,3,0],
            [0,0,3]])
a=2*a
k=np.dot(a,b)
print(k)
p=np.dot(k,c)
print(p)
