class ExtendedStack(list):
    def sum(self):
        a=self.pop()
        b=self.pop()
        c=a+b
        self.append(c)

        # операция сложения


    def sub(self):
        a = self.pop()
        b = self.pop()
        c=a-b
        self.append(c)
        # операция вычитания

    def mul(self):
        a = self.pop()
        b = self.pop()
        c=a*b
        self.append(c)
        # операция умножения

    def div(self):
        a = self.pop()
        b = self.pop()
        c=a//b
        self.append(c)
        # операция целочисленного деления
a=ExtendedStack()
a.append(1)
a.append(2)
a.append(3)
a.sum()
print(a)