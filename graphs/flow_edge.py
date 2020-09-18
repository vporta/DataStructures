"""
flow_edge.py
Capacitated edge with a flow in a flow network.
The FlowEdge class represents a capacitated edge with a
  * flow in a FlowNetwork. Each edge consists of two integers
 *  (naming the two vertices), a real-valued capacity, and a real-valued
 *  flow. The data type provides methods for accessing the two endpoints
 *  of the directed edge and the weight. It also provides methods for
 *  changing the amount of flow on the edge and determining the residual
 *  capacity of the edge.
"""
import math


class FlowEdge:
    FLOATING_POINT_EPSILON = 1E-10

    def __init__(self, v=0, w=0, capacity=0.0):
        if v < 0:
            raise AttributeError('vertex index must be a nonnegative integer')
        if w < 0:
            raise AttributeError('vertex index must be a nonnegative integer')
        if not capacity >= 0.0:
            raise AttributeError('Edge capacity must be non-negative')
        self._v = v
        self._w = w
        self._capacity = capacity
        self._flow = 0.0

    def tail(self):
        return self._v

    def head(self):
        return self._w

    def capacity(self):
        return self._capacity

    def flow(self):
        return self._flow

    def other(self, vertex):
        if vertex == self._v:
            return self._w
        elif vertex == self._w:
            return self._v
        else:
            raise AttributeError('Invalid endpoint')

    def residual_capacity_to(self, vertex):
        if vertex == self._v:
            return self._flow  # backward edge
        elif vertex == self._w:  # forward edge
            return self._capacity - self._flow
        else:
            raise AttributeError('Invalid endpoint')

    def add_residual_flow_to(self, vertex, delta):
        if not delta >= 0.0:
            raise AttributeError('Delta must be non-negative')
        if vertex == self._v:
            self._flow -= delta  # backward edge
        elif vertex == self._w:
            self._flow += delta  # forward edge
        else:
            raise AttributeError('Invalid endpoint')
        # round flow to 0 or capacity if within floating-point precision

        if abs(self._flow) <= self.FLOATING_POINT_EPSILON:
            self._flow = 0
        if abs(self._flow - self._capacity) <= self.FLOATING_POINT_EPSILON:
            self._flow = self._capacity
        if not self._flow >= 0.0:
            raise AttributeError('flow is negative')
        if not self._flow <= self._capacity:
            raise AttributeError('flow exceeds capacity')

    def __str__(self):
        return f'{self._v}->{self._w} {self._flow}/{self._capacity}'

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'_v={self._v}, ' \
               f'_w={self._w}, ' \
               f'_capacity={self._capacity},' \
               f'_flow={self._flow})>'


def main():
    e = FlowEdge(12, 23, 4.56)
    print(e)


if __name__ == '__main__':
    main()
