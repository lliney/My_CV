import numpy as np
import random
x = [1, 2, 3]
y = x
y.append(4)

s = "123"
print(type(x))
print(type(4))
print(type(s))

sizes=np.array([2, 3, 1])
weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
nabla_w = [np.zeros(w.shape) for w in weights]
print(nabla_w)