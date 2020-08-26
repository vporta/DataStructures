"""
FordFulkerson.py
Ford-Fulkerson algorithm for computing a max flow and a min cut using shortest augmenting path rule.
*  The FordFulkerson class represents a data type for computing a
 *  maximum st-flow and minimum st-cut in a flow
 *  network.
 *
 *  This implementation uses the Ford-Fulkerson algorithm with
 *  the shortest augmenting path heuristic.
 *  The constructor takes O(E V (E + V))
 *  time, where V is the number of vertices and E is
 *  the number of edges. In practice, the algorithm will run much faster.
 *  The inCut() and value() methods take Theta(1) time.
 *  It uses Theta(V) extra space (not including the network).
 *
 *  If the capacities and initial flow values are all integers, then this
 *  implementation guarantees to compute an integer-valued maximum flow.
 *  If the capacities are floating-point numbers, then floating-point
 *  round-off error can accumulate.
"""
import math
from queue import Queue

from Graphs.FlowEdge import FlowEdge
from Graphs.FlowNetwork import FlowNetwork


class FordFulkerson:
    FLOATING_POINT_EPSILON = 1E-11
    _edge_to = None
    _marked = None

    def __init__(self, g, s, t):
        self._V = g.get_V()
        self.__validate(s)
        self.__validate(t)
        self._value = self.__excess(g, t)
        if s == t:
            raise AttributeError('source equals sink')
        if not self.__is_feasible(g, s, t):
            raise AttributeError('initial flow is infeasible')

        # current value of max flow
        while self.__has_augmenting_path(g, s, t):
            bottle = math.inf

            # compute bottleneck capacity
            v = t
            while v != s:
                bottle = min(bottle, self._edge_to[v].residual_capacity_to(v))
                v = self._edge_to[v].other(v)

            # augment flow
            v = t
            while v != s:
                self._edge_to[v].add_residual_flow_to(v, bottle)
                v = self._edge_to[v].other(v)
            self._value += bottle

        # check optimality conditions
        assert self.__check(g, s, t)

    def value(self):
        return self._value

    def in_cut(self, v):
        self.__validate(v)
        return self._marked[v]

    def __has_augmenting_path(self, g, s, t):
        self._edge_to = [FlowEdge()] * self._V
        self._marked = [False] * self._V
        # breadth-first search
        queue = Queue()
        queue.put(s)
        self._marked[s] = True
        while not queue.empty() and not self._marked[t]:
            v = queue.get()
            for e in g.adj(v):
                w = e.item.other(v)

                # if residual capacity from v to w
                if e.item.residual_capacity_to(w) > 0:
                    if not self._marked[w]:
                        self._marked[w] = True
                        self._edge_to[w] = e.item
                        queue.put(w)

        # is there an augmenting path?
        return self._marked[t]

    def __excess(self, g, v):
        excess = 0.0
        for e in g.adj(v):
            if v == e.item.tail():
                excess -= e.item.flow()
            else:
                excess += e.item.flow()
        return excess

    def __is_feasible(self, g, s, t):
        # check that capacity constraints are satisfied
        for v in range(g.get_V()):
            for e in g.adj(v):
                if e.item.flow() < -self.FLOATING_POINT_EPSILON or e.item.flow() > e.item.capacity() + self.FLOATING_POINT_EPSILON:
                    print(f'Edge does not satisfy capacity constraints: {e}')
                    return False
        # check that net flow into a vertex equals zero, except at source and sink
        if abs(self._value + self.__excess(g, s)) > self.FLOATING_POINT_EPSILON:
            print(f'Excess at source = {self.__excess(g, s)}')
            print(f'Max flow         = {self._value}')
            return False
        if abs(self._value - self.__excess(g, t)) > self.FLOATING_POINT_EPSILON:
            print(f'Excess at sink = {self.__excess(g, t)}')
            print(f'Max flow         = {self._value}')
            return False
        for v in range(g.get_V()):
            if v == s or v == t:
                continue
            elif abs(self.__excess(g, v)) > self.FLOATING_POINT_EPSILON:
                print(f'Net flow out of {v} does not equal zero')
                return False
        return True

    def __validate(self, v):
        n = self._V
        if v < 0 or v >= n:
            raise AttributeError(f'vertex {v} is not between 0 and {n - 1}')

    def __check(self, g, s, t):
        if not self.__is_feasible(g, s, t):
            print('flow is infeasible')
            return False
        # check that s is on the source side of min cut and that t is not on source side
        if not self.in_cut(s):
            print(f'source {s} is not on source side of min cut')
            return False
        if self.in_cut(t):
            print(f'sink {t} is on source side of min cut')
            return False
        min_cut_value = 0.0
        for v in range(g.get_V()):
            for e in g.adj(v):
                if v == e.item.tail() and self.in_cut(e.item.tail()) and not self.in_cut(e.item.head()):
                    min_cut_value += e.item.capacity()
        if abs(min_cut_value - self._value) > self.FLOATING_POINT_EPSILON:
            print(f'Max flow value = {self._value}, min cut value = {min_cut_value}')
            return False
        return True

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'_V={self._V}, ' \
               f'_value={self._value}, ' \
               f'_edge_to={self._edge_to}, ' \
               f'_marked={self._marked})>'


def main():
    with open("../Resources/tinyFN.txt", ) as f:
        values = "".join(f.readlines()).splitlines()
        print(values)
        V, E = int(values[0]), int(values[1])
        s, t = 0, V - 1
        g = FlowNetwork(V, E)

        for line in values[2:]:
            vertices = line.split(' ')
            v, w, capacity = int(vertices[0]), int(vertices[1]), float(vertices[2])
            e = FlowEdge(v, w, capacity)
            g.add_edge(e)
        print(g)

        # compute maximum flow and minimum cut
        max_flow = FordFulkerson(g, s, t)
        print(max_flow)
        print(f'max flow from {s} to {t}')
        for v in range(g.get_V()):
            for e in g.adj(v):
                if v == e.item.tail() and e.item.flow() > 0:
                    print(f'     {e}')

        print('min cut: ')
        for v in range(g.get_V()):
            if max_flow.in_cut(v):
                print(f'{v}  ')
        print()
        print(f'max flow value = {max_flow.value()}')



if __name__ == '__main__':
    main()