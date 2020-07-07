"""
EdgeWeightedDigraph.py
An edge-weighted digraph, implemented using adjacency lists.
The EdgeWeightedDigraph class represents a edge-weighted
 *  digraph of vertices named 0 through V - 1, where each
 *  directed edge is of type DirectedEdge and has a real-valued weight.

 *  It supports the following two primary operations:
        1. add a directed edge to the digraph
        2. iterate over all of edges incident from a given vertex.

 *  It also provides methods for returning the indegree or outdegree of a
 *  vertex, the number of vertices V in the digraph, and
 *  the number of edges E in the digraph.
 *  Parallel edges and self-loops are permitted.

 *  This implementation uses an adjacency-lists representation, which
 *  is a vertex-indexed array of Bag objects.
 *  It uses Theta(E + V) space, where E is
 *  the number of edges and V is the number of vertices.
 *  All instance methods take Theta(1) time. (Though, iterating over
 *  the edges returned by #adj(int) takes time proportional
 *  to the outdegree of the vertex.)
 *  Constructing an empty edge-weighted digraph with V vertices
 *  takes Theta(V) time constructing an edge-weighted digraph
 *  with E edges and V vertices takes
 *  Theta(E + V) time.
"""

from Graphs.Bag import Bag
from Graphs.DirectedEdge import DirectedEdge
from collections import defaultdict
import random


class EdgeWeightDigraph:

    def __init__(self, v):
        """
        Initializes an empty graph with V vertices and 0 edges.
        :param v: the number of vertices
        """
        if v < 0:
            raise ValueError('Number of vertices in Digraph must be non-negative')
        self.V = v
        self.E = 0
        self._indegree = [0 for _ in range(v)]
        self.adj = defaultdict(Bag)
        for v in range(v):
            self.adj[v] = Bag()

    # Initializes a random edge-weighted digraph
    # def __init__(self, v, e):
    #     """
    #     Initializes an empty graph with V vertices and E edges.
    #     :param v: the number of vertices
    #     """
    #     if v < 0:
    #         raise ValueError('Number of vertices in Digraph must be non-negative')
    #     self.V = v
    #     if e < 0:
    #         raise ValueError('Number of edges in Digraph must be non-negative')
    #     self.E = e
    #     for _ in range(e):
    #         v = random.uniform(v)
    #         w = random.uniform(v)
    #         weight = 0.01 * random.uniform(100)
    #         edge = DirectedEdge(v, w, weight)
    #         self.add_edge(edge)
    #     self._indegree = [0 for _ in range(v)]
    #     self.adj = defaultdict(Bag)

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

    def add_edge(self, e):
        v = e.tail()  # from
        w = e.head()  # to
        self._validate_vertex(v)
        self._validate_vertex(w)
        self.adj[v].add(e)
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

    def edges(self):
        adj_list = Bag()
        for v in range(self.get_V()):
            for e in self.adj_vertices(v):
                adj_list.add(e)
        return adj_list

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'V={self.get_V()}, ' \
               f'E={self.get_E()}, ' \
               f'adj={self.adj})>'

    def __str__(self):
        s = f'{self.get_V()} {self.get_E()}\n'
        for v in range(self.get_V()):
            s += f'{v}: '
            for e in self.adj_vertices(v):
                s += f'{e} '
            s += '\n'
        return s


def main():
    g = EdgeWeightDigraph(8)
    with open("../resources/tinyEWD.txt", ) as f:
        for line in f.readlines():
            vertices = " ".join(line.splitlines()).split(' ')
            if len(vertices) < 3:
                continue
            else:
                v, w, weight = int(vertices[0]), int(vertices[1]), float(vertices[2])
                e = DirectedEdge(v, w, weight)
                g.add_edge(e)

    print(g)
    print(str(g))


if __name__ == '__main__':
    main()



