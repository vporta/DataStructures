"""
Edge.py
The Edge class represents a weighted edge.
Each edge consists of two integers
 *  (naming the two vertices) and a real-value weight. The data type
 *  provides methods for accessing the two endpoints of the edge and
 *  the weight. The natural order for this data type is by
 *  ascending order of weight.
"""
import math


class Edge:

    def __init__(self, v=0, w=0, weight=0.0):
        if v < 0:
            raise AttributeError('vertex index must be a nonnegative integer')
        if w < 0:
            raise AttributeError('vertex index must be a nonnegative integer')
        if math.isnan(weight):
            raise AttributeError('weight is NaN')
        self._v = v
        self._w = w
        self._weight = weight

    def weight(self):
        return self._weight

    def either(self):
        return self._v

    def get_v(self):
        return self._v

    def get_w(self):
        return self._w

    # Returns the endpoint of this edge that is different from the given vertex
    def other(self, vertex):
        if self.get_v() == vertex:
            return self.get_w()
        elif self.get_w() == vertex:
            return self.get_v()
        else:
            raise AttributeError('Illegal endpoint')

    def __lt__(self, other):
        return self.weight() < other.weight()

    def __gt__(self, other):
        return self.weight() > other.weight()

    def __eq__(self, other):
        return self.weight() == other.weight()

    def __repr__(self):
        return f'<Edge(v={self.get_v()}, w={self.get_w()}, weight={self.weight()})>'


def main():
    e = Edge(12, 35, 5.67)
    e1 = Edge(13, 35, 6.67)
    print(e)
    print(f'e < e1 {e < e1}')
    print(f'e > e1 {e > e1}')
    print(f'e == e1 {e == e1}')


if __name__ == '__main__':
    main()