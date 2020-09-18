"""
lazy_prim_mst.py
 *  Compute a minimum spanning forest using a lazy version of Prim's Algorithm
The LazyPrimMST class represents a data type for computing a
 *  minimum spanning tree in an edge-weighted graph.
 *  The edge weights can be positive, zero, or negative and need not
 *  be distinct. If the graph is not connected, it computes a minimum
 *  spanning forest, which is the union of minimum spanning trees
 *  in each connected component. The weight() method returns the
 *  weight of a minimum spanning tree and the edges() method
 *  returns its edges.
 *
 *  This implementation uses a lazy version of Prim's algorithm
 *  with a binary heap of edges.

 *  The constructor takes Theta(E log E) time in
 *  the worst case, where V is the number of vertices and
 *  E is the number of edges.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(E) extra space in the worst case
 *  (not including the edge-weighted graph).
"""
from heapq import *
from graphs.edge import Edge
from graphs.edge_weighted_graph import EdgeWeightedGraph
from queue import Queue

from unionfind.uf import UF


class LazyPrimMST:

    FLOATING_POINT_EPSILON = 1E-12
    _weight = 0

    def __init__(self, g: EdgeWeightedGraph):
        self._g = g
        self._mst = Queue()
        self._pq = list()
        self._marked = [False] * g.get_V()
        for v in range(g.get_V()):
            if not self._marked[v]:
                self.__prim(g, v)

        assert self.__check(g)

    def __prim(self, g, s):
        self.__scan(g, s)  # marked vertices as visited and populated pq w/ every edge v-w (w not visited) incident to v
        while self._pq:
            e = heappop(self._pq)
            print(e)
            v = e.either()
            w = e.other(v)
            assert self._marked[v] or self._marked[w]
            # disregard if both endpoints are in tree already i.e. "Lazy"
            if self._marked[v] and self._marked[w]:
                continue
            # otherwise let w be the vertex not in tree
            self._mst.put(e)
            self._weight += e.weight()
            if not self._marked[v]:
                self.__scan(g, v)  # v becomes part of the tree
            if not self._marked[w]:
                self.__scan(g, w)  # w becomes part of the tree

    def __scan(self, g, v):
        assert not self._marked[v]
        self._marked[v] = True
        for e in g.adj_vertices(v):
            w = e.item.other(v)
            if not self._marked[w]:
                heappush(self._pq, e.item)

    def edges(self):
        return self._mst.queue

    def weight(self):
        return self._weight

    def __check(self, g):
        total = 0.0
        for e in self.edges():
            total += e.weight()
        if abs(total - self.weight()) > LazyPrimMST.FLOATING_POINT_EPSILON:
            print(f'Weight of edges does not equal weight(): {total} vs {self.weight()}')
            return False

        uf = UF(g.get_V())
        # check that it is acyclic
        for e in self.edges():
            v = e.either()
            w = e.other(v)
            if uf.find(v) == uf.find(w):
                print(f'not a forest')
                return False
            uf.union(v, w)
        # check that it is a spanning forest
        for e in g.edges():
            v = e.item.either()
            w = e.item.other(v)
            if uf.find(v) != uf.find(w):
                print(f'not a spanning forest')
                return False
        # check that it is a minimal spanning forest (cut optimality conditions)
        for e in self.edges():
            uf = UF(g.get_V())
            for f in self._mst.queue:
                x = f.either()
                y = f.other(x)
                if f != e:
                    uf.union(x, y)
            for f in g.edges():
                x = f.item.either()
                y = f.item.other(x)
                if uf.find(x) != uf.find(y):
                    if f.item.weight() < e.weight():
                        print(f'Edge {f} violates cut optimality conditions')
                        return False

        return True

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'_pq={self._pq}, ' \
               f'_marked={self._marked}' \
               f'_mst={self._mst.queue})>'


def main():
    with open("../resources/tinyEWG.txt", ) as f:
        values = "".join(f.readlines()).splitlines()
        V, E = int(values[0]), int(values[1])
        g = EdgeWeightedGraph(V)
        for line in values[2:]:
            vertices = line.split(' ')
            v, w, weight = int(vertices[0]), int(vertices[1]), float(vertices[2])
            e = Edge(v, w, weight)
            g.add_edge(e)
    print(g)
    mst = LazyPrimMST(g)
    print(mst)
    for e in mst.edges():
        print(e)


if __name__ == '__main__':
    main()