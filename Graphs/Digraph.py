"""
Digraph.py
The Digraph class represents a directed graph of vertices
 *  named 0 through V - 1.
 *  It supports the following two primary operations: add an edge to the digraph,
 *  iterate over all of the vertices adjacent from a given vertex.
 *  It also provides
 *  methods for returning the indegree or outdegree of a vertex,
 *  the number of vertices V in the digraph,
 *  the number of edges E in the digraph, and the reverse digraph.
 *  Parallel edges and self-loops are permitted.
 *
 *  This implementation uses an adjacency-lists representation, which
 *  is a vertex-indexed array of Bag objects.
 *  It uses Theta(E + V) space, where E is
 *  the number of edges and V is the number of vertices.
 *  All instance methods take Theta(1) time. (Though, iterating over
 *  the vertices returned by adj(int) takes time proportional
 *  to the outdegree of the vertex.)
 *  Constructing an empty digraph with V vertices takes
 *  Theta(V) time constructing a digraph with E edges
 *  and V vertices takes Theta(E + V) time.
 *
"""
from Graphs.Graph import Graph
from Graphs.Bag import Bag
from collections import deque, defaultdict


class Digraph:

    def __init__(self, v):
        """
        Initializes an empty graph with V vertices and 0 edges.
        :param v: the number of vertices
        """
        if v < 0:
            raise ValueError('Number of vertices must be non-negative')
        self.V = v
        self.E = 0
        self._indegree = [0 for _ in range(v)]
        self.adj = defaultdict(Bag)
        for v in range(v):
            self.adj[v] = Bag()

    def get_V(self):
        """
        :returns: the number of vertices in this graph
        """
        return self.V

    def get_E(self):
        """
        :returns: the number of edges in this graph
        """
        return self.E

    def _validate_vertex(self, v):
        """
        Throw a ValueError exception if 0 <= v < V
        :param v: vertex v
        """
        if v < 0 or v >= self.V:
            raise ValueError(f'vertex {v} is not between 0 and {self.V - 1}')

    def add_edge(self, v, w):
        self._validate_vertex(v)
        self._validate_vertex(w)
        self.adj[v].add(w)
        self.get_indegree()[w] += 1
        self.E += 1

    def adj_vertices(self, v):
        """
        Returns the vertices adjacent to the vertex {v}
        :param v: v the vertex
        :returns: the vertices adjacent to vertex {v}
        """
        self._validate_vertex(v)
        return self.adj[v]

    def get_indegree(self):
        return self._indegree

    def indegree(self, v=0):
        self._validate_vertex(v)
        return self._indegree[v]

    def get_outdegree(self):
        return self.outdegree()

    def outdegree(self, v=0):
        self._validate_vertex(v)
        return self.adj[v].size()

    def reverse(self):
        reverse = Digraph(self.get_V())
        for v in range(self.get_V()):
            for w in self.adj_vertices(v):
                reverse.add_edge(w.item, v)
        return reverse

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'V={self.get_V()}, ' \
               f'E={self.get_E()}, ' \
               f'adj={self.adj})>'


def main():
    g = Digraph(4)
    print(g)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    print(g)
    print(g.get_V())
    print(f'adjacent vertices of 2 are: {g.adj_vertices(2)}')
    print(f'indegree of 2 is: {g.indegree(2)}')
    print(f'outdegree of 2 is: {g.outdegree(2)}')


if __name__ == '__main__':
    main()








