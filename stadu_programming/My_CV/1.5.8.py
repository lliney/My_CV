class MoneyBox:
    def __init__(self, capacity):
        self.vmestitilnost=capacity
        self.summa=0
# конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        if v<=(self.vmestitilnost-self.summa):
            return True
        else:
            return False
# True, если можно добавить v монет, False иначе

    def add(self, v):
        self.summa+=v

# положить v монет в копилку
