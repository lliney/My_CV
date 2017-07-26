import numpy as np
import random

def sigmoid(z):
    """The sigmoid function.
    Функция сигмоиды
    """
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    """Derivative of the sigmoid function.
    Производная сигмоиды по  x
    """
    return sigmoid(z)*(1-sigmoid(z))

def cost_function(network, test_data, onehot=True):
    c = 0
    for example, y in test_data:
        if not onehot:
            y = np.eye(3, 1, k=-int(y))
        yhat = network.feedforward(example)
        c += np.sum((y - yhat)**2)
    return c / len(test_data)


class Network:
    def __init__(self, sizes, output=True):
        """
        Список ``sizes`` содержит количество нейронов в соответствующих слоях
        нейронной сети. К примеру, если бы этот лист выглядел как [2, 3, 1],
        то мы бы получили трёхслойную нейросеть, с двумя нейронами в первом
        (входном), тремя нейронами во втором (промежуточном) и одним нейроном
        в третьем (выходном, внешнем) слое. Смещения и веса для нейронных сетей
        инициализируются случайными значениями, подчиняющимися стандартному нормальному
        распределению. Обратите внимание, что первый слой подразумевается слоем,
        принимающим входные данные, поэтому мы не будем добавлять к нему смещение
        (делать это не принято, поскольку смещения используются только при
        вычислении выходных значений нейронов последующих слоёв)
        """

        self.num_layers = len(sizes) # кількість слоїв мережі
        self.sizes = sizes #масив з кількістю нейронів в кожному слої
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        #створюємо масив базисів [size-1,1], починаючи з другого слоя, випадковими числами
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
        #створюємо масиви вагів в залежності від к-ті нейронів
        self.output = output #якась булівська змінна

    def feedforward(self, a):
        """
        Вычислить и вернуть выходную активацию нейронной сети
        при получении ``a`` на входе (бывшее forward_pass).
        запускає мережу на виконання, ане на навчання
        """
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        return a

    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):
        """
        Обучить нейронную сеть, используя алгоритм стохастического
        (mini-batch) градиентного спуска.
        ``training_data`` - лист кортежей вида ``(x, y)``, где
        x - вход обучающего примера, y - желаемый выход (в формате one-hot).
        Роль остальных обязательных параметров должна быть понятна из их названия.
        Если предоставлен опциональный аргумент ``test_data``,
        то после каждой эпохи обучения сеть будет протестирована на этих данных
        и промежуточный результат обучения будет выведен в консоль.
        ``test_data`` -- это список кортежей из входных данных
        и номеров правильных классов примеров (т.е. argmax(y),
        если y -- набор ответов в той же форме, что и в тренировочных данных).
        Тестирование полезно для мониторинга процесса обучения,
        но может существенно замедлить работу программы.
        """

        if test_data is not None: n_test = len(test_data)
        #Якщо є тестові дані то взнаємо їх к-ть
        n = len(training_data)
        # к-ть тренувальних даних
        success_tests = 0
        # к-ть успішних тестів
        for j in range(epochs):
            # запускаємо епохи
            random.shuffle(training_data)
            # перемішуємо дані
            mini_batches = [training_data[k:k + mini_batch_size] for k in range(0, n, mini_batch_size)]
            # створюємо порції  даних з всіх (масив)
            for mini_batch in mini_batches:
                self.update_mini_batch(mini_batch, eta)
                # Для кожної порції визиваємо ф-ю апдейт
            if test_data is not None and self.output:
                success_tests = self.evaluate(test_data)
                print("Эпоха {0}: {1} / {2}={3}%".format(j, success_tests, n_test,success_tests*100/n_test))
                # Якщо є провірочні дані, показує як начилася мережа
            elif self.output:
                print("Эпоха {0} завершена".format(j))
                # Якщо провірочних даних нема, просто завершена епоха№
        if test_data is not None:
            return success_tests / n_test
            # Якщо є тестові (провірочні) дані верне відношення правильних відповідей до зазальної к-ті

    def update_mini_batch(self, mini_batch, eta):
        """
        Обновить веса и смещения нейронной сети, сделав шаг градиентного
        спуска на основе алгоритма обратного распространения ошибки, примененного
        к одному mini batch.
        ``mini_batch`` - список кортежей вида ``(x, y)``,
        ``eta`` - величина шага (learning rate).
        """

        nabla_b = [np.zeros(b.shape) for b in self.biases]
        # створюємо нульову матрицю, точно таку ж як базис
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # створюємо нульові масиви розмірами такі, як матриці весів
        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            # щоб пощитати дельта набла базису, і дельта набла всіх висів визиваємо бекпроп
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]# нвіщо сума, якщо набла б 0?
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        # отримали набла б(градієнт базисів) і набла в(градієнт весів)
        eps = eta / len(mini_batch)
        # отримуємо швидкіть навчання розділену на к-ть прикладів?
        self.weights = [w - eps * nw for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b - eps * nb for b, nb in zip(self.biases, nabla_b)]
        # обновлюємо веса


    def backprop(self, x, y):
        """
        Возвращает кортеж ``(nabla_b, nabla_w)`` -- градиент целевой функции по всем параметрам сети.
        ``nabla_b`` и ``nabla_w`` -- послойные списки массивов ndarray,
        такие же, как self.biases и self.weights соответственно.
        """
        # Эту функцию необходимо реализовать
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # створюємо нульові масиви

        activation = x
        activations = [x] #Список, щоб зберігати всі активації, шар по шару
        zs = [] # Список для зберігання всіх векторів z, шар по шару
        # прямое распространение (forward pass)


        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b  # Це суматорна ф-я по 1-му прикладу
            zs.append(z) # масив, який зберігає всі суми
            activation = sigmoid(z) # приміняємо ф-ю уктивації до суми
            activations.append(activation)# додаємо активацію
            # посчитать активации
            pass

        # обратное распространение (backward pass)
        delta = self.cost_derivative(activations[-1], y) * sigmoid_prime(zs[-1]) # ошибка выходного слоя
        nabla_b[-1] = delta # производная J по смещениям выходного слоя
        nabla_w[-1] = np.dot(delta, activations[-2].transpose()) # производная J по весам выходного слоя

        # Обратите внимание, что переменная l в цикле ниже используется
        # немного иначе, чем в лекциях.  Здесь l = 1 означает последний слой,
        # l = 2 - предпоследний и так далее.
        # Мы перенумеровали схему, чтобы с удобством для себя
        # использовать тот факт, что в Python к переменной типа list
        # можно обращаться по негативному индексу.
        for l in range(2, self.num_layers):
            # дополнительные вычисления, чтобы легче записывалось
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l + 1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l - 1].transpose())
        return nabla_b, nabla_w
    def evaluate(self, test_data):
        """
        Вернуть количество тестовых примеров, для которых нейронная сеть
        возвращает правильный ответ. Обратите внимание: подразумевается,
        что выход нейронной сети - это индекс, указывающий, какой из нейронов
        последнего слоя имеет наибольшую активацию.
        """
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)

    def cost_derivative(self, output_activations, y):
        """
        Возвращает вектор частных производных (\partial C_x) / (\partial a)
        целевой функции по активациям выходного слоя.
        """
        return (output_activations - y)

