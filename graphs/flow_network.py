"""
flow_network.py
A capacitated flow network, implemented using adjacency lists.
 * The FlowNetwork class represents a capacitated network
 *  with vertices named 0 through V - 1, where each directed
 *  edge is of type FlowEdge and has a real-valued capacity
 *  and flow.
 *  It supports the following two primary operations: add an edge to the network,
 *  iterate over all of the edges incident to or from a vertex. It also provides
 *  methods for returning the number of vertices V and the number
 *  of edges E. Parallel edges and self-loops are permitted.
 *
 *  This implementation uses an adjacency-lists representation, which
 *  is a vertex-indexed array of Bag objects.
 *  All operations take constant time (in the worst case) except
 *  iterating over the edges incident to a given vertex, which takes
 *  time proportional to the number of such edges.
"""
from collections import defaultdict

from graphs.bag import Bag


class FlowNetwork:

    def __init__(self, v, e=0):
        if v < 0:
            raise AttributeError('Number of vertices in a Graph must be nonnegative')
        self._v = v
        self._e = e
        self._adj = defaultdict(Bag)
        for vertice in range(v):
            self._adj[vertice] = Bag()

    def get_V(self):
        return self._v

    def get_E(self):
        return self._e

    def __validate_vertex(self, v):
        n = self._v
        if v < 0 or v >= n:
            raise AttributeError(f'vertex {v} is not between 0 and {n - 1}')

    def add_edge(self, e):
        v = e.tail()
        w = e.head()
        self.__validate_vertex(v)
        self.__validate_vertex(w)
        self._adj[v].add(e)
        self._adj[w].add(e)
        self._e += 1

    def adj(self, v):
        self.__validate_vertex(v)
        return self._adj[v]

    def edges(self):
        flow_edge_list = Bag()
        for v in range(self._v):
            for e in self.adj(v):
                if e.head() != v:
                    flow_edge_list.add(e)
        return flow_edge_list

    def __str__(self):
        s = f""
        s += f"{self._v} {self._e}\n"
        for v in range(self._v):
            s += f"{v}: "
            for e in self._adj[v]:
                if e.item.head() != v:
                    s += f"{e} "
            s += "\n"
        return s

    # def __repr__(self):
    #     return f'<{self.__class__.__name__}(_adj={self._adj})>'
