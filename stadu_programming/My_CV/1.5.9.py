class Buffer:
    def __init__(self):
        self.lst=[]
        self.lst1=[]
# конструктор без аргументов
    def add(self, *a):
        for i in a:
            self.lst.append(i)
        while len(self.lst)>=5:
            summa=0
            for i in range(5):
                summa+=self.lst[0]
                self.lst.pop(0)
            print (summa)
# добавить следующую часть последовательности
    def get_current_part(self):
        if len(self.lst)>=0 and len(self.lst)<5:
            return (self.lst)

# вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]
