import math

class Circle:
    def __init__(self, radius):
        self._r = radius

    @property
    def area(self):
        return math.pi * self._r ** 2

    # @x.setter
    # def x(self, value):
    #     self._x = value


c = Circle(2.0)
print(c.area)