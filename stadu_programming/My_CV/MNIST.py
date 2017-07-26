#import mnist_loader
#training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
import random
import numpy as np
import pylab
def generator(a,b):
    X = np.linspace(2,10,a)[1:-1]
    X=X/10
    np.random.shuffle(X)
    X=X.reshape(len(X),1)
    zero=np.zeros((len(X),1))
    X=np.hstack([zero,X])
    for i in range(len(X)):
     X[i,0]=(random.random())
    zero=zero.astype(np.int32)
    X=np.hstack([X,zero])
    #print(X[:4])
    Y = np.linspace(0.1,2,b)[1:-1]
    Y=Y/10
    np.random.shuffle(Y)
    Y=Y.reshape(len(Y),1)
    zero=np.zeros((len(Y),1))
    Y=np.hstack([zero,Y])
    for i in range(len(Y)):
        Y[i,0]=(random.random())
    zero=zero+1
    zero=zero.astype(np.int32)
    Y=np.hstack([Y,zero])
    #print(Y[:4])
    viborka=np.vstack([X,Y])
    np.random.shuffle(viborka)
    colors = ['r' if l>0 else 'b' for l in viborka[:,2]]
    pylab.scatter(viborka[:,0],viborka[:,1], marker='o', c=colors, s=30, alpha = 0.5)
    pylab.show()
    with open("/home/lliney/dani.txt","w") as f:
        for i in range (viborka.shape[0]):
          for j in range(viborka.shape[1]):
              f.write(str(viborka[i,j])+' ')
          f.write('\n')

generator(1000,250)
data = np.loadtxt("/home/lliney/dani.txt")
#print(data[:4])
#print(data.shape)
training_data, test_data = np.split(data, [ data.shape[0]*8//10])
training_data = [(d[:2][:, np.newaxis], np.eye(2, 1, k=-int(d[-1]))) for d in training_data]
test_data =  [(d[:2][:, np.newaxis], d[-1]) for d in test_data]
print(training_data[:1])


#import Neyron_network
#net = Neyron_network.Network([2,2,2])
#net.SGD(training_data, 200, 10, 1, test_data=test_data)