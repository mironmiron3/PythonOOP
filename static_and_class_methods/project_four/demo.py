from abc import ABC, abstractmethod

class Shape():

    def __init__(self):
        self.weight= 5
    @staticmethod
    def area(self):
        return 5


class Triangle(Shape):
    def __init__(self, height):
        super().__init__()
        self.height = height

t = Triangle(5)
print(area())
