"""
AcyclicSP.py
Computes shortest paths in an edge-weighted acyclic digraph
"""
from queue import LifoQueue
from Graphs.DirectedEdge import DirectedEdge
from Graphs.EdgeWeightedDigraph import EdgeWeightedDigraph
import math
from Graphs.Topological import Topological


class AcyclicSP:

    def __init__(self, g: EdgeWeightedDigraph, s: int):
        self._dist_to = [math.inf] * g.get_V()
        self._edge_to = [None] * g.get_V()
        self._g = g
        self.__validate_vertex(s)
        self._s = s
        self._dist_to[s] = 0.0

        top_order = Topological(g)
        if not top_order.has_order():
            raise ValueError('Digraph is not acyclic')
        else:
            for v in top_order.order():
                for e in g.adj_vertices(v):
                    self.__relax(e)

    def __relax(self, e):
        v = e.item.tail()
        w = e.item.head()
        if self._dist_to[w] > self._dist_to[v] + e.item.weight():
            self._dist_to[w] = self._dist_to[v] + e.item.weight()
            self._edge_to[w] = e.item

    def dist_to(self, v):
        self.__validate_vertex(v)
        return self._dist_to[v]

    def has_path_to(self, v):
        self.__validate_vertex(v)
        return self._dist_to[v] < math.inf

    def path_to(self, v):
        self.__validate_vertex(v)
        e = self._edge_to[v]
        path = LifoQueue()
        while e is not None:
            path.put(e)
            e = self._edge_to[e.tail()]
        return path

    def __validate_vertex(self, v):
        n = len(self._dist_to)
        if v < 0 or v >= n:
            raise AttributeError(f'vertex {v} is not between 0 and {n - 1}')

    def __repr__(self):
        return f'<{self.__class__.__name__}(\n' \
               f'_dist_to={self._dist_to}, \n' \
               f'_edge_to={self._edge_to})>'


def main():
    with open("../resources/tinyEWDAG.txt", ) as f:
        values = "".join(f.readlines()).splitlines()
        V, E = int(values[0]), int(values[1])
        g = EdgeWeightedDigraph(V)
        for line in values[2:]:
            vertices = line.split(' ')
            v, w, weight = int(vertices[0]), int(vertices[1]), float(vertices[2])
            e = DirectedEdge(v, w, weight)
            g.add_edge(e)
    s = 5
    asp = AcyclicSP(g, s)
    for t in range(g.get_V()):
        if asp.has_path_to(t):
            print(f'{s} to {t} ({asp.dist_to(t)}) ', end="")
            q = asp.path_to(t)
            while not q.empty():
                print(q.get())
            print()
        else:
            print(f'{s} to {t} no path\n')


if __name__ == '__main__':
    main()



