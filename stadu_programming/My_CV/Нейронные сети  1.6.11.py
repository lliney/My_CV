from urllib.request import urlopen
import numpy as np
f = urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')
#filename = input()
#f = urlopen(filename)
sbux = np.loadtxt(f,  skiprows=1, delimiter=",")
print(sbux.mean(axis=0))  # вдоль столбцов