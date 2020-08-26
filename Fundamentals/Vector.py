"""
Vector.py
 * Implementation of a vector of real numbers.
"""
import math


class Vector:

    def __init__(self, d):
        if isinstance(d, list):
            self._d = len(d)
            self._data = [d[i] for i in range(self._d)]
        else:
            self._d = d
            self._data = [0.0 for _ in range(self._d)]

    def get_data(self):
        return self._data

    def dimension(self):
        return self._d

    def dot(self, other):
        if self._d != other.dimension():
            raise AttributeError('Dimensions don\'t agree')
        _sum = 0.0
        for i in range(self._d):
            _sum += self._data[i] * other.get_data()[i]
        return _sum

    def magnitude(self):
        # also known as the L2 norm or Euclidean norm
        return math.sqrt(self.dot(self))

    def distance_to(self, other):
        # Euclidean
        if self._d != other.dimension():
            raise AttributeError('Dimensions don\'t agree')
        return self.minus(other).magnitude()

    def minus(self, other):
        if self._d != other.dimension():
            raise AttributeError('Dimensions don\'t agree')
        c = Vector(self._d)
        c._data = [self._data[i] - other.get_data()[i] for i in range(self._d)]
        return c

    def plus(self, other):
        if self._d != other.dimension():
            raise AttributeError('Dimensions don\'t agree')
        c = Vector(self._d)
        c._data = [self._data[i] + other.get_data()[i] for i in range(self._d)]
        return c

    def cartesian(self, i):
        return self._data[i]

    def scale(self, alpha):
        # scalar vector product
        c = Vector(self._d)
        c._data = [self._data[i] * alpha for i in range(self._d)]
        return c

    def direction(self):
        if self.magnitude() == 0.0:
            raise ArithmeticError('Zero-vector has no direction')
        return self.scale(1 / self.magnitude())

    def __str__(self):
        s = ""
        for i in range(self._d):
            s += f'{self._data[i]} '
        return s


def main():
    x_data = [1.0, 2.0, 3.0, 4.0]
    y_data = [5.0, 2.0, 4.0, 1.0]
    x = Vector(x_data)
    y = Vector(y_data)

    print(f'    x   = {x}')
    print(f'    y   = {y}')

    z = x.plus(y)
    print(f'    z   = {z}')

    z = z.scale(10)
    print(f'    10z   = {z}')

    print(f'    |z|   = {x.magnitude()}')
    print(f'    <x, y>   = {x.dot(y)}')
    print(f'    dist(x, y)   = {x.distance_to(y)}')
    print(f'    direction(x)   = {x.direction()}')


if __name__ == '__main__':
    main()