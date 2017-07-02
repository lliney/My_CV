import math
import  numpy as np
mat=np.eye(3,4,0)
b=np.eye(3,4,1)
mat=2*mat
mat=mat+b
print(mat.reshape(mat.size,1))