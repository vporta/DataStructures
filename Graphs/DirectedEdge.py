"""
DirectedEdge.py
Immutable weighted directed edge.
The  DirectedEdge class represents a weighted edge in an
 *  EdgeWeightedDigraph. Each edge consists of two integers
 *  (naming the two vertices) and a real-value weight. The data type
 *  provides methods for accessing the two endpoints of the directed edge and
 *  the weight.
"""
import math


class DirectedEdge:

    def __init__(self, v, w, weight):
        if v < 0:
            raise AttributeError('Vertex names must be nonnegative integers')
        if w < 0:
            raise AttributeError('Vertex names must be nonnegative integers')
        if math.isnan(float(weight)):
            raise AttributeError('Weight is NaN')
        self._v = v
        self._w = w
        self._weight = weight

    # from
    def tail(self):
        return self._v

    # to
    def head(self):
        return self._w

    def weight(self):
        return self._weight

    def __repr__(self):
        return f'<{self.__class__.__name__}(v={self._v}, w={self._w}, weight={self._weight})>'

    def __str__(self):
        return f'{self._v}->{self._w} {self._weight}'


