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
#print(training_data[:1])


import Neyron_network
net = Neyron_network.Network([2,8,2])
net.SGD(training_data, 100, 10, 0.1, test_data=test_data)
import matplotlib.pyplot as plt
from ipywidgets import *
from ipywidgets import widgets
from IPython.display import display

@interact(layer1=IntSlider(min=0, max=10, continuous_update=False, description="1st inner layer: ", value=6),
          layer2=IntSlider(min=0, max=10, continuous_update=False, description="2nd inner layer:"),

          batch_size=BoundedIntText(min=1, max=len(data), value=10, description="Batch size: "),
          learning_rate=Dropdown(options=["0.01", "0.05", "0.1", "0.5", "1", "5", "10"],
                                 description="Learning rate: ")
          )
def learning_curve_by_network_structure(layer1, layer2, batch_size, learning_rate):
    layers = [x for x in [2, layer1, layer2, 2] if x > 0]
    print(layers)
    nn = Neyron_network.Network(layers, output=False)
    learning_rate = float(learning_rate)

    CER = []
    cost_train = []
    cost_test = []
    for _ in range(50):
        nn.SGD(training_data=training_data, epochs=1, mini_batch_size=batch_size, eta=learning_rate)
        CER.append(1 - nn.evaluate(test_data) / len(test_data))
        cost_test.append(Neyron_network.cost_function(nn, test_data, onehot=False))
        cost_train.append(Neyron_network.cost_function(nn, training_data, onehot=True))

    fig = plt.figure(figsize=(15, 5))
    fig.add_subplot(1, 2, 1)
    plt.ylim(0, 1)
    plt.plot(CER)
    plt.title("Classification error rate")
    plt.ylabel("Percent of incorrectly identified observations")
    plt.xlabel("Epoch number")

    fig.add_subplot(1, 2, 2)
    plt.plot(cost_train, label="Training error", color="orange")
    plt.plot(cost_test, label="Test error", color="blue")
    plt.title("Learning curve")
    plt.ylabel("Cost function")
    plt.xlabel("Epoch number")
    plt.legend()
    plt.show()