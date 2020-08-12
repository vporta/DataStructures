"""
DirectedDFS.py
Determine single-source or multiple-source reachability in a digraph
 *  using depth first search.
 *  Runs in O(E + V) time.

The DirectedDFS class represents a data type for
 *  determining the vertices reachable from a given source vertex s
 *  (or set of source vertices) in a digraph. For versions that find the paths,
 *  see DepthFirstDirectedPaths and BreadthFirstDirectedPaths.
 *
 *  This implementation uses depth-first search.
 *  The constructor takes time proportional to V + E
 *  (in the worst case),
 *  where V is the number of vertices and E is the number of edges.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(V) extra space (not including the digraph).
"""
from Graphs.Bag import Bag
from Graphs.Digraph import Digraph


class DirectedDFS:
    _count = 0

    def __init__(self, g, s):
        """
        :param g: the graph
        :param s: the source vertex
        """
        # print(s)
        if isinstance(s, Bag):
            assert isinstance(s, Bag)
            self._marked = [False for _ in range(g.get_V())]
            self.g = g
            self.__validate_vertices(s)
            for v in s:
                if not self._marked[v.item]:
                    self.__dfs(g, v.item)
        else:
            self._marked = [False for _ in range(g.get_V())]
            self.g = g
            self.__validate_vertex(s)
            self.__dfs(g, s)

    def get_g(self):
        return self.g

    def __dfs(self, g, v):
        self._count += 1
        self._marked[v] = True
        for w in g.adj_vertices(v):
            # print('item', w.item, w)
            if not self._marked[w.item]:
                self.__dfs(g, w.item)

    def marked(self, v):
        self.__validate_vertex(v)
        return self._marked[v]

    def __validate_vertex(self, v):
        marked_vertices = len(self._marked)
        if v < 0 or v >= marked_vertices:
            raise AttributeError(f'vertex {v} is not between 0 and {marked_vertices - 1}')

    def __validate_vertices(self, vertices):
        if vertices is None:
            raise AttributeError('argument is None')
        for v in vertices:
            if v is None:
                raise ValueError('vertex is None')
            self.__validate_vertex(v.item)

    def count(self):
        return self._count

    def __repr__(self):
        return f'<{self.__class__.__name__}(g={self.get_g()}, count={self.count()})>'


def main():

    file_name = '../resources/tinyDG.txt'
    with open(file_name) as f:
        ints = list()
        for line in f.read().split('\n'):
            ints.append(line)
        vertices, edges = int(ints[0]), int(ints[1])

    graph = Digraph(vertices)
    # print(graph)
    inp = ints[2:]  # skip first 2 lines in tiny.DG.txt i.e. # of vertices and edges
    sources = Bag()
    sources.add(1)
    sources.add(5)
    sources.add(10)

    for i in range(edges):
        v, w = inp[i].split(' ')
        graph.add_edge(int(v), int(w))

    # print(graph)

    # s = 6
    # reachable from single source vertex, s
    # dfs = DirectedDFS(graph, int(s))
    # print(dfs)

    # reachable from many source vertices, sources
    dfs = DirectedDFS(graph, sources)
    # print(dfs)

    for v in range(graph.get_V()):
        if dfs.marked(v):
            print(f'{v} ')


if __name__ == '__main__':
    main()