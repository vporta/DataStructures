"""
BreadthFirstPaths.py
The BreadthFirstPaths class represents a data type for finding
 *  shortest paths (number of edges) from a source vertex s
 *  (or a set of source vertices)
 *  to every other vertex in an undirected graph.
 *
 *  This implementation uses breadth-first search.
 *  The constructor takes Theta;(V + E) time in the
 *  worst case, where V is the number of vertices and E
 *  is the number of edges.
 *  Each instance method takes Theta;(1) time.
 *  It uses Theta;(V) extra space (not including the graph).

"""
from collections import deque
from Graphs.Graph import Graph
import math


class BreadthFirstPaths:

    def __init__(self, g, s):
        """
        :param g: the graph
        :param s: the source vertex
        """
        self._g = g
        self._s = s
        self._marked = [False for _ in range(g.get_V())]
        self._dist_to = [math.inf for _ in range(g.get_V())]
        self._edge_to = [0 for _ in range(g.get_V())]
        self.validate_vertex(s)
        self.__bfs(g, s)

    def get_g(self):
        return self._g

    def get_s(self):
        return self._s

    def get_dist_to(self):
        return self._dist_to

    def get_edge_to(self):
        return self._edge_to

    def get_marked(self):
        return self._marked

    def __bfs(self, g, s):
        queue = deque()
        self.get_dist_to()[s] = 0
        self.get_marked()[s] = True
        queue.appendleft(s)
        print(queue)
        while queue:
            v = queue.pop()
            for w in g.adj_vertices(v):
                if not self.get_marked()[w.item]:
                    self.get_edge_to()[w.item] = v
                    self.get_dist_to()[w.item] = self.get_dist_to()[v] + 1
                    self.get_marked()[w.item] = True
                    queue.appendleft(w.item)

    def has_path_to(self, v):
        self.validate_vertex(v)
        return self.get_marked()[v]

    def distance_to(self, v):
        self.validate_vertex(v)
        return self.get_dist_to()[v]

    def path_to(self, v):
        self.validate_vertex(v)
        if not self.has_path_to(v):
            return None
        path = deque()  # stack of integers
        x = v
        while self.get_dist_to()[x] != 0:
            path.append(x)
            x = self.get_edge_to()[x]
        path.append(x)
        return list(path)

    def validate_vertex(self, v):
        n = len(self.get_marked())
        if v < 0 or v >= n:
            raise AttributeError(f'vertex {v} is not between 0 and {n-1}')

    def __repr__(self):
        return f'<{self.__class__.__name__}(\n' \
               f'g={self.get_g()}, \n' \
               f's={self.get_s()}, \n' \
               f'dist_to={self.get_dist_to()}\n' \
               f'edge_to={self.get_edge_to()}\n' \
               f'marked={self.get_marked()})>'


def main():
    s = 0
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    bfs = BreadthFirstPaths(g, s)
    print(bfs)
    for v in range(g.get_V()):
        if bfs.has_path_to(v):
            print(f'{s} to {v} ({bfs.distance_to(v)})')
            for x in reversed(bfs.path_to(v)):
                if x == s:
                    print(x, end="")
                else:
                    print(f' - {x}', end="")
            print()
        else:
            print(f'{s} to {v} (-): not connected.\n')


if __name__ == '__main__':
    main()














