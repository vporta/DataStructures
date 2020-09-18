"""
sparse_vector.py
SparseVector class represents a d-dimensional mathematical vector.
 *  Vectors are mutable: their values can be changed after they are created.
 *  It includes methods for addition, subtraction,
 *  dot product, scalar product, unit vector, and Euclidean norm.
 *
 *  The implementation is a symbol table of indices and values for which the vector
 *  coordinates are nonzero. This makes it efficient when most of the vector coordinates
  * are zero.

  Matrix vector multiplication
  standard matrix: sum(a[i][j] * x[j]) = b[i] running time: n^2
  sparse vector: a[vector[index]=entry] running time: n
"""
from collections import defaultdict
import math


class SparseVector:

    def __init__(self, d):
        """
        :param d: the dimension
        :type d: int
        """
        self._st = defaultdict(float)
        self._d = d

    def get_st(self):
        return self._st

    def get_d(self):
        return self._d

    def put(self, i, value):
        if i < 0 or i >= self.get_d():
            raise AttributeError('Illegal index')
        if value == 0.0:
            del self.get_st()[i]
        else:
            self.get_st()[i] = value

    def get(self, i):
        if i < 0 or i >= self.get_d():
            raise AttributeError('Illegal index')
        if i in self.get_st():
            return self.get_st()[i]
        else:
            return 0.0

    # Returns the number of non zero entries in this vector
    def nnz(self):
        return len(self.get_st())

    def dimension(self):
        return self.get_d()

    # Returns the inner product of this vector with the specified vector.
    def dot_spv(self, that):
        if self.get_d() != that.get_d():
            raise AttributeError('Vector lengths disagree')
        _sum = 0.0
        if len(self.get_st()) <= len(that.get_st()):
            for i in self.get_st().keys():
                if i in that.get_st():
                    _sum += self.get(i) * that.get(i)
        else:
            for i in that.get_st().keys():
                if i in self.get_st():
                    _sum += self.get(i) * that.get(i)
        return _sum

    # Returns the inner product of this vector with the specified list.
    def dot(self, that):
        _sum = 0.0
        for i in self.get_st().keys():
            _sum += that[i] * self.get(i)
        return _sum

    def magnitude(self):
        return math.sqrt(self.dot_spv(self))

    def scale(self, alpha):
        c = SparseVector(self.get_d())
        for i in self.get_st().keys():
            c.put(i, alpha * self.get(i))
        return c

    def plus(self, that):
        if self.get_d() != that.get_d():
            raise AttributeError('Vector lengths disagree')
        c = SparseVector(self.get_d())
        for i in self.get_st().keys():
            c.put(i, self.get(i))
        for i in that.get_st().keys():
            c.put(i, that.get(i) + c.get(i))
        return c

    def __repr__(self):
        return f'<SparseVector(st={self.get_st()}, d={self.get_d()})>'


def main():
    a = SparseVector(10)
    b = SparseVector(10)
    a.put(3, 0.50)
    a.put(9, 0.75)
    a.put(6, 0.11)
    a.put(6, 0.00)
    b.put(3, 0.60)
    b.put(4, 0.90)
    print("a = ", a)
    print("b = ", b)
    print("a dot b = ", a.dot_spv(b))
    print("a + b   = ", a.plus(b))

if __name__ == '__main__':
    main()