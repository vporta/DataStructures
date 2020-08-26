"""
PrimMST.py
Compute a minimum spanning forest using Prim's algorithm.

The PrimMST class represents a data type for computing a
 *  minimum spanning tree in an edge-weighted graph.
 *  The edge weights can be positive, zero, or negative and need not
 *  be distinct. If the graph is not connected, it computes a minimum
 *  spanning forest, which is the union of minimum spanning trees
 *  in each connected component. The weight() method returns the
 *  weight of a minimum spanning tree and the edges() method
 *  returns its edges.
 *
 *  This implementation uses Prim's algorithm with an indexed
 *  binary heap.
 *  The constructor takes Theta(E log V) time in
 *  the worst case, where V is the number of
 *  vertices and E is the number of edges.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(V) extra space (not including the
 *  edge-weighted graph).
"""
from Graphs.EdgeWeightedGraph import EdgeWeightedGraph
from Graphs.Edge import Edge
from queue import Queue
from Queues.IndexMinPQ import IndexMinPQ
import math


class PrimMST:

    _weight = 0

    def __init__(self, g: EdgeWeightedGraph):
        self._g = g
        self._pq = IndexMinPQ(g.get_V())  # priority queue
        self._dist_to = [math.inf for _ in range(g.get_V())]
        self._edge_to = [Edge() for _ in range(g.get_V())]
        self._marked = [False for _ in range(g.get_V())]

        for v in range(g.get_V()):
            if not self._marked[v]:
                self.__prim(g, v)

        # 1.0. Start with vertex 0, and greedily grow tree sorted by Edge weights
        # 2.0. Add to _mst the min Edge weight with *exactly one endpoint in _mst*
        #   2.1 Delete min priority vertex v from the pq
        #   2.2 Add its associated edge e = v-w to tree _edge_to[]
        #   2.3 Update pq by considering all edges e = v-x incident to v
        #       2.3.0. if x is already in tree, ignore x
        #       2.3.1. if x is not already in tree, add x to pq
        #       2.3.2. decrease priority of x, if v-x becomes shortest edge
        # 3.0. Repeat until V-1 edges

    def __prim(self, g, s):
        self._dist_to[s] = 0.0
        self._pq.insert(s, self._dist_to[s])
        while not self._pq.is_empty():
            v = self._pq.del_min()
            self.__scan(g, v)

    def __scan(self, g, v):
        self._marked[v] = True
        for e in g.adj_vertices(v):
            x = e.item.other(v)
            if self._marked[x]:
                continue
            if e.item.weight() < self._dist_to[x]:
                self._dist_to[x] = e.item.weight()
                self._edge_to[x] = e.item
                if self._pq.contains(x):
                    self._pq.decrease_key(x, self._dist_to[x])
                else:
                    self._pq.insert(x, self._dist_to[x])

    def edges(self):
        mst = Queue()
        for v in range(len(self._edge_to)):
            e = self._edge_to[v]
            if e is not None:
                mst.put(e)
        return mst

    def weight(self):
        weight = 0.0
        for e in self.edges().queue:
            weight += e.weight()
        return weight

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'g={self._g}, ' \
               f'_pq={self._pq}, ' \
               f'_dist_to={self._dist_to}' \
               f'_edge_to={self._edge_to})>'


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
    mst = PrimMST(g)
    print(mst)
    q = mst.edges()
    while not q.empty():
        print(q.get())


if __name__ == '__main__':
    main()