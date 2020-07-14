"""
KruskalMST.py
Compute a minimum spanning forest using Kruskal's algorithm.
The KruskalMST class represents a data type for computing a
 *  minimum spanning tree in an edge-weighted graph.
 *  The edge weights can be positive, zero, or negative and need not
 *  be distinct. If the graph is not connected, it computes a minimum
 *  spanning forest, which is the union of minimum spanning trees
 *  in each connected component. The weight() method returns the
 *  weight of a minimum spanning tree and the edges() method
 *  returns its edges.
 *
 *  This implementation uses Krusal's algorithm and the
 *  union-find data type.
 *  The constructor takes Theta(E log E) time in
 *  the worst case.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(E) extra space (not including the graph).
"""
import heapq
from Graphs.Edge import Edge
from Graphs.EdgeWeightedGraph import EdgeWeightedGraph
from queue import Queue
from UnionFindAlgorithms.UF import UF


class KruskalMST:
    FLOATING_POINT_EPSILON = 1E-12
    _weight = 0
    _mst = Queue()

    def __init__(self, g: EdgeWeightedGraph):
        self._pq = []  # min priority queue sorted by edge weights
        for e in g.edges():
            heapq.heappush(self._pq, e.item)
        uf = UF(g.get_V())
        while self._pq and self._mst.qsize() < g.get_V() - 1:
            e = heapq.heappop(self._pq)
            v = e.either()
            w = e.other(v)
            if not uf.connected(v, w):
                uf.union(v, w)
                self._mst.put(e)
                self._weight += e.weight()

        assert self.__check(g)

    def edges(self):
        return self._mst.queue

    def weight(self):
        return self._weight

    def __check(self, g):
        total = 0.0
        for e in self.edges():
            total += e.weight()
        if abs(total - self.weight()) > KruskalMST.FLOATING_POINT_EPSILON:
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
        return f'<{self.__class__.__name__}(_pq={self._pq}, weight={self.weight()}, _mst={self._mst.queue})>'




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
    mst = KruskalMST(g)
    print(mst)


if __name__ == '__main__':
    main()










