import numpy as np
#import pylab
import matplotlib.pyplot as plt
w=np.array([0.5, 0.5, 0.5])
x=np.array([[1, 1, 0.3],
            [1, 0.4, 0.5],
            [1, 0.7, 0.8],
            [1,0.4,0.6],
            [1,0.8,0.6]])
target=np.array([1,1,0,0,0])
def activate(sum):
    if sum>0:
        return 1
    else:
        return 0

for j in range(12000):
    for i in range(x.shape[0]):
        if activate(w.T.dot(x[i])) != target[i]:
            if target[i]==1:
                w=w+x[i]
            else:
                w=w-x[i]

#colors = ['r' if l>0 else 'b' for l in target]
#plt.scatter(x[:,1],x[:,2], marker='o', c=colors, s=30, alpha = 0.5)
#line, = plt.plot([0.4,1], [1,0.5], color="black", linewidth=2)
#plt.show()

print(w)
xx = np.linspace(*plt.xlim())
a=-w[1]/w[2]
b=-w[0]/w[2]
yy=a*xx+b

colors = ['r' if l>0 else 'b' for l in target]
plt.scatter(x[:,1],x[:,2], marker='o', c=colors, s=30, alpha = 0.5)
line, = plt.plot(xx, yy, color="black", linewidth=2)
#plt.scatter(xx, yy, color="black")
plt.show()