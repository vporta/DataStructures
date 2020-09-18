"""
point2d.py
"""
import math


class Point2D:

    def __init__(self, x, y):
        if math.isinf(x) or math.isinf(y):
            raise ValueError('Coordinates must be finite.')
        if math.isnan(x) or math.isnan(y):
            raise ValueError('Coordinates cannot be NaN.')
        if x == 0.0:
            self.x = 0.0
        else:
            self.x = x
        if y == 0.0:
            self.y = 0.0
        else:
            self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def distance_to(self, that):
        dx = self.x - that.x
        dy = self.y - that.y
        return math.sqrt(dx * dx + dy * dy)  # Euclidean distance

    def distance_squared_to(self, that):
        dx = self.x - that.x
        dy = self.y - that.y
        return dx * dx + dy * dy  # Square of Euclidean distance

    def compare_to(self, that):
        if self.y < that.y:
            return -1
        if self.y > that.y:
            return +1
        if self.x < that.x:
            return -1
        if self.x > that.x:
            return +1
        return 0

    @classmethod
    def get_class(cls):
        return cls.__name__

    def equals(self, other):
        if other == self:
            return True
        if other is None:
            return False
        if self.get_class() != other.get_class():
            return False
        that = other
        return self.x == that.x and self.y == that.y

    def __repr__(self):
        return f'( {self.x}, {self.y} )'
