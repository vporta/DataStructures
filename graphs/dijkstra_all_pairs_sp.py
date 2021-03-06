"""
dijkstra_all_pairs_sp.py
Dijkstra's algorithm run from each vertex.
 *  Takes time proportional to E V log V and space proportional to EV.
The DijkstraAllPairsSP class represents a data type for solving the
 *  all-pairs shortest paths problem in edge-weighted digraphs
 *  where the edge weights are non-negative.
 *
 *  This implementation runs Dijkstra's algorithm from each vertex.
 *  The constructor takes Theta(V (E log V)) time
 *  in the worst case, where V is the number of vertices and
 *  E is the number of edges.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(V2) extra space (not including the
 *  edge-weighted digraph).
"""
import math

from graphs.directed_edge import DirectedEdge
from graphs.edge_weighted_digraph import EdgeWeightedDigraph
from graphs.dijkstra_sp import DijkstraSP


class DijkstraAllPairsSP:

    _all = list()

    def __init__(self, g):

        self._all = [DijkstraSP(g, v) for v in range(g.get_V())]

    def path(self, s, t):
        self.__validate_vertex(s)
        self.__validate_vertex(t)
        return self._all[s].path_to(t)

    def has_path(self, s, t):
        self.__validate_vertex(s)
        self.__validate_vertex(t)
        return self.dist(s, t) < math.inf

    def dist(self, s, t):
        self.__validate_vertex(s)
        self.__validate_vertex(t)
        return self._all[s].dist_to(t)

    def __validate_vertex(self, v):
        n = len(self._all)
        if v < 0 or v >= n:
            raise AttributeError(f'vertex {v} is not between 0 and {n - 1}')

    def __repr__(self):
        return f'<{self.__class__.__name__}(\n' \
               f'_all={self._all}\n)>'


def main():
    with open("../resources/tinyEWD.txt", ) as f:
        values = "".join(f.readlines()).splitlines()
        V, E = int(values[0]), int(values[1])
        g = EdgeWeightedDigraph(V)
        for line in values[2:]:
            vertices = line.split(' ')
            v, w, weight = int(vertices[0]), int(vertices[1]), float(vertices[2])
            e = DirectedEdge(v, w, weight)
            g.add_edge(e)

    dijkstra = DijkstraAllPairsSP(g)
    print(dijkstra)

if __name__ == '__main__':
    main()
