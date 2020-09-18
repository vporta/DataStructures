"""
topological_x.py
Compute topological ordering of a DAG using queue-based algorithm.
 *  Runs in O(E + V) time.
"""

from graphs.digraph import Digraph
from graphs.edge_weighted_digraph import EdgeWeightedDigraph
from graphs.edge_weighted_directed_cycle import EdgeWeightedDirectedCycle
from graphs.depth_first_order import DepthFirstOrder
from graphs.directed_cycle import DirectedCycle
from graphs.symbol_digraph import SymbolDigraph
from queue import LifoQueue, Queue


class TopologicalX:

    def __init__(self, g):
        if isinstance(g, Digraph):
            _indegree = [g.indegree(v) for v in range(g.get_V())]
            self._ranks = [0 for _ in range(g.get_V())]
            self._order = Queue()
            count = 0

            # initialize queue to contain all vertices with indegree = 0
            queue = Queue()
            for v in range(g.get_V()):
                if _indegree[v] == 0:
                    queue.put(v)
            while not queue.empty():
                v = queue.get()
                self._order.put(v)
                count += 1
                self._ranks[v] = count
                for w in g.adj_vertices(v):
                    _indegree[w.item] -= 1
                    if _indegree[w.item] == 0:
                        queue.put(w.item)
            # there is a directed cycle in subgraph of vertices with indegree >= 1.
            if count != g.get_V():
                self._order = None

            assert self.__check(g)
        else:
            _indegree = [g.indegree(v) for v in range(g.get_V())]
            self._ranks = [0 for _ in range(g.get_V())]
            self._order = Queue()
            count = 0

            # initialize queue to contain all vertices with indegree = 0
            queue = Queue()
            for v in range(g.get_V()):
                if _indegree[v] == 0:
                    queue.put(v)
            while not queue.empty():
                v = queue.get()
                self._order.put(v)
                count += 1
                self._ranks[v] = count
                for e in g.adj_vertices(v):
                    w = e.item.head()
                    _indegree[w.item] -= 1
                    if _indegree[w.item] == 0:
                        queue.put(w.item)
            # there is a directed cycle in subgraph of vertices with indegree >= 1.
            if count != g.get_V():
                self._order = None

            assert self.__check(g)

    def order(self):
        return self._order

    def has_order(self):
        return self._order is not None

    def rank(self, v):
        self.__validate_vertex(v)
        if self.has_order():
            return self._ranks[v]
        else:
            return -1

    def __validate_vertex(self, v):
        n = len(self._ranks)
        if v < 0 or v >= n:
            raise ValueError(f'vertex {v} is not between 0 and {n - 1}')

    def __check(self, g):
        if isinstance(g, Digraph):
            if self.has_order():
                found = [0 for _ in range(g.get_V())]
                for i in range(g.get_V()):
                    found[self.rank(i)] = True

                for i in range(g.get_V()):
                    if not found[i]:
                        print(f'no vertex with rank {i}')
                        return False

                for v in range(g.get_V()):
                    for e in g.adj_vertices(v):
                        w = e.item.head()
                        if self.rank(v) > self.rank(w.item):
                            print(f'{v}-{w.item}: rank({v}) = {self.rank(v)}, '
                                  f'rank({w.item}) = rank({self.rank(w.item)})')
                            return False

                r = 0
                for v in self.order():
                    if self.rank(v) != r:
                        print(f'order() and rank() are inconsistent')
                        return False
                    r += 1
                return True
        else:
            if self.has_order():
                found = [0 for _ in range(g.get_V())]
                for i in range(g.get_V()):
                    found[self.rank(i)] = True

                for i in range(g.get_V()):
                    if not found[i]:
                        print(f'no vertex with rank {i}')
                        return False

                for v in range(g.get_V()):
                    for e in g.adj_vertices(v):
                        w = e.item.head()
                        if self.rank(v) > self.rank(w.item):
                            print(f'{v}-{w.item}: rank({v}) = {self.rank(v)}, '
                                  f'rank({w.item}) = rank({self.rank(w.item)})')
                            return False

                r = 0
                for v in self.order():
                    if self.rank(v) != r:
                        print(f'order() and rank() are inconsistent')
                        return False
                    r += 1
                return True

    def __repr__(self):
        return f'<{self.__class__.__name__}(_order={self._order}, _ranks={self._ranks})>'


def main():
    sg = SymbolDigraph('jobs', '/')
    print(sg)
    topological = TopologicalX(sg.digraph())
    print(topological)
    for v in topological.order():
        print(sg.name_of(v))


if __name__ == '__main__':
    main()
