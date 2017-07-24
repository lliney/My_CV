import numpy as np
#import pylab
import matplotlib.pyplot as plt
w=np.array([0, 0, 0])
x=np.array([[1, 1, 0.3],
            [1, 0.4, 0.5],
            [1, 0.7, 0.8]])
target=np.array([1,1,0])
print(target)
def activate(sum):
    if sum>0:
        return 1
    else:
        return 0

for j in range(120):
    for i in range(3):
        if activate(w.T.dot(x[i])) != target[i]:
            if target[i]==1:
                w=w+x[i]
            else:
                w=w-x[i]
    print(j,w)
#colors = ['r' if l>0 else 'b' for l in target]
#plt.scatter(x[:,1],x[:,2], marker='o', c=colors, s=30, alpha = 0.5)
#line, = plt.plot([0.4,1], [1,0.5], color="black", linewidth=2)
#plt.show()

def plot_line(coefs):
    """
    рисует разделяющую прямую, соответствующую весам, переданным в coefs = (weights, bias),
    где weights - ndarray формы (2, 1), bias - число
    """
    w, bias = coefs
    a, b = - w[0][0] / w[1][0], - bias / w[1][0]
    xx = np.linspace(*plt.xlim())
    line.set_data(xx, a*xx + b)
print(w.shape)
print(w[1])
print(w[2])
xx = np.linspace(*plt.xlim())
a=-w[1]/w[2]
b=-1/w[2]
yy=a*xx+b

colors = ['r' if l>0 else 'b' for l in target]
plt.scatter(x[:,1],x[:,2], marker='o', c=colors, s=30, alpha = 0.5)
#line, = plt.plot(xx, yy, color="black", linewidth=2)
plt.scatter(xx, yy, color="black")
plt.show()