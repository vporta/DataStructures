"""
BipartiteMatching.py
 *  Find a maximum cardinality matching (and minimum cardinality vertex cover)
 *  in a bipartite graph using the alternating path algorithm.
 *  The BipartiteMatching class represents a data type for computing a
 *  maximum (cardinality) matching and a
 *  minimum (cardinality) vertex cover in a bipartite graph.
 *  A bipartite graph in a graph whose vertices can be partitioned
 *  into two disjoint sets such that every edge has one endpoint in either set.
 *  A matching in a graph is a subset of its edges with no common
 *  vertices. A maximum matching is a matching with the maximum number
 *  of edges.
 *  A perfect matching is a matching which matches all vertices in the graph.
 *  A vertex cover in a graph is a subset of its vertices such that
 *  every edge is incident to at least one vertex. A minimum vertex cover
 *  is a vertex cover with the minimum number of vertices.
 *  By Konig's theorem, in any biparite
 *  graph, the maximum number of edges in matching equals the minimum number
 *  of vertices in a vertex cover.
 *  The maximum matching problem in nonbipartite graphs is
 *  also important, but all known algorithms for this more general problem
 *  are substantially more complicated.
 *
 *  This implementation uses the alternating-path algorithm.
 *  It is equivalent to reducing to the maximum-flow problem and running
 *  the augmenting-path algorithm on the resulting flow network, but it
 *  does so with less overhead.
 *  The constructor takes O((E + V) V)
 *  time, where E is the number of edges and V is the
 *  number of vertices in the graph.
 *  It uses Theta(V) extra space (not including the graph).
 *
"""
from Graphs.BipartiteX import BipartiteX
from queue import Queue
from Graphs.Graph import Graph
import random


class BipartiteMatching:

    UNMATCHED = -1
    _cardinality = 0
    _marked = None
    _edge_to = None

    def __init__(self, g):
        self._g = g
        self._bipartition = BipartiteX(g)
        if not self._bipartition.get_is_bipartite():
            raise AttributeError('graph is not bipartite')
        self._V = g.get_V()
        self._mate = [self.UNMATCHED] * self._V

        # alternating path algorithm
        while self.__has_augmented_path(g):
            # find one endpoint t in alternating path
            t = -1
            for v in range(self._V):
                if not self.is_matched(v) and self._edge_to[v] != -1:
                    t = v
                    break
            # update the matching according to alternating path in edgeTo[] array
            v = t
            while v != -1:
                w = self._edge_to[v]
                self._mate[v] = w
                self._mate[w] = v
                v = self._edge_to[self._edge_to[v]]
            self._cardinality += 1

        # find min vertex cover from marked[] array
        self._in_min_vertex_cover = [False] * self._V
        for v in range(self._V):
            if self._bipartition.color(v) and not self._marked[v]:
                self._in_min_vertex_cover[v] = True
            if not self._bipartition.color(v) and self._marked[v]:
                self._in_min_vertex_cover[v] = True

    def __has_augmented_path(self, g):
        self._marked = [False] * self._V
        self._edge_to = [-1] * self._V

        # breadth-first search (starting from all unmatched vertices on one side of bipartition)
        queue = Queue()
        for v in range(self._V):
            if self._bipartition.color(v) and not self.is_matched(v):
                self._marked[v] = True
                queue.put(v)
        # run BFS, stopping as soon as an alternating path is found
        while not queue.empty():
            v = queue.get()
            for w in g.adj_vertices(v):
                # either (1) forward edge not in matching or (2) backward edge in matching
                if self.is_residual_graph_edge(v, w.item) and not self._marked[w.item]:
                    self._edge_to[w.item] = v
                    self._marked[w.item] = True
                    if not self.is_matched(w.item):
                        return True
                    queue.put(w)
        return False

    def is_residual_graph_edge(self, v, w):
        if self._mate[v] != w and self._bipartition.color(v):
            return True
        if self._mate[v] == w and not self._bipartition.color(v):
            return True
        return False

    def is_matched(self, v):
        self.__validate(v)
        return self._mate[v] != self.UNMATCHED

    def mate(self, v):
        self.__validate(v)
        return self._mate[v]

    def size(self):
        return self._cardinality

    def is_perfect(self):
        return self._cardinality * 2 == self._V

    def in_min_vertex_cover(self, v):
        self.__validate(v)
        return self._in_min_vertex_cover[v]

    def __validate(self, v):
        if v < 0 or v >= self._V:
            raise Exception("vertex " + v + " is not between 0 and " + (self._V - 1))


def bipartite_generator(v1, v2, p):

    def bernoulli(_p=0.5):
        if _p < 0 or _p > 1.0:
            raise AttributeError('probability must be between 0 and 1')
        return random.uniform(0, 1) < _p

    vertices = [i for i in range(v1 + v2)]
    random.shuffle(vertices)
    g = Graph(v1+v2)
    for i in range(v1):
        for j in range(v2):
            if bernoulli(p):
                g.add_edge(vertices[i], vertices[v1 + j])
    return g


def main():
    g = bipartite_generator(10, 10, .5)

    if g.get_V() < 1000:
        print(g)
    matching = BipartiteMatching(g)

    print('matching')
    print(f'number of edges in max matching:  {matching.size()}')
    print(f'number of vertices in min vertex cover:  {matching.size()}')
    print(f'graph has a perfect:  {matching.is_perfect()}')
    print()
    if g.get_V() >= 1000:
        return
    print('max matching: ')
    for v in range(g.get_V()):
        w = matching.mate(v)
        if matching.is_matched(v) and v < w:  # print each edge only once
            print(f'{v}-{w}  ')
    print()

    print('min vertex cover:  ')
    for v in range(g.get_V()):
        if matching.in_min_vertex_cover(v):
            print(f'{v}  ')
    print()


if __name__ == '__main__':
    main()