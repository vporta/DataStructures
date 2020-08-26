"""
DijkstraSP.py
Dijkstra's algorithm. Computes the shortest path tree.
 *  Assumes all weights are non-negative.
 The  DijkstraSP class represents a data type for solving the
 *  single-source shortest paths problem in edge-weighted digraphs
 *  where the edge weights are non-negative.
 *
 *  This implementation uses Dijkstra's algorithm with a
 *  binary heap. The constructor takes
 *  Theta(E log V) time in the worst case,
 *  where V is the number of vertices and E is
 *  the number of edges. Each instance method takes Theta(1) time.
 *  It uses Theta(V) extra space (not including the
 *  edge-weighted digraph).
"""
from Graphs.DirectedEdge import DirectedEdge
from Graphs.EdgeWeightedDigraph import EdgeWeightedDigraph
from queue import LifoQueue
import math
import heapq


class DijkstraSP:

    def __init__(self, g: EdgeWeightedDigraph, s: int):
        for e in g.edges():
            edge_weight = e.item.item.weight()
            if edge_weight < 0:
                raise ValueError(f'edge {e} has negative weight')
        self._g = g
        self._s = s
        self._edge_to = [None] * g.get_V()
        self._dist_to = [math.inf] * g.get_V()
        self._dist_to[s] = 0.0
        self._spt = [False] * g.get_V()
        self._on_queue = [False] * g.get_V()
        self.__validate_vertex(s)

        self._pq = list()
        heapq.heappush(self._pq, (self._dist_to[s], s))
        self._on_queue[s] = True

        while len(self._pq) > 0:
            current_distance, v = heapq.heappop(self._pq)
            self._on_queue[v] = False
            for e in g.adj_vertices(v):
                self.__relax(e)

    def __relax(self, e):
        v, w = e.item.tail(), e.item.head()
        # optimality condition: dist_to[w] <= dist_to[v] + e.weight()
        if self._dist_to[w] > self._dist_to[v] + e.item.weight():
            # if the edge v->w gives a shorter path to w from v,
            # then update dist_to[w] and edge_to[w]
            self._dist_to[w] = self._dist_to[v] + e.item.weight()
            self._edge_to[w] = e.item

            if self._on_queue[w]:
                # decrease-key: heapq._siftdown(pq, startpos, pos)
                print(w, self._pq)
            else:
                heapq.heappush(self._pq, (self._dist_to[w], w))

    def dist_to(self, v):
        self.__validate_vertex(v)
        return self._dist_to[v]

    def has_path_to(self, v):
        self.__validate_vertex(v)
        return self._dist_to[v] < math.inf

    def path_to(self, v):
        self.__validate_vertex(v)
        if not self.has_path_to(v):
            return None
        path = LifoQueue()  # stack
        e = self._edge_to[v]
        while e is not None:
            path.put(e)
            e = self._edge_to[e.tail()]
        return path

    def __validate_vertex(self, v):
        n = len(self._dist_to)
        if v < 0 or v >= n:
            raise AttributeError(f'vertex {v} is not between 0 and {n - 1}')

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'_g={self._g}, \n' \
               f'_pq={self._pq}, \n' \
               f'_dist_to={self._dist_to}, \n' \
               f'_edge_to={self._edge_to})>'


def main():
    with open("../Resources/tinyEWD.txt", ) as f:
        values = "".join(f.readlines()).splitlines()
        V, E = int(values[0]), int(values[1])
        g = EdgeWeightedDigraph(V)
        for line in values[2:]:
            vertices = line.split(' ')
            v, w, weight = int(vertices[0]), int(vertices[1]), float(vertices[2])
            e = DirectedEdge(v, w, weight)
            g.add_edge(e)
    s = 0
    dijkstra = DijkstraSP(g, s)
    print(dijkstra)

    for t in range(g.get_V()):
        if dijkstra.has_path_to(t):
            print(f'{s} to {t} ({dijkstra.dist_to(t)})')
            q = dijkstra.path_to(t)
            while not q.empty():
                print(q.get())
            print()
        else:
            print(f'{s} to {t} no path\n')


if __name__ == '__main__':
    main()
