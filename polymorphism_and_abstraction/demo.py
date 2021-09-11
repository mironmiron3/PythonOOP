class Num:
    def __init__(self, num):
        self.n1 = num


class Num2(Num):
    def __init__(self, num):
        super().__init__(num)
        self.n2 = num * 2

    def show(self):
        print(self.n1, self.n2)


mynumber = Num2(8)
mynumber.show()