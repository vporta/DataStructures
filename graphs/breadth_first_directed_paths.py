"""
breadth_first_directed_paths.py
Run breadth-first search on a digraph.
 *  Runs in O(E + V) time.
"""
import math
from graphs.digraph import Digraph
from queue import Queue, LifoQueue


class BreadthFirstDirectedPaths:

    def __init__(self, g, s=None, sources=None):
        """
        :param g: the digraph
        :param s: the source vertex
        """
        self._g = g
        self._s = s
        self._sources = sources
        self._marked = [False for _ in range(g.get_V())]
        self._dist_to = [math.inf for _ in range(g.get_V())]
        self._edge_to = [0 for _ in range(g.get_V())]
        self.__validate_vertex(s) if sources is None else self.__validate_vertices(sources)
        self.__bfs(g, s) if sources is None else self.__bfs_sources(g, sources)

    def get_g(self):
        return self._g

    def get_s(self):
        return self._s

    def get_sources(self):
        return self._sources

    def get_dist_to(self):
        return self._dist_to

    def get_edge_to(self):
        return self._edge_to

    def get_marked(self):
        return self._marked

    def __bfs(self, g, s):
        q = Queue()
        self._marked[s] = True
        self._dist_to[s] = 0
        q.put(s)
        while not q.empty():
            v = q.get()
            for w in g.adj_vertices(v):
                if not self._marked[w.item]:
                    self._edge_to[w.item] = v
                    self._dist_to[w.item] = self._dist_to[v] + 1
                    self._marked[w.item] = True
                    q.put(w.item)

    def __bfs_sources(self, g, sources):
        q = Queue()
        for s in sources:
            self._marked[s] = True
            self._dist_to[s] = 0
            q.put(s)
        while not q.empty():
            v = q.get()
            for w in g.adj_vertices(v):
                if not self._marked[w.item]:
                    self._edge_to[w.item] = v
                    self._dist_to[w.item] = self._dist_to[v] + 1
                    self._marked[w.item] = True
                    q.put(w.item)

    def has_path_to(self, v):
        self.__validate_vertex(v)
        return self.get_marked()[v]

    def path_to(self, v):
        self.__validate_vertex(v)
        if not self.has_path_to(v):
            return None
        path = LifoQueue()  # stack
        x = v
        while self._dist_to[x] != 0:
            path.put(x)
            x = self._edge_to[x]
        path.put(x)
        return path

    def dist_to(self, v):
        self.__validate_vertex(v)
        return self.get_dist_to()[v]

    def __validate_vertex(self, v):
        n = len(self.get_marked())
        if v < 0 or v >= n:
            raise AttributeError(f'vertex {v} is not between 0 and {n-1}')

    def __validate_vertices(self, vertices):
        if vertices is None:
            raise AttributeError('argument is None')
        for v in vertices:
            if v is None:
                raise AttributeError('vertex is None')
            self.__validate_vertex(v)

    def __repr__(self):
        return f'<{self.__class__.__name__}(\n' \
               f'g={self.get_g()}, \n' \
               f's={self.get_s()}, \n' \
               f'sources={self.get_sources()}\n' \
               f'dist_to={self.get_dist_to()}\n' \
               f'edge_to={self.get_edge_to()}\n' \
               f'marked={self.get_marked()})>'


def main():
    file_name = '../resources/digraph1.txt'
    with open(file_name) as f:
        ints = list()
        for line in f.read().split('\n'):
            ints.append(line)
        vertices, edges = int(ints[0]), int(ints[1])

    graph = Digraph(vertices)
    inp = ints[2:]  # skip first 2 lines in tiny.DG.txt i.e. # of vertices and edges

    for i in range(edges):
        v, w = inp[i].split(' ')
        graph.add_edge(int(v), int(w))

    s = 3
    sources = [3, 4, 5]
    # bfs = BreadthFirstDirectedPaths(graph, s)
    bfs = BreadthFirstDirectedPaths(graph, sources=sources)
    print(bfs)
    for v in range(graph.get_V()):
        if bfs.has_path_to(v):
            print(f'{sources} to {v} ({bfs.dist_to(v)})')
            path = bfs.path_to(v)
            while not path.empty():
                x = path.get()
                if x == s or x in sources:
                    print(f'{x}', end="")
                else:
                    print(f'->{x}', end="")
            print()
        else:
            print(f'{s} to {v} (-): not connected.\n')


if __name__ == '__main__':
    main()