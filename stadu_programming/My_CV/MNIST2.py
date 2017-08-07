import mnist_loader
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
import Neyron_network
net = Neyron_network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
#print(test_data)