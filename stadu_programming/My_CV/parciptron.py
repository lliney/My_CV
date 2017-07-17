import numpy as np
w=np.array([0, 0, 0])
x=np.array([[1, 1, 0.3],
            [1, 0.4, 0.5],
            [1, 0.7, 0.8]])
target=np.array([1,1,0])

def activate(sum):
    if sum>0:
        return 1
    else:
        return 0

for i in range(3):
    if activate(w.T.dot(x[i])) != target[i]:
        if target[i]==1:
            w=w+x[i]
        else:
            w=w-x[i]
print(w)
