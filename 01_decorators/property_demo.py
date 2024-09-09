import math

class Circle:
    def __init__(self, radius):
        self._r = radius

    @property
    def area(self):
        print('area is called')
        return math.pi * self._r ** 2

    @area.setter
    def area(self, value):
        r = (value / math.pi)**0.5
        print('new radius is', r)
        self._r = r


c = Circle(2.0)
s = c.area
print('s=', s)
c.area = 12