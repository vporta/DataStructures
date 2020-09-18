"""
depth_first_directed_paths.py
Determine reachability in a digraph from a given vertex using
 *  depth-first search.
 *  Runs in O(E + V) time.
"""
from graphs.digraph import Digraph
from collections import deque


class DepthFirstDirectedPaths:

    def __init__(self, g, s):
        self._marked = [False for _ in range(g.get_V())]
        self._edge_to = [0 for _ in range(g.get_V())]
        self._s = s
        self.__validate_vertex(s)
        self.__dfs(g, s)

    def __dfs(self, g, v):
        self._marked[v] = True
        for w in g.adj_vertices(v):
            if not self._marked[w.item]:
                self._edge_to[w.item] = v
                self.__dfs(g, w.item)

    def has_path_to(self, v):
        self.__validate_vertex(v)
        return self._marked[v]

    def path_to(self, v):
        self.__validate_vertex(v)
        if not self.has_path_to(v):
            return None
        path = deque()
        x = v
        while x != self._s:
            path.append(x)
            x = self._edge_to[x]
        path.append(self._s)
        return path

    def get_marked(self):
        return self._marked

    def get_edge_to(self):
        return self._edge_to

    def get_s(self):
        return self._s

    def __validate_vertex(self, v):
        n = len(self.get_marked())
        if v < 0 or v >= n:
            raise AttributeError(f'vertex {v} is not between 0 and {n-1}')

    def __repr__(self):
        return f'<DepthFirstPaths(' \
               f's={self.get_s()}, ' \
               f'marked={self.get_marked()}, ' \
               f'edge_to = {self.get_edge_to()})>'


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
    dfs = DepthFirstDirectedPaths(graph, s)
    print(dfs)
    for v in range(graph.get_V()):
        if dfs.has_path_to(v):
            print(f'{s} to {v} ')
            for x in reversed(dfs.path_to(v)):
                if x == s:
                    print(f'{x} ', end="")
                else:
                    print(f'- {x}', end="")
            print()
        else:
            print(f'{s} to {v} not connected.')


if __name__ == '__main__':
    main()