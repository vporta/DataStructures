"""
EdgeWeightedGraph.py
An edge-weighted undirected graph, implemented using adjacency lists.
 *  Parallel edges and self-loops are permitted.
The EdgeWeightedGraph class represents an edge-weighted
 *  graph of vertices named 0 through V – 1, where each
 *  undirected edge is of type Edge and has a real-valued weight.
 *  It supports the following two primary operations: add an edge to the graph,
 *  iterate over all of the edges incident to a vertex. It also provides
 *  methods for returning the degree of a vertex, the number of vertices
 *  V in the graph, and the number of edges E in the graph.
 *  Parallel edges and self-loops are permitted.
 *  By convention, a self-loop v-v appears in the
 *  adjacency list of v twice and contributes two to the degree
 *  of v.
 *
 *  This implementation uses an adjacency-lists representation, which
 *  is a vertex-indexed array of Bag objects.
 *  It uses Theta(E + V) space, where E is
 *  the number of edges and V is the number of vertices.
 *  All instance methods take Theta(1) time. (Though, iterating over
 *  the edges returned by #adj(int) takes time proportional
 *  to the degree of the vertex.)
 *  Constructing an empty edge-weighted graph with V vertices takes
 *  Theta(V) time constructing a edge-weighted graph with
 *  E edges and V vertices takes
 *  Theta(E + V) time.
"""
from Graphs.Edge import Edge
from Graphs.Bag import Bag
from collections import defaultdict


class EdgeWeightedGraph:

    def __init__(self, v):
        if v < 0:
            raise AttributeError('Number of vertices must be non-negative')
        self.V = v
        self.E = 0
        self.adj = defaultdict(Bag)
        for i in range(v):
            self.adj[i] = Bag()

    def adj_vertices(self, v):
        self.__validate_vertex(v)
        return self.adj[v]

    # outdegree i.e. size of Bag (LL of Nodes)
    def degree(self, v):
        self.__validate_vertex(v)
        return self.adj[v].size()

    def add_edge(self, e: Edge):
        v = e.either()
        w = e.other(v)
        self.__validate_vertex(v)
        self.__validate_vertex(w)
        self.adj[v].add(e)
        self.adj[w].add(e)
        self.E += 1

    def get_V(self):
        return self.V

    def get_E(self):
        return self.E

    def edges(self):
        adj_list = Bag()
        for v in range(self.get_V()):
            self_loops = 0
            for e in self.adj_vertices(v):
                if e.item.other(v) > v:  # if e.v == v, return e.w; if e.w == v, return e.v
                    adj_list.add(e.item)
                # add only one copy of each self loop (self loops will be consecutive)
                elif e.item.other(v) == v:
                    if self_loops % 2 == 0:
                        adj_list.add(e.item)
                    self_loops += 1
        return adj_list

    def __validate_vertex(self, v):
        if v < 0 or v >= self.V:
            raise ValueError(f'vertex {v} is not between 0 and {self.V - 1}')

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'V={self.get_V()}, ' \
               f'E={self.get_E()}, ' \
               f'adj={self.adj})>,' \
               f'edges={self.edges()}'

    def __str__(self):
        s = f'\n    v={self.get_V()},\n    e={self.get_E()},\n'
        for v in range(self.get_V()):
            s += f'     {v}: '
            for e in self.adj_vertices(v):
                s += f'     {e} '
            s += '\n'
        return s


def main():
    with open("../Resources/tinyEWG.txt", ) as f:
        values = "".join(f.readlines()).splitlines()
        V, E = int(values[0]), int(values[1])
        g = EdgeWeightedGraph(V)
        for line in values[2:]:
            vertices = line.split(' ')
            v, w, weight = int(vertices[0]), int(vertices[1]), float(vertices[2])
            e = Edge(v, w, weight)
            g.add_edge(e)
    print(g)


if __name__ == '__main__':
    main()