import numpy as np
import matplotlib.pyplot as plt
import random

data = np.loadtxt("/home/lliney/dani.txt")
np.random.shuffle(data)
np.random.shuffle(data)
#зчитую дані із підготовленого файлу
x=data[:,0:2]
#перші два стовбці це вхідні пареметри(без 1)
one=np.ones(x.shape[0])
one=one.reshape(x.shape[0],1)
x=np.hstack([one,x])
train_x, test_x = np.split(x, [ x.shape[0]*8//10])
#Добавляю в матрицю перший стовбець 1
target=data[:,2]
train_labels, test_labels = np.split(target, [x.shape[0]*8//10])
#правильні активації з файлу
w=np.array([1, 1, 1])
#створюю нульові  веса
def activate(sum):
    if sum>0:
        return 1
    else:
        return 0
#Це фу-я активації вона проста
def test(x):
    return activate(w.T.dot(x))
    # х це вектор розміром 3х1

for j in range(10):
    # j-це кількість проходів по всіх даних, (к-ть епох)
    for i in range(train_x.shape[0]):
        if activate(w.T.dot(train_x[i])) != train_labels[i]:
            if target[i]==1:
                w=w+train_x[i]
            else:
                w=w-train_x[i]

print(w)
xx = np.linspace(*plt.xlim())
a=-w[1]/w[2]
b=-w[0]/w[2]
yy=a*xx+b
er=0
for p in range(test_x.shape[0]):
    if test(test_x[p])!=int(test_labels[p]):
        er+=1
a='%'
b='error='
print(b,(er/test_x.shape[0])*100,a)

colors = ['r' if l>0 else 'b' for l in target]
plt.scatter(x[:,1],x[:,2], marker='o', c=colors, s=5, alpha = 0.5)
line, = plt.plot(xx, yy, color="black", linewidth=2)
#plt.scatter(xx, yy, marker='o',color="black", s=5, alpha = 0.5)
colors = ['g' if l>0 else 'black' for l in test_labels]
plt.scatter(test_x[:,1],test_x[:,2], marker='o', c=colors, s=5, alpha = 0.5)
plt.show()


