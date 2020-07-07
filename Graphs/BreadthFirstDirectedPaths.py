"""
BreadthFirstDirectedPaths.py
Run breadth-first search on a digraph.
 *  Runs in O(E + V) time.
"""
import math
from collections import deque
from Graphs.Digraph import Digraph


class BreadthFirstDirectedPaths:

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
        self.__validate_vertex(s)
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
        q = deque()
        self._marked[s] = True
        self._dist_to[s] = 0
        q.appendleft(s)
        while q:
            v = q.pop()
            for w in g.adj_vertices(v):
                if not self._marked[w.item]:
                    self._edge_to[w.item] = v
                    self._dist_to[w.item] = self._dist_to[v] + 1
                    self._marked[w.item] = True
                    q.appendleft(w.item)

    def has_path_to(self, v):
        self.__validate_vertex(v)
        return self.get_marked()[v]

    def path_to(self, v):
        self.__validate_vertex(v)
        if not self.has_path_to(v):
            return None
        path = deque()  # stack
        x = v
        while self._dist_to[x] != 0:
            path.append(x)
            x = self._edge_to[x]
        path.append(x)
        return list(path)

    def dist_to(self, v):
        self.__validate_vertex(v)
        return self.get_dist_to()[v]

    def __validate_vertex(self, v):
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
    file_name = '../resources/tinyDG.txt'
    with open(file_name) as f:
        ints = list()
        for line in f.read().split('\n'):
            ints.append(line)
        vertices, edges = int(ints[0]), int(ints[1])

    graph = Digraph(vertices)
    print(graph)
    inp = ints[2:]  # skip first 2 lines in tiny.DG.txt i.e. # of vertices and edges

    for i in range(edges):
        v, w = inp[i].split(' ')
        graph.add_edge(int(v), int(w))
    print(graph)
    s = 3
    bfs = BreadthFirstDirectedPaths(graph, s)
    print(bfs)
    for v in range(graph.get_V()):
        if bfs.has_path_to(v):
            print(f'{s} to {v} ({bfs.dist_to(v)})')
            for x in bfs.path_to(v):
                if x == s:
                    print(f' {x} ', end="")
                else:
                    print(f' -> {x}', end="")
            print()
        else:
            print(f'{s} to {v} (-): not connected.\n')


if __name__ == '__main__':
    main()