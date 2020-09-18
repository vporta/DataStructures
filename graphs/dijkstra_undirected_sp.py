"""
dijkstra_undirected_sp.py
Dijkstra's algorithm. Computes the shortest path tree.
 *  Assumes all weights are nonnegative.
The DijkstraUndirectedSP class represents a data type for solving
 *  the single-source shortest paths problem in edge-weighted graphs
 *  where the edge weights are non-negative.
 *
 *  This implementation uses Dijkstra's algorithm with a binary heap.
 *  The constructor takes Theta(E log V) time in the
 *  worst case, where V is the number of vertices and
 *  E is the number of edges.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(V) extra space (not including the
 *  edge-weighted graph).
"""
from graphs.edge_weighted_graph import EdgeWeightedGraph
from graphs.edge import Edge
from queue import LifoQueue
import heapq
import math


class DijkstraUndirectedSP:

    def __init__(self, g: EdgeWeightedGraph, s: int):
        for e in g.edges():
            edge_weight = e.item.weight()
            if edge_weight < 0:
                raise ValueError(f'edge {e} has negative weight')

        self._g = g
        self._s = s
        self._dist_to = [math.inf] * g.get_V()
        self._edge_to = [None] * g.get_V()

        self.__validate_vertex(s)
        self._dist_to[s] = 0.0
        self._pq = list()
        heapq.heappush(self._pq, (self._dist_to[s], s))

        while len(self._pq) > 0:
            current_distance, v = heapq.heappop(self._pq)
            for e in g.adj_vertices(v):
                self.__relax(e, v)

    def __relax(self, e, v):
        w = e.item.other(v)
        if self._dist_to[w] > self._dist_to[v] + e.item.weight():
            self._dist_to[w] = self._dist_to[v] + e.item.weight()
            self._edge_to[w] = e.item
            if w in [k for j, k in self._pq]:
                print(w, self._pq)
            else:
                heapq.heappush(self._pq, (self._dist_to[w], w))

    def has_path_to(self, v):
        self.__validate_vertex(v)
        return self._dist_to[v] < math.inf

    def path_to(self, v):
        self.__validate_vertex(v)
        if not self.has_path_to(v):
            return None
        x = v
        e = self._edge_to[v]
        path = LifoQueue()
        while e is not None:
            path.put(e)
            x = e.other(x)
            e = self._edge_to[x]
        return path

    def dist_to(self, v):
        self.__validate_vertex(v)
        return self._dist_to[v]

    def __validate_vertex(self, v):
        n = len(self._dist_to)
        if v < 0 or v > n:
            raise AttributeError(f'vertex {v} is not between 0 and {n - 1})')

    def __repr__(self):
        return f'<{self.__class__.__name__}(\n' \
               f'_g={self._g}, \n' \
               f'_pq={self._pq}, \n' \
               f'_dist_to={self._dist_to}, \n' \
               f'_edge_to={self._edge_to})>'

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
    s = 6
    sp = DijkstraUndirectedSP(g, s)
    print(sp)
    for t in range(g.get_V()):
        if sp.has_path_to(t):
            print(f'{s} to {t} ({sp.dist_to(t)})')
            q = sp.path_to(t)
            while not q.empty():
                print(q.get())
            print()
        else:
            print(f'{s} to {t} no path\n')


if __name__ == '__main__':
    main()

