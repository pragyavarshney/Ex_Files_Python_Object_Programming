# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to enforce class constraints
from abc import ABC, abstractmethod
import math


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        pi = math.pi
        return pi * (self.radius ** 2)


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side ** 2


# g = GraphicShape()

c = Circle(10)
print("{:.2f}".format(c.calcArea()))
s = Square(12)
area = s.calcArea()
print(s.calcArea())
